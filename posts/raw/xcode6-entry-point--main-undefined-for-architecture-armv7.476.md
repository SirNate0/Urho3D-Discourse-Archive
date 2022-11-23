umen | 2017-01-02 01:00:44 UTC | #1

Hey all 
after few months i coming back to check the engine ,
i must say i had the same or neer same problem befor , i dont remmber how this was fixed . 
[url]http://discourse.urho3d.io/t/linking-error-when-creating-new-project-in-osx-10-9-2-xcode/205/6[/url]

This time its the example Urho3dPlayer  that failed to link . and there is new Xcode 6 . with new IOS 8 sdk  

1. clone it from git , 
running the cmake_ios.sh -DURHO3D_SAMPLES
[code]
meirs-Mac-mini:Urho3D meiryanovich$ ./cmake_ios.sh -DURHO3D_SAMPLES=1
-- The C compiler identification is Clang 6.0.0
-- The CXX compiler identification is Clang 6.0.0
-- Check for working C compiler using: Xcode
-- Check for working C compiler using: Xcode -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Xcode
-- Check for working CXX compiler using: Xcode -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for include file stdint.h
-- Looking for include file stdint.h - not found
-- The ASM compiler identification is Clang
-- Found assembler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Failed
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Failed
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Failed
-- Performing Test COMPILER_HAS_DEPRECATED
-- Performing Test COMPILER_HAS_DEPRECATED - Failed
-- Found Urho3D: as CMake target
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build
[/code]

2 .opning Urho3D.xcodeproj in Xcode 6 , 
3. setting IOS deployment to 7.0 ( as this is what is installed in my device ) 
4. setting my developer profile from apple in the Urho3dPlayer project 
5. compiling the Urho3dPlayer project  
Boom! linking error :
[code]
Ld /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Tools/Urho3DPlayer/Urho3D.build/Debug-iphoneos/Urho3DPlayer.build/Objects-normal/armv7/Urho3DPlayer normal armv7
    cd /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/Source
    export IPHONEOS_DEPLOYMENT_TARGET=7.0
    export PATH="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin:/Applications/Xcode.app/Contents/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -arch armv7 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS8.0.sdk -L/Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Bin -F/Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Bin -filelist /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Tools/Urho3DPlayer/Urho3D.build/Debug-iphoneos/Urho3DPlayer.build/Objects-normal/armv7/Urho3DPlayer.LinkFileList -dead_strip -framework AudioToolbox -framework CoreAudio -framework CoreGraphics -framework Foundation -framework OpenGLES -framework QuartzCore -framework UIKit -Wl,-search_paths_first -Wl,-headerpad_max_install_names /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Lib/libUrho3D.a -ldl -lpthread -lpthread -lpthread -ldl -lpthread -lpthread -miphoneos-version-min=7.0 -Xlinker -dependency_info -Xlinker /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Tools/Urho3DPlayer/Urho3D.build/Debug-iphoneos/Urho3DPlayer.build/Objects-normal/armv7/Urho3DPlayer_dependency_info.dat -o /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Tools/Urho3DPlayer/Urho3D.build/Debug-iphoneos/Urho3DPlayer.build/Objects-normal/armv7/Urho3DPlayer

ld: entry point (_main) undefined. for architecture armv7
clang: error: linker command failed with exit code 1 (use -v to see invocation)
[/code]

when im doing lipo im getting :
[code]
meirs-Mac-mini:ios-Lib meiryanovich$ lipo -detailed_info libUrho3D.a 
Fat header in: libUrho3D.a
fat_magic 0xcafebabe
nfat_arch 2
architecture armv7
    cputype CPU_TYPE_ARM
    cpusubtype CPU_SUBTYPE_ARM_V7
    offset 48
    size 93139064
    align 2^2 (4)
architecture arm64
    cputype CPU_TYPE_ARM64
    cpusubtype CPU_SUBTYPE_ARM64_ALL
    offset 93139112
    size 92866672
    align 2^2 (4)
meirs-Mac-mini:ios-Lib meiryanovich$ 
[/code]

the Urho3DPlayer.app binary never created
what im doing wrong here ?
Thanks

-------------------------

weitjong | 2017-01-02 01:00:44 UTC | #2

