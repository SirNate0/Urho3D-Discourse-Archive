johnnycable | 2017-04-05 18:00:43 UTC | #1

Hello, I try to compile for release and I get the following error:

> In file included from /Users/max/Developer/Stage/Workspace/Urho/terza/src/terza.cpp:8:
> In file included from /usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/Core/CoreEvents.h:25:
> In file included from /usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/Core/../Core/Object.h:25:
> /usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/Core/../Container/LinkedList.h:31:10: fatal error: 
>       'initializer_list' file not found
 #include <initializer_list
> 1 error generated.
> ** BUILD FAILED **

> The following build commands failed:
> 	CompileC build/ios/Release/terza.build/Release-iphoneos/terza.build/Objects-normal/armv7/terza.o src/terza.cpp normal armv7 c++ com.apple.compilers.llvm.clang.1_0.compiler
> (1 failure)

Looks related to standard libraries... Funny enough, I don't get any when I build in debug mode, and the only difference is -DCMAKE_BUILD_TYPE=Debug instead or Release...
I have Os X 10.12.3, Xcode 8.2.1, Urho3d 1.6

-------------------------

Eugene | 2017-04-05 19:18:08 UTC | #2

Have you enabled URHO3D_C++11 in CMake?

-------------------------

johnnycable | 2017-04-05 20:58:05 UTC | #3

Xcodebuild log:

urho3d library (sample):

CompileC build/ios/Release/Source/Urho3D/Urho3D.build/Release-iphoneos/Urho3D.build/Objects-normal/arm64/GPUObject.o Source/Urho3D/Graphics/GPUObject.cpp normal arm64 c++ com.apple.compilers.llvm.clang.1_0.compiler
    cd /usr/local/Urho/Urho3D-1.6
    export LANG=en_US.US-ASCII
    export PATH="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin:/Applications/Xcode.app/Contents/Developer/usr/bin:/Users/max/.pyenv/shims:/Users/max/.rbenv/shims:/Users/max/Developer/Workshop/Util:/usr/local/android/ndk-bundle:/usr/local/android/build-tools/25.0.0:/usr/local/android/platform-tools:/usr/local/android/tools:/usr/local/android:/Users/max/Developer/Setup/gaming:/Users/max/Developer/Setup:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:."
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x c++ -arch arm64 -fmessage-length=100 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit=0 -fcolor-diagnostics -Wno-trigraphs -fpascal-strings -O3 -Wno-missing-field-initializers -Wno-missing-prototypes -Wno-return-type -Wno-non-virtual-dtor -Wno-overloaded-virtual -Wno-exit-time-destructors -Wno-missing-braces -Wparentheses -Wswitch -Wno-unused-function -Wno-unused-label -Wno-unused-parameter -Wno-unused-variable -Wunused-value -Wno-empty-body -Wno-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wno-constant-conversion -Wno-int-conversion -Wno-bool-conversion -Wno-enum-conversion -Wshorten-64-to-32 -Wno-newline-eof -Wno-c++11-extensions -DCMAKE_INTDIR=\"Release-iphoneos\" -DURHO3D_FILEWATCHER -DURHO3D_PROFILING -DURHO3D_LOGGING -DURHO3D_THREADING -DURHO3D_STATIC_DEFINE -DURHO3D_ANGELSCRIPT -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_URHO2D **-DURHO3D_CXX11** -DIOS -DHAVE_STDINT_H -DHAVE_UNDERSCORE_SINCOSF -DURHO3D_IS_BUILDING -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS10.2.sdk -fstrict-aliasing -Wdeprecated-declarations -Winvalid-offsetof -miphoneos-version-min=10.2 -Wno-sign-conversion -Wno-infinite-recursion -Wno-move -fembed-bitcode-marker -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/lib/include -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/Source/Urho3D -I/usr/local/Urho/Urho3D-1.6/Source/Urho3D -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/ThirdParty -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/ThirdParty/Bullet -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/ThirdParty/Detour -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/Source/Urho3D/Urho3D.build/Release-iphoneos/Urho3D.build/DerivedSources/arm64 -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/Source/Urho3D/Urho3D.build/Release-iphoneos/Urho3D.build/DerivedSources -Wmost -Wno-four-char-constants -Wno-unknown-pragmas -F/usr/local/Urho/Urho3D-1.6/build/ios/Release/lib -DSTBI_NEON **-std=c++11** -Wno-invalid-offsetof -ffast-math -pthread -Qunused-arguments -DNDEBUG -include /usr/local/Urho/Urho3D-1.6/build/ios/Release/Source/Urho3D/SharedPrecompiledHeaders/Precompiled-bunybqfnygdhqzddlwbykoomzukg/Precompiled.h -MMD -MT dependencies -MF /usr/local/Urho/Urho3D-1.6/build/ios/Release/Source/Urho3D/Urho3D.build/Release-iphoneos/Urho3D.build/Objects-normal/arm64/GPUObject.d --serialize-diagnostics /usr/local/Urho/Urho3D-1.6/build/ios/Release/Source/Urho3D/Urho3D.build/Release-iphoneos/Urho3D.build/Objects-normal/arm64/GPUObject.dia -c /usr/local/Urho/Urho3D-1.6/Source/Urho3D/Graphics/GPUObject.cpp -o /usr/local/Urho/Urho3D-1.6/build/ios/Release/Source/Urho3D/Urho3D.build/Release-iphoneos/Urho3D.build/Objects-normal/arm64/GPUObject.o

