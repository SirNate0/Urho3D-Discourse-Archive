LtPinecone | 2019-04-02 21:58:14 UTC | #1

hello everyone. I am helping the Open Space Program team with code, and I decided to try and see if I could build the project in VS 2017 on Windows(it is originally linux). We have run into an issue.

First, I was able to build everything just fine, until I came to the the project (which opens in VS fine) 

There is a GetObject reference to the Urho3D::JSON, however VS thinks its something else and references #define GetObject GetObjectA in the wingdi.h file (which is a VS thing.) I have a screen shot. Source code linked below in our GitHub.

![image|690x76](upload://twU7e8rUf3Y2iJB7co6uR1NiaKW.png)

https://github.com/TheOpenSpaceProgram/urho-osp

-------------------------

ab4daa | 2019-04-03 01:16:59 UTC | #2

In PlanetWrenderer.h, delete `#include <Urho3D/Engine/Application.h>` seems work for me.

Probably there is platform specific thing in it, not sure.

-------------------------

jmiller | 2019-04-03 03:02:55 UTC | #3

Hello and welcome to the forum! :confetti_ball:

While I am not being very specific..  `<windows.h>` dumping thousands of macros and types into the global namespace, aka 'namespace pollution', can cause conflicts.

A chunk of code I was using to target MSW:

    #pragma once
    // Somewhat limit windows header namespace pollution.

    #ifdef _WIN32
    #define WIN32_LEAN_AND_MEAN
    #define NOSERVICE
    #define NOMCX
    #define NOIME
    #define NONLS
    #include <windows.h>
    #undef CreateDirectory
    #undef GetClassName
    #undef GetProp
    #undef RemoveProp
    #undef SetProp
    #endif

-------------------------

Leith | 2019-04-03 04:32:44 UTC | #4

At (or near) the top of OspUniverse.cpp, add this:
[code]
#undef GetObject
[/code]
That should resolve the problem, for that file.
I notice that MachineRocket.cpp has the same problem.
Rather than adding it to each cpp file, you could add it to a core .h file, it's up to you.

-------------------------

LtPinecone | 2019-04-03 13:07:34 UTC | #5

Thank you, This worked for me too, however I get another error, it is 

![image|690x44](upload://8DBMYWuwicsXirVVCLpt7uZdid1.png)

-------------------------

ab4daa | 2019-04-03 13:14:27 UTC | #6

add `#include <Urho3D/Core/Context.h>`  :upside_down_face:

-------------------------

LtPinecone | 2019-04-03 13:37:09 UTC | #7

That created 61 errors...
I deleted it after it created the errors, and back to the context issue. it happens on the line here:

![image|467x79](upload://pMZSI7tcXZqOPZPZ9sKjs2gfEz2.png)

-------------------------

ab4daa | 2019-04-17 20:21:47 UTC | #8

What I did is:
1. Delete `#include <Urho3D/Engine/Application.h>` in PlanetWrenderer.h 
2. add `#include <Urho3D/Core/Context.h>` in PlanetTerrain.cpp
3. help `Pow` in PlanetWrenderer.h: `UpdateRange(): m_start(Pow((int)2ul, (int)sizeof(buindex) * 8) - 1u), m_end(0)`

I can build successfully by doing the 3 steps.

-------------------------

LtPinecone | 2019-04-03 15:24:11 UTC | #9

Thank you for the help! It worked, I will add your instructions to our wiki if you don't mind

-------------------------

ab4daa | 2019-04-03 15:23:22 UTC | #11

Glad it helps. :slightly_smiling_face:

-------------------------

LtPinecone | 2019-04-03 15:24:18 UTC | #12

Also, how do I...play the game from Visual Studio? Sorry for the dumb question, I am kind of new to Urho3D.

-------------------------

ab4daa | 2019-04-03 15:46:01 UTC | #13

You mean execute the program?
There is a button with this icon 
![%E5%9C%96%E7%89%87|19x23](upload://tmeemGRA1rAkmryG5Ee1Mnp99Mr.png)

or press F5 I think

EDIT:  remember to right click on the osp project in solution explorer and set it as startup project, then F5 will run osp project.

-------------------------

LtPinecone | 2019-04-03 17:55:01 UTC | #14

I got that, Was able to run it except an exception was thrown causing it to crash. Keeps happening in a random place every time. For example: 

![image|462x112](upload://iiYlDGL56o6nSiBx5CzhDDDxtiL.png)

-------------------------

Leith | 2019-04-04 05:18:58 UTC | #15

That's a breakpoint, a special kind of exception, it's deliberate! Assuming you're on windows, when the breakpoint is reached, examine the "call stack", and double click on the most recent (topmost?) "stack frame" - that should take you to the exact line of sourcecode that contains this "harcoded breakpoint" - likely it will say "__asm {int 3}" or similar. If so, remove it.
If you can't find the breakpoint in the topmost stack frame, then look at the next one before it, which will give you a clue about where the call to the offending code originated, which you can then follow to find the issue.

-------------------------

