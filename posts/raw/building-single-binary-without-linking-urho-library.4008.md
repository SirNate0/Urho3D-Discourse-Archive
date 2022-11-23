slapin | 2018-02-12 03:48:26 UTC | #1

When using Urho as separate library, I need to build single tool binary without linking to
Urho library. Is there some flag I could set in CMakeLists.txt for that to happen?

Thanks!

-------------------------

S.L.C | 2018-02-12 03:57:05 UTC | #2

Shouldn't there be `URHO3D_LIB_TYPE` = `STATIC` ?

-------------------------

slapin | 2018-02-12 04:58:02 UTC | #3

Well, I ask about something different.

In my project I need to build a single binary (among others) which do not
reqyuire use of Urho3D library (and conflicts with it at link time).
However this module depends on another project files.
So I want to avoid linking Urho3D library just for this file. How can I approach this?

-------------------------

S.L.C | 2018-02-12 05:08:51 UTC | #4

I'm still confused. Perhaps actual details or examples?

-------------------------

slapin | 2018-02-12 05:42:03 UTC | #5

Please do not elaborate. I will just wait for build system guys help.
@weitjong @Eugene

-------------------------

weitjong | 2018-02-12 05:53:56 UTC | #6

Actually I am as clueless as S.L.C. So I would need the same clarification. 

In any case, if your target does not require Urho3D lib then don’t use our macro to set it up, simply use the CMake own vanilla command for setting up target.

-------------------------

slapin | 2018-02-12 05:59:44 UTC | #7

Well, the problem is that I can't link Urho3D library, but I need to link other libs
which are produced by Urho3D macros, so basically I need everything except for
linking library itself. So ideally I would just set somsthing in CMakeLists.txt and
libUrho3D.a is not linked to a binary produced in that directory. Is it possible?

-------------------------

weitjong | 2018-02-12 06:04:49 UTC | #8

You are not very clear here. Instead of guessing what is your problem and guessing on how to fix it, you will have to elaborate more on what you trying to achieve, especially it sounds like you have a non-standard setup.

-------------------------

slapin | 2018-02-12 06:17:59 UTC | #9

well my setup is standard project with separate library.
Standard build works well.

I add a lot of tool binaries for the project, which do various work, like data importing, etc.
Some of them do not require linking Urho lirary at all, but that is not a problem as long
as there is no conflicts.

Now I need to add tool, which uses separate Recast and Detour libraries, which produce conflict, but depends on project libraries (which are built using Urho3D CMake macros),
but there is no dependency on Urho3D library.

So I want to know easiest way to integrate tools like this into the same project.

-------------------------

weitjong | 2018-02-12 06:26:55 UTC | #10

Not sure I understood your “standard” project entirely. But for what it’s worth, you can check how we setup our Urho host tool targets. A few of them do not depend on Urho3D lib directly too. Look for “nodep” as the keyword. That’s all I could comment for now.

-------------------------

slapin | 2018-02-12 06:56:00 UTC | #11

`setup_main_executable (NODEPS)`

is exactly what I need, thanks a lot for your help!

-------------------------

