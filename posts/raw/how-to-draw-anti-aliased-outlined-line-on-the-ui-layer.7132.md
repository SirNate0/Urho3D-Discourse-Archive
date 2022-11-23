najak3d | 2022-01-17 22:09:11 UTC | #1

We are a mapping App, and support split screen.

When you tap on a map location, we popup up an info box, and want to draw a line from Pop-up box to the map location, with a circle at the end, as shown here (screenshot from our old app that we are porting):
![image|381x500](upload://rqKURPhHQrAf9PidrOUU8kUq715.jpeg)

What is the best method to create this line in the UI?   (it needs to ignore Viewports, and use the whole screen)

Also to note, that as you pan the map, the circle-end will move with the map dynamically, without jitter.

-------------------------

Modanung | 2022-01-18 00:41:05 UTC | #2

You might basically want to create a mesh and render it to a texture in a separate scene. If it's only about the straight line, just transform a plane. The outline is simply a little wider and drawn below.

-------------------------

najak3d | 2022-01-19 05:19:45 UTC | #3

We do have a very nice line-drawing capacity here in the 3D scene (works in World 3D space).  We could adapt this to work in Screen space, but would have to do it in a fashion that ignores the Viewports (split-screen).

I know how to render a full-screen transparent sprite to the screen, and do it that way.   But I think we'd prefer to just use our Line Renderer in ScreenSpace, so long as we could render it across the full screen (both viewports, ignoring view ports entirely).

Is the only (easy) way to do this, to render a whole different scene "RenderToTexture" style, then use this result as a Full-Screen UI Sprite?  (so would require a full-screen texture with transparent background)?

Our preference would be to create a vertex buffer of verts (i.e. a mesh that follows the line contours) in screenspace, and then have our Line Renderer render similar to how we're doing it in scene.  But we're not sure how you use the Urho UI in this fashion.

-------------------------

SirNate0 | 2022-01-19 12:15:48 UTC | #4

Not certain of this at all, but I think another option is to have a third viewport that takes up the entire screen and adjust it's renderpath to remove the clear command (and maybe also use a fully transparent fog color for it). I think you could also use an orthographic camera for that viewport if you didn't want to deal with converting coordinates for it.

-------------------------

Modanung | 2022-01-19 13:04:06 UTC | #5

Overlaying viewports _is_ also an option. It just seemed more logical to keep them small and separate.
Each could be manually updated as needed, and be its own `Sprite`. Overlaying viewports sounds a bit like reinventing the `UI` to me; goodbye drawing order 'n all that.

-------------------------

najak3d | 2022-01-19 20:26:41 UTC | #6

Does Urho's UI system permit us to create a screen-based vertex buffer, to which I can assign a material/shader?   If so, that would work swell.   It would work the same as our current 3D lines work in the regular 3D views... except it would simply all be in screen space.  

I figured the current Urho UI must operate as a last pass on the full-screen render output buffer -- which would allow a sensible/efficient implementation.  (Does the Urho UI ignore view port concept?)

-------------------------

JTippetts1 | 2022-01-20 19:32:03 UTC | #7

You could create a custom UI element for this. I do something like that to implement noodle links between nodes in a node graph. UIElement provides a virtual function called GetBatches that you can use to draw your own custom stuff. You can build whatever you need to draw as a [UIBatch](https://github.com/rbfx/rbfx/blob/master/Source/Urho3D/UI/UIBatch.h)

-------------------------

najak3d | 2022-01-20 20:13:30 UTC | #8

@JTippetts1  - this sounds like exactly what we are looking for here.  Thank you!

-------------------------

