mldevs | 2018-10-12 04:41:45 UTC | #1

Alrighty so here it goes-
If some of y'all recall I asked about it being able to run in an OpenGL context. Well, I had an idea for this. 
As a community, because I do not have time to wok on it myself- work on an integration into an IDE such as Code::Blocks, that will display a rendered view in a separate window/tab whatever of the IDE.
This would work through the use of wxWidget's OpenGL context, Urho3D passes into the wxWidgets OpenGL context, and renders there. Objects put into this scene have the code automatically put in the proper file for the editor to compile. The rendering based of objects that are put in could be done through scripting, maybe? Or it gets put in then the user has to recompile each time. I haven't thought that far. This is to implement the coding side to it, for more dynamic scenes. Heck, static scenes could be made with the current Urho3D editor, then loaded into this plugin/project, with dynamic objects rendered in, as those are code based compared to a file based thing.

Anyway its just an idea.
If anyone wants to take it and run, I will gladly contribute when I have the time.
I know there's lots of ideas for the editor, but hey what's one more? At least this would help to offload some work from the engine itself.

An example of the "write the relevant code" or whatever wording I used is wxWidget's use of wxSmith, to create GUIs

-------------------------

Sinoid | 2018-10-12 06:42:41 UTC | #2

Being tied to any specific render-system guarantees it fails (OpenGL ... barf .... Khronos ... barf).

You'd have better luck trying to convince the Electron team to add arbitrary hosting (need a hosted window to render into).

Sort of shocked you didn't say anything about glTF being the future or such - despite glTF2 being khronos-barf-2.0 (format explicitly refuses to codify animation - that's bad, super bad ... FBX on the other-hand, explicitly defines animation - which is a dream).

---

That's the extent of my rebuttal on the matter of tools. There will be no further comment from me. Technically that'd be illegal since I'm in the US and USC-1036 does forbid that.

-------------------------

rku | 2018-10-16 07:15:34 UTC | #4

[quote="turbo9, post:3, topic:4590"]
Please don’t turn Urho3D into a “Unity”.
[/quote]

It is like saying "please do not bring fast iteration times to urho" and that is not fair. Urho will never loose it's function to work as a library which you seem to prefer. There is nothing wrong in other tools existing side by side.

As for original idea - shoehorning engine into any IDE is just wrong. Quality of such product is questionable. More importantly - every one of us have their favourite IDE and we hate when someone else tells us we should use some other particular IDE we have no love for.

A proper approach imho is having scene editing in a separate tool while that tool works in symbiosis with any IDE user uses. And best part is that we hardly need to do anything in IDE itself to achieve this. Scene editor can handle it all.

-------------------------

rku | 2018-10-16 17:45:51 UTC | #6

Unity/unreal were never lib engines so i do not think they are good examples. I am yet to see a lib engine to turn into editor-not-optional kind of tool.

-------------------------

Modanung | 2018-10-16 22:42:00 UTC | #8

This will likely start as a fork (like [Atomic](https://discourse.urho3d.io/t/atomic-game-engine-mit-urho3d-fork/643)), motivate one or start as a seperate project that extends Urho3D. Nothing to worry. :railway_track:

-------------------------

Sinoid | 2018-10-18 03:07:25 UTC | #9

Objectively, I'd like to see the stuff @rku did for C# binding find its way into core with some moderate improvement (helpers and ease of use). That opens up much more realistically usable tools than a lot of the ImGui stuff many of us have done or are doing.

I deeply regret putting so much time into ImGui instead of revitalizing my older C++/CLI bindings and ATF-based editor and addressing the real problem in that department ... multiple swaps.

It was probably one of the objectively worst calls I've ever made code wise.

-------------------------

