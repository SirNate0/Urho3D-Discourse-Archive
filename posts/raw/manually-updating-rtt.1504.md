Enhex | 2017-01-02 01:08:10 UTC | #1

From what I understand, RenderSurface can use SetUpdateMode(SURFACE_MANUALUPDATE), and QueueUpdate() to manually render.

I have dedicated scene for RTT, in which I want to render individual models.
Right now my plan is to create a node for each model and disable all nodes except the one which I want to render.

The problem is when does the render actually happen?
Is it enough to enable a node, call QueueUpdate(), and disable it?
Do I have to wait until the render finishes before I can switch a node?
If so, does it mean I need a RTT scene for each model in order to render several models simultaneously?
(I want to avoid hacks like trying to position models far apart from each other to have a single scene, but if there's an elegant solution I'd like to know)

-------------------------

Enhex | 2017-01-02 01:08:10 UTC | #2

So in order to render several individual models I'll need a scene for each?
Any idea if creating and/or having many scenes is expensive?

I'm thinking about pooling RTT scenes.

-------------------------

codingmonkey | 2017-01-02 01:08:10 UTC | #3

>So in order to render several individual models I'll need a scene for each?
No, you may use additional camera (with viewMask setup) + yours models (with same viewMask) and try render this into RTT.
You may also rearrange the placement of your "individual visible" models to fit all space of RTT (grid 2x2 4x4...), and get they separately from this RTT (with material offset adjusting or copying parts from this RTT to other)

-------------------------

Enhex | 2017-01-02 01:08:11 UTC | #4

[quote="codingmonkey"]>So in order to render several individual models I'll need a scene for each?
No, you may use additional camera (with viewMask setup) + yours models (with same viewMask) and try render this into RTT.
You may also rearrange the placement of your "individual visible" models to fit all space of RTT (grid 2x2 4x4...), and get they separately from this RTT (with material offset adjusting or copying parts from this RTT to other)[/quote]

I liked the viewmask suggestion, tho it will still require more scenes once the mask is fully used.

I don't like the positioning hack, it adds a lot of complexity and doesn't scale well - making sure other models aren't inside each other's view, having to cull the rest of the models, floating point error, translating the camera, and so on.

-------------------------

codingmonkey | 2017-01-02 01:08:12 UTC | #5

>It shouldn't be
Scene by it self no, but I guessing there will be camera with own RTT this is heaviest switching operation for renderer.

-------------------------

Enhex | 2017-01-02 01:08:12 UTC | #6

I have another question:
Are scenes rendered in specific order?
I want to use the RTT result in the same frame for the main scene.
If the main scene is rendered before the RTT, wouldn't it be missing the current result?

-------------------------

cadaver | 2017-01-02 01:08:12 UTC | #7

It should go so that the backbuffer views are rendered last, so they can rely on RTT's being up-to-date.

-------------------------

