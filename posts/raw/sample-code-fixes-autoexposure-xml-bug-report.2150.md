coffee | 2017-01-02 01:13:29 UTC | #1

Cloned Urho3D on Linux. Took the Source/Samples/UrhoSampleProject and copied it out of tree. Did "cmake .". Did, "make". Provides two warnings of redefined defines for URHO3D_OPENGL and URHO3D_SSE. I ignored those even though they are annoying on every make. Run the resulting binary in bin. It works. It complains about missing PostProcess files. The sample's Data/Postprocess directory is incorrectly named. I fix case so that it's Data/PostProcess, as is expected in code. It compiles. It runs, but screen is now entirely black. Narrow down black screen to PostProcess/AutoExposure.xml. Remove line, "effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/AutoExposure.xml"));", and things render properly.

Found old bug stating that AutoExposure doesn't work properly on OpenGL. Also found code in the OpenGL renderer, which according to comments, fixes this issue. Only other comments seem to imply I should see a white screen, not a black screen. Regardless, appears AutoExposure is still broken on OpenGL.

TL/DR: The sample incorrectly has a directory named, "Postprocess". It should be, "PostProcess". Also, AutoExposure.xml seems to be buggy on OpenGL/Linux.

OpenGL vendor string: NVIDIA Corporation
OpenGL renderer string: GeForce GTX 970M/PCIe/SSE2
OpenGL core profile version string: 4.4.0 NVIDIA 364.19
OpenGL core profile shading language version string: 4.40 NVIDIA via Cg compiler
OpenGL core profile context flags: (none)
OpenGL core profile profile mask: core profile

Running on: 4.2.0-42-lowlatency #49-Ubuntu SMP PREEMPT Tue Jun 28 23:12:17 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

How does one begin debugging the AutoExposure.xml bug?

-------------------------

cadaver | 2017-01-02 01:13:29 UTC | #2

Thanks for the path related bug report.
EDIT: Which repository you did clone? Official repo doesn't have Source/Samples/UrhoSampleProject.

As for the AutoExposure shader, last time the problem was uninitialized texture data. The shader needs the previous frame to adjust the exposure, but if it was uninitialized (NaN, possibly) the calculation would never converge to sane values. Typically you would make experimental changes to the AutoExposure shader to determine where the problem lies.

-------------------------

cadaver | 2017-01-02 01:13:31 UTC | #3

Didn't reproduce trouble with AutoExposure shader on Linux, the machine in question was running Ubuntu 14.04 with an Intel GPU.

-------------------------

