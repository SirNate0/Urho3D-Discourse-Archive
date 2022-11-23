Tinimini | 2017-01-02 01:04:45 UTC | #1

I just found out about Urho3D and I've been trying to get it built on my Mac. I've run ./cmake_macosx.sh osx-Build -DURHO3D_SAMPLES=1 in the root folder (I checked out the source from github) and the build completes without a hitch. But when I open the resulting Urho3D.xcoderpoj and try to build the ALL_BUILD target, I get the following error: "'AssimpPCH.h' file not found. I was wondering if anybody could point me in the right direction to get the build working. Thanks.

-------------------------

sabotage3d | 2017-01-02 01:04:45 UTC | #2

I just build it the other day on Yosemite , it builds perfectly fine. You need to install command-lines tools with Xcode and cmake .

-------------------------

Tinimini | 2017-01-02 01:04:45 UTC | #3

Done that. I didn't get past the first part without command-line tools. But as I said, I've opened the resulting xcode project file in xcode, but that won't build

-------------------------

weitjong | 2017-01-02 01:04:45 UTC | #4

Possibly you have checked out the master branch at the bad time. There was an Xcode build error caused by a recent PR which is now already resolved. So you may want to do another git pull first before retrying.

-------------------------

Tinimini | 2017-01-02 01:04:45 UTC | #5

Just did a pull and started from a clean slate. Redid everything from scratch, but still getting the same error :frowning:

-------------------------

weitjong | 2017-01-02 01:04:45 UTC | #6

Did you also delete the old build tree?

-------------------------

Tinimini | 2017-01-02 01:04:45 UTC | #7

Yup, removed the whole osx-Build directory and ran cmake again with "./cmake_macosx.sh osx-Build -DURHO3D_SAMPLES=1"

-------------------------

weitjong | 2017-01-02 01:04:46 UTC | #8

This is strange. Earlier our Xcode CI builds did flag up build error caused by the recent change in the PCH handling introduced by a PR. A correction was made and all our Xcode CI builds are running fine since then. I am also not able to reproduce your error in my Mac OS X VM. I am using xcodebuild command line to build the generated project (as does our CI build). However, that should not make any differences with building it with Xcode IDE.

-------------------------

weitjong | 2017-01-02 01:04:46 UTC | #9

BTW, I always create my build-tree outside of the Urho3D  project root. Try that and see it makes any difference.

-------------------------

Tinimini | 2017-01-02 01:04:46 UTC | #10

Tried the latest version of cmake (earlier I used homebrew installed 3.1) and building outside of main Urho3d project root. Still failing. Going to try xcodebuild next

-------------------------

Tinimini | 2017-01-02 01:04:46 UTC | #11

