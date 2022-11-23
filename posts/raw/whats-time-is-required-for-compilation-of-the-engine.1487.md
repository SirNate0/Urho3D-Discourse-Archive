GoldNotch | 2017-01-02 01:08:06 UTC | #1

I have a problem: When i try to compile Urho3d, compilation reaches to 
[code]Assimp.vcxproj -> Z:\Engines\Urho3D-master\Build\Source\ThirdParty\Assimp\Debug\Assimp.lib[/code]
and stops. It goes, simply the compiler long compiles the file. It and has to be? or I made a mistake? And I'd like to know: what's time is required for compilation.

-------------------------

thebluefish | 2017-01-02 01:08:06 UTC | #2

[quote="GoldNotch"]what's time is required for compilation.[/quote]

It compile in ~3-4 minutes on my work machine, and ~2-3 minutes at my home machine.

-------------------------

bvanevery | 2017-01-02 01:08:20 UTC | #3

I'm using 3 old 2007..2008 era laptops with Core2 Duo processors, 4GB RAM, Windows 7.  Building the Urho3D 1.5 release in debug with VS 2015 64-bit took about 12 minutes.  I did not build the docs.

-------------------------

