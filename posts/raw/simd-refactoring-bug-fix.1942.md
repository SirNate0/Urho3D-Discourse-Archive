weitjong | 2017-01-02 01:11:42 UTC | #1

Thanks to cosmy1 who brought to our attention that we have a problem with one of the Urho3D-specific compiler define being used in Bullet code base. Due to a series of unfortunate events :wink: , we have basically disabled SSE code path in Bullet library for OSX, Linux, and Windows (with MinGW) platforms for the past few months in the master branch. The problem started to happen after we/I (use the latter when you want someone to blame) have baked some of our compiler defines and auto-discovered them later to avoid potential miss-configuration in downstream projects. Unfortunately we have overlooked the "URHO3D_SSE" compiler define was used in our modified version of Bullet source files. As Bullet source files do not include Urho3D export header, the SSE was disabled since then. However, the full story is not that simple. I am not a Bullet expert but it appears that after that Bullet library ended up in a conflicting state and some of you notice it (see [github.com/urho3d/Urho3D/issues/1193](https://github.com/urho3d/Urho3D/issues/1193)). I think the BT_USE_SSE_IN_API was turned off to solve the conflicting state.

The "refactor-simd" branch attempts to address all these. It should bring back SSE code path to those affected platforms. I have already tested as much as possible. So far it appears that vehicle demo tested to run fine on OSX and Linux. The serialization/deserialization of gravity attribute value seems to be working fine on Linux. But we will need your help to test out the branch before it gets merge.

-------------------------

cadaver | 2017-01-02 01:11:42 UTC | #2

Excellent! Yeah, naturally if Bullet can't use the SIMD operations in its vector / matrix class outward-facing API, it cannot use them internally either, which can be a (large) performance loss.

-------------------------

