sabotage3d | 2017-01-02 01:07:22 UTC | #1

Hi, 
I am testing GammaCorrection shader on Android but I can't get it to work as it fails to compile.
This is my output.
[code]E/Urho3D  ( 6045): Failed to compile pixel shader GammaCorrection():
E/Urho3D  ( 6045): Compile failed.
E/Urho3D  ( 6045): ERROR: 0:536:33 reserved keyword 'sampler3D'.
E/Urho3D  ( 6045): ERROR: 1 compilation errors. No code generated.[/code]

-------------------------

rasteron | 2017-01-02 01:07:22 UTC | #2

To follow-up on this issue and not to be off topic, but I'm also curious as well on what default Urho3D postprocess/shaders work on Android/iOS.

-------------------------

cadaver | 2017-01-02 01:07:22 UTC | #3

Best bet will be to simply exclude anything related to 3D samplers on GLES. Seems this was forgotten in PostProcess.glsl common functions.

EDIT: should be fixed in master branch.

-------------------------

