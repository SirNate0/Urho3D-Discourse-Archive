rogerdv | 2017-01-02 01:02:46 UTC | #1

After the reorganization, cmake no longer generates de exe file in Bin, but in Sources/Bin. how can I fix this behaviour? I tried set (TARGET_NAME ../Bin/exe_name), but it didnt worked.

-------------------------

weitjong | 2017-01-02 01:02:46 UTC | #2

Sorry for any inconvenience has caused. The binary output directory has been renamed to "bin" in the build tree recently in the master branch. As you are referring to reorg, I am assuming you git pull from master branch instead of using 1.32 release. Could you list the directory in your source and build tree(s), make sure all the used to be "Bin" are now "bin". Also make sure when you use cmake-gui to configure/generate the build tree then in the first text field for the source tree you have entered the path to the Urho3D project root (and not the Source subdir as used to be).

-------------------------

rogerdv | 2017-01-02 01:02:47 UTC | #3

Im using master, but last time I compiled my exe was after reorganization, 2 weeks ago. Noticed the change to bin yesterday.
This is my structure
Project
 Bin
  Data@ etc
 Source

Previously, the exe was created in Bin, both in windows and linux. Now, it is created in Sources/Bin. Havent tried to recompile with yesterday's changes.

-------------------------

weitjong | 2017-01-02 01:02:47 UTC | #4

Here is the line that sets the "bin" as output dir. [github.com/urho3d/Urho3D/blob/m ... cmake#L410](https://github.com/urho3d/Urho3D/blob/master/CMake/Modules/Urho3D-CMake-common.cmake#L410)

Like I said before, if you are using cmake-gui or cmake directly, and not using our provided build scripts, then you have to be careful on entering the correct paths for your source tree and build tree.

-------------------------

rogerdv | 2017-01-02 01:02:47 UTC | #5

Im using the sample cmakelists.txt provided in the docs.

-------------------------

weitjong | 2017-01-02 01:02:48 UTC | #6

It is not CMakeLists.txt that has problem here. It is how you invoke cmake to configure/generate your build tree with that CMakeListst.txt.

-------------------------

