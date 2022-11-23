ab4daa | 2019-03-17 05:30:36 UTC | #1

In D3D11Graphics.cpp, d3dBlendEnable[] does not have the same size as d3dSrcBlend[].

They should have the same size because they will be indexed by the same blend mode, right?

-------------------------

weitjong | 2019-03-12 14:58:55 UTC | #2

Yes, it looks like it.

-------------------------

weitjong | 2019-03-12 15:04:50 UTC | #3

I believe the code for 3D9 has the mistake too.

-------------------------

ab4daa | 2019-03-12 15:06:42 UTC | #4

Yes, d3dBlendEnable[] have different size in D3D9Graphics.cpp, too.

-------------------------

weitjong | 2019-03-12 15:10:23 UTC | #5

Care to submit that as a PR? I could do it too but I don't like to take other's credit :)

-------------------------

ab4daa | 2019-03-13 02:52:48 UTC | #6

OK.


Here is [PR](https://github.com/urho3d/Urho3D/pull/2429)

-------------------------

