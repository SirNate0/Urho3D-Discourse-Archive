practicing01 | 2017-01-02 01:08:20 UTC | #1

Hello, I noticed that in the angelscript ninja demo, bitwise operators are used [code]if (joystick.hatPosition[0] & HAT_LEFT != 0)[/code]. How can I use bitwise operators with lua since urho used 5.1 but only 5.2 has the bit32 library?  Thanks for any help.

-------------------------

thebluefish | 2017-01-02 01:08:21 UTC | #2

LuaJIT provides several LUA extensions out-of-the-box. This includes Lua BitOp.

-------------------------

