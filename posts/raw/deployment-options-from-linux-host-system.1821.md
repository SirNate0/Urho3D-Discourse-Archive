mcra3005 | 2017-01-02 01:10:27 UTC | #1

Hi All,

I am hoping to Develop in Urho3D from one host and generate code for Linux, Macosx, Ios, Android and Windows. From Documentation
it appears you can do this, but from Linux Host I can not  seem to compile for OSX and IOS it complains about Xcode Generator not being their.

How does everyone else Achieve this deployment or do you need several Hosts different OS's to Compile executables ???

Any Help thanks

-------------------------

weitjong | 2017-01-02 01:10:27 UTC | #2

Just to be fair, all host systems in theory should be able to do cross-compiling, including Windows host systems to some certain extent. However, in practice there are only a few host systems capable of doing it with flying colors like *nixes do. The reason is simple. They use GCC as the compiler toolchains and they support GNU build system (target triplets). You can see the target triplets at the prefix string of the compiler toolchains in Android NDK, MinGW, linaro GCC for RPI, etc. So, in short if you use Linux host system then you have almost all the targets covered, except OSX and iOS. In theory again Linux host system should be able target OSX because OSX is actually a BSD/Darwin which GCC could target. In practice though it is much easier to target OSX and iOS on an actual Mac host system using xcodebuild as it uses Apple own version of Clang/LLVM, so they target OSX and iOS much better. So, in short you need at least two host systems to do cross-compiling efficiently: Linux and Mac. Now, if you are a cheapskate like me, then you can use paravirtualization technology (e.g. VirtualBox) to squeeze them into just one host (and one guest host). If you comply with Apple DSMOS then that means Mac is your primary host and Linux runs as guest OS under Mac. If you don't care about DSMOS then it can be in the other direction, Linux is the primary host. The online documentation does not say anything explicitly about this, it just assumes you have the right host for the right target you want to build. For me personally, Linux is the one host to rule them all.  :laughing:

-------------------------

