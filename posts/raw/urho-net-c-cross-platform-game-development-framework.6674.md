elix22 | 2021-04-25 11:26:29 UTC | #1

In the last couple of months I had a lot of spare time (thanks to Covid) 
I have been working on a C# cross platform game development framework .
Basically it's updated C# bindings (using UrhoSharp binding tools) for Urho3D .
Currently runs on Windows,Linux,Mac,iOS,Android.
No dependency on Xamarin.iOS or Xamarin.Android .
First class Visual Studio Code support on all 3 platforms Linux,Window,MacOS (autocompletion , debugging , Mobile deployment for iOS and Android) 
Why I did it ? 
Because I can :)
And I wanted to check how much effort would it take to embed the Mono runtime into Urho3D.
It was quit challenging but I am quite happy with the result.
it is still W.I.P. and I don't know yet how much time will I continue to invest in this , it all depends on the feedback I will get from the games development community and my interest in this.  

You can find it here : 
https://github.com/Urho-Net

-------------------------

glebedev | 2021-01-27 16:11:35 UTC | #2

Is UWP supported as a target platform?

-------------------------

elix22 | 2021-01-27 17:21:00 UTC | #3

Not right now
I looked briefly into UrhoSharp's UWP implementation , so in theory it should be possible but will require some work ,   I can't provide any estimate at the current present time .
My current objective is to stabilize it first on the 5 supported platforms before trying to add more platforms .

-------------------------

rku | 2021-01-27 19:08:13 UTC | #4

I do not see source code, only binaries.

-------------------------

elix22 | 2021-01-27 20:16:28 UTC | #5

Right , the package contains all the required scripts
And precompiled binaries.
The source code is scattered over several repositories.
I provided all the links to the source code in Github
Just read the Readme file carefully.
The only thing I didn’t provide yet is how to build and assemble this package , which is done manually.
This is still an ongoing development and the structure of the package might change .
Once I will be satisfied with the end result
I will provide an how-to to build it.

-------------------------

dertom | 2021-01-28 14:49:43 UTC | #6

Looks good and so userfriendly already. :+1:

-------------------------

elix22 | 2021-01-28 17:27:16 UTC | #7

Thanks for the feedback 
There are still issues that have to be resolved
Such as project size which I find it to be unacceptable , Working on reducing it .
Android AOT support , for now only supports JIT (currently only iOS and Desktop support AOT)
WebAssembly support.
Maybe UWP support.
Some annoying bugs that have to be fixed
And more goodies later ...

-------------------------

rku | 2021-01-30 07:14:31 UTC | #8

Did you get bindings generator to run on OS other than MacOS?

-------------------------

elix22 | 2021-01-30 09:45:50 UTC | #9

No I didn’t try on any other OS.
I used MacOS to generate them and I also added some tweaks to the outcome to make it work.

Once the bindings are generated you can compile them on any OS that has Mono installed

-------------------------

elix22 | 2021-01-31 20:23:05 UTC | #10

Reduced project size from 440 MB to 58 MB (18 MB for Assets Data/CoreData).
One will have to call "configure.sh/configure.bat" once (or it will be called transparently once a new project is created).
This script should be called every time the Urho.Net folder is moved to another destination .

