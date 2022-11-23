Taymindis | 2017-11-18 22:56:22 UTC | #1

I’ve recently watch a link below that he can runtime compile. 
https://youtu.be/uRf0LXjZWO0 

Does anyone have instruction to setup this?

-------------------------

johnnycable | 2017-11-19 11:17:15 UTC | #2

https://github.com/RuntimeCompiledCPlusPlus/RuntimeCompiledCPlusPlus/wiki/Alternatives

which turns to be:

https://github.com/pamarcos/Urho3D/tree/RCCpp

https://discourse.urho3d.io/t/runtime-compiled-c-in-urho3d-aka-scripting-in-c/318

This is interesting. When I have a moment, I'll into this... anyway it's from 2014...

-------------------------

johnnycable | 2017-11-19 17:16:49 UTC | #3

Forgot to mention the recent attempt with Cling by @godan [here](https://discourse.urho3d.io/t/use-clang-to-compile-urho/3723)

-------------------------

Pablo | 2017-11-19 19:29:22 UTC | #4

Actually, RuntimeCompiledCplusPlus is not used in the PoC I did for Urho3D a few years ago. You should be able to test RCCpp by simply compiling Urho3D with support for it (https://github.com/pamarcos/Urho3D/blob/RCCpp/RCCpp.sh). You will also need to copy the `Data` and `CoreData` folders into your `Build/bin` directory.

For RCCpp to find your Urho3D includes you need to set the URHO3D_HOME environment variable before running Urho3DPlayer:

`URHO3D_HOME=~/GameDev/Urho3D/Build/ ./Urho3DPlayer Data/RCCpp/24_Urho2DSprite/Urho2DSprite.cpp`

-------------------------

Taymindis | 2017-11-20 09:52:48 UTC | #5

Hi Pablo, 

Have tried latest version but 

n file included from /Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCpp.cpp:34:
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppFile.h:35:5: error: unknown type name 'OBJECT'
    OBJECT(RCCppFile);
    ^
In file included from /Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCpp.cpp:35:
In file included from /Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCpp.h:33:
In file included from /Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppImpl.h:30:
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppObject.h:37:5: error: unknown type name 'OBJECT'
    OBJECT(RCCppObject);
    ^
In file included from /Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCpp.cpp:35:
In file included from /Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCpp.h:33:
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppImpl.h:39:5: error: unknown type name 'OBJECT'
    OBJECT(RCCppImpl);
    ^
In file included from /Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCpp.cpp:35:
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCpp.h:45:5: error: unknown type name 'OBJECT'
    OBJECT(CompilationThread);
    ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCpp.h:60:5: error: unknown type name 'OBJECT'
    OBJECT(RCCpp);
    ^
In file included from /Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCpp.cpp:36:
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:31:7: error: C++ requires a type specifier for all declarations
EVENT(E_RCCPP_COMPILATION_STARTED, RCCppCompilationStarted)
      ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:31:36: error: unknown type name 'RCCppCompilationStarted'
EVENT(E_RCCPP_COMPILATION_STARTED, RCCppCompilationStarted)
                                   ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:31:1: error: C++ requires a type specifier for all declarations
EVENT(E_RCCPP_COMPILATION_STARTED, RCCppCompilationStarted)
^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:33:11: error: use of undeclared identifier 'P_FILE'
    PARAM(P_FILE, CompileFile);
          ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:33:19: error: use of undeclared identifier 'CompileFile'
    PARAM(P_FILE, CompileFile);
                  ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:36:7: error: C++ requires a type specifier for all declarations
EVENT(E_RCCPP_COMPILATION_FINISHED, RCCppCompilationFinished)
      ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:36:37: error: unknown type name 'RCCppCompilationFinished'
EVENT(E_RCCPP_COMPILATION_FINISHED, RCCppCompilationFinished)
                                    ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:36:1: error: C++ requires a type specifier for all declarations
EVENT(E_RCCPP_COMPILATION_FINISHED, RCCppCompilationFinished)
^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:38:11: error: use of undeclared identifier 'P_SUCCESSFUL'
    PARAM(P_SUCCESSFUL, CompilationSuccessful);
          ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:38:25: error: use of undeclared identifier 'CompilationSuccessful'
    PARAM(P_SUCCESSFUL, CompilationSuccessful);
                        ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:39:11: error: use of undeclared identifier 'P_FILE'
    PARAM(P_FILE, CompiledFile);
          ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:39:19: error: use of undeclared identifier 'CompiledFile'
    PARAM(P_FILE, CompiledFile);
                  ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:40:11: error: use of undeclared identifier 'P_OUTPUT'
    PARAM(P_OUTPUT, CompilationOutput);
          ^
/Users/taymindis/MyGit/Urho3D/Source/Urho3D/RCCpp/RCCppEvents.h:40:21: error: use of undeclared identifier 'CompilationOutput'
    PARAM(P_OUTPUT, CompilationOutput);
                    ^

-------------------------

Pablo | 2017-11-20 10:13:20 UTC | #6

What do you mean with latest version? Are you using the latest commit of my RCCpp branch? That should be `b94a0a71ec8fd42fbbc6bde0d240b40801d47210`. If by latest you mean merging the latest of Urho3D into the RCCpp branch, you'd probably need to do some work in the CMake files to make it work again.

-------------------------

Taymindis | 2017-11-20 10:19:41 UTC | #7

I see. Noted with Thanks

-------------------------

