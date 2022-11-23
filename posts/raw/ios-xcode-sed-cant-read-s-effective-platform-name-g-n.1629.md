shlomok | 2017-01-02 01:09:04 UTC | #1

Dear All,
I am trying to build for IOS as the target. I successfully compile and run all the examples when my target is OSX, but all my attempts to compile for IOS failed. 
What I did is (How do I attach/upload images here ...?):
Download the latest source code
Run ./cmake_ios.sh

[code]
nsa-000:Urho3D-1.5 freebsd$ ./cmake_ios.sh   /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/
-- The C compiler identification is AppleClang 7.0.2.7000181
-- The CXX compiler identification is AppleClang 7.0.2.7000181
-- Check for working C compiler using: Xcode
-- Check for working C compiler using: Xcode -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Xcode
-- Check for working CXX compiler using: Xcode -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
2015-12-27 22:01:35.608 xcodebuild[50716:704381] [MT] PluginLoading: Required plug-in compatibility UUID F41BD31E-2683-44B8-AE7F-5F09E919790E for plug-in at path '~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/MarmaladeGCC.xcplugin' not present in DVTPlugInCompatibilityUUIDs
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
-- Found Doxygen: /usr/local/bin/doxygen (found version "1.8.9.1") 
-- Could NOT find Dot (missing:  DOXYGEN_DOT_EXECUTABLE) 
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5
-- post_cmake: Fix generated Xcode project
nsa-000:Urho3D-1.5 freebsd$ 
[/code]

I then open the project in Xcode, and run the ALL_BUILD target which results in:
(tolua++ fails complaining about SED and post install script)

