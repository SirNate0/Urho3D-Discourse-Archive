greenhouse | 2017-01-02 01:08:52 UTC | #1

I'm looking for a beginners tutorial on creating 2D games with Urho3D.

Where should I look for it?

-------------------------

greenhouse | 2017-01-02 01:08:58 UTC | #2

I'm specifically interested in using UrhoEditor for scene creation of 2D game. 
Where can I get more info on this topic, please? 

I'm new to Urho3D, where to start from? :slight_smile:

-------------------------

practicing01 | 2017-01-02 01:08:58 UTC | #3

I haven't done a 2D-only game yet, I always use 2D sprites in 3D (for a flat look just use an orthographic camera).  Very few people have dealt with that area of the engine.  Is there something you have in mind that cannot be achieved in 3D?

-------------------------

greenhouse | 2017-01-02 01:08:58 UTC | #4

[quote="practicing01"]I haven't done a 2D-only game yet, I always use 2D sprites in 3D (for a flat look just use an orthographic camera).  Very few people have dealt with that area of the engine.  Is there something you have in mind that cannot be achieved in 3D?[/quote]
Hi practicing01,
The idea I have (nothing original, a kind of fluppy-bird :laughing: ) probably can be made in 3D, but that means I have to find someone who makes 3d graphics and me myself I have almost zero experience with developing 3D games. That's way I'm looking more toward 2D solution.

-------------------------

practicing01 | 2017-01-02 01:08:59 UTC | #5

You misunderstood, you can animate textures and/or you can attach sprites to a node (which resides in 3d space).  Skeletal animation can be done in blender as well.

-------------------------

greenhouse | 2017-01-02 01:08:59 UTC | #6

[quote="practicing01"]You misunderstood, you can animate textures and/or you can attach sprites to a node (which resides in 3d space).  Skeletal animation can be done in blender as well.[/quote]
Yes, I understand that. I can add sprites (and animate their textures) to 3d space, and move them across x and y axis, and use z axis as depth's layer.
Currently, I'm struggling to understand how to setup camera for 2d scenario. As I understood I need to use Orthographical camera with some negative z transpose. But how to determine such camera's size in order to match to the mobile device the game should run on?

-------------------------

practicing01 | 2017-01-02 01:08:59 UTC | #7

