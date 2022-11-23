JTippetts | 2017-01-02 00:58:07 UTC | #1

Woot! 2D stuffs. I do love me some 2D stuffs. Thanks, aster2013!

-------------------------

weitjong | 2017-01-02 00:58:07 UTC | #2

Been waiting for it to reach master branch and eager to check it out immediately. I tried both the cpp and Lua samples. On my Linux 64-bit machine, the cpp sample runs fine initially but occasionally segfault on exit; after that it is kind of alternating between running and core-dump on starting. The Lua sample segfault more often than cpp sample. It is late here now, so I think I will continue to check it tomorrow when I am free. Regardless, kudos to Aster!

-------------------------

friesencr | 2017-01-02 00:58:07 UTC | #3

wow!  i am going to get testing on this stuff as soon as i get a free moment.  now that we have the base we can iterate! <3

-------------------------

aster2013 | 2017-01-02 00:58:07 UTC | #4

Thanks, I will give two 2D sample in C++ Lua and AngelScript.

-------------------------

cadaver | 2017-01-02 00:58:08 UTC | #5

Nice! I will get to test the code during weekend.

-------------------------

weitjong | 2017-01-02 00:58:08 UTC | #6

[quote="weitjong"]On my Linux 64-bit machine, the cpp sample runs fine initially but occasionally segfault on exit; after that it is kind of alternating between running and core-dump on starting. The Lua sample segfault more often than cpp sample. It is late here now, so I think I will continue to check it tomorrow when I am free[/quote]

Sorry for the delay. I had been away to continue to debug the seg fault issue. I am not entirely sure yet, but I think it has something to do with Drawable2D::UpdateMaterial() method. I notice two things:
1. The material_ instance variable never get assigned in the cpp sample. I fail to see where SetMaterial() is being or should be called.
2. The UpdateMaterial() method is being referenced by UpdateBatches() which may be called from worker threads. Current implementation may not be thread-safe. If I run the sample by forcing it to run in a single threaded mode then it does not crash in my system. If I run it normally (I have a 4-core machine) then it crashes mainly in this method - double releasing refcounted object.

-------------------------

cadaver | 2017-01-02 00:58:08 UTC | #7

Now got to test this as well. Excellent work!

I found the same that it would randomly segfault when run with threads on. UpdateBatches() is indeed not a good place to be creating objects or cloning them, because SharedPtr / WeakPtr refcounts are not thread-safe. Rather, I think the material update can be moved to happen on-demand in the setter functions, so that when it's time for the render update, the material is already correct.

EDIT: it shouldn't crash any more. 

Btw. if you want to improve the instancing and render queue behavior, there could be a "material cache" for Drawable2D's that you'd request materials from (base material + texture + blendmode) and it would look up if one already exists and not clone / create more than once. Now, when each material is unique, it creates a separate batch group for each without being able to benefit from instancing. The same could be done for vertex buffers, if their content is the same.

-------------------------

weitjong | 2017-01-02 00:58:08 UTC | #8

I can confirm it is not crashing on my system anymore. Thanks for the quick fix!

I have also observed one peculiarity with Lua sample (24_Urho2DSprite.lua) which I could not yet explain or understand why it happens, the flower movement is not all the way smooth. It is more pronounce when the Urho3DPlayer is built using Debug configuration but it is also observable using Release configuration. Using profiling tool, I can see the max FPS is alternating between 200 (cap) and 190, back and forth. So, there is a noticeable small jump in the flower movement every now and then. This symptom does not occur on the cpp and AngeScript implementation on the same sample. So, it could be more to do with Lua/LuaJIT then to Urho2D subsystem. Anyone else also seeing this?

-------------------------

Mike | 2017-01-02 00:58:08 UTC | #9

I noticed it either (I thought it was coming from my old computer). Translation is globally less fluid (slightly blured) and becomes jerky from time to time.
Perfect for C++ and AS.

-------------------------

aster2013 | 2017-01-02 00:58:09 UTC | #10

It is that we current use Vector3 in Lua, when call Vector3::operator+ or Vector3::operator*, it will return new Vector3 with Lua GC. so the FPS not smooth.  
I have do some change,  just use Node::GetPositionXYZ function and SetPositionXYZ replace old source, It will not new User data in Lua.

