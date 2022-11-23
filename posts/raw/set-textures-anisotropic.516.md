ucupumar | 2017-01-02 01:01:02 UTC | #1

I want to change global texture anisotropic, but this code didn't work for me.
[code]Renderer* renderer = GetSubsystem<Renderer>();
renderer->SetTextureFilterMode(FILTER_ANISOTROPIC);
renderer->SetTextureAnisotropy(16);[/code]Textures on the scene still look as if it's bilinear filtered.

Do I miss something? 
:confused:

-------------------------

weitjong | 2017-01-02 01:01:02 UTC | #2

The global default texture filtering mode will only be applied when the texture's filtering mode is set to "FILTER_DEFAULT", which is the default. If the texture itself has a specific filtering mode then it won't use the global default. Have you accidentally altered the texture's own filtering mode to other than "FILTER_DEFAULT"? I am sorry if I what I have just stated is already obvious to you.

-------------------------

ucupumar | 2017-01-02 01:01:02 UTC | #3

I have checked my textures, and yes, it was using "FILTER_DEFAULT". 
It looks like a bug, because anisotropic filter works if I set the texture filter one by one.
Do this issue happen to you too?

-------------------------

weitjong | 2017-01-02 01:01:03 UTC | #4

IMHO, if you set the filtering mode to anisotropic for each individual texture and it works then it indicates there is no problem with engine code. If there is a bug somewhere then I suspect it is in your own code. Although the code snippet in your first post seems correct to me, its effect could be zero if you have that code snippet done too early in the engine initialization phase. Whatever you have set could be potentially overwritten by the engine initialization later. Why didn't you use the engine parameter to initialize filtering mode in the first place? See [urho3d.github.io/documentation/H ... _loop.html](http://urho3d.github.io/documentation/HEAD/_main_loop.html). This would not just eliminate that possibility but also make your code cleaner.

I only tested briefly the filtering mode using OpenGL graphic back-end without actually modifying any existing code. I tested it with Urho3DPlayer by using "-af" option and "-tf" option. The "-af" would enable anisotropic filtering mode automatically while setting the anisotropic level.

-------------------------

ucupumar | 2017-01-02 01:01:03 UTC | #5

I've tested using engine parameters and Urho3dPlayer, but the it still doesn't work.  :confused: 
After digging some more, it works if I'm using Directx but it isn't if I'm using OpenGL. I'm using Windows 7 x64 and Nvidia GPU. 
I'm afraid it's really a bug.

-------------------------

weitjong | 2017-01-02 01:01:03 UTC | #6

Yes, I can see it clearly now after changing to another test scene. It is a bug.

-------------------------

ucupumar | 2017-10-12 20:04:26 UTC | #7

Okay, I'm reporting this bug, [url]https://github.com/urho3d/Urho3D/issues/509[/url]

-------------------------

