I3DB | 2019-02-21 14:48:43 UTC | #1

The difference between these two, codewise, is one runs [the hlsl water shader](https://github.com/urho3d/Urho3D/blob/05db29f6357ba1b409d7a61d04380f9d213dc62d/bin/CoreData/Shaders/HLSL/Water.hlsl#L1), and the other [the glsl water shader.](https://github.com/urho3d/Urho3D/blob/05db29f6357ba1b409d7a61d04380f9d213dc62d/bin/CoreData/Shaders/GLSL/Water.glsl#L1)

When run on D3D11 water is black. 
![PNG|545x500](upload://zDeDiGjT8EA9TKoVm99rnjUsTeT.jpeg) 

Here it is run on openGL with urhosharp bindings to winforms platform and the water is clear. 
![PNG|690x398](upload://dWocCJDkG0XGOgowpYabsESiNFg.jpeg)

Any ideas? Is it a transparent vs. black sort of issue or something in the shader?

EDIT:
There is a solution provided at end of this thread. To test that proposed solution, used the 1.7 urho3d version urhosharp distributes and tested on D3D11 win 10 x86 platform, and this did NOT solve the problem, nor provide any visible change. Water still painted black. Not solved.

-------------------------

Sinoid | 2019-02-20 03:59:35 UTC | #2

Please enumerate the machine specifications.

Also, the render is correct but the blend-states or buffer management are all kinds of messed up. Too many things can make this happen - if an AMD chip though, you're probably sunk on Win10 in GL.

-------------------------

Leith | 2019-02-20 06:49:52 UTC | #3

This is very strange - I suspect the issue is the refractColor term, but the code appears to have the same output for glsl and hlsl. I mean, you're getting reflections, so it's not the fresnel term, and it's not the reflection term, it has to be about refraction term by pure deduction. That's being sourced from an environmental map, so it looks like the problem is narrowed down to a failure on environmental probe to render to (I assume) a cubemap. This is boilerplate code, it should "just work". I agree, we need to see the hardware capabilities to figure out what's going wrong.
Also, I kind of like it - the water looks murky, it has more character than the "working" version.
It's absolutely not correct, but it looks nice :)

-------------------------

I3DB | 2019-02-20 17:43:45 UTC | #4

[quote="Sinoid, post:2, topic:4944"]
you’re probably sunk on Win10
[/quote]

Ran the UWP on two hardware platforms, but both running Win10. One is an intel powered desktop, the other platform is a hololens.

I've come across a number of anamolies in addition to this. For instance, shadows not working on hololens/UWP. [Another instance is the Outline.HLSL that was put up on another thread](https://discourse.urho3d.io/t/outline-v2/1766/46), where it was not working correctly.

At first I thought this was just hololens, but now have concluded it is D3D11 and the hlsl shaders. 
**Something is not correct here, and it's affecting numerous HLSL shaders**.

So here in this thread, I point out Water, Shadows, Outline ... all working INCORRECTLY on D3D11 platforms.

For shadows, here is UWP sample
![PNG|548x500](upload://jZtLphyTnqHDOLKCSrUttWclTf8.jpeg) 

Here is the winForms (opengl) sample
![WinFormsWithShadows|690x399](upload://eVVOqWYoRl8XYxZG4hy4su5aiT9.png)

-------------------------

I3DB | 2019-02-20 16:32:59 UTC | #5

[quote="Sinoid, post:2, topic:4944"]
Please enumerate the machine specifications.
[/quote]

[For hololens, here is a hardware breakdown](https://www.windowscentral.com/microsoft-hololens-processor-storage-and-ram).

For other platform:
Processor	Intel(R) Core(TM) i7-4770S CPU @ 3.10GHz, 3101 Mhz, 4 Core(s), 8 Logical Processor(s)
Adapter Description	Intel(R) HD Graphics 4600


Not sure what other info is useful. Let me know and I'll get it.

Best for me would be advice on how to troubleshoot further. This issue is readily repeatable for me ... just don't know what to look for next ... ???

-------------------------

I3DB | 2019-02-20 16:29:56 UTC | #6

[quote="Sinoid, post:2, topic:4944"]
you’re probably sunk on Win10 in GL.
[/quote]

Is that a statement of calm defeat? Not sure what you mean specifically.

-------------------------

I3DB | 2019-02-20 17:39:33 UTC | #7

[quote="Sinoid, post:2, topic:4944"]
the blend-states
[/quote]

Also, I could not get a NoTextureMultiply to work. The blend state always errors with this error:
System.Exception: Failed to create blend state (HRESULT 80070057).

The Decode: **`E_INVALIDARG` :**  One or more arguments are not valid ( `0x80070057` )

[I saw this error on another issue](https://discourse.urho3d.io/t/litsolid-ao-missing-vertex-element/4810/9), where the second UV map was missing. @lezak pointed out the underlying issue, the text of the message was different though, and it pointed out missing vertex elements, but this one doesn't have that just the blend state failure.

The result is shown, the NoTextureMultiply on UWP:
![PNG|690x227](upload://gsm4r4Leylknra2Zetkwqd4uYtO.jpeg) 

But on winForms looks like it works, and no errors:
![winFormsNoTextureMultiplyWorks|690x166](upload://ojckvhP5ScvwLkvYTUWxNQP3PqW.png)

I suspect there is something going on that is common amongst all these D3D11 shaders, such as blend state. But I have too little experience to know where to look next.

-------------------------

I3DB | 2019-02-20 20:55:05 UTC | #8

[quote="Leith, post:3, topic:4944"]
That’s being sourced from an environmental map,
[/quote]

I thought that too, and perhaps it is. [But the sample setup uses a reflection camera](https://github.com/urho3d/Urho3D/blob/05db29f6357ba1b409d7a61d04380f9d213dc62d/Source/Samples/23_Water/Water.cpp#L200) and a reflection plane, and there is nowhere an environmental map is specified looking through the material, technique and shader files. Also, if I mix a couple of the samples, for instance mix the animating scene with the water sample, the floating cubes from the animating scene are visible in the reflection, so conclude an environmental map isn't used.

No ... [I'm wrong. Actually environment is used as described by this comment.](https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/FeatureSamples/Assets/Data/Sample43/MatWater.xml#L3) This also explains another reason porting the water sample to a stereo application has been so hard. As per the sample code, I've only been creating a single refraction camera, but suspect I need two, and they must be working in stereo mode, so the refract pass might (hopefully) get it correct.

[quote="Leith, post:3, topic:4944"]
the water looks murky, it has more character than the “working” version.
[/quote]

When viewed without the nice reflection, for instance, move up and over the water, it just turns black and loses it's 'character'. On hololens, this is even more apparent. Though, using a BlueTransparent material looks sort of nice, but there is no rippling of the water.

The overall goal here is to replicate the c++ functionality on hololens using urhosharp. And replicate it perfectly. This is one of the samples that I've failed on thus far.

-------------------------

I3DB | 2019-02-20 16:50:53 UTC | #9

Here's another sample where the water isn't painted black and it seems to work fine:
![UWPWaterNotBlack|261x500](upload://kfIuWueW8bbMw3zYuQfA6CV8vV8.png)

[This sample just assigns the water material to a sphere.](https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/FeatureSamples/Core/43_BasicTechniques/BasicTechniques.cs#L104)

-------------------------

lezak | 2019-02-20 18:46:47 UTC | #10

I'm unable to reproduce Your issuses on 'normal' (c++) version of the engine (running on dx11, win10), so I've downloaded urhosharp samples and I can see them when running on UWP, so the problem is on the urhosharp's side.

-------------------------

I3DB | 2019-02-20 18:57:49 UTC | #11

Are there any clues you could give me on how to narrow this down in the urhosharp implementation?

Where to look, what to look for? It's just a c# wrapper, so if I could gain enough insight on the data flow for this issue I might find something.

-------------------------

Modanung | 2019-02-20 19:29:23 UTC | #12

Have you tried copy-pasting the shader file from the Urho3D repository or are they identical?

-------------------------

I3DB | 2019-02-20 20:36:43 UTC | #13

As I've gone down this craggy road of shader exploration, mostly I've found what is delivered with urhosharp is identical. In some cases they are different, but also renamed in those cases.

I purposely copied or reviewed differences, between water.xml material, water.xml technique and water.hlsl. There is a single difference found, on the water.xml material file, where the water feature sample has changed one parameter used for the [water feature sample called basic techniques where a custom material has been defined](https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/FeatureSamples/Assets/Data/Sample43/MatWater.xml#L7). But currently the same on urho3d and urhosharp sites.

https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/FeatureSamples/Assets/Data/Materials/Water.xml#L7

Doing this is when I found that whatever is in CoreData.pak is always chosen when there. So when I edited various hlsl files I had, those were always ignored in favor of choosing the unedited original in CoreData.pak. I had to rename techniques and shaders to get them to be loaded.

[The urhosharp project forked urho3d 1.7, and those coredata shaders haven't been changed in 3 years](https://github.com/xamarin/urho/tree/master/Urho3D/CoreData/Shaders/HLSL).

So for instance the [urhosharp water.hlsl shade](https://github.com/xamarin/urho/blob/master/Urho3D/CoreData/Shaders/HLSL/Water.hlsl)r, is identical to the current [urho3d shader](https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Shaders/HLSL/Water.hlsl).

In a loosely related issue, I found a missing hlsl custom shader, and rewrote it from glsl and had fairly good success, but my rewrite wasn't quite correct, it seemed to change when moving camera from left to right in a stereo application. Eventually I found there was a D3D11 conversion from glsl that I'd missed.[A pattern for it shown in the water.hlsl shader](https://github.com/urho3d/Urho3D/blob/05db29f6357ba1b409d7a61d04380f9d213dc62d/bin/CoreData/Shaders/HLSL/Water.hlsl#L19). The cbuffer pattern specifically. I put this into the custom shader rewrite and it fixed it. This particular pattern is briefly mentioned, but not in a useful way for this on [microsoft's page about hlsl conversion from glsl](https://docs.microsoft.com/en-us/windows/uwp/gaming/glsl-to-hlsl-reference).

-------------------------

I3DB | 2019-02-20 20:43:42 UTC | #14

[quote="I3DB, post:11, topic:4944"]
Are there any clues you could give me on how to narrow this down in the urhosharp implementation?
[/quote]

Maybe @Egorbo or @migueldeicaza will jump in and offer a direction of exploration to get this issue fixed?

-------------------------

cosar | 2019-02-20 23:53:06 UTC | #15

@I3DB Are you using the latest version or 1.7 release. I submitted a bug report sometime ago (#2232) that was creating a similar issue. I think it is fixed on the head.

-------------------------

I3DB | 2019-02-22 02:56:56 UTC | #16

[quote="cosar, post:15, topic:4944"]
Are you using the latest version or 1.7 release
[/quote]

Using this [latest github version of urho3d](https://github.com/xamarin/urho) that downloads on clone.

[And assume this is the issue 2232](https://github.com/urho3d/Urho3D/issues/2232).

The file that I'm using has the changes in that commit. If you're saying these introduced changes caused the issue, then it's not been fixed.

I'm using urhosharp, but will revert that change and see what happens.

---------------
Edit: 
This thread has been locked, but can still edit the prior posts. The issue is not solved by this change. It does seem like it's the spot on issue, but perhaps the Urhosharp guys did some other changes. Continuing to test this, but so far have found it has no effect by reversing the changes in the commit highlighted in the #2232 closed case.

Edit Next: 
The reason it has no effect is because on the testing I've done so far, the multisample test, or the need for multisample processing, isn't set in the code I'm executing. Haven't tracked down the reason why. That bug was opened for the case where multisample > 1, and apparently it failed and treated multisample as false resulting in water being painted black. In my case, it is false and doesn't incur the failure, but the end result is the same. 

However, this bug case gets right to a spot which can be used to track back the issue.

Edit Final:

Haven't solved the issue at all. 
1. The bug referenced by @cosar is for a specific case that isn't happening on the platforms I'm testing.
2. Additionally, the urho 1.7 branch I'm using has additional code related to the urhosharp implementation of UWP and Hololens. For example compare this [urhosharp urho3d file](https://github.com/xamarin/Urho3D/blob/4862691d18c0ed40895ba532dd7ba6f17cd2c763/Source/Urho3D/Graphics/Direct3D11/D3D11Graphics.cpp), with the [urho3d C++ file,](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Direct3D11/D3D11Graphics.cpp) and search on UWP to see some of the changes, or note they differ by over 100 lines. But @lezak is correct in that it's an urhosharp problem.
3. I did back out the changes as per the bug fix, but it has zero effect on the cases I'm looking at, running on both an x64 and an x86 win10 UWP platforms and one is a hololens. Both behave identically meaning both paint water black in this case and neither produces shadows.

Since this issue is closed here, I'll try to keep it updated on xamarin once solved.

-------------------------

cosar | 2019-02-21 11:08:41 UTC | #17

[quote="I3DB, post:16, topic:4944, full:true"]
[quote="cosar, post:15, topic:4944"]
Are you using the latest version or 1.7 release
[/quote]

Using this [latest github version of urho3d](https://github.com/xamarin/urho) that downloads on clone.

[And assume this is the issue 2232](https://github.com/urho3d/Urho3D/issues/2232).
[/quote]

That is the issue.
The repository that you indicated does not contain the fix for issue 2232. I think the fix is in this commit: [https://github.com/cadaver/Urho3D/commit/b00fab9b2850031bd6b22316d8df26419a16efca](https://github.com/cadaver/Urho3D/commit/b00fab9b2850031bd6b22316d8df26419a16efca) (you can easily apply it manually)

-------------------------

Modanung | 2019-02-21 11:08:46 UTC | #18



-------------------------

