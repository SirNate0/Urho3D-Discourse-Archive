johnnycable | 2017-02-28 22:53:19 UTC | #1

Hello there, I'm an Urho noob coming from cocos2dx. I'm experiencing problems with the standard releases...
I download 1.6 release from the website, and try to build os x release (I have El Capitan 10.11.6, Xcode8.1). Compilation stops with:
>  /usr/local/Urho/Urho3D-1.6/Source/ThirdParty/Civetweb/src/civetweb.c:136:5: Conflicting types for 'clock_gettime'

If I download master release from git directly, compilation is ok, and examples works fine. The Editor, anyway, crashes on a thread with: 

> Thread 10 Crashed:
> 0   Urho3DPlayer                  	0x000000010ea698a7 SDL_RunThread + 71 (SDL_thread.c:274)
> 1   Urho3DPlayer                  	0x000000010ea6aaa5 RunThread + 21 (SDL_systhread.c:74)
> 2   libsystem_pthread.dylib       	0x00007fff9136099d _pthread_body + 131
> 3   libsystem_pthread.dylib       	0x00007fff9136091a _pthread_start + 168
> 4   libsystem_pthread.dylib       	0x00007fff9135e351 thread_start + 13

How can I get around these? Thank you.

-------------------------

weitjong | 2017-03-01 01:53:30 UTC | #2

Welcome to our forums.

I thought this issues was fixed a few months ago in master branch. See [issue #1588](https://github.com/urho3d/Urho3D/issues/1588). Have you set the deployment target correctly in your build?

-------------------------

johnnycable | 2017-03-01 09:43:38 UTC | #3

Thank you for your prompt reply.
So, regarding the issue you pointed out: I'm compiling Urho3D-1.6.tar.gz downloaded from the website on Os X 10.11 (El Capitan) with XCode 8 and mac os X deployment target 10.11 and 10.12 both give rise to the civetweb error.
I'll probably upgrade to Sierra in the next few days but I don't think the problem is that...
commenting out the whole declaration and definition in civetweb.c solves the problem, but this is of course not correct... and there's no sign of guards or checking in the code.
So I'd say the issue is still open on Urho3D-1.6.tar.gz. No sign of it on the master branch.
Can I use the 1.6 editor with the master branch version?

-------------------------

weitjong | 2017-03-01 10:12:49 UTC | #4

The fix (if it works for you also) is only available in the master branch. The compiler define is set by CMake build script, so the guard logic is there and not in the C source code. https://github.com/urho3d/Urho3D/commit/e071b2096768221fcb4b21259cd4a5cf624185e2

-------------------------

johnnycable | 2017-03-01 11:08:15 UTC | #5

Update: rake system for library build works on Urho3D-1.6.tar.gz

> rake cmake URHO3D_C++11=1 URHO3D_SAMPLES=1 URHO3D_TOOLS=1 URHO3D_DOCS=1 URHO3D_EXTRAS=1 CMAKE_BUILD_TYPE=Debug 

> rake make clean_first

works flawlessly, no errors, editor and examples workin. So it's something about Xcode probably.
I remember when you open the xcode project for the first time, xcode asks to 'automatically build targets' that are missing... maybe, in that step? anyway Xcode sees way too much, and gives errors...
Now I'm going to try the master branch, thank you.

-------------------------

weitjong | 2017-03-01 11:43:33 UTC | #6

Your rake command gave you Makefile build tree using AppleClang as compiler. It is a legacy setup that is not being well tested anymore. That setup does not give you iOS build support and universal binary build support. You have to use Xcode (xcodebuild) build tree for that. Passing "xcode" as one of the parameter "rake cmake" command will give you that. Good luck.

-------------------------

