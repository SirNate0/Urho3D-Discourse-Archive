1vanK | 2018-06-12 08:00:35 UTC | #1

Interpreter benchmark
----------------

AngelScript
--
```
int fibR(int n)
{
    if (n < 2) return n;
    return (fibR(n-2) + fibR(n-1));
}

void Start()
{
    for (int i = 0; i < 10; i++)
    {
        uint startTime = time.systemTime;
        fibR(30);
        uint deltaTime = time.systemTime - startTime;
        log.Info("Fib AS test #" + i + " " + String(deltaTime));
    }
    engine.Exit();
}
```

Lua
----

```
function fibR(n)

    if (n < 2) then return n end
    return (fibR(n-2) + fibR(n-1))
end

function Start()
    for i = 0, 10 do
        local startTime = time:GetSystemTime()
        fibR(30)
        local deltaTime = time:GetSystemTime() - startTime
        log:Write(LOG_INFO, "Fib LUA test #" .. i .. " " .. deltaTime)
    end
    engine:Exit()
end
```

Result
---
```
Lua with JIT
------------
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #0 9
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #1 8
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #2 8
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #3 8
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #4 8
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #5 8
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #6 8
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #7 8
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #8 8
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #9 8
[Tue Jun 12 10:36:10 2018] INFO: Fib LUA test #10 8

Lua without JIT
---------------
[Tue Jun 12 10:37:08 2018] INFO: Fib LUA test #0 147
[Tue Jun 12 10:37:08 2018] INFO: Fib LUA test #1 147
[Tue Jun 12 10:37:08 2018] INFO: Fib LUA test #2 146
[Tue Jun 12 10:37:08 2018] INFO: Fib LUA test #3 145
[Tue Jun 12 10:37:08 2018] INFO: Fib LUA test #4 146
[Tue Jun 12 10:37:09 2018] INFO: Fib LUA test #5 147
[Tue Jun 12 10:37:09 2018] INFO: Fib LUA test #6 147
[Tue Jun 12 10:37:09 2018] INFO: Fib LUA test #7 146
[Tue Jun 12 10:37:09 2018] INFO: Fib LUA test #8 146
[Tue Jun 12 10:37:09 2018] INFO: Fib LUA test #9 146
[Tue Jun 12 10:37:09 2018] INFO: Fib LUA test #10 146

AngelScript
-----------
[Tue Jun 12 10:37:56 2018] INFO: Fib AS test #0 93
[Tue Jun 12 10:37:56 2018] INFO: Fib AS test #1 93
[Tue Jun 12 10:37:56 2018] INFO: Fib AS test #2 92
[Tue Jun 12 10:37:56 2018] INFO: Fib AS test #3 93
[Tue Jun 12 10:37:56 2018] INFO: Fib AS test #4 93
[Tue Jun 12 10:37:57 2018] INFO: Fib AS test #5 93
[Tue Jun 12 10:37:57 2018] INFO: Fib AS test #6 95
[Tue Jun 12 10:37:57 2018] INFO: Fib AS test #7 93
[Tue Jun 12 10:37:57 2018] INFO: Fib AS test #8 93
[Tue Jun 12 10:37:57 2018] INFO: Fib AS test #9 92
```

Native function calls
----------------

AngelScript
-----
```
void Start()
{
    for (int i = 0; i < 10; i++)
    {
        uint startTime = time.systemTime;
        for (int j = 0; j < 50000; j++)
        {
            IntVector2 x = input.mousePosition;
            x = input.mouseMove;
        }
        uint deltaTime = time.systemTime - startTime;
        log.Info("Native function calls AS test #" + i + " " + String(deltaTime));
    }
    engine.Exit();
}
```

LUA
----
```
function Start()
    for i = 0, 10 do
        local startTime = time:GetSystemTime()
        for j = 0, 50000 do
            local x = input:GetMousePosition()
            x = input:GetMousePosition()
        end
        local deltaTime = time:GetSystemTime() - startTime
        log:Write(LOG_INFO, "Native function calls LUA test #" .. i .. " " .. deltaTime)
    end
    engine:Exit()
end

```

