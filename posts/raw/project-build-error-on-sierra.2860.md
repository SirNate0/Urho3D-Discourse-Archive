sabotage3d | 2017-03-18 02:04:40 UTC | #1

Hi,

I am trying to build an older project with the latest Urho3d from the master branch on Sierra, but I am getting the error below. My URHO3D_HOME is set to the correct location. And the symlink of the project CMake is pointing to the right location. Urho3d itself builds without errors.

    CMake Error at CMake/Modules/FindUrho3D.cmake:332 (message):
      Could NOT find compatible Urho3D library in Urho3D SDK installation or
      build tree.  Use URHO3D_HOME environment variable or build option to
      specify the location of the non-default SDK installation or build tree.
      Change Dir: /Users/sab/DEV/PF/build/CMakeFiles/CMakeTmp



      Run Build Command:"/usr/bin/make" "cmTC_a0f93/fast"

      /Library/Developer/CommandLineTools/usr/bin/make -f
      CMakeFiles/cmTC_a0f93.dir/build.make CMakeFiles/cmTC_a0f93.dir/build

      Building CXX object CMakeFiles/cmTC_a0f93.dir/CheckUrho3DLibrary.cpp.o

      /Library/Developer/CommandLineTools/usr/bin/c++ -DURHO3D_STATIC_DEFINE -m32
      -o CMakeFiles/cmTC_a0f93.dir/CheckUrho3DLibrary.cpp.o -c
      /Users/sab/DEV/PF/CMake/Modules/CheckUrho3DLibrary.cpp

      /Users/sa/DEV/PF/CMake/Modules/CheckUrho3DLibrary.cpp:23:10:
      fatal error: 'Urho3D/LibraryInfo.h' file not found

      #include <Urho3D/LibraryInfo.h>

               ^

      1 error generated.

      make[1]: *** [CMakeFiles/cmTC_a0f93.dir/CheckUrho3DLibrary.cpp.o] Error 1

      make: *** [cmTC_a0f93/fast] Error 2

    Call Stack (most recent call first):
      CMake/Modules/UrhoCommon.cmake:199 (find_package)
      CMakeLists.txt:18 (include)


    -- Configuring incomplete, errors occurred!
    See also "/Users/sab/DEV/PF/build/CMakeFiles/CMakeOutput.log".

-------------------------

weitjong | 2017-03-07 00:28:39 UTC | #2

In case you haven't tried them. Try run "cmake /path/to/Urho3D/build/tree" one more time. If still not working then nuke and regenerate the build tree from scratch and rebuild Urho3D first.

-------------------------

sabotage3d | 2017-03-08 21:05:00 UTC | #3

Its my bad. I didn't set-up Xcode properly and the command line tools were broken. Everything works fine.

-------------------------

