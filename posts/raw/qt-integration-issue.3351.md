kostik1337 | 2017-07-14 14:46:24 UTC | #1

Hello everybody! I am trying to compile ParticleEditor2D by aster2013 (https://github.com/aster2013/ParticleEditor2D). This project seems outdated, I didn't succeeded to compile it with current Urho3D version, all includes are pointing to files in lowest directory, some macros names differ with engine version.
I replaced all wrong stuff (you can check out corrected version at https://github.com/kostik1337/ParticleEditor2D), now the program compiles successfully, but now it crashes right at the start with segfault, gdb prints out this backtrace:
[details=Backtrace]
#0  0x00007ffff3f5a190 in XVisualIDFromVisual () from /usr/lib/x86_64-linux-gnu/libX11.so.6
#1  0x0000000000d2e51e in X11_GL_CreateContext ()
#2  0x0000000000abef4c in SDL_GL_CreateContext ()
#3  0x000000000080af91 in Urho3D::Graphics::Restore() ()
#4  0x000000000080ec2d in Urho3D::Graphics::SetMode(int, int, bool, bool, bool, bool, bool, bool, int, int, int) ()
#5  0x00000000006093c9 in Urho3D::Engine::Initialize(Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant> const&) ()
#6  0x00000000005e7e52 in Urho3D::ParticleEditor::Run() ()
#7  0x00000000005b3d48 in main ()
[/details]
Removing "ExternalWindow" parameter seems to kind of fixing this crash, but it still crashes with another error.

I run Linux Mint 18.1 with Mesa 11.2.0, tried this on two computers, results are same.
Any suggestions how this can be fixed?

-------------------------

kostik1337 | 2017-07-16 12:31:13 UTC | #2

Finally got this working. The problem with external window was that it requires QGLWidget, but QWidget was used.

If someone is interested in fixed version, it's still here: https://github.com/kostik1337/ParticleEditor2D. There still some issues: sometimes it crashes on open dialog with strange crash, and there are some artifacts on QGLWidget, but I hope i'll fix them... someday

-------------------------

