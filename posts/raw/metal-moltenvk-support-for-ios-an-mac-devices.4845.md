elix22 | 2019-01-22 00:30:55 UTC | #1

HI all.
As most of you know , Apple announced about deprecation of OpenGL & OpenGL-ES on its devices.
There is still a grace period that allows to use them , but its matter of time until they will pull the plug.
As a result Urho3D won't run on Apple devices anymore in the future.

The last couple of weeks I was working on a solution by using 2 open source libraries :

1 - **ANGLE** ( *Almost Native Graphics Layer Engine* ) , an open source BSD licensed abstraction developed by Google , basically an OpenGL-ES abstraction running on top of DirectX/Vulkan backends.

2- **MoltenVK** , its an Vulkan abstraction running on top of Metal on iOS and Mac , Appache 2 license , developed by The Brenwill Workshop Ltd .

Both of these libraries are actively developed by big cooperates  and there are daily fixes and improvements.

I completed the work successfully .
So basically it's an OpenGL-ES running on top of Metal , using liberal open source libraries.
You can find the code in : **https://github.com/elix22/Urho3D/tree/angle-vulkan**
It's on the angle-vulkan branch.
You can clone it using : **git clone -b angle-vulkan https://github.com/elix22/Urho3D.git**

There are 4 scripts that will create for you the Xcode projects :
cmake_ios-metal.sh - will create an iOS Xcode project using the metal backend (my work)
cmake_ios-gles.sh - will  create an iOS Xcode project using the default OpenGL-ES backend
cmake_xcode-metal.sh  - will create an Mac Xcode project using the metal backend (my work)
cmake_xcode-gl.sh -  will  create an Mac Xcode project using the default OpenGL-ES backend

These are all debug builds .
In order to get the best performance you will have to modify the scheme to release build configuration and also disable metal API validation .

All the samples seem to work  on my iPad .
On my Mac all are working except 10_RenderToTexture.
The performance is great , getting stable 60 FPS on my  iPAD in release configuration. 

Known issues : 
- On my Mac , once exiting from the app , it crashes , I will try to provide a fix for that in the coming weeks.
- Shadows are disabled due to missing functionality on Angle side, needs some investigation
- I disabled HDPI for now , not working properly , it needs more investigation.

I plan to write a blog in the coming weeks describing the inner workings of the implementation to help other developers continue improving this solution and to incorporate it into other game engines.

You are encouraged to try it ( a specially on iOS devices) and provide some feedback .


Enjoy !

-------------------------

Leith | 2019-01-22 05:10:42 UTC | #2

I don't have any Apple devices (which is strange because I worked there for a while) but the value of a vulkan wrapper extends to other devices. This is interesting.

[I quit working at That Fruit Company due to a four hour commute, my car breaking down and taking three weeks to remedy, and finally, a nasty accident involving facial reconstruction - it was not my best year to be honest]

-------------------------

johnnycable | 2019-01-22 16:18:12 UTC | #3

Thanks, I'll give them a round of test on the first free time i find.

-------------------------

johnnycable | 2019-01-23 19:10:25 UTC | #4

First test on Mac Os:

