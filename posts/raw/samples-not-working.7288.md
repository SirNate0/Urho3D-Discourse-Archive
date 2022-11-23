cqrtxwd | 2022-06-26 08:30:05 UTC | #1

windows 10 + mingw
I compiled the project, and gen all the samples . But all the samples are just a black window after I run it.
some sample have sounds but not picture. How to fix it?

-------------------------

Nerrik | 2022-06-26 14:00:12 UTC | #2

hard to help here with the little information.

First how did you build it?
What have you tried so far?
Are you using an IDE?
Did you look into the LOG Files? "C:\user\xxx\appdata\roaming\uhro3d\logs\"
Did you using the actual github version of Urho3d?

Out of the belly you can try to build it with CMAKE-GUI and useing an IDE like Codeblocks or Visual Studio Community, maybe with this steps youll find the problem for your self.

-------------------------

cqrtxwd | 2022-06-26 14:00:05 UTC | #3

I build it using cmake and mingw in terminals
no ide was used
using the master branch from github

-------------------------

Nerrik | 2022-06-26 14:20:21 UTC | #4

cmake log, urho3d log? Without informations we cant help ...

-------------------------

cqrtxwd | 2022-06-26 14:23:47 UTC | #5

[Sun Jun 26 22:03:43 2022] INFO: Opened log file C:/Users/cqrtx/AppData/Roaming/urho3d/logs/HelloGUI.log
[Sun Jun 26 22:03:43 2022] INFO: Created 5 worker threads
[Sun Jun 26 22:03:43 2022] INFO: Added resource path H:/unity_ws/Urho3D-master/build/bin/Data/
[Sun Jun 26 22:03:43 2022] INFO: Added resource path H:/unity_ws/Urho3D-master/build/bin/CoreData/
[Sun Jun 26 22:03:43 2022] INFO: Added resource path H:/unity_ws/Urho3D-master/build/bin/Autoload/LargeData/
[Sun Jun 26 22:03:44 2022] INFO: Adapter used NVIDIA GeForce GTX 1060
[Sun Jun 26 22:03:44 2022] INFO: Set screen mode 1024x768 rate 144 Hz windowed monitor 0
[Sun Jun 26 22:03:44 2022] INFO: Initialized input
[Sun Jun 26 22:03:44 2022] INFO: Initialized user interface
[Sun Jun 26 22:03:44 2022] INFO: Initialized renderer
[Sun Jun 26 22:03:44 2022] INFO: Initialized engine
Used resources:
Textures/Ramp.png
Textures/Spot.png
Textures/FishBoneLogo.png
Textures/UI.png
Textures/UrhoDecal.dds
Techniques/NoTexture.xml
RenderPaths/Forward.xml
UI/DefaultStyle.xml
Textures/UrhoIcon.png
Fonts/Anonymous Pro.ttf
Shaders/HLSL/Basic.hlsl

-------------------------

cqrtxwd | 2022-06-26 14:24:40 UTC | #6

[Sun Jun 26 22:01:57 2022] INFO: Opened log file C:/Users/cqrtx/AppData/Roaming/urho3d/logs/AnimatingScene.log
[Sun Jun 26 22:01:57 2022] INFO: Created 5 worker threads
[Sun Jun 26 22:01:57 2022] INFO: Added resource path H:/unity_ws/Urho3D-master/build/bin/Data/
[Sun Jun 26 22:01:57 2022] INFO: Added resource path H:/unity_ws/Urho3D-master/build/bin/CoreData/
[Sun Jun 26 22:01:57 2022] INFO: Added resource path H:/unity_ws/Urho3D-master/build/bin/Autoload/LargeData/
[Sun Jun 26 22:02:00 2022] INFO: Adapter used NVIDIA GeForce GTX 1060
[Sun Jun 26 22:02:01 2022] INFO: Set screen mode 1024x768 rate 144 Hz windowed monitor 0
[Sun Jun 26 22:02:01 2022] INFO: Initialized input
[Sun Jun 26 22:02:01 2022] INFO: Initialized user interface
[Sun Jun 26 22:02:01 2022] INFO: Initialized renderer
[Sun Jun 26 22:02:01 2022] INFO: Initialized engine
[Sun Jun 26 22:02:02 2022] ERROR: Failed to reflect vertex shader's input signature (HRESULT 80070057)
[Sun Jun 26 22:02:02 2022] ERROR: Failed to reflect vertex shader's input signature (HRESULT 80070057)
[Sun Jun 26 22:02:02 2022] ERROR: Failed to reflect vertex shader's input signature (HRESULT 80070057)
[Sun Jun 26 22:02:02 2022] ERROR: Failed to reflect vertex shader's input signature (HRESULT 80070057)
[Sun Jun 26 22:02:04 2022] ERROR: Failed to reflect vertex shader's input signature (HRESULT 80070057)
[Sun Jun 26 22:02:16 2022] INFO: Set screen mode 1920x1080 rate 144 Hz windowed monitor 0 borderless
[Sun Jun 26 22:02:18 2022] INFO: Set screen mode 1024x768 rate 144 Hz windowed monitor 0
Used resources:
Textures/Ramp.png
Textures/Spot.png
Textures/FishBoneLogo.png
Textures/UI.png
Textures/StoneDiffuse.dds
Textures/StoneNormal.dds
Techniques/NoTexture.xml
Techniques/DiffNormal.xml
Techniques/Diff.xml
RenderPaths/Forward.xml
UI/DefaultStyle.xml
Textures/UrhoIcon.png
Fonts/Anonymous Pro.ttf
Models/Box.mdl
Materials/Stone.xml
Shaders/HLSL/LitSolid.hlsl
Shaders/HLSL/Basic.hlsl

-------------------------

cqrtxwd | 2022-06-26 14:28:36 UTC | #7

Did I miss some pre-requirements? 
I only install DXSDK_Jun10

-------------------------

Nerrik | 2022-06-26 14:32:10 UTC | #8

with mingw i would use OpenGL instead of DirectX, if you want DirectX use Visual Studio.or try another mingw version

https://discourse.urho3d.io/t/snapshot-versions-of-1-6-with-d3d11-are-not-working/2475

-------------------------

cqrtxwd | 2022-06-26 15:04:25 UTC | #9

Thanks a lot.
how to switch to Opengl? I notice that there are GLEW in thirdPartys. So can I just add some definition flag to switch to opengl? Or I have to install an opengl lib somehow

-------------------------

Nerrik | 2022-06-26 15:16:12 UTC | #10

"-DURHO3D_OPENGL=1" 

https://urho3d.io/documentation/1.6/_building.html

better clean your cmake files first

-------------------------

1vanK | 2022-06-26 16:54:23 UTC | #11

Old version of MinGW has bugs and writes incorrect shader cache, use latest Mingw from msys2 and remove broken shader cache <https://github.com/urho3d/Urho3D/issues/2887>

-------------------------

