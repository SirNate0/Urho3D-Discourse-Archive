Lys0gen | 2021-05-27 23:23:08 UTC | #1

Hey there,
in the documentation of [LuaFunction::EndCall](https://urho3d.io/documentation/HEAD/class_urho3_d_1_1_lua_function.html#a10c1b2a030d1763e524b5fd50e4afd8b) it says

>  bool [EndCall](https://urho3d.io/documentation/HEAD/class_urho3_d_1_1_lua_function.html#a10c1b2a030d1763e524b5fd50e4afd8b) (int numReturns=0)
  End call and actually execute the function. **The return values, if any, are still left in the stack when this call returns.**

But I don't really see any way to retrieve these values from the stack. Neither with LuaFunction nor LuaScriptInstance.
Was this just never implemented? I could get a return value by writing into a passed parameter, but I'm wondering if the proper way is possible as well.

-------------------------

SirNate0 | 2021-05-28 12:57:41 UTC | #2

You can retrieve it from the `lua_state`: 

https://www.lua.org/pil/24.2.2.html

You can get the Lua state using [`LuaScript::GetState`](https://urho3d.io/documentation/HEAD/class_urho3_d_1_1_lua_script.html#a260a19a02bf93a6f77c654adf515daf1)

-------------------------

Lys0gen | 2021-05-28 13:00:07 UTC | #3

Thanks! So Urho3D just doesn't have an abstraction implemented for this and I have to work with the raw interface, got it.

E.g. like this after EndCall.

    double retNum = lua_tonumber(scriptSystem->GetState(), -1);
    lua_pop(scriptSystem->GetState(), 1);

-------------------------

