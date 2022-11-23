UrOhNo3D | 2017-01-02 01:07:48 UTC | #1

Hi all,

I've been recently trying to build on top of some Urho3D sample code; specifically '36_Urho2DTileMap'. At the most basic level, I have been trying to add a player class which can then interact with the 2D background.

Here is the output that I am currently getting (I am running XCode 7.1 [I have also had the same error running on 6.3.2] on Mac OSX 10.10 to build):
[code]Ld Build/bin/gameexe normal x86_64
    cd /Users/UrOhNo3D/Desktop/urho2dgame
    export MACOSX_DEPLOYMENT_TARGET=10.10
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -arch x86_64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.10.sdk -L/Users/UrOhNo3D/Desktop/urho2dgame/Build/bin -F/Users/UrOhNo3D/Desktop/urho2dgame/Build/bin -filelist /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/gameexe.LinkFileList -mmacosx-version-min=10.10 -framework AudioUnit -framework Carbon -framework Cocoa -framework CoreAudio -framework ForceFeedback -framework IOKit -framework OpenGL -framework CoreServices -Wl,-search_paths_first -Wl,-headerpad_max_install_names /Users/UrOhNo3D/CEED-Internal/native-Build/lib/libUrho3D.a -ldl -Xlinker -dependency_info -Xlinker /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/gameexe_dependency_info.dat -o /Users/UrOhNo3D/Desktop/urho2dgame/Build/bin/gameexe

duplicate symbol __ZN6Sample14InitTouchInputEv in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample5StartEv in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample5SetupEv in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample4StopEv in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample10CreateLogoEv in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample21SetWindowTitleAndIconEv in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample24CreateConsoleAndDebugHudEv in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol _ui in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZTV6Sample in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZTS6Sample in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZTI6Sample in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol _cache in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample14SetLogoVisibleEb in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6SampleC2EPN6Urho3D7ContextE in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6SampleC1EPN6Urho3D7ContextE in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample13HandleKeyDownEN6Urho3D10StringHashERNS0_7HashMapIS1_NS0_7VariantEEE in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample16HandleTouchBeginEN6Urho3D10StringHashERNS0_7HashMapIS1_NS0_7VariantEEE in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
duplicate symbol __ZN6Sample17HandleSceneUpdateEN6Urho3D10StringHashERNS0_7HashMapIS1_NS0_7VariantEEE in:
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/main.o
    /Users/UrOhNo3D/Desktop/urho2dgame/Build/game.build/Debug/gameexe.build/Objects-normal/x86_64/player.o
ld: 18 duplicate symbols for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)[/code]

Some Googling has led me to believe that this issue relates to the way in which files are included, rather anything syntax-related, and so I think it is reasonable to assume that all other relevant Urho3D files are adequately included.

The source files I have, and the files they include are as follows:
[b]Main.cpp:[/b]
#include "main.h"
#include "player.h"

[b]Main.h:[/b]
#include "Sample.h"

[b]Player.cpp:[/b]
#include "main.h"
#include "player.h"

[b]Player.h:[/b]
no includes


In the header files, I also include
[code]#ifndef NAME_OF_FILE_H
#define NAME_OF_FILE_H
<header_file_contents>
#endif[/code] to ensure that if they are referenced multiple times, they are not considered as duplicates.


If anybody is able to help me with this, it would be hugely appreciated! Thanks!

-------------------------

