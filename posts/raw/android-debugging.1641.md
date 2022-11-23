boberfly | 2017-01-02 01:09:11 UTC | #1

Hi all,

I've been doing some OpenGL ES 3.1 development for Urho3D (with plans to send the patches back, provided they're at a good enough standard).

Just curious, how do you normally do Android shader development (if anyone does?) I think the main thing I want is the most efficient way to save out a log file back to the development system. Does anyone just make it so it reads files off the dev machine instead of the APK? Do you make a network connection and just send data back this way? I'm hoping Android dev tools have something...

A good use case is that the GL driver returns an error when compiling a shader and a line number, but because the shaders are generated at runtime the line numbers practically mean nothing, so I need a way to dump the final shader to file (I guess via the ShaderCache system). I can't unfortunately print the whole shader to Android's logging system as it's far too long.

I've tried Android's GL ES tracer but it seems to be lacking any of the shader compile calls, and I've found it to sometimes refuse to open trace files generated on the phone with a vague parsing error message (Galaxy S6) so it's a bit useless sadly.

Cheers!
-Alex

-------------------------

sabotage3d | 2017-01-02 01:09:11 UTC | #2

I am quite happy with PVRTune and PVRTrace. I think they both need root access on the phone to install the client app. For the PVRTrace it needs to be recorded on the phone and you have to copy the file to your desktop machine, could be automated with scripts.  It also allows detailed shader and opengl debugging. I found this tutorial quite useful:[url]http://blog.imgtec.com/powervr-developers/powervr-graphics-sdk-tools-explained-quickstart-guide-running-pvrtrace-android[/url]

[b]PVRTune[/b]
[url]https://community.imgtec.com/developers/powervr/tools/pvrtune/[/url]
[b]PVRTrace[/b]
[url]https://community.imgtec.com/developers/powervr/tools/pvrtrace/[/url]

-------------------------

