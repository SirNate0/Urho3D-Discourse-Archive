misc | 2019-12-12 01:05:56 UTC | #1

I'm debugging my application in the gdb and after continuing from a breakpoint my monitor screen flashes black  and then the urho3d app disappears (the window is gone) but it's still running. Since there's no more window I needed to interrupt it in the gdb as you can see below. Anyone else had the same experience? Any fix? Thanks.
> (gdb) continue
> Continuing.
> ALSA lib pcm.c:8432:(snd_pcm_recover) underrun occurred
> [Thu Dec 12 08:54:57 2019] INFO: OpenGL context lost
> [Thu Dec 12 08:54:57 2019] INFO: Adapter used Intel Open Source Technology Center Mesa DRI Intel(R) Sandybridge Desktop 
> [Thu Dec 12 08:54:57 2019] INFO: Set screen mode 1360x768 rate 60 Hz fullscreen monitor 0
> 
> ^[^[^C                                                                                                                                                                                          
> Thread 1 "learn" received signal SIGINT, Interrupt.                                                                                                                                             
> 0x00007fffef968945 in ?? () from /usr/lib/x86_64-linux-gnu/dri/i965_dri.so                                                                                                                      
> (gdb) kill                                                                                                                                                                                      
> Kill the program being debugged? (y or n) y                                                                                                                                                     
> [Inferior 1 (process 2256) killed]

-------------------------

SirNate0 | 2019-12-12 02:47:13 UTC | #2

Are you using windowed or full screen mode? I don't think I've ever experienced this, but I always use windowed mode.

-------------------------

misc | 2019-12-12 04:56:00 UTC | #3

I use window mode.
> engineParameters_[EP_FULL_SCREEN] = false;  
> engineParameters_[EP_WINDOW_RESIZABLE] = true;
> engineParameters_[EP_WINDOW_WIDTH] = 1280;
> engineParameters_[EP_WINDOW_HEIGHT] = 720;

I'll try an IDE later and see if it also has problems.

-------------------------

misc | 2019-12-13 09:59:52 UTC | #4

Tried it with codeblocks and it doesn't have problems. I generated the build tree, both for cmake_generic and cmake_codeblocks, using the same flags below. Does codeblocks do something extra when I build my project with it? How come its fine when I debug it in codeblocks but not when just using gdb in the terminal?

> -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
>                 -DCMAKE_BUILD_TYPE=Debug -DURHO3D_HOME=*path to urho lib*
> 

By the way, I'm using Ubuntu 19.10, clang-8.0.1, gdb 8.3. Also tried with lldb but with same result.

-------------------------

SirNate0 | 2019-12-13 17:34:59 UTC | #5

My guess is that it's not about extra compilation flags, but about how codeblocks uses the debugger. To check if that's the case you could try copying your command line build executable over the codeblocks built one and then debugging in codeblocks (without building again) or the opposite, try debugging the codeblocks executable from the command line and see if you observe the same behavior.

-------------------------

misc | 2019-12-14 00:28:40 UTC | #6

This is how codeblocks does it:
> Starting debugger: /usr/bin/gdb -nx -fullname -quiet  -args *executable*

Anyway, after testing with the terminal many times, the problem does not seem to occur everyime. I noticed it only happens if I switched windows by pressing alt + tab and not by mouse click. This is after 10 or so attempts. Maybe it's because of my desktop.

At least it works with codeblocks. I'm fine with it.

-------------------------

