ghidra | 2017-01-02 01:13:34 UTC | #1

I was unable to build Urho from source recently where not so long ago, it was no issue.
Using the "default" gcc which is 5.4.0. It appears to be related to this bug (I have not confirmed, this is just a guess): [bugs.launchpad.net/ubuntu/+sour ... ug/1568899](https://bugs.launchpad.net/ubuntu/+source/gcc-5/+bug/1568899)

I guess that because this is where the compilation failed:

[code]
74%
/usr/bin/ld: ../../../bin/Urho3DPlayer: hidden symbol `__cpu_model' in /usr/lib/gcc/x86_64-linux-gnu/5/libgcc.a(cpuinfo.o) is referenced by DSO
/usr/bin/ld: final link failed: Bad value
collect2: error: ld returned 1 exit status
Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:95: recipe for target 'bin/Urho3DPlayer' failed
make[2]: *** [bin/Urho3DPlayer] Error 1
CMakeFiles/Makefile2:1516: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all' failed
make[1]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2
[/code]

but urho was compiling fine on arch with the latest gcc. So I just decided to update gcc. [askubuntu.com/questions/466651/h ... -on-ubuntu](http://askubuntu.com/questions/466651/how-do-i-use-the-latest-gcc-on-ubuntu)
[code]
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-6 g++-6
[/code]

instead of making gcc 6 the default when invoking cmake_generic.sh add the arguments:
[code]
-DCMAKE_C_COMPILER=/usr/bin/gcc-6 -DCMAKE_CXX_COMPILER=/usr/bin/g++-6
[/code]

I was able to compile Urho3D the same as always.
The same was needed to compile my project as well, using Urho as a shared library.

Just wanted to put this out in the ether, incase anyone was trying to build the latest revision with vanilla ubuntu.
also thanks to carnalis for helping me through it as well.

-------------------------

weitjong | 2017-01-02 01:13:35 UTC | #2

This has been reported in [github.com/urho3d/Urho3D/pull/1499](https://github.com/urho3d/Urho3D/pull/1499) too. Since it is a GCC bug, i.e. Urho3D can be built correctly in the previous non-problematic version of GCC, we could only accept the workaround to be incorporated into our build script when there is a check first on the range of problematic GCC versions. I like your "solution" better though as it does not require any change to the build script, however, some may not have the luxury to upgrade to GCC 6.0 now. BTW, I believe you can also use "CC" and "CXX" environment variables to point to your desired compiler toolchain, be it GCC or Clang to workaround this problem.

-------------------------