I added a new VS code Action : "Shift+Ctrl+P Clean" (Shift+Command+P Clean on Mac)
Will delete/clean all the folder/files that were generated during the build process (Desktop/iOS/Android)

 du -sch TestApp/*
18M TestApp/Assets
4.0K TestApp/Program.cs
1.4M TestApp/References
28K TestApp/Source
12K TestApp/TestApp.csproj
276K TestApp/include
28K TestApp/script
38M TestApp/tools
58M total

-------------------------

rku | 2021-02-04 13:57:46 UTC | #11

Are you intend on making working on engine any more approachable? Working on a complicated project it is inevitable that one will have to modify engine to add features. Seem like not only adding stuff to engine is complicated, exposing new functionality to C# is also a major obstacle.

-------------------------

Eugene | 2021-02-04 15:50:39 UTC | #12

[quote="rku, post:11, topic:6674"]
Working on a complicated project it is inevitable that one will have to modify engine to add features.
[/quote]
By the way, I don’t think it’s as obvious as you state.

For example, only a fraction of per cent of Unity users need access to Unity sources code. Most of users are just fine working with engine API. 

Same goes for Urho: e.g. Hellbreaker was made entirely in AS.
There *is* a domain of projects that don’t need touching engine code ever.

-------------------------

elix22 | 2021-02-04 15:56:29 UTC | #13

Just yesterday I added new functionality and a new sample that reflects it.
@Lumak's  OffroadVehicle Sample in C# (see link bellow).
One will have to use the latest Urho.Net branch to  check it.
Currently I am writing Hot-Reload sample (I am very eager to know how it will work).
Frankly I don't know what are my next plans  .
I decide what to do next after my morning coffee , just trying to enjoy the process .

https://github.com/elix22/Urho.Net-Samples/tree/main/OffroadVehicle

P.S.
I wrote some other working solutions , see below .
I decided to halt  although other game dev teams showed some interest in one of these solutions.  


Hashlink runtime integration 
(Some other game engine dev team showed some interest in this one)

https://github.com/elix22/Urho3D-Hashlink

https://github.com/elix22/Urho3D/tree/hashlink-poc


Cling embedding 

https://github.com/elix22/cling
https://github.com/elix22/Urho3D/tree/cling-embed-poc
https://github.com/elix22/Urho3D/tree/cling-embed-poc/Source/Samples/71_ClingEmbedded

-------------------------

1vanK | 2021-02-04 17:34:44 UTC | #14

Hellbreaker uses own CharacterController written in C ++

-------------------------

rku | 2021-02-05 07:22:13 UTC | #16

[quote="Eugene, post:12, topic:6674"]
By the way, I don’t think it’s as obvious as you state.

For example, only a fraction of per cent of Unity users need access to Unity sources code. Most of users are just fine working with engine API.
[/quote]


This is hardly a fair comparison. Unity is far more complete than any opensource hobby project will ever be. And yet, while only a fraction of unity users _have_ source code access, majority (again im talking about commercial projects that are not of irrelevant size) _need_ it. Internet is full of "unity this", "unity that", "unity but stalled our progress" etc etc. Those people would be perfectly happy fixing bugs they encounter themselves, but they can not. The fact that they can not does not mean they do not need it.

---

Basically what im saying is that a convenient way to develop entire codebase is paramount to the project success. Unity is so popular for a reason - it drastically reduces iteration times. Scattering codebase across multiple independent projects, where final product is stacked on to pile of binary artifacts, some of which need generating on a specific operating system is opposite of low iteration times.

[quote="elix22, post:13, topic:6674"]
Currently I am writing Hot-Reload sample (I am very eager to know how it will work).
[/quote]
Awesome! I can share how i did it. Nothing spectacular really. All you do on hot-reload is:
1. Serialize scene.
2. Destroy scene.
3. Unregister factories that create objects backed by C#.
4. Load new .net assembly.
5. Register factories of types from the new assembly.
6. Deserialize scene.

This still has a minor memory leak as we do not unload out of date assemblies. Flax has custom patches for mono to do that. I read that .net core is getting this functionality officially as well. I plan to investigate this when .net runtimes used on all platforms (including mobile) support this. I suspect this will be with .net 6, when it is ported to mobiles, but im not certain.

P.S. To avoid file-in-use issues you should never straight-load .net assembly produced by compiler. Instead this file should be copied, and also patched a bit to fix .pdb path so debugging works. Then load a copy. When original file updates - make a new copy and do the same. If you would load a file produced by compiler, you wont be able to update code and recompile as file now is in use and remains such for the duration of application execution.

-------------------------

elix22 | 2021-02-08 13:41:14 UTC | #17

Thanks for the tips .
Yes I am aware of locked dll file issues  . 
Basically in my implementation I am loading the source file into memory and compiling it using the  the Roslyn compiler and using the  generated assembly to instantiate the component  .
- I load the source file of the modified component
- compile it 
- if compilation succeeds , go through all the nodes in the scene that contain this component
-- remove old one , instantiate new one and add it to the node.

It supports only Desktop (Windows,Mac,Linux) 
 
My Hot-Reload sample implementation can be found in the link below (must use the latest Urho.Net main branch)

https://github.com/elix22/Urho.Net-Samples/tree/main/HotReload


P.S. Flax is an good example on what can be achieved by 1 person (after 8 years of development)
      I know that there is some hype around it but I don't think that it is in any way
      posing a threat/challenge to any game engine  because if its licensing terms .

-------------------------

George1 | 2021-02-11 15:43:58 UTC | #18

Hi elix22 great work. 
I have just tested your .Net examples, they works great.
The hot load example is fantastic, but there is an error when you exit the application.  See images below.

![image|690x157](upload://3dUCA0EjP2CVVLxF5WOb9dZ6nJl.png) 

![image|574x104](upload://g7Ute1lSFi7ylGTkx8ZNJQUVOjk.png) 

Maybe it is due to multi-thread.

-------------------------

elix22 | 2021-02-11 18:26:08 UTC | #19

Thanks @George1 , glad you liked it :slight_smile:  .
Yes I am aware of this issue , it occurs only on Windows , it works fine on MacOS and Linux.
I will look into it once I will feature complete this framework.

As a temporary workaround you can do the following 

                    bool isWindows = System.Runtime.InteropServices.RuntimeInformation
                                               .IsOSPlatform(System.Runtime.InteropServices.OSPlatform.Windows);
                    if(isWindows == false)
                    {
                         context?.Unload();
                    }

-------------------------

George1 | 2021-02-11 21:57:26 UTC | #20

Thanks elix22,  that solves the stack error on Windows for the hot load example.

-------------------------

elix22 | 2021-02-15 14:07:04 UTC | #21

More Demo Samples (verified on desktop and mobile , at least most of them)
Also Updated Urho.Net , in sync with my own latest Urho3D master branch.

Added support for HDPI on iOS Metal graphics backend \
(In VS-Code it's "**Shift+Cmd+P , Run Action , ios-deploy-metal or ios-build-metal**").

If you try them , make sure you are using the latest Urho.Net master .
Every time you update Urho.Net ,  first make a clean build in your project \
(In VS-Code it's "**Shift + Ctrl/Cmd + P , Run Action , clean**" )

-------------------------

elix22 | 2021-02-28 11:12:21 UTC | #22

Now it's networking time .
Added 2 new samples .
Verified on Desktop (Windows,Linux,Mac)  and mobiles (iOS/Android) , using WIFI LAN.
Must be used with the latest Urho.Net master branch.

- Chat -  Messaging app between multiple devices.
- SceneReplication - Running authoritative  Synchronized scene on multiple devices

-------------------------

Modanung | 2021-02-28 11:46:48 UTC | #23

You may want to register that domain.

-------------------------

Modanung | 2021-02-28 11:53:22 UTC | #24

> :scroll::musical_score: 
> Fear for the day when it returns from the dead
And traps you into a *net*
> [:metal:](http://www.mikseri.net/artists/urho/fish-executioner/364603)

-------------------------

elix22 | 2021-02-28 16:29:21 UTC | #25

Ik vond het leuk :+1:

-------------------------

Modanung | 2021-02-28 16:36:14 UTC | #26

@cadaver's words, niet de mijne. :slightly_smiling_face:

-------------------------

elix22 | 2021-03-05 15:34:29 UTC | #27

Added new Game sample ,  FlappyUrho
Basically it's a port from C++ to C#
The original was written by @1vanK  and later enhanced by @Modanung 
 
Verified on Desktop (Windows,Linux,Mac) and mobiles (iOS/Android) .
Must be used with the latest [Urho.Net ](https://github.com/elix22/Urho.Net) master branch otherwise it won't work .

-------------------------

elix22 | 2021-03-23 14:27:31 UTC | #28

New Version , added new Component support **KinematicCharacterController** (+ fixes)
2 new Sample demos utilizing the **KinematicCharacterController** component
* MovingPlatforms
* KinematicCharacterDemo

Verified on Desktop (Windows,Linux,Mac),  iOS (GLES2 & Metal) , Android (GLES2).
Must be used with the latest [Urho.Net ](https://github.com/elix22/Urho.Net) master branch otherwise it won’t work .

-------------------------

sahandt | 2021-03-28 11:40:53 UTC | #29

Nice job elix. Do you think it will work on UWP too?

-------------------------

glebedev | 2021-03-28 15:46:27 UTC | #30

Some Urho3D compatible content you may be interested too ;-)
https://dev.azure.com/gloomprojects/Urho3DAssets/_packaging?_a=feed&feed=Urho3DAssets%40Local

-------------------------

elix22 | 2021-03-28 20:42:53 UTC | #31

@sahandt 
I plan to add UWP (including Xbox)  support in the coming months .
Will happen after my game submission ( based upon this framework ) to the Apple App store & Google Play store.

@glebedev thanks for the assets ,  looks really cool,  I will use them in future demo samples.

-------------------------

glebedev | 2021-03-28 22:01:43 UTC | #32

My UWP app made with Urho3D. Works on XBox.
https://www.microsoft.com/en-gb/p/psychedelic-radio-player/9p9f2j918b2t

-------------------------

najak3d | 2021-04-08 02:33:30 UTC | #33

@elix22 - FYI, our commercial project is currently using UrhoSharp, but since this branch is now years old, and nobody that I'm aware of can even rebuild it...   It makes UrhoSharp not-good for us.

We're looking for an alternate product, and the two candidates we currently see are:
1. Urho3DNET - by @glebedev  - built on Rbfx,   AND
2. Urho.Net - your project here, built on vanilla Urho3D.

There is a HUGE gap currently for .NET5/Xamarin developers who want to do 3D rendering or game development.   Urho.NET and Urho3DNET - both seem like they could potentially step up and fill this void.

-------------------------

elix22 | 2021-04-08 15:22:27 UTC | #34

Urho.Net is still in the development phase .
Although  It runs pretty well on Desktop and mobiles ,  I wouldn't recommend using it in a commercial project.
Please note that it is not dependent on Xamarin in any way , as a result you won't be able to use it in conjunction with Xamarin Forms .

-------------------------

elix22 | 2021-04-25 11:36:11 UTC | #35

Added more demo samples 
More fixes 
New link 
https://github.com/Urho-Net

I uploaded the samples to Google Play (Open Testing)  .
The motivation is to verify the framework on as many devices as possible and to fix any critical issues that will arise during the testing process.
https://play.google.com/store/apps/details?id=com.elix22.urhonetsamples

-------------------------

Modanung | 2021-04-25 12:52:24 UTC | #36

[![urhonet](upload://7lC869onWDAkloOTBfwrGue5vM5.png)](https://luckeyproductions.nl/blends/urhonet.blend)

Happy huntin'

-------------------------

najak3d | 2021-05-28 08:58:37 UTC | #37

@elix22  - we are very interested in what you are doing here.  We are a commercial app written in Xamarain.Forms, and so in order for us to use it, we'd need to be able to render it in this context.

We have an alternate idea that might be easy/appealing.  Can you make your Urho.Net run "headless" (without a visible Render Surface), such that it still has it's OpenGL Context with RenderBuffer for the virtual Screen -- but doesn't bind this to a visible surface.

We would then use Urho's facility for copying the RenderBuffer frame to Bitmap Pixels in RAM.  From there, it's easy to display that bitmap to a visible PictureBox control (or for us, this will be a SkiaCanvasView, showing a Skiasharp Bitmap).

We've already tested this concept with UrhoSharp, and it's performant (takes about 1 msec total).  The only issue is that in order to start up Urho, it seems to want to be bound to a visible Render Surface.  Instead, we're just wanting to have it run headless, and allow us to set the Render Buffer size/format manually.

Thoughts?

-------------------------

elix22 | 2021-05-29 08:00:53 UTC | #38

Headless by definition doesn't include any Graphics backend , no OpenGL context.

My main objective in this framework was to decouple it entirely from Xamarin and Xamarin.Forms , zero dependency (otherwise I could have continued to enhance and bring UrhoSharp up to date).
I want it to be truly multi-platform and at the same time utilize state of the art multi-platform development tools such as Visual-Studio-Code (in my view it outperforms some commercial IDE's)

.NET MAUI looks very promising but it doesn't support Linux yet.
Once it will become more clear about the support of .Net MAUI for Linux , I will review it and try to find a way to integrate it with Urho.Net

For now my main objective is to focus on adding more features (to support my game)  such as plugins , the first one "Admob , Google mobile ads " support for Android and iOS will be available in my Urho.Net repo in the coming weeks.

-------------------------

George1 | 2021-05-29 08:40:15 UTC | #39

[quote="elix22, post:38, topic:6674"]
e more clear about the support of .
[/quote]

https://urho3d.io/documentation/1.4/_main_loop.html
The first line describe about headless mode, where I think you can define in engine parameter.

There is also some detail about ExternalWindow, where you can render to. Not sure if it is cross platform.

regards

-------------------------

elix22 | 2021-05-29 09:43:59 UTC | #40

Right.

In Headless mode , the "Graphics" and the "Renderer" subsystems are not registered and not initialized 
So there is no GPU and No OpenGL Context
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Engine/Engine.cpp#L174

Yes , ExternalWindow is supported in Urho.Net  ,you can pass an External window handle via ApplicationOptions.ExternalWindow .
It allows to pass an external window such as WinForms Panel.Handle to be rendered upon.
Eventually it propagates to SDL_CreateWindowFrom()

But  SDL_CreateWindowFrom() doesn't work on all platforms  so currently it's not a good solution .
I intend to investigate and fix/enhance that once .NET MAUI  will support all the relevant platforms including Linux (Linux,Mac,Windows,iOS,Android)

-------------------------

najak3d | 2021-05-29 09:52:14 UTC | #41

Thanks, right, "Headless" is an inaccurate term, but you got my gist.  I'm not wanting to pass it *any* handle.   In our previous project, we made heavy use of OpenGL, and it was *not* bound to a surface.  We just defined the Render Buffer size with parameters, and then at the end of each frame, we blitted the pixels from that Render Buffer to a Bitmap memory location.   Then we rendered the bitmap in a PictureBox.

I'm only asking about this, because if Urho.Net supported it, we could then use this technique to render the Urho output in Xamarin.Forms, via a SkiaSharp.CanvasView.

If we had a way to render Urho.Net to Xamarin.Forms, we could use it (assuming it works on UWP, iOS, and Android).  Right now, we're using UrhoSharp, and feeling considerable pain.

-------------------------

elix22 | 2021-05-29 11:37:50 UTC | #42

So it involves 2  copy operations (seems to me very expensive) 
1 - Copy data from a GPU resource to a RAM buffer
2 - And then copy from RAM buffer to a SkiaSharp.CanvasView .

Are you sure it works on All Android devices ?
Because I think it won't work on some of them 
Specifically step 1 is not supported on all Android devices .

I don't plan to deviate from my current objectives .
I don't promise anything , don't promise to implement it  but you can create an issue in my Github repo and attach a small sample project.

I still think it's not the way to go , the right way would be to pass an external window handle .
But for that I will wait for .NET MAUI

-------------------------

najak3d | 2021-05-29 18:09:08 UTC | #43

@elix22  - We already do this with OpenGL back to Android OS 4.2, to present.   And it's only ONE copy... from GPU to CPU RAM Bitmap Pixel's location.  The RenderBuffer and Bitmap buffer have the same format (equivalent).   On one platform we have to reverse the RGB to BGR to make this work.

So we "Copy Render Buffer to RAM" (which defines the bitmap), then we Invalidate the PictureBox, and it refreshes.   The whole operation takes about 1 msec, and so is acceptable cost (e.g. 60 msec per 1 second... about 6%).   Do do this technique on WinCE, Windows, Android, and iOS.   I think when you "bind to a window surface" the process may be near equivalent to what we're doing already.

Without the ability to render results to a Xamarin.Form, we won't be able to use Urho.Net.   If you only support MAUI, I don't think we'll be able to use that (I assume it won't be backward compatible with Xamarin.Forms).  We are 1.5 years into development right now, using .NS2.0 and Xamarin.Forms.

-------------------------

elix22 | 2021-05-29 19:52:30 UTC | #44

As I mentioned , you can open an issue on My Urho.Net Github Repo and attach a small sample 
That mimics only the operation that you described (using Xamarin.Forms and UrhosSharp)
I am not promising anything , but I will take a look at it and evaluate the effort to implement it .
But even if I will decide to implement it , it will not happen in the next 3 months because of my other tasks

-------------------------

najak3d | 2021-05-29 20:43:17 UTC | #45

The sample is simply this - allow us to "start Urho.Net without giving it an actual Window Surface to bind to."   Allow us to simply set Urho.Net's RenderBuffer Size/Format/etc manually....  and have it simply run the same as if it were bound to a surface, except that it skips the final step of blitting pixels to the surface.  Just give us an event that notifies us that a frame is complete, and we'll do the rest.

If you do this, I'll write the wrapper that makes this work with SkiaCanvas inside Xamarin.Forms (and MAUI) for UWP, Android, WPF, and iOS.    And then I'll release my code MIT style back to your repository, for use by anyone.

I'll open the issue as you requested.

DONE:  
https://github.com/Urho-Net/Urho.Net/issues/5

-------------------------

najak3d | 2021-06-01 21:32:34 UTC | #46

What do you anticipate to be the difficulty level for this request, to allow startup without a visible binding surface?  We are REALLY wanting to switch off of UrhoSharp, given that it's built on a 3 yr-old Urho, and is not buildable by anyone.

We scoured the internet for options of a "code-first" style engine that will work with C# and is cross-platform to UWP/iOS/Android, and there are truly no good options available.  Urho rocks.

-------------------------

elix22 | 2021-06-02 08:54:33 UTC | #47

[quote="najak3d, post:46, topic:6674"]
What do you anticipate to be the difficulty level for this request, to allow startup without a visible binding surface?
[/quote]

Some challenges and unknowns : 
1- Create OpenGL context , with no surface attached
    - Possible on desktop , on mobile remains to be seen , some people are using an hack by creating 1x1 
       pixel size surface.
2- Creating and binding  a FrameBuffer for Offscreen rendering , no issues here should work on all platforms.
3- Reading/copying the Framebuffer (color attachment) to RAM (glReadPixels) , works on desktop , works on iOS and most of the Android devices (not sure if it works on low-end Android devices)


As I mentioned , in the coming months I am working solely on my game projects .
Releasing/open-sourcing what ever I can to the community .
(Admob , Google mobile ads support for iOS and Android is my latest submission , in my Repo )

I will start evaluating this feature only once I am done with my game projects
Please note that  Urho.Net doesn't support UWP yet (which I plan todo)

-------------------------

najak3d | 2021-06-02 17:57:36 UTC | #48

In our current project, we've been doing this method for Android 4.0+, since 2012. We do have to create an "android surface" but it's not bound to anything.

The packages we used were Mono.Android, and OpenTK.

I have attached our two short code files -- the first one is Android-specific, the other is fully multi-platform.

(Attachment OGL.Control.Droid.cs is missing)



(Attachment OGL.Control.cs is missing)

-------------------------

najak3d | 2021-06-02 18:21:02 UTC | #49

Oops, my attachments were rejected, so I am pasting them here. Here is the Android Specific logic to create the EGL context:

using System;
using System.Drawing;
using gpx = OpenTK.Graphics;
using jgl = Javax.Microedition.Khronos.Egl;
using jgl10 = Javax.Microedition.Khronos.Egl.EGL10;
using Java.Interop;

namespace iFly.Vision3D
{
public static partial class OGL
{
private class _Control
{
private OGL.Control _owner;
private jgl.IEGL10 _EGL;
private jgl.EGLDisplay _display;
private jgl.EGLConfig[] _configList;
private jgl.EGLConfig _config;
private jgl.EGLContext _context;
private jgl.EGLSurface _surface;
private System.Threading.Thread _threadOwner;
private bool _isConfigured;
private Size _size = new Size(200, 120);

public _Control(OGL.Control ctrl)
{
_owner = ctrl;
}

public Size Size
{
get { return _size; }
set { _size = value; Configure(_size); }
}

public void MakeCurrent(bool forced)
{
if (!_isConfigured)
return; // too soon

_EGL.EglMakeCurrent(_display, _surface, _surface, _context);
}

public void Configure(Size size)
{
_size = size;
Initialize(null, size);
}

public bool Initialize(iGraphicsMode graphicsMode, Size size)
{
_size = size;

if (_config == null && graphicsMode != null)
{
int[] version = new int[2];

_EGL = jgl.EGLContext.EGL.JavaCast<jgl.IEGL10>();
_display = _EGL.EglGetDisplay(jgl10.EglDefaultDisplay);
_EGL.EglInitialize(_display, version);

const int EGL_CONTEXT_CLIENT_VERSION = 0x3098;
int[] ctxAttr = new int[] { EGL_CONTEXT_CLIENT_VERSION, 2, jgl10.EglNone }; // also try: jgl10.EglVersion

_config = _ChooseConfig(graphicsMode); // Choosing a config is a little more complicated

_context = _EGL.EglCreateContext(_display, _config, jgl10.EglNoContext, ctxAttr);
}

int[] sfcAttr = new int[] { jgl10.EglWidth, _size.Width, jgl10.EglHeight, _size.Height, jgl10.EglNone };

_surface = _EGL.EglCreatePbufferSurface(_display, _config, sfcAttr);

_isConfigured = true;

MakeCurrent(true);

Log.Info("OGL.Control.Initialize() - complete: {0}, {1}, {2}, {3}", _size, _config, _surface, _display);
return true;
}

private jgl.EGLConfig _ChooseConfig(iGraphicsMode graphicsMode)
{
const int EGL_OPENGL_ES2_BIT = 4;
const int EGL_PBUFFER_BIT = 1;

int[] attribList = new int[] {
jgl10.EglRenderableType, EGL_OPENGL_ES2_BIT,
jgl10.EglSurfaceType, EGL_PBUFFER_BIT,
jgl10.EglDepthSize, graphicsMode.Depth,
jgl10.EglStencilSize, graphicsMode.Stencil,
jgl10.EglRedSize, graphicsMode.ColorFormat.Red,
jgl10.EglGreenSize, graphicsMode.ColorFormat.Green,
jgl10.EglBlueSize, graphicsMode.ColorFormat.Blue,
jgl10.EglAlphaSize, graphicsMode.ColorFormat.Alpha,
jgl10.EglSamples, graphicsMode.Samples,
jgl10.EglNone
};

// No error checking performed, minimum required code to elucidate logic
// Expand on this logic to be more selective in choosing a configuration
int[] numConfig = new int[1];
_EGL.EglChooseConfig(_display, attribList, null, 0, numConfig);
int configSize = numConfig[0];

_configList = new jgl.EGLConfig[configSize];
_EGL.EglChooseConfig(_display, attribList, _configList, configSize, numConfig);

return _configList[0]; // _configList.Length - 1]; // Best match is often the first one.
}

}

}

}

-------------------------

elix22 | 2021-06-06 15:29:27 UTC | #50

New demo sample ...
Urho.Net Nakama client-server showcase .

Nakama is a realtime fully open-source commercial game server  developed by Heroic Labs. 
The server supports all the features that are expected from a commercial social and realtime game server.

This demo showcases KinematicCharacters running in realtime mode on multiple devices (connected to the same Nakama server)
This demo runs on all Urho.Net supported platforms (Windows,MacOS,Linux,iOS,Android)

More information on Nakama and the demo can be found in the link below.

https://github.com/Urho-Net/Samples/tree/main/NakamaNetworking

-------------------------

dertom | 2021-06-07 20:13:50 UTC | #51

Cool :+1: 
Amazing work you constantly doing :+1: 
Btw, what if I e.g. would want to add some custom cpp-subsystem and expose its methods to dotnet. Is that possible for someone!=you already?
I had a look in your dotnet-branch and tried to convert the steps of script/make_csharp_bindings.sh to work on linux. 
1) The clang-step
```
  ${CUSTOM_CLANG} -cc1 -stdlib=libc++ -std=c++0x -emit-pch -DURHO3D_OPENGL -o DotNet/Bindings/Urho.pch DotNet/Bindings/Native/all-urho.cpp  -Ibuild-xcode/include -Ibuild-xcode/include/Urho3D/ThirdParty -Ibuild-xcode/include/Urho3D/ThirdParty/Bullet
```
Didn't work. (Was using clang11 instead of you having clang3 for osx,...might this be the problem?)
My error:
```
DotNet/Bindings/Native/all-urho.cpp:1:10: fatal error: 'stdint.h' file not found
#include <stdint.h>
```



I could build SharpieBinder,though. But running it results in this error ;)
```
Unhandled Exception:
System.Exception: Unable to load libclang-mono ---> System.DllNotFoundException: clang-mono assembly:<unknown assembly> type:<unknown type> member:(null)
  at (wrapper managed-to-native) Clang.InternalCallRegistrar.libclang_mono_register_icalls()
  at Clang.InternalCallRegistrar.EnsureRegistered () [0x0000d] in <a4fb0aa1b6164896bc1de773790576f6>:0 
   --- End of inner exception stack trace ---
  at Clang.InternalCallRegistrar.EnsureRegistered () [0x0003a] in <a4fb0aa1b6164896bc1de773790576f6>:0 
  at Clang.Ast.AstReader..ctor () [0x00006] in <a4fb0aa1b6164896bc1de773790576f6>:0 
  at SharpieBinder.MainClass.Main (System.String[] args) [0x00068] in <262143e0ecba429bbb052fbdd3aec89e>:0 
[ERROR] FATAL UNHANDLED EXCEPTION: System.Exception: Unable to load libclang-mono ---> System.DllNotFoundException: clang-mono assembly:<unknown assembly> type:<unknown type> member:(null)
  at (wrapper managed-to-native) Clang.InternalCallRegistrar.libclang_mono_register_icalls()
  at Clang.InternalCallRegistrar.EnsureRegistered () [0x0000d] in <a4fb0aa1b6164896bc1de773790576f6>:0 
   --- End of inner exception stack trace ---
  at Clang.InternalCallRegistrar.EnsureRegistered () [0x0003a] in <a4fb0aa1b6164896bc1de773790576f6>:0 
  at Clang.Ast.AstReader..ctor () [0x00006] in <a4fb0aa1b6164896bc1de773790576f6>:0 
  at SharpieBinder.MainClass.Main (System.String[] args) [0x00068] in <262143e0ecba429bbb052fbdd3aec89e>:0 
```
(...ah ok,...this is because I need libclang-mono.so for linux...??)

Well,...after that I stopped... ;) And in the end I have to admit that I'm a bit lost there. :D

Then I tried just compiling cmake_linux_dotnet_so.sh. That ended with an link error to mono...
```
mono_support.cpp:(.text._Z25urho3d_mono_load_assemblyPN6Urho3D7ContextERKNS_6StringEbP17_MonoAssemblyName+0xe5): undefined reference to `mono_image_open_from_data_with_name'
/usr/bin/ld: mono_support.cpp:(.text._Z25urho3d_mono_load_assemblyPN6Urho3D7ContextERKNS_6StringEbP17_MonoAssemblyName+0x10a): undefined reference to `mono_image_get_table_info'
/usr/bin/ld: mono_support.cpp:(.text._Z25urho3d_mono_load_assemblyPN6Urho3D7ContextERKNS_6StringEbP17_MonoAssemblyName+0x115): undefined reference to `mono_table_info_get_rows'
/usr/bin/ld: mono_support.cpp:(.text._Z25urho3d_mono_load_assemblyPN6Urho3D7ContextERKNS_6StringEbP17_MonoAssemblyName+0x131): undefined reference to `mono_metadata_decode_row'
/usr/bin/ld: mono_support.cpp:(.text._Z25urho3d_mono_load_assemblyPN6Urho3D7ContextERKNS_6StringEbP17_MonoAssemblyName+0x14f): undefined reference to `mono_assembly_name_get_version'
/usr/bin/ld: mono_support.cpp:(.text._Z25urho3d_mono_load_assemblyPN6Urho3D7ContextERKNS_6StringEbP17_MonoAssemblyName+0x17a): undefined reference to `mono_image_close'
/usr/bin/ld: mono_support.cpp:(.text._Z25urho3d_mono_load_assemblyPN6Urho3D7ContextERKNS_6StringEbP17_MonoAssemblyName+0x266): undefined reference to `mono_assembly_load_from_full'
/usr/bin/ld: mono_support.cpp:(.text._Z25urho3d_mono_load_assemblyPN6Urho3D7ContextERKNS_6StringEbP17_MonoAssemblyName+0x271): undefined reference to `mono_image_close'
/usr/bin/ld: CMakeFiles/MonoEmbedded.dir/mono_support.cpp.o: in function `urho3d_mono_assembly_preload(_MonoAssemblyName*, char**, void*, bool)':
`

```


This is nothing urgent and I know you are working on your game, so keep doing that. (good luck with that :+1: )
But it would be epic to know that someday in the future there are some instructions about how to customize urho.net (if it works at all) Till then keep on rocking

-------------------------

elix22 | 2021-06-08 08:09:15 UTC | #52

Thanks for the kind words :slight_smile: 

As you know SharpieBinder was written by the Xamarin guys
It is not perfect , has some hacks , I am learning how to use and modify it as I go.
I think in theory it should be possible to make it work on Linux (and Windows) but it requires some effort
Currently I don't have the time resources to investigate that.
I wrote **script/make_csharp_bindings.sh**  only using MacOS in mind.
So unfortunately for now it will work only on MacOS.
Some day if I have more time I will try make it work also on other platforms 

SharpieBinder dependent on clang version 3.7
https://github.com/xamarin/urho/blob/master/Makefile#L3


Regarding the linking failure in Linux 
**cmake_linux_dotnet_so.sh** should work , you are probably missing the Mono installation.
See https://www.mono-project.com/download/stable/#download-lin

In any case you can always add bindings manually ,  I don't think it's the right way for large subsystems.
See example :https://github.com/elix22/Urho3D/commit/b4246eb54569419917c7911c5baa2b7821b7f6cd

-------------------------

elix22 | 2021-06-08 09:43:14 UTC | #53

**cmake_linux_dotnet_so.sh** should work without Mono installation.
For some reason you compile one of the Mono samples in the sample folder 
But in **cmake_linux_dotnet_so.sh** , **-DURHO3D_SAMPLES=0**
I can't reproduce it on my Linux machine

-------------------------

dertom | 2021-06-08 10:31:57 UTC | #54

Yes, I guess I could make it compile with the URHO3D_DOTNET-Option deactivated(but of course I want it to be active, as this is the whole point about do it in the first place ;) )...I have already samples deactivated, but cmake will compile it anyway.:
```
if (URHO3D_SAMPLES)
    file (GLOB_RECURSE DIRS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} CMakeLists.txt)
    list (SORT DIRS)
    foreach (DIR ${DIRS})
        get_filename_component (DIR ${DIR} PATH)
        if (DIR)
            add_sample_subdirectory (${DIR})
        endif ()
    endforeach ()
else()
    if (URHO3D_DOTNET)
        add_sample_subdirectory (${CMAKE_CURRENT_SOURCE_DIR}/71_MonoEmbed)
    endif ()
endif ()
```
Which is fine.... I also found out why it didn't link. Btw, I have mono installed.

I added this to MonoEmbed's CMakeLists.txt 
```
if(UNIX)
set (LIBS
     libmonosgen-2.0.so
     libmono-native.so
     libmono-btls-shared.so
     libMonoPosixHelper.so
)
endif()
```
Now it compiles and links... :+1:  (was just about to create a pull-request but so it is even easier ;) )
I copied the new libUrho3D.so and DotNet/UrhoDotNet/desktop/UrhoDotNet.dll in the bin-folder and it actually starts urho3d... ...but there is a problem with a method that is not found:

```
Unhandled Exception:
System.MissingMethodException: Method not found: void Urho.Network.Network.add_NetworkMessage(System.Action`1<Urho.Network.NetworkMessageEventArgs>)
  at Chat.Chat.Start () [0x00019] in <6620b2dd3c914aaf85eb698c592ecb21>:0 
  at Urho.Application.ProxyStart (System.IntPtr h) [0x0001f] in <f4623b0d1bad4cf89bbac757c7876271>:0 
  at (wrapper native-to-managed) Urho.Application.ProxyStart(intptr)
  at (wrapper managed-to-native) Urho.Application.Application_Run(intptr)
  at Urho.Application.Run () [0x00000] in <f4623b0d1bad4cf89bbac757c7876271>:0 
  at Chat.Program.Main (System.String[] args) [0x00005] in <6620b2dd3c914aaf85eb698c592ecb21>:0 
[ERROR] FATAL UNHANDLED EXCEPTION: System.MissingMethodException: Method not found: void Urho.Network.Network.add_NetworkMessage(System.Action`1<Urho.Network.NetworkMessageEventArgs>)
```

I'm not sure how to read this error. My first guess was that UrhoDotNet.dll is not in sync with the .so, since I just used the one that is present in the DotNet-Folder and didn't create it on my own with the compiled version.
This line:
```
[ERROR] FATAL UNHANDLED EXCEPTION: System.MissingMethodException: Method not found: void Urho.Network.Network.add_NetworkMessage(System.Action`1<Urho.Network.NetworkMessageEventArgs>)
```
Actually seems to indicate that the problem is in the shared-lib (libUrho3D.so) not having this method.... ...and it is right. There is no AddNetworkMessage(...) method in Urho3D/Network/Network.h 

(ps: Apart from that I guess the used Game.dll is not the one that is intended as 'Hello World'-Embedded-C# as it seems to be the Chat-sample. Maybe also something that went wrong with me not doing the full build).

Greets :+1:

-------------------------

elix22 | 2021-06-08 11:14:59 UTC | #55

Sorry about that but 71_MonoEmbed is not supposed to be part of **cmake_linux_dotnet_so.sh**
It is only related to Android and iOS , not related to desktop platforms.
I fixed it in my repo , check it out.

Regarding UrhoDotNet.dll  not in sync with libUrho3D.so , I will check it and provide some feedback.
You can build  UrhoDotNet.dll  in Linux  using **../DotNet/Bindings/build-desktop-bindings.sh**

-------------------------

elix22 | 2021-06-08 11:21:55 UTC | #56

To make it work 
You have to put the new UrhoDotNet.dll into :
`.../Urho.Net/template/libs/dotnet/urho/desktop/UrhoDotNet.dll`

And libUrho3D.so into  :
`.../Urho.Net/template/libs/linux/libUrho3D.so`

-------------------------

dertom | 2021-06-08 14:55:23 UTC | #57

Ok, thx for the info.
Just for info.
I actually downloaded a clang 3.7-version for linux ( https://releases.llvm.org/3.7.0/clang+llvm-3.7.0-x86_64-linux-gnu-ubuntu-14.04.tar.xz )
And used this to create the Urho.pch-file. I had to add a couple of standard-includes like this:
```
${CUSTOM_CLANG} -cc1 -stdlib=libc++ -std=c++0x -emit-pch -DURHO3D_OPENGL -o DotNet/Bindings/Urho.pch DotNet/Bindings/Native/all-urho.cpp  -Ibuild-xcode/include -Ibuild-xcode/include/Urho3D/ThirdParty -Ibuild-xcode/include/Urho3D/ThirdParty/Bullet -I/home/ttrocha/_dev/ALWAYSDEL/clang/clang+llvm-3.7.0-x86_64-linux-gnu-ubuntu-14.04/lib/clang/3.7.0/include -I/home/ttrocha/_dev/ALWAYSDEL/clang/clang+llvm-3.7.0-x86_64-linux-gnu-ubuntu-14.04/include/c++/v1 -I/usr/include
```

But at least I got this step. As you mentioned SharpieBinder is osx only since they rely on that osx-only clang-library. Maybe someday we could replace this with ClangSharp( https://github.com/microsoft/ClangSharp ). Not sure if that actually can do the same ;)

I guess I will have a look at using the manual binding as you linked (when I have some time). Looks easy enough...
Thx, so far.

-------------------------

dertom | 2021-09-26 07:54:45 UTC | #58

Ok,...thx again for the info. With your hints it was actually straight forward to include custom cpp UrhoObjects into Urho.net. Once you know where to put what.

I wonder, is the macos-only part 'only' for generating the cs-files 'Bindings/Portable/Generated' and its corresponding 'binding.cpp'?

Greets

-------------------------

elix22 | 2021-09-26 09:17:21 UTC | #59

[quote="dertom, post:58, topic:6674"]
I wonder, is the macos-only part ‘only’ for generating the cs-files ‘Bindings/Portable/Generated’ and its corresponding ‘binding.cpp’?
[/quote]

Yes , you are absolutely right the folders/files that you mentioned are the only part that is unique to macOS and currently can only be generated on Mac. .

This is the script  that  I use on Mac to generate all the stuff related to Mac, iOS and Android

https://github.com/elix22/Urho3D/blob/dotnet/script/build_install_dotnet_macos.sh

> script/make_csharp_bindings.sh

Generates the bindings as you mentioned above.
Also Generates DotNet assemblies **UrhoDotNet.dll** for desktop and mobile and **Mono.Android.dll** , but this part can be done also on Linux and Windows

> script/build_xcode_dotnet_dylib.sh

Generates  native library **libUrho3D.dylib** for mac  , can be done only on Mac

> script/build_ios_dotnet_libs.sh

Generates native libraries **libUrho3D-GLES.a**  and **libUrho3D-Metal.a**  for IOS
Can be done only on Mac.

> script/build_android_dotnet_libs.sh

Generates native libraries **libUrho3D.so** and **libMonoEmbedded.so** (glue Urho<->Mono-runtime) for Android (arm64-v8a,armeabi-v7a,x86,x86_64) , can be done on all desktop platforms

> script/build_vs2019_dotnet_dll.bat

Generates  native library **Urho3D.dll** for Windows , can be done only on Windows

> for Linux you will have to do it manually (I guess I was too lazy to write an automated script :) )
> ./script/cmake_linux_dotnet_so.sh  build
> cd build 
> make -j4
> copy  libUrho3D.so to ${URHONET_HOME_ROOT}/template/libs/linux

> script/copy_urhonet_libs.sh

Copies all the generated dotnet assemblies and libraries to Urho.Net installation folder

-------------------------

dertom | 2021-10-18 12:40:59 UTC | #60

Hola,...I have a question about 'publishing' a game. Yesterday I attended a small 3h-gamejam and used urho.net. In vsc you have a task 'publish' which will create '[game]\bin\Debug\netcoreapp3.1\publish' 
In this publish folder there are no CoreData / Data folders but in the one one level above. 
So what folder to use the content of "publish"-folder with CoreData/Data manually added or ignore publish and use the one one level above?
I used later and it works as intended on my computer.
But actually the first guy to comment said he cannot start the game at all.

Are there any prerequisites? Do they need a special version of dotnet installed or such?
Actually I'm the only one without web-version. I wonder if web-deployment would be technically(!) possible or are there any limitations that make it impossible (e.g. on the mono-side). (and I'm not asking if or when you will implement it) 

I personally love urho.net. It is a really smooth development-experience 👍

EDIT:
This seems to be the error:
```
A fatal error occurred. The required library hostfxr.dll could not be found.
If this is a self-contained application, that library should exist in [C:\Users\Stephan\Desktop\trijam141-dertom-win].
If this is a framework-dependent application, install the runtime in the global location [C:\Program Files\dotnet] or use the DOTNET_ROOT environment variable to specify the runtime location or register the runtime location in [HKLM\SOFTWARE\dotnet\Setup\InstalledVersions\x64\InstallLocation].

The .NET Core runtime can be found at:
  - https://aka.ms/dotnet-core-applaunch?missing_runtime=true&arch=x64&rid=win10-x64
```
Does this mean dotnet-core needs to be installed? Or did I publish the wrong way?

EDIT2: I used now this command to publish with lots of extra (dotnet-core) dlls:
```
dotnet publish --configuration Release -r win-x64
```

Edit3: upper works for some and for one other(The navmesh-error is not the problem...at least I have this as well without the graphical glitch):
https://img.itch.zone/aW1nLzcyMjk0NzQucG5n/original/%2F7eh4T.png

Edit4: Whoever wants to test: https://dertom1895.itch.io/trijam141-gate-to-another-world

-------------------------

elix22 | 2021-10-18 15:27:54 UTC | #61

Very Cool dude :slight_smile: 
I would suggest to create a new thread for your work , so the focus would be on your game on not on Urho.Net.
I didn't pay much attention to dotnet deploy , so for now you will have to copy manually Data , CoreData and Urho3D.dll to the deploy folder.
To my understanding , according to Microsoft Dotnet runtime should be installed on the host machine inorder to run dotnet applications.

See 
https://docs.microsoft.com/en-us/dotnet/core/deploying/deploy-with-cli#self-contained-deployment

-------------------------

elix22 | 2021-10-18 15:38:05 UTC | #62

[quote="dertom, post:60, topic:6674"]
Are there any prerequisites? Do they need a special version of dotnet installed or such?
Actually I’m the only one without web-version. I wonder if web-deployment would be technically(!) possible or are there any limitations that make it impossible (e.g. on the mono-side). (and I’m not asking if or when you will implement it)
[/quote]

It's possible in theory (Emscripten) , but  currently it's not supported out of the box   

One comment regarding your game , I would use the following option **ResizableWindow = true** in **ApplicationOptions**  so the game will fit the entire screen 
Just my 2 cents

-------------------------

elix22 | 2021-10-19 06:43:53 UTC | #63

[quote="dertom, post:60, topic:6674"]
Edit3: upper works for some and for one other(The navmesh-error is not the problem…at least I have this as well without the graphical glitch):
[/quote]

I noticed that one player complained about the graphical glitch .
Did she provide you any logs ?
My guess it's a drivers issue installed on her Windows , but some logs would be helpful in figuring out the root cause.

-------------------------

elix22 | 2021-10-20 07:15:54 UTC | #64

OK 
I played/experimented  with **dotnet deploy**
I used the following **dotnet publish** command on my Mac (fully optimized AOT compiled binary)
```
dotnet publish -c Release -r osx-x64 --self-contained true -p:PublishReadyToRun=true -p:PublishReadyToRunShowWarnings=true -p:PublishSingleFile=true -p:PublishTrimmed=true
```
Some insights

* I noticed that if I deploy it as 1 file self contained executable , double clicking the executable will fail to start the application , it can't find Urho library and assets .
 RootCause , for some reason the working directory is set to the home user directory and not the executable directory , I think it's a wrong behavior (I guess Microsoft thinks differently :) )

A workaround would be to set the working directory to the executable directory path prior of starting the Urho Application .

I verified it on my Mac and it seems to work (relevant only for Desktop , not for mobile) .

**Example** 
```
namespace TestProject
{
    class Program
    {
        static void Main(string[] args)
        {
            var applicationPath = System.IO.Path.GetDirectoryName(System.Diagnostics.Process.GetCurrentProcess().MainModule.FileName);
            System.IO.Directory.SetCurrentDirectory(applicationPath);

            new TestProject().Run();
        }
    }
}
```

* I mentioned in previous thread that according to Microsoft , dotnet runtime should be installed on the host machine in order to run dotnet applications , I think it's a wrong statement.
 A Self contained binary contains all the stuff to run the app on the host machine.

* I fixed the **dontet publish**  use case on the Urho.Net side , now it copies Assets and Urho  library to the publish folder

-------------------------

dertom | 2021-10-20 08:27:44 UTC | #65

Cool,...thx a lot :+1:

-------------------------

elix22 | 2021-10-21 09:24:39 UTC | #66

I went a little bit further .
Added **cross-platform** publish support for Window,Mac and Linux
You can now generate Binaries from **any**  desktop platform to **any**  desktop platform
Added 3 new tasks 
**publish-windows**
**publish-linux**
**publish-mac**

You can generate binaries  **from** `Windows,Mac,Linux` **for** `Windows,Mac,Linux`
The generated binaries are single file self contained 64 bit executables.

-------------------------

dertom | 2021-10-21 10:10:25 UTC | #67

Cool! I already wondered if that is possible as this '-r' options seemed to be not only for the host-os.

-------------------------

dertom | 2021-10-21 18:41:33 UTC | #68

I tested this now. It packs everything but the native library could not be found. At least not on linux:
```
Unhandled exception. System.DllNotFoundException: Unable to load shared library 'Urho3D' or one of its
dependencies. In order to help diagnose loading problems, consider setting the LD_DEBUG 
environment variable: libUrho3D: cannot open shared object file: No such file or directory
```

Btw, setting the directory in Program.cs seems not to be necessary as 'System.IO.Directory.GetCurrentDirectory()' has already the value that is set in the #if-block.

Everything starts to work, if removing the 'PublishSingleFile'.property. But actually this is what makes it so nice, right ;). 

One workaround could be to pack an start.sh like tha (which is good enough for me)t:
```
#/bin/bash

export LD_LIBRARY_PATH=$PWD
./Game
```

Not tested windows, yet.

-------------------------

elix22 | 2021-10-21 18:51:46 UTC | #69

Strange :roll_eyes:
I actually verified it on Linux , worked for me .
Did you try on the latest commit (from today ) ?

The motivation is to use PublishSingleFile  , however at least in my case 
**System.IO.Directory.GetCurrentDirectory()’** returns my home directory and not the binary directory , My workaround is supposed to solve this issue .

I also update the FeatureSamples today , can you please try that on your Linux machine

Thanks

-------------------------

elix22 | 2021-10-21 19:17:34 UTC | #70

[quote="dertom, post:68, topic:6674"]
Btw, setting the directory in Program.cs seems not to be necessary as ‘System.IO.Directory.GetCurrentDirectory()’ has already the value that is set in the #if-block.
[/quote]

You are right , on Linux it returns the same  and it's not needed  however on a Mac it's needed  (that's my main development/debug platform) and I guess also on Windows it's needed.

So  I guess that in your case it actually can't find libUrho3D which resides in the same folder as the executable, for some reason I can't reproduce it on my Linux machine.

Your start.sh is actually a good solution .

-------------------------

dertom | 2021-10-21 20:32:44 UTC | #71

[quote="elix22, post:69, topic:6674"]
actually verified it on Linux , worked for me .
Did you try on the latest commit (from today ) ?
[/quote]

Yes. Checked out just some hours ago. I'm on ubuntu 20.04.  Hmm,...maybe you have an something like this set already: 
```
LD_LIBRARY_PATH=. 
```
My LD_LIBRARY_PATH is not set at all which I guess is the default!?

-------------------------

elix22 | 2021-10-21 20:56:44 UTC | #72

(base) eli@eli-Lenovo-Y50-70:~/Development/Samples/FeatureSamples/bin/Release/netcoreapp3.1/linux-x64/publish$ ls
CoreData  Data  Game  libUrho3D.so  Urho3D.log
(base) eli@eli-Lenovo-Y50-70:~/Development/Samples/FeatureSamples/bin/Release/netcoreapp3.1/linux-x64/publish$ uname -a 
Linux eli-Lenovo-Y50-70 5.8.0-55-generic #62~20.04.1-Ubuntu SMP Wed Jun 2 08:55:04 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
(base) eli@eli-Lenovo-Y50-70:~/Development/Samples/FeatureSamples/bin/Release/netcoreapp3.1/linux-x64/publish$ echo ${LD_LIBRARY_PATH}
/home/eli/Development/torch/install/lib:/home/eli/Development/torch/install/lib:

-------------------------

dertom | 2021-10-21 21:21:06 UTC | #73

libUrho3D.so is not by chance also in one of those folders:

[quote="elix22, post:72, topic:6674"]
/home/eli/Development/torch/install/lib:/home/eli/Development/torch/install/lib:
[/quote]

Beside that,...don't know. Don't put too much effort into that. I'm totally fine with the shell-script startet. For some reason my 'explorer' can't run Game because it thinks its a shared library!? ...and I do have to write a shell script no matter what. (Not sure this is a local problem!?)

-------------------------

elix22 | 2021-10-22 19:09:28 UTC | #74

[quote="dertom, post:68, topic:6674"]
Btw, setting the directory in Program.cs seems not to be necessary as ‘System.IO.Directory.GetCurrentDirectory()’ has already the value that is set in the #if-block.
[/quote]

It seems it's not necessary also for Window , only relevant to Mac  .
I will keep it anyway for all 3 platforms as a precaution .

Another trick , relevant only for Windows (will cause exception on Linux or Mac) 
is in case one wants to hide the console .

To be added in Program.cs
```
        [DllImport("kernel32.dll")]
        static extern IntPtr GetConsoleWindow();

        [DllImport("user32.dll")]
        static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);



        static void Main(string[] args)
        {
 
#if _DESKTOP_PUBLISHED_BINARY_
            var handle = GetConsoleWindow();

            // Hide console
            ShowWindow(handle, 0);

            var applicationPath = System.IO.Path.GetDirectoryName(System.Diagnostics.Process.GetCurrentProcess().MainModule.FileName);
            System.IO.Directory.SetCurrentDirectory(applicationPath);
#endif          
            new TestApp().Run();
        }
```

-------------------------

elix22 | 2021-11-14 15:26:52 UTC | #75

First test run on the Browser .
This was tough , I didn't anticipate the complexity of Web support ,specifically generating the bindings for  native<->managed interactions (for Web).
At least I know now that it's definitely feasible but it will take some time till feature complete . 

https://elix22.itch.io/urhonet-test-sample

-------------------------

dertom | 2021-11-14 19:49:10 UTC | #76

Cool. Thx for working on that 👍👍👍

-------------------------

elix22 | 2021-11-17 09:20:15 UTC | #77

Second test run on the browser .
This one is more advanced ,  works like a charm on desktop and mobile browsers

https://elix22.itch.io/samply-game

-------------------------

bayganik | 2021-11-19 17:08:05 UTC | #78

I've created a C# example using Urho.Net .  I would like to thank you guys for keeping this engine alive.  Although the lack of documentation is a hurdle to cross BUT I am determined to promote it by creating more examples :-) 

(https://github.com/bayganik/Urho.Net_CardGame_Example)

-------------------------

elix22 | 2021-11-19 19:10:11 UTC | #79

Very cool :slightly_smiling_face:
I am glad that people are using it and most importantly having fun in making games  .

[quote="bayganik, post:78, topic:6674"]
Although the lack of documentation is a hurdle
[/quote]

Yes this is an Achilles' heel , something that will have to improve in the future .
I had a plan to take the UrhoSharp documentation and to extend it , but Microsoft removed the documentation link , I can't find it anymore .

In any case the Urho3D vanilla  documentation applies also to Urho.Net (by the end of the the day it's a C# wrapper to Urho3D such as Lua and Angelscript )  .
There are some extra  features that were added by Xamarin in UrhoSharp  (and by me in Urho.Net) that  will have to be addressed with some  more documentation .

-------------------------

elix22 | 2021-11-26 21:25:38 UTC | #80

Third test run on the Browser 
Runs both on desktop and mobile browsers (joystick shown on mobile browsers , sorry for its size)
I find it absolutely mind blowing that it runs 60 FPS on the browser of my  mid-range Android mobile device

https://elix22.itch.io/urhonet-feature-samples

-------------------------

elix22 | 2021-11-27 10:48:01 UTC | #81

Web support is now part of my [main](https://github.com/Urho-Net/Urho.Net) branch.

  - Building for Web is done via Visual Studio Code editor
  - To build the application for web deployment 
    - Press Ctrl+P (Cmd+P on Mac)
    - Choose Tasks: Run Task
    - Choose web-build
    - The build will generate **Web** folder in the project directory
    - The **Web** folder contains everything that is needed for web deployment.
    - You can test it on your local browser with the [Live Server extention](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
  - Although it already mostly supported , web support is still in the development phase , you may submit any issues found with a detailed description of the issue and  Browser Console logs.

-------------------------

elix22 | 2021-11-27 20:06:52 UTC | #82

I fixed an annoying bug related to the Chrome Browser , keyboard was not responding on the first upload of the page

-------------------------

elix22 | 2021-12-02 15:11:08 UTC | #83

Another game demo running flawlessly on all supported platforms.

Web browser link https://elix22.itch.io/shape-blaster
 
YouTube link , running on my iPhone ( disregard my poor game play)

https://www.youtube.com/watch?v=q-sU-5j-7uk


Source code link
https://github.com/Urho-Net/Samples/tree/main/ShapeBlaster

-------------------------

elix22 | 2021-12-04 19:46:54 UTC | #84

Added a cute little demo Racer2D
Needles to say all samples run on all browsers , desktop and mobile devices .
Source code available in the Samples repository. 

https://elix22.itch.io/urhonet-feature-samples

-------------------------

