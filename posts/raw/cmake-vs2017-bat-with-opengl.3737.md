stark7 | 2017-11-13 17:05:38 UTC | #1

Hello,

I am trying to run cmake_vs2017.bat with opengl on windows instead of direct x only I can't figure out how to properly write full console line - can someone please provide some direction on this?

-------------------------

JTippetts | 2017-11-13 18:27:27 UTC | #2

    cmake_vs2017.bat {Build Directory} -DURHO3D_OPENGL=1 {Other defines as needed}

For example, 

    cmake_vs2017.bat BuildVS2017GL -DURHO3D_OPENGL=1 -DURHO3D_64BIT=1 -DURHO3D_LUAJIT=1

-------------------------

