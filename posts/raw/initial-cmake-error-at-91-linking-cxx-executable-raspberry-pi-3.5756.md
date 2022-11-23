Kelmen | 2019-12-10 21:34:09 UTC | #1

Hi all.

I'm trying to make a 3D racing game for a fourth year project on the rpi 3.
I'm after running into a problem when doing the initial cmake to make the build for the engine.

[ 91%] Linking CXX executable ../../../bin/tool/AssetImporter
/usr/bin/ld: ../../ThirdParty/Assimp/code/libAssimp.a(IFCLoader.cpp.o): in function `Assimp::IFCImporter::InternReadFile(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, aiScene*, Assimp::IOSystem*)':
IFCLoader.cpp:(.text+0x7068): undefined reference to `Assimp::IFC::GetSchema(Assimp::STEP::EXPRESS::ConversionSchema&)'
collect2: error: ld returned 1 exit status
make[2]: *** [Source/Tools/AssetImporter/CMakeFiles/AssetImporter.dir/build.make:88: bin/tool/AssetImporter] Error 1
make[1]: *** [CMakeFiles/Makefile2:1639: Source/Tools/AssetImporter/CMakeFiles/AssetImporter.dir/all] Error 2
make: *** [Makefile:152: all] Error 2
 
I'm not sure if its a missing dependency or if its because I'm a total noob when it comes to linux and rpi's or both.

Any help is greatly appreciated

-------------------------

S.L.C | 2019-12-11 07:29:12 UTC | #2

If You are trying to develop it on the RPI as well then you'll need ASSIMP. Otherwise, you might as well disable the asset importer and just keep engine itself.

-------------------------

Kelmen | 2019-12-11 09:54:08 UTC | #3

Hi S.L.C thanks for the reply

is there an apt-get install command call for it or do i need to download and make the library itself?

-------------------------

JimMarlowe | 2019-12-11 15:00:06 UTC | #4

This error happens to me too, on my RPI2,  I "fixed" it by disabling just the IFC Importer.  You can modify this file : Urho3dBaseDir/Source/ThirdParty/Assimp/CMakeLists.txt
At about line 56ish, add the code

if (RPI)
  ADD_DEFINITIONS( -DASSIMP_BUILD_NO_IFC_IMPORTER )
endif()

Then rerun the 'cmake_rpi.sh ...' command again to push out new makefiles, then run the 'make' command, and it should be able to complete. Or start a new build, simpler, but slower.

-------------------------

weitjong | 2019-12-19 14:48:57 UTC | #5

Are you guys using Raspbian or other distro? What is the version of your GCC? I would be interested to know why it failed for your case too, especially if it is reproducible. Our CI uses the cross-compiler GCC version  4.8.3 from [here](https://github.com/raspberrypi/tools/tree/master/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64), rather old but it still gets the job done[?] with the default build options including assimp. I know I am not solving your issue by stating this. Perhaps we should upgrade our CI compiler toolchain. And, perhaps it will then see the same issue[?] Anyone know where a new cross-compiling toolchain for RPI can be found?

-------------------------

