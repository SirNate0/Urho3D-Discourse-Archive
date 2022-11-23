joe | 2020-08-15 02:43:47 UTC | #1

Hi I have a few questions regarding this game engine.

1. Does it come with its own GUI game editor?
2. Can the game be written in C++?
3. Does the entire game code get compiled into the game?

-------------------------

JTippetts1 | 2020-08-15 02:58:22 UTC | #2

1 - Not really. It has a GUI editor, and you can use it to compose scene node hierarchies, UI elements, etc... but it's not a gestalt editor like Unity or Godot. There is no 'deploy' button because eventually...

2 - You pretty much have to write some code, either in C++ or one of the 2 supported script languages, AngelScript or Lua. The 'structure' of your game is going to most likely live here.

3 - If you use C++ then yes. AngelScript and Lua script files live in the data directory.

-------------------------

jmiller | 2020-08-15 03:40:25 UTC | #3

Re. editors, [wiki:editors](https://github.com/urho3d/Urho3D/wiki#editors) (however incomplete) links to working editors/exporters (e.g. Blender, or other workflows), many of which live here on the forum.

-------------------------

joe | 2020-08-15 05:38:12 UTC | #4

[quote="JTippetts1, post:2, topic:6324"]
2 - You pretty much have to write some code, either in C++
[/quote]

If using C++, does the entire source code of Urho3D get compiled into the game itself or does C++ generate some dll files?

-------------------------

joe | 2020-08-15 05:39:31 UTC | #5

Just one question so with the addon, is it like Armory where it treats Blender like a GUI game editor?

-------------------------

JTippetts1 | 2020-08-15 08:27:46 UTC | #6

If you choose a static build for the library, then no DLL. You can change to shared if you want Urho3D to live in a DLL.

-------------------------

joe | 2020-08-15 08:48:22 UTC | #7

Oh nice, thanks  mate :)

-------------------------

