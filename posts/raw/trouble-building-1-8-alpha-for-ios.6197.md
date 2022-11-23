jzpekarek | 2020-06-10 04:39:44 UTC | #1

After upgrading from 1.5 to 1.8 alpha, I'm having troubles building Urho3D for iOS (I had it working for 1.5). First, should you be able to use the CMAKE gui to create the Xcode build projects, or is this still a WIP given that it is alpha code? I have a lot of experience on Windows, but not so much with Mac OS and CMAKE, so I always struggle to get the initial projects built (for me, getting the projects to build is the hardest part of using Urho3D). 

When I run the CMAKE configure, I get some messages like below towards the end:

    CMake Warning (dev) at /Applications/CMake.app/Contents/share/cmake-3.17/Modules/FindPackageHandleStandardArgs.cmake:272 (message):
      The package name passed to `find_package_handle_standard_args` (rt) does
      not match the name of the calling package (RT).  This can lead to problems
      in calling code that expects `find_package` result variables (e.g.,
      `_FOUND`) to follow a certain pattern.
    Call Stack (most recent call first):
      Source/ThirdParty/Assimp/cmake-modules/FindRT.cmake:19 (find_package_handle_standard_args)
      Source/ThirdParty/Assimp/code/CMakeLists.txt:854 (FIND_PACKAGE)
    This warning is for project developers.  Use -Wno-dev to suppress it.

    Could NOT find rt (missing: RT_LIBRARY) 
    RT-extension not found. glTF import/export will be built without Open3DGC-compression.
    Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE) 
    Configuring done

Then, if I select the IOS option, and push Generate, I get:

Configuring incomplete, errors occurred!
See also "/Users/jpekarek/Dev/urho3d-1.8a1/CMakeFiles/CMakeOutput.log".
See also "/Users/jpekarek/Dev/urho3d-1.8a1/CMakeFiles/CMakeError.log".

The CMakeOutput.log looks pretty normal, but there is an error at the end of CMakeError.log. As I don't really understand CMake so much, I don't have any idea how to proceed. If this is something that just isn't done yet because it is alpha code, I could wait to get iOS going, and continue developing on Windows for now. Note that I also tried running the command line version of CMake, with different, but equally confusing issues. Any suggestions would be greatly appreciated. 

** BUILD FAILED **
The following build commands failed:
	CompileC CMAKE_TRY_COMPILE.build/Debug/cmTC_21254.build/Objects-normal/x86_64/src.o src.cxx normal x86_64 c++ com.apple.compilers.llvm.clang.1_0.compiler
(1 failure)

Source file was:
#include <stdio.h>
int main() {
char s[80];
int x = 1;
va_list args = {};
vsnprintf_s(s, 80, "Test:%d", args);}

-------------------------

SirNate0 | 2020-06-10 15:22:39 UTC | #2

What versions of CMake and xcode are you using? My impression is that CMake and xcode often have problems unless you have the right versions. Though I've also not developed on a Mac before, so I can't really say....

-------------------------

jzpekarek | 2020-06-12 03:23:40 UTC | #3

CMake version 3.17.3, Xcode version 11.5(11E608c). I just updated to the latest versions of both very recently, maybe they are too new.

-------------------------

SirNate0 | 2020-06-12 18:16:06 UTC | #4

Maybe related, maybe not? 
https://stackoverflow.com/questions/58278260/cant-compile-a-c-program-on-a-mac-after-upgrading-to-catalina-10-15

One question, though: did you create a new build tree for the iOS build? I'm not certain, but I imagine it's like other cross compiling builds and you'll need to tell it to build for iOS before the first Configure or it will select the default native compilers (and you aren't allowed to change the compiler after CMake has created the Cache). If you use script/cmake_ios.sh to create a new build tree (e.g. './script/cmake_ios.sh iosBuild' from the root Urho directory, where iosBuild is the new build directory) it should handle this for you. 

I hope that solves your problem, if not maybe someone with experience with building Urho for iOS can help.

-------------------------

jzpekarek | 2020-06-13 18:25:08 UTC | #5

If I understand correctly, yes I created a new build tree for the iOS build. Also, as I tried different things, I always delete the cache through the CMake gui first. I had also tried the command line cmake_ios.sh, and also got errors (although not the same ones). I guess I'll try to learn more about CMake to see if I can figure out what the cryptic error messages actually mean.

-------------------------

SirNate0 | 2020-06-13 18:50:35 UTC | #6

[quote="jzpekarek, post:5, topic:6197"]
I had also tried the command line cmake_ios.sh, and also got errors (although not the same ones). I guess I’ll try to learn more about CMake to see if I can figure out what the cryptic error messages actually mean.
[/quote]

If you included the errors here someone might be able to provide some more useful assistance. Assuming the errors are different from your first post, which is how I'm reading your statement.

Either way, good luck with it!

-------------------------

jzpekarek | 2020-06-13 19:02:48 UTC | #7

I was reading the stackoverflow post in SirNate0's response, and one suggestion was to add the following CPATH variable
`    export CPATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include`

One question I have, is if I'm trying to build for iOS, should it be one of the iPhoneOS platforms like shown below

`export CPATH=/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/usr/include`

Note that there are quite a few possible permutations (iPhoneOS and iPhoneSimulator for platforms, and iPhoneOS 13.5 and iPhoneOS for the sdk), so I'm not sure which permutation of this path to use either. I had always assumed that you could switch between the simulator and the iOS device within the same Xcode project, so selecting one for the CPATH seems odd.

Or am I totally on the wrong track here? I noticed in the CMAKE gui, that even with IOS selected, all the paths (like IOKIT) reference the MacOSX platform, not the iPhoneOS, but maybe that is intentional?

-------------------------

jzpekarek | 2020-06-14 01:37:41 UTC | #8

I added the following to .zshrc in my home directory, and I was able to run the command line cmake_ios.sh successfully and get an Xcode project.

`export CPATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include`

That was the good news, when I tried to build the Xcode project, it failed on a missing header (winsock.h), which I'm pretty sure is a Windows header, so not sure why it is trying to compile Windows code for iOS. Has anyone seen this before?

I reran cmake_ios.sh with the -DURHO3D_NETWORK=0 option, to remove the network code (I wasn't using it) to get rid of that problem, and then I ran into 'unknown type wchar_t' in the part that compiles SDL. I googled that, and found you can get that from a missing header, but it seems like there should be a missing header error if that was the case. Anyone seen this error before?

-------------------------

Miegamicis | 2020-06-14 12:31:28 UTC | #9

Got the same problem recently with the `wchar_t`. Problem was that while first launching cmake, SDL dependencies was not detected correctly. 

Adding these 2 lines to the main CMakeLists.txt file fixed the problem for me. 
```
include (UrhoCommon)
...
include_directories(/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include)
include_directories(/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk/usr/include)

```

I'm using OSX catalina and tried to use the engine with the XCode.

Not sure why the `winsock.h` is included tho.

-------------------------

