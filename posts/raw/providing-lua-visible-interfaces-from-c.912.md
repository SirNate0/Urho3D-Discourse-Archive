j15r | 2017-01-02 01:04:03 UTC | #1

All,

Apologies if there's obvious documentation on this, but I can't seem to find it. I'm attempting to build a game that's implemented in a mixture of Lua and C++. Unsurprisingly, my intent is to implement the coarse-grained game logic in Lua, with performance-critical bits in C++. So far, I've had not trouble implementing custom Drawable components in C++ (kudos to the team for making bootstrapping a C++ project far easier than I'm accustomed to!), but I've hit a bit of a snag in the Lua integration.

Calling simple Lua scripts is easy enough. Where I'm having trouble is in exposing interfaces to my custom components to script code. I believe I understand the structure and logic used for the built-in classes -- as I understand it, there's a .pkg definition file for each exposed interface, run through tolua++ to generate, e.g., NodeLuaAPI.cpp, which appears to include all the necessary Lua binding logic. So far, so good.

However, when I attempt to do the same for my own custom classes, I hit build issues at every turn, giving me the impression I'm fundamentally misunderstanding something. The package definitions seem straightforward enough. But the compiled output (via ToCppHook.lua) #includes <tolua++.h>, "lua.h", and "LuaScript/ToLuaUtils.h". These references appear to assume that they'll be running within the Urho3D source build, not external projects (e.g., otherwise, I'd expect to see #include "Urho3D/LuaScript/ToLuaUtils.h").

My next step was to hope that ToCppHook.lua was not actually necessary (it might be the case that the stuff for PODVector, et al, in there is only needed for the library itself), so I dropped the {-L [...]/ToCppHook.lua from my tolua++ invocation. If I also add Source/ThirdParty/Lua/src to my include path, then manually call {tolua_MyThing_open(luaScript->GetState());} during startup, then (yay!) it actually works, and I can call {node:CreateComponent("MyThing")} without it crashing in the lua binding code.

My question is this -- am I swimming upstream on this approach, and/or is there a simpler way to achieve my goals? I feel like my build's more than a little precarious, reaching around into the Urho3D source tree for include paths for lua.h, and I have the sneaking suspicion that dropping ToCppHook.lua from the tolua++ invocation is causing problems I haven't hit yet. Any guidance or pointers would be greatly appreciated. And if it happens that this is a legitimate-but-not-well-supported use-case, I'm glad to lend a hand in supporting it.

Thanks in advance,
joel.

-------------------------

weitjong | 2017-01-02 01:04:04 UTC | #2

In regard to 'add Source/ThirdParty/Lua/src' to include path - It is not clear whether you are using the Urho3D 1.32 release or the Urho3D master branch. If it is the latter and if you have used the provided FindUrho3D CMake module in your external project then the problem can be fixed by enabling the URHO3D_LUA build option when you configure/generate your external project files. The latest master branch has a commit which "install" the Lua/LuaJIT and tolua++ header files and let the FindUrho3D module to add the Lua include dir into the include search path for external project. See [github.com/urho3d/Urho3D/issues/610](https://github.com/urho3d/Urho3D/issues/610) for more detail.

In regard to ToCppHook.lua assumption - You have made a good observation there. It will be beneficial to change this script to accept extra parameter to indicate whether it should emit cpp source code for [b]building[/b] Urho3D library or for [b]using[/b] Urho3D library, i.e. alternating the include statement between "LuaScript/ToluaUtils.h" and <Urho3D/LuaScript/ToluaUtils.h>, for example. Alternatively, for a quicker fix, you can just customize this hook to suit your own project need and invoke tolua++ tool with your custom version. I would not, however, advice you to bypass it altogether because besides losing on the performance of using Lua's table, I am not sure what else would break in the Lua bindings without it.

-------------------------

j15r | 2017-01-02 01:04:04 UTC | #3

Thanks -- I just realized that I hadn't been running cmake in my local build with -D URHO3D_LUA. Doing so appears to have added Build/include/ThirdParty/Lua to my include path, which resolves part of the problem. But .../ThirdParty/toluapp is not on the include path. Looking at [github.com/urho3d/Urho3D/commit ... 4b1a604f3f](https://github.com/urho3d/Urho3D/commit/8682ba781a48925899b4fe5fb31efb4b1a604f3f), I *think* it just needs include/ThirdParty/toluapp added to the `if (URHO3D_LUA)` bit. This patch does correctly add the toluapp symlink to the Build/include output, so it's pretty close.

Regarding ToCppHook.lua, what I have is actually working so far, but I'll try to find some time soon to look at it more closely. I should be able to get a patch together to make it reasonably simple to create a combination C++/Lua project. If anyone thinks it would be useful, I could also create a sample project explaining how to get bootstrapped for that case, which I suspect is pretty common. I'll probably need someone to review the intricacies of extending Drawable to make sure I didn't screw anything up -- I'm still getting my sea legs in the framework's APIs and assumptions.

-------------------------

weitjong | 2017-01-02 01:04:04 UTC | #4

The "ThirdParty/toluapp" is not needed in the include search path specifically. It is because the generated CPP source file should have the tolua++.h header file included in this way: "#include <toluapp/tolua++.h>". This form is correct regardless of whether we are building Urho3D library or using Urho3D library. All we just need to ensure is that when building we have "${CMAKE_BINARY_DIR}/${DEST_INCLUDE_DIR}/ThirdParty" in the include search path and when using we have "${URHO3D_HOME}/include/${PATH_SUFFIX}/ThirdParty" in the include search path.

I am looking forward for your sample project. Thanks in advance for your plan to sharing it.

-------------------------

j15r | 2017-01-02 01:04:05 UTC | #5

I missed that bit -- ToCppHook.lua includes the nasty search and replace that fixes that. That was the impetus I needed to hoist out ToCppHook.lua and adjust the include paths. Turns out that wasn't a big deal, and everything works now in my project's build tree. Now the only slightly smelly part is having to copy most of ToCppHook, but that's eminently tolerable for the time being.

Thanks again for your help!

-------------------------

weitjong | 2017-01-02 01:04:05 UTC | #6

There is a small patch in the latest master branch now to address your last issue. You should be able to reuse the ToCppHook.lua now as it is.

-------------------------

j15r | 2017-01-02 01:04:10 UTC | #7

Cool, thanks -- the only remaining problem is that it's missing an #include <Urho3D/Urho3D.h>, which is required to avoid compile errors in ToluaUtils.h.

-------------------------

weitjong | 2017-01-02 01:04:11 UTC | #8

Yes, of course. It will be included soon.

-------------------------

