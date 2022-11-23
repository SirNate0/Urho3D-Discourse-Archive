Lunarovich | 2020-03-31 22:43:07 UTC | #1

Hello, I have a custom C++ component `Actor`. When I try to get it from Lua script with `self.node:GetComponent("Actor")`, I get a segmentation fault error. I can get any other Urho3D component from the same node. Also, I can also nil "get" a non-existing component without crashing.

-------------------------

JTippetts | 2020-04-01 21:47:49 UTC | #2

Just offhand, but have you written and loaded bindings to bind your custom class to Lua so that Lua knows about it? I've done quite a bit of custom component usage with Lua in the past, and never had any issues, but I don't think I ever tried to obtain a pointer to a component that hadn't been bound to Lua so I can't say for sure if this is it or not.

-------------------------

Lunarovich | 2020-04-01 21:53:04 UTC | #3

Yeah, ih fact, I've realized that I did not do it. I am not sure if I know how to do it though. There is [a guide here](https://urho3d.fandom.com/wiki/Registering_your_C%2B%2B_components_to_the_Lua_Script_API_with_tolua%2B%2B) but I dont find `tolua++` in my tools folder. 

@JTippetts can you, please, direct me to some source that explains how to do the binding?

-------------------------

JTippetts | 2020-04-01 22:17:03 UTC | #4

It essentially involves writing a custom 'cleaned' header for your class, that is processed by the tolua++.exe executable. You can find the tolua exe in the bin/tool/ subfolder in your build directory. You can either add a directive to your cmake file to call tolua++ with your header, or do it manually (which is what I typically tend to do), but either way once tolua does it's thing you will have a .cpp file that you add to your project. That .cpp file defines a function that you call when initializing your Lua context.

When constructing your cleaned header, you will build it as so:

    // testcomponent.pkg

    $#include <Urho3D/Scene/Component.h>
    $#include "testcomponent.h"
    $using namespace Urho3D;

    class TestComponent : public Component
    {
      // Omit object constructor and destructor, since you shouldn't ever manually be creating components in script.

      // Declare member functions, public variables, etc...
    };

Make sure you have the `$#` directives, which will be directly transplanted (minus the `$`) into the generated .cpp file. Process this cleaned header with the tolua exe:

    tolua++.exe -o bindtestcomponent.cpp bindtestcomponent.pkg

This will output a file, bindtestcomponent.cpp, inside of which will be defined a function to call in order to load the bindings for your class, something like:

    TOLUA_API int tolua_testcomponent_open (lua_State* tolua_S);

Once you have gotten that far, you can add your .cpp to your project. Then, wherever you initialize your Lua context, you can call that function and pass your context and the bindings will be loaded and available, so that you can use the component in script just like any built-in component. For example, if using the Urho3DPlayer, you could edit Urho3DPlayer.cpp and around lines [185](https://github.com/urho3d/Urho3D/blob/master/Source/Tools/Urho3DPlayer/Urho3DPlayer.cpp#L185) and [206](https://github.com/urho3d/Urho3D/blob/master/Source/Tools/Urho3DPlayer/Urho3DPlayer.cpp#L206) (the first location is if both AngelScript and Lua are enabled, the second location is if only Lua is enabled) you would then call your open function like so:

    TOLUA_API int tolua_testcomponent_open (lua_State* tolua_S);
    tolua_testcomponent_open(GetSubsystem<LuaScript>()->GetState());

-------------------------

Lunarovich | 2020-04-01 22:28:29 UTC | #5

Wow! Thank you very much! Will try it tomorrow and inform about results.

-------------------------

Lunarovich | 2020-04-01 22:34:17 UTC | #6

@JTippetts a question though. I'm developing under Linux. Is tolua++ available for Linux?

-------------------------

JTippetts1 | 2020-04-01 23:53:22 UTC | #7

Yes, it should still be an executable in bin/tool. It is built as part of the process when Urho3D is built, since the library build process invokes it.

-------------------------

Lunarovich | 2020-04-02 07:19:31 UTC | #8

Thanks! I've successfully bound my first component :slight_smile:

I have several questions though:

1. I can't find `tolua++` in *bin/tools* of Linux shared and static builds.
2. I don't find either *ToCppHook.lua* file in the *LuaScripts/pkg* - in fact, I don't find the folder at all.
3. Can you direct me where to look for the info on how to make a custom-made subsystem available as a global variable, like input or so.

FYI, I've installed tolua++ from the Ubuntu repository.

-------------------------

Lunarovich | 2020-04-02 08:53:55 UTC | #9

In fact, I've compiled myself Urho3D and got `tolua++` and I've found also *ToCppHook.lua* in Source/Urho3D/LuaScript/pkgs/ToCppHook.lua

Now, however, I have a problem. When I try to tolua++ a function like 
```
Text3D* CreateDrawable(const String& ch);
```
everything is ok, but when I try to compile, I get 
```
BindEntity.cpp:(.text+0xd1): undefined reference to `tolua_tourho3dstring(lua_State*, int, char const*)'
```

I see that it is related to `#include <Urho3D/LuaScript/ToluaUtils.h>` and I have *ToluaUtils.h* in the include dir, however, somehow it does not compile.

-------------------------

JTippetts1 | 2020-04-02 12:12:37 UTC | #10

Sorry, yeah, I had forgotten the line to include ToluaUtils. Just throw that include in there like

    $#include <Urho3D/LuaScript/ToluaUtils.h>

-------------------------

Lunarovich | 2020-04-02 13:00:22 UTC | #11

[quote="JTippetts1, post:10, topic:6037"]
$#include <Urho3D/LuaScript/ToluaUtils.h>
[/quote]

Thanks for the response. However, when I look at the bind cpp file, I see it included. However, I still get an undefined reference. Even when I include it excplicitely in the pkg file, I get an undefined reference. Btw, I'm using 1.71 linux 64 shared deb package as Urho3D.

-------------------------

JTippetts1 | 2020-04-02 13:49:11 UTC | #12

Can't really say what the problem might be, other than to double check your build and settings. If you built urho with Lua support, then the code from ToluaUtils.cpp should be in there during link, so if it's not then something is messed up somewhere.

Edit: just noticed you are using a 1.7 package. I highly recommend pulling from master and building it. There have been a lot of bug fixes since the 1.7 release.

-------------------------

