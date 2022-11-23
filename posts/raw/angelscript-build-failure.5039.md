pleduc | 2019-03-18 10:31:38 UTC | #1

hye, first thanks for your so great work...
im trying to use Urho3d on ios/tvos/emcc tag 1.7 as external librairie,
with the fips ( cmake ) toolchain...
but i get:

Install/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:31:
Install/include/Urho3D/ThirdParty/AngelScript/wrap16.h:18:11: error: 
      argument may not have 'void' type
                Proxy(T value) : value(value) {}
                        ^

it work when i set the AS_IS_BUILDING to true ( but should not be )
but then i get error on registering function at run time.

all is working well on linux, macos, android.
this is really blocking me.
i looked over c++ version support but did not figure it out...
hope i am in the right place for this question... 
thanks

-------------------------

Leith | 2019-03-18 10:33:12 UTC | #2

Welcome to the community! :confetti_ball:
I'm not the right guy to deal with build issues, he will be along soon. Hang in there! It's going to be ok :)

-------------------------

Modanung | 2019-03-18 10:34:32 UTC | #3

Welcome! :confetti_ball: :slightly_smiling_face: 
Have you tried using the latest master branch instead of the pre-built library?

-------------------------

weitjong | 2019-03-18 10:47:45 UTC | #4

[quote="pleduc, post:1, topic:5039"]
with the fips ( cmake ) toolchain…
[/quote]

I am afraid you are on your own on this one. First time I heard anyone using that for Urho3D building.

-------------------------

pleduc | 2019-03-18 11:00:50 UTC | #5

ok, few precision, i'm building my own static lib from 1.7 tag ( as i need stable ) from the normal build flow ( urho cmake ) then i build my own surcharge of urho3d kinked as lib with https://github.com/floooh/fips. 
i just do not get the error kind as it seems to be c++ kind template wired stuff....

-------------------------

weitjong | 2019-03-18 13:36:18 UTC | #6

As our resources are limited, we cannot possibly support all kind of new build tools out there. If I were you, I would double check my compiler defines. This is my educated guess of what possibly went wrong and probably my last comment for this thread. Good luck.

-------------------------

S.L.C | 2019-03-18 16:17:10 UTC | #7

You probably omitted the actual source of the error. By the looks of it, something is causing the `Proxy` template from `wrap16.h` header to be instantiated as `Proxy< void >`. Which is a no-no for the compiler if you look at what that template tries to achieve.

But you don't show the full trace-back of the error to see what causes the whole issue. Actually, I don't even know what you're trying to do. Whether this gets caused by your code or the engine itself.

This issue seems very particular to your case because you made it so by choosing an alternate build-system.

-------------------------

pleduc | 2019-03-18 16:34:52 UTC | #8

first, thanks for your reactivity and consideration of this pb.
the pb only appear on arm arch ( simulator build is ok )

