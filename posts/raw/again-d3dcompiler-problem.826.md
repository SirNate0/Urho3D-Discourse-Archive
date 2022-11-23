rogerdv | 2017-01-02 01:03:13 UTC | #1

A couple of weeks ago I installed Windows 8.1, but just yesterday I installed VS Express 2012, recompiled the project and tried to execute. Again, I got the missing d3dcompiler dll. I thought that such problem was solved by the SDK included in VS 2012. Tried to copy the dll from another game to my application directory, but that caused a program error. I guess that perhaps the SDK requires to be manually installed, or maybe there is another step that I missed. I could compile Urho to use OpenGL, but then the perfomance on Intel cards would be crappy.
Any way to solve this?

-------------------------

JamesK89 | 2017-01-02 01:03:13 UTC | #2

Do you have the [i]Microsoft DirectX SDK (June 2010)[/i] package installed?

I have Visual Studio Premium 2010, Premium 2012 and Community Edition 2013 all installed but despite the fact that DirectX is integrated into the Windows 8.x SDK I could not get Direct3D 9 projects to build until I installed the Microsoft DirectX SDK (June 2010) package.
From what I gather the modern Windows SDK drops a lot of legacy stuff from DirectX starting with DirectX 11 and going forward so you'll probably need the older seperate DirectX SDK for DirectX 10 and earlier.

-------------------------

rogerdv | 2017-01-02 01:03:13 UTC | #3

About that, there is a problem. When I try to install the SDK I get an error saying that I need to install .Net framework. If I try to install any .net framework, it says it is already included in the system. The Dx SDK offers to download it, but I dont have internet at home, so, havent tried that option.

-------------------------

JamesK89 | 2017-01-02 01:03:13 UTC | #4

NOTE: You'll probably want to make a system restore backup before doing this.

Try right clicking on the bottom right of your desktop and clicking "Programs and Features."
When the "Programs and Features" window appears click "Turn Windows features on or off" from the left hand side of the window and a new window entitled "Windows Features" will appear.
From the tree view in the "Windows Features" dialog uncheck ".NET Framework 3.5 (include .NET 2.0 and 3.0)" then click "OK" and Windows should proceed with removing the .NET Framework (it may tell you to reboot afterward, in which case I would suggest you do).
Once Windows has removed the .NET Framework try running the DirectX SDK (June 2010) installer again.

Should the DirectX SDK installer succeed you will want to run Windows Update to ensure your .NET Framework is the latest version:

After the DirectX SDK installer has completed right click on the bottom left of your desktop and select "Control Panel."
Once the "Control Panel" window appears click on the icon entitled "Windows Update."
Once at the "Windows Update" screen click on "Check for updates" from the left hand side and Windows Update will check for updates.

-------------------------

Stinkfist | 2017-01-02 01:03:15 UTC | #5

"When building with the Windows 8 SDK, copy d3dcompiler_46.dll from "C:\Program Files (x86)\Windows Kits\8.0\bin\x86" to build tree's "bin" directory so that Urho3D executables will run correctly." - from Getting Started documentation. Have you tried that? Note: copy the DLL from x64 folder if building an x64 version.

-------------------------

rogerdv | 2017-01-02 01:03:17 UTC | #6

To Urho's bin or my project's bin? Did the second, and got an error.

-------------------------

