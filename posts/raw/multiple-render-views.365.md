Bluemoon | 2017-01-02 00:59:53 UTC | #1

Is there a way to implement a multiple Urho3d view window in a gui appliction. For example a wxWidgets application having two panels each showing a different Urho3d scene. Would I have to create separate Urho3d instance with sperate context for each view? How exactly can this be achieved if its possible at all?

-------------------------

cadaver | 2017-01-02 00:59:53 UTC | #2

If you have a central view widget, it's easy and natively supported to split that into multiple viewports. However, multiple OS-level rendering windows (or widgets in a GUI application) are not supported, so you will need to resort to a bit dirty and performance-costly tricks: render to a texture, GetData() the RGB pixels out, set those pixels into the GUI library's image class, and paint that into the extra widget.

-------------------------

najak3d | 2020-09-16 16:13:04 UTC | #3

Is this still the answer as of November 2018? (we're using UrhoSharp which is currently bound to that version)

We need to target multiple-surfaces with our app (separate Xamarin Forms controls).

-------------------------

Modanung | 2020-09-16 18:50:09 UTC | #4

Why not update the bindings?
[spoiler]
[details=""]
![](https://www.telegraph.co.uk/content/dam/tv/2017/05/11/TELEMMGLPICT000128359591-xlarge_trans_NvBQzQNjv4BqQ7WNz19EjnCWyGlhqb7K115gAV53SP55Ss8DEC6APkA.jpeg)
[/details]
[/spoiler]

-------------------------

Eugene | 2020-09-16 20:54:26 UTC | #5

I thought you already asked this question before... Yes, manually copying textures is the way to go if you cannot hack into C++ code.

-------------------------

najak3d | 2020-09-16 21:58:08 UTC | #6

Modanung - does the latest Urho3D support rendering to multiple surfaces?  If not, then updating the bindings doesn't help us any.  We are not planning to modify Urho3D, and are trying to avoid modifying UrhoSharp.   Right now we are pushing on Microsoft for a few UrhoSharp fixes, and if they do this, they might update to the latest Urho3D as well.   .NET 5 is released in November, and I think they're going to want to make UrhoSharp .NET 5 compatible.  So there is hope of another build soon.  (From Egorbo who works for them now.)

-------------------------

najak3d | 2020-09-16 22:03:12 UTC | #7

Eugene - I asked similar question, but not this one (that I recall).

We're trying to decide between doing RenderToTexture, or just doing the Application.Renderer.GetScreenBuffer() -- I'm not even sure what that is supposed to do, but it seems like it *might* be something we want to consider.  Thoughts?

-------------------------

Eugene | 2020-09-16 22:45:41 UTC | #8

[quote="najak3d, post:7, topic:365"]
We’re trying to decide between doing RenderToTexture, or just doing the Application.Renderer.GetScreenBuffer()
[/quote]

`GetScreenBuffer` return you a texture that you can render into. So it's not much of a choice.
`GetScreenBuffer` doesn't return screen buffer that you render to by default -- it returns clean new one.

-------------------------

najak3d | 2020-09-17 00:03:48 UTC | #9

Is there an advantage to using this ScreenBuffer vs. just manually my own Texture2D?    I can think of one possible assumed advantage which is that the ScreenBuffer is not auto-Disposed if not attached to an in-scene Node/Model  (that would be my assumption).

-------------------------