here the full stask, just in case:

  /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x c++ -arch arm64 -fmessage-length=109 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit=0 -fcolor-diagnostics -std=c++11 -stdlib=libc++ -Wno-trigraphs -fpascal-strings -O0 -Wno-missing-field-initializers -Wno-missing-prototypes -Wno-return-type -Wno-non-virtual-dtor -Wno-overloaded-virtual -Wno-exit-time-destructors -Wno-missing-braces -Wparentheses -Wswitch -Wno-unused-function -Wno-unused-label -Wno-unused-parameter -Wno-unused-variable -Wunused-value -Wno-empty-body -Wno-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wno-constant-conversion -Wno-int-conversion -Wno-bool-conversion -Wno-enum-conversion -Wno-float-conversion -Wno-non-literal-null-conversion -Wno-objc-literal-conversion -Wshorten-64-to-32 -Wno-newline-eof -Wno-c++11-extensions -DCMAKE_INTDIR=\"Debug-iphoneos\" -DURHO3D_LOGGING -DIOS -DURHO3D_CXX11 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS12.1.sdk -fstrict-aliasing -Wdeprecated-declarations -Winvalid-offsetof -miphoneos-version-min=9.0 -g -Wno-sign-conversion -Wno-infinite-recursion -Wno-move -Wno-comma -Wno-block-capture-autoreleasing -Wno-strict-prototypes -Wno-range-loop-analysis -Wno-semicolon-before-method-body -index-store-path /Users/ifs/Library/Developer/Xcode/DerivedData/hop-ddoobgobcrcyhyekfdcnylptxlpm/Index/DataStore -I/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Build/lib/include -I/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include -I/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty -I/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/SQLite -I/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/libcurl/ios-x86_64-release/Install/include -I/Users/ifs/work/wks-ifs/hop/Sources/Engine -I/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Toolbox -I/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/OS -I/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Storage -I/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Data -I/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/UI -I/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/TV -I/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Backend -I/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Media -I/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Build/Engine/Framework/hop.build/Debug-iphoneos/Framework.build/DerivedSources/arm64 -I/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Build/Engine/Framework/hop.build/Debug-iphoneos/Framework.build/DerivedSources -Wmost -Wno-four-char-constants -Wno-unknown-pragmas -F/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Build/lib -fstrict-aliasing -Wno-multichar -Wall -Wextra -Wno-unused-parameter -Wno-unknown-pragmas -Wno-ignored-qualifiers -Wno-long-long -Wno-overloaded-virtual -Wno-unused-volatile-lvalue -Wno-deprecated-writable-strings -std=c++11 -D_DEBUG_ -D_DEBUG -DCMART_DEBUG=1 -std=gnu++11 -MMD -MT dependencies -MF /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Build/Engine/Framework/hop.build/Debug-iphoneos/Framework.build/Objects-normal/arm64/BackendScript.d --serialize-diagnostics /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Build/Engine/Framework/hop.build/Debug-iphoneos/Framework.build/Objects-normal/arm64/BackendScript.dia -c /Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Backend/BackendScript.cpp -o /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Build/Engine/Framework/hop.build/Debug-iphoneos/Framework.build/Objects-normal/arm64/BackendScript.o
In file included from /Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Backend/BackendScript.cpp:4:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/APITemplates.h:25:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/../AngelScript/Addons.h:34:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/angelscript.h:1997:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:31:
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrap16.h:17:5: error: 
      field has incomplete type 'void'
                T value;
                  ^
