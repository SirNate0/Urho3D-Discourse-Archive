wieszak17 | 2021-04-04 15:19:41 UTC | #1

Hello, 

I'm trying to compile project using mingw-w64 on linux for windows. I use cmake_mingw then make, and all goes ok. I copied binary to windows (7) - and it doesn't run - no window appears, while running from cmd it prints nothing. I tried add -DURHO3D_WIN32_CONSOLE=1 and recompile. Result - this time windows show "Program has encountered a bug..." window and nothing more. 
I tried to write simple hello world program and it works both as console (simple printf) and as gui application (open window with some title). So apparently cross compiler works.
I also tried to modify Source/Urho3D/Core/Main.h including printf("kuku01\n"); as first instruction in URHO3D_DEFINE_MAIN to maybe find out where it have problem, but newer get any result - nothing was printed:

    int main(int argc, char** argv) \int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE prevInstance, PSTR cmdLine, int showCmd) \
    { \
        printf("kuku01\n"); \
        Urho3D::ParseArguments(GetCommandLineW()); \
        return function; \
    }

    int main(int argc, char** argv) \
    { \
    printf ("kuku01\n"); \
        Urho3D::ParseArguments(argc, argv); \
        return function; \
    }

(string kuku01 was found in binary) 

Also exactly in same way all urho samples fails.

Urho3D from git, mingw MinGW-w64-v7.0.0_gcc9.3.0-x86_64 on slackware 14.2

What i'm doing wrong?

-------------------------

SirNate0 | 2021-04-04 20:09:42 UTC | #2

Try making sure that you are using the "generic" target and not a "native"(default) one (at least if you are using two different computers). The CMake flag is URHO3D_DEPLOYMENT_TARGET. I think another possible cause would be a missing DLL, though that might have a different error message, I'm not sure.

-------------------------

wieszak17 | 2021-04-04 18:08:46 UTC | #3

Strange. It partially helped. 

./cmake_mingw.sh -DURHO3D_WIN32_CONSOLE=1 -DURHO3D_DEPLOYMENT_TARGET=generic

builds working executable (console one), but

./cmake_mingw.sh -DURHO3D_WIN32_CONSOLE=0 -DURHO3D_DEPLOYMENT_TARGET=generic

fails same way as previous...
Ok, for me there is no practival difference in GUI or console... Thanks for help.

-------------------------