Getting the same error from xcodebuild (running it without any command line arguments). 
[code]
CompileC /Users/tinimini/Development/Urho3D-OSX/Source/ThirdParty/Assimp/Urho3D.build/Release/Assimp.build/Objects-normal/x86_64/AssimpPCH.o Source/ThirdParty/Assimp/code/AssimpPCH.cpp normal x86_64 c++ com.apple.compilers.llvm.clang.1_0.compiler
    cd /Users/tinimini/Development/Urho3D
    export LANG=en_US.US-ASCII
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x c++ -arch x86_64 -fmessage-length=181 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit=0 -fcolor-diagnostics -Wno-trigraphs -fpascal-strings -O3 -Wno-missing-field-initializers -Wno-missing-prototypes -Wno-return-type -Wno-non-virtual-dtor -Wno-overloaded-virtual -Wno-exit-time-destructors -Wno-missing-braces -Wparentheses -Wswitch -Wno-unused-function -Wno-unused-label -Wno-unused-parameter -Wno-unused-variable -Wunused-value -Wno-empty-body -Wno-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wno-constant-conversion -Wno-int-conversion -Wno-bool-conversion -Wno-enum-conversion -Wno-shorten-64-to-32 -Wno-newline-eof -Wno-c++11-extensions -DCMAKE_INTDIR=\"Release\" -DURHO3D_SSE -DURHO3D_FILEWATCHER -DURHO3D_PROFILING -DURHO3D_LOGGING -DKNET_UNIX -DURHO3D_OPENGL -DGLEW_STATIC -DGLEW_NO_GLU -DURHO3D_ANGELSCRIPT -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_URHO2D -DURHO3D_STATIC_DEFINE -DHAVE_STDINT_H -DASSIMP_BUILD_BOOST_WORKAROUND -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.10.sdk -fasm-blocks -fstrict-aliasing -Wdeprecated-declarations -Winvalid-offsetof -mmacosx-version-min=10.10 -Wno-sign-conversion -I/Users/tinimini/Development/Urho3D-OSX/Source/ThirdParty/Assimp/Release/include -I/Users/tinimini/Development/Urho3D-OSX/include -I/Users/tinimini/Development/Urho3D-OSX/include/Urho3D/ThirdParty -I/Users/tinimini/Development/Urho3D-OSX/include/Urho3D/ThirdParty/Bullet -I/Users/tinimini/Development/Urho3D/Source/ThirdParty/Assimp/include -I/Users/tinimini/Development/Urho3D/Source/ThirdParty/Assimp/code/BoostWorkaround -I/Users/tinimini/Development/Urho3D/Source/ThirdParty/Assimp/contrib/unzip -I/Users/tinimini/Development/Urho3D-OSX/Source/ThirdParty/Assimp/Urho3D.build/Release/Assimp.build/DerivedSources/x86_64 -I/Users/tinimini/Development/Urho3D-OSX/Source/ThirdParty/Assimp/Urho3D.build/Release/Assimp.build/DerivedSources -Wmost -Wno-four-char-constants -Wno-unknown-pragmas -F/Users/tinimini/Development/Urho3D-OSX/Source/ThirdParty/Assimp/Release -Wno-invalid-offsetof -ffast-math -m64 -DNDEBUG -include AssimpPCH.h -MMD -MT dependencies -MF /Users/tinimini/Development/Urho3D-OSX/Source/ThirdParty/Assimp/Urho3D.build/Release/Assimp.build/Objects-normal/x86_64/AssimpPCH.d --serialize-diagnostics /Users/tinimini/Development/Urho3D-OSX/Source/ThirdParty/Assimp/Urho3D.build/Release/Assimp.build/Objects-normal/x86_64/AssimpPCH.dia -c /Users/tinimini/Development/Urho3D/Source/ThirdParty/Assimp/code/AssimpPCH.cpp -o /Users/tinimini/Development/Urho3D-OSX/Source/ThirdParty/Assimp/Urho3D.build/Release/Assimp.build/Objects-normal/x86_64/AssimpPCH.o
In file included from <built-in>:328:
<command line>:19:10: fatal error: 'AssimpPCH.h' file not found
#include "AssimpPCH.h"
[/code]

-------------------------

weitjong | 2017-01-02 01:04:46 UTC | #12

Which Xcode version do you have? The version used on Travis CI VM is 6.1 and on my personal VM is 5.1.1. If yours is higher than 6.1 then there could be a possibility Apple has improved AppleClang which flags up new issues with our code. If so, perhaps your next course of action is to test by reverting recent changes on using PCH for Assimp library. Comment out the line which says "enable_pch()" in the Source/ThirdParty/Assimp/CMakeLists.txt and rebuild again to see how it goes.

-------------------------

Tinimini | 2017-01-02 01:04:46 UTC | #13

I'm using 6.3. I will try what you suggested and see if that helps

-------------------------

Tinimini | 2017-01-02 01:04:46 UTC | #14

Haa! That seemed to have done the trick. I got it built now. Am able to run the samples now, getting some "check the documentation on how to set the 'resource prefix path'" errors when launching them, but I will figure them out. Thanks for your help!

-------------------------

Tinimini | 2017-01-02 01:04:46 UTC | #15

Ok, I just copied the CoreData and Data folders to my bin folder in my build directory and the samples work now. Now I have a lot of studying to do! :slight_smile:

-------------------------

weitjong | 2017-01-02 01:04:47 UTC | #16

Glad to hear that.  You may help to raise this as an issue in our GitHub issues tracker so we don't forget about fixing  this properly later.

-------------------------

Tinimini | 2017-01-02 01:04:47 UTC | #17

Sure thing!

-------------------------

Tinimini | 2017-01-02 01:04:47 UTC | #18

