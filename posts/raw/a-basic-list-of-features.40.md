Hevedy | 2017-01-02 00:57:33 UTC | #1

Hi all.
Here i give a list of features that might be good to implement...
I made this for participate in a good project (best engine open source i see) and give ideas, not for give work to make.

--Needed, -Normal,-* Extras.

[b]Examples:[/b]

	- Inverse Kinematics example.
	- Upgrade the vehicle example ?
	- Graphics example with some thinks.
	-- Glass example.
	-- FPS with camera hands(Basic).
	-- Light types example and projectors.
	-- Trigger examples move objects or enable others.
	-* Breakable examples.
	-* Flag physics example.
	-* Day - Night cycle example.
	-* Water with physics example.
	
[b]AI/Physics/Animation:[/b]

	- Add Inverse Kinematics with ground alignment.
	-- Zone of animation or action for AI.
	-* Add Flag/Cloth physics from Bullet.
	-* Add Basic water sim (basic waves and var for physic objects(float or not, mass)).
	- Breakable objects 4 types:
		-- 	1- Jointed breakable object (jointed parts in 3d editor, in game have individual physics and start static).
		--	2- Same as 1 but the model change in other models and at the end part select have to breakable object or not).
		-- 	3- Pre-Backed physics object (Animation + physics).
		-*     4- Deformable objects (the object 3d model vertex change procedural).
		-** 	5- Procedural physics object (Physics procedural calculation).
	-* Environment controlled objects (Clouds, Vegetation wind, Water...)(For vegetation use for example some animations cycle or procedural but is hard).
        -- Material types and class, (metal,wood, others) give different properties.
	
[b]Render/Light/Shaders:[/b]

	-- Add Glow.
        -- God Rays.
	-- Add HDR and Global Ilumination.
	-* Add SSAO.
	-* Add Projected Decals. (Box in editor)
	- Add Light with texture projected.
	-* Add different types of Antialising. (SMAA, MSAA...)
	-- Add Glass.
	
[b]Tools:[/b]

	- Enviorment, Skybox, Fog, HDR configurator.
	- Terrain editor(heightmap)
	-* Build editor(editor like id tech3 or 4 with views) BSP/GSC.
	
	Sorry for my english.
	
Thanks all.

[size=85][i]edited for best reading by moderator.[/i][/size]

-------------------------

cadaver | 2017-01-02 00:57:33 UTC | #2

A couple of quick notes:
- Animation blending already exists and is based on layer priority. You'll see multiple animations blended in eg. NinjaSnowWar. 
- The 17_SceneReplication example is a controllable physics ball, but it's networked only (you can run a client and server on same machine)
- HDR rendering is being implemented in the Shaders branch.

It's fine to write these kinds of "wishlists" to inspire/stimulate development, and to keep record so that good ideas aren't forgotten. Progress usually happens when developers are also interested in the same things. However the basic risk in an open source project is that when you make a request, you have the risk of it never completing. So if you want to be certain that it's done, you start doing it yourself :slight_smile:

-------------------------

cin | 2017-01-02 00:57:33 UTC | #3

[quote] Day - Night cycle example.[/quote]
Simple rotate directional light and disable light if sun under horizont. For sky box you can use three textures (night, morning and day) and interpolate it over time in shader. Also change Zone parameters ad ambient light and fog parameters. It easy. In my game it maked as component. May be later I share it.