app output:

CompileC build/ios/Release/terza.build/Release-iphoneos/terza.build/Objects-normal/armv7/terza.o src/terza.cpp normal armv7 c++ com.apple.compilers.llvm.clang.1_0.compiler
    cd /Users/max/Developer/Stage/Workspace/Urho/terza
    export LANG=en_US.US-ASCII
    export PATH="/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin:/Applications/Xcode.app/Contents/Developer/usr/bin:/Users/max/.pyenv/shims:/Users/max/.rbenv/shims:/Users/max/Developer/Workshop/Util:/usr/local/android/ndk-bundle:/usr/local/android/build-tools/25.0.0:/usr/local/android/platform-tools:/usr/local/android/tools:/usr/local/android:/Users/max/Developer/Setup/gaming:/Users/max/Developer/Setup:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:."
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x c++ -arch armv7 -fmessage-length=100 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit=0 -fcolor-diagnostics -Wno-trigraphs -fpascal-strings -O3 -Wno-missing-field-initializers -Wno-missing-prototypes -Wno-return-type -Wno-non-virtual-dtor -Wno-overloaded-virtual -Wno-exit-time-destructors -Wno-missing-braces -Wparentheses -Wswitch -Wno-unused-function -Wno-unused-label -Wno-unused-parameter -Wno-unused-variable -Wunused-value -Wno-empty-body -Wno-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wno-constant-conversion -Wno-int-conversion -Wno-bool-conversion -Wno-enum-conversion -Wno-shorten-64-to-32 -Wno-newline-eof -Wno-c++11-extensions -DCMAKE_INTDIR=\"Release-iphoneos\" -DURHO3D_PROFILING -DURHO3D_LOGGING -DURHO3D_THREADING -DURHO3D_STATIC_DEFINE -DURHO3D_ANGELSCRIPT -DURHO3D_LUA -DTOLUA_RELEASE -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_URHO2D **-DURHO3D_CXX1**1 -DIOS -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS10.2.sdk -fstrict-aliasing -Wdeprecated-declarations -Winvalid-offsetof -miphoneos-version-min=3.0 -Wno-sign-conversion -Wno-infinite-recursion -Wno-move -I/Users/max/Developer/Stage/Workspace/Urho/terza/build/ios/Release/bin/include -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/include -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/ThirdParty -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/ThirdParty/Bullet -I/usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/ThirdParty/Lua -I/Users/max/Developer/Stage/Workspace/Urho/terza/build/ios/Release/terza.build/Release-iphoneos/terza.build/DerivedSources/armv7 -I/Users/max/Developer/Stage/Workspace/Urho/terza/build/ios/Release/terza.build/Release-iphoneos/terza.build/DerivedSources -Wmost -Wno-four-char-constants -Wno-unknown-pragmas -F/Users/max/Developer/Stage/Workspace/Urho/terza/build/ios/Release/bin -DSTBI_NEON **-std=c++11** -Wno-invalid-offsetof -ffast-math -pthread -Qunused-arguments -DNDEBUG -MMD -MT dependencies -MF /Users/max/Developer/Stage/Workspace/Urho/terza/build/ios/Release/terza.build/Release-iphoneos/terza.build/Objects-normal/armv7/terza.d --serialize-diagnostics /Users/max/Developer/Stage/Workspace/Urho/terza/build/ios/Release/terza.build/Release-iphoneos/terza.build/Objects-normal/armv7/terza.dia -c /Users/max/Developer/Stage/Workspace/Urho/terza/src/terza.cpp -o /Users/max/Developer/Stage/Workspace/Urho/terza/build/ios/Release/terza.build/Release-iphoneos/terza.build/Objects-normal/armv7/terza.o
In file included from /Users/max/Developer/Stage/Workspace/Urho/terza/src/terza.cpp:8:
In file included from /usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/Core/CoreEvents.h:25:
In file included from /usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/Core/../Core/Object.h:25:
/usr/local/Urho/Urho3D-1.6/build/ios/Release/include/Urho3D/Core/../Container/LinkedList.h:31:10: fatal error: 
      **'initializer_list' file not found**
include <initializer_list>
         ^
1 error generated.

** BUILD FAILED **


The following build commands failed:
	CompileC build/ios/Release/terza.build/Release-iphoneos/terza.build/Objects-normal/armv7/terza.o src/terza.cpp normal armv7 c++ com.apple.compilers.llvm.clang.1_0.compiler
(1 failure)



----------
I don't get it. Both release and debug options are the same...

-------------------------

Eugene | 2017-04-05 21:11:43 UTC | #4

Then... Does your compiler support C++11?
It seems that no.
You may not enable URHO3D_C++11 in this case.

-------------------------

johnnycable | 2017-04-06 15:19:39 UTC | #5

Gotcha. Took me some time to figure it out...
-DIPHONEOS_DEPLOYMENT_TARGET=3.0
I set this option and this gets ios back to the times it didn't support C++...
The compiler is ok and every other option for c++ too
Thank you for the help!

-------------------------

