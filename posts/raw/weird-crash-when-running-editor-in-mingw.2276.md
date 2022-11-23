Bluemoon | 2017-01-02 01:14:27 UTC | #1

I'm currently experiencing a weird crash when i run the editor. I noticed this after building Urho3D v1.6 and even the current master branch, all in release mode. Funny enough this does not show up in debug mode. My build environment is Mingw-w64 GCC 5.3.0 and I'm on Windows 10. I even setting up a build process with the supplied cmake batch file for mingw and editor still crashed on starting up.
Equally, I noticed this crash in one of my projects that makes use of the scripting subsystem (AngelScript)

-------------------------

cadaver | 2017-01-02 01:14:27 UTC | #2

My guess is Angelscript interacting unfavorably with the compiler in question & optimizations. Quick fix would be to use a known good MinGW, for example 32-bit 4.9.2 has worked problem-free for a long time.

-------------------------

Bluemoon | 2017-01-02 01:14:28 UTC | #3

I just built Urhro3D v1.5 and everything ran well. It seems some commits just before v1.6 broke AngelScript on my platform  :cry:

-------------------------

