JeriX | 2017-01-02 00:59:33 UTC | #1

Hi all!
Thank you all very much for such a great game engine!

There is one build issue I want to notice:
cmake has special variable CMAKE_DEBUG_POSTFIX and Urho3D cmake scripts seems to not respect this :frowning: 
android debug release build all generates libUrho3D.a
but mingw debug will produce libUrho3D_d.a and msvs debug build result will be Urho3D_d.lib no matter what value contains CMAKE_DEBUG_POSTFIX :confused: 

Is it behaviour was mentioned to be or it is an issue?

// sorry for my English

-------------------------

weitjong | 2017-01-02 00:59:33 UTC | #2

Welcome to our forum.

Perhaps it will be clear to you when you look at this build script "Source/Engine/CMakeLists.txt". At the top we have this CMake variable set as such. [code]if (WIN32)
    set (CMAKE_DEBUG_POSTFIX _d)
endif ()[/code] Thus, we will always get _d postfix for debug build on Windows platform. On non-Windows platform, it does not make too much sense to differentiate between debug and release library by using postfix naming convention, at least to me.

-------------------------

JeriX | 2017-01-02 00:59:34 UTC | #3

Ok, thx to clarifying this up!

-------------------------