-------------------------

Mike | 2017-01-02 00:58:09 UTC | #11

Thanks Aster, everything is perfect for me  :stuck_out_tongue:

-------------------------

aster2013 | 2017-01-02 00:58:09 UTC | #12

This is not the best solution. 
The better solution may be like we dispose Vector<> and PODVector<> to Lua table. We can create a table call Vector3 in Lua, and build the mapping between Lua and C++.

-------------------------

Hevedy | 2017-01-02 00:58:10 UTC | #13

If add 2D why not add 2D physics with Box2D ?

-------------------------

weitjong | 2017-01-02 00:58:10 UTC | #14

Aster had Box2D once added into 2D branch but the integration is incomplete. At least that is how I understand it. I don't think Box2D integration will make it into the coming release, which should be any time now.

-------------------------

aster2013 | 2017-01-02 00:58:11 UTC | #15

Hi, Hgdavidy

Do you want to make 2D game with Urho3D? Box2D suport will be add later.

-------------------------

cadaver | 2017-01-02 00:58:11 UTC | #16

Another thing that came to my mind is that the 2D features will need documentation in the Doxygen pages. It doesn't need to be very fancy or long, but to just explain how the new resources and new components work. For now I'll just add the 2D drawables to the list on the "Rendering" page. Aster, if you make the documentation (as you actually know the features best) others can then help with grammar / editing, if necessary.

-------------------------

Hevedy | 2017-01-02 00:58:11 UTC | #17

[quote="aster2013"]Hi, Hgdavidy

Do you want to make 2D game with Urho3D? Box2D suport will be add later.[/quote]

Oh, no at this moment i have other 2D games engines, but at see the 2D topic i give the idea, for 2D games i use SDL or SFML with custom basic engine only for 2D, and i have the Gamemaker Studio purchased for make a fast 2D game, 
but i like make 3D game in near future with (Urho or Ogre) for make the custom base engine with the game on this, and if this is impossible with (Unity or UDK) if don't see advantages here. I prefer the Urho build of graphics + network + all and networked physics is rather for me than basic of Ogre, but Ogre have more worked graphics and gui (I'm waiting for 2.0 version with Opengl 3.2) and you can build all structure, the Urho structure for me not good (for me), i like more the structure of Id Tech3 or 4 or Cryengine (The file system (locations, shaders, scripts, paks, commands) (Old school, no for mobile devices)) the Tesseract engine structure (external) is ok for example (but need pak the files and the engine no support LODs or networked physics...).
The Urho editor idea of show nodes, don't is he best idea and need channels and folders, because if you make a normal map for a pc game you add from 200 nodes to 100.000? that is insane.
See at GTKRadiant or Cryengine (Editors) structure.
For the 3D i need the network physics(already), a tutorial about how add models (static, dynamic, physics, character with bones and collision), FPS and TPS camera, basic support of animations with kinematics (if is possible), scripting of the maps for animated models in the map (rotation,... networked).

Conclusion, i like use this for 3D game but need changes...

-------------------------

aster2013 | 2017-01-02 00:58:11 UTC | #18

Hi, 2D rendering is simple enough. the no much feature on it. Here is some explain for 2D rendering resources.

[b]SpriteSheet2D[/b]
A 2D sprite sheet is a texture atlas, it contains many texture call Sprite2D. Urho3D use same file format as Sprarrow / Starling engine. Sprite sheet can be created use a tool call TexturePackager [url]http://www.codeandweb.com/texturepacker[/url].

[b]Animation2D[/b]
A 2D Animation is a XML file define a sequence Sprite2D call frame. The frame include duration time and refer a Sprite2D. These is no tool for it, but the file format is simple enough. Here is a sample of 2D animation:
[code]<Animation >
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@0" />
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@1" />
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@2" />
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@3" />
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@4" />
</Animation>[/code]

[b]ParticlesEmitter2D[/b]
A 2D partile system can be created use 71squared's ParticleDesigner [url]http://71squared.com/particledesigner[/url]. The tool can only run on Mac OSX.

-------------------------

