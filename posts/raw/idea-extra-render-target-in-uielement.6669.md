WangKai | 2021-01-21 15:25:47 UTC | #1

If we have an optional render texture in UIElement, we set this render target as a canvas for its children before rendering, then we use this canvas to draw this UIElement itself. We can easily scale this UIElement, without caring about layout. Just like any window scaling animation you can see in desktop OS.

By introducing grid vertices as the structure of the canvas of UIElement, we can further deform it to achieve advanced animation effect.

We have to modify UI Batch implementation to achieve this.

-------------------------

WangKai | 2021-01-21 15:45:56 UTC | #2

I posted as an idea since I don't see a quick change work :stuck_out_tongue:

-------------------------

JSandusky | 2021-01-22 03:05:32 UTC | #3

If you really need a deformable or shader-processed GUI (I'm assuming it's for purposes like a "*glitch*" effect) you can stick one in using UIComponent on a Node after adding access to the material (so you can change it). See 48_Hello3DUI examples.

That's limited but covers the reasonable use cases I can think of (deforming intro/outro, glitch/emp effect, etc).

Edit: I missed the caveat that if you need ortho rather than perspective for those you'll need to layer a view (clear only depth/stencil in the renderpath for it) and setup your view masks.

-------------------------

WangKai | 2021-01-22 04:25:14 UTC | #4

Yes, I have checked UIComponent, however, I think render target in UI should not be only limited to 3D UI, it can be anywhere. UIComponent UI is rendered at very last after other UI elements finished, which caused an issue that UICompoent cannot be overlapped by other normal UI.

-------------------------

JTippetts1 | 2021-01-22 17:19:08 UTC | #5

@Lumak did a [custom UI widget](https://github.com/Lumak/Urho3D-Custom-UI-Mesh) a few years ago that allows you to use a model mesh for a UI element. That might be something you could look into. Hasn't updated it in awhile, so not sure how well it would still integrate into Urho, but it shouldn't be too difficult to update if necessary.

-------------------------

