abcjjy | 2017-01-02 01:02:05 UTC | #1

When I run the sample 37_UIDrag.as, the window shows without cursor. And it does not response to any mouse drag or click. Is it a bug?

And the UI editing functionality in editor seems not support positioning UI element by mouse dragging. Is it a bug?

My environment is OSX 64bit. Urho3d is built with cmake_macos.sh.

Thanks

-------------------------

hdunderscore | 2017-01-02 01:02:05 UTC | #2

The UI Drag sample may have a bug where it hides the mouse (although I believe it was corrected in master).

The editor doesn't support editing UI elements by mouse dragging yet, this feature has been requested: [github.com/urho3d/Urho3D/issues/59](https://github.com/urho3d/Urho3D/issues/59)

-------------------------

