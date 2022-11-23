gawag | 2017-01-02 01:08:39 UTC | #1

Edit: The solution is to put add_compile_options("-std=c++11") inside the CMakeLists.txt of the project. That didn't work for me for quite a while for some reason.

Maybe I'm missing something but I think there was a CMake option for Urho 1.4 to enable C++11. Now there isn't and I can't use C++11 stuff in my project (which also doesn't have a C++11 option in the CMake GUI.)
I tried [code]add_compile_options ("-std=c++11")[/code] in my projects CMakeLists.txt but still no C++11.

Also In another really similar project using the same Urho build I have C++11, which is quite odd.
Am I doing something wrong? What happened to the option?

(Using MinGW64 5.2.0 on Windows 10 with Codeblocks)

-------------------------

weitjong | 2017-01-02 01:08:39 UTC | #2

Strictly speaking Urho3D library does not use C++11 standard. The C++11 build option was added briefly by mistake. The option is removed before 1.5 is being released. Well, actually, the logic to enable the standard is still there. It just that it is not being exposed as a build option anymore to avoid the impression that Urho3D code base has a different code path that supports the standard. The C++11 standard is only necessary and auto-enabled when and only when URHO3D_DATABASE_ODBC build option is enabled. You can of course just pass "-DURHO3D_C++11=1" or add the variable yourself in the GUI if you inclined to have it.

-------------------------

namic | 2017-06-29 09:40:52 UTC | #3

Have you guys considered using clang-tidy and the modernizer options? 

https://youtube.com/watch?v=nzCLcfH3pb0

-------------------------

gawag | 2017-01-02 01:08:39 UTC | #4

When I add URHO3D_C++11 with true in the GUI it just disappears when I press configure or generate and C++11 is still disabled.

Also I found out that changing the CMakeList.txt does require deleting the CMake cache so that it sees the change (stupid CMake).
Adding add_compile_options ("-std=c++11") weirdly gives the error C:\dev\Urho3D-1.5\Build\lib\libUrho3D.a(D3D9Graphics.cpp.obj):D3D9Graphics.cpp|| undefined reference to `Direct3DCreate9'|
Same with add_definitions(-std=c++11).
Both have the DirectX11 option enabled and Urho is build with that. Giving the C++11 option seems to disable D3D11 and switch to DirectX9 ??

I searched a bit and found that custom CMake options can be added with something like set(URHO3D_C++11 "1" CACHE BOOL "Enable C++11") in the CMakeLists.txt.
If I add that to the project I get
[code]
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:492 (message):
  Your GCC version 5.2.0

   is too old to enable C++11 standard
Call Stack (most recent call first):
  CMakeLists.txt:29 (include)
[/code]
GCC seems to have full C++11 support starting 4.8.1.
If I try to configure Urho 1.5 itself with that option I get the same error.

The CMake log: [pastebin.com/BbsW0Bq7](http://pastebin.com/BbsW0Bq7)
At the end it seems to check for various C++11 features and some seem to be unavailable. That's weird but I don't want all of them anyway. Can that check be disabled?

add_definitions(URHO3D_C++11) or add_definitions(-DURHO3D_C++11=1) does also not work.

It was so easy with Urho 1.4...

-------------------------

gawag | 2017-01-02 01:08:39 UTC | #5

Now it's getting even weirder. I just tried to build without C++11 at all and it still tries to build with DirectX 9 instead of 11. Doesn't matter if via CMake GUI or cmake_codeblocks.bat with -DURHO3D_D3D11=1.
[code]D3D9Graphics.cpp|| undefined reference to `Direct3DCreate9'[/code]

Both say
[code]-- Found Direct3D: d3d11;d3dcompiler;dxgi;dxguid[/code]
Which looks like it's kinda trying to build with DirectX 11.
I'm now completely rebuilding Urho with D3D11.

Or is it normal that D3D11 needs this Direct3DCreate9?

-------------------------

bvanevery | 2017-01-02 01:08:39 UTC | #6

