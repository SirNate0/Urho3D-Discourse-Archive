slapin | 2017-05-15 00:17:49 UTC | #1

AngelScript tries to delete my RefCounted object.

I register like this:

    template<class A, class B>
    static B *refCast(A *a)
    {
            if (!a)
                    return NULL;
            B *b = dynamic_cast<B *>(a);
            return b;
    }


    template<class M>
    static M *ConstructSimple()
    {
            return new M();
    }

    template<class T>
    void RegisterBTNode(asIScriptEngine* engine, String name)
    {
            RegisterRefCounted<T>(engine, name.CString());
            engine->RegisterObjectBehaviour(name.CString(), asBEHAVE_FACTORY, (name + "@+ f()").CString(), asFUNCTION(ConstructSimple<T>), asCALL_CDECL);
            engine->RegisterObjectMethod(name.CString(), "BehaviorNode@+ opImplCast()", asFUNCTION((refCast<T, BTBaseNode>)), asCALL_CDECL_OBJLAST);
            engine->RegisterObjectMethod(name.CString(), "BehaviorNode@+ opCast()", asFUNCTION((refCast<T, BTBaseNode>)), asCALL_CDECL_OBJLAST);
            engine->RegisterObjectMethod(name.CString(), "BehaviorStatus Activate(BTBlackboard@+)", asMETHOD(T, Activate), asCALL_THISCALL);
    }

    template<class T>
    void RegisterBTCompositeNode(asIScriptEngine* engine, String name)
    {
            RegisterBTNode<T>(engine, name);
            engine->RegisterObjectMethod(name.CString(), "void AddChild(BehaviorNode@)", asMETHOD(T, add_child), asCALL_THISCALL);
            engine->RegisterObjectMethod(name.CString(), "CompositeNode@+ opImplCast()", asFUNCTION((refCast<T, BTCompositeNode>)), asCALL_CDECL_OBJLAST);
            engine->RegisterObjectMethod(name.CString(), "CompositeNode@+ opCast()", asFUNCTION((refCast<T, BTCompositeNode>)), asCALL_CDECL_OBJLAST);
    }

    void RegisterScriptBehavior(Context *context)
    {
    ...
            /* CompositeNode */
            RegisterBTNode<BTCompositeNode>(engine, "CompositeNode");
    ...
    }

Any ideas?

-------------------------

slapin | 2017-05-15 00:20:57 UTC | #2

@cadaver could you please look and tell me how can I use RefCounted with AngelScript objects?
As pointer is out of scope it immediately calls object destructor, which produces assert error:

RefCounted.cpp:42: virtual Urho3D::RefCounted::~RefCounted(): Assertion `refCount_->refs_ == 0' failed.

So while object is held it is still destroyed. I wonder what I miss here.

-------------------------

slapin | 2017-05-15 00:25:13 UTC | #3

In AngelScript I just put the pointer into array, and leave the scope. The array is object property,
so it should remain. But AS is out for blood on my poor little RefCounted object and calls its destructor anyway...
I wonder how to fight it...

-------------------------

slapin | 2017-05-15 00:27:00 UTC | #4

Also, if objects are not put into array, nothing bad happens, they are just destroyed.
If I add them to array which remains, assertion happens when scope is left.
Otherwise objects work perfectly well.

-------------------------

slapin | 2017-05-15 01:20:11 UTC | #5

What happens to thhe object:

    [Mon May 15 04:08:51 2017] INFO: AddRef: 0b06a6c0
    [Mon May 15 04:08:51 2017] INFO: AddRef: 0b06a6c0
    [Mon May 15 04:08:51 2017] INFO: ReleaseRef: count = 2 0b06a6c0
    done calling constructor
    [Mon May 15 04:08:51 2017] INFO: Deleting: 0b06a6c0

The last line is call of destructor. (the hex number is pointer value/object address)
The actual deletion happens through AS engine, not through ReleaseRef:

        `RefCounted.cpp:45: virtual Urho3D::RefCounted::~RefCounted(): Assertion `refCount_->refs_ == 0' failed.`

        Program received signal SIGABRT, Aborted.
        0x00007ffff69161c8 in raise () from /lib/x86_64-linux-gnu/libc.so.6
        (gdb) bt
        #0  0x00007ffff69161c8 in raise () from /lib/x86_64-linux-gnu/libc.so.6
        #1  0x00007ffff691764a in abort () from /lib/x86_64-linux-gnu/libc.so.6
        #2  0x00007ffff690f107 in __assert_fail_base () from /lib/x86_64-linux-gnu/libc.so.6
        #3  0x00007ffff690f1b2 in __assert_fail () from /lib/x86_64-linux-gnu/libc.so.6
        #4  0x0000000000b9434f in Urho3D::RefCounted::~RefCounted (this=0x99abf40, __in_chrg=<optimized out>) at /home/slapin/Urho3D/Source/Urho3D/Container/RefCounted.cpp:45
        #5  0x00000000008bdeea in BTBaseNode::~BTBaseNode (this=0x99abf40, __in_chrg=<optimized out>) at /home/slapin/dungeon/rework/BehaviorTree.h:22
        #6  0x00000000008c24d0 in BTCompositeNode::~BTCompositeNode (this=0x99abf40, __in_chrg=<optimized out>) at /home/slapin/dungeon/rework/BehaviorTree.h:36
        #7  0x00000000008c79de in BTSequenceNode::~BTSequenceNode (this=0x99abf40, __in_chrg=<optimized out>) at /home/slapin/dungeon/rework/BehaviorTree.h:47
        #8  0x0000000000f073c2 in asCScriptEngine::CallObjectMethod (this=0x239de30, obj=0x99abf40, i=0x23a2580, s=0x23a2600) at /home/slapin/Urho3D/Source/ThirdParty/AngelScript/source/as_scriptengine.cpp:4038
        #9  0x0000000000f0729f in asCScriptEngine::CallObjectMethod (this=0x239de30, obj=0x99abf40, func=2) at /home/slapin/Urho3D/Source/ThirdParty/AngelScript/source/as_scriptengine.cpp:4010
        #10 0x00000000008d7d38 in asCContext::ExecuteNext (this=0x30a25d0) at /home/slapin/Urho3D/Source/ThirdParty/AngelScript/source/as_context.cpp:4106
        #11 0x00000000008d0c77 in asCContext::Execute (this=0x30a25d0) at /home/slapin/Urho3D/Source/ThirdParty/AngelScript/source/as_context.cpp:1297
        #12 0x00000000009ad572 in Urho3D::ScriptFile::Execute (this=0x2f04070, function=0x30a2e60, parameters=..., unprepare=true) at /home/slapin/Urho3D/Source/Urho3D/AngelScript/ScriptFile.cpp:324
        #13 0x00000000009b038a in Urho3D::ScriptEventInvoker::HandleScriptEvent (this=0x30d6790, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/AngelScript/ScriptFile.cpp:956
        #14 0x00000000009b4394 in Urho3D::EventHandlerImpl<Urho3D::ScriptEventInvoker>::Invoke (this=0x9009110, eventData=...) at /home/slapin/Urho3D/Source/Urho3D/AngelScript/../AngelScript/../Core/Object.h:307
        #15 0x0000000000b6caeb in Urho3D::Object::OnEvent (this=0x30d6790, sender=0x1cbae10, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:121
        #16 0x0000000000b6d680 in Urho3D::Object::SendEvent (this=0x1cbae10, eventType=..., eventData=...) at /home/slapin/Urho3D/Source/Urho3D/Core/Object.cpp:355
        #17 0x0000000000b8bfea in Urho3D::Engine::Update (this=0x1cbae10) at /home/slapin/Urho3D/Source/Urho3D/Engine/Engine.cpp:695
        #18 0x0000000000b8b92a in Urho3D::Engine::RunFrame (this=0x1cbae10) at /home/slapin/Urho3D/Source/Urho3D/Engine/Engine.cpp:519
        #19 0x0000000000b884ce in Urho3D::Application::Run (this=0x1cbaca0) at /home/slapin/Urho3D/Source/Urho3D/Engine/Application.cpp:86
        #20 0x00000000008ca359 in RunApplication () at /home/slapin/dungeon/rework/Urho3DPlayer.cpp:46
        #21 0x00000000008ca400 in main (argc=1, argv=0x7fffffffe248) at /home/slapin/dungeon/rework/Urho3DPlayer.cpp:46

So this is kind of reaction on scope loss. Is there some way to prevent AS from deleting objects
and just use reference counting behaviors?

-------------------------

