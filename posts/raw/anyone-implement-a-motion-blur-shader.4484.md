GodMan | 2018-08-21 18:16:16 UTC | #1

I am recreating a game from the original xbox and I believe one of the post processing effects used motion blur. I could be wrong though. Here is a screenshot.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/e/e054fc4faef3786dded867ed6337842c056d4a8a.jpeg'>

-------------------------

Modanung | 2018-08-21 18:23:43 UTC | #2

Is that Soul Reaver? :)

About the blur: did you try a [search](https://discourse.urho3d.io/search?q=motion%20blur)?

-------------------------

GodMan | 2018-08-21 22:35:30 UTC | #3

Yes it's Soul Reaver.

I did find some results but some of the links were broken.

-------------------------

Modanung | 2018-08-22 08:11:12 UTC | #4

Is this not the motion blur you're looking for?
https://discourse.urho3d.io/t/motion-blur-like-doom4/2026
https://discourse.urho3d.io/t/zoom-blur-postprocess-shader-glsl/1337

-------------------------

GodMan | 2018-08-24 15:19:33 UTC | #5

They did a good job on the motion blur. After running the demo that effect does not seem like the one in the picture above. The picture above looks like it uses a overblown blur shader, but it is hard to tell.

-------------------------

GodMan | 2018-08-24 16:49:33 UTC | #6

Okay so after lowering the samples in the shader I got something closer to my screenshot above. However I wonder what would be the best way to make it constant. The effect in the demo is applied to movement and not constant. Which is what motion blur is really for.

-------------------------

Bananaft | 2018-09-19 07:19:37 UTC | #7

I believe this type of yearly 2000s motion blur is done by adding new frame on top of previos one. What renderpath are you using?

-------------------------

GodMan | 2018-09-19 23:33:34 UTC | #8

I am using direct3d9.

-------------------------

Bananaft | 2018-09-23 13:24:06 UTC | #9

Oh ok, nevermind. I just made it but for openGL. Sorry, I don't have dx version ready at hand.

You have to convert copyblur.glsl to hlsl. Should be easy. I just took CopyFramebuffer and added a few lines.
Here how it looks like, I hope that's what you are looking for. You can also try different blending methods.
https://www.youtube.com/watch?v=ArQ0Rg_c79I

https://gist.github.com/Bananaft/461c78495a2878cb132676ccab9535a9

-------------------------

Modanung | 2018-09-23 14:50:08 UTC | #11

@Bananaft What he said.
And if you intend to enslave all of humanity, be sure to add a stereoscopic option. People would donate blood just to walk around in that. :pill: 
If you plan on making it open source, btw, I'd love to contribute. :slight_smile:

-------------------------

Bananaft | 2018-09-23 21:02:07 UTC | #12

Thank you. You already contributed by contributing Urho.

-------------------------

GodMan | 2018-09-24 03:47:16 UTC | #13

Looks great. How much would I have to change for it to work on direct3d9. The shader will not be hard for me to adapt. I have a lot of experience with hlsl.

-------------------------

Bananaft | 2018-09-24 16:14:07 UTC | #14

just convert the shader and it should work.

-------------------------

