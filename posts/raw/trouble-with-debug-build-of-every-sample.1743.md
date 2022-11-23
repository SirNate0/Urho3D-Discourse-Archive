snake23 | 2017-01-02 01:09:49 UTC | #1

Hi,

I'm having trouble when building samples in debug using Eclipse on Linux. Here's what I get with CrowdNavigation:
[img]https://framapic.org/d8zGYbKcEsy0/MexCut4WioZs.png[/img]

And here's what a release build looks like:
[img]https://framapic.org/OXS296nCBDpO/QbOfprUyzzBQ.png[/img]

I built and installed Urho in debug by following these steps:
[code]
./cmake_generic.sh build_debug/ -URHO3D_LUA=1 -URHO3D_SAMPLES=1 -URHO3D_EXTRAS=1 -URHO3D_DOCS_QUIET=1 -DCMAKE_BUILD_TYPE=Debug -DCMAKE_DEBUG_POSTFIX=D
cd build_debug
make -j8
sudo make install
[/code]

Then I created an Eclipse project using CrowdNavigation.cpp and CrowdNavigation.h from Urho's "Source/Samples/39_CrowdNavigation" folder and Sample.inl and Sample.h from "Source/Samples" folder.

I set my project's debug configuration to use these build and link settings:
-I (include paths)
[ul]/usr/include/bullet
/usr/include[/ul]
-L (library search paths)
[ul]/usr/local/lib/Urho3D[/ul]
-l (libraries)
[ul]Urho3DD
dl
pthread
GL[/ul]

I built the project's debug config and got this ouput, which looks just fine:
[code]21:24:25 **** Build of configuration Debug for project UrhoDemo ****
make -j4 all 
Building file: ../CrowdNavigation.cpp
Invoking: GCC C++ Compiler
g++ -I"WORKSPACE_LOCATION/UrhoDemo" -I/usr/include/bullet -I/usr/include -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"CrowdNavigation.d" -MT"CrowdNavigation.o" -o "CrowdNavigation.o" "../CrowdNavigation.cpp"
Finished building: ../CrowdNavigation.cpp
 
Building target: UrhoDemo
Invoking: GCC C++ Linker
g++ -L/usr/local/lib/Urho3D -o "UrhoDemo"  ./CrowdNavigation.o   -lUrho3D -ldl -lpthread -lGL
Finished building target: UrhoDemo[/code]

Finally, I copied "CoreData" and "Data" folders into my executable's folder and ran it.

If I link Urho3D (release) instead of Urho3DD, it solves my problem. I thought that there might be a problem with my debug build of Urho3D. But, at the same time, the sample executables generated when building the debug library (located in build_debug/bin) work fine.

Any idea?

Thanks.

Additional information:
OS: Ubuntu 15.10
Eclipse 4.5.1
g++ 5.2.1
Urho3D 1.5

-------------------------

thebluefish | 2017-01-02 01:09:49 UTC | #2

What version of Urho3D are you using? 1.5? Master?

-------------------------

snake23 | 2017-01-02 01:09:50 UTC | #3

Sorry, I updated my post, I'm using Urho3D 1.5.

-------------------------

rasteron | 2017-01-02 01:09:50 UTC | #4

Any console errors on the debug build? You could post your log file here.

-------------------------

snake23 | 2017-01-02 01:09:50 UTC | #5

