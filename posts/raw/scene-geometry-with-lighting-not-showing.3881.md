gkontadakis | 2017-12-26 10:09:09 UTC | #1

I am new to Urho3D. I was going through the samples past week which till yesterday worked perfectly fine.
Today after a Windows update and some Visual Studio reinstallation I am building just fine with Visual Studio 2017 (and 2015) and CMake(3.10.1), but I have rendering issues.
Objects are there but not rendered when there is at least one light on the scene. To repro this I used 38_SceneAndUILoad.
Repro:
Turn on off all lights --> 3 boxes appear.
Turn on at least 1 light --> 3 boxes dissapear.

Below is sample repro screenshot.
What am I doing wrong?

![Screenshot_Mon_Dec_25_23_33_08_2017|666x500](upload://4erh6zuhI4lk3irrKJ2K91SFjgz.png)

-------------------------

Eugene | 2017-12-26 09:41:16 UTC | #2

What graphical API and render path do you use?
Try another.

-------------------------

gkontadakis | 2017-12-26 10:16:40 UTC | #3

Haven't changed any configuration so by default I see D3D9 and "RenderPaths/Forward.xml". But I wiil experiment with these sttings and will report any feedback. Thanks!

-------------------------

gkontadakis | 2017-12-26 13:03:09 UTC | #4

ok after some experimentation both D3D11 and GL3 work fine for the default forward render technique.
Only D3D9 has issues with forward rendering and variants. With Deferred and Prepass geometry was shown (maybe on prepass material was not rendered in some cases but haven't tested much). Still strange that it stopped working for D3D9, hope this will not give me many problems in the future. But ok now I can work either with Directx 11 or OpenGL 3.
Thanks for pointing to the right direction!

-------------------------

Eugene | 2017-12-26 13:27:35 UTC | #5

[quote="gkontadakis, post:4, topic:3881"]
Only D3D9 has issues with forward rendering and variants
[/quote]

I accept that it could be Urho bug, but it could also be an environment issue.
If you have time and wish to investigate it, try to press F2 and check number of batches/triangles in buggy and working versions.

[quote="gkontadakis, post:1, topic:3881"]
Today after a Windows update
[/quote]

If don't know what updates you are talking about, but keep in mind that that Windows 10 Fail Creators Update and such "head" builds of Win10 are unstable as shit. I've recently encountered two fatal bugs that are confirmed to be Win10 fault (at my day job).

-------------------------

gkontadakis | 2017-12-26 14:07:36 UTC | #6

Sure no problem. I attach the screenshot comparisons of the profiler.
Without really knowing I don't think it is a bug, more like environment issue. All I did is Windows 10 update and removing older versions of Visual Studio leaving only 2017. Source code is the same as before (using 1.7 release not master).
And I confirmed it was the Fail Creators Update and I cannot rollback (at least easilly) because I cleaned up my drive after that arghh!
Thanks for the help again
![D3D11vsD3D9|690x258](upload://3FYYAQDItXc5dDhkIugRzQtpxLD.png)

-------------------------

