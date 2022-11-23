johnnycable | 2018-03-23 11:50:51 UTC | #1

I'm in the process of converting some old 1.6 things to 1.7.
I'm using 24_Urho2dSprite, but any example would do. 
I add a setup() function to it, and set:

> void Urho2DSprite::Setup() {
>     engineParameters_["FullScreen"] = false;
>     engineParameters_["VSync"] = true;
>     engineParameters_["WindowWidth"]=1280;
>     engineParameters_["WindowHeight"]=800;
> }

expecting to get a precise window size. This is blatantly ignored. The usual

> Graphics* graphics = GetSubsystem<Graphics>();
> range_.width = (float)(graphics->GetWidth());

show range_.width to be 2560. What now?
I'm on Os X 10.13.3

-------------------------

weitjong | 2018-03-23 13:11:31 UTC | #2

if you have Mac with retina display then 1.7 will enable the high DPI support by default. If you don't want to take advantage of it then you need to pass the engine parameter to switch it off.

https://github.com/urho3d/Urho3D/blob/1.7/Source/Urho3D/Engine/Engine.cpp#L256

-------------------------

johnnycable | 2018-03-23 13:32:52 UTC | #3

Setting HIGH-DPI to false allows to set any resolution freely on Os X...
So what's the meaning of this parameter?

-------------------------

weitjong | 2018-03-23 14:02:02 UTC | #4

It passes along the flag (i.e. the developer intention) to SDL. See

https://github.com/urho3d/Urho3D/blob/1.7/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp#L444-L445

and

https://wiki.libsdl.org/SDL_WindowFlags

-------------------------

johnnycable | 2018-03-23 16:06:14 UTC | #5

sdl remark says that:

> On Apple's OS X you must set the NSHighResolutionCapable Info.plist property to YES, otherwise you will not receive a High DPI OpenGL canvas.

gotta try. Thank you.

-------------------------

weitjong | 2018-03-23 16:11:12 UTC | #6

Yes, one of the key/value in the plist need to be updated accordingly and I think we have discussed this before. https://discourse.urho3d.io/t/mac-retina-window/3389

-------------------------

