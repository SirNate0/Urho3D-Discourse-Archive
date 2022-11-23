JimMarlowe | 2017-01-02 01:08:09 UTC | #1

Any executable I try to run from the Urho3D-1.5-Linux-64bit-STATIC release results in an Illegal instruction. My system is Linux Mint 17 Cinnamon 64 bit, 3.13.0-24 kernel, AMD E2-2000 APU with Radeon(tm) Graphics x 2. It happens in the 32 bit release also. Is it me or the distribution?

md5sum Urho3D-1.5-Linux-64bit-STATIC.tar.gz = d3515a57e4653bd6cf4b7e9a5453db14

./01_HelloWorld -pp ~/darkdove/Urho3D-1.5-Linux-64bit-STATIC/usr/local/share/Urho3D/Resources
Illegal instruction

jimmarlowe@Marlowe-SX2855 ~/darkdove/Urho3D-1.5-Linux-64bit-STATIC/usr/local/bin $ gdb 01_HelloWorld 
GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from 01_HelloWorld...done.
(gdb) run -pp ~/darkdove/Urho3D-1.5-Linux-64bit-STATIC/usr/local/share/Urho3D/Resources
Starting program: /home/jimmarlowe/darkdove/Urho3D-1.5-Linux-64bit-STATIC/usr/local/bin/01_HelloWorld -pp ~/darkdove/Urho3D-1.5-Linux-64bit-STATIC/usr/local/share/Urho3D/Resources
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGILL, Illegal instruction.
0x00000000005cebd8 in Urho3D::String::operator=(char const*) ()
(gdb) where
#0  0x00000000005cebd8 in Urho3D::String::operator=(char const*) ()
#1  0x000000000059dc23 in _GLOBAL__sub_I__ZN6Urho3D20horizontalAlignmentsE ()
#2  0x0000000000cfbd3d in __libc_csu_init ()
#3  0x00007ffff690de55 in __libc_start_main () from /lib/x86_64-linux-gnu/libc.so.6
#4  0x00000000005b93dd in _start ()
(gdb)

-------------------------

weitjong | 2017-01-02 01:08:09 UTC | #2

I think I know the problem. In release 1.5 the build system has introduced a new build option called URHO3D_DEPLOYMENT_TARGET. The option is defaulted to "native" when it is not explicitly set. It is highly likely that all the build artifacts have been built for incompatible CPU type than yours.

-------------------------

JimMarlowe | 2017-01-02 01:08:10 UTC | #3

I have tried the same Urho3D 1.5 release on an Intel Celeron and Atom CPU, with the same result. Are releases really going to be targeted to CPU type or is this done with a command line switch?

-------------------------

weitjong | 2017-01-02 01:08:10 UTC | #4

See this issue [github.com/urho3d/Urho3D/issues/1047](https://github.com/urho3d/Urho3D/issues/1047) which I just logged to our GitHub issue tracker. While we are discussing this, what do other thinks the default should be? Leave it default to "native", so build system will always generate the target binaries most suitable for the user's own machine; and only need to set the deployment target build option at the time of actually releasing a product? Or, leave it default to "generic" or blank, so the generated target binaries by default work for most of the users but may not be optimized for the actual CPU a user/developer has. In either case, deployment target build option should be correctly set at product release time. The question is, what the most convenient default value is?

-------------------------

thebluefish | 2017-01-02 01:08:11 UTC | #5

Quite honestly, we don't need significant performance optimizations on a binary release. Ideally a binary release would be able to reach out to a larger audience and allow more people an easy route to getting their hands dirty working with the engine. 

If they really need performance, which ideally would be towards the end of the development cycle, they should be perfectly capable of building the engine with the parameters that they want, targeting the system that they want.

-------------------------

weitjong | 2017-01-02 01:08:11 UTC | #6

Yes, I have admitted that it was a mistake to leave that new build option to its default value in the Travis CI builds. That will be corrected soon. But still that is not the question in my comment. There are two ways we could correct this:
a) Leave the build option default as it is now in our build system; and specifically pass another value, say 'generic', in .travis.yml to override the default.
OR
b) Change the build option default value in our build system to 'generic'; and we don't need to override anything in the .travis.yml as the default value is already what we want.
Either a) or b) would get the illegal instruction problem corrected in the next generation of the build artifacts. However, whether we choose a) or b) have a big impact on the actual users when they configure/generate build trees in their own host system. Choosing a) would give optimized performance by default on the user own host system, while b) would not.

-------------------------

thebluefish | 2017-01-02 01:08:11 UTC | #7

Ah, in that case I'd say have the default option be for performance.

-------------------------

JimMarlowe | 2017-01-02 01:08:15 UTC | #8

Urho3D-1.5.37-Linux-64bit-STATIC-snapshot works for me, thanks.

-------------------------

weitjong | 2017-01-02 01:08:16 UTC | #9

Thanks for the confirmation. The release artifacts for 1.5 are being regenerated now. The build artifacts will contain new binaries using the same code base as the 1.5 release tag, but minus the packaging problem.

-------------------------

