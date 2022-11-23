tbutton2005 | 2019-05-16 16:43:59 UTC | #1

when i create staticmodel, editor closes. why?

-------------------------

Leith | 2019-05-10 02:17:17 UTC | #2

Can I assume that you downloaded the latest sourcecode from https://github.com/urho3d/Urho3D ?
And you are using Linux?

I have the same issue - there is a bug in the latest version of the editor.
If you download the older Urho3D 1.7 sourcecode from https://urho3d.github.io/ you will find that copy of the editor will work - and you can copy that working binary into your more recent source folder with no problems.

-------------------------

tbutton2005 | 2019-05-10 05:59:26 UTC | #3

yes, im using latest version from github.
no, i use windows

-------------------------

tbutton2005 | 2019-05-10 06:34:01 UTC | #4

thanks, editor urho3d 1.7 does works! ![tex1|690x227](upload://sQsGOe3uyktZni4B6eWa3WjAUVE.png)

-------------------------

JTippetts | 2019-05-10 18:20:31 UTC | #6

Out of curiosity, has anyone figured out what the issue with the editor is? Maybe we can get a pull request together to fix it.

-------------------------

Leith | 2019-05-11 01:48:00 UTC | #7

From where I stand (Linux), this issue appears to be something to do with selecting objects in the scene - at least that is part of the issue - application crashes silently when attempting to select any scene object. No error is logged. I have not attempted to reproduce the issue under gdb so I currently have no firm details on exactly what exception is being triggered or where. Note that I can create scene objects, but I can't select them for manipulation purposes.
Now I hear there is a similar issue in the Windows build! I was not expecting to hear that :P

-------------------------

weitjong | 2019-05-11 14:58:44 UTC | #8

See https://github.com/urho3d/Urho3D/issues/2384. Retested using Fedora 30 with GCC 9.0.1 and the Editor didn't crash on me.

-------------------------

weitjong | 2019-05-12 09:54:14 UTC | #9

I have upgraded AS in the "upgrade-angelscript" dev branch which contains some upstream bug fixes. I would appreciate feedback if it resolves the issue here.

-------------------------

Leith | 2019-05-12 09:41:59 UTC | #10

I will look into it tomorrow, I'm fried for today, the teaching course is much more challenging than expected - hopeful for an instant fix, but happy to be part of the solution.

-------------------------

weitjong | 2019-05-12 10:05:17 UTC | #11

One of the CI (Clang STATIC) build test failed due to segfault when test running the Editor, which is great because now I may have a deterministic way to reproduce the issue just by using CI instead of launching my MacOS VM.

-------------------------

weitjong | 2019-05-14 15:47:12 UTC | #12

I am observing a weird behavior from AS in the Editor that I cannot yet explain. Somehow it only happens for me when I build using the latest Clang version that Fedora 30 provides. It also means I have a way to reproduce the “issue” locally now. What I am not sure at this moment is whether it is the same issue at all because what I have now with Clang is the same with CI, segfault on starting up.

EDIT: Unfortunately it is different issue.

-------------------------

weitjong | 2019-05-16 02:31:32 UTC | #13

I am able to reproduce the segfault after a component (e.g. Light component) is selected in the Editor locally using my Ubuntu VM yesterday night. Hopefully it would make finding the root cause easier using this Linux VM later when I got time. Should all the attempts fail then I would probably consider to push Lezak's workaround into the branch.

p.s. The Editor scripts are very ugly as the result of all these years of individual patching :)

-------------------------

JTippetts | 2019-05-16 02:54:25 UTC | #14

Ugly code == Bugfixed code. Be proud of all those hairs and warts, because each one of them was hard-earned.

-------------------------

Modanung | 2019-05-16 17:02:48 UTC | #15

@cadaver often mentioned how the editor that comes with the engine is mainly a neat AngelScript demo. Maybe this is a nice opportunity to consider forking the [**rbfx** editor](https://github.com/rokups/rbfx/tree/master/Source/Tools/Editor) that was written in the meantime?
It *should* be quite compatible..[spoiler] with the C# bits surgically removed.[/spoiler]
[details="Screenshot"]
![Screenshot](https://user-images.githubusercontent.com/19151258/49943614-09376980-fef1-11e8-88fe-8c26fcf30a59.jpg)
[/details]

-------------------------

weitjong | 2019-05-19 08:05:35 UTC | #16

I have committed a change in the Editor script to ensure the intended method binding for the `StringHash::operator ==()` is being called.

https://github.com/urho3d/Urho3D/commit/c8469ba8c3991a941151d55836a09ffe391bbd52

-------------------------

Modanung | 2019-05-20 18:45:34 UTC | #17

Oh, and there's also [Atomic Editor](https://github.com/AtomicGameEngine/AtomicGameEngine/tree/master/Source/AtomicEditor) of course.

-------------------------

