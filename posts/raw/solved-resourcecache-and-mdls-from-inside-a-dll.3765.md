godan | 2017-11-22 12:54:17 UTC | #1

So, I am having trouble with the ResourceCache when it is access from inside a DLL. My setup is this:

I have an app, MyApp.exe, which links to Urho3D.dll (on Win64). I also have MyLib.dll, which is dynamically loaded at runtime. MyLib.dll is linked to Urho3D and contains various utility functions/components.

When I try code like:

`Texture* tex = rc->GetResource<Texture>("Textures/TestHeightField.png");`

I will always get a null reference, or a message saying that the resource could not be loaded (yes I have check all the paths).
Also, when I write stuff like:

`Model* mdl = new Model(context);`
`mdl->LoadFile("path/to/Box.mdl");`

My app crashes completely. [In this post](https://discourse.urho3d.io/t/solved-resourcecache-dont-working-in-dll/2043), the suggestion was to make sure the lib options are the same. I have verified that. Is there a specific reference in the code to where those defines make a difference? Is it simply a case of inserting `#define URHO3D_OPENGL` and `#define URH3D_SSE` (or whatever the right options are) somewhere in MyApp?

-------------------------

Victor | 2017-11-21 05:17:50 UTC | #2

What you've described seems very familiar to something I've tried, but with no luck. My current setup uses a statically linked Urho3D lib with my game dll file.

Urho3D.lib
Game.dll (links urho3d lib)
GameLauncher.exe (links game.dll)

You just have to make sure to create the Context/Application object within the Game.dll, otherwise (at least from my experience), you run into issues like the one you've described. I've seen where the Context, if created from the .exe (in my case), would be null or corrupt when passed and used throughout the dll.

Not sure if this relates to your issues, but I thought I'd share this experience so that perhaps it can give you some clues on solving your issues.

-------------------------

godan | 2017-11-21 17:21:12 UTC | #3

Thanks for the tip. Unfortunately, I'm still getting null resources....Strangely, this code will return the correct file:

`			SharedPtr<File> f = rc->GetFile("Models/Box.mdl");`

but

`Model* mdl = rc->GetResource<Model>("Models/Box.mdl");`

returns null....

-------------------------

Eugene | 2017-11-21 18:51:04 UTC | #4

Could you debug it? `ResourceCache::GetResource` doesn't look very complicated.

-------------------------

godan | 2017-11-21 19:53:36 UTC | #5

OK, so debugging dlls at runtime is not fun. BUT, it looks like the problem is here:

    if (!Thread::IsMainThread())
    {
        URHO3D_LOGERROR("Attempted to get resource " + name + " from outside the main thread");
        return 0;
    }

That is, when calling the ResourceCache from inside the DLL, this check fails. Is this a bug? Or do DLLs get their own thread?

This explains a lot, actually!

Not sure how to fix it, though.... any suggestions?

-------------------------

godan | 2017-11-21 20:02:39 UTC | #6

For now I've just commented out that check. Living on the edge....

-------------------------

Eugene | 2017-11-21 20:33:46 UTC | #7

[quote="godan, post:5, topic:3765"]
Not sure how to fix it, though… any suggestions?
[/quote]

Main Thread in Urho is just a thread that the Context has born. Could you ensure in debugger that you create Contex is the same thread as use cache?

UPD: You could probably _override_ main thread via `Thread::SetMainThread` if you want to "move" Context into another thread.

-------------------------

Victor | 2017-11-21 20:25:37 UTC | #8

Arg, you beat me too it (you're too fast Eugene heh)

-------------------------

