rogerdv | 2017-01-02 01:03:10 UTC | #1

Tried again to compile luajit support and samples, but they are skipped without any warning, in both linux and Windows.

-------------------------

Enhex | 2017-01-02 01:03:19 UTC | #2

A confusing problem that I had when trying to enable LuaJIT is that I first tried to use URHO3D_LUAJIT_AMALG alone. Later on I found out I need to enable URHO3D_LUAJIT too, that is URHO3D_LUAJIT_AMALG is only an option to set when you have URHO3D_LUAJIT enabled.

-------------------------

rogerdv | 2017-01-02 01:03:40 UTC | #3

Found my probl;em: I wasnt using -D. Now I put it in front of each parameter, just to be sure.

-------------------------