[code]
-- The C compiler identification is AppleClang 7.0.2.7000181
-- The CXX compiler identification is AppleClang 7.0.2.7000181
-- Check for working C compiler using: Xcode
-- Check for working C compiler using: Xcode -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Xcode
-- Check for working CXX compiler using: Xcode -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build
cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && /opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-configure
echo "Performing build step for 'tolua++'"
Performing build step for 'tolua++'
[b][size=150][color=#BF0040]cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && bash -c "sed -i '' 's/EFFECTIVE_PLATFORM_NAME//g' CMakeScripts/install_postBuildPhase.make*"
sed: can't read s/EFFECTIVE_PLATFORM_NAME//g: No such file or directory[/color][/size][/b]
make: *** [/Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-build] Error 2

[/code]

What am I doing wrong? 

Any help would be greatly appreciated.

-------------------------

shlomok | 2017-01-02 01:09:04 UTC | #2

The full error:
[code]
PhaseScriptExecution CMake\ Rules Urho3D.build/Debug-iphoneos/POST_CMAKE_FIXES.build/Script-81ABED168ABE48E1B2FFE7FB.sh
    cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5
    /bin/sh -c /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Urho3D.build/Debug-iphoneos/POST_CMAKE_FIXES.build/Script-81ABED168ABE48E1B2FFE7FB.sh

echo "Applying post-cmake fixes"
Applying post-cmake fixes
sed -i '' 's/EFFECTIVE_PLATFORM_NAME//g' /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/CMakeScripts/install_postBuildPhase.make* || exit 0
sed: can't read s/EFFECTIVE_PLATFORM_NAME//g: No such file or directory
Command /bin/sh emitted errors but did not return a nonzero exit code to indicate failure

[/code]

-------------------------

weitjong | 2017-01-02 01:09:05 UTC | #3

Welcome to our forum.

Which version of CMake are you using? Can you do this in a terminal/console:

[code]$ ls -ltr /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/CMakeScripts/install_postBuildPhase.make*[/code]
Due to a bug in CMake/Xcode generator ([github.com/urho3d/Urho3D/blob/m ... 1750-L1766](https://github.com/urho3d/Urho3D/blob/master/CMake/Modules/Urho3D-CMake-common.cmake#L1750-L1766), and repeat your attempt to build.

-------------------------

shlomok | 2017-01-02 01:09:05 UTC | #4

Hi,
Thank you very much for your reply, I am glad to help.

[code]
nsa-000:bin freebsd$ ls -ltr /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/CMakeScripts/install_postBuildPhase.make*
-rw-r--r--  1 freebsd  staff  226 Dec 27 22:43 /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/CMakeScripts/install_postBuildPhase.makeRelease
-rw-r--r--  1 freebsd  staff  226 Dec 27 22:43 /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/CMakeScripts/install_postBuildPhase.makeRelWithDebInfo
-rw-r--r--  1 freebsd  staff  226 Dec 27 22:43 /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/CMakeScripts/install_postBuildPhase.makeDebug
[/code]

and i have cmake 3.1.3:

[code]
nsa-000:bin freebsd$ cmake --version
cmake version 3.1.3
CMake suite maintained and supported by Kitware (kitware.com/cmake).
[/code]

I did what you asked and commented out the section in build-common but I still have the same error:

[code]
PhaseScriptExecution CMake\ Rules Source/Urho3D/Urho3D.build/Debug-iphonesimulator/tolua++.build/Script-9CC35DF222A54313B4B669C4.sh
    cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5
    /bin/sh -c /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/Urho3D.build/Debug-iphonesimulator/tolua++.build/Script-9CC35DF222A54313B4B669C4.sh

echo "Creating directories for 'tolua++'"
Creating directories for 'tolua++'
/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/ThirdParty/toluapp/src/bin
/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build
/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix
/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/tmp
/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator
/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src
/opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-mkdir
echo "No download step for 'tolua++'"
No download step for 'tolua++'
/opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-download
echo "No update step for 'tolua++'"
No update step for 'tolua++'
/opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-update
echo "No patch step for 'tolua++'"
No patch step for 'tolua++'
/opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-patch
echo "Performing configure step for 'tolua++'"
Performing configure step for 'tolua++'
cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && /usr/bin/env -i PATH=/opt/local/bin:/opt/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Applications/Marmalade.app/Contents/s3e/bin /opt/local/bin/cmake -DURHO3D_LUAJIT=OFF -DDEST_RUNTIME_DIR=/Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/bin/tool -DBAKED_CMAKE_SOURCE_DIR=/Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5 -GXcode /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/ThirdParty/toluapp/src/bin
-- The C compiler identification is AppleClang 7.0.2.7000181
-- The CXX compiler identification is AppleClang 7.0.2.7000181
-- Check for working C compiler using: Xcode
-- Check for working C compiler using: Xcode -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Xcode
-- Check for working CXX compiler using: Xcode -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build
cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && /opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-configure
echo "Performing build step for 'tolua++'"
Performing build step for 'tolua++'
cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && bash -c "sed -i '' 's/EFFECTIVE_PLATFORM_NAME//g' CMakeScripts/install_postBuildPhase.make*"
sed: can't read s/EFFECTIVE_PLATFORM_NAME//g: No such file or directory
make: *** [/Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-build] Error 2
[/code]

and:

[code]
echo "Creating directories for 'tolua++'"


Creating directories for 'tolua++'


/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/ThirdParty/toluapp/src/bin


/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build


/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix


/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/tmp


/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator


/opt/local/bin/cmake -E make_directory /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src


/opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-mkdir


echo "No download step for 'tolua++'"


No download step for 'tolua++'


/opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-download


echo "No update step for 'tolua++'"


No update step for 'tolua++'


/opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-update


echo "No patch step for 'tolua++'"


No patch step for 'tolua++'


/opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-patch


echo "Performing configure step for 'tolua++'"


Performing configure step for 'tolua++'


cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && /usr/bin/env -i PATH=/opt/local/bin:/opt/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Applications/Marmalade.app/Contents/s3e/bin /opt/local/bin/cmake -DURHO3D_LUAJIT=OFF -DDEST_RUNTIME_DIR=/Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/bin/tool -DBAKED_CMAKE_SOURCE_DIR=/Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5 -GXcode /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/ThirdParty/toluapp/src/bin


-- The C compiler identification is AppleClang 7.0.2.7000181


-- The CXX compiler identification is AppleClang 7.0.2.7000181


-- Check for working C compiler using: Xcode


-- Check for working C compiler using: Xcode -- works


-- Detecting C compiler ABI info


-- Detecting C compiler ABI info - done


-- Check for working CXX compiler using: Xcode


-- Check for working CXX compiler using: Xcode -- works


-- Detecting CXX compiler ABI info


-- Detecting CXX compiler ABI info - done


-- Configuring done


-- Generating done


-- Build files have been written to: /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build


cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && /opt/local/bin/cmake -E touch /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-configure


echo "Performing build step for 'tolua++'"


Performing build step for 'tolua++'


cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && bash -c "sed -i '' 's/EFFECTIVE_PLATFORM_NAME//g' CMakeScripts/install_postBuildPhase.make*"


sed: can't read s/EFFECTIVE_PLATFORM_NAME//g: No such file or directory


make: *** [/Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-stamp/Debug-iphonesimulator/tolua++-build] Error 2

[/code]

Any more ideas? I am happy to try.

-------------------------

weitjong | 2017-01-02 01:09:05 UTC | #5

If you are running CMake version prior to 3.4 then you can ignore the step I have commented earlier as it does not applicable to your CMake version. Are you using "genuine" Mac OS X or Hackintosh?  :wink:   Or are you running with macport or homebrew installation? Because my next suspicion is on the "sed" command itself. Notice that we call this command with a few command line arguments.

[code]sed -i '' 's/EFFECTIVE_PLATFORM_NAME//g' /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/CMakeScripts/install_postBuildPhase.make*[/code]
Your error message looks like it attempted to use 's/EFFECTIVE_PLATFORM_NAME//g' as the name of the file to be processed, which of course does not exist. Perhaps the command line argument passing is being messed up by the '' argument for the -i. The sed command that we have tested before all expects this '' argument for the -i, but I would not be surprise if somehow your version can do it without especially if you acquire it from elsewhere. Try remove the '' in the custom command that I have highlighted earlier and retry again. You can of course just try the altered command directly in a terminal also to speed up the test.

-------------------------

weitjong | 2017-01-02 01:09:05 UTC | #6

One more thing. You probably need to nuke your build tree for each test because tolua++ target for iOS is configured using so-called CMake "ExternalProjectAdd" macro. If you know where the tolua++ external project build tree resided then you can simply just nuke this build tree instead of the whole Urho3D project build tree. When in doubt, just nuke everything.

-------------------------

shlomok | 2017-01-02 01:09:06 UTC | #7

Thanks :slight_smile:
I am using a real MAC. Indeed running this manually works:
[code]
nsa-000:Urho3D-1.5 freebsd$ cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && bash -c "sed -i '' 's/EFFECTIVE_PLATFORM_NAME//g' CMakeScripts/install_postBuildPhase.make*"
sed: can't read s/EFFECTIVE_PLATFORM_NAME//g: No such file or directory
nsa-000:tolua++-build freebsd$ cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Urho3D/tolua++-prefix/src/tolua++-build && bash -c "sed -i  's/EFFECTIVE_PLATFORM_NAME//g' CMakeScripts/install_postBuildPhase.make*"
nsa-000:tolua++-build freebsd$ 
[/code]
Returns without an error, but the change in Urho3D-CMake-common.cmake [b]has no effect.[/b] 

Do I need to remove the '' in some other scripts?:
POST_CMAKE_FIXES_cmakeRulesBuildPhase.makeDebug
POST_CMAKE_FIXES_cmakeRulesBuildPhase.makeRelease
POST_CMAKE_FIXES_cmakeRulesBuildPhase.makeRelWithDebInfo
tolua++_cmakeRulesBuildPhase.makeDebug
tolua++_cmakeRulesBuildPhase.makeRelease
tolua++_cmakeRulesBuildPhase.makeRelWithDebInfo

I removed all of them and I have a new error now:
[code]
Ld Source/Samples/01_HelloWorld/Urho3D.build/Debug-iphonesimulator/01_HelloWorld.build/Objects-normal/x86_64/01_HelloWorld normal x86_64
    cd /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5
    export IPHONEOS_DEPLOYMENT_TARGET=9.2
    export PATH="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/usr/bin:/Applications/Xcode.app/Contents/Developer/usr/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -arch x86_64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator9.2.sdk -L/Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/bin -F/Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/bin -filelist /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Samples/01_HelloWorld/Urho3D.build/Debug-iphonesimulator/01_HelloWorld.build/Objects-normal/x86_64/01_HelloWorld.LinkFileList -mios-simulator-version-min=9.2 -Xlinker -objc_abi_version -Xlinker 2 -framework AudioToolbox -framework CoreAudio -framework CoreGraphics -framework Foundation -framework OpenGLES -framework QuartzCore -framework UIKit -Wl,-search_paths_first -Wl,-headerpad_max_install_names /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/lib/libUrho3D.a -ldl -Xlinker -dependency_info -Xlinker /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Samples/01_HelloWorld/Urho3D.build/Debug-iphonesimulator/01_HelloWorld.build/Objects-normal/x86_64/01_HelloWorld_dependency_info.dat -o /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/Source/Samples/01_HelloWorld/Urho3D.build/Debug-iphonesimulator/01_HelloWorld.build/Objects-normal/x86_64/01_HelloWorld

duplicate symbol _main in:
    /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/lib/libUrho3D.a(CMakeCXXCompilerId.o)
    /Users/freebsd/repo/dev/games-engines/ios/Urho3D-1.5/lib/libUrho3D.a(SDL_uikitappdelegate.o)
ld: 1 duplicate symbol for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
[/code]

Is that related to removing the '' from the sed command?

-------------------------

weitjong | 2017-01-02 01:09:06 UTC | #8

[quote="shlomok"]Is that related to removing the '' from the sed command?[/quote]
In a way, yes. But more precisely the main culprit is the "sed" command itself. As I already mentioned in my other comment, our build system relies on "sed" to behave as we have expected it. Your "sed", however, is not. So, if our build system has problem in the post-cmake custom target for iOS then you can expect breakage in other places as well because the command is used several times through out the build system. I am still wondering why the "sed" behave differently in your Mac OS X though. Which version of Mac OS X are you using? Do you have macport or homebrew?

-------------------------

shlomok | 2017-01-02 01:09:06 UTC | #9

I moved to using OSX, but I really need it on IOS. I am using brew. 
Meanwhile:
[code]
uname -a
Darwin nsa-000.local 15.2.0 Darwin Kernel Version 15.2.0: Fri Nov 13 19:56:56 PST 2015; root:xnu-3248.20.55~2/RELEASE_X86_64 x86_64
[/code]

I used both version of sed as in here:
[sagebionetworks.jira.com/wiki/d ... sed+on+OSx](https://sagebionetworks.jira.com/wiki/display/PLFM/Fixing+sed+on+OSx)

Can you tell me which sed version/distro should I work with?

-------------------------

shlomok | 2017-01-02 01:09:06 UTC | #10

Problem resolved:

[code]
nsa-000:Urho3D-1.5 freebsd$ sudo rm -rf /usr/local/bin/sed
nsa-000:Urho3D-1.5 freebsd$ sudo ln -s /usr/local/bin/gsed /usr/local/bin/sed
[/code]

Thank you all for helping me out!

BTW, the min version is now IOS 9.2, do I need to specify a parameter somewhere to support 9.0? 
Thanks.

-------------------------

weitjong | 2017-01-02 01:09:06 UTC | #11

You are welcome. For your last question,  you can use IPHONEOS_DEPLOYMENT_TARGET build option to specify your min target.

-------------------------

