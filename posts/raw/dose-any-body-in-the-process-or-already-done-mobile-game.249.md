umen | 2017-01-02 00:59:08 UTC | #1

Something that really Interesting to me , its not have to be finished.
does any body doing  something mobile related with the engine and can post his / her Impressions?

-------------------------

Stinkfist | 2017-01-02 00:59:13 UTC | #2

Pugsy in done using Urho3D:  [play.google.com/store/apps/deta ... rfly.pugsy](https://play.google.com/store/apps/details?id=com.boberfly.pugsy) Cannot remember the guy's nick though.

-------------------------

rasteron | 2017-01-02 00:59:13 UTC | #3

Ah yes. this is [b]Alex Fuller[/b]'s game way back..

[groups.google.com/forum/#!msg/u ... NSQuJlYVoJ](https://groups.google.com/forum/#!msg/urho3d/vDK-NIqzeoQ/scNSQuJlYVoJ)

You can also check out Sinsoft's Poker game. They mentioned their old version used this engine but not sure their latest one though.

[sinsoft1.rssing.com/chan-9537995/all_p1.html](http://sinsoft1.rssing.com/chan-9537995/all_p1.html)

-------------------------

boberfly | 2017-01-02 00:59:15 UTC | #4

Hi,

Probably not the most compelling example of Urho3D's potential on mobile but it is a released app and it uses physics, accelerometer, multi-touch, audio (my dog voice impressions need work though), you name it... :slight_smile:

My impression is that it is perfect for mobile app deployment, and this was back when the CMake build system wasn't as robust as it is now with iOS and Android, which used its own .mk build scripts for Android back then. Prototyping on Linux was a breeze and then later deploying to Android, and copying it over to a Mac Mini+XCode for iOS. The app is scripted in AngelScript, and I only used a small amount of iOS/Android-specific things like the accelerometer values which came out differently but that might be fixed now, and I used an OpenAL audio back-end on iOS because I had audio glitches, and added microphone capture support for iOS only [url]https://github.com/boberfly/Urho3D/tree/openal[/url]. Exporting out animation and geometry was mostly reliable out of Maya via FBX for the pug dog and OBJ for the fence (I had issues with the normals getting flipped with FBX and the fence).

A notable point is that the engine footprint is much smaller than things like Unity3D, and you have the power to opt-out on building scripting support which should reduce the engine size dramatically by symbol stripping if you choose to code in C++ so that would be an important note for deployment. Some shaders probably need optimising though but you can read up on a lot of techniques if you're not afraid of GLSL coding, but I only use simple 1-texture shaders so performance isn't a problem and they compile fine on each mobile platform I've tested them on.

One of these days I want to make another crazy action game, my first choice of engine would be Urho3D definitely!

-------------------------

