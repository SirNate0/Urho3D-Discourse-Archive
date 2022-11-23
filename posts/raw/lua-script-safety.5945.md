SirNate0 | 2020-02-25 08:05:05 UTC | #1

I don't at all use Lua, I just noticed the behavior while testing an answer to a different thread, but is the Lua subsystem supposed to be unsafe (i.e. the program crashes if there are some errors in the logic of the script)?

For example, if you place this in your script, the only error I got was `Segmentation fault (core dumped)`

```
    -- Failed without these    v
    -- targetPosition = Vector3(10,1,1)
    -- up = Vector3(1,0,0)
    -- Failed without these ^
    
    local to = Quaternion()
    if to:FromLookRotation(targetPosition, up) then
        Print(to)
    end
```

If this is expected, (particularly if this is behavior controlled by a build flag) I suppose that's fine, I was just really surprised when the program crashed from something a simple as using an undefined variable.

-------------------------

JTippetts | 2020-02-25 08:05:37 UTC | #2

The URHO3D_SAFE_LUA flag can be enabled to turn on some safety checks, like ensuring that parameters to a function are correct. Adds a bit of overhead, so it can be a good idea to enable it for development/debugging and disable it for release.

-------------------------

