Miegamicis | 2017-01-02 01:13:04 UTC | #1

Hi, 

Recently came across this article [topic1354.html](http://discourse.urho3d.io/t/btraycastvehicle-example/1306/1) . Author managed to implement raycast vehicle support for the urho3D. I succesfully managed to get it to work on linux systems but when I try to build the same thing on windows (visual studio), it throws "unresolved external symbol" errors for the bullet classes. Does anyone have any solution to this problem? Thanks!

-------------------------

Lumak | 2017-01-02 01:13:04 UTC | #2

Make sure you have: -DURHO3D_PHYSICS=1
It's ON by default but it sounds like it's turned OFF.

-------------------------

Miegamicis | 2017-01-02 01:13:04 UTC | #3

[quote="Lumak"]Make sure you have: -DURHO3D_PHYSICS=1
It's ON by default but it sounds like it's turned OFF.[/quote]

Hi, 

I already had URHO3D_PHYSICS preprocessor defined but the problem still occurs.
Just to make it clearer, I tried  using Urho3D 1.5 prebuilt shared x32 and x64 windows versions.

-------------------------

Miegamicis | 2017-01-02 01:13:04 UTC | #4

Managed to find a workaround for this problem! I added prebuilt bullet libraries directly to my project configuration besides the Urho3D library, looks something like this:

Linker -> Input -> Additional dependencies:

For the x64 build:
C:\Users\Admin\DevWorkspace\bullet3-2.83.4\build64\lib\Release\BulletCollision.lib
C:\Users\Admin\DevWorkspace\bullet3-2.83.4\build64\lib\Release\BulletDynamics.lib
C:\Users\Admin\DevWorkspace\bullet3-2.83.4\build64\lib\Release\LinearMath.lib

For the x32 build:
C:\Users\Admin\DevWorkspace\bullet3-2.83.4\build\lib\Release\BulletDynamics.lib
C:\Users\Admin\DevWorkspace\bullet3-2.83.4\build\lib\Release\BulletCollision.lib
C:\Users\Admin\DevWorkspace\bullet3-2.83.4\build\lib\Release\LinearMath.lib

Built bullet library myself using CMake and VS 2013

I guess that the problem it that the bullet physics library is not directly accessible using Urho3D. Physics itself works when I use Urho3D wrapper, but when creating Bullet objects directly, I got the "unresolved external symbol" errors.

-------------------------

Lumak | 2017-01-02 01:13:04 UTC | #5

I've never used any prebuild libs, but I thought they include the default build options as described here [url]http://urho3d.github.io/documentation/1.5/_building.html[/url].  I find it strange that physics is not enabled.  Maybe someone in the community can give you more info about what flags are enabled for prebuilds.

Anyway, good to hear you found a work around.

-------------------------

weitjong | 2017-01-02 01:13:06 UTC | #6

I do not think the root cause of the problem was the physics being disabled. The "unresolved external symbol" means a required symbol is not found in the Urho3D library. Urho3D library can be built as either STATIC or SHARED type. Both have its own pros and cons, but I will not discuss them here. I just like to point out that STATIC library will have all the symbols from all the 3rd-party libraries included (whether the symbol is used or not), while SHARED library will only have the symbols from 3rd-party libraries that are used by Urho3D game engine code. I guess some how you have used STATIC lib type when targeting Linux platform and SHARED lib type for Windows platform?

Building and using 3rd-party library externally in this manner in the linking phase as the workaround for the above error is quite dangerous, IMHO. For one, the source code for the 3rd-party libraries (like Bullet) in our codebase may contain our own local patches. I suppose the workaround works because it makes linker resolves the missing symbol(s) from the externally pre-built lib. But what if the linker also resolves other symbols from it too or what if it ends up with duplicate global.

In this case, I would just use STATIC lib type as the "workaround".

-------------------------

Miegamicis | 2017-01-02 01:13:06 UTC | #7

[quote="weitjong"]I do not think the root cause of the problem was the physics being disabled. The "unresolved external symbol" means a required symbol is not found in the Urho3D library. Urho3D library can be built as either STATIC or SHARED type. Both have its own pros and cons, but I will not discuss them here. I just like to point out that STATIC library will have all the symbols from all the 3rd-party libraries included (whether the symbol is used or not), while SHARED library will only have the symbols from 3rd-party libraries that are used by Urho3D game engine code. I guess some how you have used STATIC lib type when targeting Linux platform and SHARED lib type for Windows platform?

Building and using 3rd-party library externally in this manner in the linking phase as the workaround for the above error is quite dangerous, IMHO. For one, the source code for the 3rd-party libraries (like Bullet) in our codebase may contain our own local patches. I suppose the workaround works because it makes linker resolves the missing symbol(s) from the externally pre-built lib. But what if the linker also resolves other symbols from it too or what if it ends up with duplicate global.

In this case, I would just use STATIC lib type as the "workaround".[/quote]

Thanks for the suggestion, will definitely try out the static version of the lib. Will let you know about the results!

-------------------------

