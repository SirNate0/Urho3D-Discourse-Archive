slapin | 2017-05-17 23:58:23 UTC | #1

Looking at the following Valgrind dump I see that my Node is gone inside AngelScript.
In my code I use `SharedPtr<Node>` to store that node in hope that it will keep reference, but it looks
like I don't understand the concept:

    ==18789== Invalid read of size 8
    ==18789==    at 0x8B9AD2: Urho3D::UniquePtr<Urho3D::NodeImpl>::operator->() const (Ptr.h:571)
    ==18789==    by 0x8CCCA3: Urho3D::Node::GetName() const (Node.h:341)
    ==18789==    by 0x8C9645: BTBlackboard::HandlePhysicsPreStep(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) (BehaviorTree.cpp:83)
    ==18789==    by 0x8CE123: Urho3D::EventHandlerImpl<BTBlackboard>::Invoke(Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) (Object.h:307)
    ==18789==    by 0xB731A3: Urho3D::Object::OnEvent(Urho3D::Object*, Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) (Object.cpp:113)
    ==18789==    by 0xB73BE1: Urho3D::Object::SendEvent(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) (Object.cpp:325)
    ==18789==    by 0xC0A8EC: Urho3D::PhysicsWorld::PreStep(float) (PhysicsWorld.cpp:807)
    ==18789==    by 0xC06355: Urho3D::InternalPreTickCallback(btDynamicsWorld*, float) (PhysicsWorld.cpp:71)
    ==18789==    by 0xDB6510: btDiscreteDynamicsWorld::internalSingleStepSimulation(float) (btDiscreteDynamicsWorld.cpp:478)
    ==18789==    by 0xDB647D: btDiscreteDynamicsWorld::stepSimulation(float, int, float) (btDiscreteDynamicsWorld.cpp:455)
    ==18789==    by 0xC07A60: Urho3D::PhysicsWorld::Update(float) (PhysicsWorld.cpp:256)
    ==18789==    by 0xC0A85A: Urho3D::PhysicsWorld::HandleSceneSubsystemUpdate(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) (PhysicsWorld.cpp:796)
    ==18789==  Address 0x1634cb58 is 312 bytes inside a block of size 352 free'd
    ==18789==    at 0x4C2D360: operator delete(void*) (vg_replace_malloc.c:507)
    ==18789==    by 0x96073C: Urho3D::Node::~Node() (Node.cpp:75)
    ==18789==    by 0xB9AB6D: Urho3D::RefCounted::ReleaseRef() (RefCounted.cpp:65)
    ==18789==    by 0xF0DACD: asCScriptEngine::CallObjectMethod(void*, asSSystemFunctionInterface*, asCScriptFunction*) const (as_scriptengine.cpp:4038)
    ==18789==    by 0xF0D9AA: asCScriptEngine::CallObjectMethod(void*, int) const (as_scriptengine.cpp:4010)
    ==18789==    by 0x8D9BF1: asCContext::ExecuteNext() (as_context.cpp:2771)
    ==18789==    by 0x8D66BC: asCContext::Execute() (as_context.cpp:1297)
    ==18789==    by 0x8BF99C: ScriptBehavior::update(BTBlackboard*) (ScriptBehavior.cpp:111)
    ==18789==    by 0x8CAF72: BTBaseNode::Activate(BTBlackboard*) (BehaviorTree.cpp:167)
    ==18789==    by 0x8CB05F: BTSequenceNode::update(BTBlackboard*) (BehaviorTree.cpp:188)
    ==18789==    by 0x8CAF72: BTBaseNode::Activate(BTBlackboard*) (BehaviorTree.cpp:167)
    ==18789==    by 0x8CB221: BTSelectorNode::update(BTBlackboard*) (BehaviorTree.cpp:242)

How can I prevent of Node being free'd or could I at least get notified about this to prevent data corruption?
Or is there some completely different way to handle such things?

-------------------------

cadaver | 2017-05-18 07:28:24 UTC | #2

