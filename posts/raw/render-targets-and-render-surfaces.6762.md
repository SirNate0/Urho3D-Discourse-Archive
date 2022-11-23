Lunarovich | 2021-03-18 11:48:05 UTC | #1

I've been re-reading documentation and can't get my head around the difference between the render target and render surface. More precisely, I understand that render surface is a "color or depth-stencil surface that can be rendered into" and since I know a bit of OpenGL, this is clear to me. Also, I use it to render to texture (as shown in the Urho3D samples).

However, I can't understand what is exactly the meaning of the render target. Is it the same thing? Is it different from render surface? 

The complementary question would be this: what is the difference between a pass and a renderpath command?

Thank you!

-------------------------

Eugene | 2021-03-18 13:11:28 UTC | #2

[quote="Lunarovich, post:1, topic:6762"]
what is exactly the meaning of the render target. Is it the same thing? Is it different from render surface?
[/quote]
RenderSurface is _any_ destination surface, which could be color or depth texture, non-readable depth renderbuffer or framebuffer color/depth.
Render Target often means _readable_ render surface, i.e. texture one.

[quote="Lunarovich, post:1, topic:6762"]
The complementary question would be this: what is the difference between a pass and a renderpath command?
[/quote]
`Pass` as class aka `pass` in material is... well... a pass of object rendering. I.e. lit geometry has base pass that renders ambient, light pass that renders per-pixel light from light source, shadow pass that renders object to shadow map, depth pass that renders object w/o color for depth pre-pass.

"renderpath command" is global sequential stage of scene rendering which may render zero, one or several object "passes".

-------------------------

Lunarovich | 2021-03-18 17:08:45 UTC | #3

@Eugene thank you! So, to check my understanding, render target is one type of render surface. If yes, I have another dilemma here. Namely, I have this code:

```
    RenderSurface* surface = renderTexture->GetRenderSurface();
    Viewport* viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    surface->SetViewport(0, viewport);

    SharedPtr<RenderPath> renderPath = viewport->GetRenderPath()->Clone();
    URHO3D_LOGINFOF("%d", renderPath->GetNumRenderTargets()); // debug
```
The last line gives me `0` as if I did not have any render targets attached...

As to the renderpath command, I see that default render paths from the CoreData refer to some of the passes referred to in techniques. However, there is an added info as to the pass type and there are some types of passes that do not appear in material related techniques. If I understand well, there are passes that happen "outside" of the scene, so to say, or "on top of the scene" and the final render is the result of all these passes.

-------------------------

Eugene | 2021-03-20 06:52:34 UTC | #4

[quote="Lunarovich, post:3, topic:6762"]
The last line gives me `0` as if I did not have any render targets attached…
[/quote]

`surface` contains `viewport`, `viewport` contains `renderPath`, `renderPath` contains auxiliary render surfaces counted by `GetNumRenderTargets`. `renderPath` never knows about its destination, it references it by keyword "viewport" but it never owns it.

[quote="Lunarovich, post:3, topic:6762"]
If I understand well, there are passes that happen “outside” of the scene, so to say, or “on top of the scene” and the final render is the result of all these passes.
[/quote]
"on top" is good analogy, because non-scene passes are usually some kind of pre- or post-processing done at some point.
Note that "post-processing" may happen at any point, not only after all scene passes. I.e. deferred lighting via `lightvolumes`.

-------------------------

Lunarovich | 2021-03-24 21:13:55 UTC | #5

Thank you! Certainly not an easiest of all the topics :)

-------------------------

