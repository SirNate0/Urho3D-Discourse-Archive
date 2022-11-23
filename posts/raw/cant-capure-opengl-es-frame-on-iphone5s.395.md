sophiepeithos | 2017-01-02 01:00:07 UTC | #1

hi,

I find urho3dplayer app can't capture opengl es frame on iphone5s, there is no "capture opengl es frame" icon on top of the debug area.

thanks

-------------------------

cadaver | 2017-01-02 01:00:08 UTC | #2

Welcome to the forums!

Verified that this is the case. Urho3D itself is not in charge of OpenGL initialization, but the SDL2 library is. My guess is that SDL2 initializes rendering in such way that Xcode doesn't realize it's an OpenGL application, and therefore the Debug Navigator doesn't show the whole FPS tab + frame capture option, instead it only shows the CPU and memory statistics. Some things you can do: verify whether the same happens in a barebones SDL2 OpenGL iOS application, and ask about this on the SDL forums.

-------------------------

