SeeSoftware | 2017-11-18 22:55:29 UTC | #1

Im trying to build Urho3D on Windows myself using the build script but i dont know how to pass aditional parameters into the build options, i currently have this:

    cmake_vs2017.bat build64 -URHO3D_64BIT=1 -URHO3D_LUAJIT=1 -URHO3D_SAFE_LUA=1 -URHO3D_C++11=1 -URHO3D_SSE=1 -URHO3D_D3D11=1 -URHO3D_LIB_TYPE=STATIC  

it works but it doesnt generate a 64bit vs2017 project even though i have  -URHO3D_64BIT=1 specified.

-------------------------

JTippetts | 2017-11-18 23:57:31 UTC | #2

You have to prepend -D to the option. -DURHO3D_64BIT=1 etc... See https://urho3d.github.io/documentation/HEAD/_building.html

-------------------------

SeeSoftware | 2017-11-19 01:01:52 UTC | #3

Thanks for the answer ! 
but is it normal to have A LOT of Warnings while building because i got about 300 warnings about type conversion and i even got 3 errors but the library still compiled successfully.
some screen:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/e/e7f88756d9562f7ccd6d93455e663f492a008e9a.png'>

-------------------------

weitjong | 2017-11-19 02:12:49 UTC | #4

The compiler warnings are normal, especially when they are from 3rd-party library dependency. Although we could fix the code to get rid of those warnings, we try not to do so because it will make the 3rd-party library upgrade process more difficult than they already are. As for compiler error, there should not be any, but I haven't tried to build Urho using VS lately. Show us what are those errors.

-------------------------

SeeSoftware | 2017-11-19 01:57:31 UTC | #5

its something with the Assimp lib

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/aefb82f5797e2077a4e269b8cf51968ecda564e8.png'>

it says that '!=' is not valid for a struct and that '!=' wasnt overloaded for type Assimp::WordIterator
but its like in the algorithm file

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/7/74c0e008376b8fe8794125d8c18e585a844f50c7.png'>

-------------------------

weitjong | 2017-11-19 02:09:03 UTC | #6

We recently just upgraded Assimp to version 4.0.1 form 3.2, and the X3D support is a new addition in version 4.0.0. So, it would appear you have found a bug when building that on VS. The latest Assimp build fine on Linux using GCC with all the options enabled. You can raise this as an issue in our issue tracker or better yet, try to fix it and submit it as a PR.

The Assimp is a dependency for AssetImporter tool only.

-------------------------

SeeSoftware | 2017-11-19 02:50:55 UTC | #7

apparently there is allready a issue open for that exact problem

https://github.com/assimp/assimp/issues/1548

its probably going to be fixed in the next release
in the meantime im going to fallback to visual studio 2015

-------------------------

weitjong | 2017-11-19 03:34:48 UTC | #8

Thanks for the link. I have raised it as a new issue, so other VS users could find it if they hit the same problem.
https://github.com/urho3d/Urho3D/issues/2175

-------------------------

