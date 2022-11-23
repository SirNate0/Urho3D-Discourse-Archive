rbnpontes | 2017-01-02 01:12:31 UTC | #1

Hello Guys, i have a problem when i try using ResourceCache->GetResource inside Component in external Dll
the returned value of method is only null
example:
[code]
// if i access this code inside LogicComponent in Dll, the resource is returned NULL
ResourceCache* cache = GetSubsystem<ResourceCache>();
cache->GetResource<Model>("Models/Box.mdl");
[/code]
*The same things happens if i'm try get mouse position in input.
Sorry for English :/

-------------------------

cadaver | 2017-01-02 01:12:31 UTC | #2

Welcome to the forums.

I assume this is the same situation as in the issue you reported. There you left out the fact that you use a DLL, which would have given more information to diagnose. Two things come to mind to first.
- Have you compiled also Urho as DLL? If not, you should.
- Are the preprocessor definitions in sync between Urho and your DLL? The major ones are those like graphics subsystem (eg. URHO3D_OPENGL / URHO3D_D3D11) and URHO3D_SSE. The reason why this could cause trouble is if Urho compilation and your DLL's compilation interpret the Urho classes' memory layouts (from header files) differently.

-------------------------

rbnpontes | 2017-01-02 01:12:32 UTC | #3

Thank's for the help, i'm trying to compile urho3D into DLL

-------------------------

