j15r | 2017-01-02 01:04:03 UTC | #1

Sorry for the slew of Lua questions! I'm sure I'll get my bearings soon and be able to keep quiet :slight_smile:

Related to my last question, I'm also attempting to get Lua remote debugging working, via [studio.zerobrane.com/doc-remote-debugging.html](https://studio.zerobrane.com/doc-remote-debugging.html). It looks like it should be pretty straightforward, but I've hit a snag with the Lua build coming out of Urho3D. mobdebug requires luasocket, which I have built and running. But when I try to require it from my Lua entry point script, I hit the error "error loading module 'socket.core' from file '/usr/local/lib/lua/5.1/socket/core.so': dynamic libraries not enabled; check your Lua installation".

I'm sure there's some way deep in the bowels of the Lua build that's turning off .so loading (or failing to enable it), but I can't seem to find it. I've tried both Lua and LuaJIT to no avail. This message stems from lua/loadlib.c, and is triggered by none of {LUA_DL_DLOPEN, LUA_DL_DLL, LUA_DL_DYLD} being defined. But AFAICT each of the Windows/Mac/Linux should automatically define one of these shared library types, and I see nothing in the Urho3D build that explicitly disables them.

Again, any pointers would be greatly appreciated, and I am of course open to other ways (apart from printf, which I loathe) to debug Lua code.

Cheers,
joel.

-------------------------

feltech | 2017-01-02 01:05:32 UTC | #2

Hey.  I stumbled on this post when attempting to figure out myself how to debug Urho3D's embedded Lua.  I've managed to get debugging working under the following conditions (note I tried to post some links but am not allowed yet - google is your friend):

[ul]
[li] I have to use the LuaJIT Urho3D interpreter option, to get around the "dynamic libraries not enabled" issue (you say LuaJIT didn't work for you, but it definitely does for me, only the standard Lua interpreter fails with this error).[/li]
[li] I also had problems getting the `socket` library installed in a "nice" way.  Eventually I installed via the luarocks package manager, which installs to the system path rather than the project folder (annoying), but since it's just for debugging and won't be shipped I figured it's fine.[/li]
[li] I use eclipse with the LDT plugin, which comes with a `debugger.lua` that can be injected into your project.[/li][/ul]
This then got me a semi-working debugger.  However, I found that breakpoints wouldn't be hit.  I enabled the "break on first line" option in LDT debugger, which did pause the script on loading it, but the source was not available.  Interestingly, the source higher up the stack was available, however, just not the source of my script.

I traced this to the way Urho3D (necessarily) loads it's scripts into Lua.  A file is read to a character array and then the character array is read by the Lua interpreter, so the mapping to the original file is lost (see `LuaFile.cpp`).

So, to execute a Lua file directly, rather than going through the resource cache, I added the following method to `LuaScript.cpp` as an alternative the the existing `ExecuteFile` method:

[code]
bool LuaScript::ExecuteRawFile(const String& fileName)
{
    PROFILE(ExecuteRawFile);

    ResourceCache* cache = GetSubsystem<ResourceCache>();
    String filePath = cache->GetResourceFileName(fileName);

    LOGINFO("Executing Lua file from file system: " + filePath);

    if (filePath.Empty())
    {
        LOGERROR("Lua file not found: " + filePath);
    	return false;
    }

    int top = lua_gettop(luaState_);

    if (luaL_loadfile (luaState_, filePath.CString()))
    {
        const char* message = lua_tostring(luaState_, -1);
        LOGERROR("Load Lua file failed: " + String(message));
        lua_settop(luaState_, top);
        return false;
    }

    if (lua_pcall(luaState_, 0, 0, 0))
    {
        const char* message = lua_tostring(luaState_, -1);
        LOGERROR("Execute Lua file failed: " + String(message));
        lua_settop(luaState_, top);
        return false;
    }

    return true;
}
[/code]

This combined with my findings above allows me to set breakpoints and step through my Lua code just fine (gotta love simultaneous debugging C++ and Lua code breakpoints).

NOTE: I am very new to Urho3D and Lua and the code above is spliced together from other methods and may not be the correct way of doing things.  But it does work for now and I'll switch back to the 'proper' resource cache way of loading scripts in production.

Hope this helps.

-------------------------

feltech | 2017-01-02 01:05:33 UTC | #3

A quick update on this.  My solution above doesn't work for script files imported within the script itself (i.e. `require (anotherscript)` - breakpoints in "anotherscript" will not be hit).

This is because the loader function registered with Lua (`LuaScript::Loader`) uses the `luaL_loadbuffer` method rather than `luaL_loadfile`.  Again, this is necessary for proper use of Urho3D's resource cache (so the script file is loaded into an in-memory buffer and the buffer reused if/when the file is needed again).  However, it means that breakpoints are not hit when debugging Lua scripts.

My solution is to add a CMake option that will force Urho3D to attempt the `luaL_loadfile` method to load a raw script file, before falling back on using the resource cache (which I think is necessary if the script file is packaged rather than a simple filesystem file).  This option can then be disabled for deployment, leaving the implementation exactly as it was before.

I'll have a look at creating a pull request for this (I use git professionally, but never done a github pull request before, so have some reading to do).

-------------------------