> 02_HelloGUI 
> [Wed Jan 23 20:05:42 2019] INFO: Opened log file /Users/max/Library/Application Support/urho3d/logs/HelloGUI.log
> [Wed Jan 23 20:05:42 2019] INFO: Created 1 worker thread
> [Wed Jan 23 20:05:42 2019] INFO: Added resource path /usr/local/Urho/anglevk/Urho3D/build-xcode-metal/bin/Data/
> [Wed Jan 23 20:05:42 2019] INFO: Added resource path /usr/local/Urho/anglevk/Urho3D/build-xcode-metal/bin/CoreData/
> [Wed Jan 23 20:05:42 2019] INFO: Added resource path /usr/local/Urho/anglevk/Urho3D/build-xcode-metal/bin/Autoload/LargeData/
> [mvk-info] MoltenVK version 1.0.28. Vulkan version 1.0.95.
> 	The following Vulkan extensions are supported:
> 		VK_KHR_16bit_storage v1
> 		VK_KHR_8bit_storage v1
> 		VK_KHR_bind_memory2 v1
> 		VK_KHR_dedicated_allocation v3
> 		VK_KHR_descriptor_update_template v1
> 		VK_KHR_get_memory_requirements2 v1
> 		VK_KHR_get_physical_device_properties2 v1
> 		VK_KHR_image_format_list v1
> 		VK_KHR_maintenance1 v2
> 		VK_KHR_maintenance2 v1
> 		VK_KHR_maintenance3 v1
> 		VK_KHR_push_descriptor v2
> 		VK_KHR_relaxed_block_layout v1
> 		VK_KHR_sampler_mirror_clamp_to_edge v1
> 		VK_KHR_shader_draw_parameters v1
> 		VK_KHR_shader_float16_int8 v1
> 		VK_KHR_storage_buffer_storage_class v1
> 		VK_KHR_surface v25
> 		VK_KHR_swapchain v70
> 		VK_KHR_swapchain_mutable_format v1
> 		VK_EXT_shader_viewport_index_layer v1
> 		VK_EXT_vertex_attribute_divisor v3
> 		VK_MVK_macos_surface v2
> 		VK_MVK_moltenvk v12
> 		VK_AMD_negative_viewport_height v1
> 	Created VkInstance with the following Vulkan extensions enabled:
> 		VK_KHR_surface v25
> 		VK_MVK_macos_surface v2
> [mvk-info] GPU device:
> 		model: Intel Iris Graphics
> 		type: Integrated
> 		vendorID: 0x8086
> 		deviceID: 0x0a2e
> 		pipelineCacheUUID: 00000000-0000-0000-0000-27130000272C
> 	supports the following Metal Feature Sets:
> 		macOS GPU Family 1 v3
> 		macOS GPU Family 1 v2
> 		macOS GPU Family 1 v1
> [mvk-info] Created VkDevice to run on GPU Intel Iris Graphics with the following Vulkan extensions enabled:
> 		VK_KHR_swapchain v70
> [mvk-info] Created 2 swapchain images with initial size (1024, 768).
> [Wed Jan 23 20:05:42 2019] INFO: Adapter used Google Inc. ANGLE (Vulkan 1.0.95(Intel Iris Graphics (0x00000A2E)))
> [Wed Jan 23 20:05:42 2019] INFO: Set screen mode 1024x768 windowed monitor 0
> [Wed Jan 23 20:05:42 2019] INFO: Initialized input
> [Wed Jan 23 20:05:42 2019] INFO: Initialized user interface
> [Wed Jan 23 20:05:42 2019] INFO: Initialized renderer
> [Wed Jan 23 20:05:42 2019] INFO: Initialized engine
> [mvk-info] Shader library compilation succeeded with warnings (code 4):
> 
> Compilation succeeded with: 
> 
> program_source:92:12: warning: unused variable '_uiBlendIndices'
>     float4 _uiBlendIndices;
>            ^
> program_source:88:12: warning: unused variable '_uiNormal'
>     float3 _uiNormal;
>            ^
> program_source:95:11: warning: unused variable '_uiObjectIndex'
>     float _uiObjectIndex;
>           ^
> program_source:91:12: warning: unused variable '_uiBlendWeights'
>     float4 _uiBlendWeights;
>            ^
> program_source:94:12: warning: unused variable '_uiCubeTexCoord1'
>     float4 _uiCubeTexCoord1;
>            ^
> program_source:90:12: warning: unused variable '_uiTangent'
>     float4 _uiTangent;
>            ^
> program_source:89:12: warning: unused variable '_uiTexCoord1'
>     float2 _uiTexCoord1;
>            ^
> program_source:93:12: warning: unused variable '_uiCubeTexCoord'
>     float3 _uiCubeTexCoord;
>            ^
> 
> [mvk-info] Shader library compilation succeeded with warnings (code 4):
> 
> Compilation succeeded with: 
> 
> program_source:200:12: warning: unused variable 'flippedFragCoord'
>     float4 flippedFragCoord;
>            ^
> 
> [mvk-info] Shader library compilation succeeded with warnings (code 4):
> 
> Compilation succeeded with: 
> 
> program_source:200:12: warning: unused variable 'flippedFragCoord'
>     float4 flippedFragCoord;
>            ^
> 
> [mvk-info] Shader library compilation succeeded with warnings (code 4):
> 
> Compilation succeeded with: 
> 
> program_source:199:12: warning: unused variable 'flippedFragCoord'
>     float4 flippedFragCoord;
>            ^
> 
> Used resources:
> Textures/Ramp.png
> Textures/Spot.png
> Textures/FishBoneLogo.png
> Textures/UI.png
> Textures/UrhoDecal.dds
> Techniques/NoTexture.xml
> RenderPaths/Forward.xml
> UI/DefaultStyle.xml
> Textures/UrhoIcon.png
> Fonts/Anonymous Pro.ttf
> Shaders/GLSL/Basic.glsl
> 

It works.

