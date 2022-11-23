ak88 | 2017-01-31 00:18:00 UTC | #1

Hi guys,

I am new in Urho3D, and I have a problem to compile it for Android in Debug mode, but it fails with errors like:

    [86%] Linking CXX shared library ../../../libs/armeabi-v7a/libUrho3DPlayer.so
    ../Urho3D/src2/Source/ThirdParty/FreeType/src/gzip/infcodes.c:77: error: undefined reference to 'ft2_z_verbose'
    ../Urho3D/src2/Source/ThirdParty/FreeType/src/gzip/infcodes.c:219: error: undefined reference to 'ft2_z_error'
    ../Urho3D/src2/Source/ThirdParty/FreeType/src/gzip/infcodes.c:224: error: undefined reference to 'ft2_z_verbose'
    ../Urho3D/src2/Source/ThirdParty/FreeType/src/gzip/infcodes.c:250: error: undefined reference to 'ft2_z_verbose'
    ../Urho3D/src2/Source/ThirdParty/FreeType/src/gzip/infblock.c:85: error: undefined reference to 'ft2_z_verbose'
    collect2: error: ld returned 1 exit status
    Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:121: recipe for target 'libs/armeabi-v7a/libUrho3DPlayer.so' failed

I found that the root cause of this error is CMake settings:

    if (XCODE OR CMAKE_BUILD_TYPE STREQUAL Debug)
        add_definitions (-Dz_verbose=ft2_z_verbose -Dz_error=ft2_z_error)
    endif ()
in _../Urho3D/src2/Source/ThirdParty/FreeType/ **CMakeLists.txt**_ (29-31)
I was wonder if somebody can describe why it fails?
Is it possible to compile for Android in debug mode?

**My environment:** 
**Urho3D src**: https://github.com/urho3d/Urho3D 23c5dd1..be9257a  master     -> origin/master
**gcc version** 5.4.1 20160904
**android NDK**: r12b
**android list target** | grep android- : 
id: 1 or "android-21"
 Tag/ABIs : android-tv/armeabi-v7a, android-tv/x86, android-wear/armeabi-v7a, default/armeabi-v7a, default/x86
id: 2 or "android-23"
id: 3 or "android-25"
**run command**: 
> ./cmake_generic.sh ../Urho3D/build/android/debug -DANDROID=1 -DCMAKE_BUILD_TYPE=Debug -DANDROID_NATIVE_API_LEVEL=android-21

BTW **Release** mode compiles OK.
Thanks in advance.

-------------------------

cadaver | 2017-01-31 20:32:37 UTC | #2

This was caused by recent FreeType update. It still needs a fix for debug mode. Should be in now. Thanks for noticing!

-------------------------

