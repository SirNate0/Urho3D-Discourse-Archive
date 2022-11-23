Hevedy | 2017-01-02 01:00:22 UTC | #1

Hi.
This month i find a tool kit released by  sony written in c# under apache2, have a complete editors (map, model, audio...)
Is a good idea implement this in Urho ?

Tools: [github.com/SonyWWS](https://github.com/SonyWWS)
Videos: [youtube.com/channel/UCuUcAf ... gouVQ/feed](https://www.youtube.com/channel/UCuUcAf-iOrjBGGNEtugouVQ/feed)

-------------------------

friesencr | 2017-01-02 01:00:22 UTC | #2

I noticed this a while ago too.  It will be interesting to see how it progresses.  It's road map is ambitious.  Currently I think urho can boast that it has more functionality.  After reading c# + managed extensibility framework I didn't look much into it.  I had a lifetime of sorrow from the wpf prism framework.  C# hasn't had the best of luck with its component architecture.  Although mef is far better.

-------------------------

cadaver | 2017-01-02 01:00:25 UTC | #3

If someone was to code, let's say, a converter that spits out Urho compatible data from the Sony editor, I would have nothing against it. But I don't think the Urho runtime itself should contain code for loading the Sony editor data, or have a promise of supporting it, as we already have Urho's own scene representation which works for several usecases (savegames, network replication, prefabs..) It would be an additional maintenance burden and mismatches in loading the data would be seen as Urho bugs.

-------------------------

boberfly | 2017-01-02 01:00:26 UTC | #4

I do have a WIP project I didn't want to quite disclose yet until it's in a better state, but I'm currently looking into the Cortex VFX/Gaffer projects from ImageEngine and extending it to support Urho3D:
[imageengine.github.io/gaffer/](http://imageengine.github.io/gaffer/)

The tech behind it is C++/Python with Qt and Boost for the most part, which is a bit heavy and definitely not for the Urho3D runtime, but it's very platform-agnostic in terms of supporting Linux/OSX currently (and I'm in the process of porting it to Windows in my Github). Gaffer really shines at procedurally building scenes using nodes from existing exported assets from a DCC package in Alembic or its own internal Cortex-specific format, and applying shaders, attributes, procedures, etc. and building scenes for offline renderers (Arnold and 3Delight/PRman currently).

My plan was to first make an 'IECoreUrho3D' which would link just the system+network libs of Urho for serialisation and to run a server in Cortex/Gaffer and the idea was to hook in an Urho3D client to pick up changes and hot-reloads of files to produce renders very very fast (and to save out EXRs at the other end), but this certainly could be extended for building environments procedurally for a game as the framework is very easy to extend in Python or C++. Gaffer's file format .gfr is just a large python script full of operators so everything stays procedural and non-destructive when transforming your asset data, so this can be a huge production win for a large project.

As an example the most simple problem this could automatically solve is where you export out an asset from your DCC and modify attributes in the editor like add physics and shader settings, but then need to re-export your asset, you wouldn't need to redo all that work in the editor because of the asset change. Imagine doing this on a large game, or you need to add some change to the xml data to all your assets due to some added feature. Cortex/Gaffer can also work headless so using a render farm or cloud service for a large change could be done as well. Lots of potential here. :slight_smile:

The Urho3D editor itself is certainly very good, but I think some things should stay in an external tool as it doesn't make sense to have some stuff in the runtime itself, like non-destructive asset formats, the runtime only cares about optimised final assets most of the time (depending on your game), there's always going to be a conflict here on where to draw the line and not cause performance bottlenecks because your asset needs to stay non-destructive. Something like Sony's editor could be really good here, I've not seen the API but the C#/WinForms/DX11 stuff isn't too interesting to me.

-------------------------