Here you go: [github.com/urho3d/Urho3D/issues/709](https://github.com/urho3d/Urho3D/issues/709)

-------------------------

weitjong | 2017-01-02 01:04:47 UTC | #19

Could you help me to do one more thing since I don't have latest Xcode to experiment with. Can you temporarily revert back the change that I told you earlier but instead comment out the lines being highlighted here [github.com/urho3d/Urho3D/blob/m ... #L663-L665](https://github.com/urho3d/Urho3D/blob/master/CMake/Modules/Urho3D-CMake-common.cmake#L663-L665). Rebuild and let us know the result. Thanks.

-------------------------

Tinimini | 2017-01-02 01:04:47 UTC | #20

Absolutely! I'll get back to you once I have the time to try it out.

-------------------------

Tinimini | 2017-01-02 01:04:47 UTC | #21

Unfortunately it looks like it's still failing using the fix you suggested.

-------------------------

weitjong | 2017-01-02 01:04:47 UTC | #22

Ok. Thanks for testing it. In that case we will have to investigate it further later.

-------------------------

grumbly | 2017-01-02 01:04:48 UTC | #23

If you're looking to just play around a bit while the XCode build system is fixed, you could try the cmake_generic.sh build process. That's what I use since I've never been able to get the official XCode Mac build script to work for me. I'm using a 2011 Macbook w/ Yosemite and build using the following steps. Anyone who knows better, suggestions please! Note, this is for the current development version of Urho3D available from the github repository (date of this post).

EDIT: I've *facepalm* figured out how to build the xcode version of the latest github code. I've modified the steps below to account for this.

1) Install Homebrew (it makes life easier)
[code]ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"[/code]
2a) Install rake and cmake (using homebrew)
[code]
brew install rake cmake
[/code]
2b) Optionally, install doxygen and graphviz to generate beautiful local documentation
[code]
brew install doxygen graphviz
[/code]
3) Download the Urho3D source either using git or manually.
[code]
git clone https://github.com/urho3d/Urho3D.git urho
[/code]
4) Build the SDK, samples, documentation, extra tools, etc. Set to 0 anything you don't want. Note, when you later want to simply update the sdk based on updated Urho3D source, you won't necessarily need to generate samples, docs, and extras again.
[code]
cd urho
./cmake_generic.sh . -DURHO3D_SAMPLES=1 -DURHO3D_DOCS=1 -DURHO3D_EXTRAS=1
[/code]
5) Use the make command to build Urho3D, specifying the number of cores you can allocate to the task (which helps a lot). I have 4 cores, so...
[code]
make -j4
[/code]
6) Let's copy the sdk portion (include and lib dirs) of what we've built to a folder called 'sdk' just to be clear.
[code]
mkdir sdk
cp -r include lib sdk/
[/code]
7) Create a new dir for your new project, let's call it 'test'.
[code]
rake scaffolding dir=test project=Test target=test
[/code]
8) Your project dir called 'test' should now exist. Now the automated scaffolding has placed the Urho3DPlayer source files as working placeholders in your new project dir. Any source files you place in this dir will be included in a build for your project. In other words, if you add or remove source files, then you need to rerun step 8 commands. Let's create a mac build target for your project, leaving the placeholder code there for now (or replace it with something you're equally confident will work).
[code]
cd test
./cmake_macosx.sh mac-build -DURHO3D_HOME=$PWD/../ -DURHO3D_INCLUDE_DIRS=$PWD/../sdk/include/Urho3D -DURHO3D_LIBRARIES=$PWD/../sdk/lib/libUrho3D.a
[/code]
9) Compile your build for mac.
[code]
cd mac-build
make -j4
[/code]
10) Before running your executable, you'll need the CoreData and Data dirs. Copy (or symbolically link) the bin/CoreData and bin/Data dirs from the base urho dir to your project bin dir.
[code]
cp -r ../../bin/CoreData bin/CoreData
cp -r ../../bin/Data bin/Data
[/code]
11) You will find your executable in the bin dir. The path in total from the root urho dir should be urho/test/mac-build/bin/

I'm still a bumbling noob myself, so hope to get some useful feedback here too (like "why didn't you see obvious thread xyz describing this?" probably)

-------------------------

Tinimini | 2017-01-02 01:04:49 UTC | #24

Nice! Thank you very much. I will try this method out.

-------------------------