Here's what the sample logs:
[code][Thu Feb  4 01:50:50 2016] INFO: Opened log file /home/snake23/.local/share/urho3d/logs/CrowdNavigation.log
[Thu Feb  4 01:50:50 2016] INFO: Created 3 worker threads
[Thu Feb  4 01:50:50 2016] INFO: Added resource path /mnt/Fox/Code/Workspace/UrhoDemo/Debug/Data/
[Thu Feb  4 01:50:50 2016] INFO: Added resource path /mnt/Fox/Code/Workspace/UrhoDemo/Debug/CoreData/
[Thu Feb  4 01:50:50 2016] DEBUG: Skipped autoload path 'Autoload' as it does not exist, check the documentation on how to set the 'resource prefix path'
[Thu Feb  4 01:50:51 2016] INFO: Set screen mode 1024x768 windowed
[Thu Feb  4 01:50:51 2016] INFO: Initialized input
[Thu Feb  4 01:50:51 2016] INFO: Initialized user interface
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/Ramp.png
[Thu Feb  4 01:50:51 2016] DEBUG: Loading temporary resource Textures/Ramp.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/Spot.png
[Thu Feb  4 01:50:51 2016] DEBUG: Loading temporary resource Textures/Spot.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Techniques/NoTexture.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource RenderPaths/Forward.xml
[Thu Feb  4 01:50:51 2016] INFO: Initialized renderer
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource UI/MessageBox.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading UI layout UI/MessageBox.xml
[Thu Feb  4 01:50:51 2016] INFO: Initialized engine
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/LogoLarge.png
[Thu Feb  4 01:50:51 2016] DEBUG: Loading temporary resource Textures/LogoLarge.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/UrhoIcon.png
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource UI/DefaultStyle.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/UI.png
[Thu Feb  4 01:50:51 2016] DEBUG: Loading temporary resource Textures/UI.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Fonts/Anonymous Pro.ttf
[Thu Feb  4 01:50:51 2016] DEBUG: Font face Anonymous Pro (11pt) has 624 glyphs
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Models/Plane.mdl
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Materials/StoneTiled.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Techniques/DiffNormalPacked.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Techniques/Diff.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/StoneDiffuse.dds
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/StoneNormal.dds
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Models/Box.mdl
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Materials/Stone.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Built navigation mesh with 36 tiles
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Models/Mushroom.mdl
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Materials/Mushroom.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/Mushroom.dds
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Models/Cylinder.mdl
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/TerrainDetail2.dds
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Models/Jack.mdl
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Materials/Jack.xml
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Textures/UI.png
[Thu Feb  4 01:50:51 2016] DEBUG: Font face Anonymous Pro (15pt) has 624 glyphs
[Thu Feb  4 01:50:51 2016] DEBUG: Reloading shaders
[Thu Feb  4 01:50:51 2016] DEBUG: Set occlusion buffer size 256x192 with 5 mip levels and 1 thread buffers
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Shaders/GLSL/Shadow.glsl
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Shaders/GLSL/LitSolid.glsl
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled vertex shader Shadow(INSTANCED)
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled pixel shader Shadow()
[Thu Feb  4 01:50:51 2016] DEBUG: Linked vertex shader Shadow(INSTANCED) and pixel shader Shadow()
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled vertex shader Shadow(SKINNED)
[Thu Feb  4 01:50:51 2016] DEBUG: Linked vertex shader Shadow(SKINNED) and pixel shader Shadow()
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT INSTANCED NORMALMAP PERPIXEL SHADOW)
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT NORMALMAP PACKEDNORMAL PERPIXEL SHADOW SPECULAR)
[Thu Feb  4 01:50:51 2016] DEBUG: Linked vertex shader LitSolid(DIRLIGHT INSTANCED NORMALMAP PERPIXEL SHADOW) and pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT NORMALMAP PACKEDNORMAL PERPIXEL SHADOW SPECULAR)
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT INSTANCED PERPIXEL SHADOW)
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT PERPIXEL SHADOW SPECULAR)
[Thu Feb  4 01:50:51 2016] DEBUG: Linked vertex shader LitSolid(DIRLIGHT INSTANCED PERPIXEL SHADOW) and pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT PERPIXEL SHADOW SPECULAR)
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT NORMALMAP PERPIXEL SHADOW)
[Thu Feb  4 01:50:51 2016] DEBUG: Linked vertex shader LitSolid(DIRLIGHT NORMALMAP PERPIXEL SHADOW) and pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT NORMALMAP PACKEDNORMAL PERPIXEL SHADOW SPECULAR)
[Thu Feb  4 01:50:51 2016] WARNING: Shader LitSolid(DIRLIGHT NOUV PERPIXEL SHADOW SKINNED) does not use the define NOUV
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled vertex shader LitSolid(DIRLIGHT NOUV PERPIXEL SHADOW SKINNED)
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIRLIGHT PERPIXEL SHADOW SPECULAR)
[Thu Feb  4 01:50:51 2016] DEBUG: Linked vertex shader LitSolid(DIRLIGHT NOUV PERPIXEL SHADOW SKINNED) and pixel shader LitSolid(AMBIENT DIRLIGHT PERPIXEL SHADOW SPECULAR)
[Thu Feb  4 01:50:51 2016] DEBUG: Loading resource Shaders/GLSL/Basic.glsl
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled vertex shader Basic(DIFFMAP VERTEXCOLOR)
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled pixel shader Basic(DIFFMAP VERTEXCOLOR)
[Thu Feb  4 01:50:51 2016] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(DIFFMAP VERTEXCOLOR)
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled pixel shader Basic(ALPHAMAP VERTEXCOLOR)
[Thu Feb  4 01:50:51 2016] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(ALPHAMAP VERTEXCOLOR)
[Thu Feb  4 01:50:51 2016] DEBUG: Compiled pixel shader Basic(ALPHAMASK DIFFMAP VERTEXCOLOR)
[Thu Feb  4 01:50:51 2016] DEBUG: Linked vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(ALPHAMASK DIFFMAP VERTEXCOLOR)

