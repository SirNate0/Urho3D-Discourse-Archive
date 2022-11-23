cap | 2017-01-02 01:06:55 UTC | #1

Trying to create a new C++ project that builds a static library, and this project links to Urho3D as an external library (similar to the setup I asked about in this topic [topic1380.html](http://discourse.urho3d.io/t/solved-urho3d-as-external-library-in-another-c-project/1332/1) but there the new project built an executable), and once again referring to the advice given here:

[urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html)

Seems the top level CMakeLists.txt (the one in the new project) will need to be modified from what's given at the link above. I'm thinking (hoping) this can be accomplished by simply changing the last line from

setup_main_executable ()

to

setup_library ()

Does that sound right? I will definitely try this and post back here if it works, but I also thought I'd ask about it since I am not well-acquainted with the CMake macros (for those not familiar, these macros like setup_main_executable and setup_library are defined in Urho3D-CMake-common.cmake in CMake/Modules/).

-------------------------

cap | 2017-01-02 01:06:55 UTC | #2

Okay, the above strategy worked.

But note that if yet another project X wanted to link to the static library Y built above, then project X would also have to link to Urho. (I think.... That's what I found by experiment anyway. I had kind of hoped that library Y would be usable on its own, but maybe that's just not how static libs work. I think Visual Studio provides a way to combine the libs to give something like a single lib Y+Urho but maybe that's not a cross platform thing or not a cmake thing. Not sure about all this, just thinking out loud in case it's helpful.)

-------------------------

weitjong | 2017-01-02 01:06:56 UTC | #3

No, that's how static library works in any platforms I have known of. It basically just an archive of object files. Unless you have explicitly instructed your build system to archive all objects into one (this is an extra step that CMake does not do for you), the user of your static libraries need to link to each one of them for the final target normally. Perhaps you have confused it with a shared library. A shared library works differently where it has linked all the objects into one by default. So, in general you only need one shared lib (from your previous build stage) in linking the final target.

-------------------------

