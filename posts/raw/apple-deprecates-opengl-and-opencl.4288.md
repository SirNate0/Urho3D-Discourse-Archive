extobias | 2018-06-05 13:42:17 UTC | #1

All in favor of Metal
https://developer.apple.com/macos/whats-new/#deprecationofopenglandopencl

-------------------------

Eugene | 2018-06-05 14:15:55 UTC | #2

Sucks.
@boberfly it's your chance! xD

-------------------------

johnnycable | 2018-06-05 17:50:17 UTC | #3

That was expected. Anyway WTF. While you can expect Mac to take ages before open gl goes away, this is almost sure to be removed on next ios version (that is, ios 13). This means we probably won't be able to ship anymore for ios in one year.

-------------------------

weitjong | 2018-06-06 01:37:08 UTC | #4

It is actually an opportunity to see whether this project is dead as the fish or not.

-------------------------

WangKai | 2018-06-06 03:19:26 UTC | #5

World needs to be saved!

-------------------------

WangKai | 2018-06-06 04:39:50 UTC | #6

https://github.com/floooh/sokol/blob/master/sokol_gfx.h
https://github.com/bkaradzic/bgfx/blob/master/src/renderer_mtl.h

-------------------------

johnnycable | 2018-06-06 07:37:27 UTC | #7

Indeed. Everybody welcome the Urho showdown.:fish::tropical_fish::blowfish:
Will it survive, or will we have to rename it "the deadfish engine?"

-------------------------

WangKai | 2018-06-06 08:33:07 UTC | #8

MoltenVK, translation layer from Vulkan to Metal is open sourced - 
https://github.com/KhronosGroup/MoltenVK

Currently, we have DX9, DX11, OpenGL renderers.
The practical way to survive for Urho is -
* Add Vulkan (especially for Android)
* Support Metal (via something as MoltenVK or directly by using Metal API)
* Abandon DX9 (goodbye a few WinXP users)
* Optional support for DX12 (DX11 is good enough for a lightweight game engine) 
* We are able to be more advanced for the graphics, sitting on the modern graphics APIs: DX11/Vulkan/Metal

Edit: for optimists, we only need to add one Vulkan renderer :sweat_smile:

-------------------------

Eugene | 2018-06-06 08:55:18 UTC | #9

Or add BGFX backend and don't care anymore :laughing:
BGFX has its own problems tho. Too highlevel batch processing is one of them.

-------------------------

Eugene | 2018-06-06 14:56:05 UTC | #10

I also wonder what Apple is going to do with WebGL to keep it working in iOS browsers.

-------------------------

TheComet | 2018-06-07 08:11:20 UTC | #11

Excuse my ignorance, but I always thought Vulkan ran directly on Mac. Why would you need a vulkan-to-metal layer?

-------------------------

johnnycable | 2018-06-07 08:19:54 UTC | #12

https://github.com/KhronosGroup/MoltenVK

Even if Urho had Vulkan shaders, you would need this on Mac Os / Ios
In short only Metal and Open gl are supported by Apple as of now.

-------------------------

elix22 | 2018-06-07 11:01:48 UTC | #13

I am afraid that no one will add any support for Metal .

The best way  would be to take an off the shelf  cross platform solution that is actively developed , i.e. BGFX.

Another option  would be to use ANGLE with an Vulkan backend which is currently under development  and put it on top of  MoltenVK

https://github.com/google/angle/tree/master/src/libANGLE/renderer/vulkan

So the translation would be :   OpenGL ES -> Angle -> Vulkan -> MoltenVK

-------------------------

artgolf1000 | 2018-06-10 02:26:08 UTC | #14

Urho heavily dependents on OpenGL, I have been studying Metal for several days, there are too few tutorials and examples to cover all cases, such as water, grass etc. To port the render part, you need to re-write nearly all codes, include c++ part and shader part.

-------------------------

WangKai | 2018-06-10 02:58:16 UTC | #15

Not hard for Po, the kungfu panda. As rabbit and pig, I'm calling for the panda to save the world, or his fish master :sweat_smile:

-------------------------

johnnycable | 2018-06-10 10:07:12 UTC | #16

[quote="Eugene, post:9, topic:4288"]
Too highlevel batch processing is one of them.
[/quote]

I'm trying bgfx these days. Could you elaborate on this?

-------------------------

Eugene | 2018-06-10 11:14:39 UTC | #17

[quote="johnnycable, post:16, topic:4288"]
I’m trying bgfx these days. Could you elaborate on this?
[/quote]

AFAIK batches are totally independent.
If you want process 20k batches, you have to fill every batch with all possible data including all shader uniforms.

It allows more optimization, but require more processing.

-------------------------

gunbolt | 2018-06-10 15:53:25 UTC | #18

When's the next release of Urho3D ? Is the project really dead in the water ? It's been a long time since 1.7 and slant.co is saying the popularity of Urho3d is on the decline.

-------------------------

Modanung | 2018-06-10 16:18:59 UTC | #19

I'd say resources are low on many fronts and we lost our commander, but there sure is a pulse and steady progress on this already very functional engine. What _lightweight_ bells and whistles did you have in mind?
As you may know from [metal lore](http://www.mikseri.net/artists/urho.114651.php), Urho is quite comfortable in the dark, and as long as it works for Linux it works for me. :+1:

-------------------------

gunbolt | 2018-06-10 17:08:16 UTC | #20

What lightweight bells and whistles? An easy way to export project to Android Studio for compilation/signing. To me, urho3d is feature complete for now. Just missing the most important obvious support for Android.

-------------------------

weitjong | 2018-06-10 19:54:44 UTC | #22

If you really look at the recent release history then you should know usually Urho only release about one version a year and that version 1.8 is not overdue yet. Also note that we are not in a hurry of releasing anything. It’s ready when it’s ready. And as for Android build support using Gradle out of the box is just perhaps a day work. The problem is, no one works full day for this project.

-------------------------

johnnycable | 2018-06-11 10:48:07 UTC | #23

A good intro tutorial is here, albeit old: https://www.raywenderlich.com/146414/metal-tutorial-swift-3-part-1-getting-started
Anyway just reading it is sufficient to agree to what you say: it would take a complete rewrite. Difficult.
Besides that, I've checked out bgfx. Same, even worst; that's more low-level too, imho. That's another rewrite.
No opt-out of open gl as of now. Bye bye, Apple.

-------------------------

Eugene | 2018-06-11 12:12:12 UTC | #24

[quote="johnnycable, post:23, topic:4288"]
Besides that, I’ve checked out bgfx. Same, even worst; that’s more low-level too, imho
[/quote]

@boberfly had some progress with it.
Why do you think that BGFX would be even harder to adopt?

-------------------------

johnnycable | 2018-06-11 16:16:00 UTC | #25

The metal approach looks like much Urho; high level abstraction. I feel bgfx is abstracted someway but low level at the same time. Just a feeling, probably stemming from differences between c++ and swift.
Not really sure anyway about which would be tougher to integrate in Urho...

-------------------------

