najak3d | 2020-12-04 18:52:42 UTC | #1

We have a commercial map application that is being ported from WinForms to XamarinForms and .NET Standard 2.0.    We have also elected to use UrhoSharp as our rendering engine, and it's working out very well so far.

But there are a few bugs in the UrhoSharp.Forms code, as follows:

1. When you navigate to a new Page, it disposes/stops the Urho Application.   So when you come back to the page that hosts Urho, we have to re-start Urho App from scratch!.... this causes lag, and thrashes memory.

2. Touch Input is skewed on any view of Urho where it doesn't consume the full window / screen.  So the touch input position calculations need a bug fix.

3. It might be nice to build against the latest release of Urho3D.  The current package is compiled against Urho3D from mid-2018.

====
Our current big issue is that we can't get UrhoSharp to build!   Our company is a C#-shop, and not great with C++, and the UrhoSharp project is a mix of both.   It binds C#/.NET to the C++ Urho3d.dll.

If anyone can get this to build, and walk me through the steps of getting it to build, then we'll update the public build instructions, and we'll pay you for this job.

We're hoping someone can do this for $300 USD, our current budget.

-------------------------

JSandusky | 2020-12-06 05:31:50 UTC | #3

Use fragment navigation overlays? Render nothing on full overlay.

(In Android terms) It sounds like you're trying to navigate between Activities and keep GL intact ... AFAIK you can't do that, your GL context can be dumped at any moment on mobile for activity switches, app switches, power switches, etc.

-------------------------

najak3d | 2020-12-06 07:24:45 UTC | #4

Thanks for the tip JSandusky.  I think it's just an oversight in how they wrapped this for XamarinForms.  The rest of our app remains intact, and doesn't dispose.   The C# context that hosts Urho sharp remains fully intact - -it's just that the Navigate operation itself makes a purposed decision to call "StopApplication" on the Urho App when you navigate to a new page.  Everything else about the previous page is still the *same instance* -- nothing is disposed..   Only Urho.   So appears to be a bug in how Urho was integrated into Xamarin forms.

But perhaps you are right, and there is some underlying unavoidable reason for us to dispose of Urho3D.   I'll see if I can ask the question to Egorbo who was the author of this wrapper.

-------------------------

extobias | 2020-12-06 13:24:37 UTC | #5

Does anybody already has taken the job? I've sent you a PM

-------------------------

najak3d | 2020-12-09 01:22:58 UTC | #6

BTW, so far, looks like extobias is going to be able to service this request.  So far, his progress is looking good.

If we have success, then we may be able to revive UrhoSharp, which basically just means we can update it to the latest Urho3D revisions, and fix some bugs, as they arise.

-------------------------

archwind | 2020-12-22 00:17:37 UTC | #7

It is nice to see someone has revived it. I remember back in May I did a lot of restructure to the math library by adding a number of function that were in Axiom so I didn't have to convert the math in the Urho version of the Multiverse engine. I also included using the GPU for math function with System.Numerics instead of CPU.

One of the biggest issues I had was the lack of direct control of starting the render system and how UrhoSharp seems to only work for games made with it. Trying to use it as a engine just doesn't seem possible.

I still can't find a function in the C++ Urho were one can independently control the engine startup without kicking in the game mode so I went back to the old Axiom and put it on GitHub as is. I think I may just go ahead and use SharpDX and modify the existing code. I would use the latest Axiom but the code has a lot of broken features.

-------------------------

najak3d | 2020-12-22 03:51:15 UTC | #8

Wow, Axiom goes way back.  That's where I got my start, around 2003.  It's what propelled me into the world of C# 3D game engines.   I co-founded Visual3D, which built off of Axiom originally (from leedgitar), and then developed up into a gargantuan house-of-cards, that grew too fast, and became unwieldy.  Then Unity3D ate-our-lunch, and we closed our doors, and I turned to making money by programming Unity3D apps for the US army.   I dislike Unity though.

We're currently using UrhoSharp with our 2.5D GPS moving map application with loads of dynamic data being rendered, along with a 3D ground view.

Egorbo, has returned to the scene, to attempt a better hand-off of UrhoSharp, so that we can maintain it, as needed.  However, it might end up being RbfxSharp -- the verdict is still out.

-------------------------

