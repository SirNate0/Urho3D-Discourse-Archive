simple | 2017-01-02 01:08:09 UTC | #1

I use [b]MSVC2010 Source.zip[/b] i build by this command line:
[b]cmake_vs2010 f:\projects\urho -DURHO3D_SAMPLES=1 -DURHO3D_LIB_TYPE=SHARED -DURHO3D_OPENGL=1[/b]
When i open ALL_BUILD.sln in MSVC IDE and I build with DEBUG option, everything is ok, and all urho examples working fine.
But problem is then if i change to RELEASE MODE in IDE.
Every example where are [b]scene_->CreateComponent<Octree>();[/b] going to crash in release-mode, only working examples where are 2D and sound examples (so they not use Octree).
Even urho's SceneEditor crash (only work in DEBUG).
Binary version of urho package's (like: Urho3D-1.5-Windows-SHARED-3D9.zip), i think they are compiled in DEBUG mode, because dll have 20mb (so editor work), RELEASE mode of dll have 8mb.

[img]http://images.tinypic.pl/i/00725/zxh9eqtau1o6.png[/img]

-------------------------

cadaver | 2017-01-02 01:08:09 UTC | #2

Try the build option URHO3D_SSE=0. Urho V1.5 has increased use of SSE math optimizations and it looks like VS2010 will hit some nasty compiler bugs. Alternatively, upgrade to a newer VS.

Btw. if you are using V1.5 tag version, it's important that the value of URHO3D_SSE matches between Urho and any own projects you may compile. Otherwise at least the BoundingBox class will be ABI incompatible. This is no longer critical in the current head revision.

-------------------------

simple | 2017-01-02 01:08:09 UTC | #3

Ok, thanx.
With -DURHO3D_SSE=0 its works.

-------------------------

weitjong | 2017-01-02 01:08:09 UTC | #4

Just want to add that all the release artifacts for Windows platform were generated using MinGW for OpenGL and D3D9. Only D3D11 artifacts were generated using VS2015. All release artifacts were built using Release build configuration. The increase in size that you observed in MinGW build is due to GCC and its C++ standard lib being statically linked into the target binaries, even for shared library target.

-------------------------

