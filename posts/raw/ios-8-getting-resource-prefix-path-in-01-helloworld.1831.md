umen | 2017-01-02 01:10:30 UTC | #1

I try to compile the latest engine code in xcode 7.2 targeting iOS 8 on deploying on real device 

getting the error: 
[code]2016-03-01 22:27:37.866 01_HelloWorld[9930:9231097] Created 1 worker thread
2016-03-01 22:27:37.875 01_HelloWorld[9930:9231097] Added resource path /private/var/mobile/Containers/Bundle/Application/847EADB8-09D2-4825-9E74-97C17EA8CAE1/01_HelloWorld.app/Data/
2016-03-01 22:27:37.877 01_HelloWorld[9930:9231097] Added resource path /private/var/mobile/Containers/Bundle/Application/847EADB8-09D2-4825-9E74-97C17EA8CAE1/01_HelloWorld.app/CoreData/
2016-03-01 22:27:37.877 01_HelloWorld[9930:9231097] Skipped autoload path 'Autoload' as it does not exist, check the documentation on how to set the 'resource prefix path'[/code]

i executed:
[code]./cmake_ios.sh /Users/meiryanovich/Documents/3d/Urho3D/Urho3D_2/build-tree -DURHO3D_SAMPLES=1[/code]

what is wrong here ?
Thanks

-------------------------

weitjong | 2017-01-02 01:10:30 UTC | #2

Unless the sample app did not run correctly otherwise you don't have to worry about the last log entry. Perhaps the only problem here is the wording of debug log entry itself when the autoload feature is not being used.

-------------------------

umen | 2017-01-02 01:10:30 UTC | #3

The sample didn't run , it got error 
Can't continue

-------------------------

weitjong | 2017-01-02 01:10:30 UTC | #4

I recall you have reported your problem before. Our build system defaults to the latest iOS version for the deployment target for a given iOS SDK you are using. Since you are targeting lower iOS version, I believe you may need to pass the "IPHONEOS_DEPLOYMENT_TARGET" build option. Good luck.

-------------------------

umen | 2017-01-02 01:10:30 UTC | #5

Ok i will try it , later 
Thanks

-------------------------

umen | 2017-01-02 01:10:32 UTC | #6

I added the the parameter and now i executed like this :
[code]meirs-Mac-mini:Urho3D meiryanovich$ ./cmake_ios.sh /Users/meiryanovich/Documents/3d/Urho3D/Urho3D_2/build-tree -DURHO3D_SAMPLES=1 -DIPHONEOS_DEPLOYMENT_TARGET=8.0
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
2016-03-02 19:57:00.057 xcodebuild[677:10483] [MT] PluginLoading: Required plug-in compatibility UUID F41BD31E-2683-44B8-AE7F-5F09E919790E for plug-in at path '~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/Unity4XC.xcplugin' not present in DVTPlugInCompatibilityUUIDs
2016-03-02 19:57:00.059 xcodebuild[677:10483] [MT] PluginLoading: Required plug-in compatibility UUID F41BD31E-2683-44B8-AE7F-5F09E919790E for plug-in at path '~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/MarmaladeGCC.xcplugin' not present in DVTPlugInCompatibilityUUIDs
2016-03-02 19:57:00.060 xcodebuild[677:10483] Failed to load plugin at: /Users/meiryanovich/Library/Application Support/Developer/Shared/Xcode/Plug-ins/MarmaladeGCC.xcplugin, skipping.  Reason for failure: *** -[__NSPlaceholderDictionary initWithObjects:forKeys:count:]: attempt to insert nil object from objects[0]
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
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/meiryanovich/Documents/3d/Urho3D/Urho3D_2/build-tree
-- post_cmake: Fix generated Xcode project
meirs-Mac-mini:Urho3D meiryanovich$ 
[/code]

when i run the helloworld from xcode i got exception that looks like this :
[img]http://i.imgur.com/aqYZVcs.png[/img]

by the the app do run from the iphone device when i stop the xcode session

-------------------------

sabotage3d | 2017-01-02 01:10:32 UTC | #7

Might be SDL related. Are you using the latest Urho3D with SDL 2.0.4?

-------------------------

umen | 2017-01-02 01:10:33 UTC | #8

yes i cloned it from the github , the master .

-------------------------

