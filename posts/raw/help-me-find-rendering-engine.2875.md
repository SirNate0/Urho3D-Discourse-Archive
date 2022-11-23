olegklimov | 2017-03-09 17:23:16 UTC | #1

Hello, I'm implementing robotics simulator, I need quality rendering engine. I already have elaborate physics, scripting, etc. All shapes and meshes already are in memory.

I see you have nice documentation page:

https://urho3d.github.io/documentation/HEAD/_rendering.html

which sounds like what I need, but:

1) Can I compile Urho rendering without compiling everything else? Dependencies list is just ridiculous, 27 libraries, including Lua and SQL databases!

2) If I can't, maybe someone knows library that will suit better for this purposes? I'm looking for it for some time now, no luck...

Thanks!

-------------------------

Eugene | 2017-03-09 17:29:36 UTC | #2

You can disable some libraries in CMake configuration, but the most are mandatory.
However, I don't understand how does it disturb you.

-------------------------

olegklimov | 2017-03-09 17:53:23 UTC | #3

> I don't understand how does it disturb you

My project will be distributed in source code form. Every user will compile it, automatic installation and compilation using `pip` is highly desirable. If it will have a lot of dependencies, especially hard-to-compile dependencies, the whole project will be less useful. Not 27, no.

-------------------------

1vanK | 2017-03-09 17:59:10 UTC | #4

Ogre3D and bgfx - graphical libraries only (although I have not tried them, Urho arranges me completely)

-------------------------

Eugene | 2017-03-09 18:17:49 UTC | #5

As far as I know, you can't easily 'subfolder' Urho like some small library inside your repo because its build process is pretty complex. You will probably have to fork & tune it or use separate CMake build tree just for Urho library.

-------------------------

slapin | 2017-03-09 23:42:40 UTC | #6

I use Urho as static library, there are docs how to do that on official site.

As for rendering engines, I myself use Quake2 one as it supports software rendering among OpenGL.
Ogre is cool too. There is also Open Scene Graph (OSG).

-------------------------

olegklimov | 2017-03-10 08:31:58 UTC | #7

OK thanks everyone especially @1vanK for helping out!

-------------------------

rku | 2017-03-10 15:20:09 UTC | #8

[Yes you can](https://github.com/rokups/Urho3D/commit/1f847271a709306fc502f4ade9dcca2b9c2164db). This patch breaks SDK builds but that is not needed if engine is included as subfolder.

@olegklimov the nice thing about Urho3D is that it bundles all third party dependencies and has proper build scripts. Engine is self-contained and it is highly unlikely to have build issues as external engine dependencies are only ones provided by the OS/platform.


Edit: forgot ti mention that my `add_subdirectory()` support hack requires `project(Urho3D)` in main `CMakeLists.txt` file of game project.

-------------------------

codingmonkey | 2017-03-12 10:58:04 UTC | #9

[quote="olegklimov, post:1, topic:2875"]
2) If I can't, maybe someone knows library that will suit better for this purposes?
[/quote]

You may try other render engine https://github.com/cadaver/turso3d

-------------------------

cadaver | 2017-03-13 12:00:21 UTC | #10

Turso3D is a toy engine for the time being and it has been dormant some time due to not enough time for development. It's possible that when I continue it, I will nuke the code once more. All that said I don't recommend trying it currently, at least for anything serious.

-------------------------

