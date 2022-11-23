rku | 2018-10-29 14:35:17 UTC | #1

While mucking in UI internals i noticed that `MM_WRAP` causes [mouse to be grabbed](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Input/Input.cpp#L892). Clicks are [not processed](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/UI/UI.cpp#L1705-L1706) when mouse is grabbed. Docs do mention that this happens but do not mention why. So why is this so? And when should `MM_WRAP` be used? And is UI interaction supported when `MM_WRAP` is enabled?

-------------------------

Sinoid | 2018-10-31 03:53:20 UTC | #2

Gave it a quick test, MM_WRAP does disable UI interaction.

-------------------------