Not exactly sure why you have this problem. Our CI build for iOS builds successfully for both 64- and 32-bit using Xcode 6 and iOS 8.0 SDK but targeting 7.0, which is exactly the same as your build configuration minus the signing part.

I would suggest you try to start from scratch again but this time add the build option -DURHO3D_64BIT=0, if you intend to build for 32-bit. We have changed the default value for that build option recently. It now defaulted to 64-bit on Xcode as per new documentation. HTH.

-------------------------

umen | 2017-01-02 01:00:46 UTC | #3

today i did:
[code]meirs-Mac-mini:Urho3D meiryanovich$ ./cmake_clean.sh 
meirs-Mac-mini:Urho3D meiryanovich$ ./cmake_ios.sh -DURHO3D_64BIT=0 -DURHO3D_SAMPLES=1[/code]

compiled and still the same compilation error : 
[code]
Ld /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Bin/Urho3DPlayer.app/Urho3DPlayer normal armv7
    cd /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/Source
    export IPHONEOS_DEPLOYMENT_TARGET=7.0
    export PATH="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin:/Applications/Xcode.app/Contents/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -arch armv7 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS8.0.sdk -L/Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Bin -F/Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Bin -filelist /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Tools/Urho3DPlayer/Urho3D.build/Debug-iphoneos/Urho3DPlayer.build/Objects-normal/armv7/Urho3DPlayer.LinkFileList -dead_strip -framework AudioToolbox -framework CoreAudio -framework CoreGraphics -framework Foundation -framework OpenGLES -framework QuartzCore -framework UIKit -Wl,-search_paths_first -Wl,-headerpad_max_install_names /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Lib/libUrho3D.a -ldl -lpthread -lpthread -lpthread -ldl -lpthread -lpthread -miphoneos-version-min=7.0 -Xlinker -dependency_info -Xlinker /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Tools/Urho3DPlayer/Urho3D.build/Debug-iphoneos/Urho3DPlayer.build/Objects-normal/armv7/Urho3DPlayer_dependency_info.dat -o /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Bin/Urho3DPlayer.app/Urho3DPlayer

ld: entry point (_main) undefined. for architecture armv7
clang: error: linker command failed with exit code 1 (use -v to see invocation)

[/code]

also when i move the deployment to use the simulator im getting other set of errors i don't know if they are related 
[code]
Ld /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Samples/01_HelloWorld/Urho3D.build/Debug-iphonesimulator/01_HelloWorld.build/Objects-normal/i386/01_HelloWorld normal i386
    cd /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/Source
    export IPHONEOS_DEPLOYMENT_TARGET=7.0
    export PATH="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/usr/bin:/Applications/Xcode.app/Contents/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -arch i386 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator8.0.sdk -L/Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Bin -F/Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Bin -filelist /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Samples/01_HelloWorld/Urho3D.build/Debug-iphonesimulator/01_HelloWorld.build/Objects-normal/i386/01_HelloWorld.LinkFileList -Xlinker -objc_abi_version -Xlinker 2 -framework AudioToolbox -framework CoreAudio -framework CoreGraphics -framework Foundation -framework OpenGLES -framework QuartzCore -framework UIKit -Wl,-search_paths_first -Wl,-headerpad_max_install_names /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Lib/libUrho3D.a -ldl -lpthread -lpthread -lpthread -Xlinker -no_implicit_dylibs -mios-simulator-version-min=7.0 -Xlinker -dependency_info -Xlinker /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Samples/01_HelloWorld/Urho3D.build/Debug-iphonesimulator/01_HelloWorld.build/Objects-normal/i386/01_HelloWorld_dependency_info.dat -o /Users/meiryanovich/Documents/3d/urho3d/git/Urho3D/ios-Build/Samples/01_HelloWorld/Urho3D.build/Debug-iphonesimulator/01_HelloWorld.build/Objects-normal/i386/01_HelloWorld