/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Backend/BackendScript.cpp:65:34: note: in instantiation
      of template class 'gw::Proxy<void>' requested here
        iResult = pScriptEngine->RegisterObjectMethod( "AuthenticationManager", "Account@+ CreateAcco...
                                 ^
In file included from /Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Backend/BackendScript.cpp:4:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/APITemplates.h:25:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/../AngelScript/Addons.h:34:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/angelscript.h:1997:
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:68:35: note: 
      expanded from macro 'RegisterObjectMethod'
#define RegisterObjectMethod(...) RegObjectMethodIndirect(__VA_ARGS__)
                                  ^
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:70:64: note: 
      expanded from macro 'RegObjectMethodIndirect'
#define RegObjectMethodIndirect(clsdcl,decl, F, clsfunc, kind) RegisterObjectMethod##F##kind (clsdcl,...
                                                               ^
<scratch space>:89:1: note: expanded from here
RegisterObjectMethodMPRasCALL_THISCALL
^
In file included from /Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Backend/BackendScript.cpp:4:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/APITemplates.h:25:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/../AngelScript/Addons.h:34:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/angelscript.h:1997:
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:134:69: note: 
      expanded from macro 'RegisterObjectMethodMPRasCALL_THISCALL'
#define RegisterObjectMethodMPRasCALL_THISCALL(clsdcl,decl,clsfunc) RegisterObjectMethodMPRasCALL_THI...
                                                                    ^
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:135:101: note: 
      expanded from macro 'RegisterObjectMethodMPRasCALL_THISCALL_2'
#define RegisterObjectMethodMPRasCALL_THISCALL_2(clsdcl,decl,...) RegisterObjectMethod(clsdcl,decl, WRAP_MFN_...
                                                                                                    ^
In file included from /Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Backend/BackendScript.cpp:4:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/APITemplates.h:25:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/../AngelScript/Addons.h:34:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/angelscript.h:1997:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:31:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrap16.h:2930:
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrap.h:87:66: note: 
      expanded from macro 'WRAP_MFN_PR'
#define WRAP_MFN_PR(class_t,method,parameters,return_t) EV(EV(EV(CreateGenericFromMethod_2(class_t,me...
                                                                 ^
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrap.h:74:43: note: 
      expanded from macro 'CreateGenericFromMethod_2'
#define CreateGenericFromMethod_2(...) EV(CreateGenericFromMethod_3(__VA_ARGS__))
                                          ^
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrap.h:82:26: note: 
      expanded from macro 'CreateGenericFromMethod_3'
                        ,__GEN_NONEMPTY_ARGS \
                         ^
In file included from /Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Backend/BackendScript.cpp:4:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/APITemplates.h:25:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/AngelScript/../AngelScript/Addons.h:34:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/angelscript.h:1997:
In file included from /Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:31:
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrap16.h:18:11: error: 
      argument may not have 'void' type
                Proxy(T value) : value(value) {}
                        ^
2 errors generated.

-------------------------

S.L.C | 2019-03-19 10:40:08 UTC | #9

Man that's an eye sore. Really annoying to track something in that dump. However it does confirm that the `Proxy` template gets instantiated as `Proxy<void>`. How that gets achieved is beyond my reach since it seems to happen somewhere in `/Sources/Engine/Framework/Backend/BackendScript.cpp`. A file which I can't seem to find in the engine source code.

So if you have access to the code from that file, the error is detailed here:
```
/Users/ifs/work/wks-ifs/hop/Outputs/hop/ios-x86_64-debug-engine-device/Deps/urho3d/ios-x86_64-release-device-nocodesign/Install/include/Urho3D/ThirdParty/AngelScript/wrap16.h:17:5: error:
field has incomplete type ‘void’
T value;
^
/Users/ifs/work/wks-ifs/hop/Sources/Engine/Framework/Backend/BackendScript.cpp:65:34: note: in instantiation
of template class ‘gw::Proxy’ requested here
iResult = pScriptEngine->RegisterObjectMethod( “AuthenticationManager”, "Account@+ CreateAcco…
^
```

Simply put, in file `Urho3D/ThirdParty/AngelScript/wrap16.h` at line `15` there's a template like:
```cpp
template <typename T> class Proxy { ....
```
And at line `17` a member variable is created in that `Proxy` class, of whatever type was given via the template `T`, like so:
```cpp
T value;
```
So now if you take it by logic, if I instantiate `Proxy` as `Proxy<void>` then the `value` member type will be void. And you can't have a void member variable. Basically the whole thing translates to:
```cpp
class Proxy {
    void value;
};
```
Which is what makes the compiler to moan.

So if you keep extracting  further information from that message, you'll notice that the instantiation happens in file `hop/Sources/Engine/Framework/Backend/BackendScript.cpp` at line `65` Where you attempt to register this function:
```cpp
iResult = pScriptEngine->RegisterObjectMethod( “AuthenticationManager”, "Account@+ CreateAcco…
```
Which is nicely trimmed exactly where you're supposed to see how the API is registered and why does it blow up like that.

Now, I haven't looked much into how the API is exposed to AngelScript. But the approach taken with `Proxy` is common in many script binding utilities. Which is basically used to provide storage and type information for a value extracted from a generic storage with no type information.

The storage part plays a nice role in extracting values in a tuple-like fashion and then forward them to a native function-like object (*or a similar fashion*).

However, since you can't have void parameters in functions, I assume the failure happens on the returned value.

Long story short, the dump does show where the error originates from, but since it doesn't show the actual code involved, none of us are likely to understand the cause of it. Let alone explain why.

-------------------------

pleduc | 2019-03-19 09:05:02 UTC | #10

aie, sorry for the stack format... my really bad... 
your analyse was very helpful... 
it was because the void param wasn't allowed in registering function !!, 

so i replaced all:

> iResult = pScriptEngine->RegisterObjectMethod( "Image3DExt", "void reset()", asMETHODPR( Image3DExt, reset, (void), void ), asCALL_THISCALL );

by

> iResult = pScriptEngine->RegisterObjectMethod( "Image3DExt", "void reset()", asMETHODPR( Image3DExt, reset, (), void ), asCALL_THISCALL );

everywhere and it worked !! thanks very much for your analyse and time on this.
it remain true that only clang ios/tvos arm and emcc compilers where sensible of this declaration issue. 
thread close !!

-------------------------

pleduc | 2019-03-19 10:01:59 UTC | #12

really, just the:

>  reset, (void),

to

> reset, (),

just ...

-------------------------

