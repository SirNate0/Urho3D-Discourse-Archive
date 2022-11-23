rogerdv | 2017-01-02 01:01:29 UTC | #1

This weekend I started working on my project on Linux, after I had some code in place I decided to try how it owrked on Windows. Created the project without problems, but I got a lot of syntax errors with Application class:

[code]
     1>d:\projects\keyw\source\GameState.h(23): error C2061: error de sintaxis : identificador 'Application'
     1>d:\projects\keyw\source\GameState.h(31): error C2143: error de sintaxis : falta ';' delante de '*'
     1>d:\projects\keyw\source\GameState.h(31): error C4430: falta el especificador de tipo; se presupone int. Nota: C++ no admite default-int
     1>d:\projects\keyw\source\GameState.h(23): error C2065: 'parent' : identificador no declarado[/code]

This is the code:

[code]#include "Application.h"
#include "Engine.h"
#include "CoreEvents.h"
#include "SceneEvents.h"
#include "Input.h"

#pragma once

using namespace Urho3D;

class GameState
{
	public:
		GameState(Application *ap) { parent = ap; } ;[/code]

The project compiles and runs perfectly under linux, the problem is only when compiling with VS 2012.

-------------------------

thebluefish | 2017-01-02 01:01:30 UTC | #2

Is that really the full code, or only a snippet? Pretty much everything vital is missing, could you instead post the whole project or temporarily host it on Github?

-------------------------

rogerdv | 2017-01-02 01:01:30 UTC | #3

It is just the first header causing the error (there are mucho more problems, derived from this). My solution was to restart the project using AS instead of C++. Now the app is a minimal launcher and I will implement everything in scripts, including classes. Also, I plan to spend more development time in Windows instead of Linux.

-------------------------

