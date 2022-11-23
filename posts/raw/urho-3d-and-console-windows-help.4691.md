Elendil | 2018-11-25 14:11:14 UTC | #1

I download latest Urho3D and create build for Windows 32bit with OpenGL with VisualStudio 2017 CE. Everything is fine, except I can not run project as Windows console application. I twice build Urho with WIN32_CONSOLE option on, without succes.

Here is error when I try build sample as windows Console project.
    1>MSVCRTD.lib(exe_main.obj) : error LNK2019: unresolved external symbol _main referenced in function "int __cdecl invoke_main(void)" (?invoke_main@@YAHXZ)
    1>D:\...\Debug\Test 01.exe : fatal error LNK1120: 1 unresolved externals
    1>Done building project "Test 01.vcxproj" -- FAILED.

(I am on Windows 7 64bit Home Edition)

-------------------------

Sinoid | 2018-11-25 19:26:57 UTC | #2

More specifics are needed.

- If what you're after is a custom player application you need to use `URHO3D_DEFINE_APPLICATION_MAIN` if you want to use the built in **Application** class
    - See `Source/Tools/Urho3DPlayer/Urho3DPlayer.cpp`
    - However, the player subsystem is windows, as it should be (and has to be for windows sticker passing)
- Is this something you set up in CMake that links Urho3D
    - See the **RampGenerator** tool `Sources/Tools/RampGenerator` which links Urho3D for a command-line tool.
- You're not trying to compile the Urho3D library itself under console subsystem (`/SUBSYSTEM:CONSOLE` in VS) are you? You can't do that trivially.
    - Shouldn't be what you're doing unless you manually tweaked the generated projects though

-------------------------

Elendil | 2018-11-25 19:55:15 UTC | #3

[quote="Sinoid, post:2, topic:4691"]
If what you’re after is a custom player application you need to use `URHO3D_DEFINE_APPLICATION_MAIN`
[/quote]
Unfortunately this is not working and sample code I use from WIki Documentation (the first one) use it.

But I remember that there is comented custom main() inside sample. I uncomented it and add my class in it and "hop" it is working as console. :)

-------------------------

