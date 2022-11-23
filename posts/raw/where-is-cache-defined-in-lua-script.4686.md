ezark | 2018-11-21 03:16:52 UTC | #1

    -- Set font and text color
    helloText:SetFont(cache:GetResource("Font", "Fonts/Anonymous Pro.ttf"), 30)
    helloText.color = Color(0.0, 1.0, 0.0)

  i am a starter to urho3d, i want to know where is this cache defined in the 01_HelloWorld.lua file, thanks.

-------------------------

Sinoid | 2018-11-21 06:38:16 UTC | #2

It's a special registered thing: See **global properties** on https://urho3d.github.io/documentation/1.7/_lua_script_a_p_i.html (towards the bottom)

Edit: Urho3D uses ToLua++ to generate Lua bindings so it can be a bit tricky to track down bindings, unless you're intimate with lua (or using a fork that's lua only) I'd strongly suggest using Angelscript, as it's superior to C# up until C# 7.0 (7.2 is almost a C++ killer - 8.0 might deliver on promises I was told 15 years ago [default interfaces]).

-------------------------

ezark | 2018-11-21 06:42:08 UTC | #3

ok，thank you very much. i find the cache.
but can you tell me where is this global property defined in the code? c++ or lua exactly position.

-------------------------

Sinoid | 2018-11-21 06:51:40 UTC | #4

It's in `\pkgs\Resource\ResourceCache.pkg`

Line 50:

```
ResourceCache* GetCache();
tolua_readonly tolua_property__get_set ResourceCache* cache;
```
Sorry to be so vague, but Lua is not my space - Angelscript is.

-------------------------

orefkov | 2018-11-21 07:07:42 UTC | #5

"cache" - it is global name in script for ResourceCache subsystem.
It is equivalent to C++
`GetSubsystem<ResourceCache>()`
It is not defined in lua itself, it is binding to C++ code.

-------------------------

