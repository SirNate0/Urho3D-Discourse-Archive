Sir_Nate | 2017-01-02 01:12:33 UTC | #1

I recently switched (only temporarily, thank goodness) to a low-end HP notebook from my previous laptop. When I ran the executables created on that previous laptop on the new one, I consistently get "Illegal instruction (core dumped)" when I run them. I ran one of them with gdb and it output 
[code]Program received signal SIGILL, Illegal instruction.
0x0000000001071adb in SDL_EventState (type=771, state=0)
    at /home/nathan/Projects/Urho/UrhoRocket/Source/ThirdParty/SDL/src/events/SDL_events.c:591
591	            SDL_disabled_events[hi]->bits[lo/32] |= (1 << (lo&31));[/code]
Any suggestions, as this seems it could be problematic in actually deploying a game later on?

If it helps, my previous setup was an Intel i7-4720hq with an Nvidia GTX960M (it worked both on integrated Intel and Nvidia graphics) and my new setup is an AMD A6-5200 APU with Radeon(TM) HD Graphics.

-------------------------

weitjong | 2017-01-02 01:12:33 UTC | #2

Let me guess. You didn't rebuild your binary on your low-end HP notebook (which probably has different CPU model than the one you used to build the binary), and you have not modified the URHO3D_DEPLOYMENT_TARGET build option from its default value "native" to "generic". If so then you will for sure hit by this illegal instruction problem.

-------------------------

