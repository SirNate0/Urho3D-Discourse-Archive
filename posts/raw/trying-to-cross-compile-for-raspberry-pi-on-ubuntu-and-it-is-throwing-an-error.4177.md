rahulsanjay18 | 2018-04-16 02:54:24 UTC | #1

Compiling for the raspberry pi has proven to be a problem. It keeps throwing this error

        ./cmake_generic.sh: line 30: /home/rahul/Documents/3dGraph/.bash_helpers.sh: No such file or directory
    CMake Error at CMake/Toolchains/RaspberryPi.cmake:81 (message):
      Could not find Raspberry Pi cross compilation tool.  Use RPI_PREFIX
      environment variable or build option to specify the location of the
      toolchain.

for reference, my environment variables are as follows:
  `  RPI_PREFIX=/home/rahul/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/arm-linux-gnueabihf/bin`

    RPI_SYSROOT=/home/rahul/rpi-sysroot

I tried using this:
[quote="weitjong, post:8, topic:1094"]
Clone the RPI cross-compiler toolchain from github.com/raspberrypi/tools . Set RPI_PREFIX environment variable accordingly. Note this is not just a path to the tool directory. The variable must also contain the prefix string. So, it should be set to something like this: /path/to/raspi-tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/bin/arm-linux-gnueabihf
Clone the RPI sysroot from github.com/urho3d/rpi-sysroot. Set RPI_SYSROOT environment variable to where you have cloned the sysroot.
[/quote]

But the prefix path specified above does not exist; it doesn't point to a folder, but the bin folder does point to a folder with a bunch of files starting with arm-linux-gnueabihf.
I'm guessing the SYSROOT works because it threw that error first but after setting the variable it stopped.

I did download rpi-sysroot and I compiled crosstool-ng for ARM processors, though I did not use that compiled folder because I had no idea where to point the variable from that folder (named x-tools)

-------------------------

weitjong | 2018-04-16 03:54:44 UTC | #2

The RPI CI on Travis is setup as per document in the link above. The CI works as expected. You can use the `.travis.yml` at the root of Urho source tree as a guide to quickly get your development environment setup. HTH.

-------------------------

rahulsanjay18 | 2018-04-16 04:36:51 UTC | #3

I'm sorry. I don't know what you mean by that. I tried looking for .travis.yml everywhere and couldn't find it (looked in repos and in my Linux VM). Am I missing a file? Is this file Urho source the RPI_PREFIX environment variable? Also is the link above the one I posted, because I don't know what you mean by that. Sorry if this is annoying.

-------------------------

Miegamicis | 2018-04-16 05:38:55 UTC | #4

Travis config file is located here: https://github.com/urho3d/Urho3D/blob/master/.travis.yml#L361

-------------------------

rahulsanjay18 | 2018-04-16 20:17:05 UTC | #5

So, do I add that to where my project is and then build using the cmake_rpi.sh script? Or do I somehow run the .yml file? No idea how to use the travis.config file either. Is there anywhere I can find how to run or use the file?

EDIT: Figured out how to use Travis, but now it wants a Rakefile and I don't know what that is nor can I get any info on it

-------------------------

Miegamicis | 2018-04-16 20:21:43 UTC | #6

No, you can't run the file directly (as far as I know) but you can find a lot of useful stuff there - basically a bunch of commands that you can run to get your build up and running

From `.travis.yml`:
```
git clone --depth 1 https://github.com/raspberrypi/tools.git rpi-tools
export RPI_PREFIX=$(pwd)/rpi-tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin/arm-linux-gnueabihf
git clone --depth 1 https://github.com/urho3d/rpi-sysroot.git
export RPI_SYSROOT=$(pwd)/rpi-sysroot 
```

-------------------------

rahulsanjay18 | 2018-04-17 03:09:41 UTC | #7

