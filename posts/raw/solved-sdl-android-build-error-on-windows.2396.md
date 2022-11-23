yushli | 2017-01-02 01:15:11 UTC | #1

Seems like the newly merged sdl has some config issues:

[  4%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/core/android/SDL_android.c.o
D:/software/Urho3D_dev/Source/ThirdParty/SDL/src/core/android/SDL_android.c: In function 'SDL_Android_Init':
D:/software/Urho3D_dev/Source/ThirdParty/SDL/src/core/android/SDL_android.c:135:5: error: ISO C90 forbids mixed declarations and code [-Werror=declaration-after-statement]
     const char *str;
     ^
D:/software/Urho3D_dev/Source/ThirdParty/SDL/src/core/android/SDL_android.c:142:9: error: ISO C90 forbids mixed declarations and code [-Werror=declaration-after-statement]
         size_t length = strlen(str) + 1;

Windows 8 64bit, Android NDK r12b, latest master branch.

-------------------------

weitjong | 2017-01-02 01:15:11 UTC | #2

This is a known GCC issue and has been reported in our issue tracker. Our build system has been adapted to work with Clang compiler for Android build for sometime now and it builds the latest master branch just fine.

-------------------------

yushli | 2017-01-02 01:15:11 UTC | #3

How can I use Clang instead of GCC? Does Urho3D have a tutorial on that?

-------------------------

weitjong | 2017-01-02 01:15:11 UTC | #4

My apology, I thought it was obvious so I didn't mention how to do it. It can be configured by using CMake build option as always with our build system. See "ANDROID_TOOLCHAIN_NAME" in the [urho3d.github.io/documentation/ ... ld_Options](https://urho3d.github.io/documentation/HEAD/_building.html#Build_Options). If you need more concrete examples, check out how it is used in the Android-CI here.
[github.com/urho3d/Urho3D/blob/f ... #L210-L224](https://github.com/urho3d/Urho3D/blob/f1cb469a34c13c56e9d6a9a75c38539cf2de8bd2/.travis.yml#L210-L224)

-------------------------

yushli | 2017-01-02 01:15:11 UTC | #5

Thank you for the information. You ARE the master on the Urho3D build system. I will try it out.

-------------------------

