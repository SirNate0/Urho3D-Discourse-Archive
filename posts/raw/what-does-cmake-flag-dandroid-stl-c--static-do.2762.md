ak88 | 2017-01-31 00:38:29 UTC | #1

Hi all,

I read lots of tutors about Urho3D compilation for android and there is was **cmake** flag `-DANDROID_STL=c++_static` in some of them.
I want to understand what does the this flag and what it affects.
Because when I set up it my compilation fails with a lot of mistakes like:

    ../Urho3D/src2/Source/Urho3D/Physics/CollisionShape.cpp:1054: error: undefined reference to '__dynamic_cast'
    ../Urho3D/src2/Source/Urho3D/Physics/CollisionShape.cpp:1092: error: undefined reference to '__dynamic_cast'
    ../Urho3D/src2/Source/Urho3D/Scene/Scene.cpp:152: error: undefined reference to '__dynamic_cast'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/vector:751: error: undefined reference to '__cxa_call_unexpected'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/map:561: error: undefined reference to '__cxa_call_unexpected'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/map:561: error: undefined reference to '__cxa_call_unexpected'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/map:561: error: undefined reference to '__cxa_call_unexpected'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/ostream:488: error: undefined reference to '__cxa_end_catch'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/ostream:488: error: undefined reference to '__cxa_begin_catch'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/ostream:488: error: undefined reference to '__cxa_end_catch'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/ostream:458: error: undefined reference to '__cxa_begin_catch'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/ostream:755: error: undefined reference to '__cxa_begin_catch'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/string:1210: error: undefined reference to '__cxa_allocate_exception'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/string:1210: error: undefined reference to '__cxa_throw'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/string:1210: error: undefined reference to '__cxa_free_exception'
    ../android-ndk-r12b/sources/cxx-stl/llvm-libc++/libcxx/include/string:1210: error: undefined reference to 'vtable for std::length_error'
    ../android-ndk-r12b/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/../lib/gcc/arm-linux-androideabi/4.9.x/../../../../arm-linux-androideabi/bin/ld: the vtable symbol may be undefined because the class is missing its key function (see go/missingkeymethod)

so I want to understand what it affects and what is wrong with it?

What is the difference from `-DANDROID_STL=gnustl_static` and `-DANDROID_STL=c++_shared`?

Thanks in advance.

-------------------------

weitjong | 2017-01-31 19:08:28 UTC | #2

That build option controls which C++ STL runtime to use. You can find more information about it by reading the comment lines in [android.toolchain.cmake](https://github.com/urho3d/Urho3D/blob/b8ee493454f172aab3edaee433c740bc6bd24e90/CMake/Toolchains/android.toolchain.cmake#L151-L186). This is an "old" CMake toolchain file that was not originally developed by us. So far in the master branch we only use the default STL runtime "gnustl_static" and has never really tested with other runtimes with this old toolchain file. I am not surprised if it is broken with other runtime because it appears the upstream has stopped maintaining this toolchain file (at least the last time I checked it). Therefore, we have decided to rewrite a new toolchain file of our own from scratch. You can find the new toolchain file called [Android.cmake](https://github.com/urho3d/Urho3D/blob/7970801a30740b85047afe5d2c9f85ba2ae6af5d/CMake/Toolchains/Android.cmake#L95-L111) in the "refactor-buildsystem" feature branch. The development for this new toolchain is already completed and all the STL runtimes work. Having said that, we have not really tested it in the wild on the actual applications/devices. If you really need to use LLVM libc++ runtime then you may want to try to build your project with the new toolchain.

-------------------------

ak88 | 2017-01-31 19:08:21 UTC | #3

Thank you for the explanations.

-------------------------

sabotage3d | 2017-01-31 22:05:34 UTC | #4

I have tested refactor-buildsystem for a while I think everything works. The only thing that was weird it couldn't find libc++ library on Android so I had to copy it from android-ndk.

-------------------------

weitjong | 2017-02-01 11:49:43 UTC | #5

That is a bit strange. I think our macro will not only automatically "pull" the dependant shared library into the APK, but also make sure the libs are being loaded in the right order in the SDLActivity class.

-------------------------