That got rid of that error, and brought a new one

    CMake Error at CMake/Modules/FindUrho3D.cmake:346 (message):
      Could NOT find compatible Urho3D library in Urho3D SDK installation or
      build tree.  Use URHO3D_HOME environment variable or build option to
      specify the location of the non-default SDK installation or build tree.
      Change Dir: /home/rahul/Documents/3dGraph/work/CMakeFiles/CMakeTmp

      

      Run Build Command:"/usr/bin/make" "cmTC_3da6f/fast"

      /usr/bin/make -f CMakeFiles/cmTC_3da6f.dir/build.make
      CMakeFiles/cmTC_3da6f.dir/build

      make[1]: Entering directory
      '/home/rahul/Documents/3dGraph/work/CMakeFiles/CMakeTmp'

      Building CXX object CMakeFiles/cmTC_3da6f.dir/CheckUrhoLibrary.cpp.o

      
      /home/rahul/Documents/3dGraph/rpi-tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin/arm-linux-gnueabihf-g++
      --sysroot=/home/rahul/Documents/3dGraph/rpi-sysroot -DURHO3D_STATIC_DEFINE
      -I/home/rahul/Urho3D/include
      -Wl,-rpath-link,"/home/rahul/Documents/3dGraph/rpi-sysroot/opt/vc/lib"
      -Wl,-rpath-link,"/home/rahul/Documents/3dGraph/rpi-sysroot/usr/lib/arm-linux-gnueabihf":"/home/rahul/Documents/3dGraph/rpi-sysroot/lib/arm-linux-gnueabihf"
      -o CMakeFiles/cmTC_3da6f.dir/CheckUrhoLibrary.cpp.o -c
      /home/rahul/Documents/3dGraph/CMake/Modules/CheckUrhoLibrary.cpp

      Linking CXX executable cmTC_3da6f

      /usr/bin/cmake -E cmake_link_script CMakeFiles/cmTC_3da6f.dir/link.txt
      --verbose=1

      
      /home/rahul/Documents/3dGraph/rpi-tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin/arm-linux-gnueabihf-g++
      --sysroot=/home/rahul/Documents/3dGraph/rpi-sysroot
      -Wl,-rpath-link,"/home/rahul/Documents/3dGraph/rpi-sysroot/opt/vc/lib"
      -Wl,-rpath-link,"/home/rahul/Documents/3dGraph/rpi-sysroot/usr/lib/arm-linux-gnueabihf":"/home/rahul/Documents/3dGraph/rpi-sysroot/lib/arm-linux-gnueabihf"
      CMakeFiles/cmTC_3da6f.dir/CheckUrhoLibrary.cpp.o -o cmTC_3da6f -rdynamic
      /home/rahul/Urho3D/lib/libUrho3D.a

      /home/rahul/Urho3D/lib/libUrho3D.a: error adding symbols: File format not
      recognized

      collect2: error: ld returned 1 exit status

      CMakeFiles/cmTC_3da6f.dir/build.make:98: recipe for target 'cmTC_3da6f'
      failed

      make[1]: *** [cmTC_3da6f] Error 1

      make[1]: Leaving directory
      '/home/rahul/Documents/3dGraph/work/CMakeFiles/CMakeTmp'

      Makefile:126: recipe for target 'cmTC_3da6f/fast' failed

      make: *** [cmTC_3da6f/fast] Error 2

    Call Stack (most recent call first):
      CMake/Modules/UrhoCommon.cmake:238 (find_package)
      CMakeLists.txt:21 (include)


    -- Configuring incomplete, errors occurred!
    See also "/home/rahul/Documents/3dGraph/work/CMakeFiles/CMakeOutput.log".
    See also "/home/rahul/Documents/3dGraph/work/CMakeFiles/CMakeError.log".

Relevant environment variables: `URHO3D_HOME=/home/rahul/Urho3D`

I thought it may have been that my Urho3D hadnt been compiled for the raspi, but when I tried doing that, this happened

        CMake Error at /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
      Could NOT find Broadcom VideoCore firmware (missing: VIDEOCORE_LIBRARIES
          VIDEOCORE_INCLUDE_DIRS)
        Call Stack (most recent call first):
          /usr/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:388 (_FPHSA_FAILURE_MESSAGE)
          CMake/Modules/FindVideoCore.cmake:39 (find_package_handle_standard_args)
          CMake/Modules/UrhoCommon.cmake:158 (find_package)
          CMakeLists.txt:45 (include)


        -- Configuring incomplete, errors occurred!
        See also "/home/rahul/Urho3D/CMakeFiles/CMakeOutput.log".
        See also "/home/rahul/Urho3D/CMakeFiles/CMakeError.log".

-------------------------