Used resources:
Textures/Ramp.png
Textures/Spot.png
Textures/LogoLarge.png
Textures/UI.png
Textures/StoneDiffuse.dds
Textures/StoneNormal.dds
Textures/Mushroom.dds
Textures/TerrainDetail2.dds
Techniques/NoTexture.xml
Techniques/DiffNormalPacked.xml
Techniques/Diff.xml
RenderPaths/Forward.xml
UI/MessageBox.xml
UI/DefaultStyle.xml
Textures/UrhoIcon.png
Textures/UI.png
Fonts/Anonymous Pro.ttf
Models/Plane.mdl
Models/Box.mdl
Models/Mushroom.mdl
Models/Cylinder.mdl
Models/Jack.mdl
Materials/StoneTiled.xml
Materials/Stone.xml
Materials/Mushroom.xml
Materials/Jack.xml
Shaders/GLSL/Shadow.glsl
Shaders/GLSL/LitSolid.glsl
Shaders/GLSL/Basic.glsl
[/code]

-------------------------

weitjong | 2017-01-02 01:09:50 UTC | #6

Welcome to our forum.

How did you generate the Makefile for your project in the first place? From the build output log it does not seem to be generated using our CMake build system. Just in case you don't know, you can reuse Urho3D build system in your own project. However, if you already know that but still decided to generate the Makefile for your project using other means then you have to be prepared to take care a lot of things by your own. And even after you have done that correctly, it probably may only work for one platform or two. While using the latter gives you the potential to target all platforms with little effort on your own. Additionally, you will get better support simply because it has been used and tested by most of us so we already know what to expect and how to troubleshoot when/if it does not work. Back to your problem, I have never seen that myself before. I can only suspect that it has something to do with compiler defines not being defined at all.

-------------------------

snake23 | 2017-01-02 01:09:51 UTC | #7

Hi and thanks for your answer,

As I said, I'm using Eclipse for my project, which generates the makefile I'm using.

I'm not sure I completely understand what you mean by "reuse Urho3D build system" in my project...

I've uploaded my complete Eclipse project. It includes the source code, Eclipse project files, and the generated makefiles for both build and release configurations. I also emptied "CoreData" and "Data" folders but left them in place.

You can download it by following this link: [framadrop.org/r/0GAbUuF6PH#1JwB ... 3NEZa23qY=](https://framadrop.org/r/0GAbUuF6PH#1JwBpkQGSFCXc9ZZdIcsKdcmStF0IqeG/O3NEZa23qY=).

Thanks again.

-------------------------

weitjong | 2017-01-02 01:09:52 UTC | #8

I suppose you have not read this [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html). Use the "switcher" to switch to 1.5 if you are using that version.

Basically, we use CMake to generate the project file instead of using the IDE. This is true for both Urho3D project or your own project. In essense the downstream projects reuse the build system originally designed for Urho3D. 

So in your case,  after the project file is generated then simply import it into Eclipse workspace. HTH.

-------------------------