SharedPtr is a strong ref, so it should keep the object alive. If your object dies even while a SharedPtr should still be pointing to it, I'd suspect your script binding doing too many Release()'s somewhere. AngelScript handles should be equivalent to SharedPtr in their behavior.

The idiom used in Urho event handlers which expect potential self-destruction is to use a self-pointing WeakPtr and check whether that expires.

-------------------------

Sinoid | 2017-05-19 02:02:25 UTC | #3

If I'm reading that log correctly it looks like you constructed a UniquePtr with a RefCounted object through the "by pointer" constructor. 

If that's the case - UniquePtr doesn't care about anything else and will let you hang yourself (it's for local stuff you own) - you probably want to be either keeping a WeakPtr that you'll check before using or a solid SharedPtr.

-------------------------

slapin | 2017-05-19 20:17:41 UTC | #4

Well, the problem looks like I still need RefCounted for all objects if I want to use SharedPtr/WeakPtr.

Now I try to use WeakRef<Node> target; Then I select target node and set to "target" pointer.
then after some time I check the pointer and it looks fine. When I access it I get crash.
Valgrind shows the node was freed. So there is something fundamental which I don't get.
1. If node is freed, then RefCounted values are freed too and might and will contain junk.
If I access WeakPtr after node was freed I can't trust RefCounted values so I can't know if it is safe to
access the pointer. So why bother? WeakPtr doesn't have any useful purpose.
2. Same for SharedPtr - if the structure is freed, it is unsafe to use SharedPtr.

So all possible solution I see is to disable RefCounting completely.

Please tell me I'm wrong and where I'm wrong.
I'm debugging the crash for so long it hurts. With C it would take no longer than hour.
My hate to C++ is here again, I thought it is possible to do anything useful with C++ but i was wrong.
I will probably drop all my class-based code and go for small C
routines for hot stuff, as I don't see any progress.

-------------------------

Eugene | 2017-05-19 21:30:03 UTC | #5

[quote="slapin, post:4, topic:3130"]
If I access WeakPtr after node was freed I can't trust RefCounted values so I can't know if it is safe to
access the pointer. So why bother? WeakPtr doesn't have any useful purpose.
[/quote]

WeakPtr doesn't get bad when object is destroyed, it is the only safe way to hold pointer that you don't own.
Looks like refcounting is broken somewhere.
You should probably share some code because refcounting itself doesn't have such problems.

-------------------------

slapin | 2017-05-19 23:00:05 UTC | #6

If the object was freed and overwritten, neither WeakPtr nor SharedPtr can be safely accessed.

-------------------------

Eugene | 2017-05-19 23:10:47 UTC | #7

Accessed via arrow-op - no, it can't. But WeakPtr remains valid. Null, but valid.
It is, actually, safe. You can't get dangling pointers if use only SharedPtr and WeakPtr-s.

-------------------------

slapin | 2017-05-20 12:41:44 UTC | #8

I wonder why I never get NULL WeakPtr if Node is freed and overwritten...

-------------------------

slapin | 2017-05-20 15:00:01 UTC | #9

I know I was right!

1. If Node is deleted by ReleaseRef, SharedPtr/WeakPtr are not safe.
This can happen if we have more refs than we should. Like we get pointer from AS, process it and give back to AS, then the object gets destroyed, but the pointer is still in scene hierarchy, which leads to crashes and NULL pointer errors (later one is fine).

2. The question is why this happens. If I AddRef pointer I got from AS, then I get one kind of crash (deletion by AS), if I don't I get another crash (memory corruption). What is proper procedure for AS API binding to handle pointers
received from AS? Any docs? The code works fine without AS involved but I need AS binding there.

-------------------------

slapin | 2017-05-20 18:05:09 UTC | #10

Well, It looks like I'm closer.

In AS I do the following:
`Array<Node@>@ data = FindSomeNodes();`
where FindSomeNodes() is another AS function which looks for nodes complying to some criteria.

Then I parse this array and find one element, which I set to C++ code:
`btb.target = data[closest_index];`

which leads to calling set_target() on my object, which just sets WeakRef<Node> target;

Running this seems to drop reference count on node.
After this I do `data.Clear()` in AS which leads to deletion of all array elements
and runs ReleaseRef on all array elements. This particular node was assigned to WeakRef,
and its refcount was decreased, which leads to node deletion.

Now I wonder how to prevent release of reference on on object in this situation?
if btb was AS object, that would not happen, but btb is C++ object, and the magic happens.
What can I do?
I already worked this around by using node ID, but I wonder how to prevent this from happening?
Thanks!

-------------------------

Eugene | 2017-05-20 21:04:11 UTC | #11

[quote="slapin, post:10, topic:3130"]
After this I do data.Clear() in AS which leads to deletion of all array elements
and runs ReleaseRef on all array elements. This particular node was assigned to WeakRef,
and its refcount was decreased, which leads to node deletion.
[/quote]

That's strange. Where does your node initially live?
If Scene owns these nodes, they can't be destroyed by clearing some array.

-------------------------

slapin | 2017-05-22 13:29:58 UTC | #12

They can, as reference count is reduced to 0.

-------------------------

Eugene | 2017-05-22 14:39:23 UTC | #13

How can ref counter get zero if Node is owned by the Scene?

-------------------------

slapin | 2017-05-22 14:56:37 UTC | #14

Easily - something calls ReleaseRef on it.
For example this happens when prividing pointer to it to C++ property which is implemented as AS set/get.
If get doesn't AddRef it, it will be ReleaseRef'ed twice, which will lead to freeing (ReleaseRef calls delete if refcount goes to 0). This way SharedPtr/WeakPtr will hold invalid reference.
So SharedPtr work bad as holders unless you do all operations through them.
Or basically don't forget to AddRef everything you give to AS, which will eleminate a problem (which is really hard to debug). But the rule about using WeakPtr/SharedPtr on freed object is unsafe still persists.
If you used object through WeakPtr and found it invalidated through that ptr, that is fine. Otherwise, don't bother.
The same goes for SharedPtr - if you can't control AddRef/ReleaseRef, you're in trouble.
If you don't use AS, you will be fine using SharedPtrs asn you will NEVER use AddRef/ReleaseRef directly
unless you do something weird. But if you use AS (and probably Lua, not sure) - BEWARE.

However if you use only C++ you probably don't need these pointer magic - just hold them in `Vector<SharedPtr<Foo>>` and use raw pointers after this. But if you're doing something complicated like object streaming (whatever that is) you might be interested in some object management. I think it is easier to hold everything "scenic" in scene, and components in nodes. Custom things might be static. Or kept these in vector. I'd recommend custom things which won't change on the run and do not inherit RefCounted to keep in standard C++ management.
That will at least keep them out of scope of possible debugging nightmare.

-------------------------

Eugene | 2017-05-22 16:00:05 UTC | #15

[quote="slapin, post:14, topic:3130"]
Easily - something calls ReleaseRef on it.
[/quote]

But it means that this _something_ (e.g. script binding) is written badly!
E.g. I've already found (and fixed) one problem in AS container with memory leaks caused by missing ReleaseRef.

It is not the problem of SharedPtr, it is misusing of refcounter mechanism.

Do you have some small code? I'd like to debug it if there is a chance that Urho has broken bindings.

If you write your own bindings, check counting there, especially `@+` and `@`.

-------------------------

cadaver | 2017-05-22 16:38:03 UTC | #16

Urho's inbuilt bindings use auto handles (@+) for the most part, that means no AddRef() / ReleaseRef() in bindings C++ code. In some cases bindings code first constructs an object into a SharedPtr, which will go out of scope; in this case we do manual AddRef() and don't use auto handle for the return parameter.

-------------------------

slapin | 2017-05-22 16:48:00 UTC | #17

My problem was that object was created in AS and handled to C++ get/set,
which meant immediate destruction of object if not using AddRef. (I used Node).
WeakPtr did not helped in this situation, but WeakPtr + AddRef did the trick.

-------------------------

