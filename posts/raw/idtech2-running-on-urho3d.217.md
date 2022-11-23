jenge | 2017-01-02 00:58:56 UTC | #1

[size=150]idTech2 running on Urho3D[/size]

[video]https://www.youtube.com/watch?v=_eSRhcfeb_U[/video]

[size=120]What is this and why?[/size]

A fun weekend project to see how well using Urho3D as a rendering/platform layer for idTech2 would work.  This was a test and and a proof of concept.  

I've wanted to make a game using idTech2 and learn GTKRadiant for a long time.  This prototype pushes that desire forward another notch.  

I also worked a bunch on some Urho3D tech last winter including a Unity3D exporter (VIDEO: [youtube.com/watch?v=m3ehQwfbjGg](https://www.youtube.com/watch?v=m3ehQwfbjGg)).  I have been working more on the Unity3D exporter and I think this will be a very good content path for Urho3D projects.

[size=120]Goals[/size]

A feature complete idTech2 renderer and platform layer built using Urho3D which supports both demo playback and actually playing Quake2.

It needed support for transparency, animated lightmaps and world textures (lightstyles!), dynamic lights, alias morph models, water effetcts, particles, and moving/rotating brush models.  The parts that I haven't gotten to being "beams" and some view blends.  However, dynamic lights casting shadows and Urho's refracting water all working kind of make up for these :slight_smile:

I wanted to run on both OpenGL and Direct3D.  I developed using QtCreator on OSX and spent maybe 30 minutes at the end getting the Windows/D3D build working, again with QtCreator :slight_smile:

The platform layer isn't "feature complete", though it would be easy to make it so.  The biggest missing thing is that I didn't hook up WAV loading/playback.  However, I did get keyboard/mouse input working and the game is fully playable.

[size=120]Anti-Goals[/size]

I didn't want to add/change anything in the stock Urho3D rendering code.  I also wanted to make sure idTech2 stayed intact without any core changes.  idTech2 has a nice rendering "plugin" system, so all the Urho3D stuff is completely opaque to it.  

[size=120]Why idTech2?[/size]

idTech2 solves a lot of really hard problems (which modern engines continue to struggle with) in a very elegant and small codebase.

It has really smooth networked physics, excellent PVS and PHS support (which is still really important especially when doing [b]per pixel lighting[/b]!), and is a game engine with working content pipeline and processing tools (GTKRadiant is still in use by major studios!).  This is an interesting review on idTech2: [fabiensanglard.net/quake2](http://fabiensanglard.net/quake2)

[size=120]Why Urho3D?[/size]

Urho3D is a fantastic engine, I really love working with it.  I think Urho is a great fit for indie developers due to its (extremely) clean design and relatively small footprint.  It also has excellent cross platform support.

[size=120]What does the code look like?[/size]

It is very much a prototype ATM: [gist.github.com/JoshEngebretson ... f793fbe422](https://gist.github.com/JoshEngebretson/fc08622b25f793fbe422)

However, it is a quite small amount of code and would be easy to refactor it for OOP and for better Urho3D styling.  I think this will be a good project, for next weekend! :slight_smile:

- Josh

-------------------------

Canardian | 2017-01-02 00:58:56 UTC | #2

Holy cow, and I thought John Carmack was a god :slight_smile:
And it's really nice to see how clean and perfectly designed the Urho3D engine is, that it can serve even this kinds of requirements.

-------------------------

cadaver | 2017-01-02 00:58:56 UTC | #3

This is very nice. Actually I didn't think Urho would fit to this kind of work well, as all it has is the retained scenegraph and no easily accessible full-functionality immediate rendering (ie. "render this model with these lights"), but you worked around it cleverly. :slight_smile:

-------------------------

jenge | 2017-01-02 00:58:57 UTC | #4

Thanks Lasse :slight_smile:

Urho3D is really great to work with... so many solid features and design choices!

I really wanted to use stock Urho3D rendering features while still retaining idTech2 PVS to the degree that makes sense.  This wasn't at the polygon level, however at the cluster level the PVS still breaks a level up pretty well.  The prototype runs well on my MBAir with an Intel HD3000, but this particular GPU is a bit underpowered so the PVS is actually super important when doing the per pixel lighting effects.  

You can kind of see in the video that shadows are being cast, but the lighting is pretty fast paced in Quake2 so hard to see...  there is also support for lightmap styles, so lightmaps can flicker/pulse/turn on and off, etc.  It is awesome how well the lightmaps and realtime lights mix!  The refracting water effect you did is also really nice on water brushes!

At every corner, Urho3D provided a way of handling something... Alias model? Use morphs! Global particle pool?  Use a billboard object and turn off sorting!, etc   I want to keep going with it, the code prototype was mostly about figuring out the hows without concern for style.  I also really like Urho3D's style guide :slight_smile:

Thanks again for all the hard work!

- Josh

-------------------------

scorvi | 2017-01-02 00:58:57 UTC | #5

wow :slight_smile:

i just downloaded the idTech2 engine and i am now playing with it. 

But i have a problem how to start implementing uhro3d as the rendering plugin. Can you give me some hints ? (or a little more source code) I really like to implement it :slight_smile: 

Can you say a little more about the headers  "TBESystem.h" , "TBEMapModel.h" , "TBEAliasModel.h"  and how you implemented which interface function ? 

thx

-------------------------

jenge | 2017-01-02 00:58:58 UTC | #6

Hi scorvi,

You can checkout the source from our Urho3D fork here: [github.com/ThunderBeastGames/Ur ... /QuakeToon](https://github.com/ThunderBeastGames/Urho3D/tree/tb_master/Source/ThunderBeast/QuakeToon)

You'll need to unpack the Quake2 demo assets in the pak file so you have a Data/baseq2 and you'll also need to drop the hires texture pack textures into the root of Data/Textures

Please note that this iteration is very protoype and I plan to rewrite the code, so it will drastically change.  

- Josh

-------------------------

friesencr | 2017-01-02 00:58:58 UTC | #7

We may need to test the netcode over a coop game.  You know... for science.

-------------------------

scorvi | 2017-01-02 00:58:59 UTC | #8

[url=http://imgur.com/EUuh11p][img]http://i.imgur.com/EUuh11pl.png[/img][/url]

so its working :slight_smile: but i could not find the hires textures pack ...

[quote="friesencr"]We may need to test the netcode over a coop game.  You know... for science.[/quote]
yes i think we should do that!

-------------------------

Hevedy | 2017-01-02 00:58:59 UTC | #9

Why no use Doom 3 or Id tech 3?
You are comparing idtech with Urho3D really ?
If Urho3D have support with Radiant for import scenes, that change some things...

-------------------------

barrettcolin | 2017-01-02 00:59:12 UTC | #10

This is inspired lunacy: I approve  :slight_smile: 

I found the hi-res texture pack here: deponie.yamagi.org/quake2/texturepack/

(As it's my first post, the forum won't let me embed a URL; but I'm sure if you're sufficiently motivated you'll figure it out)

-------------------------

1vanK | 2017-01-02 01:09:09 UTC | #11

[quote="jenge"]Hi scorvi,

You can checkout the source from our Urho3D fork here: [github.com/ThunderBeastGames/Ur ... /QuakeToon](https://github.com/ThunderBeastGames/Urho3D/tree/tb_master/Source/ThunderBeast/QuakeToon)

- Josh[/quote]

Is it possible to view the source code now?

-------------------------

jenge | 2017-01-02 01:09:09 UTC | #12

Hello,

Yup, I moved it to my personal account here:

[github.com/JoshEngebretson/Urho ... /QuakeToon](https://github.com/JoshEngebretson/Urho3D/tree/tb_master/Source/ThunderBeast/QuakeToon)

- Josh

-------------------------

1vanK | 2017-01-02 01:09:09 UTC | #13

Thank you!

-------------------------

1vanK | 2017-01-02 01:12:14 UTC | #14

I found a playable port Quake 2 to Urho3D engine. [github.com/barrettcolin/Urho3D/tree/quake2](https://github.com/barrettcolin/Urho3D/tree/quake2) It's strange that I didn't know about it before  :shock: 
It seems that works only software render.

EDIT: It just output quake's render to texture and show on plane

-------------------------

