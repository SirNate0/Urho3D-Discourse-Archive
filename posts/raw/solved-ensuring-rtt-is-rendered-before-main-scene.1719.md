Enhex | 2017-01-02 01:09:40 UTC | #1

I create a scene with a camera and no viewport, and use it to do RTT and save the result to a texture to be used in a main scene, but there's a 1 frame delay before that texture becomes visible in the main scene.
Is it possible to make sure the RTT texture is ready before rendering the main scene?

-------------------------

codingmonkey | 2017-01-02 01:09:40 UTC | #2

So, actually how did you got 1 frame delay if I guessing what all offscreen RT's are rendered before main view RT ?)

-------------------------

Enhex | 2017-01-02 01:09:41 UTC | #3

I manually update the texture render surface with SetUpdateMode(SURFACE_MANUALUPDATE) and QueueUpdate() in PostUpdate().
If I don't use manual updating it works fine, only using QueueUpdate() is enough to cause it.

I looked into how Urho ensures the viewport order.
In Renderer::Update() this code suppose to ensure that the viewport with the lowest index is rendered first, since it says rendering order is also reverse (from size to 0, so last element is rendered first).
[code]
    // Queue update of the main viewports. Use reverse order, as rendering order is also reverse
    // to render auxiliary views before dependant main views
    for (unsigned i = viewports_.Size() - 1; i < viewports_.Size(); --i)
        QueueViewport(0, viewports_[i]);
[/code]

viewports_ is private and Renderer::SetViewport() is the only function that adds elements to it. That means that only viewports that are added with Renderer::SetViewport() are ordered.

Renderer::QueueViewport() adds the viewport with its render target to queuedViewports_ .

RenderSurface::QueueUpdate() calls Renderer::QueueRenderSurface() which directly uses Renderer::QueueViewport(). That means RenderSurface::QueueUpdate() isn't added to viewports_ and therefore skips the viewport ordering.
That means it would be at the beginning of queuedViewports_, that means it renders after all of the elements in viewports_ because of the reveresed order.

Assuming this is a bug, a possible solution would be to collect all the render surface viewports in Renderer::QueueRenderSurface(), and push them to queuedViewports_ in Renderer::Update() only after the main views are added, so they're rendered first.

Reported as a bug: [github.com/urho3d/Urho3D/issues/1171](https://github.com/urho3d/Urho3D/issues/1171)

-------------------------

