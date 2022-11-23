Matechx | 2017-07-13 10:50:13 UTC | #1

How to pack macos app with xcode?like xxx.app

-------------------------

weitjong | 2017-07-13 11:02:10 UTC | #2

Use the URHO3D_MACOSX_BUNDLE build option.

-------------------------

Matechx | 2017-07-13 11:27:54 UTC | #3

<sh cmake_xcode.sh xxxpath -URHO3D_MACOSX_BUNDLE=1> like this?

-------------------------

weitjong | 2017-07-13 11:31:49 UTC | #4

Read the docs, especially the [build option](https://urho3d.github.io/documentation/HEAD/_building.html#Build_Options) section.

-------------------------

