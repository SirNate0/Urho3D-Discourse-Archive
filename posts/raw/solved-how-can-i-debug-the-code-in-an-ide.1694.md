Kanfor | 2017-01-02 01:09:32 UTC | #1

Hi again and thank you for your time.

I can compile a new project perfectly in Netbeans, but when I put a breakpoint for debug, the code not stop there. Why?

Thanks!

-------------------------

valera_rozuvan | 2017-01-02 01:09:32 UTC | #2

Have you seen this tutorial [b]"NetBeans IDE: Debugging C/C++ Projects Tutorial"[/b] [netbeans.org/kb/docs/cnd/debugging.html](https://netbeans.org/kb/docs/cnd/debugging.html) ?

-------------------------

valera_rozuvan | 2017-01-02 01:09:32 UTC | #3

Also, make sure that you compile your project with [b]-g[/b] option, otherwise the debugger won't be able to stop on a breakpoint.

Please see: "GCC: Options for Debugging Your Program" -> [gcc.gnu.org/onlinedocs/gcc/Debu ... tions.html](https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html)

-------------------------

Kanfor | 2017-01-02 01:09:32 UTC | #4

You are my hero  :smiley: 

If I add "-ggdb" at the end of the makefile g++ commmand, it works!  :sunglasses: 

[color=#0000FF]g++ -o MyGame.cpp -O3 -I$(URHO3D_INCLUDE_DIR) -I$(3RD_PARTY_INCLUDE_DIR) -L$(LIB_DIR) -lUrho3D -ggdb[/color]

-------------------------

