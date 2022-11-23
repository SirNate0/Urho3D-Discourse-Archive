CrackedP0t | 2017-01-02 01:00:33 UTC | #1

I'm trying to build Urho3d on Ubuntu 14.04, but I can't build the player.
It's weird, because I definately have libGL in my library search path thingy.

The error:
[code]
Linking CXX executable /home/toby/Urho3D-1.31/Bin/Urho3DPlayer
/usr/bin/ld: cannot find -lGL
collect2: error: ld returned 1 exit status
make[2]: *** [/home/user/Urho3D-1.31/Bin/Urho3DPlayer] Error 1
make[1]: *** [Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
make: *** [all] Error 2
[/code]

ldconfig -p | grep libGL.so
[code]
libGL.so.1 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1
libGL.so.1 (libc6) => /usr/lib/i386-linux-gnu/mesa/libGL.so.1
libGL.so (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libGL.so
libGL.so (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/mesa/libGL.so
[/code]

EDIT:
I fixed it by running:
sudo ln -s /usr/lib/i386-linux-gnu/mesa/libGL.so.1 /usr/lib/i386-linux-gnu/libGL.so

-------------------------

friesencr | 2017-01-02 01:00:33 UTC | #2

It sounds like you need mesa: 

[github.com/urho3d/Urho3D/blob/m ... e.txt#L141](https://github.com/urho3d/Urho3D/blob/master/Readme.txt#L141)

For debian based use sudo apt-get install libgl1-mesa-dev

-------------------------

weitjong | 2017-01-02 01:00:33 UTC | #3

Welcome to our forum.

The Mesa driver should only be used as a fallback because it does not have great performance.

To me, your problem looks like a common 32bit vs 64bit mistake. From your output, I assume you have a 64bit host system but you were mistakenly building 32bit Urho because you didn't supply URHO3D_64BIT build option.

-------------------------

friesencr | 2017-01-02 01:00:33 UTC | #4

[quote="weitjong"]Welcome to our forum.

The Mesa driver should only be used as a fallback because it does not have great performance.

To me, your problem looks like a common 32bit vs 64bit mistake. From your output, I assume you have a 64bit host system but you were mistakenly building 32bit Urho because you didn't supply URHO3D_64BIT build option.[/quote]

I wonder if the default settings for the arch should be the host system for linux with 32/64 overrides.

-------------------------

weitjong | 2017-01-02 01:00:33 UTC | #5

Yes. I have thought about that as well when replying the earlier post. With more and more peoples embracing 64-bit OS, the default setting to build Urho3D as 32-bit seems to going out of favor. It should be relatively easy to let the build script detects the native arch of the host system and use that information to set which version of Urho3D library to be built by default. Then the existing URHO3D_64BIT build option can be used just as a way to override the default. So those 64-bit hosts that have 32-bit toolchain installed can still build 32-bit Urho3D as before.

-------------------------

friesencr | 2017-01-02 01:00:33 UTC | #6

[quote="weitjong"]Yes. I have thought about that as well when replying the earlier post. With more and more peoples embracing 64-bit OS, the default setting to build Urho3D as 32-bit seems to going out of favor. It should be relatively easy to let the build script detects the native arch of the host system and use that information to set which version of Urho3D library to be built by default. Then the existing URHO3D_64BIT build option can be used just as a way to override the default. So those 64-bit hosts that have 32-bit toolchain installed can still build 32-bit Urho3D as before.[/quote]

This will probably lead to fewer problems for people just picking up urho and is probably a sensible default for linux users.   In my experience most win games are still 32bit and still seems to be the default.  Someone else may know better.  If a user manages to stick with urho long enough to finish a game hopefully its architecture and build are apparent.

-------------------------

weitjong | 2017-01-02 01:00:34 UTC | #7

Instead of checking the native architecture of the host system, I have just submitted changes that set the default based on the compiler toolchain used by a particular build. So, a 64-bit host system trying to cross-compile for Android or Raspberry-Pi, should still get the correct default setting set to 32-bit (or so I hope).

-------------------------

