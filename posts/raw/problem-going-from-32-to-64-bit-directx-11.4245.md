DavidHT | 2018-05-26 20:25:14 UTC | #1

Dear all,

I've come to a point that I want to move my application to 64 bits. I'm using VS2017, DirectX11.
I use Urho3D as separate a library, to display a 3D view of a design, so as a CView in MFC.
This always worked fine in the 32 bit version of the program.

Now that I've changed everything to 64 bits, the 3D viewer is behaving weirdly.
When moving the camera, most of the time nothing is visible. But at certain angles/positions, I can see the Skybox that used to surround the scene. I see it as a sphere now. See attached picture.

![empty_3D|690x311](upload://jZqGVplSPiEAc4vzbWOvXjU4cEX.jpg)

Code:
`    skyNodeBlue_ = scene_->CreateChild("SkyBlue");`
`Skybox* skyBlue = skyNodeBlue_->CreateComponent<Skybox>();`
`skyBlue->SetModel(cache->GetResource<Model>("Models/Sphere.mdl"));`
`skyBlue->SetMaterial(cache->GetResource<Material>("Materials/SkyBlue.xml"));`


I've been searching for two days now trying to find out what's causing this, but still no real clue. 
It might be compiler settings in the Urho3D project files, or perhaps a #define somewhere.
As you can see the DebugHud appears as it should.

Hopefully any of you can give me a push in the right direction?

Thanks for reading.

David.

-------------------------

Eugene | 2018-05-21 10:49:01 UTC | #2

Could you reproduce the problem with any standrad x64 sample, e.g. `04_StaticScene`?

-------------------------

DavidHT | 2018-05-21 11:22:02 UTC | #3

Thanks for your reply.

No, when I use the standard CMake/Win64 procedure, the examples work fine.

About a year ago, I took from Urho3D (1.7) the elements I needed, and over time, I changed a few things like the AssImp Collada exporter. Also, as some of the third party components share libraries with other parts of my application (zlib, unzip), some changes had to be made to make it all work together.

Now, I just tried to change the target to x64, hoping it would work.

I understand very well that using a slightly adapted version of Urho3D makes it very hard to say anything, but I hope that someone would recognize the Skybox turning into a sphere, and would think aha: you need to make sure that this library setting is such and such, or that this or that DirectX directive is set correctly :slight_smile:. I think it has something to do with basic primitive type sizes, but as far as I know they're the same for int, float, etc. for 32 and 64 bit environments in MSVC at least.

Otherwise, I'll try and make baby steps from the working sample into my application.

Thanks!

-------------------------

Eugene | 2018-05-21 11:50:56 UTC | #4

[quote="DavidHT, post:3, topic:4245"]
About a year ago, I took from Urho3D (1.7) the elements I needed, and over time, I changed a few things like the AssImp Collada exporter. Also, as some of the third party components share libraries with other parts of my application (zlib, unzip), some changes had to be made to make it all work together.
[/quote]

Do you use up-to-date (master) parts of Urho?
It might be some old defect.

If you make and share minimal sample code with the defect (w/o binaries, please), I could try to reproduce and debug it.

I also wonder whether it is reproduced
1) On other machines
2) With other renderers

-------------------------

DavidHT | 2018-05-24 09:04:27 UTC | #5

I hope you're still there!

I just use the Urho3D 1.7 download from the main Urho3d page.
It can be reproduced with the standard examples, **debug** version. I'm not sure it's 100% the same problem, but it looks similar.

The steps I took:
- Download and unzip Urho3D-1.7.zip
- Run CMake, for Visual Studio 2017 Win 64
- Start VS2017, and open Urho3D.sln
- Build the **Debug** configuration
- Run example 4, StaticScene
- When looking around using the mouse the Window goes fully black for certain angles

Example 11 (Physics) and 23 (Water) have a similar behavior.

I've built it on my main desktop computer, but see the same behavior on different computers I run the resulting executable on.

Thanks for reading!

-------------------------

Miegamicis | 2018-05-24 09:15:19 UTC | #6

Hi, could you test this with the latest changes from the Urho3D master branch? The build steps are the same as it was for 1.7.

-------------------------

DavidHT | 2018-05-24 09:38:49 UTC | #7

Of course. I just did, but it has the same behavior. Master 2482502.

-------------------------

Miegamicis | 2018-05-24 09:44:59 UTC | #8

Okay. I will also test this out myself (hopefully today). I usually build only x64 version on Windows but haven't experienced anything like that before.

-------------------------

DavidHT | 2018-05-24 09:54:04 UTC | #9

Thanks! Just for illustration, here are two screen captures of example 4:
Release:
https://www.screencast.com/t/qifO5D3DQRTh

Debug:
https://www.screencast.com/t/3WLS6ost

