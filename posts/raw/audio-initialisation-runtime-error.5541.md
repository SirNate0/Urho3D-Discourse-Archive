EoanErmine | 2019-09-01 15:08:12 UTC | #1

Any started Urho3D compiled binary (C++/AngelScript) returns the following error in OpenSUSE Tumbleweed XFCE Kernel 5.1.10-1-default.

`ERROR: Failed to initialise SDL subsystem: Audio target 'pulse' not available`

And the sound (Because of that error, I think) not play in any Urho3D project.

-------------------------

Modanung | 2019-09-01 17:14:03 UTC | #2

Welcome to the forums! :confetti_ball: :slightly_smiling_face:

Have you read the *building* documentation carefully? Especially the bits about the sound server prerequisites and `SDL_AUDIODRIVER` environment variable might be useful.

https://urho3d.github.io/documentation/HEAD/_building.html

-------------------------