[quote]Global Ilumination[/quote]
Some like this? [sdrv.ms/1cb8N99](http://sdrv.ms/1cb8N99)?

[flash=640,480]http://www.youtube.com/v/1pjupG1YPgE?version=3&amp;hl=ru_RU&amp;rel=0[/flash]
I think this is very complex. 

I think what we all must learn engine and make some things by self and help for [b][color=#800000]Lasse[/color][/b], he make great engine :wink: which only on begin of path to peoples.

But some things may be realized. Later.

-------------------------

Hevedy | 2017-01-02 00:57:33 UTC | #4

[quote="cadaver"]A couple of quick notes:
- Animation blending already exists and is based on layer priority. You'll see multiple animations blended in eg. NinjaSnowWar. 
- The 17_SceneReplication example is a controllable physics ball, but it's networked only (you can run a client and server on same machine)
- HDR rendering is being implemented in the Shaders branch.

It's fine to write these kinds of "wishlists" to inspire/stimulate development, and to keep record so that good ideas aren't forgotten. Progress usually happens when developers are also interested in the same things. However the basic risk in an open source project is that when you make a request, you have the risk of it never completing. So if you want to be certain that it's done, you start doing it yourself :slight_smile:[/quote]

Thanks for fast reply.
Ok sorry i remove the animation blending.(me fail)
Oh wow i dont see the "17_SceneReplication" ball  :astonished:  thanks.
I'm now making a launcher for Urho3D for the lua, as and asc scripts... in QT, C++. (Launcher MIT, QT Lgpl)

[quote="cin"][quote] Day - Night cycle example.[/quote]
Simple rotate directional light and disable light if sun under horizont. For sky box you can use three textures (night, morning and day) and interpolate it over time in shader. Also change Zone parameters ad ambient light and fog parameters. It easy. In my game it maked as component. May be later I share it.

[quote]Global Ilumination[/quote]
Some like this? [sdrv.ms/1cb8N99](http://sdrv.ms/1cb8N99)?

I think this is very complex. 

I think what we all must learn engine and make some things by self and help for [b][color=#800000]Lasse[/color][/b], he make great engine :wink: which only on begin of path to peoples.

But some things may be realized. Later.[/quote]

Oh thanks for the interest but that look too advanced(i only say GI without Voxel Cone Tracing, that is only DX11 and OpenGL 4.x?), i say more like this, look at this. [tesseract.gg/](http://tesseract.gg/)
This have global ilumination, GSC, camera view hands, antialiasing smaa... and shaders is the Tesseract Engine [tesseract.gg/](http://tesseract.gg/) and is Zlib license with all source code, 
for view the GI and other thinks in.

Oh the app you upload dont run for me, use DX11 ? i only support to Dx10. (9800GTX+)  :frowning: 

Thanks all.

-------------------------

cadaver | 2017-01-02 00:57:34 UTC | #5

Thanks for the Tesseract link, their description of their rendering pipeline is very interesting. Being that they implement a specific game instead of a general-purpose engine they have greater freedom to implement the rendering pipeline just as they want (and what fits best for that scenario) but I'd believe at least some of those techniques (such as the GI) could be generally usable.

-------------------------

Hevedy | 2017-01-02 00:57:34 UTC | #6

[quote="cadaver"]Thanks for the Tesseract link, their description of their rendering pipeline is very interesting. Being that they implement a specific game instead of a general-purpose engine they have greater freedom to implement the rendering pipeline just as they want (and what fits best for that scenario) but I'd believe at least some of those techniques (such as the GI) could be generally usable.[/quote]

Ok nice thanks.
But the GI have a problem with indoors, need create a zone to disable the GI in some zones of map. (No dark zones).

Ty.

-------------------------

Jace | 2017-01-02 00:57:35 UTC | #7

[quote="cadaver"]Thanks for the Tesseract link, their description of their rendering pipeline is very interesting. Being that they implement a specific game instead of a general-purpose engine they have greater freedom to implement the rendering pipeline just as they want (and what fits best for that scenario) but I'd believe at least some of those techniques (such as the GI) could be generally usable.[/quote]

It's funny you mention that becauseI had actually thought of combining the features of Tesseract with Urho3D to create an 'ultimate game engine' of sorts. Yes, corny I know but what's wrong with taking the best parts of both and putting them together?  :smiley: 

On a serious note, both projects are SDL2 and octree based with very similar, permissive licenses. I see no reason why they shouldn't/couldn't benefit one an other. That's part of what open source is all about isn't it?

Also, here is a very nice Game engine based on the Tessurect source I've been following for some time known as [url=https://github.com/OctaForge/OF-Engine]"octaforge"[/url] that the Urho3D community and devs may find very intersting. The developer quaker66 has made some very noteworthy improvements to the original source of Tesseract.

-------------------------

Hevedy | 2017-01-02 00:57:35 UTC | #8

[quote="Jace"][quote="cadaver"]Thanks for the Tesseract link, their description of their rendering pipeline is very interesting. Being that they implement a specific game instead of a general-purpose engine they have greater freedom to implement the rendering pipeline just as they want (and what fits best for that scenario) but I'd believe at least some of those techniques (such as the GI) could be generally usable.[/quote]

It's funny you mention that becauseI had actually thought of combining the features of Tesseract with Urho3D to create an 'ultimate game engine' of sorts. Yes, corny I know but what's wrong with taking the best parts of both and putting them together?  :smiley: 

On a serious note, both projects are SDL2 and octree based with very similar, permissive licenses. I see no reason why they shouldn't/couldn't benefit one an other. That's part of what open source is all about isn't it?

Also, here is a very nice Game engine based on the Tessurect source I've been following for some time known as [url=https://github.com/OctaForge/OF-Engine]"octaforge"[/url] that the Urho3D community and devs may find very intersting. The developer quaker66 has made some very noteworthy improvements to the original source of Tesseract.[/quote]

The Tesseract engine is very basic engine and limited. (Bad optimization of 3d external models) but good graphics(medium-high).
The OctaForge look like a clone of Tesseract with lua and some changes with bad optimization... ?
Here have other engines to view:

*- [url]https://github.com/ivansafrin/Polycode[/url] (2D and 3D engine with editors look good, (work in progress))
*- [url]http://www.ogre3d.org/[/url] (Nice render engine)(Need updates).
*- [url]https://github.com/TTimo/doom3.gpl[/url] // [url]https://github.com/id-Software/DOOM-3-BFG[/url] (ID Tech4 nice)(Old, but realtime and editors).
- [url]https://github.com/GarageGames/Torque3D[/url] (Mega bad optimization).
- [url]http://irrlicht.sourceforge.net/[/url] (Good basic engine).

Ty.

-------------------------

friesencr | 2017-01-02 00:57:36 UTC | #9

I have no idea how i missed this game engine.
[github.com/mosra/magnum](https://github.com/mosra/magnum)

Here is a rendering engine:
[github.com/bkaradzic/bgfx](https://github.com/bkaradzic/bgfx)

-------------------------

Hevedy | 2017-01-02 00:57:36 UTC | #10

[quote="friesencr"]I have no idea how i missed this game engine.
[github.com/mosra/magnum](https://github.com/mosra/magnum)

Here is a rendering engine:
[github.com/bkaradzic/bgfx](https://github.com/bkaradzic/bgfx)[/quote]

Oh wow thats is nice, advanced examples/codes (metaballs,hdr...)

I have this others:
[url]http://www.spinxengine.com/[/url]
[url]http://pixellight.sourceforge.net/website/[/url] (Looks good)
Features: [url]http://pixellight.sourceforge.net/docs/PixelLightFeatures.pdf[/url]

-------------------------

magic.lixin | 2017-01-02 00:57:37 UTC | #11

Renderering is not the only part of a game engine.
   To me, what I like urho3d engine most is that:
      1.  a c++ reflection system with generic variant attribute
            so you can do a lot of things with it,  your custom component can be edited quickly in editor, you can tweak values just like Unity3d without hard code anything.
            you can make your tools not only in c++, you can make it in c# or html, check the editor script code.

      2. a well designed resource system and resource hot-load system (plus !)
          so you can edit your resource in DCC tools with your engine running, you can event edit your game play script without close the engine and reopen it!
          
      3. variant event system
          you can send event with any typed parameter, the sender never needs to know each other with event handler.
          engine update is never called by function, just send event to the registered event handlers, that make subsystems decoupled with each other.
          
          plus: later delayed event handler support ?

    4. a good script intergration 
        angel script and even lua support !! (I`m using angel script cause I like the c++ like syntax)
        you can handle any event in your script code,  engine code is always engine code, script code will do the logic and game event handling.
        register your custom function is very easy.

    5. data driven render path.
        customize your render style but not modify the source code.

       All the features makes easy prototype and quick iteration. 

       Things I don`t like?
           too much memory allocation and deallocation every frame.

           every time construct and destruct a variantmap will do system malloc and free like: 

           VariantMap eventData;
           //.....
          SendEvent(xx, eventData);  
          
          in this case eventData`s lifetime is every short, I ended up with a walk around that, make eventData static like this
          static VariantMap eventData;
          //......
          SendEvent(xx, eventData);

         maybe a frame allocator or statck allocator is the best in this case.

         Too much string used( this also makes memory allocation too much), most cases string hash is good enough for for addressing or compare.
         But it`s not friendly for editor or debugging, so in my case, I add a global HashMap<StringHash, const char*> to store this information, if editor
         want to get the string just look up this table.

-------------------------

cadaver | 2017-01-02 00:57:37 UTC | #12

[quote="Hgdavidy"]
[url]http://pixellight.sourceforge.net/website/[/url] (Looks good)
Features: [url]http://pixellight.sourceforge.net/docs/PixelLightFeatures.pdf[/url][/quote]
I used to follow PixelLight for some time, unfortunately it seems they have ceased development.
[url]http://www.game-coder.de/page/pixellight?lang=en[/url]

-------------------------

cadaver | 2017-01-02 00:57:37 UTC | #13

[quote="magic.lixin"]too much memory allocation and deallocation every frame.[/quote]
Hi,
if you can supply non-destructive patches (ie. ones that don't change the API radically) for better memory allocation they are very welcome. Also if your profiling has revealed some specific hotspots due to allocation or string use you could file issues. I'm thinking that Context could handle handing out preallocated VariantMaps for each SendEvent nesting level.

-------------------------

Hevedy | 2017-01-02 00:57:37 UTC | #14

Cadaver the engine is multi-threaded ?

-------------------------

cadaver | 2017-01-02 00:57:37 UTC | #15

There's the WorkQueue subsystem, which is used for certain tasks, like splitting up animation/particle updates and culling between worker threads. You can also submit your own background tasks into that system but you basically have to be operating on your own isolated data, as the engine API itself is not safe to call from other than the main thread.

-------------------------

Hevedy | 2017-01-02 00:58:13 UTC | #16

More docs of render gi and others from crytek:
[crytek.com/cryengine/cryengi ... lumination](http://www.crytek.com/cryengine/cryengine3/presentations/cascaded-light-propagation-volumes-for-real-time-indirect-illumination)

-------------------------

jmiller | 2017-01-02 01:00:08 UTC | #17

Re. VariantMap, there is now Context::GetEventDataMap() used by much of the code, and working well in my own.
/// Return a preallocated map for event data. Used for optimization to avoid constant re-allocation of event data maps.
also available as Object::GetEventDataMap()

-------------------------

cadaver | 2017-01-02 01:00:08 UTC | #18

In the previous code the VariantMap object itself would be allocated on stack, but it would start to make heap allocations when you insert keyvalue pairs into it. Now that we reuse a single eventdata map most of the time, it also reuses its already allocated keyvalue elements without making new heap allocations.

-------------------------

magic.lixin | 2017-01-02 01:00:08 UTC | #19

[quote="Sinoid"][quote]Things I don`t like?
too much memory allocation and deallocation every frame.

every time construct and destruct a variantmap will do system malloc and free like: 

VariantMap eventData;
//.....
SendEvent(xx, eventData); 

in this case eventData`s lifetime is every short, I ended up with a walk around that, make eventData static like this
static VariantMap eventData;
//......
SendEvent(xx, eventData);

maybe a frame allocator or statck allocator is the best in this case.
[/quote]

Have you profiled? Could you maybe tell us a bit about your background?

I see a stack allocation. It's also static as far as the compiler is concerned. You are definitely not a better optimizer than the compiler is. Yes, there's construction effort and destruction effort - assuming the compiler didn't write all of that off, but this smells like something someone from Java or C# would say.

You called it a "malloc and free," you definitely don't have a C++ or even a C background beyond theoretical. It's a stack allocation, not a heap allocation. In theory that could be costly, but in practice, the compiler dumped everything that didn't matter.[/quote]


 ??) please check the constructor function of HashMap,  you will know what I mean.

-------------------------

Hevedy | 2017-01-02 01:02:16 UTC | #20

Check the Panda3D update:

[panda3d.org/blog/](https://www.panda3d.org/blog/)
[github.com/tobspr/RenderPipeline](https://github.com/tobspr/RenderPipeline)
[dropbox.com/sh/dq4wu3g9jwjq ... hWa?dl=0#/](https://www.dropbox.com/sh/dq4wu3g9jwjqnht/AAABSOPnglDHZYsG5HXR-mhWa?dl=0#/)

-------------------------

