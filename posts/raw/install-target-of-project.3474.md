TheComet | 2017-08-21 21:38:04 UTC | #1

When invoking ```make install``` or similar on my project, is there an easy way to have the build system copy the local Data and CoreData directories to ```bin/``` (so not the Data/CoreData directories that were installed with Urho3D, but the project specific Data/CoreData directories) and also copy libUrho3D.so as well as libraries that were created using ```setup_library (SHARED)``` to ```lib/```?

-------------------------

weitjong | 2017-08-22 03:02:17 UTC | #2

If you don't explicitly define your own resource dirs then the build system will default it to Urho provided resource dirs. See the usage of `define_resource_dirs()` macro. Although I haven't tested it that way, but I believe `make install` should install whichever resource dirs being explicitly defined.

As for the `libUrho3D.so`, it is already configured to be installed to /lib dir from the install prefix path. You don't need other *.so from other sub-libs that Urho depended on. However, if it is one of your own then of course you have to tell the build system to do that yourself, when the macro has not done it yet (didn't check the code, not 100% sure). 

One thing to note, we have configured the RPATH for common use cases. You may have to adjust this when you have deviated from the common use cases. Anyway, If after installing and you find that `ldd` command output complaints about missing shared libs while they are actually physically installed, now you know what to look for.

-------------------------

TheComet | 2017-08-22 20:22:58 UTC | #3

Okay, I've played around with this some more and I'm not getting anywhere. I have multiple issues.

```
...
set (RESOURCE_DIRS
      "${CMAKE_SOURCE_DIR}/bin/CoreData"
      "${CMAKE_SOURCE_DIR}/bin/Data")
setup_main_executable ()
```

This causes symlinks to be created in build/bin which is good, but ```make install``` does not copy Data or CoreData to the installation directory. How do I make that happen?

```
set (DEST_RUNTIME_DIR ${CMAKE_BINARY_DIR}/bin)
```
Doing this in the top-most CMakeLists.txt for some reason causes the executable file to be deleted right before ```install``` can copy it. If I look in ```build/bin``` right before I run ```make install``` I see the target "lightship-server". When I run ```make install``` I get the following error and suddenly "lightship-server" is no longer in ```build/bin```.
```
-- Install configuration: "Debug"
CMake Error at server/cmake_install.cmake:50 (file):
  file INSTALL cannot find
  "/home/thecomet/documents/programming/cpp/lightship-cpp/build/bin/lightship-server".
Call Stack (most recent call first):
  cmake_install.cmake:38 (include)

```
```
define_source_files (
    GLOB_CPP_PATTERNS src/*.cpp
    GLOB_H_PATTERNS include/lightship/*.h)
setup_library (SHARED)
```
This does not by default install my library to `lib/` so I assume I have to do that myself with:
```
install (TARGETS lightship DESTINATION "lib")
```
which works. I was just wondering if there was an existing mechanism I could use from the Urho3D build system, to, for example, figure out if it should be `lib32` or `lib64` or if there was a mechanism to version my library and create symlinks (e.g. `liblightship.so.1` and a symlink `liblightship.so` to it) or if I have to do this myself.

And finally, libUrho3D.so does not get installed to `lib/`

```
$ make install                                                                                                        (master✱) 
[ 45%] Built target lightship
[ 68%] Built target lightship-server
[ 86%] Built target lightship-client
[100%] Built target lightship-mapconverter
Install the project...
-- Install configuration: "Debug"
-- Installing: /home/thecomet/documents/programming/cpp/lightship-cpp/build/dist/lib/liblightship.so
-- Set runtime path of "/home/thecomet/documents/programming/cpp/lightship-cpp/build/dist/lib/liblightship.so" to ""
-- Installing: /home/thecomet/documents/programming/cpp/lightship-cpp/build/dist/bin/lightship-server
-- Set runtime path of "/home/thecomet/documents/programming/cpp/lightship-cpp/build/dist/bin/lightship-server" to ""
-- Installing: /home/thecomet/documents/programming/cpp/lightship-cpp/build/dist/bin/lightship-client
-- Set runtime path of "/home/thecomet/documents/programming/cpp/lightship-cpp/build/dist/bin/lightship-client" to ""
-- Installing: /home/thecomet/documents/programming/cpp/lightship-cpp/build/dist/bin/lightship-mapconverter
-- Set runtime path of "/home/thecomet/documents/programming/cpp/lightship-cpp/build/dist/bin/lightship-mapconverter" to ""
```
(I'm not going to worry about rpath for now, I first just want this to work). As you can see, libUrho3D.so is not installed. What do I have to do to have it copied along with my game to `lib/`?

Thanks!

-------------------------

weitjong | 2017-08-22 23:55:33 UTC | #4

Hmm, you didn't use the new macro that I mentioned in last comment? Check its usage in the online doc with the latest 1.7 revision.

-------------------------

