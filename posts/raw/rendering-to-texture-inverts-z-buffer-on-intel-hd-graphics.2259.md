Beyboy | 2017-01-02 01:14:20 UTC | #1

Hi all!
I need to render image to texture using Urho. I am talking about Windows 10 64bit desktop. I am using UrhoSharp. The software works fine on Nvidia as well as ATI (AMD) graphic cards, however it fails on Intel HD graphic cards (Intel HD, Intel HD 4000). By "failing" I mean that objects that are far are displayed on top of objects that are close. Like if the Z-buffer was inverted somehow.

I have found your official example, namely example #10 (RenderToTexture) in which I would like to point out the problem:
I have two versions of this example:
 1) One is released binary (10_RenderToTexture.exe) downloaded as part of Urho3D-1.6-Windows-64bit-STATIC-3D11.zip and this works fine on all graphic cards.
 2) I have built second version from sources (Visual Studio 2015). I got it from xamarin/urho-samples on GitHub. I am getting the problem in this version.

I have circled the problematic parts: In left circle there is a smaller lighter box on top of darker big box. Obviously, the big box should be on top of the smaller one as it is closer to the camera. Similar problem is in second circle where there are three boxes in wrong order.
[img]http://beyboy.wz.cz/z_buffer_problem.png[/img]
Unfortunately, the problem is not 100% consistent, sometimes it seems that the order is fine. But it can be replicated in at least 50% of cases when I run the example. 

I have managed to reproduce this problem on two computers with integrated Intel HD graphic cards. I am unable to get their exact name or version - one shows just as Intel HD Graphics, second is described as Intel HD Graphics 4000.

The problem appears when I debug the code in Visual Studio as well as when I make a release from Visual Studio.

I would like to know how did you build original released examples - they seems that they are slightly different - each is a separate EXE file. Maybe you have used different building process?

Anyway, can anybody reproduce my problems? Can anybody give me any hints how to solve it?

Thanks!
Karel

-------------------------

cadaver | 2017-01-02 01:14:20 UTC | #2

Welcome to the forums.
What graphics API is your compiled version using (D3D9, D3D11, OpenGL?)

It looks like your build is not using the depth buffer when rendering to a texture. Don't think I've encountered that myself on Intel GPU's. Whether you're running individual samples or script samples via Urho3DPlayer should not make a difference to how the engine works, rendering-wise.

-------------------------

weitjong | 2017-01-02 01:14:21 UTC | #3

[quote="Beyboy"]I would like to know how did you build original released examples - they seems that they are slightly different - each is a separate EXE file. Maybe you have used different building process?[/quote]
We use a unified "rake ci" task for all our automated CI builds. It is the same task for Windows Server, Linux Server, and OSX VMs. See Rakefile at the root of Urho3D project source tree for more detail. Look for "task :ci". On Windows Server, the task basically called "rake cmake vs2015 URHO3D_D3D11=1 URHO3D_LUAJIT=1 URHO3D_DATABASE_SQLITE=1 URHO3D_EXTRAS=1" which actually in turn called the "cmake_vs2015.bat" with those build options supplied. In short there are nothing special about it.

-------------------------

