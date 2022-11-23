feresmu | 2022-05-02 16:47:01 UTC | #1


Hi

This is working fine: script\cmake_vs2019.bat URHO3D_VS2019

But script\cmake_vs2019.bat URHO3D_VS2019 -DURHO3D_OPENGL=1
freezes
The same happens with script\cmake_vs2019.bat URHO3D_VS2019 -DURHO3D_LUA=0

I use CMake 3.19.2 on Windows.
Is correct to do: script\cmake_vs2019.bat URHO3D_VS2019 -DURHO3D_OPENGL=1?
anyone can reproduce it?

-------------------------

elix22 | 2022-05-02 20:01:43 UTC | #2

Insert a space in between -D and the rest .
i.e.   **-DURHO3D_OPENGL=1**  should be  **-D URHO3D_OPENGL=1**

-------------------------

feresmu | 2022-05-06 08:26:07 UTC | #3

Hi.
It works.
But I had to do engineParameters_[EP_OPENGL] = true; in sample.inl
With urho1.7 I didn't have to did it.

Perhaps it must to be in https://urho3d.io/documentation/HEAD/_building.html

-------------------------

