theak472009 | 2017-01-02 01:06:50 UTC | #1

Hello,
We are planning to use Urho3D as our game engine for a game and changing some stuff in engine code, move around code, rename files, functions and it all compiles perfectly.
But when it comes to generating and compiling the lua bindings, we get the compiler error that it cannot find function tolua_pushurho3dstring.
We have renamed this function in our engine to be PushLuaString but the generator still keeps on spitting out tolua_pushurho3dstring
We could not find this function anywhere in the repository, so is it hard-coded somewhere in ascii or something?
To work around this, we tried to use the -S switch in luabind.c but then the program crashes when a lua script file tries to use a string.

I think it is the luabind.c file which was generated before we made the changes to the engine. How would we generate this file again?

Edit: It was indeed stored nicely in ascii in luabind.c. But it would be nice to see how to create the bindings of these lua files.

Thanks.

-------------------------

weitjong | 2017-01-02 01:06:51 UTC | #2

I believe those are Lua bytecode (not ASCII representation of the Lua script). I have to keep a small note myself on how to generate these two files. The instruction is now included as part of the toluapp CMakeLists.txt. Knock yourself out.

-------------------------

theak472009 | 2017-01-02 01:06:53 UTC | #3

Thanks.

-------------------------

