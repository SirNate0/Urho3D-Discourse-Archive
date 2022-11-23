namic | 2017-01-02 01:05:45 UTC | #1

I'm deciding between Panda and Urho and i wanted to know if Urho supports deferred rendering and PBR, like Panda?

[panda3d.org/forums/viewtopi ... =6&t=17050](https://www.panda3d.org/forums/viewtopic.php?f=6&t=17050)

-------------------------

krstefan42 | 2017-01-02 01:05:46 UTC | #2

Urho3D supports deferred rendering. PBR is not currently supported. But since Urho3D lets you set custom shaders for both the G-Buffer filling pass and the deferred lights themselves, and it supports custom G-buffer layouts, there's no reason you couldn't implement it yourself, no source code changes necessary. The flexibility of Urho3D's rendering system was a big draw for me. You can pretty much do anything you want with it, as long you don't need geometry shaders, tesselation, or compute shaders.

That new Panda3D rendering system looks fantastic, though. I'll need to check that engine out. The only issue is that it requires OpenGL 4.3, at the moment.

-------------------------

hdunderscore | 2017-01-02 01:05:46 UTC | #3

I feel the metalness/roughness method is probably the better direction, and is the direction I would take my work. It's definitely a large amount of work for one person to do, between:
- Basic surface shader (forward and deferred) and all the possible techniques
- Extended shaders like hair, terrain, vegetation, skin, wetness, alpha
- PBR lights

Extra features like:
- parallax corrected cubemapping
- Reflection probe and blending

I took a shot at a few of those things, but it would need a lot more love to get it where it should be.

-------------------------

sabotage3d | 2017-01-02 01:05:46 UTC | #4

There is this one [unrealengine.com/blog/physi ... -on-mobile](https://www.unrealengine.com/blog/physically-based-shading-on-mobile) 
Which is quite cheap for mobile it should work fine for desktop as well.

-------------------------

boberfly | 2017-01-02 01:05:50 UTC | #5

Cheers for the Panda3D link! That could be a great base to work from for Urho3D albeit it targets the highest high-end deferred-only. Bumping the GL version from 3.x to 4.3+ at startup time with a flag could be done though, with graceful fallbacks.

The Panda3D codebase is quite epic though, I would rather just extend Urho3D with these same features than go into the C++/Python combo (Python is absolutely excellent for tools dev, I would never ever use it in a game runtime though). Is it true it's like 40 mins to compile Panda on a modern rig???

I'm biased towards VFX so I'd go spec/roughness vs roughness/metallic at least for the working set of files, although it's a smaller memory footprint with the latter.

I would really like to see how area lights could be incorporated to keep it more physically plausible, but I think producing shadows for these lights you need either raycasting in compute or a voxelised scene to cone trace.

-------------------------

Hevedy | 2017-01-02 01:07:45 UTC | #6

The updates of this are awesome [github.com/tobspr/RenderPipeline/tree/master](https://github.com/tobspr/RenderPipeline/tree/master) if Urho3D include some of the things here in CPP this will be something awesome to create games.

-------------------------

sabotage3d | 2017-01-02 01:07:47 UTC | #7

The renders are quite good. I wonder what is the benchmark of these renders.

-------------------------

rasteron | 2017-01-02 01:07:47 UTC | #8

[quote]The Panda3D codebase is quite epic though, I would rather just extend Urho3D with these same features than go into the C++/Python combo (Python is absolutely excellent for tools dev, I would never ever use it in a game runtime though). Is it true it's like 40 mins to compile Panda on a modern rig???
[/quote]

As another python coder, I already tried Panda3D and Tobias' RenderPipeline build. RenderPipeline is still experimental so I would not bet on it to make serious or mid size PBR based games yet, it is great for tech demos though :wink:. The build time is really slow (vanilla Panda3d) and could take as much as a couple of hours if you include all options, which is the default. Sources and generated files also  huge around 8GB total.

There were large scale and established MMO games with Panda3D so I would say it's really another great engine.  :smiley: 

Pirates of the Carribean Online
[video]https://www.youtube.com/watch?v=K1P5F1WEV3I[/video]

ToonTown Online
[video]https://www.youtube.com/watch?v=TgNeb9XRPMs[/video]

-------------------------

tobspr | 2017-01-02 01:07:48 UTC | #9

[quote="Sinoid"]Surprise, the project is dead.[/quote]

I have investigated into this and the lines of code in question were freely available from multiple presentations, for example
the presentation from DICE about moving to physically based rendering, also some Disney Presentations (Actually, most of the BRDF's are those from Disney, which are reused from Unreal and Frostbite).

However, the code you mentioned was only temporary code, and I'd like to thank you for pointing this out. I have changed this code, and
also added a License file to the refactoring_beta branch of the RenderPipeline. 

I have also replied to your issue request, if you have any other concerns, please let me know.

[quote="Hevedy"]if Urho3D include some of the things here in CPP this will be something awesome to create games.[/quote]
Feel free to use parts of the RenderPipeline in Urho3D if you like, I'd be more than happy to help if there are any questions.

Cheers,
tobspr

-------------------------

Hevedy | 2017-01-02 01:07:49 UTC | #10

[quote="Sinoid"]I've raised an issue about the stolen code and contacted the original author of the code. This project is likely effectively dead and nuked in a few days. Either way, if you even touch this code you are subjected to Epic's license to whom it belongs.[/quote]

Wow then that code is stolen ? i don't know that, me bad then and I'm a user of UE4 and I don't see that...

[quote="tobspr"][quote="Sinoid"]Surprise, the project is dead.[/quote]

I have investigated into this and the lines of code in question were freely available from multiple presentations, for example
the presentation from DICE about moving to physically based rendering, also some Disney Presentations (Actually, most of the BRDF's are those from Disney, which are reused from Unreal and Frostbite).

However, the code you mentioned was only temporary code, and I'd like to thank you for pointing this out. I have changed this code, and
also added a License file to the refactoring_beta branch of the RenderPipeline. 

I have also replied to your issue request, if you have any other concerns, please let me know.

[quote="Hevedy"]if Urho3D include some of the things here in CPP this will be something awesome to create games.[/quote]
Feel free to use parts of the RenderPipeline in Urho3D if you like, I'd be more than happy to help if there are any questions.

Cheers,
tobspr[/quote]

Sorry I'm a noob in the core programming or shaders  :unamused:

There is too this other project [github.com/bkaradzic/bgfx](https://github.com/bkaradzic/bgfx) and have some interesting things.

-------------------------