Google to the rescue :stuck_out_tongue:! [indiehoodgames.wordpress.com/20 ... a-unity3d/](https://indiehoodgames.wordpress.com/2013/07/27/pixel-perfect-calculator-for-orthographic-camera-unity3d/)  You can change the camera settings through code or the editor.

-------------------------

greenhouse | 2017-01-02 01:08:59 UTC | #8

[quote="practicing01"]Google to the rescue :stuck_out_tongue:! [indiehoodgames.wordpress.com/20 ... a-unity3d/](https://indiehoodgames.wordpress.com/2013/07/27/pixel-perfect-calculator-for-orthographic-camera-unity3d/)  You can change the camera settings through code or the editor.[/quote]
Thanks a lot! Looks very interesting, I'll investigate it more thoroughly...

-------------------------

Mike | 2017-01-02 01:08:59 UTC | #9

2D samples currently adjust camera zoom to fit user's screen resolution. For example in sample 27_Urho2DPhysics.as:

[code]camera.zoom = 1.2f * Min(graphics.width / 1280.0f, graphics.height / 800.0f); // Set zoom according to user's resolution to ensure full visibility (initial zoom (1.2) is set for full visibility at 1280x800 resolution)[/code]

In your project, simply replace 1280 and 800 by your own screen resolution then adjust zoom as you like. You only have to do this once: when you run your project on another device, content display will automatically adapt to your new screen resolution.

-------------------------

greenhouse | 2017-01-02 01:08:59 UTC | #10

[quote="Mike"]2D samples currently adjust camera zoom to fit user's screen resolution. For example in sample 27_Urho2DPhysics.as:

[code]camera.zoom = 1.2f * Min(graphics.width / 1280.0f, graphics.height / 800.0f); // Set zoom according to user's resolution to ensure full visibility (initial zoom (1.2) is set for full visibility at 1280x800 resolution)[/code]

In your project, simply replace 1280 and 800 by your own screen resolution then adjust zoom as you like. You only have to do this once: when you run your project on another device, content display will automatically adapt to your new screen resolution.[/quote]

Hi Mike,
What does it mean [i]user's screen resolution[/i]? Is it a resolution which designer used for preparing game assets or it's a resolution of the mobile device screen?

[url=http://v-play.net/doc/vplay-different-screen-sizes/]My current workflow[/url] for preparing assets and adopting to different mobile device screen sizes : (in Cocos2d-x)
I use 1920 x 1280 (3:2 aspect ratio) as safe-zone resolution, that's the game area that will always be shown on any mobile device screen. 
I prepare graphics according to that resolution and for background I use slightly bigger 2280 x 1520 (3:2 aspect ratio) resolution, for nice padding on mobile device which screen aspect ratio is different than 3:2.
All that graphics are scaled and duplicated for HD (1.0 scaling), SD (0.5 scaling) and LD (0.25 scaling) assets folders.
On game start up I query device's screen size and set the search path for relevant assets folder.

-------------------------

Mike | 2017-01-02 01:09:00 UTC | #11

You can try it for yourself with sample 32_Urho2DConstraints.as :
- run the sample with a 800x600 resolution (or less, this is just an example)
- replace 1280 and 800 by 800 and 600 => camera.zoom = 1.2f * Min(graphics.width / 800.0f, graphics.height / 600.0f);
- tweak 1.2 to adjust zoom to what looks best for you

-------------------------

greenhouse | 2017-01-02 01:09:00 UTC | #12

[quote="Mike"]You can try it for yourself with sample 32_Urho2DConstraints.as :
- run the sample with a 800x600 resolution (or less, this is just an example)
- replace 1280 and 800 by 800 and 600 => camera.zoom = 1.2f * Min(graphics.width / 800.0f, graphics.height / 600.0f);
- tweak 1.2 to adjust zoom to what looks best for you[/quote]
I can try but the problem is that I cannot grab what stands behind these numbers...  :frowning: 

graphics.width and graphics.height is probably (I hope) screen size of my laptop (which is 1280 x 800)
next we divide screen width by 1280 and height by 800, but what those 1280 and 800 represents? size of what?
next multiply by zoom factor Min of both...

Also line before that which sets Ortho size:
[code]camera_->SetOrthoSize((float)graphics->GetHeight() * PIXEL_SIZE); [/code]  
I don't get it...  :blush: 

Say I have made 2 images for my game which should be played only in landscape mode: 
one is a background of size 2280 x 1520
another is a hero of size 800 x 600 positioned in the center of safe-zone
And I want my safe-zone to be of size 1920 x 1280, that's the game area that will always be shown on any device out there

How to make it work properly on different devices? I know how to do it on another engine, but have no clue how to accomplish this with Urho3D.

-------------------------

greenhouse | 2017-01-02 01:09:01 UTC | #13

[quote="practicing01"]Google to the rescue :stuck_out_tongue:! [indiehoodgames.wordpress.com/20 ... a-unity3d/](https://indiehoodgames.wordpress.com/2013/07/27/pixel-perfect-calculator-for-orthographic-camera-unity3d/)  You can change the camera settings through code or the editor.[/quote]
Seems like nice formula to calculate ortho camera size... but I can't figure out what [quote]s = Desired Height of Photoshop Square (px)[/quote] does mean? 

I'm zero in Photoshop  :cry:

-------------------------

Mike | 2017-01-02 01:09:02 UTC | #14

Using PIXEL_SIZE ensures that the display doesn't stretch when rotating your device.

Zoom ratio (1.2) is determined from my desktop resolution (1280x800).
Now if I want my display to be the same on another desktop or a mobile device, I have to account for the new resolution, that's why I scale with graphics.width and graphics.height.
If I had tested with a 800x600 resolution then the zoom ratio would have been much lower to display the entire scene.

-------------------------

Modanung | 2017-01-02 01:09:18 UTC | #15

On a sidenote: Since Urho3D [url=http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_tmx_file2_d.html]supports[/url] [url=http://doc.mapeditor.org/reference/tmx-map-format/]TMX[/url] quite well, [url=http://www.mapeditor.org/]Tiled[/url] can be a very convenient level editor for 2D projects.

-------------------------

greenhouse | 2017-01-02 01:09:18 UTC | #16

[quote="Mike"]Using PIXEL_SIZE ensures that the display doesn't stretch when rotating your device.

Zoom ratio (1.2) is determined from my desktop resolution (1280x800).
Now if I want my display to be the same on another desktop or a mobile device, I have to account for the new resolution, that's why I scale with graphics.width and graphics.height.
If I had tested with a 800x600 resolution then the zoom ratio would have been much lower to display the entire scene.[/quote]

Thanks for clarifications, Mike. I have to play with different settings to get a feel of how it all works.

-------------------------

greenhouse | 2017-01-02 01:09:18 UTC | #17

[quote="Modanung"]On a sidenote: Since Urho3D [url=http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_tmx_file2_d.html]supports[/url] [url=http://doc.mapeditor.org/reference/tmx-map-format/]TMX[/url] quite well, [url=http://www.mapeditor.org/]Tiled[/url] can be a very convenient level editor for 2D projects.[/quote]

On a sidenote, I have bought all 3 tools from CodeAndWeb for my cocos2d-x projects. As I understood, TexturePacker and PhysicsEditor I can use for Urho3D projects as well (with Sparrow template selected). But, can I use their 3rd tool SpriteIlluminator with Urho3D as well?

-------------------------

BratSinot | 2017-01-22 16:59:36 UTC | #18

Hello there!

Can anyone help me?
I create simple scene in editor, create ortho camera and load scene in AngelScript. But when i load script into Player i got black screen.
https://yadi.sk/d/GIC68Zes3ALYEP

-------------------------

Eugene | 2017-01-22 19:11:02 UTC | #19

You have black screen because you draw nothing.
Have you tried examples?

BTW, read forum rules. You abused them.

-------------------------

BratSinot | 2017-01-22 19:22:01 UTC | #20

[quote="Eugene, post:19, topic:1607"]
lack screen because you draw nothing.Have you tried exam
[/quote]
I try find some Urho2D examples, but got nothing special. In all examples i see the same thing that I have.

-------------------------

Eugene | 2017-01-22 19:42:33 UTC | #21

All scripts in `bin/Data/Scripts` work fine.

-------------------------

BratSinot | 2017-01-23 12:34:27 UTC | #22

They didn't load XML file from editor. Of course, if you do everything yourself, it will work!

-------------------------

Eugene | 2017-01-23 12:44:00 UTC | #23

Loading XML scene from editor is a single line of code. So I don't think that it is a problem to make any of example scripts load scene from XML. Anyway, these examples is a good start point for learning Urho script API.

-------------------------

BratSinot | 2017-01-23 13:03:05 UTC | #24

[quote="Eugene, post:23, topic:1607"]
m editor is a single line of code. So I don't think that it is a problem to make any of example scripts load scene from XML. Anyway
[/quote]
It not is problem, this just NOT WORK.

In my XML scene i have TileMap2D and ortho camera. I load scene like this: "scene_.LoadXML(cache.GetFile("test.xml"))" in AS script.

-------------------------

Eugene | 2017-01-23 13:48:42 UTC | #25

[quote="BratSinot, post:24, topic:1607"]
It not is problem, this just NOT WORK.
[/quote]

Huh, I'm a bit confused now.
Are you talking about code from the archive above?
Or you've tried to add scene loading into _working_ example scripts?

-------------------------

BratSinot | 2017-01-23 16:52:19 UTC | #26

I tried create script. Only example with XML scene is NinjaSnow. I load scene by LoadXML(), get camera from camera node and set viewports[0].
http://pastebin.com/kHjtam87

-------------------------

johnnycable | 2017-03-01 16:35:12 UTC | #27

Hello there, I'm from cocos2dx too, and i'm trying to understand the differences between cocos design resolution and urho magnifying factor...
incidentally, sprite illuminator could be used... but one has to adapt the shaders from c++ codenweb sdk to urho one... so not out of the box...

-------------------------

