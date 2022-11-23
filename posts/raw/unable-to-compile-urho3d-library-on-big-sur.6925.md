CrazySnail-LLLL | 2021-08-15 03:34:47 UTC | #1

Xcode version: 12.5.1
System version: macOS Big Sur 11.4

CompileC build/macos-xcode/Source/ThirdParty/SDL/Urho3D.build/Release/SDL.build/Objects-normal/arm64/SDL_error.o Source/ThirdParty/SDL/src/SDL_error.c normal arm64 c com.apple. compilers.llvm.clang.1_0.compiler
    cd /Users/liu/Urho3D
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -xc -target arm64-apple-macos11.4 -fmessage-length=91 -fdiagnostics-show-note-include-stack- fmacro-backtrace-limit=0 -fcolor-diagnostics -Wno-trigraphs -fpascal-strings -O3 -Wno-missing-field-initializers -Wno-missing-prototypes -Wno-return-type -Wno-missing-braces -Wparentheses- Wswitch -Wno-unused-function -Wno-unused-label -Wno-unused-parameter -Wno-unused-variable -Wunused-value -Wno-empty-body -Wno-uninitialized -Wno-unknown-pragmas -Wno-shadow- Wno-four-char-constants -Wno-conversion -Wno-constant-conversion -Wno-int-conversion -Wno-bool-conversion -Wno-enum-conversion -Wno-float-conversion -Wno-non-literal-null- conversion -Wno-objc-literal-conversion -Wno-shorten-64-to-32 -Wpointer-sign -Wno-newline-eof -DCMAKE_INTDIR=\"Release\" -DURHO3D_STATIC_DEFINE -DURHO3D_ANGELSCRIPT -DURHO3D_FILEDWATC_I -DURHO3D_FILEWATC_HERI -DURHO3D_HOURING -DURHO3D- DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSI CS -DURHO3D_PROFILING -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -DUSING_GENERATED_CONFIG_H -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.platform/Developer/SDKs/MacOSX.platform/Developer/SDKs/MacOSX. sign-conversion -Wno-infinite-recursion -Wno-comma -Wno-block-capture-autoreleasing -Wno-strict-prototypes -Wno-semicolon-before-method-body -I/Users/liu/Urho3D/build/macos- xcode/Source/ThirdParty/SDL/Release/include -I/Users/liu/Urho3D/build/macos-xcode/Source/ThirdParty/SDL/include/generated -I/Users/liu/Urho3D/Source/ThirdParty/SDL/ include -I/Users/liu/Urho3D/build/macos-xcode/Source/ThirdParty/SDL/Urho3D.build/Release/SDL.build/DerivedSources-normal/arm64 -I/Users/liu/Urho3D/build/macos- xcode/Source/ThirdParty/SDL/Urho3D.build/Release/SDL.build/DerivedSources/arm64 -I/Users/liu/Urho3D/build/macos-xcode/Source/ThirdParty/SDL/Urho3D.build/Release/SDL. build/DerivedSources -F/Users/liu/Urho3D/build/macos-xcode/Source/ThirdParty/SDL/Re lease -pthread -Qunused-arguments -Wno-argument-outside-range -I/Users/liu/Urho3D/Source/ThirdParty/SDL/src/hidapi/hidapi -DNDEBUG -MMD -MT dependencies -MF /Users/liu/Urho3D /build/macos-xcode/Source/ThirdParty/SDL/Urho3D.build/Release/SDL.build/Objects-normal/arm64/SDL_error.d --serialize-diagnostics /Users/liu/Urho3D/build/macos-xcode/ Source/ThirdParty/SDL/Urho3D.build/Release/SDL.build/Objects-normal/arm64/SDL_error.dia -c /Users/liu/Urho3D/Source/ThirdParty/SDL/src/SDL_error.c -o /Users/ liu/Urho3D/build/macos-xcode/Source/ThirdParty/SDL/Urho3D.build/Release/SDL.build/Objects-normal/arm64/SDL_error.o
In file included from /Users/liu/Urho3D/Source/ThirdParty/SDL/src/SDL_error.c:25:
In file included from /Users/liu/Urho3D/Source/ThirdParty/SDL/include/SDL_log.h:40:
/Users/liu/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:453:17: error:
      unknown type name'wchar_t'
