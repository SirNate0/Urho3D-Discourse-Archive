umen | 2017-01-02 01:09:01 UTC | #1

Hey i try to build the engine with the examples in Xcode 7.2 into the device 
my IPhone is using iOS 8.2 , when i try to lower the deployment target it doesn't give any option 
is it Xcode problem or Urho3d settings ? 
also i executed the cmake script like this :

[code]
meirs-Mac-mini:Urho3D meiryanovich$ ./cmake_ios.sh /Users/meiryanovich/Documents/3d/Urho3D/git/build_ios -DURHO3D_SAMPLES=1 -DIPHONEOS_DEPLOYMENT_TARGET=7.0
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
2015-12-25 14:42:55.352 xcodebuild[2751:53095] [MT] PluginLoading: Required plug-in compatibility UUID F41BD31E-2683-44B8-AE7F-5F09E919790E for plug-in at path '~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/Unity4XC.xcplugin' not present in DVTPlugInCompatibilityUUIDs
2015-12-25 14:42:55.353 xcodebuild[2751:53095] [MT] PluginLoading: Required plug-in compatibility UUID F41BD31E-2683-44B8-AE7F-5F09E919790E for plug-in at path '~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/MarmaladeGCC.xcplugin' not present in DVTPlugInCompatibilityUUIDs
2015-12-25 14:42:55.353 xcodebuild[2751:53095] Failed to load plugin at: /Users/meiryanovich/Library/Application Support/Developer/Shared/Xcode/Plug-ins/MarmaladeGCC.xcplugin, skipping.  Reason for failure: *** -[__NSPlaceholderDictionary initWithObjects:forKeys:count:]: attempt to insert nil object from objects[0]
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
-- Build files have been written to: /Users/meiryanovich/Documents/3d/Urho3D/git/build_ios
-- post_cmake: Fix generated Xcode project

[/code]

[img]http://i.imgur.com/qSitl1u.png[/img]

-------------------------

weitjong | 2017-01-02 01:09:02 UTC | #2

Have you checked the "Deployment Target" setting in the generated Xcode project?

-------------------------

umen | 2017-01-02 01:09:02 UTC | #3

i did try this :
[img]http://i.imgur.com/6RiR1qy.png[/img]
but it still don't let me to change deployment target in all the projects.

-------------------------

umen | 2017-01-02 01:09:02 UTC | #4

This is kind of strange and confusing .
in the documentation is written that you should build from "Build_All" target but it haven't  gave me the option to select Deployment target below the latest 9.2 
BUT ....
if i select individual projects for example 23_Water example i can change the Deployment target to 7.0 or 8.0 and it compiles fine but there is Deployment target bug when i try to deploy to my iPhone 
i will open new thread on the subject.

[code]
2015-12-26 09:13:11.850 23_Water[1486:864806] Skipped autoload path 'Autoload' as it does not exist, check the documentation on how to set the 'resource prefix path'
[/code]

-------------------------

