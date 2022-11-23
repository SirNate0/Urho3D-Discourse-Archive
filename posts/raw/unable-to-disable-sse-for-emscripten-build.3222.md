hcomere | 2017-06-07 09:13:24 UTC | #1

Hello,

I am trying to integrate urho3D into my multiplateform project and i have an issue with the emscripten build.

The emscripten build of urho3D is ok and samples run well.
Then my project link to the urho3d.a but compilation fails with following error :

```
emscripten/xmmintrin.h
SSE instruction set is not enabled
```

So i have recompiled Urho3D with the URHO3D_SSE cmake option disabled and also added -DURHO3D_SSE=0 into my projects definitions.
This has no effect, i still have the same error.

If i look to the code of Math/BoundingBox.h i see 

```
#ifdef URHO3D_SSE
#include <xmmintrin.h>
#endif
```

which should be OK.

But the #define seems to be overriden in Urho3D.h

```
#define URHO3D_STATIC_DEFINE
#define URHO3D_OPENGL
/* #undef URHO3D_D3D11 */
#define URHO3D_SSE
/* #undef URHO3D_DATABASE_ODBC */
/* #undef URHO3D_DATABASE_SQLITE */
/* #undef URHO3D_LUAJIT */
/* #undef URHO3D_TESTING */
```

I think i have missed something :slight_smile:
How can i disable properly SSE ?

Regards,
Harold

-------------------------

weitjong | 2017-06-09 07:09:26 UTC | #2

The export header for Urho3D is auto-generated based on the chosen build options and target platform. It is resided only in the build tree and not in source tree, which should also mean it should be used in tandem with the built library found. If you use our CMake module (FindUrho3D) in your own project then it should automatically process the "found" export header to auto-configure the correct build options for your project, in this case the SSE option. Well, that in theory. Reading from your post, it is still unclear to me where you have done wrong.

-------------------------

hcomere | 2017-06-07 12:33:47 UTC | #3

Ok, i missed the autogeneration part, thanks :)
If i use the Urho3D.h from my asmjs build it compiles.

To use Urho3D as an external lib i copy windows / asmjs generated libs and shared headers into my project's 3rdparty folder. Then my own FindUrho3D.cmake will pick the right libs according to platform.
Therefore headers and libs are versionned and i have to compile only once for each platform.

My issue was that i had copied headers from windows build, with SSE enabled, thinking that there will not have any difference with headers from asmjs build.
Well, in my case i think i have to provide one extra include directory per platform with the right Urho3D.h in and then my FindUrho3D.cmake should add the correct include dir for the current platform.
It should work :)

Regards,
Harold

-------------------------

godan | 2017-06-07 12:37:51 UTC | #4

I have seen this issue as well. I'm not sure why it happens, but nuking my project's build tree and rebuilding worked for me.

The only thing I noticed is that in Urho's CMake > Toolchains, `emscripten.toolchain.cmake` got renamed to `Emscripten.toolchain` at some point. My project still uses the former, and webgl builds fine. Is this a possible cause for the SSE error?

-------------------------

weitjong | 2017-06-07 13:45:25 UTC | #5

No, I don't think the toolchain name changes has anything to do with this. The toolchain name change is for a more consistent naming convention between the CMake module and CMake toolchain. Be expect to have more changes in future. I am planning to pull the good bits out to a separate project in my own repo.

-------------------------

