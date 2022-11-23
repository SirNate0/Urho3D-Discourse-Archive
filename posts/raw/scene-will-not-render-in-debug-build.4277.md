TheGreatMonkey | 2018-06-02 23:44:47 UTC | #1

When I build a debug executable (any of the samples or my own project) in debug I only get a blank screen when the application runs. If I build as release everything renders just fine. Is there some CMake option I missed, or something in Visual Studio I need to change?

-------------------------

Eugene | 2018-06-02 23:44:36 UTC | #2

Let me guess. Do you use Visual Studion 2017 x64 that have broken debug code generator?
 https://discourse.urho3d.io/t/problem-going-from-32-to-64-bit-directx-11/4245/18

-------------------------

TheGreatMonkey | 2018-06-01 07:42:30 UTC | #3

You would guess correctly.

Thanks for the link. As per the comments there I updated VS and everything works great now.

-------------------------

