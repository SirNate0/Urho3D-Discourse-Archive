orefkov | 2019-10-26 10:04:20 UTC | #1

Hi!
I m add support for GLES3 rendering API and it features:
- Instancing
- Uniform buffer object
- Multiple render targets
- Texture2DArray
- Texture3D
- Support for textures: ETC2, sRGB, floating point, depth, 1 & 2 channel (R & R/G).
Worked render pathes - Deferred, DeferredHWDepth, Prepass, PrepassHWDepth.

Sources - https://github.com/orefkov/Urho3D/tree/GLES3_Support

For build set option URHO3D_GLES3=1
For CMake need -DURHO3D_GLES3=1, for Gradle /PURHO3D_GLES3=1.

Builded for Android (arm64, armv7a) - https://yadi.sk/d/PYWhzveBu58epg
Please test on some devices.

In the builded version, there are no Lua and Lua scripts, and in the example 06_SkeletalAnimation.as added 70 point lights and deferred render path used. Here is a screenshot from the phone - CPU MTK Helio P60, GPU - Mali G72 MP3.

![Urho3D_gles3|690x318](upload://89osK5IkAgwxT5KffIWoO5JxBo1.png) 

After test I will PR it at main repo.

-------------------------

glitch-method | 2019-10-27 04:51:13 UTC | #2

this is great! and I really like your launcher. the ui is a bit small, but still functional. (I had to use back softkey to exit console, touch wouldn't register at the close button.)

are you planning to add an option for user data, like scripts/resources in /sdcard/urho3d/?

-------------------------

orefkov | 2019-10-27 05:28:31 UTC | #3

Launcher is not my work, it is stock Urho3D launcher. Later I will publish my own laucher, which I use for develop script games for Android.

-------------------------

Alibaba | 2019-10-31 05:04:52 UTC | #4

There seems to be a problem with shadows.

![Screenshot_20191030-104915|690x329](upload://ohtJDcNI2b0EZbIVreeLwMKh3k5.png) 
I test on VinSmart Active 1+ ( CPU: Snapdragon 660, GPU: Adreno 512)

-------------------------

orefkov | 2019-10-30 06:52:07 UTC | #5

Yes, a strange picture.
On my device, it’s like that.
![Screenshot_20191030-094121|690x318](upload://XMimnkb5u9q2TTysINXK3CcDtb.png)
Now, for optimization on mobile devices, shadows from distant objects are not drawn.
And for some reason you have a character far from the camera, not like mine.
Can you take a screenshot with the HUD turned on?

-------------------------

Alibaba | 2019-10-30 11:00:15 UTC | #6

Yes, 
![Screenshot_20191030-172658|690x329](upload://wZqknIrvxrR0OTy5gMCjCtC5BNf.png)

-------------------------

orefkov | 2019-10-30 20:17:41 UTC | #7

Confirm. On other my phone with Adreno same picture. I will investigate it.

-------------------------

orefkov | 2019-11-01 11:10:18 UTC | #8

I am not a very big specialist in OpenGL, so it took a couple of days to find the cause. As a result, it turned out that it was just necessary to set the GL_TEXTURE_COMPARE_MODE parameter to GL_COMPARE_REF_TO_TEXTURE for the shadowmap texture.

Now I corrected it, plus a few more edits - I activated the use of constant buffers in uniforms.glsl for tests, and corrected a few more minor errors. I’ll make a commit soon, but for now, using the same link https://yadi.sk/d/PYWhzveBu58epg, you can download a new build for testing.

Here I checked the shadows on Adreno:
![screen3|690x388](upload://k7bVZEhrJIMklDWtuDQxP90NY9b.jpeg) 

... In Mali:
![screen4|690x318](upload://4t0tFwYpThhCHOgceVQ05lRdwkR.jpeg) 

Even on the old weak Adreno 330, deferred rendering works (although not so fast, but for its power the scene is complicated)
![screen6|690x388](upload://jXGG0lNQHzoLDl6yR4Qrum1wXaY.jpeg) 

In general, according to https://developer.android.com/about/dashboards/index.html#OpenGL - OpenGL ES3.0-3.2 occupies about 80% of devices, it is strange that there is so little interest in adapting the engine for ES3. Using only ES2 now you will not achieve much on Android - there is no intansing, no ETC2 - the biggest problems.
I hope, with my improvements for ES3 and to improve interaction with Android (https://github.com/urho3d/Urho3D/pull/2538), the engine will be an excellent choice in the niche of creating Android games.

-------------------------

Alibaba | 2019-11-01 16:40:09 UTC | #9

Yeah, this is great ^^![Screenshot_20191101-204627|690x329](upload://l9ebGPUK25uE5WPDGvTnmZXDvXr.png)

-------------------------

orefkov | 2019-11-08 07:17:20 UTC | #10

By the way, I noticed that in terms of instancing on GLES3 Urho3D works better than Unity. In particular, Unity disables the use of instancing when working in GLES3 on the weak models of Adreno (330 and others, with the GL ES 3.0 driver), while on Urho3D, the instancing on these GPUs works. This is due to the fact that Unity uses the uniforms array for instancing and fetching from it through gl_instanceID, which does not work correctly on these drivers. Urho3D uses vertex buffers with instanced attributes and glVertexAttribDivisor. They work correctly on these GPUs, and in addition, they allow transferring a much larger number of instances per draw call than when using uniforms arrays.

-------------------------

weitjong | 2019-11-17 10:45:25 UTC | #11

Since the majority of the mobile devices support GLES3, should we enable the GLES3 build option by default?

-------------------------

elix22 | 2019-11-17 14:42:22 UTC | #12

Please read below ,
https://godotengine.org/article/abandoning-gles3-vulkan-and-gles2 

21.1% of the Android devices still support only GLES2
On some there is 3.x support but with some issues/bugs .
I think GLES2 should be the default configuration with the ability to enable GLES 3.x by using CC

-------------------------

weitjong | 2019-11-17 15:31:26 UTC | #13

Just to clarify. I am not planning to remove that build option. The "URHO3D_GLES3" build option stays. What I have in mind is to set its default to true for Android and iOS/tvOS, but user can still opt to explicitly disable it to get GLES 2 instead. Something like this in CMake build script.

```
cmake_dependent_option (URHO3D_GLES3 "Use GLES 3 instead of GLES 2 (Android/RPI/ARM/iOS/tvOS platforms only); default to true for Android and iOS/tvOS" "ANDROID OR IOS OR TVOS" ARM FALSE)
```

The GLES days for iOS/tvOS should be numbered. So if we exclude these two platforms, we left with Android. If you guys think that for Android it should not be defaulted to true too then we could simplify the above script.

```
cmake_dependent_option (URHO3D_GLES3 "Use GLES 3 instead of GLES 2" FALSE ARM FALSE)
```

-------------------------

elix22 | 2019-11-17 16:09:15 UTC | #14

My 2 cents , 
Currently the iOS/tvOS angle-metal-backend implementation   is not part of Urho3D , hopefully that will change in the near future.
So for now the configuration should remain common to both Android , iOS/tvOS 

[quote="weitjong, post:13, topic:5688"]
cmake_dependent_option (URHO3D_GLES3 "Use GLES 3 instead of GLES 2 (Android/RPI/ARM/iOS/tvOS platforms only); default to true for Android and iOS/tvOS" "ANDROID OR IOS OR TVOS" ARM FALSE)
[/quote]

-------------------------

orefkov | 2019-11-17 16:41:09 UTC | #15

What scholastic disputes do you have? Can you immediately name the game in the playmarket on the Urho3D engine? What about two? This is what should really serve as a sad subject for discussion, and not what option to default. Game developers will be able to solve this issue for themselves. But where are they? No matter how beautiful the engine is, but without the games made on it, the meaning disappears in it.
If there are no games, then it makes no difference whether the developers DO NOT make games on GLES2 or GLES3.

-------------------------

elix22 | 2019-11-17 17:17:50 UTC | #16

I really don't have any disputes with anyone .
I really would like this amazing game engine to prosper and still be relevant in the future  .

I agree with you , there are not so much developers that are making games with this amazing engine .
Chicken and the egg problem :
Developers will not invest time in making games with a game engine that is rarely maintained. 
Developers will not maintain an game engine that is rarely being used to develop games.

I think you made a great job with GLES3 .
With my limited resources I am trying to bring Metal to iOS/macOS .
Hopefully more developers will join in the future ...

-------------------------

weitjong | 2019-11-17 23:34:18 UTC | #17

I don’t want to answer your other question here, but as for why I care for which options be made default matter for me because I am a CLI user. The default should be set to what makes the most sense. Whether the engine takes off or not, I do not really care much. If we do, we would probably stop long time ago.

-------------------------

JTippetts | 2019-11-19 03:51:46 UTC | #18

The engine is being used a bit more than would be apparent looking at these forums or the contribution activity lately. I know personally of three potential commercial projects in the works (not mine), plus I know of a high school teacher who is using it to teach students. Please, you guys, don't be discouraged by the seeming lack of interest. Urho3D is a project that has a great deal of merit and potential, and a larger audience than it seems, and it has really always been that way. Rest assured that everyone here is appreciated for their efforts by people, such as myself, who don't necessarily have the time to contribute to the codebase or the forums that much anymore.

-------------------------

rku | 2019-11-21 08:48:57 UTC | #19

I worked on [big commercial game](https://play.google.com/store/apps/details?id=com.playwing.instantwar) that was built on urho3d fork. Game was GLES3 initially, but they insisted on implementing GLES2 support in order to expand possible audience. GLES may be a minority, but it is not insignificant minority yet. With that said - it probably does not matter which is default. GLES3 can be default if only to get more performant and prettier samples..

Edit: I should note that by saying *big* i meant size of the project, not necessarily it's popularity.

-------------------------

orefkov | 2019-11-20 09:53:34 UTC | #20

Hi, I was started my GLES3-work based on your fork :slight_smile:
For me personally, the most important thing from GLES3 is the guaranteed instancing and ETC2 textures. In my game was up to 608  simultaneous objects of the same type in the frame, and in new version it  there can be up to 860, and without instancing I had to go to different tricks in order to realize this. Although I also have to do this and with instancing :)

-------------------------

rku | 2019-11-20 09:57:07 UTC | #21

Awesome! I only implemented bare minimal functionality i needed. Thanks for finally finishing it properly :+1:

-------------------------

extobias | 2019-11-20 23:06:23 UTC | #22

hey rku, can we know the name of the game?

-------------------------

QBkGames | 2019-11-21 06:16:42 UTC | #23

[Planetoid Escape](https://discourse.urho3d.io/t/planetoid-escape-sci-fi-survival-fps-wip/5110) is also a fairly big project, which I'm planning to eventually commercialize (hopefully sometimes next year), so that could count as commercial project under development using Urho.

I'm also interested in GLES3 mostly for Oculus Quest. For puzzle type games for the mobile market I'd probably stick to GLES2 to maximize compatibility.

-------------------------

orefkov | 2019-11-21 06:52:04 UTC | #24

Im now release my old game https://discourse.urho3d.io/t/brick-break-andriod-mobile-game/4602 on GLES3. The game has a lot of small identical elements in the frame, and without instancing it is difficult to make it.

-------------------------

rku | 2019-11-21 08:49:13 UTC | #25

I updated my post with a link.

-------------------------

weitjong | 2020-01-18 10:39:38 UTC | #26

I have requested help in our GitHub issue tracker but I have not getting the help I need. The original PR seems to break the Web platform, all the samples have runtime error and just displaying blank canvas. I need help from others to confirm my observation because my local test branch is not clean and it could be my own doing, and also help to fix the issue if it is indeed a regression issue.

-------------------------

Modanung | 2020-01-18 12:16:50 UTC | #27

https://github.com/urho3d/Urho3D/pull/2536

-------------------------

Modanung | 2020-01-18 12:24:25 UTC | #28

[quote="orefkov, post:15, topic:5688"]
If there are no games, then it makes no difference whether the developers DO NOT make games on GLES2 or GLES3.
[/quote]

@orefkov 
https://discourse.urho3d.io/t/urho3d-project-is-listed-on-the-first-page-search-result/5810

-------------------------

JTippetts1 | 2020-01-18 15:32:53 UTC | #29

I kicked off a build before I left for work this morning, I will let you know how it goes tonight.

-------------------------

weitjong | 2020-01-18 16:32:10 UTC | #30

I got it working again. I have to revert back one line of change from the PR to what it was before.

```
diff --git a/bin/CoreData/Shaders/GLSL/Uniforms.glsl b/bin/CoreData/Shaders/GLSL/Uniforms.glsl
index b823be7f84..2ee0bcaafd 100644
--- a/bin/CoreData/Shaders/GLSL/Uniforms.glsl
+++ b/bin/CoreData/Shaders/GLSL/Uniforms.glsl
@@ -48,7 +48,7 @@ uniform mat4 cZone;
 #ifdef COMPILEPS
 
 // Fragment shader uniforms
-#ifdef MOBILE_GRAPHICS
+#ifdef GL_ES
     precision mediump float;
 #endif
 ```

Still, I become not that confident with all the proposed changes as the result. i.e. I think we need more eyeballs to validate this PR.

-------------------------

weitjong | 2020-01-19 06:11:01 UTC | #31

Let me know if my approach is wrong. As I understand the GLES 3 is more or less equivalent to WebGL 2. So, in my test branch I have added (experimental) build option to enable WebGL 2 for Web build. It builds cleanly now but runtime still gives error. I intend to "fix" the current GLES 3 implementation by fixing the runtime errors from WebGL2 build that I observed. Hopefully I do not cause further regression issue to GLES 3 on other platforms in the process. This is far beyond my comfort zone.

-------------------------

JTippetts | 2020-01-20 23:03:58 UTC | #32

I built the orefkov_GLES3_Support branch both with EMSCRIPTEN_WEBGL2 and without, and with the fix to change MOBILE_GRAPHICS to GL_ES in Uniforms.glsl, I have no runtime errors. Without that change, I get runtime errors on both builds. GraphicsDefs.h considers WebGL to be a Desktop platform instead of a mobile platform and MOBILE_GRAPHICS isn't being set for WebGL builds, so no float precision is being specified unless, as your recent commit does, the float precision specifier is based on GL_ES instead of MOBILE_GRAPHICS.

-------------------------

weitjong | 2020-01-21 01:07:07 UTC | #33

I totally agree with your conclusion. For Web platform, I think it is also difficult to draw the line between DESKTOP_GRAPHICS and MOBILE_GRAPHICS. The same WebGL/2 API might have slightly different implementation between mobile browser and desktop browser, for example.

-------------------------