extern DECLSPEC wchar_t *SDLCALL SDL_wcsdup(const wchar_t *wstr);
                ^
/Users/liu/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:453:51: error:
      unknown type name'wchar_t'
extern DECLSPEC wchar_t *SDLCALL SDL_wcsdup(const wchar_t *wstr);
                                                  ^
/Users/liu/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:454:49: error:
      unknown type name'wchar_t'
extern DECLSPEC size_t SDLCALL SDL_wcslen(const wchar_t *wstr);
                                                ^
/Users/liu/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:455:66: error:
      unknown type name'wchar_t'
extern DECLSPEC size_t SDLCALL SDL_wcslcpy(SDL_OUT_Z_CAP(maxlen) wchar_t *dst, cons...
                                                                 ^
/Users/liu/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:455:86: error:
      unknown type name'wchar_t'
  ...size_t SDLCALL SDL_wcslcpy(SDL_OUT_Z_CAP(maxlen) wchar_t *dst, const wchar_t *src, ...
                                                                          ^
/Users/liu/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:456:68: error:
      unknown type name'wchar_t'
extern DECLSPEC size_t SDLCALL SDL_wcslcat(SDL_INOUT_Z_CAP(maxlen) wchar_t *dst, co...
                                                                   ^
/Users/liu/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:456:88: error:
      unknown type name'wchar_t'
  ...size_t SDLCALL SDL_wcslcat(SDL_INOUT_Z_CAP(maxlen) wchar_t *dst, const wchar_t *src...
                                                                            ^
/Users/liu/Urho3D/Source/ThirdParty/SDL/include/SDL_stdinc.h:457:46: error:
      unknown type name'wchar_t'
extern DECLSPEC int SDLCALL SDL_wcscmp(const wchar_t *str1, const wchar_t *str2);

-------------------------

weitjong | 2021-07-16 05:49:40 UTC | #2

Welcome to our forum.

It is not enough just putting all the errors from the build. You need to tell us how you generated the build tree in the first place. Did you use our shell script? Currently our script still instructs CMake to use the legacy Xcode build system, even though when Xcode 12 is available. It won’t work with latest Xcode 12 build system yet and the library does not support ARM on macOS yet. 

Until one of the core dev eventually got a new Mac with Big Sur that runs on ARM natively, and then got time to upgrade the SDL to the latest version that support Big Sur, and submit PR to make it work out of the box for other new user, you may encounter a lot of issues along the way at the moment.

-------------------------

S.L.C | 2021-07-16 09:46:11 UTC | #3

Does `wchar_t` exist on macos? Or the build system or code mistook it for Win32? Something doesn't add up.

-------------------------

CrazySnail-LLLL | 2021-07-19 09:25:49 UTC | #4

Sorry, this is the first time I have asked a question on Urho3D's forum.

I use the cmake_xcode.sh script to generate the project, my cmake version is 3.21.0, the type of w_char does exist in xcode12.

-------------------------

weitjong | 2021-07-19 09:44:13 UTC | #5

If you use our provided script then it should at least work using the legacy Xcode build system the CMake still supports. Have you tried to regenerate your build tree again, in case it was caused by some other changes in the Xcode project file after the initial generation. Our CI build currently uses CMake version 3.20.5 without any issue with the default build options. So, if you still having issue in your newly generated build tree then probably you may want to try your luck with that CMake version.

-------------------------

CrazySnail-LLLL | 2021-07-23 01:15:26 UTC | #6

thanks! It work. Use CMake 3.20.5

-------------------------

