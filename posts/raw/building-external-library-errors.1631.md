Enhex | 2017-01-02 01:09:05 UTC | #1

I'm using Windows 7, 64 bit, VS2015.

Using HEAD, I'm getting some sort of mismatch between release and debug in some test thing.
I'm getting the following error when trying to configure the CMake project:
[code]
CMake Error at CMake/Modules/FindUrho3D.cmake:317 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree.  Use URHO3D_HOME environment variable or build option to
  specify the location of the non-default SDK installation or build tree.

...

Urho3D.lib(LibraryInfo.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '0' doesn't match value '2' in CheckUrho3DLibrary.obj
Urho3D.lib(LibraryInfo.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MD_DynamicRelease' doesn't match value 'MDd_DynamicDebug' in CheckUrho3DLibrary.obj
Urho3D.lib(Precompiled.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '0' doesn't match value '2' in CheckUrho3DLibrary.obj
Urho3D.lib(Precompiled.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MD_DynamicRelease' doesn't match value 'MDd_DynamicDebug' in CheckUrho3DLibrary.obj
[/code]

In my Urho build bin folder, if I rename "Urho3D.lib" to something else, it seems to find "Urho3D_d.lib" and configures without errors, but then it doesn't find "Urho3D.lib".
If I generate with "URHO3D_LIBRARIES-NOTFOUND" it would use "Urho3D_d.lib" in release.

-------------------------

weitjong | 2017-01-02 01:09:05 UTC | #2

Thanks for reporting this. There is a configuration error for try_run() command for WIN32 platform. The fix will be committed shortly.

-------------------------

Enhex | 2017-01-02 01:09:08 UTC | #3

I tested it again. Now configuration works but generation gives the following error:
[code]CMake Error: CMake can not determine linker language for target: MyExecutableName[/code]

"MyExecutableName" is the placeholder from [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html)

-------------------------

weitjong | 2017-01-02 01:09:08 UTC | #4

I am not able to reproduce your error this time. I use the following to test (I hope I didn't miss any instructions): "set build_tree=native-Build && rake cmake vs2015 URHO3D_64BIT=1 && rake make" to build the lib and then on the same terminal session: "rake scaffolding dir=test && cd test && rake cmake vs2015 URHO3D_64BIT=1 URHO3D_HOME=../../native-Build && rake make". I have tried with Debug build configuration and Release build configuration and also with both Debug + Release libs available in the URHO3D_HOME.

-------------------------

Enhex | 2017-01-02 01:09:08 UTC | #5

Ah it was my error, I accidentally deleted the CMakeLists.txt file when cleaning up for a new build and forgot to set my source files folder when making a new one.

-------------------------