Are you building [github.com/gawag/UrhoSampleProject](https://github.com/gawag/UrhoSampleProject) ?  I'm building it on Windows 7/10, Visual Studio 2015, CMake 3.3.1.  In the GUI I select different source and destination directories, URHO3D_D3D11, set my URHO3D_HOME to my installed DX11 version of Urho3D, and URHO3D_LUAJIT.  In VS2015 I fire up the results.  I get a spinning planet and a torch, all of the lighting looks correct.  Performance in debug and release is 10 FPS on my crappy old AMD integrated laptop.

I did pull, build, and install a fresh Urho3D today.  Also some of your earlier issues sound like dirty CMake builds.  Sometimes CMake itself is bugged, are you using a recent version?  Are you using VS2015 or something else?

-------------------------

gawag | 2017-01-02 01:08:40 UTC | #7

Yes it's that project.

I rebuild Urho (DirectX 11) and I could build my project. But when starting I can't see anything and the log says a lot of stuff like:
[quote]
[Mon Dec 14 18:21:29 2015] ERROR: Failed to create rasterizer state
[Mon Dec 14 18:21:32 2015] ERROR: Failed to create texture
[Mon Dec 14 18:21:32 2015] ERROR: Failed to create sampler state
[Mon Dec 14 18:21:32 2015] ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT NORMALMAP PERPIXEL):
Could not create vertex shader
[Mon Dec 14 18:21:32 2015] ERROR: Failed to compile pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT NORMALMAP PERPIXEL SPECMAP SPECULAR):
Could not create pixel shader
[/quote]
The Urho samples are also all just black.

Oh I just tried it outside my virtual machine and everything works fine there.
That's odd. Yesterday It worked with DirectX 11 inside the VM besides the broke shadows (different topic). OpenGL never worked in the VM but DirectX usually does.

...
wat
After adding add_compile_options ("-std=c++11") again to the CMakeLists.txt it still compiles (in my Win10 VM), runs (only outside the VM, on Win7) and I even have C++11!

What the fuck was that? That did cost me like my whole fucking day.
That was the first thing I tried because that works in a different project, I also wrote that in my thread start post. Now it works here too. 
CMake fuckup? Urho is not build with that option.

I'm so done.

On to the next issue!

-------------------------

bvanevery | 2017-01-02 01:08:40 UTC | #8

I'm not sure there's a moral to this story.  Virtual machines suck?  MinGW sucks?  I'm guessing you're using that, because -std=c++11 is not an option that VS2015 understands.  The CMake generator for MinGW Makefiles or Code::Blocks sucks?  MinGW handling of DX11 sucks?  C++11 sucks?  I can try to reproduce your problem but you'd need to tell me what your toolchain is and how/where you're inserting your compile flag.  Did you use that flag for both Urho3D and Urho Sample Project?  If you didn't, I wouldn't be shocked at a C++ runtime mismatch.

-------------------------

AReichl | 2017-01-02 01:08:40 UTC | #9

In my opinion there is a mistake in "Urho3D-CMake-common.cmake".

In line 487 you see
execute_process (COMMAND echo COMMAND ${CMAKE_CXX_COMPILER} -std=${STANDARD} -E - RESULT_VARIABLE GCC_EXIT_CODE OUTPUT_QUIET ERROR_QUIET)

I replaced it with
execute_process (COMMAND ${CMAKE_CXX_COMPILER} -std=${STANDARD} -E - RESULT_VARIABLE GCC_EXIT_CODE OUTPUT_QUIET ERROR_QUIET)

( i took away the first "COMMAND echo" )

Now i don't get the message
"Your GCC version ... is too old to enable C++11 standard"
any more.

Probably this is only a workaround by me, because i don't know the real intention of the author.

-------------------------

gawag | 2017-01-02 01:08:41 UTC | #10

No that message seemed to be an error report and the processes seemed to stop there.
Setting URHO3D_C++11 seems to be broken. That's one morale.
weitjong stated that that should work, though either I did it wrong, or my system is weird, or it doesn't work at all. I could try it in my Linux virtual machine, that could work better.
Which methods of doing it are there?

The other morale is that something got really messed up the first time I tried add_compile_options("-std=c++11"). I'm not completely sure if I deleted the CMake cache or did something else wrong. Could have have been a CMake hickup, which shouldn't happen.