S.L.C | 2017-05-15 06:31:03 UTC | #6

Have you considered the following behavior:


    struct RefCounted
    {
        void GrabRef()
        {
            ++m_RefCount;
        }
        void DropRef()
        {
            if (--m_RefCount == 0)
            {
                puts("Counter Reached 0...");
                delete this;
            }
        }
    protected:

        RefCounted()
            : m_RefCount(1)
        {
            //...
        }
        virtual ~RefCounted()
        {
            puts("Deleting Object...");
        }
    private:

        int m_RefCount;
    };

    struct Foo : public RefCounted
    {
        Foo()
            : RefCounted()
        {

        }
        virtual ~Foo()
        {
            puts("Deleting Foo...");
        }
    };

    struct Bar : public RefCounted
    {
        Bar()
            : RefCounted()
        {

        }
        virtual ~Bar()
        {
            puts("Deleting Bar...");
        }
    };

    struct Baz : public Foo, public Bar
    {
        Baz()
            : Foo(), Bar()
        {

        }
        virtual ~Baz()
        {
            puts("Deleting Baz...");
        }
    };

Example:

    Baz * baz = new Baz();

    Foo * foo = baz;
    foo->GrabRef();
    foo->GrabRef();
    Bar * bar = baz;
    bar->DropRef();

Output:

    Counter Reached 0...
    Deleting Baz...
    Deleting Bar...
    Deleting Object...
    Deleting Foo...
    Deleting Object...

Such that you actually have several reference counters for the same instance. And depending through which base you modify the counter, you may not have a guarantee that you're working with the same counter.

-------------------------

slapin | 2017-05-15 12:26:16 UTC | #7

In such case the pointers would be different, as these are different objects.
In this case I see this happening on the same object. This looks like for some reason
AS decided to delete the object, while it should just drop references. This means I miss something in API
setup. This is also indicated by assert - it would not happen if reference was dropped, it is direct deletion of object.

-------------------------

slapin | 2017-05-15 12:27:13 UTC | #8

I know it is possible to do as this works on Urho objects, I just trying to find what I miss there.

-------------------------

weitjong | 2017-05-15 14:12:15 UTC | #9

You may want to read this documentation page from AS.

http://www.angelcode.com/angelscript/sdk/docs/manual/doc_obj_handle.html

-------------------------

slapin | 2017-05-15 18:34:38 UTC | #10

@weitjong I have read all the docs. as I mentioned I register via urho RefCounted template, which registers behaviors intended to add/release reference automatically. What I don't understand is why destructor is called directly instead of ReleaseRef().
Please see the original post.
Also in arificial example I could not reproduce this, which looks that there are some additional requirements which I currently investigate.

-------------------------

slapin | 2017-05-15 20:31:20 UTC | #11

Well, I solved this by using + in all function arguments taking objects, and not directly using pointers.
But it looks like I got dictionary corruption somehow, or something.

AngelScript/source/as_atomic.cpp:68: asDWORD asCAtomic::atomicInc(): Assertion `value < 1000000' failed.

This is not work with custom objects, it is just acquiring function pointer:
`funcdef BehaviorNode@ create_bvh_node(VariantMap props);
create_bvh_node@ func = cast<create_bvh_node>(bhvnodes[nodetype]);`

bhvnode is Dictionary in style of

    Dictionary bhvnodes = {
    // group composites (Composites)
    // ------------------------------
            // sequence (Sequence)
            {"bhv_sequence", Create_sequence},

            // memsequence (MemSequence)
            {"bhv_memsequence", Create_memsequence},

            // selection (Selection)
            {"bhv_selection", Create_selection},
    ...

and Create.. functions are factories and look like

    BehaviorNode@ Create_sequence(VariantMap props)
    {
            return SequenceNode();
    }
    BehaviorNode@ Create_memsequence(VariantMap props)
    {
            return MemSequenceNode();
    }

This looks like not really directly related to Dictionary, but I wonder how come some Dictionary entry got corrupted...
So I have fun debugging again...

-------------------------

slapin | 2017-05-15 20:44:01 UTC | #12

The strange thing is that If I do not run constructors at all, just pass through dictionary, it is still asserts.
I wonder why...

-------------------------

slapin | 2017-05-15 22:09:18 UTC | #13

Something is definitely gets corrupted, but where...

-------------------------