![29|625x399](upload://j5DXd3zEQB69qpWiDYfxG9J1020.png)

:grinning:

-------------------------

Leith | 2019-01-24 06:20:13 UTC | #5

Sweet!
Please issue PR, so we can deal with any cross platform issues!

I have been looking forward to the benefits of Vulkan for such a long time.
This could trigger more work, since we can now render using multiple threads etc.
But the return is worth the effort.

-------------------------

johnnycable | 2019-01-24 11:17:13 UTC | #6

Basically this seems to be ok on Mac Os. Open points:
- I've tested on 10.13.6, still not upgraded to Mojave. To compile, I had to change two files:
Source/ThirdParty/MoltenVK/MoltenVK/MoltenVK/GPUObjects/MVKDevice.mm, changed MTLFeatureSet_macOS_GPUFamily1_v4 to v3
Source/ThirdParty/MoltenVK/MoltenVK/MoltenVK/Vulkan/mvk_datatypes.mm, changed MTLTextureType2DMultisampleArray to MTLTextureType2DMultisample
This gave no error apparently.
- all example works with the exception of 42_PBR, which shows blank. That was expected
- within some examples, mouse coordinates are off someway. Probably the retina screen adaptation. This is nasty.
- the system is in general WAY faster; some examples are incredibly speedy;
- random crashes happen when exiting. This is the recurrent log:

> Thread 1 Crashed:: Dispatch queue: MoltenVKQueue-0-0-0.0-Dispatch
> 0   com.apple.driver.AppleIntelHD5000GraphicsMTLDriver	0x00007fff48b8ad7a IGAccelRenderCommandEncoder::setVertexBuffer(MTLIGAccelBuffer*, unsigned int, unsigned int) + 120
> 1   11_Physics                    	0x000000010bfde0aa MVKGraphicsResourcesCommandEncoderState::encodeImpl() + 346
> 2   11_Physics                    	0x000000010bfdab2f MVKCommandEncoder::finalizeDrawState() + 63
> 3   11_Physics                    	0x000000010bfccee5 MVKCmdDrawIndexed::encode(MVKCommandEncoder*) + 21
> 4   11_Physics                    	0x000000010bfd9fac MVKCommandEncoder::encodeSecondary(MVKCommandBuffer*) + 44
> 5   11_Physics                    	0x000000010bfd0aeb MVKCmdExecuteCommands::encode(MVKCommandEncoder*) + 43
> 6   11_Physics                    	0x000000010bfd97f2 MVKCommandBuffer::submit(MVKQueueCommandBufferSubmission*) + 370
> 7   11_Physics                    	0x000000010c00fe6b MVKQueueCommandBufferSubmission::execute() + 59
> 8   11_Physics                    	0x000000010c00f0dc invocation function for block in MVKQueue::submit(MVKQueueSubmission*) + 28
> 9   libdispatch.dylib             	0x00007fff76ae65fa _dispatch_call_block_and_release + 12
> 10  libdispatch.dylib             	0x00007fff76adedb8 _dispatch_client_callout + 8
> 11  libdispatch.dylib             	0x00007fff76af3217 _dispatch_queue_serial_drain + 635
> 12  libdispatch.dylib             	0x00007fff76ae6166 _dispatch_queue_invoke + 373
> 13  libdispatch.dylib             	0x00007fff76af3f0d _dispatch_root_queue_drain_deferred_wlh + 332
> 14  libdispatch.dylib             	0x00007fff76af7d21 _dispatch_workloop_worker_thread + 880
> 15  libsystem_pthread.dylib       	0x00007fff76e2ffd2 _pthread_wqthread + 980
> 16  libsystem_pthread.dylib       	0x00007fff76e2fbe9 start_wqthread + 13

Everything seems quite usable anyway. Setting off with retina issues and exiting crashes should do for a good PR.

Now I'll proceed testing on Ios. :grinning:

-------------------------

elix22 | 2019-01-24 19:20:40 UTC | #7

[johnnycable](/u/johnnycable)
Thanks for your detailed report .
I am currently very bussy on some development stuff I doing at my work so my answers will be delayed.
You are right , I forgot to mention that in order to compile the code , the minimal OS version
Should be 10.14 (Mojave).

MoltenVK is the only component that I didn't modify , 
I guess your workarounds are ok to validate the functionality , but for an actual fix I think an issue 
should be submitted against MoltenVK  , MoltenVK dev team should provide a solution for OS < 10.14

I will address the other issues once you will complete your validation on iOS..

Thanks again for your help.

-------------------------

elix22 | 2019-01-24 23:37:11 UTC | #8

[johnnycable](/u/johnnycable)
Disregard my previous statement .
You can use version 10.13.6 (High Sierra)
To fix the compilation errors (missing enums) , update only Xcode to latest version 10.1 
It works for me.

-------------------------

Leith | 2019-01-25 03:36:24 UTC | #9

With respect to the 42_PBR example, I have only managed to run it once on Linux, without it turning up black - I am not sure why, as no errors were reported. Something is very wrong in there.

-------------------------

johnnycable | 2019-01-25 10:21:36 UTC | #10

[quote="elix22, post:8, topic:4845"]
To fix the compilation errors (missing enums) , update only Xcode to latest version 10.1
[/quote]

I was suspecting that.
Regarding Ios, I get:

> /usr/local/Urho/anglevk/Urho3D/Source/ThirdParty/MoltenVK/MoltenVK/MoltenVK/API/mvk_datatypes.h:336:1: 'MTLPrimitiveTopologyClass' is unavailable: not available on iOS

possibly the same problem?
I have to backup before I can upgrade. It's going to take a couple of days.

-------------------------

elix22 | 2019-01-25 22:05:49 UTC | #11

[quote="johnnycable, post:10, topic:4845"]
‘MTLPrimitiveTopologyClass’ is unavailable: not available on iOS
[/quote]


Yep , Xcode 10.1 will fix it.

I fixed the issues you mentioned , I pushed them to angle-vulkan branch.
Also I wrote an short howto in the wiki tab

-------------------------

migueldeicaza | 2019-01-29 14:46:52 UTC | #12

This is incredible!   A fantastic contribution.

Thank you!

-------------------------

elix22 | 2019-01-30 06:55:02 UTC | #13

Thanks for the kind words Miguel.
Nice to hear from a famous Software Guru.

Anyone please share your impressions , a specially if you ran it on any iOS device
I am very curious to know how it runs on various iOS devices in release build configuration
(I have only my 6 Gen. iPad to verify it)

-------------------------

johnnycable | 2019-01-30 12:17:37 UTC | #14

Upgraded Xcode and re-run the Mac Os tests again.
Everything generally appears to be fine. No more exit crashes, speed is ok. No more coords/mouse problems.

Latest finds:
10_rendertotexture doesn't render anything inside the wall:

![10_RenderToTexture|654x500](upload://svKiDt2gz9dHwZuyL6DTzbYucQU.png) 

the following two are not probably render-related. Anyway:

15_Navigation shows jagged lines on some objects. As it's the usual resource, could be a demo bug:

![15_Navigation|658x500](upload://yp86qbBCUzaRXroDrQqPSHmfeEM.png) 

50_Urho2dplatformer some enemies are invisible (but they kill you on contact). Again, could be a demo bug. If someone can confirm...

![50_Urho2dPlatformer|614x500](upload://s6Sgs5mZu52m1rCBsBwFIAQ9fsP.png)

So, almost everything is working. 
Wonderful! Great job!

-------------------------

elix22 | 2019-01-30 17:45:29 UTC | #15

johnnycable
Thanks for the update.

10_rendertotexture - Known  issue on Mac , works fine on my iPad, I might work on it during the weekend if I will have some spare time.

15_Navigation - Are you referring to the yellow lines ?
It's debug geometry , just press space to remove it.

50_Urho2dplatformer - Demo bug , happens also on the default OpenGL/ES backend.


Did you have the time to run it on iOS device ?

-------------------------

Modanung | 2019-01-30 18:42:31 UTC | #16

[quote="elix22, post:15, topic:4845"]
It’s debug geometry , just press space to remove it.
[/quote]

I think he was referring to what seems like [z-fighting](https://en.wikipedia.org/wiki/Z-fighting) between the mushrooms and the ground.

-------------------------

elix22 | 2019-01-30 19:45:58 UTC | #17

[quote="Modanung, post:16, topic:4845"]
I think he was referring to what seems like [z-fighting](https://en.wikipedia.org/wiki/Z-fighting) between the mushrooms and the ground.
[/quote]


Thanks for clarifying :slight_smile:
Yep , I verified it , definitely  z-fighting .
Needs some debugging.

-------------------------

johnnycable | 2019-01-30 21:13:22 UTC | #18

Yes, I was referring to z-fighting indeed.
Now I'm going to test on Ios

-------------------------

johnnycable | 2019-01-31 11:45:05 UTC | #19

Tested first 10 examples. 1-6 and 8 are ok. 07 - 09 - 10 crashed for various reasons.
07 shows increasing resources consumption and falling fps. Probably leaks and in the end crashes. The VK_Format error is recurrent.

![07_billboards_leaks|690x426](upload://iFQJiWi7njQHsbyxUzbtOYdjTav.png) 

<a class="attachment" href="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/d1c32d758e4573be5fe856f3fcc569fdb55c834d.csv">07_billboards_xcode_log.csv</a> (613.2 KB)

-------------------------

johnnycable | 2019-01-31 11:42:31 UTC | #20

09 and 10 crashes for the same reason, some depth stencil conflict apparently. 10 crashes on the spot.

![09_multipleviewport_depthstencil|690x431](upload://nvrdEUjigTqMvE29wDYeHBf9LpB.png) 

![10_rendertotexture_depthstencil|690x431](upload://3piRfpRzk8QWqFpYFcJqF6oia8C.png) 

<a class="attachment" href="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/102f481c4d04ee3e77ac51e371d783d83c920cf7.csv">10_rendertotexture_xcode_log.csv</a> (7.4 KB)
 
HTH

-------------------------

elix22 | 2019-01-31 12:42:52 UTC | #21

Thanks
For the update  .
I will take a look at the logs during the weekend .

- What device are you using ?
-You can try disabling the crash for now in your Xcode : 
 **Menu : Product -> Scheme -> Edit Scheme -> Run** 
Select Options tab and disable Metal API Validation.
**Options -> Metal API Validation : Disabled**

-------------------------

elix22 | 2019-02-02 21:43:13 UTC | #22

I fixed  samples 09 & 10
Sample 07 - Needs more time to debug , will work on it next weekend

In addition :
Since Google supports Windows Angle Vulkan backend officilly (and not supporting Metal)
I added Windows Vulkan backend support using the same development branch (angle-vulkan)  .
Windows would be used only for reference , and finding bugs on the Angle side .
So people that have a Windows machine and would like to try it , please read the WIKI on my Github

-------------------------

Leith | 2019-02-03 12:45:31 UTC | #23

You're on a roll :) Me too!! Most stuff is just working how I expect, and I'm asking less stupid questions :smiley: I'm hoping to be able to build your code soon

-------------------------

johnnycable | 2019-02-04 18:21:07 UTC | #24

MGKL2TY/A iPad AIR 2 64gb wifi 2014, Ios 11.4.1

Samples 9 and 10 are ok now. :smiley:

Here comes the biggest one.

11-12-13 Physics - Every time objects move, frame rate drops to 3-4 fps. :open_mouth:

ex 11 when the crates settles and when you throw at them 3 fps. 
ex 12 it takes 20 seconds for crates to start rolling down.
ex.13 7 fps taking down the guys

Did I miss some building step, maybe?

EDIT: False alarm.
I tried latest Ios build from master, and it has the same problems... :disappointed_relieved::disappointed_relieved::disappointed_relieved:

-------------------------

elix22 | 2019-02-04 20:24:34 UTC | #25

It's ok :slight_smile:  

Just run release build configuration , you will see 60 FPS .


1. Choose Legacy Build System .

> Menu : File -&gt; Project Settings … -&gt; Build System : Legacy Build System

2. Edit the project Scheme , choose the run action.

> Menu : Product -&gt; Scheme -&gt; Edit Scheme -&gt; Run

3. Select the Info tab , set build configuration to Release.

> Info -&gt; Build Configuration : Release

4. Still in the Info tab , Debug executable checkbox should be unchecked.

> Info -&gt; Debug executable : unchecked

5. Select Options tab and disable Metal API Validation.

> Options -&gt; Metal API Validation : Disabled

-------------------------

Leith | 2019-02-06 05:18:08 UTC | #26

I had a similar problem in my first few days on Urho, frame rate would go below 1FPS - it could take several seconds for each frame! It had something to do with contacts, and only happened with debug draw enabled, I will try to remember the exact details.

-------------------------

johnnycable | 2019-02-06 16:38:47 UTC | #27

Ok. Basically it has to run in release mode.
Physics is ok. Steady 60 fps. :open_mouth:

-------------------------

johnnycable | 2019-02-07 20:36:56 UTC | #28

Aaargh :scream::scream::scream:  I'm stuck with the dreaded

> The request was denied by service delegate (SBMainWorkspace) for reason: Unspecified

I've gotta to clean everything and restart... f$%£*ing Apple... :confounded::confounded::confounded:

-------------------------

johnnycable | 2019-02-08 20:43:29 UTC | #29

@elix22 going forward after cleaning everything
looks like XCode doesn't like switching from debug builds to release and vice-versa...
15_Navigation, 18_CharacterDemo, 19_VehicleDemo are ok.
:test_tube::test_tube::test_tube:

-------------------------

elix22 | 2019-02-08 22:06:18 UTC | #30

[quote="johnnycable, post:29, topic:4845"]
looks like XCode doesn’t like switching from debug builds to release and vice-versa…
[/quote]


Yes I am aware of this , seems to be an Xcode bug.
Initially release build was failing for me , I googled it and people were reporting the same issue .
The only thing that fixed it for me was choosing the Legacy build system .
**Menu : File -&gt; Project Settings … -&gt; Build System : Legacy Build System**

So my advice would be to use the legacy build system for both debug and release.

-------------------------

Leith | 2019-02-09 09:35:09 UTC | #31

i quit working for That Fruit Company, but I can't talk about it for a while

-------------------------

elix22 | 2019-02-11 16:55:49 UTC | #32

[quote="johnnycable, post:19, topic:4845"]
07 shows increasing resources consumption and falling fps
[/quote]

I had some spare time so I debugged this issue , it appears to be an angle-vulkan bug .
I communicated that to Angle development.
An issue was filled .and will be fixed  , I will integrate it once the fix will be provided .

You can follow my  discussion with the Google guys on this https://groups.google.com/forum/#!topic/angleproject/D2GNJ7wB1HA

Issue link 
https://bugs.chromium.org/p/angleproject/issues/detail?id=3143

-------------------------

johnnycable | 2019-02-11 20:37:19 UTC | #33

24_Urho2dSprite and 25_Urho2dParticle are ok.
23_Water has problems. Even in release mode and without debug, average frame rate is stuck around 45...

Read about the issue. What a nuisance. Memory hog calls for sure rejection from the app store... :confused:

-------------------------

johnnycable | 2019-02-14 18:19:58 UTC | #34

Argh, finally found some time to go on...

27_Urho2DPhysics,28_Urho2DPhysicsRope,30_LightAnimation,31_MaterialAnimation,32_Urho2DConstraints are all ok

33_Urho2DSpriterAnimation there's no physical button to test animations, rendering looks ok

34_DynamicGeometry
looks ok. Only the center triangle is all black. My mistake, or was it lightened?

20_HugeObjectCount - totally broken
759476 tris, 62339 batches, 3fps :open_mouth:

-------------------------

elix22 | 2019-02-16 07:35:44 UTC | #35

> 07 shows increasing resources consumption and falling fps

I fixed it for now  (on my branch) ,specific  use case in which multiple non-directional lights are moving in different directions.
Once Angle will provide a more general fix for the Scissor test issue  then I will revert my fix.

> 23_Water has problems. Even in release mode and without debug, average frame rate is stuck around 45…

Yep  , in this scenario it performs worse than the default legacy OpenGL/ES .
 Current phase is to make it all functional , we didn't reach the optimization phase yet.

> 20_HugeObjectCount - totally broken
759476 tris, 62339 batches, 3fps :open_mouth:

Did you try it in release build configuration ?
This specific sample is a nice performance marker indicator but no more than that , it's not a valid use case in any game .
If anyone is making a mobile game that has tens of thousands of draw-calls each frame than something is wrong with the game design not the game engine.

-------------------------

Leith | 2019-02-16 08:31:42 UTC | #36

Something is wrong with the culling, is more likely - I take it that the Huge Object Count sample does not cull by visibility, and certainly does not attempt to cull by occlusion. The former would make sense and cost little, but the latter makes no sense and costs a lot.

-------------------------

johnnycable | 2019-02-16 13:15:43 UTC | #37

[quote="elix22, post:35, topic:4845"]
Did you try it in release build configuration ?
[/quote]

Yes, I disabled molten debug and used release conf.
I think you have a point here - probably the 62339 batches don't fit the ipad. Tris count is not so high - I've loaded multi million models some time ago inside Urho on this ipad with apparently no slow down...
I'm going to update the branch and retest 07...

-------------------------

Leith | 2019-02-17 03:30:37 UTC | #38

Are we using gpu instancing? If we were, the batch count would be a lot lower...

-------------------------

johnnycable | 2019-02-17 14:17:36 UTC | #39

[quote="Leith, post:38, topic:4845, full:true"]
Are we using gpu instancing? If we were, the batch count would be a lot lower…
[/quote]

I don't have the slightest idea...

-------------------------

Leith | 2019-02-18 08:18:31 UTC | #40

when we want to draw ten thousand of the same thing, gpu instancing offers us a way to set up a buffer full of instance transforms, and make one draw call to draw all the instances, so the number of batches comes down to how big a buffer we provided for our instance transforms (typically 4x4 matrices)
This helps batch count immensely, but we're really just moving the bottleneck from the cpu to the gpu, and it's not useful in a wide number of use cases, but its worth looking into for things like drawing grass

-------------------------

johnnycable | 2019-02-18 16:09:46 UTC | #41

[quote="Leith, post:40, topic:4845"]
when we want to draw ten thousand of the same thing, gpu instancing offers us a way to set up a buffer full of instance transforms, and make one draw call to draw all the instances, so the number of batches comes down to how big a buffer we provided
[/quote]

Of course I know that. I meant I don't know _in this case_

-------------------------

Leith | 2019-02-19 06:52:09 UTC | #42

According to the rendering docs (for opengl 3.2 or higher)
[quote]
The ARB_instanced_arrays extension is also checked for but not required; it will enable hardware instancing support when present.
[/quote]

It also says that gpu instancing will be used by default, when available. 
However, since you're not using opengl, this extension is obviously unavailable, and I must presume that is resulting in a crapload of small draw calls... I have no idea how Vulkan deals with gpu instancing, but I presume it's similar - I figure it should be fairly easy to hack the render pipe to deal with instancing on vulkan.

-------------------------

johnnycable | 2019-02-20 16:43:08 UTC | #43

@elix22

Gave another swing at it.
Testing on latest commit 763109e2d6f85d34b169e47f9663a7968f959396, Sat Feb 16 09:03:51 2019 +0200

07_Billboards
Still not ok. It's 50+ fps when few distant billboards are in sight, and drop to 40 when 3-4 are in sight at short range. Can go to 30 something if overloaded.

35_SignedDistanceFieldText
Example is not working functionally, no text.
Don't know if this is related, but gave an error:
failed to compile pixel shader Text(SIGNED_DISTANCE_FIELD TEXT_EFFECT_SHADOW)
ERROR: GL_OES_standard_derivatives : extension not supported

36_Urho2DTileMap
Appears ok. Example is not working functionally (doesn't create tiles)

37_UIDrag
Rendering ok.
Functional: Ipad multitouch doesn't work

38_SceneAndUILoad
Rendering ok.

39_CrowdNavigation
Rendering ok.

42_PBRMaterials
Not functional

44_RibbonTrailDemo
Rendering ok.

-------------------------

elix22 | 2019-02-20 16:59:56 UTC | #44

> 07_Billboards
Still not ok. It’s 50+ fps when few distant billboards are in sight, and drop to 40 when 3-4 are in sight at short range. Can go to 30 something if overloaded.

Is it release build ? 
My fix was about the memory  hog issue , meaning  after long time of running you should not see any FPS decrease and eventually crash (without doing anything )

> 37_UIDrag
Rendering ok.
Functional: Ipad multitouch doesn’t work

Yes I am aware about the multi-touch issue , it's not directly  related to my implementation , you will see it also if using the legacy OpenGL/ES rendering backend.
However I will debug it once I will have some spare time and provide a fix for that.

> 42_PBRMaterials
Not functional

We will have to wait until Angle-Vulkan will support OpenGL ES 3.0  to make it work

-------------------------

johnnycable | 2019-02-20 20:41:17 UTC | #45

[quote="elix22, post:44, topic:4845"]
Is it release build ?
My fix was about the memory hog issue , meaning after long time of running you should not see any FPS decrease and eventually crash (without doing anything )
[/quote]

Yes, release build. Probably I didn't notice this issue first time I tried... 
I'll let it run long time now, to profile the memory

[quote="elix22, post:44, topic:4845"]
However I will debug it once I will have some spare time and provide a fix for that.
[/quote]
Sorry, my mistake. Forgot to stress that "functional" it's just a  note I'm taking while testing which, unless it prevents rendering, can be ignored.
Basically "Rendering" is what we are interested in. For this reason, I'm skipping all examples not directly related to that, things like networking, and so on...

-------------------------

johnnycable | 2019-02-21 09:11:45 UTC | #46

I've checked signed distance field example for mac os

![35_SignedDistanceFieldText|553x381](upload://bn44P3UN6qQNDYQt1xLiAqvlimX.png) 

the text is not shown on ios version. Just to confirm the bug, I was unsure

-------------------------

elix22 | 2019-02-21 09:49:31 UTC | #47

Yep , looks like a bug .
Issues begin to pile up , I would suggest to track them on Github .
Feel free to open issues on my Github .
For this specific scenario  if possible please attach logs for both Mac and iOS

General note ,
The main components (Angle-Vulkan and MoltenVK ) are still under heavy development , so there are still some missing features (and some bugs) , I plan to merge the latest Angle branch once a month .

Since Angle-Vulkan is probably going to be officially supported in Android-Q 
My guess is that Angle-Vulkan will be feature complete by 08/2019 (possible release date of Android Q)

Hopefully we will have a production ready solution once Apple will remove OopenGL/ES from their platforms.

-------------------------

Leith | 2019-02-21 11:02:47 UTC | #48

you're throwing out a number 8/19, how many people are working on that branch? if you want help, I can boot back to windows any time, but shudder at the thought

-------------------------

elix22 | 2019-02-21 13:50:05 UTC | #49

> you’re throwing out a number 8/19, how many people are working on that branch?


The  08/2019 date is just a guess based on previous releases  of Android ,
I am referring to the Release date of Android Q , not to my implementation  .

On my branch its only me at my spare time during the weekends .

If you or anyone else has the knowledge  on the internals of Urho3D , SDL,   OpenGL/ES , Angle , Vulkan or MoltenVK  , you are more than welcome to contribute to this branch  (my branch) .
 
At the end it will benefit all the game developers that would like to continue to use Urho3D  and develop games for MacOS and iOS .
This is the only open source option to keep this engine alive in the future (at least for MacOS and iOS).

Google has unlimited resources  , you can follow the development on Angle and get some estimation on the amount of people that are working on it :slight_smile:

https://chromium-review.googlesource.com/q/project:angle/angle+status:open
https://chromium-review.googlesource.com/q/project:angle/angle+status:merged 

You can also read some stuff on Angle-Vulkan and Android Q release date
https://www.xda-developers.com/android-q-support-vulkan-backend-angle-game-development/
https://www.techradar.com/news/android-q

-------------------------

Leith | 2019-02-22 06:55:41 UTC | #50

Homework :slight_smile:

-------------------------

johnnycable | 2019-02-22 08:59:40 UTC | #51

Alright, I'll move bug reports to github.
Didn't know about google's, I'll have a look.

-------------------------

elix22 | 2019-07-23 05:12:01 UTC | #52

I had some time in the last few weeks .
So I merged up the latest Angle & MoltenVK code , I also fixed some issues.
Shadows are supported now but only on Windows and MacOS devices , for now it's not supported on iOS devices(I will have to debug it).
It's on my angle-20190712 branch on Github  https://github.com/elix22/Urho3D/tree/angle-20190712 
In order to try it ,checkout my angle-20190712 branch , to generate XCODE-Metal or Visual-Studio-Vulkan projects follow my WIKI page on Github.
It's still a W.I.P.  most of the features are working  and all demos are working but using it for a real project is not advised for now (you can use it on your own risk :slight_smile: ).

-------------------------

elix22 | 2019-10-21 15:20:56 UTC | #53

A very talented guy implemented a Metal backend for Angle (OpenGLES 2 to Metal abstraction/translation)
You can read more about it in this link https://groups.google.com/forum/#!topic/angleproject/ObYRiFxmIM0

I made a quick work during the weekend integrating it into my Urho3D  Github repo.
You can retrieve the source code :
**git clone -b angle-metal-backend https://github.com/elix22/Urho3D.git**

**2 scripts :**

**./cmake_xcode-metal.sh    will generate an Xcode MacOS project with all the samples** 

**./cmake_ios-metal.sh.  will generate an Xcode iOS project with all the samples**

Most of the samples do work (very well) , but not all of them ,
Currently  it's not mature as the Angle-Vulkan-MoltenVK implementation  , but I hope it will be more mature once Apple will remove OpenGL/ES from its products   .

-------------------------

elix22 | 2019-11-11 07:25:57 UTC | #54

All Samples are working smoothly now on the metal backend .
I tested it on numerous iOS devices.
Whoever wants to try it:
**git clone -b angle-metal-backend [https://github.com/elix22/Urho3D.git ](https://github.com/elix22/Urho3D.git)**
**./cmake_xcode-metal.sh will generate an Xcode MacOS project with all the samples**
**./cmake_ios-metal.sh. will generate an Xcode iOS project with all the samples**
**./cmake_ios-metal-12.4.sh. will generate an Xcode iOS 12.4 project with all the samples**

This could only happen due to the amazing work that was done by Le Hoang Quyen (A.K.A kakashidinho) , actually  implementing OpenGL ES 2.0 translation on top of the Metal backend.
See his work: https://github.com/kakashidinho/metalangle

-------------------------

johnnycable | 2019-11-11 16:20:10 UTC | #55

Yes Indeed.
End of a nightmare.

-------------------------

cosar | 2019-11-11 16:59:58 UTC | #56

Is this going to be integrated with Urho's mainline?

-------------------------

elix22 | 2019-11-12 06:57:42 UTC | #57

Yes I am going to submit a P.R.
First the branch needs a major cleanup and rebased 
To the latest Urho3D commit.
I am working on this only during the weekends so it will take several weeks.

-------------------------

elix22 | 2019-11-18 07:35:12 UTC | #58

Le Hoang Quyen (A.K.A kakashidinho) continues to make an amazing work on the metal-backend
Now there is full shadows support both on macOS and iOS 
and the also new instanced draw support .

Meaning 20_HugeObjectCount sample on the metal-backend outperforms the OpenGL/ES vanilla implementation by far  (at least on iOS devices).
I made several measurements 

=======================================
ANGLE-GLES2 on top of Metal backend
=======================================
20_HugeObjectCount sample
Release build configuration on all devices 

MBP 13’ 2017 (dual core Intel chip) , SW version 10.15.1 
Animation off  - 13 FPS ,  Group optimization enabled  60 FPS
Animation on  - 8 FPS ,    Group optimization enabled  26 FPS

iPhone 5s , SW version 12.4.2
Animation off  -  7 FPS ,   Group optimization enabled 9 FPS
Animation on  -   5 FPS ,   Group optimization enabled 7 FPS

iPhone 6s , SW version 13.2
Animation off  - 25 FPS ,   Group optimization enabled 60 FPS
Animation on  -  16 FPS ,   Group optimization enabled 36 FPS

iPhone 7 , SW version 13.1.3
Animation off  - 31 FPS ,  Group optimization enabled  60 FPS
Animation on  -  21 FPS ,  Group optimization enabled  60 FPS

iPad 6th generation , SW version 13.1
Animation off  -  28 FPS ,  Group optimization enabled 60 FPS
Animation on  -  20 FPS ,  Group optimization enabled  60 FPS

=======================================
GL/ES2 vanilla
=======================================
20_HugeObjectCount sample
Release build configuration on all devices 

MBP 13’ 2017 (dual core Intel chip) , SW version 10.15.1 
Animation off  -  35 FPS ,  Group optimization enabled 147  FPS
Animation on  -   21 FPS ,  Group optimization enabled  61 FPS

iPhone 5s , SW version 12.4.2
Animation off  -  4 FPS ,   Group optimization enabled 6 FPS
Animation on  -   4 FPS ,   Group optimization enabled 5 FPS

iPhone 6s , SW version 13.2
Animation off  - 13 FPS ,   Group optimization enabled 23 FPS
Animation on  - 10  FPS ,   Group optimization enabled 20 FPS

iPhone 7 , SW version 13.1.3
Animation off  - 17 FPS ,  Group optimization enabled  36 FPS
Animation on  -  13 FPS ,  Group optimization enabled  25 FPS

iPad 6th generation , SW version 13.1
Animation off  -  16 FPS ,  Group optimization enabled 30 FPS
Animation on  -  13  FPS ,  Group optimization enabled 24 FPS
 
 As usual you can try the latest :

**git clone -b angle-metal-backend** [ **https://github.com/elix22/Urho3D.git** 2](https://github.com/elix22/Urho3D.git)

**./cmake_xcode-metal.sh will generate an Xcode MacOS project with all the samples**

**./cmake_ios-metal.sh. will generate an Xcode iOS project with all the samples**

**./cmake_ios-metal-12.4.sh. will generate an Xcode iOS 12.4 project with all the samples**

-------------------------

johnnycable | 2019-11-19 20:05:43 UTC | #59

Aww, I can't find a few time to test it yet, I'm overburdened right now...
Hope this wk. Keep it up!

-------------------------

kakashidinho | 2019-11-20 14:16:46 UTC | #60

Hi, I'm the one doing the project MetalANGLE implementing OpenGL ES on top of Metal. Just noticed this topic now.
I'm doing this project for fun, originally I just want to reimplement MacOSX OpenGL on top of Metal since I think Apple purposely slowdown their GL implementations since Mojave release, all OpenGL games run very poorly on Mac compare to pre-Mojave. So in order to achieve that goal (might have a long way to go), I started with OpenGL ES reimplementation first. And this engine project is very helpful since it is a very good test bed for my OpenGL implementation. Thanks elix22 for doing and experimenting the integration.

I think the engine would benefit from Metal's faster draw calls compare to pure/vanilla OpenGL implementation if it chooses to replace vanilla OpenGL with MetalANGLE in future (of course if you want to).
That being said, there are couple of things I just want to let you know about the future of MetalANGLE. Currently it is almost 100% OpenGL ES 2.0 compliant (original ANGLE project has very comprehensive test suites to verify this). It will be full GLES 3.0 compliant in future, but some important features of GLES 3.0 are already implemented, and MetalANGLE can expose them via GLES 2.0 extensions. Currently, for examples, instanced draws, depth textures are already supported. I just want to know for this kind of engine, what are your most wanted GLES 3.0 features, so that I would like to give them higher priority to be implemented first.
Example GLES 3.0 features to be implemented:
- Multiple render targets. Useful for deferred rendering.
- 3D textures, 2D texture arrays.

-------------------------

elix22 | 2019-11-21 10:11:04 UTC | #61

[kakashidinho](https://discourse.urho3d.io/u/kakashidinho) welcome to the  Urho3D forum .
Your MetalANGLE implementation is priceless .
It's a win-win situation  ,
1 - From one side you are using the Urho3D as a test-bed for your metal back-end development 
2 - From the other side Urho3D gains  a metal back-end implementation .

M.R.T support  would be great .
In general , making 42_PBRMaterials  sample work would be great .

I am in the process of up-merging your back-end to Urho3D latest commit with HDPI enabled  (and some additional fixes on the Urho3D side ).
In the mid-term future I will add more samples created by the community over the years  .

Please note  that the Urho3D community is small compared to the other Game engines communities out there .
But it contains very talented people .
I think that there are a very small amount of developers in the Urho3D community  that are currently  developing for macOS and iOS , so please don't be discouraged if you won't receive much of a feedback  .
 
In any case I will provide you some support in my free time during the weekends .

Thanks for your amazing work .

-------------------------

johnnycable | 2019-11-24 19:49:44 UTC | #62

Just chimed in to tell I finally been able to do some beginning test today. Everything looks ok for now.
Thank you, guys.

-------------------------

johnnycable | 2019-12-30 16:58:54 UTC | #63

@elix22 @kakashidinho
I finally found the time to complete a round of testing on my Ipad. 
As a general note, everything appears to work correctly. Performances are good, and almost all example behaves normally as it should be. 
The hud shows everything runs on GL ES 2 thru metal, without instancing. Ios 12.4. Example have been run without Metal validation and debugging, release build.
Following are the only exceptions:

20 huge object counts is 10 fps speed.
12 physics stress test shows some hiccups, but never drops under 55 fps

These two are the only ones showing some performance drop. Instead, a strange thing happens on 23 water:



![shadows|690x411](upload://c6eFeMzSLMKDWZAG3DazlI4jjpW.jpeg) 

There's an inverted shadow reflection effect on the water surface from the boxes under the water level. The ones on the hill back there, for instance, are correct.
Mind, I don't know. This could be a bug related to the example itself...

I think that's all. I'm going to test next on Mac, but from what I've seen until now, this thing works ok. Thank you, guys.

-------------------------

kakashidinho | 2019-12-31 01:45:48 UTC | #64

From what I skimmed through the demo code, I think the water demo needs Desktop OpenGL's custom clip planes features to work correctly https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glClipPlane.xml. I might be wrong though.
This feature is not available in any version of OpenGL ES, it is certainly not available in metal either.

What is your ipad model anw? just curious.

-------------------------

johnnycable | 2020-01-01 15:40:09 UTC | #65

I see. This is expected behaviour then.
Ipad Air 2, MGKL2TY/A
Happy New Year

-------------------------

kakashidinho | 2020-03-04 16:36:14 UTC | #66

I just realized that the shader based clip plane can be made available to OpenGL ES via extension, and I have implemented it in MetalANGLE. The water demo should work correctly now, the boxes reflections should be clipped, you can test it once Elix merges the changes to his repo.

Additionally, these changes in Urho code should also enable the shader based clip plane feature on any mobile device supporting this extension (be it android or iOS, not just ANGLE). Previously Urho only enables this feature on Desktop GL3+ and ignore GLES.

-------------------------

elix22 | 2020-03-05 08:07:12 UTC | #67

I merged @kakashidinho work into my dev branch
Looks great (I think it outperforms even the commercial solutions :wink:  ).

**Please note that I am using a new branch:**
**git clone -b dev https://github.com/elix22/Urho3D.git**

The script folder contains 2 cmake script generating Xcode project with Angle-Metal backend enabled
**cmake_xcode_metal.sh & cmake_ios_metal.sh**

Or you can use the -DURHO3D_ANGLE_METAL=1 switch in your own script ignorer to enable the Angle-Metal backend

In addition this branch has additional samples made by @Lumak and @Modanung
I plan to add additional samples in the near future ...
Please pay attention to the licensing terms of each sample, specifically @Modanung's samples .  

I can't say enough about the amazing work that was done by @kakashidinho ,To me it is clearly the  best solution for those that would like to make games on  Apple devices now and in the future using "no strings attached" an open source game engine.
 
P.S.
I plan to open a new thread , this one became too long and some of it is already obsolete

-------------------------