My system is MinGW64 5.2.0 on Windows 10 with Codeblocks. The exact same system as described here [urho3d.wikia.com/wiki/Building_U ... nGW/GCC%29](http://urho3d.wikia.com/wiki/Building_Urho_1.5_%28Windows_10,_MinGW/GCC%29)

About -std=c++11: CLang and GCC support that and Visual Studio seems to ignore it (though gives a warning) but has C++11 as default in newer versions. So the biggest compilers seem to be fine with -std=c++11. If there is a better way to do it I would be glad to use and recommend that. Currently it seems to be the only way to get C++11 (if it's not on by default).

-------------------------

weitjong | 2017-01-02 01:08:41 UTC | #11

[quote="AReichl"]In my opinion there is a mistake in "Urho3D-CMake-common.cmake".

In line 487 you see
execute_process (COMMAND echo COMMAND ${CMAKE_CXX_COMPILER} -std=${STANDARD} -E - RESULT_VARIABLE GCC_EXIT_CODE OUTPUT_QUIET ERROR_QUIET)

I replaced it with
execute_process (COMMAND ${CMAKE_CXX_COMPILER} -std=${STANDARD} -E - RESULT_VARIABLE GCC_EXIT_CODE OUTPUT_QUIET ERROR_QUIET)

( i took away the first "COMMAND echo" )

Now i don't get the message
"Your GCC version ... is too old to enable C++11 standard"
any more.

Probably this is only a workaround by me, because i don't know the real intention of the author.[/quote]
No, that is not a mistake. The echo there is intentional. It performs something similar to this on a terminal. Mind the last '-' character in the command as it is also meaningful.

[code]$ echo |g++ -std=gnu++11 -E -[/code]
It basically tests whether the g++ compiler configured for this build tree is capable to accept that standard. It asks the compiler to preprocess an empty source "file" with that standard. The purpose of the echo is to supply this empty content of the file via process pipe which pipes the echo stdout into g++ stdin (that the purpose of the last '-' if you wonder).

[quote="gawag"]Setting URHO3D_C++11 seems to be broken. That's one morale.[/quote]
I just tried it with "-DURHO3D_C++11=1/0" on a CLI, it seems to work for me as advertised. However, if you are using cmake-gui by adding a new variable as I mentioned earlier and didn't work then I apology for that. I have given a wrong information there. I just double check the script now and can confirm the build option is in fact still there. It just being mark as advanced for the GUI users. So, if you are using cmake-gui, you can just tick the advanced check box to reveal those hidden options and enable the URHO3D_C++11 option by ticking it. My apology again. In my last comment, I was recalling I have removed the said option from the documentation. Some how I thought the option was also being removed for good. Instead it is being kept for advanced users such as you . :wink:

-------------------------

AReichl | 2017-01-02 01:08:41 UTC | #12

I think the problem is NOT about finding or activating the option URHO3D_C++11, but if you activate it, you get the message
"Your GCC version ... is too old to enable C++11 standard", even if the compiler supports it.

Maybe this is only on Windows (i use - besides Visual Studio - also gcc 5.2.0).

-------------------------

bvanevery | 2017-01-02 01:08:42 UTC | #13

Ok I've successfully built UrhoSampleProject with codeblocks, mingw-w64, and DX11.  Runs fine.  What are you now wanting me to do regarding C++11?  What are the reproducer steps to show your problem?

BTW I do not agree with the directions given on the wiki for providing DX11.  DirectX has been part of the regular Windows SDKs for a long time now.  Nobody should be told to download the ancient standalone DirectX SDK, it's only useful for legacy projects.

-------------------------

cadaver | 2017-01-02 01:08:42 UTC | #14

Whether or not the DirectX SDK is required depends on the VS version used. The Windows SDK does not attach itself to VS2008 and VS2010 default directories, and that makes the DX SDK (or manual configuration) necessary. On newer versions it is indeed unnecessary.

-------------------------

bvanevery | 2017-01-02 01:08:42 UTC | #15

[quote="cadaver"]Whether or not the DirectX SDK is required depends on the VS version used. The Windows SDK does not attach itself to VS2008 and VS2010 default directories, and that makes the DX SDK (or manual configuration) necessary. On newer versions it is indeed unnecessary.[/quote]

As well as [i]if[/i] VS is being used.   :astonished:  The [url=http://urho3d.wikia.com/wiki/Building_Urho_1.5_%28Windows_10,_MinGW/GCC%29]build advice I was referring to[/url] is for Windows 10 and MinGW-w64.  Downloading the ancient DirectX SDK is totally inapplicable.  I just proved that things build just fine with the Windows 10 SDK.  Frankly the SDK chosen should be the Windows SDK that matches or exceeds the OS in use, from Windows 7 onwards.  I don't know about Vista nor do I care anymore.  Nobody should care about XP.  People who have VS compilers that are too old should be told to get a new one.  Not like VS2015 Community Edition isn't free.  I'll stand by my original statement: the DirectX SDK is legacy use only and nobody should be publicly told to use it.  If people have some legit, complicated legacy reason why they want it, then they should worry about it themselves.

Surprisingly I had edit authority on the wiki, so I nuked the offending text.   :smiley:  The Windows 10 SDK is the one, true, glorious SDK... for Windows 10.

Actually I lied.  It works for Windows 7 too.  So I nuked more text.

-------------------------

Canardian | 2017-01-02 01:08:42 UTC | #16

As I've always said, never upgrade Windows, unless you really need to.
Forget the Windows GUI, you can make a better one with Urho3D in a matter of hours, just run your app in fullscreen mode and add some taskmanager to it.
I had to upgrade from XP to 7, just because XP64 was not very supported.
Windows 7 will last for about 3.5 billion years, since it's 64-bit.
Everyone is having problems with Windows 10, mostly because hardware is not supported.
I had one big problem when switching from XP to 7 with my SoundBlaster32 card, but fortunately I found some 3rd party kx drivers which made it work under 7.

-------------------------

bvanevery | 2017-01-02 01:08:42 UTC | #17

[quote="Canardian"]As I've always said, never upgrade Windows, unless you really need to.[/quote]

That's not accurate right now.  There's a limited 1 year window for upgrading from Windows 7/8 to 10 for free.  It has worked on 2 old clunker laptops from 2007..2008.  Much to my surprise, they're working fine.  One of them had a legit but inherited corporate license for Windows Ultimate.  I'm quite happy to have turned that into an equivalent pricey license for Windows 10.  The other laptop was originally a Vista machine, not legally eligible for the free upgrade.  I proved you can put a pirate copy of Windows 7 on such a machine, then upgrade it to a legit Windows 10.  I don't feel bad about "ripping off" MS just because they orphaned Vista.

[quote]
Everyone is having problems with Windows 10, mostly because hardware is not supported.
[/quote]

False in my case.  The only casualty has been, my cheesy business class laptop with integrated Intel graphics, had pretty marginal OpenGL support.  Transitioning to Windows 10, they haven't provided a modern OpenGL driver at all.  I think it identifies as OpenGL 1.2.  I don't think Intel got on the stick with OpenGL prior to their "HD" stuff, and I think you need at least that to get proper OpenGL support on Windows 10.

I recently gave up on 3 years of Linuxing, as IMO it went nowhere for game development.  Having only DirectX on one of my laptops is fine by me.  

[quote]
I had one big problem when switching from XP to 7 with my SoundBlaster32 card, but fortunately I found some 3rd party kx drivers which made it work under 7.[/quote]

Well I'm not going to recommend a XP --> 10 jump.  I'd be shocked if it worked.  But Vista class machine --> 10 worked.

-------------------------

gawag | 2017-01-02 01:08:42 UTC | #18

[quote="weitjong"]
I just tried it with "-DURHO3D_C++11=1/0" on a CLI, it seems to work for me as advertised.[/quote]
I just tried it again after deleting the build directory and it still tells me that GCC 5.2.0 is too old for C++11.

Also I totally missed that "Advanced" checkbox in the CMake GUI. I tried to add the option manually and it just disappeared.
I just tried checking that option and it again told me that GCC 5.2.0 is too old for C++11.

See: [i.imgur.com/3iGD68y.png](http://i.imgur.com/3iGD68y.png)

[quote]Ok I've successfully built UrhoSampleProject with codeblocks, mingw-w64, and DX11. Runs fine. What are you now wanting me to do regarding C++11? What are the reproducer steps to show your problem?[/quote]
There's no C++11 in that project. Try putting some C++11 in there to test if C++11 is really activated. I replaced a Node* ...=...; with an auto ...=...; to test that.

[quote="bvanevery"]
BTW I do not agree with the directions given on the wiki for providing DX11.  DirectX has been part of the regular Windows SDKs for a long time now.  Nobody should be told to download the ancient standalone DirectX SDK, it's only useful for legacy projects.[/quote]
:unamused: I didn't knew that. I searched for Direct X SDK, found that, it worked and so I wrote that. I was really surprised that it seemed to be sold, from 2010. Getting the DirectX 9 SDK was the usual step when wanting to use DirectX 9 back in my CrystalSpace and Ogre days.
After seeing your(?) wiki edit I researched a while and found a note about DirectX being now part of this Windows SDK in the Wikipedia. [i]The more you know[/i]

I can't find any information if the Windows 10 SDK is also usable for Windows 7 or 8. It sounds weird using W10 SDK in earlier Windows versions. Are you sure one should always pick the newest Windows SDK?
Also I'm not even sure if the Windows SDK is required, some compiler seem to already ship headers for DirectX. I'm going to test that later in a fresh Windows 10 VM. Also I'll test if the "GCC to old for C++11"-issue happens again.

-------------------------

bvanevery | 2017-01-02 01:08:43 UTC | #19

[quote="gawag"]
I can't find any information if the Windows 10 SDK is also usable for Windows 7 or 8.
[/quote]

It is.  I've proven it in the real world on Windows 7.  The official docs on what is supported are in the SDK Release Notes.  Notably, Vista is not supported.  However I didn't try it either.  Of greater importance is where VS2015 is supported.  I don't really care about Vista anymore, those machines got nuked / upgraded to 10.

[quote]
It sounds weird using W10 SDK in earlier Windows versions.
[/quote]

Not weird if you think in terms of "latest greatest SDK with most MS bugfixes."

[quote]
Are you sure one should always pick the newest Windows SDK?
[/quote]

No, not for [i]all [/i]possible scenarios.  But for code written from scratch with Urho3D, seems like the right thing to do.  Anyways Windows 10 SDK and VS2015 is the only way I've ever built anything, regardless of underlying Windows OS.

[quote]
Also I'm not even sure if the Windows SDK is required, some compiler seem to already ship headers for DirectX. 
[/quote]

That I don't know about.  But to be honest I don't really care.  Anyways the tiny number of DirectX Redistributables live in the Windows SDK, so you'll need those.  I think the Windows SDK EULA prohibits just grabbing them to distribute in your own SDK but don't quote me on that.  I do know there's an exception made for a "build system machine".

-------------------------

gawag | 2017-01-02 01:08:43 UTC | #20

I tested the C++11 issue on a fresh Windows 10, it's still there.

I tested a bit, does this help?:
[quote]C:\dev\Urho3D-1.5>echo |g++ -std=gnu++11 -E -
cc1.exe: warning: command line option '-std=gnu++11' is valid for C++/ObjC++ but not for C
# 1 "<stdin>"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "<stdin>"
ECHO is on.

C:\dev\Urho3D-1.5>g++ -std=c++11 -E -
cc1.exe: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C[/quote]
Sounds like g++ is in C mode or something.

Edit:
It works when I uncomment lines 491 and 492 in CMake/Modules/Urho3D-CMake-common.cmake  :stuck_out_tongue:

I guess the C++11 check has to be modified to ignore this warning. Or maybe this cc1.exe warning can be disabled.

Edit 2:
The warning disappeares when the option -x c++ is added:
[quote]C:\dev\Urho3D-1.5>g++ -std=c++11 -E -
cc1.exe: warning: command line option '-std=c++11' is valid for C++/ObjC++ but not for C

C:\dev\Urho3D-1.5>g++ -x c++ -std=c++11 -E -

C:\dev\Urho3D-1.5>echo |g++ -std=gnu++11 -E -
cc1.exe: warning: command line option '-std=gnu++11' is valid for C++/ObjC++ but not for C
# 1 "<stdin>"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "<stdin>"
ECHO is on.

C:\dev\Urho3D-1.5>echo |g++ -x c++ -std=gnu++11 -E -
# 1 "<stdin>"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "<stdin>"
ECHO is on.
[/quote]
I tried putting that -x c++ somewhere in the Urho3D-CMake-common.cmake but no success.

-------------------------

weitjong | 2017-01-02 01:08:45 UTC | #21

The warning is normal. I have that warning too on Linux host system. I just booted into my Windows 10 partition today and was able to reproduce the error. The problem was with the "echo" command. Some how on Windows host system, the plain vanilla "echo" command did not work. In my case, I guess that the side effect after the PATH environment variable has been altered by the batch file provided by standalone MinGW-W64. Probably it happens on your system as well. Anyway, the fix is quite simple and I have committed it to the master branch.

-------------------------

bvanevery | 2017-01-02 01:08:45 UTC | #22

I have a memory of MSYS shells having different quoting behavior from a Windows command prompt.  Something that can drive you nuts in CMake configuration situations.

-------------------------

gawag | 2017-01-02 01:08:47 UTC | #23

[quote]Anyway, the fix is quite simple and I have committed it to the master branch.[/quote]
That fixed it  :smiley:

Why is URHO3D_C++11 hidden under advanced anyway? C++11 is now everywhere and hiding it seems odd. We have 2015 now, even C++14 is nearly there. C++17 is incoming, though still experimental.

-------------------------

Enhex | 2017-01-02 01:08:47 UTC | #24

Also, if modules make it into C++17, it would be a sin not to use them. From what I understand should greatly reduce compile time, and also provides isolation of macros, so the "URHO3D_" prefix won't be needed.
So if modules makes it into C++17, and if Urho's main developers plan to use it, upgrading Urho to C++11/14 would be progress towards it that can be started now, and compatibility with old compilers won't matter anyway once using C++17.

-------------------------

weitjong | 2017-01-02 01:08:47 UTC | #25

You are all welcome to make the changes to the current configuration. I have explained the rationale why it was removed/hidden from public view and only use internally at the moment. Nothing in our code base is cast in stone. When the time comes and things need change, the code will be changed too.

-------------------------

