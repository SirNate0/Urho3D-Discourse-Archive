sabotage3d | 2017-01-02 01:03:50 UTC | #1

Often I am unsure when to use SharedPtr or WeakPtr with Urho3d . Can someone show me some more Urho3D specific examples when to use one or the other ?
Thanks in advance :slight_smile:

-------------------------

cadaver | 2017-01-02 01:03:50 UTC | #2

Use SharedPtr when you want to own an object and keep it alive.

Use WeakPtr when you want to safely access an object (ie. you will know when it has been destroyed) but you don't want to own it. This requires there to be a SharedPtr keeping the object alive somewhere else. Typically, Nodes are kept alive by their scene, UI elements by the UI hierarchy, and Resources by the resource cache.

Some game-related examples: 
- If you have a tank scene node which has a rotating turret as a child scene node, and the tank will never exist without its turret, the tank's logic code could hold a SharedPtr to the turret scene node.
- If the tank is AI controlled it could track its latest target scene node. In this case there's no ownership, and the target might get destroyed by outside factors at any time, so the target should be pointed to by a WeakPtr.

Note that you can easily create circular references with SharedPtr's, so use them carefully and prefer WeakPtr when ownership is not intended.

-------------------------

sabotage3d | 2017-01-02 01:03:50 UTC | #3

Thanks cadaver,
Just to clarify, if understand correctly. If I have weapons, bullets, healing potions or any other objects that will be deleted and they are not owned by any other nodes in the scene, I should use WeakPtr. As there is no ownership. 
If I have nodes or objects owned by a parent in the scene and they are intended to be alive as long as the parent is alive, I should keep them SharedPtr.

-------------------------

devrich | 2017-01-02 01:03:51 UTC | #4

[quote="cadaver"]Some game-related examples: 
- If you have a tank scene node which has a rotating turret as a child scene node, and the tank will never exist without its turret, the tank's logic code could hold a SharedPtr to the turret scene node.
- If the tank is AI controlled it could track its latest target scene node. In this case there's no ownership, and the target might get destroyed by outside factors at any time, so the target should be pointed to by a WeakPtr.[/quote]

( This is going to sound like a question i should already know but since i'm more familiar with scripting than C++ please bare with me here )

I remember from my personal studies of C++11/14 that weakptr is a pointer to an object without owning it and that sharedptrs increment with a iterator ( iterators confuse me, at the moment ) as other objects wish to use the sharedptr....

For me to understand the proper way to use this:
1: I have a tank scene node which has a rotating turret as a child scene node
2: I create a weakptr to the child scene node to access it and make it rotate or fire
3: At some point; the tank gets destroyed by a bomb from a plane
4: ?? How to delete the weakptr, and the sharedptr, and also how to delete the tank scene node but without causing any c++ related issues with all these deletes?

( i assume i'm overanalyzing this but i've decided to go forward building my project using C++ for porting through emscripten )

-------------------------

cadaver | 2017-01-02 01:03:51 UTC | #5

Remember that the scene always keeps its own node hierarchy authoritatively alive by nodes having a Vector<SharedPtr<Node> > of their child nodes. 

When you want something gone from the scene, call Remove() on the node, which will detach it from parent, or alternatively RemoveChild() from the parent node. If there are no SharedPtr's pointing to it elsewhere, the node is going to be destroyed, and its child nodes will be destroyed too. If SharedPtr's point to the removed node outside the scene, the node will continue to live on, but is detached from the scene. Call Reset() on a SharedPtr or WeakPtr to stop it pointing to an object; that will also happen automatically when the ptr goes out of scope or is destroyed. You should not have any issues related to deletion as long as you don't attempt to manually delete an object pointed to by SharedPtr. I hope this answers your questions.

-------------------------

TikariSakari | 2017-01-02 01:04:54 UTC | #6

I just had something not so well thought out, like this:

[code]
class Main
{
   Urho3D::SharedPtr<ClassA> classA_;
}
Class ClassA 
{
   Urho3D::SharedPtr<ClassB> other_;
}

Class ClassB
{
   Urho3D::SharedPtr<ClassA> other_;
}
[/code]
They both refer to each other, such as Main::classA_->other_->other_.Get() == Main::classA_.Get()

According to Visual Studio at least when compiling to debug-mode this caused a memory leak when exiting. I solved this by changing ClassBs other-member to weak pointer, since the ClassBs cannot live without classA object.

-------------------------

GoogleBot42 | 2017-01-02 01:04:54 UTC | #7

Hmm it seems that Visual studio detected that an instance of each classA and classB referenced each other and kept each other alive.  But IDK.  :stuck_out_tongue:

-------------------------

thebluefish | 2017-01-02 01:04:54 UTC | #8

Visual Studio's memory leak detector basically checks to see if there is anything created with 'new' that wasn't deleted by the time the application exits.

In this case, a SharedPtr from each class referring to the other would keep both classes alive. Even if all other SharedPtr objects were removed, either ClassA or ClassB would need to delete its SharedPtr reference to the other to reduce the reference count. TikariSakari's fix, by replacing one with a WeakPtr, means that one of these classes will reach a reference count of 0, deleting itself, deleting its SharedPtr, which causes the other class's reference count to hit 0, deleting it.

-------------------------

GoogleBot42 | 2017-01-02 01:04:55 UTC | #9

[quote="thebluefish"]Visual Studio's memory leak detector basically checks to see if there is anything created with 'new' that wasn't deleted by the time the application exits.

In this case, a SharedPtr from each class referring to the other would keep both classes alive. Even if all other SharedPtr objects were removed, either ClassA or ClassB would need to delete its SharedPtr reference to the other to reduce the reference count. TikariSakari's fix, by replacing one with a WeakPtr, means that one of these classes will reach a reference count of 0, deleting itself, deleting its SharedPtr, which causes the other class's reference count to hit 0, deleting it.[/quote]

That is pretty much what I said I think...  :confused:

-------------------------

thebluefish | 2017-01-02 01:04:55 UTC | #10

I was more-so specifying that this is a C++ standard thing, not "Visual Studio detecting...", with a bit more detail.

-------------------------

TikariSakari | 2017-01-02 01:04:56 UTC | #11

[quote="thebluefish"]I was more-so specifying that this is a C++ standard thing, not "Visual Studio detecting...", with a bit more detail.[/quote]

I was myself wondering if I would have used standard c++ sharedpointers, would they actually behave the same way? I can understand that there is a problem when both of the objects are waiting for the other object to release the pointer, but I was wondering if the standard c++ shared pointers work the same way? Also I guess this is just bad coding to have both objects refering each other, and if I would figure out how to effectively use the urhos event-system, I could probably remove the weakpointter and just use custom event to inform the parent object.

Edit: Seems that this is really something that even the standard c++11 smart pointers have troubles with.

-------------------------

GoogleBot42 | 2017-01-02 01:04:56 UTC | #12

[quote="thebluefish"]I was more-so specifying that this is a C++ standard thing, not "Visual Studio detecting...", with a bit more detail.[/quote]

Ahh ok gotcha :wink:

[quote="TikariSakari"]Edit: Seems that this is really something that even the standard c++11 smart pointers have troubles with.[/quote]

Yeah this is just one of the disadvantages of reference counting.  If two objects reference each other they exist "forever".  Lua has an advanced garbage collection system where, even if two objects reference each other the objects will still be deleted.  But checking for this kind of thing is slow and best avoided if possible. :slight_smile:

-------------------------

