1vanK | 2017-01-02 01:09:17 UTC | #1

I do not understand

[code]void AnimatingScene::SetupViewport()
{
    Renderer* renderer = GetSubsystem<Renderer>();

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);
}
[/code]
[b]SharedPtr<Viewport> viewport[/b] is local variable
[b]SharedPtr<Viewport> viewport[/b] convert to raw pointer [b]Viewport*[/b] (reference count not increased) and used in SetViewport()
[b]SharedPtr<Viewport> viewport[/b] deleted as local variable (reference count == 0)
Why [b]Viewport*[/b] is not destroyed?

-------------------------

jmiller | 2017-01-02 01:09:17 UTC | #2

Renderer::SetViewport() also stores the pointer in Renderer's Vector<SharedPtr<Viewport> > viewports_

-------------------------

1vanK | 2017-01-02 01:09:18 UTC | #3

[quote="carnalis"]Renderer::SetViewport() also stores the pointer in Renderer's Vector<SharedPtr<Viewport> > viewports_[/quote]

It creates a new SharedPtr from raw pointer

-------------------------

1vanK | 2017-01-02 01:09:18 UTC | #4

Oh, I understand my mistake. Ref coundet stored in object, but not in SharedPtr

-------------------------

greenhouse | 2017-01-02 01:09:18 UTC | #5

I thought the same...Then what is the functionality behind SharedPtr? To update Ref Counted state of a pointed to object?

-------------------------

cadaver | 2017-01-02 01:09:19 UTC | #6

Yes, it automatizes strong refcount management, so that you don't have to do manual calls to increment / decrement it.

Intrusive shared pointers may be strange at first to someone coming from a std::shared_ptr background, but once you understand how they work, there should be relatively few ways to shoot yourself in the foot with them. The tendency of API functions to store shared pointers internally is documented in the conventions:

[url]http://urho3d.github.io/documentation/HEAD/_conventions.html[/url]

-------------------------

1vanK | 2017-01-02 01:09:19 UTC | #7

[quote="cadaver"]
[url]http://urho3d.github.io/documentation/HEAD/_conventions.html[/url][/quote]

[quote]When an object's public API allows assigning a reference counted object to it through a Set...() function, this implies ownership through a SharedPtr. For example assigning a Material to a Drawable. To end the assignment and free the reference counted object, call the Set...() function again with a null argument.
[/quote]

I think here we need another example. Drawable has no the member SetMaterial. Only some derived classes

-------------------------

cadaver | 2017-01-02 01:09:19 UTC | #8

Thanks for bringing to attention. Now StaticModel & Renderer are used as examples.

-------------------------