So the debug build has the problem. The release build seems to be fine. I'm using the mouse and the WASD keys. You see items disappear when using the W key.

-------------------------

DavidHT | 2018-05-24 10:24:10 UTC | #10

I just built everything on another machine (Surface Pro/Windows 10) with a fresh installation of Visual Studio 2017.
The debug build has the same problem.

So I hope you can reproduce it.

Thanks a lot for looking into it. I appreciate it a lot!

-------------------------

Miegamicis | 2018-05-24 10:56:35 UTC | #11

From the 2nd video it seems like the camera is not actually moving. Is there anything inside the console logs (by pressing F1 in the samples)?

-------------------------

DavidHT | 2018-05-24 11:23:19 UTC | #12

Indeed, it doesn't seem to move forward and backward.
It goes sideways though.
Release build works as it should, it's only the debug version.

When looking around (Mouse), the screen goes black for some angles.

Here's another capture. With F1/F2 on and off. Near the end, you can see the camera moving sideways.

https://www.screencast.com/t/I6zsbiAvys0

-------------------------

Miegamicis | 2018-05-24 19:40:17 UTC | #13

I'm seeing the same issue using Visual studio 2017, 64bit and using Directx11 debug build. 
So far I couldn't find out what could be the issue, but my suggestion would be using Visual Studio 2015 till it's fixed.

Also it would be useful if you could register this issue in the github.

-------------------------

DavidHT | 2018-05-25 07:38:19 UTC | #14

Thanks for confirming that you reproduced the problem.

I reported it as a bug:
https://github.com/urho3d/Urho3D/issues/2318

Going back to VS2015 is not really an option, as much of the rest of the project uses C++14 and C++17 features, but I verified and indeed, in VS2015, it does work as it should.

Does anyone else have any idea what might be the difference between the VS2015 and VS2017 builds?

-------------------------

Eugene | 2018-05-25 16:37:56 UTC | #15

@Miegamicis, @DavidHT I'm unable to reproduce the defect :confused:
Win 7 professional SP1, VS 2017 (15.6.4)
Debug x64.

I need more info. Exact VS 2017 version, OS version...
And my question about GAPI used is still open. Please test this for GL, DX9 and DX11.

-------------------------

DavidHT | 2018-05-25 18:21:09 UTC | #16

Window 10 Home, Microsoft Visual Studio Community, 2017, version 15.7.1.
I'll check the builds for GL, DX9 and DX11.

-------------------------

DavidHT | 2018-05-25 19:49:13 UTC | #17

I've compiled and tested the debug versions for GL, DX9 and DX11. They all show the same behavior for Example 04, StaticScene.

-------------------------

DavidHT | 2018-05-26 21:35:11 UTC | #18

I found the following, perhaps making it easier to find the bug.

If, in example 04, StaticScene, you change the initial camera position in line 124 to:
`  cameraNode_->SetPosition(Vector3(0.0f, 5.0f, 16.0083713531494f));`
You'll see the missing bits in the foreground from the start.

If you change the initial camera position to:
`  cameraNode_->SetPosition(Vector3(0.0f, 5.0f, -1.21793007850647f));`
The screen is black from the start. If you move forward (by pressing 'W'), the scene becomes visible again.

-------------------------

Eugene | 2018-05-27 10:26:11 UTC | #19

This is 95% confirmed VS bug
https://developercommunity.visualstudio.com/content/problem/260301/invalid-code-in-x64-debug-mode.html
As temporary workaround pick locally commit from here:
https://github.com/eugeneko/Urho3D/commits/master-vc2017

-------------------------

DavidHT | 2018-05-27 11:52:19 UTC | #20

You're great! I'm impressed by how quickly you found this compiler issue.

I can confirm that both my original problem is solved, and that example 04 now works as it should.
Let's hope for a quick fix from Microsoft.

Please note that the original problem was not only showing in the Debug build, but also in Release.

Thanks again.

-------------------------

Eugene | 2018-05-28 09:50:58 UTC | #21

The bug is fixed, according to the same link.
Wait for VS update.
It's interesting whether the Release bug is fixed too...

-------------------------

DavidHT | 2018-05-28 18:27:22 UTC | #22

That's great news. 
In my original situation, the release build indeed suffered from the same bug. Hopefully they solve it for all configurations.

-------------------------

lezak | 2018-05-31 23:23:32 UTC | #23

I've just intalled leatest update for VS (15.7.3) and it seems that the bug is indeed fixed.

-------------------------

DavidHT | 2018-06-02 08:06:13 UTC | #24

I can confirm that. Also the release mode where I had problems originally, works fine now. Sometimes Microsoft is more responsive than you think! This forum too, by the way :). Thank you all.

-------------------------

