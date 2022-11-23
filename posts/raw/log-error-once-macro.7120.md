SirNate0 | 2022-01-04 02:24:55 UTC | #1

I thought of this earlier when I realized certain of the draw calls will fail silently, and I finally decided to actually write the code to do it. And it turned out a lot simpler than I expected, which is nice.

```
#define URHO3D_LOGERROR_ONCE(message) do {static bool once = true; if (once) {once = false; URHO3D_LOGERROR(message);} } while (false)
```

How it works:

- Creates a unique static variable that will be initialized only once per variable for a given function (potentially per thread or something like that -- I don't remember the exact rules, and I'm not concerned in this case. LOG_FEW is still good enough versus LOG_PER_FRAME). 
- This single initialization is used to carry out the body of the if (the actual logging) only once.
- The entirety is wrapped in a `do {...} while(false)` so that the macro still requires a semicolon after it like the other LOG macros.

-------------------------

