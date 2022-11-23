Barefists | 2018-12-29 03:05:53 UTC | #1

I've recently starting using UrhoSharp, and I'm running into an issue where:

    StaticSprite2D spr = scene.CreateChild().CreateComponent<StaticSprite2D>();
    spr.Sprite = ResourceCache.GetSprite2D("path/to/filename.jpg");

works and renders the image to screen, but:

    StaticSprite2D spr = scene.CreateChild().CreateComponent<StaticSprite2D>();
    spr.Sprite = new Sprite2D();
    spr.Sprite.Texture = ResourceCache.GetTexture2D("path/to/filename.jpg");

doesn't. It just shows a blank screen.

I'm not sure if this is UrhoSharp specific, or something missing from my understanding of the Urho3D pipeline in general, so I'd thought to ask here. Would appreciate any help whatsoever. Thanks!

-------------------------

Modanung | 2018-12-29 17:08:57 UTC | #2

I could imagine the sprite created using the `new` keyword to be initialized - and remain - dimensionless. Does it work if you also call `SetRectangle` on that sprite?

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

Barefists | 2018-12-29 17:59:14 UTC | #3

[quote=" Modanung, post:2, topic:4780"]
I could imagine the sprite created using the `new` keyword to be initialized - and remain - dimensionless. Does it work if you also call `SetRectangle` on that sprite?

Also, welcome to the forums! :slightly_smiling_face: :slightly_smiling_face:
[/quote]

Thanks for the welcome! 

This was the closest thing I could find in the documentation to SetRectangle:

```
StaticSprite2D spr = scene.CreateChild().CreateComponent<StaticSprite2D>();
spr.Sprite = new Sprite2D();
spr.Sprite.Texture = ResourceCache.GetTexture2D("path/to/filename.jpg");
spr.Sprite.Rectangle = new IntRect(0, 0, spr.Sprite.Texture.Width, spr.Sprite.Texture.Height);
```

Still nada. :confused:

-------------------------

Barefists | 2018-12-29 18:04:22 UTC | #4

I'm still curious about the answer, but I've since implemented an alternative using the GUI library instead.

UrhoSharp has some neat pre-scripted Actions you can use to auto-animate nodes, which I was hoping to use for my sprites... but, I guess I can write something similar myself for GUI elements. :slight_smile:

-------------------------

Modanung | 2018-12-29 18:36:57 UTC | #5

I don't mean to chase you away, but since you're writing in C# you might be interested in [Xenko](https://xenko.com/).
It's an open-source (MIT) game engine as well, but written in C#.

-------------------------

Barefists | 2018-12-30 12:49:24 UTC | #6

Xenko (and a few other engines I've looked at) feels a little too much for my simple card game project. I also prefer the simplicity and familarity of visual studio to more complex and featured IDEs that come with these bigger engines. It's just a matter of preference I suppose. :slight_smile:

-------------------------

I3DB | 2019-01-03 17:15:37 UTC | #7

@Barefists I dont have access to the Graphics.UI on my platform (WMxR), but even so would like to see your solution since you opened this thread and only really add you found another way to do it, without showing that way. 

This code is used with all the following:
```
var spriteContainer = Scene.CreateChild("StaticSprite2D");
var staticSprite = spriteContainer.CreateComponent\<StaticSprite2D\>();
staticSprite.Sprite = sprite;
```
When I use:
```
Sprite2D sprite = ResourceCache.GetSprite2D("Textures/UrhoDecal.dds");
sprite.Texture = ResourceCache.GetTexture2D("Textures/UrhoDecal.dds");
```
Or just
```
Sprite2D sprite = ResourceCache.GetSprite2D("Textures/UrhoDecal.dds");
```
It works for me.

If I use:
```
Sprite2D sprite = new Sprite2D();
sprite.Texture = ResourceCache.GetTexture2D("Textures/UrhoDecal.dds");
sprite.Rectangle = new IntRect(0,0, sprite.Texture.Height, sprite.Texture.Width);
```
This also works, but paints a rectangular shape with only a partial texture and black filling as my texture is not rectangular.

If I use just:
```
Sprite2D sprite = new Sprite2D();
sprite.Texture = ResourceCache.GetTexture2D("Textures/UrhoDecal.dds");
```
Then nothing paints but everything else works as intended.

@Modanung Why redirect to go look at a completely different engine, just because it's not well known how to add a texture to a 2D sprite with C# bindings for Urho3D?  I'm writing in C# and find Urho3D does most everything needed, but with C# bindings there is practically no documentation so it's necessary to root through the C# feature samples and figure out with experimentation. That said I've been unable to get shadows working yet.

Edit: The black rectangle fill being visible depends upon the BlendMode chosen for the Static sprite. BlendMode.Add doesn't show it, but BlendMode.Alpha does.

-------------------------

Barefists | 2019-01-03 02:31:29 UTC | #8

@13DB I used the following code (inside the Application class) to display the texture using GUI.
```
Sprite spr = new Sprite();
spr.Texture = ResourceCache.GetTexture2D("path/to/filename.jpg");
UI.Root.AddChild(spr)
```

For shadows, it works only on Drawable Classes (Light, StaticModel, AnimatedModel, RibbonTrail, etc), and not for Drawable2D classes. For those objects (and the light shining on them), you'll need to set the `CastShadows` property to `true`.

That said, it does not seem to work on Android when I tested, only on Windows.

-------------------------

Barefists | 2019-01-03 02:30:35 UTC | #9

I'm really enjoying the C# bindings so far. _Almost_ everything works as intended, and is very simple to understand (I'm not a trained programmer, C++ scares me). Like 13DB said, documentation is sparse, but the samples are pretty useful in figuring out most of what you need to make things work.

I say almost everything because there are still some known bugs, like networking doesn't really work. I recently added my comments to the [relevant bug thread](https://github.com/xamarin/urho/issues/180) on their Github, which has remained open for nearly 2 years.

-------------------------

I3DB | 2019-01-03 17:34:41 UTC | #10

I've been looking at p2p networking rather than using a server, but haven't coded up anything yet. Looking at [datagramsockets](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/DatagramSocket) or [app services](https://docs.microsoft.com/en-us/windows/uwp/launch-resume/communicate-with-a-remote-app-service). Though this is windows specific and would prefer to use something cross platform. Also looking at [unet](https://github.com/maddnias/uNet) and others used with Unity such as [tnet](http://www.tasharen.com/?page_id=4518).

As for shadows, have yet to see a shadow on a Hololens. Even a simple example with a drawable plane and a drawable box above it, and the light positioned above or to the side of the box. The box material will be correctly shaded based on light positions, but no shadows appear on the plane.

-------------------------

Barefists | 2019-01-04 00:21:48 UTC | #11

If you are looking for proven C# networking libs, look at [Lidgren Network](https://github.com/lidgren/lidgren-network-gen3). It was used for [Stardew Valley](https://twitter.com/concernedape/status/697246539849175040?lang=en), among other games. Personally, I'm using [LiteNetLib](https://github.com/RevenantX/LiteNetLib), which pretty much does the same thing, but it supports .NET Standard 2.0.

Both of them are very easy to use and have an active community.

-------------------------

