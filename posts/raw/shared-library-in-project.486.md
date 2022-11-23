alexrass | 2017-01-02 01:00:48 UTC | #1

How to make a library based on Urho to use a few executable files?
How to use setup_library () correctly?

-------------------------

weitjong | 2017-01-02 01:00:49 UTC | #2

This Urho3D-specific macro, like its setup[_main]_executable() counterpart, depends on a few CMake variables that need to be set prior to calling the macro. The setup_library() macro also accepts optional arguments which when provided, the macro simply passes them to the underlying CMake add_library() command. See [cmake.org/cmake/help/v3.0/co ... brary.html](http://www.cmake.org/cmake/help/v3.0/command/add_library.html). So for your case, you would need to pass "SHARED" as the extra argument to the macro. Note the macro also performs "other necessary setup" depends on the library type, so if for some reason you can only use the vanilla CMake add_library() command instead of our macro then you will have to configure those "other necessary setup" yourself.

Following are the list of the CMake variables used by the Urho3D-specific macros in general when configuring target (be it executable or library target):

[ul][li]SOURCE_FILES[/li]
[li]INCLUDE_DIRS_ONLY[/li]
[li]LINK_LIBS_ONLY[/li]
[li]LIBS[/li]
[li]ABSOLUTE_PATH_LIBS[/li][/ul]

The first variable is mandatory. It can be defined manually or via another macro called define_source_files(). I think I may need another half a page or so to fully explain how this macro works alone but by default it simply globs all the C++ class implementation and header files "in the current scope" of CMakeLists.txt. The remaining variables are optional but need to be set when your library itself depends on other header or library files.

Last but not the least, once you have configured your new shared library target then you need to tell CMake that your other executable targets are depending on it. In other words, if you stick with Urho all the way then you will definetely need to use the LINK_LIBS_ONLY or LIBS variable when setting up your executable target in order to make it depends on your new shared library. Somewhere in the Urho's macro we pass these variables when calling the underlying CMake target_link_libraries() command which performs the actual dependency setup. See [cmake.org/cmake/help/v3.0/co ... aries.html](http://www.cmake.org/cmake/help/v3.0/command/target_link_libraries.html).

HTH.

-------------------------

alexrass | 2017-01-02 01:00:49 UTC | #3

I post about results...

-------------------------