Result
-------
```
Lua with JIT
------------
[Tue Jun 12 10:53:48 2018] INFO: Native function calls LUA test #0 108
[Tue Jun 12 10:53:48 2018] INFO: Native function calls LUA test #1 115
[Tue Jun 12 10:53:48 2018] INFO: Native function calls LUA test #2 135
[Tue Jun 12 10:53:48 2018] INFO: Native function calls LUA test #3 105
[Tue Jun 12 10:53:48 2018] INFO: Native function calls LUA test #4 91
[Tue Jun 12 10:53:48 2018] INFO: Native function calls LUA test #5 137
[Tue Jun 12 10:53:48 2018] INFO: Native function calls LUA test #6 82
[Tue Jun 12 10:53:49 2018] INFO: Native function calls LUA test #7 101
[Tue Jun 12 10:53:49 2018] INFO: Native function calls LUA test #8 168
[Tue Jun 12 10:53:49 2018] INFO: Native function calls LUA test #9 131
[Tue Jun 12 10:53:49 2018] INFO: Native function calls LUA test #10 77

Lua without JIT
--------------
[Tue Jun 12 10:52:35 2018] INFO: Native function calls LUA test #0 149
[Tue Jun 12 10:52:35 2018] INFO: Native function calls LUA test #1 146
[Tue Jun 12 10:52:36 2018] INFO: Native function calls LUA test #2 157
[Tue Jun 12 10:52:36 2018] INFO: Native function calls LUA test #3 171
[Tue Jun 12 10:52:36 2018] INFO: Native function calls LUA test #4 127
[Tue Jun 12 10:52:36 2018] INFO: Native function calls LUA test #5 190
[Tue Jun 12 10:52:36 2018] INFO: Native function calls LUA test #6 119
[Tue Jun 12 10:52:36 2018] INFO: Native function calls LUA test #7 229
[Tue Jun 12 10:52:36 2018] INFO: Native function calls LUA test #8 125
[Tue Jun 12 10:52:37 2018] INFO: Native function calls LUA test #9 128
[Tue Jun 12 10:52:37 2018] INFO: Native function calls LUA test #10 257

AngelScript
-----------
[Tue Jun 12 10:52:27 2018] INFO: Native function calls AS test #0 98
[Tue Jun 12 10:52:27 2018] INFO: Native function calls AS test #1 97
[Tue Jun 12 10:52:27 2018] INFO: Native function calls AS test #2 97
[Tue Jun 12 10:52:27 2018] INFO: Native function calls AS test #3 97
[Tue Jun 12 10:52:28 2018] INFO: Native function calls AS test #4 96
[Tue Jun 12 10:52:28 2018] INFO: Native function calls AS test #5 97
[Tue Jun 12 10:52:28 2018] INFO: Native function calls AS test #6 97
[Tue Jun 12 10:52:28 2018] INFO: Native function calls AS test #7 96
[Tue Jun 12 10:52:28 2018] INFO: Native function calls AS test #8 97
[Tue Jun 12 10:52:28 2018] INFO: Native function calls AS test #9 96

```

-------------------------

S.L.C | 2018-06-12 10:20:08 UTC | #2

The native function call performance is understandable since AS has static typing like c/c++ and there's less conversion to be made.

Not to mention that Lua with jit doesn't use FFI but rather the usual vm stack. Which could be worse than regular Lua.

Nothing new or unexpected here.

-------------------------

Modanung | 2018-06-12 17:25:10 UTC | #3

Still, it's good to have some data to point to.

-------------------------

S.L.C | 2018-06-12 20:19:23 UTC | #4

I cannot disagree with that.

-------------------------

gunbolt | 2018-06-22 03:33:25 UTC | #5

Where's the AngelScript with JIT benchmark ?

-------------------------

1vanK | 2018-07-08 13:53:34 UTC | #6

UrhoSharp

```
using System;
using System.Diagnostics;
using Urho;
using Urho.Actions;
using Urho.Gui;
using Urho.Shapes;

namespace UrhoSharp
{
    public class MyGame : Application
    {
        int fibR(int n)
        {
            if (n < 2) return n;
            return (fibR(n - 2) + fibR(n - 1));
        }

        [Preserve]
        public MyGame(ApplicationOptions options) : base(options) { }

        static MyGame()
        {
        }

        protected override async void Start()
        {
            for (int i = 0; i < 10; i++)
            {
                uint startTime = Time.SystemTime;
                fibR(30);
                uint deltaTime = Time.SystemTime - startTime;
                Urho.IO.Log.Write(LogLevel.Error, "Fib C# test #" + i + " " + deltaTime);
            }

        }
    }
}

```

```
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #0 5
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #1 6
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #2 4
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #3 5
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #4 5
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #5 5
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #6 5
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #7 6
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #8 5
[Sun Jul  8 16:43:50 2018] WARNING: Fib C# test #9 5
```

```
using System;
using System.Diagnostics;
using Urho;
using Urho.Actions;
using Urho.Gui;
using Urho.Shapes;

namespace UrhoSharp
{
    public class MyGame : Application
    {
        [Preserve]
        public MyGame(ApplicationOptions options) : base(options) { }

        static MyGame()
        {
        }

        protected override async void Start()
        {
            for (int i = 0; i < 10; i++)
            {
                uint startTime = Time.SystemTime;
                for (int j = 0; j < 50000; j++)
                {
                    IntVector2 x = Input.MousePosition;
                    x = Input.MouseMove;
                }
                uint deltaTime = Time.SystemTime - startTime;
                Urho.IO.Log.Write(LogLevel.Error, "Native function calls C# test #" + i + " " + deltaTime);
            }
        }
    }
}
```

```
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #0 5
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #1 3
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #2 3
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #3 4
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #4 3
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #5 3
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #6 4
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #7 3
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #8 3
[Sun Jul  8 16:52:48 2018] WARNING: Native function calls C# test #9 4
```

-------------------------

