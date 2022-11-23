Sinoid | 2018-03-07 13:42:25 UTC | #1

Has anyone else run into the Y coordinate of `Camera::GetScreenRay` erroneously getting optimized out in release builds?

I had to wrap the function in `#pragma optimize("", off) / #pragma optimize("", on)` for the raycasts to work as everything needing that Y was getting a gobbly-gook value.

- MSVC 2015 (14.0.25431.01 Update 3)
- CMake 3.10.2

-------------------------

Eugene | 2018-03-07 13:45:45 UTC | #2

Wow. I'll try it, have very similar environment on my laptop.

-------------------------

Sinoid | 2018-03-07 14:10:12 UTC | #3

The ray direction `ret.direction_ = ((viewProjInverse * far) - ret.origin_).Normalized();` seems to be the bit that kicks it all off.

Any change that puts the intermediate `((viewProjInverse * far) - ret.origin_)` into meaningful storage results in happiness without the heavy handed disabling of optimization.

    ret.direction_ = ((viewProjInverse * far) - ret.origin_);
    ret.direction_.Normalize();

-------------------------

