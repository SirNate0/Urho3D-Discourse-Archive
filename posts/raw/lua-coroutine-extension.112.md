aster2013 | 2017-01-02 00:58:06 UTC | #1

Hi, all

I have add coroutine support in Lua, and provide two extension functions for Lua coroutine.
[b]coroutine.start(func)[/b] -- create new coroutine and resume it. the function code:
[code]
function coroutine.start(func)
    local co = coroutine.create(func)
    return coroutine.resume(co)
end
[/code]
[b]coroutine.sleep(time)[/b] -- sleep current coroutine, it will wake up until the time arrived.

I think it is helpful. For more information, please refer the Coroutine.lua sample in LuaScripts.

-------------------------

weitjong | 2017-01-02 00:58:06 UTC | #2

??

Is it possible to make the coroutine yield/resume based on other events and not just based on time step?

-------------------------

aster2013 | 2017-01-02 00:58:06 UTC | #3

?????????????

-------------------------

friesencr | 2017-01-02 00:58:07 UTC | #4

with this, debugger support, and code completion is becoming more tempting to give up my static typing.  except i have about half of the api i use commonly in my fingers now.  on my resource editor branch i have a hacky version of a coroutine built into the update loop.  getting the real deal would be much better.

 [angelcode.com/angelscript/sd ... orout.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_samples_corout.html)

-------------------------

aster2013 | 2017-01-02 00:58:07 UTC | #5

Two functions will be added:

[code]
coroutine.waitevent( event )
coroutine.sendevent( event )
[/code]

weitjong ??????????

-------------------------

weitjong | 2017-01-02 00:58:07 UTC | #6

Yes, I think so. With this, the coroutine will be more versatile.

-------------------------

aster2013 | 2017-01-02 00:58:07 UTC | #7

coroutine.waitevent( event )
coroutine.sendevent( event )

added, please get it.

-------------------------

weitjong | 2017-01-02 00:58:08 UTC | #8

For a second, I thought I read "add please, (in order to) get it.  :laughing: 
Thanks Aster. You are the best.

-------------------------

