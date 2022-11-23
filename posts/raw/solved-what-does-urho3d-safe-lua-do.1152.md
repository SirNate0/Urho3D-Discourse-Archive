setzer22 | 2017-01-02 01:05:44 UTC | #1

Hello,

I had the following Lua code in a script (I'll just cut it down to the bare minimum for example purposes):

[code]
path = pathfinder:getPath() -- This C++ function returns a Vector<Vector3>&, which happens to be empty
self.node:SetPosition(path[1]);
[/code]

This, as expected, causes my application to crash with a segmentation fault because of path[1] being nil.

I thought URHO3D_SAFE_LUA added checkings for this kind of errors, which would help as I'm using Lua mainly to do quick prototypes and the final code is done in C++. But compiling with that option didn't change anything in the above script.

So my question is. Should URHO3D_SAFE_LUA have caught that? And in any case, what does the flag actually do? The documentation is kind of vague in that sense.

Thank you!  :smiley:

-------------------------

cadaver | 2017-01-02 01:05:44 UTC | #2

It controls whether TOLUA_RELEASE is defined to disable tolua++ runtime checks (the SAFE_LUA mode leaves the checks enabled, which reduces performance) 

These checks catch some crashprone errors like trying to call a missing member function or supplying wrong type parameters to a function.

The example you give is not caught, as Node::SetPosition() expects a Vector3 reference instead of pointer, and in C++ itself you can't create a null reference. In the lua bindings pointers and references are for the most part interchangeable, but it seems tolua++ doesn't have a specific check for null in that case.

-------------------------

setzer22 | 2017-01-02 01:05:44 UTC | #3

I'll always wonder why C++ has two kind of references (references and pointers, I mean)...

Anyway thank you very much for the info!  :smiley:

-------------------------

weitjong | 2017-01-02 01:05:46 UTC | #4

[quote="setzer22"]I'll always wonder why C++ has two kind of references (references and pointers, I mean)...[/quote]
Because they are different. The way I understand it, 'reference' is almost guaranteed to be a, well, valid reference. While 'pointer' makes no such promise. The pointer can point to a valid reference or an invalid one or can be just null (not point to anything).

-------------------------