Undefined symbols for architecture i386:
  "_FT_Done_Face", referenced from:
      Urho3D::FontFaceFreeType::~FontFaceFreeType() in libUrho3D.a(FontFaceFreeType.o)
      Urho3D::FontFaceFreeType::Load(unsigned char const*, unsigned int, int) in libUrho3D.a(FontFaceFreeType.o)
  "_FT_Done_FreeType", referenced from:
      Urho3D::FreeTypeLibrary::~FreeTypeLibrary() in libUrho3D.a(FontFaceFreeType.o)
  "_FT_Get_First_Char", referenced from:
      Urho3D::FontFaceFreeType::Load(unsigned char const*, unsigned int, int) in libUrho3D.a(FontFaceFreeType.o)
  "_FT_Get_Next_Char", referenced from:
      Urho3D::FontFaceFreeType::Load(unsigned char const*, unsigned int, int) in libUrho3D.a(FontFaceFreeType.o)
  "_FT_Get_Sfnt_Table", referenced from:
      Urho3D::FontFaceFreeType::Load(unsigned char const*, unsigned int, int) in libUrho3D.a(FontFaceFreeType.o)
  "_FT_Init_FreeType", referenced from:
      Urho3D::FreeTypeLibrary::FreeTypeLibrary(Urho3D::Context*) in libUrho3D.a(FontFaceFreeType.o)
  "_FT_Load_Char", referenced from:
      Urho3D::FontFaceFreeType::LoadCharGlyph(unsigned int, Urho3D::Image*) in libUrho3D.a(FontFaceFreeType.o)

and so on ... 

[/code]

Do you have some other idea or direction on what is wrong ?

-------------------------

umen | 2017-01-02 01:00:46 UTC | #4

any body successfully compile the engine with Xcode 6 Not on simulator but on device ?

-------------------------

sabotage3d | 2017-01-02 01:01:04 UTC | #5

I would revert to Xcode 5 if you are targeting IOS 7.1 . There are too many bugs and problems than solutions.
Urho3D works perfectly fine on IOS 7.1 compiled with Xcode 5 .

-------------------------

umen | 2017-01-02 01:01:05 UTC | #6

xcode 5 is absolute in apple world , 
its only xcode 6 now , i will try to work on it .

-------------------------

sabotage3d | 2017-01-02 01:01:09 UTC | #7

Btw have you tried Urho3d on IOS 8 are there are any problems ?
 Technically if SDL do not update to IOS 8 Urho itself won't work.

-------------------------

umen | 2017-01-02 01:01:09 UTC | #8

tried on simulator my device is still 7.1

-------------------------

umen | 2017-01-02 01:01:37 UTC | #9

Hey im sorry to say that the problem is still remain the same , i dont know if its just in my case but its hardly to believe as allot of frameworks i do compile out of the box , cocos2d-x , gameplay3d .. 
but this i just can't compile for iOS , is there any body here that successfully compile the framework 1.3.2 on XOS 10.10 with Xcode 6.1 for iphone 5 with ios 8.1 ?
using cmake_ios.sh ?

-------------------------

sabotage3d | 2017-01-02 01:01:37 UTC | #10

I am following some threads over SDL compatibility for IOS 8 it is still not perfect but you could try this : [bitbucket.org/slime73/sdl-exper ... provements](https://bitbucket.org/slime73/sdl-experiments/branch/iOS-improvements)
You can try and compile it with Urho 3d and fix any compatibility issues . I will try it as well in the coming weeks. The official SDL IOS 8 status it is not ready .

-------------------------

umen | 2017-01-02 01:01:37 UTC | #11

Thanks for the response , 
how do you know that the problem is SDL ? from what i see in the SDL2 forums there is not issue to compile for iOS 8 , im not sure i want to make modified SDL version . 
also how can it be you managed to compile for iOS 8 and i dont ? im not Xcode expert but i guess we did the same thing cloning fresh code and running cmake_ios.sh

-------------------------

xpol | 2017-01-02 01:01:37 UTC | #12

Same here with make_macosx.sh and Xcode 6.

1. fresh clone the source
2. ./cmake_macosx.sh
3. open project with Xcode 6
4. build

Got lots of error saying:

[quote]Undefined symbols for architecture x86_64:[/quote]

-------------------------

sabotage3d | 2017-01-02 01:01:39 UTC | #13

As far as I can see this has already been solved here : [github.com/urho3d/Urho3D/issues/498](https://github.com/urho3d/Urho3D/issues/498)

-------------------------

umen | 2017-01-02 01:01:39 UTC | #14

well it is probbly working for @antont , 
but for me this is not working i have no idea why .

-------------------------