cadaver | 2017-01-02 00:58:11 UTC | #19

Hgdavidy, you can use "dummy" scene nodes to group things in scenes. Similar as you would do in Unity. But if we are realistic I don't think extensive changes will happen to the editor/engine in any near future. More tutorials also depend on the community activity, for example, I know very little about modeling animated characters in Blender et al. and exporting them so that they work in an engine, so I can't actually help there. As a summary, you may be better off to choose another engine and not frustrate yourself with Urho3D.

Aster: please do not just post on the forum, put that in the .dox files :slight_smile: For the soon coming release it's not necessary, but for the next one it's nice to have full documentation, when there's 2D physics components also.

-------------------------

Hevedy | 2017-01-02 00:58:11 UTC | #20

[quote="cadaver"]Hgdavidy, you can use "dummy" scene nodes to group things in scenes. Similar as you would do in Unity. But if we are realistic I don't think extensive changes will happen to the editor/engine in any near future. More tutorials also depend on the community activity, for example, I know very little about modeling animated characters in Blender et al. and exporting them so that they work in an engine, so I can't actually help there. As a summary, you may be better off to choose another engine and not frustrate yourself with Urho3D.[/quote]

Not are more engines is Urho or Ogre (Only graphics and not a best of graphics ) or id tech 4 (bad license and outdated) (All frustrate  :slight_smile: ) that or pay to win with UDK (script of the hell). Don't have a engine with all or ~80% of tools...

-------------------------

cadaver | 2017-01-02 00:58:11 UTC | #21

When editing the 2D components I noticed that the Unit Per Pixel parameter decreases sprite size, but increases particle size. I've made an issue to the github tracker. I could do the proposed change (rename it Pixels Per Unit and make it behave consistently) before release.

-------------------------

Hevedy | 2017-01-02 00:59:11 UTC | #22

[quote="aster2013"]Hi, 2D rendering is simple enough. the no much feature on it. Here is some explain for 2D rendering resources.

[b]SpriteSheet2D[/b]
A 2D sprite sheet is a texture atlas, it contains many texture call Sprite2D. Urho3D use same file format as Sprarrow / Starling engine. Sprite sheet can be created use a tool call TexturePackager [url]http://www.codeandweb.com/texturepacker[/url].

[b]Animation2D[/b]
A 2D Animation is a XML file define a sequence Sprite2D call frame. The frame include duration time and refer a Sprite2D. These is no tool for it, but the file format is simple enough. Here is a sample of 2D animation:
[code]<Animation >
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@0" />
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@1" />
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@2" />
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@3" />
    <Frame duration="0.1" sprite="Urho2D/GoldIcon.xml@4" />
</Animation>[/code]

[b]ParticlesEmitter2D[/b]
A 2D partile system can be created use 71squared's ParticleDesigner [url]http://71squared.com/particledesigner[/url]. The tool can only run on Mac OSX.[/quote]

Have a tutorial to use the SpriteSheet2D with static textures in a generated texturemap/atlas ?

-------------------------

Mike | 2017-01-02 00:59:11 UTC | #23

Urho2D documentation has been updated recently, please check [url]http://urho3d.github.io/documentation/a00034.html[/url].
Note that 29_Urho2DConstraints sample is not released yet.

-------------------------

Faizol | 2017-01-02 00:59:18 UTC | #24

[quote="Mike"]Urho2D documentation has been updated recently, please check [url]http://urho3d.github.io/documentation/a00034.html[/url].
Note that 29_Urho2DConstraints sample is not released yet.[/quote]

Hi Mike,

  is there any publicly available roadmap for 2D implementation in Urho3D engine? I'm trying to get more information regarding isometric tiling and 2d particle plans if any.

  Thanks.

-------------------------

Mike | 2017-01-02 00:59:18 UTC | #25

Urho2D is brought to us thanks to Aster  :stuck_out_tongue: 
I don't know about his personal roadmap in terms of new features and horizon.

-------------------------

aster2013 | 2017-01-02 00:59:21 UTC | #26

I have no roadmap on Uhro2D.
It may add tile-map to Urho2D, but I am working on a Qt based editor for Urho3D, it may delay for tile-map.

-------------------------

