zauberparacelsus | 2017-04-29 17:28:40 UTC | #1

I have plans to make a game with Urho3D, and one of the features I wish to support in it is modding.  So, I have the following questions:

1. Does Urho3D require that scripts be bytecode compiled ahead of time, or will it just compile/recompile them as needed?
2. Does Urho3D (or rather, Lua or AngelScript) provide a way to restrict the script engines so that scripts cannot do potentially dangerous things, or to limit filesystem access to certain directories?

-------------------------

Enhex | 2017-04-29 17:53:00 UTC | #2

1. You can provide scripts in source code form and compile them at runtime (I'm doing it myself).

2. The script system is made to be sandboxed (can't mess with the user's machine).
I asked about it before here: https://discourse.urho3d.io/t/is-urhos-scripting-sandboxed/1985

-------------------------

zauberparacelsus | 2017-04-29 20:21:47 UTC | #3

Excellent, thanks for the reply!

-------------------------

