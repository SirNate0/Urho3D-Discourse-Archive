mcra3005 | 2017-01-02 01:11:00 UTC | #1

Hi All,

I am trying to Deploy to Android i.e. make a .apk , now I can run a Cmake and it works to my Build directory but when I run make it fails. Now i look on forums etc
and followed all ways but when they make on the how to's they never get errors, so no idea I listed the error Below.

From the Urho Repository, i.e. Source code Directory I run the command ./cmake_android.sh $URHO3D_HOME -DURHO3D_SAMPLES=1 and it works.
But when I change directory to Build Directory i.e. $URHO3D_HOME I get the following error any Idea???

Thankyou

[  0%] Linking C static library libFreeType.a
sorry - this program has been built without plugin support
Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/build.make:1108: recipe for target 'Source/ThirdParty/FreeType/libFreeType.a' failed
make[2]: *** [Source/ThirdParty/FreeType/libFreeType.a] Error 176
CMakeFiles/Makefile2:166: recipe for target 'Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all' failed
make[1]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2

-------------------------

weitjong | 2017-01-02 01:11:00 UTC | #2

To target Android platform, you need two things: Android NDK for building native C/C++ source files into libs; and Android SDK for building Java source files + others into apk. The problem you faced seems to be caused by the wrong Android NDK. Check your ANDROID_NDK env-var properly.

-------------------------

mcra3005 | 2017-01-02 01:11:01 UTC | #3

What NDK version I am using ndk 8 which everyone said you had to from other forums due to Compiling issues.

Anyway what version are you using?

My env variable is set to.

What is your env variable set to ?

ANDROID_NDK=/UBUNENV/MIKEDOCUMENTS/TAKEHOME/BUILDURHO3D/android-ndk-r8d

Thanks.

-------------------------

weitjong | 2017-01-02 01:11:01 UTC | #4

To me, the build log entry that said "sorry - this program has been built without plugin support" already gives an indication that something is not correct with your Android NDK. Personally I use Android NDK 10e on Fedora 64-bit host system. My workstation is currently not booted into my Fedora partition so I cannot give you my env-var setting, but it's not rocket science. If you have that variable set properly (ensure you have actually checked it, most of the time people set env-var in their bash profile and forget to relogin or source the profile itself in a same login session) then it may be the Android NDK itself. Have you tried to build something simpler (i.e. not Urho3D project) with your current setup? Upgrade to 10e if you don't have any special reason to keep 8d.

-------------------------

mcra3005 | 2017-01-02 01:11:24 UTC | #5

Thanks everyone your Forum is great and with NDK replaced with recommended NDK  I was
able to get andriod to compile correctly and  tested it on a simulator fine.

-------------------------

