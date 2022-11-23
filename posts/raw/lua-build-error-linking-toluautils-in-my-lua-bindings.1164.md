setzer22 | 2017-01-02 01:05:49 UTC | #1

I'm trying to learn how to bind C++ code to the Lua API. 

What I've managed so far is registering simple functions and components, but so far I had never registered a function that received a Vector parameter. 

It appears that Urho uses some binding code in <Urho3D/LuaScript/ToLuaUtils.h>, the relevant functions for me right now are ToluaIsVector and ToluaToVector. So I #included the file (with the Urho full path, like I just wrote) in my pkg file. 

The binding code is generated with the proper include and the code correctly sees the functions and compiles. But it's failing to link. One of the errors is:

[code]LuaBindings.cpp:(.text+0xdbc): undefined reference to `int ToluaIsVector<Urho3D::WeakPtr<UnitAgent> >(lua_State*, int, char const*, int, tolua_Error*)'[/code]

The other errors are very similar.

I'm correctly linking to Urho3D as a library so why are those symbols not included? Maybe that file doesn't get built in the library version? 

[b]EDIT:[/b] I'm pretty sure it's not that as I just looked through libUrho3D.a (with grep) and ToluaIsVector is in there.

Would it be better to just maintain a copy of ToLuaUtils in my Source folder and just build it as if it was part of my game?

Also, I was wondering, why are relative include paths being used inside Urho files? I'm talking for exaple about this file, ToLuaUtils.h:
[code]#include "../Core/Context.h"[/code]

Thanks!

-------------------------

setzer22 | 2017-01-02 01:05:49 UTC | #2

Ok I've figured it out. Apparently the implementation in ToluaUtils is only provided for certain types of Vectors like Vector<String> or PODVector<unsigned> despite being declared as a completely generic function and thus, it only fails at the linking phase. 

Isn't there any way I can get it to accept Vector<WeakPtr<MyComponent>>?

-------------------------

cadaver | 2017-01-02 01:05:49 UTC | #3

Somewhat of a hack, but it should be possible to define the whole Lua binding function in the pkg file, using the #define mechanism to disable the generated binding. You would first take the generated function as a base, and modify it to push your custom vector without going through ToLuaUtils.

Take a look at for example ResourceCache.pkg:

[code]
${
#define TOLUA_DISABLE_tolua_ResourceLuaAPI_GetCache00
static int tolua_ResourceLuaAPI_GetCache00(lua_State* tolua_S)
{
    return ToluaGetSubsystem<ResourceCache>(tolua_S);
}
[/code]

Another possibility (not 100% sure it will work) is to define the necessary template implementation of the ToLuaUtils pushvector for your specific vector specialization in your code.

-------------------------

setzer22 | 2017-01-02 01:05:50 UTC | #4

Thank you, 

As a sollution I'd rather implement the needed template functions instead of manually defining each function with vector parameters. Right now I'm a bit confused on what ToluaIsVector and ToluaToVector do. From the context (an when do they get called) I assumed they were to convert a C++ Vector<T> to an indexed lua table. But from what I can read in the implementation, my assumptions don't make sense. So basically, what's the use of those functions? And more specifically, what do those parameter names mean (lo, type, def, err)? Is that part of the lua API?

For now I've made a workaround by having the function take a Vector<unsigned> (which works) containing the node ids that contain the components the function should received.

-------------------------

