devhang | 2020-08-22 15:11:53 UTC | #1

I wish to use civetweb module to make http API call, modern API service usually require https protocol, I could URHO3D_SSL and URHO3D_SSL_DYNAMIC flag and place related .dll to enable the usage in Windows platform.

But I cannot find a solution in Android. As my some little old NDK experience, I need to include those shared library inside jniLibs and need modified Android.mk to link the library. But seems the project is not similar to JNI project I used to before.

May anyone hint me some guideline for me, am I right to put those libcrypto.so, libssl.so in launcher-app project? or I can static link the library in compile time?

-------------------------

weitjong | 2020-08-23 04:14:32 UTC | #2

I think you can add the external library into your target by configuring it in one of these two ways:

1. Urho3D-way by setting relevant variable before invoking macro to create the target:
    ```
    set (ABSOLUTE_PATH_LIBS /path/to/your/external/lib)
    setup_main_executable ()
    ```
2. CMake-way by calling `target_link_libraries` command after the target has been created:
    ```
    target_link_libraries (your-target-name /path/to/your/external/lib)
    ```

-------------------------

devhang | 2020-10-01 19:17:29 UTC | #3

Really thank you for your solution, finally I am using find_package to include OpenSSL library (just like iOS flow), and also customize "CMake\Modules\FindOpenSSL.cmake" to override the finding path to search the prebuilt OpenSSL shared library for Android ABI (arm64-v8a, armeabi-v7a, x86, x86_64).
It is a bit panic since not familiar with cmake and also Urho3D cmake macro.

By the way, is it possible to use the "Civetweb" (or other Third party library inside Urho3D) in sample project directly (not involve the sub-systems) ? I have encounter some "undefined reference to ..." issues when calling their methods. Thanks very much

-------------------------

weitjong | 2020-10-03 01:19:58 UTC | #4

Yes, you can do that but you have to modify the Utho3D build scripts for that, currently we intentionally hide the engine internal. Search for “BUILD_TREE_ONLY” keyword in the scripts and remove the keyword from the macro call if you really decide to expose the 3rd-party headers in your would-be customized version of engine library. And, you have to use STATIC lib type so that none of the symbols are optimized away yet.

-------------------------

