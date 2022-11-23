atai | 2017-01-02 01:09:40 UTC | #1

Hi, Urho3d includes some third party libraries in the build, SDL and stb_image, to name two.  If I link Urho3d to another library that also contains these included libraries, duplicated symbols errors result at link time on GNU/Linux.  What is the general approach to work around this issue?

-------------------------

TheComet | 2017-01-02 01:09:40 UTC | #2

The easiest solution is to build Urho3D as a shared library (-DURHO3D_LIB_TYPE=SHARED).

-------------------------

atai | 2017-01-02 01:09:42 UTC | #3

Yes, building a shared library in general does solve the problem.  However, I find an issue.

Not every Urho3d classes or structs are prefixed with "URHO3D_API" in the declarations.  So what happens is that certain symbols are available when linking to a static Urho3D library, but are undefined when linking to Urho3D as a .so.  And I need to add URHO3D_API to the declaration of the class/struct to make it "visible."
Example: struct RenderPathCommand in RenderPath.h

This is an inconsistency between building Urho3D statically or shared.

-------------------------

weitjong | 2017-01-02 01:09:43 UTC | #4

[quote="atai"]Yes, building a shared library in general does solve the problem.  However, I find an issue.

Not every Urho3d classes or structs are prefixed with "URHO3D_API" in the declarations.  So what happens is that certain symbols are available when linking to a static Urho3D library, but are undefined when linking to Urho3D as a .so.  And I need to add URHO3D_API to the declaration of the class/struct to make it "visible."
Example: struct RenderPathCommand in RenderPath.h

This is an inconsistency between building Urho3D statically or shared.[/quote]
There are two ways to see this. First, If you find a struct/class that should be "rightfully" be exposed as Urho3D API, but it is not, in order to use the library in the downstream project then it is a bug. Second, if the private struct/class is not exposed intentionally then you are literally using private implementation at your own risk. Having said that, by staying within the Urho3D public API would also not guarantee you of future breakage  :wink: . Urho3D devs break the existing API as we see fit. If you strongly believe it is the first and it is a bug then you can log it into Urho3D issue tracker.

-------------------------

atai | 2017-01-02 01:09:44 UTC | #5

In this case, RenderPathCommand is well documented in the documentation, and core developers even answered questions elsewhere in this forum on how to use it to achieve desired rendering effects.  I imagine it is a class for public use...

-------------------------

weitjong | 2017-01-02 01:09:46 UTC | #6

[quote="atai"]In this case, RenderPathCommand is well documented in the documentation, and core developers even answered questions elsewhere in this forum on how to use it to achieve desired rendering effects.  I imagine it is a class for public use...[/quote]
In this particular case, I would agree with you. The changes should be in the master branch shortly.

-------------------------

atai | 2017-01-02 01:09:46 UTC | #7

[quote="weitjong"][quote="atai"]In this case, RenderPathCommand is well documented in the documentation, and core developers even answered questions elsewhere in this forum on how to use it to achieve desired rendering effects.  I imagine it is a class for public use...[/quote]
In this particular case, I would agree with you. The changes should be in the master branch shortly.[/quote]

Thank  you!

-------------------------

