dakilla | 2017-01-02 01:15:21 UTC | #1

Hi

A topic to quickly share screenshots from your projects wip or works using urho3d.
I can't wait to see cool graphics using this great engine :wink:

-------------------------

magic.lixin | 2017-01-28 14:09:20 UTC | #2

https://www.youtube.com/watch?v=zdj2sudU4jE

-------------------------

dragonCASTjosh | 2017-01-02 01:15:22 UTC | #3

I dont think i will beat having life is strange in Urho, but i do have some work to show. I have been working on improving Urhos renderer as many of you know, recently i started work on Sub-Surface Scattering that can be use on many many materials including skin. Here are some images of my work.

[img]http://i.imgur.com/E5jclf4.jpg[/img]
[img]http://i.imgur.com/HoD50RM.png[/img]

-------------------------

ghidra | 2017-01-02 01:15:24 UTC | #4

[url=http://imgur.com/GbnnSoA.png][img]http://i.imgur.com/GbnnSoA.png?1[/img][/url]
[url=http://imgur.com/mV2EF97.png][img]http://i.imgur.com/mV2EF97.png?1[/img][/url]
[url=http://imgur.com/1lWcyU5.png][img]http://i.imgur.com/1lWcyU5.png?1[/img][/url]

-------------------------

dakilla | 2017-01-02 01:15:26 UTC | #5

@magic.lixin: really cool
@dragonCASTjosh: you make an awesome work
@ghidra: strange, what's that ?

A particle editor with emitter hierarchy I'm workin on:
[img]https://s14.postimg.org/d6vfc7w3l/Capture_du_2016_12_02_20_17_50.png[/img]

-------------------------

Lumak | 2017-01-02 01:15:29 UTC | #6

@dakilla, I like the idea. How's your progress?

-------------------------

dakilla | 2017-01-02 01:15:30 UTC | #7

Most parts are done... It remains to finish the editor and tune all  :wink:

-------------------------

godan | 2017-01-02 02:11:05 UTC | #8

We are hard at work on a new IOgram release. A few of the recent successes:

Runs great on linux! And you can target Linux in the build system...
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/49a6e31efc013d6c6089931540da2dd438cbf75d.jpg[/img]

Same with OSX, although the Retina thing has proved a bit of a challenge. Found a fix, though.
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/24ef2323542bbe17d8addd22c2bab8a1e3c08349.jpg[/img]

Sweet new LineRenderer:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/cf046e143c2fde0af6bacf207ea6bf57ae41e2f8.jpg[/img]

-------------------------

cosmy | 2017-01-28 11:31:46 UTC | #9

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6772d01eab54c1db628941c3f8399af937771a93.png" width="690" height="401">

Working on a Debug UI

-------------------------

cosmy | 2017-01-28 11:36:20 UTC | #10

@godan Did you use the standard Urho3D UI?

-------------------------

hdunderscore | 2017-01-29 02:58:39 UTC | #11

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0b430436c964660588972739fc3793fb5a9ab77b.png" width="690" height="373">

Some shader work I have recently started working on again.

-------------------------

godan | 2017-01-29 18:12:44 UTC | #12

@cosmy yep, urho ui all the way.

-------------------------

JTippetts1 | 2019-05-23 13:20:00 UTC | #13

After a months-long hiatus, I've started working again on my game, [Goblinson Crusoe](https://www.gamedev.net/blog/33-why-you-crying/) which is a turn-based RPG taking place on a hex grid. You play the role of a young goblin wizard apprentice working to pass your trials and become a full-fledged goblin wizard. Some shots:

![Object Highlighting](upload://1ttptzWtigQhboUYdUoDHPQY81q.jpg)
![Game Start](upload://60K91yHXBR8Ecz0LKn4cEnBvIDH.jpg)
![Three-way Brawl on Bridges](upload://n7nDfb9NlLTw0A44hVZR1GjLg0E.jpg)

-------------------------

hdunderscore | 2017-01-30 20:05:40 UTC | #14

That's looking pretty good.

Looks like the lights are burning the textures though, I'd suggest looking at loading textures with sRGB=true and then maybe using gamma correction post process.

-------------------------

hdunderscore | 2017-01-31 10:48:13 UTC | #15

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/84da0e2bd414b7a97071bce44e6fe68f0977eedc.png" width="690" height="373">
Added a metallic effect with screen-space IBL.

-------------------------

Liichi | 2017-01-31 16:02:52 UTC | #16

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/54d24fd7b1e048b92cc8d8f20b355c7b25b058e7.png" width="690" height="358">

-------------------------

Liichi | 2017-01-31 16:05:00 UTC | #17

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/e6929beaeea899aa368f0ad09e43e35154971aa6.png" width="690" height="358">

-------------------------

hdunderscore | 2017-02-13 18:57:42 UTC | #18

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/12b974f82292e69f9d7634060b07fb16a0bd6770.png" width="690" height="373">

-------------------------

hdunderscore | 2017-02-27 07:58:50 UTC | #19

Experimenting with vector field terrains, I wrote an export script in blender to export sculpted terrains into vector field texture, and made some hacks to urho terrain to load them (incomplete progress):
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6dff884a4c83e487915d134c3ce7bc3522291992.png" width="256" height="256">
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0971ae21996bfeed17a4e45068ec82bab36e0743.png" width="690" height="373">
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/154d6a2ff4e152a872b7ff780b207bf141f92509.jpg" width="690" height="388">

-------------------------

TheTophatDemon | 2017-02-28 02:34:50 UTC | #20

I'm working on an FPS where the guns fire automatically and your goal is to not shoot people. I'm kind of aiming for Quake II graphics so I can finish the game eventually, but I have this neat thing going on with the diffuse shader that makes it look kinda cartoony.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/76b3d442aab9bc5f210e366b869a849c9b0dc71d.png" width="690" height="388">

-------------------------

hdunderscore | 2017-03-02 15:14:06 UTC | #21

Reduced the restrictions on the blender exporter, now designing terrains is much more practical.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/eec6571d2837f2c46ef1d532a834a841e152037b.jpg" width="690" height="373">

-------------------------

hdunderscore | 2017-03-16 12:34:01 UTC | #22

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ded955dc0334898f8e64899fe0d4e7a63019f905.png" width="690" height="373">
I was finding blender a little on the slow side to work with on larger resolutions, so I started experimenting with my own in-urho terrain editor that mimics blenders modifier stack, with optimisations directed at working with terrains. At first I implemented it in angelscript, now I've moved the main parts to C++.

So far I have a basic fractal terrain generator, a 'hook' displace (ala blenders hook to vertex), a road excavator, smoothing and also toyed with using physics to erode terrain.

-------------------------

godan | 2017-03-16 15:06:35 UTC | #23

Prototype of Urho's Navigation mesh and Crowd manager system in IOGRAM:

https://youtu.be/5UAC6sbeYV8

-------------------------

GoldenThumbs | 2018-06-13 04:43:26 UTC | #24

Dang, I feel less original now...

-------------------------

GoldenThumbs | 2018-06-13 11:30:31 UTC | #26

I'm working on a survival fps with old-school shooter elements. Very early in development though. I say I'm not original because I'm going for an artsyle similar to your other thing.![Arcadius_EarlyDevSceenshot0|690x388](upload://fbNU6zSgwarS6AN9SROUmy8TQvM.PNG)

-------------------------

GoldenThumbs | 2018-08-16 00:35:50 UTC | #27

Something more up-to-date on the project.![Arcadius_EarlyDevSceenshot3|690x388](upload://z2kSr6lhFqyDGd4lWccY8dEAhM3.png)

-------------------------

rku | 2018-09-29 08:37:07 UTC | #28

https://youtu.be/11QDmTOkq38

-------------------------

TrevorCash | 2018-09-29 21:25:01 UTC | #29

Super awesome to see this in action!

-------------------------

rptr | 2018-10-03 20:10:47 UTC | #30

![Screenshot%20at%202018-04-20%2023-09-16|690x428](upload://r0xqtEUmy9e8VisJIGanZZiNFX6.png)

-------------------------

Sinoid | 2018-10-05 02:32:43 UTC | #31

@rku, I've lightened my attitude a bit and the dump @ https://github.com/JSandusky/Blocks is MIT'd, lift whatever you want from it if there's anything useful to you there ... though it's like 50% robot generated so yeah ... whatever you can get from it great.

I'll update the dump in a couple of days, after I've trimmed out the stuff I care about and that won't work in anyone's repos but my own.

I've abandoned the approach I took there and now regard docking as a bullshit excuse to let poor UI slide under the guise of customization. Current reincarnation is like Akeytsu mashed with zBrush ... though I still stick with WPF for the stuff I sell.

-------------------------

Modanung | 2018-11-22 01:37:02 UTC | #32

https://vimeo.com/293830077

Progress video of [A-Mazing Urho](https://gitlab.com/luckeyproductions/AmazingUrho), the LucKey Productions entry for the [Open Jam 2018](https://discourse.urho3d.io/t/open-jam-2018).

EDIT: And another video...

https://vimeo.com/301056456

-------------------------

Sinoid | 2018-11-19 03:15:36 UTC | #34

NoesisGUI implementation (drawn overtop of ImGui here).

![image|690x418](upload://oytm08jRzLkPBI2vYiWF4hLq1vg.png) 

Has not been fun, quite painful actually with interfaces for this and interfaces for that and whole lot of *"nope, you really have no idea WTF anything is ... so query and pray it's there"*.

Still a ton to do with it before it's plausibly usable - even then, I don't see how it's mappable to any *generic use* with MVVM/extension registration and the like plus the extra steps in making Blend and the runtime coherent.

-------------------------

Elendil | 2018-11-26 16:08:29 UTC | #35

Hi [Sinoid](https://discourse.urho3d.io/u/Sinoid), do you have your project on github? I tried integrate Noesis GUI too in to Urho, but I am not successful. How you render gui? You use NoesisRenderDevice or you create cusom?

-------------------------

Sinoid | 2018-11-27 03:24:55 UTC | #36

@Elendil

I've only implemented for DX11, so I don't know what I'll face should I try for OpenGL (which I never ever will).

The biggest thing was GPU-state. Noesis' prewritten renderers do not save or restore state. To do that I lifted the state save/restore from the DearImGui implementations. I call a SaveGPUState before Noesis does anything and I call RestoreGPUState function after Noesis does offscreen rendering and primary rendering.

That's in a loop because right now I support multiple views, basically it's:

    Save GPU State
    foreach view
        view -> UpdateSize
        if view needs offscreen render?
            view -> Render Offscreen
            Restore GPU State
        view -> Render
        Restore GPU State
    end foreach

**Noesis Renderer**: I used the example `D3D11RenderDevice` from the NoesisApp sources. I just changed it to not have any ID3D11Device/ID3D11DeviceContext ownership - it receives them from Urho3D - all functions for creating/disposing those is removed.

**Noesis Interfaces**: pretty crude, I construct them with an Urho3D context so they can access the ResourceCache. Textures always go through the wrapper API as in the Noesis D3D11 example (wrap the native handle).

**Urho3D::Graphics**: I had to modify `Graphics::ResetRenderTargets` to force a rebind to defaults. The current implementation is *soft*, I forced `impl_->renderTargetsDirty_ = true;` inside of the function to make it *hard*.

**Input Handling**: still a work in progress, just mouse at the moment - more concerned with data/view management right now.

**View management**: really crude, `XAMLGui` is a Subsystem (like ResourceCache) that is used to construct `XAMLView` instances. Those views have a few helpers for storyboards, setting the root datacontext, etc. Otherwise it's all still early and raw.

I'm doubtful that it's really possible to do outside of an extremely raw setting, it's GUI though - there is no such thing as generic GUI. Angelscript bindings do look to be hell though.

**Building**: Noesis has a completely psychotic SDK folder layout, I use Premake so my build is not relevant to anyone using CMake, however. The stuff I use from the NoesisApp/example sources is straight copied over rather than referenced because the paths are stupid nuts (`D3D11RenderDevice`).

-------------------------

rku | 2018-11-28 16:10:35 UTC | #37

Progress. C# fields for subclasses of `Serializable` are automatically exposed to editor and included in serialization. 

https://www.youtube.com/watch?v=27uNO3CD09M

-------------------------

Dave82 | 2018-11-28 19:09:46 UTC | #38

Cool rain and dynamic light effects :D No special shaders just Diffuse texures and the character uses a DiffSpecular with a slight specular power.
EDIT : Except the Color correction / desaturation fullscreen shader i'm using

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/5b19ac34ca814dcc1817f9aa6f4e9d6fab095baa.jpeg'>

-------------------------

Sinoid | 2018-11-29 03:21:16 UTC | #39

@Dave82 nice as usual

---

Starting to put that CivetWeb dependency to work for something other than websockets, embedded info server:

![Resource_Cache_Content_-_Mozilla_Firefox_2018-11-28_21-25-37|427x500](upload://huVphvHtiBACqKiQetLAfRziv79.png)  

Not planning to do anything crazy with it, really just about being able to serve Image/text-blobs up for diagnostics on demand with some basic querying, attribute editing at the absolute maximum.

I'm absolutely horrid at web development anyways and CivetWeb runs connections in threads which locks a lot off (angelscript debugging only works because it freezes things), so I can't go bonkers.

-------------------------

dakilla | 2018-11-30 06:07:59 UTC | #40

[rku](https://discourse.urho3d.io/u/rku) Nice, your editor looks very good. can it be launched as an in-game editor ? do you have a base version that works with the original urho3D ? I'd like to integrate it independtly of your engine fork.

-------------------------

GodMan | 2018-11-30 18:55:20 UTC | #41

![screenshot|690x291](upload://vPdc4usr1rkgdOIKciWYoonoBkO.jpeg)

-------------------------

Don | 2018-12-01 01:21:39 UTC | #42

I like the look of that a lot! Where's it heading?

-------------------------

GodMan | 2018-12-01 03:59:00 UTC | #43

Now that I have more free time. I'm going to try and make a better environment.

-------------------------

rku | 2018-12-02 09:39:57 UTC | #44

> can it be launched as an in-game editor ?

Editor is a wrapper around the game, not the other way around. You can launch your game inside editor much like in unity. Of course it is way easier to crash editor from your own code because c++ and because engine was not designed with this functionality in mind. Not a big deal though, because editor starts fairly fast and it is no different than debugging your game without editor and crashing it.

> do you have a base version that works with the original urho3D ? I’d like to integrate it independently of your engine fork.

There is an older standalone version that i ported from my fork. https://github.com/rokups/Urho3D-Toolbox
It was not updated for a long time and i do not intend to continue on it. This is both because dealing with build system of upstream Urho3D is annoying and because at times changes are needed to the engine to make certain things work (C# especially). Also i have zero desire to deal with manual script integration of upstream Urho3D, especially angelscript.

-------------------------

Sinoid | 2018-12-08 01:50:17 UTC | #45

Worked a bit more on the embedded server thing today:

![image|382x499](upload://c6cHxGGwPFJKA8UQ6LK8rG4tpSN.png) 

Scenes/Nodes/Components are inspectable (not all fields editable, not sure if they all should be), 

![image|382x499](upload://2eF5zfnafZkYWCmHvkNEnZbyT5U.png) 

Lambda commands can be registered (run in E_BEGINFRAME) in addition the existing text/image publishing.

---

Only a few fingers of things left to go and I'll toss it onto github (just "*wow, I really botched that*" stuff).

-------------------------

GodMan | 2018-12-12 18:43:38 UTC | #46

![demo|690x291](upload://gKzIQHBuC8FB3rO5EevGhqJetN5.jpeg) 

Demo with halo 2 masterchief. Has controls for running, jumping, moving left,right, and backwards.

-------------------------

GodMan | 2018-12-21 07:03:40 UTC | #47

![Untitled-1|690x291](upload://vKTZOT0fv1iSn1hB4FCbU8sfd5d.jpeg) 

Physics Fun

-------------------------

GoldenThumbs | 2018-12-21 22:13:26 UTC | #48

Making a halo fan game? Or is this all just tests?

-------------------------

GodMan | 2018-12-21 23:08:44 UTC | #49

Yeah fan game lol. I was always a big fan of halo ce, and halo 2. I use to mod them on halo ce, so I know the models, and animations very well. Also 3d max like the back of my hand.

-------------------------

GoldenThumbs | 2018-12-23 01:57:58 UTC | #50

Cool, let me know if you need anything graphics related (art, shaders, etc.). I've been practicing and giving out my work when I feel it's ready.

-------------------------

GodMan | 2018-12-24 08:38:31 UTC | #51

![Untitled-1|690x291](upload://b64hsgGzv9vORV4AyIuPGrpY4on.jpeg) 

Added proper color changing to the default shaders that come with urho3d. This allows you to set any color for a character based off a texture lookup that defines the areas of a texture that you want to be affected by color change.

-------------------------

GodMan | 2018-12-30 16:20:41 UTC | #52

Custom passes for skies.

![Untitled-1|690x291](upload://2HE5iRxZfu026IU6t1QxY1ru0l5.jpeg)

-------------------------

GoldenThumbs | 2018-12-30 22:47:45 UTC | #53

Very cool! Aside from colors being a bit washed out this is looking really nice.

-------------------------

GodMan | 2018-12-31 00:34:53 UTC | #54

I think some of that is due to the hdr, and eye adaptation effect. Some of the background items are lacking there detail textures. I have not made a shader for this yet.

-------------------------

GodMan | 2018-12-31 13:58:14 UTC | #55

Added new blending modes to urho3d. I used them to blend the stars in the sky model. I also tweaked the AutoExposure, and HDR. They still look the same to me I could be wrong.

![Untitled-1|690x291](upload://o9BoVyyNkYNNrI6d1tUVmvYFS6h.jpeg)

-------------------------

GodMan | 2018-12-31 15:58:16 UTC | #56

Added detail textures for the bland look on some things. This helped the tone mapping grey-out affect on some things in the scene.

![Untitled-1|690x291](upload://bHZjQ6y4HpqL6M3JGo5mep5olxD.jpeg)

-------------------------

smellymumbler | 2018-12-31 16:45:31 UTC | #57

How did you do detail textures? Really cool!

-------------------------

GodMan | 2018-12-31 17:10:17 UTC | #58

I just extended the shader that comes with Urho3d. Then you call the custom pixel shader define for that particular material that is using the detail texture.

-------------------------

GodMan | 2019-01-01 15:12:26 UTC | #59

@smellymumbler Do you want the code? It's for HLSL though. It can easily be applied to GLSL.

-------------------------

smellymumbler | 2019-01-01 21:26:31 UTC | #60

That would be great! Did you follow any tutorial or article?

-------------------------

GodMan | 2019-01-01 22:40:50 UTC | #61

No. I have a lot of experience with shaders from my time working with Irrlicht Engine.

-------------------------

GodMan | 2019-01-02 22:57:56 UTC | #62

Here is a demo of my crappy rocket launcher.
[Rocket Launcher Demo](https://youtu.be/6CWsEUnHTNo)

-------------------------

GodMan | 2019-01-05 18:33:38 UTC | #63

Added multiplayer emblems:
![multiplayer_emblems|690x291](upload://cZA84PYpFVlkidgM201dTaFCggv.jpeg)


@smellymumbler

Here is the code for the LitSolid.hlsl shader. Make sure you are using forward rendering otherwise this will not work.

    // Get material diffuse albedo
        #ifdef DIFFMAP
            float4 diffInput = Sample2D(DiffMap, iTexCoord.xy);
            #ifdef ALPHAMASK
                if (diffInput.a < 0.5)
                    discard;
            #endif
    		float4 diffColor = cMatDiffColor * diffInput;
    				#ifdef CHANGECOLOR		
                                   // Removed this code becuase you don't need this part.
    				#endif
    				#ifdef DETAILNOCOLORCHANGE		
    					float4 detail = Sample2D(detailMap, iTexCoord.xy * 32.0f);
    					diffColor = cMatDiffColor * Multiply(diffInput , detail);	

    				#endif
        #else
            float4 diffColor = cMatDiffColor;
        #endif


Put this in your material file:
`<shader  psdefines= "DetailNoColorChange" />`

-------------------------

zedraken | 2019-05-23 13:20:03 UTC | #65

![](upload://lFnwTIk8DGowWc6bumNUPQJIOaw.jpeg)

-------------------------

GodMan | 2019-01-08 21:15:17 UTC | #66

@zedraken

Are you using HDR?

-------------------------

zedraken | 2019-01-09 06:27:51 UTC | #67

No, I do not use HDR. In fact, I have never used it and may be I should look out at what it is exactly and how can I set it up.
If you have already used HDR in images, I can be interested to have your feedback.
Thanks!

-------------------------

GodMan | 2019-01-09 15:43:58 UTC | #68

I've used HDR in Urho3d, but not hdr images such as an hdr skybox.

-------------------------

Modanung | 2019-01-09 22:14:03 UTC | #69

Know [HDRI Haven](https://discourse.urho3d.io/t/hdri-haven-opening-up/3799) if you do.

-------------------------

GoldenThumbs | 2019-01-10 18:59:59 UTC | #70

Love that site. It's great

-------------------------

glebedev | 2019-01-12 18:37:53 UTC | #71

https://www.youtube.com/watch?v=RyDREqWJAyE

-------------------------

glebedev | 2019-01-19 15:55:36 UTC | #72

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/a55ba905608b031a47824719c1f913a4c577f552.jpeg'>

-------------------------

GodMan | 2019-01-20 21:35:21 UTC | #73

Fixed HDR greyout effect. Also added a cheap shield effect. It's hard to see it animate in a picture though.
![Untitled-1|690x291](upload://ehkQnvBk62pS7yYQvNy7G0IO4HZ.jpeg)

-------------------------

Dave82 | 2019-01-23 21:02:51 UTC | #74

Just finished my navmesh based pathfinding system. I currently gave up on Recast because it handles things very strangely.Also i ran into problems every time i rebuild recast navmesh the detour crowd becomes invalid (the internal crowd_ pointer is null for some reason.) So i picked up my clunky navigation , polished it and this is what i have so far.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/a171584f4bf8d11a281ff6b4bc747a2b32cd699c.jpeg'> 

The purple line is the path , the red lines are the bounding edges.Works so far , i tried it with very complex zig-zaggy mesh and always worked flawlessly. Some diferences between Recast an mine : 

- Works on XZ plane. No slopes and other unrealistic crap. The pathfinding is done in 3d but the final Y is decided by the level geometry not the navmesh.
- Automatically picks the closest layer to the character feet. With Recast i had some issues if the enemy is slightly above the navmesh it just doesn't work anymore (probably i miss some setting)
- I use the real mesh when i build the nav mesh and keep the distance from walls corners by pushing the path points towards normals using the NPC/ Character radius. As i see Recast does this totally the opposite. Builds the navmesh by pushing the navmesh points using the radius. This could led to a problem if the mesh has narrow paths the navmesh is not built (no enough space). Both solutions lead to the same pitfall except in my version i have full controll what happens if the NPC is off navmesh.

So all in all if i can't get the steering working properly i will most likely return to Recast but i just  want to try something new. :D

-------------------------

QBkGames | 2019-01-24 03:32:13 UTC | #75

We should also consider updating the Recast/Detour library to the latest (stable) build which could have useful bug fixes and improvements. I (might be wrong but I) suspect it hasn't been updated in a while. Might be more efficient than reinventing the wheel.
It's cool though that you have know-how to write your own pathfinding system :+1:.

-------------------------

GodMan | 2019-01-27 04:08:03 UTC | #76

So your saying I should use your project lol.

-------------------------

Dave82 | 2019-01-27 06:26:04 UTC | #77

Haha . The "project" (if we can even call it that) , is far from usable. The pathfinding works nicely but still struggling with realistic path smoothing and collision avoidance...

-------------------------

GodMan | 2019-01-28 00:04:52 UTC | #78

Ah I see. Smoke and Mirrors.

-------------------------

GodMan | 2019-01-28 00:06:59 UTC | #79

![Untitled-1|690x291](upload://99JLKvHg5JJjQBjboQOeEO4Obur.jpeg) 
Play as the bogeyman from SilentHill.

-------------------------

Modanung | 2019-01-28 10:34:39 UTC | #80

Working on Masterchief vs. Bogeyman? ;)

-------------------------

GodMan | 2019-01-28 17:24:13 UTC | #81

LOL. No just a bunch of character demos.

-------------------------

GoldenThumbs | 2019-03-29 22:37:10 UTC | #82

Working on a comic book shader. Adds some nice crosshatching. Everything is per-pixel so you can use this with normal maps and specular highlights.![Monster_Inky_3|690x408](upload://edD172Ajuzyj8gUlLuPAMUdaHBM.png)

-------------------------

Leith | 2019-03-30 03:44:25 UTC | #83

Pretty cool - "Sin City" style. It's quite a unique look with the cross-hatching. Very lo-fi comicbook. I like it :)

-------------------------

Pencheff | 2019-03-30 13:59:32 UTC | #84

Slightly different usage of the engine - a video player :)
![video-player|690x404,75%](upload://x4WOVyrWs6sZxw3OlulZx3v1RJU.jpeg)

-------------------------

GoldenThumbs | 2019-03-30 17:52:29 UTC | #85

Now I have an outline post processing shader. Kinda looks like Borderlands now.![PNG|690x468](upload://kk4hTESAlWORpYndW1AePTgXKRV.jpeg)

-------------------------

glebedev | 2019-03-30 18:31:02 UTC | #86

https://youtu.be/yhGjCzxJV3E

Something to consider ;-)

-------------------------

Dave82 | 2019-03-30 23:14:22 UTC | #87

@Pencheff  
That looks awesome. May i ask which library did you use ? Urho really needs a video player...

-------------------------

Pencheff | 2019-03-30 23:57:14 UTC | #88

Its my own library for playing videos, sadly I cannot share it since its my company proprietary code. Its using FFmpeg (LGPL version) with hardware decoders where available. Its actually not that big of a deal to make one, but there are plenty of pitfalls I was stuck on while developing it, especially the Linux and Android versions. FFmpeg license would not fit with Urho3D, however.

There's this tho: https://discourse.urho3d.io/t/video-playback-example/3694.

-------------------------

glebedev | 2019-03-31 07:26:51 UTC | #89

On android you can play a video into texture via media player.

-------------------------

green-zone | 2019-03-31 11:10:56 UTC | #90

Very good shader
Exist a chance to see shader code?

-------------------------

GoldenThumbs | 2019-03-31 15:13:01 UTC | #91

Sure, when I feel like they are good enough. Which one would you like to see? The outlines post effect or the material shader for the crosshatching?

-------------------------

green-zone | 2019-03-31 16:37:54 UTC | #92

Totality, but preferably crosshatching part
It look like ink graphics.

-------------------------

smellymumbler | 2019-03-31 19:47:01 UTC | #93

The outline effect is really good. Can you apply AA only to it?

-------------------------

GoldenThumbs | 2019-03-31 19:48:55 UTC | #94

Worth a shot.If you want to test the renderpath out you can get it here: https://github.com/GoldenThumbs/Urho3D-Toon-Shaders

-------------------------

green-zone | 2019-03-31 20:29:19 UTC | #95

Many thanks
I need to complete current work to experiment with it.
But fantasy already began to play 
Thank you once again.

-------------------------

green-zone | 2019-03-31 21:31:48 UTC | #96

Yes, it work for my.
I need time to experiment with it.
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/e/e962a7897d35e93cc3efda5630216e300d7ee25d.jpeg'>

-------------------------

GoldenThumbs | 2019-03-31 22:30:01 UTC | #97

Bit of an update to this: Switching from a forward renderpath to a deferred renderpath. Makes my life easier and it also gives better results.

-------------------------

green-zone | 2019-04-01 06:32:23 UTC | #98

[quote="GoldenThumbs, post:97, topic:2431"]
Makes my life easier
[/quote]
I can not confirm. In Deferred mode I get such result:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/458ed8cf57a2eba5db608154e159b3a2aea5d979.jpeg'>
There are not shadows
When I comment addition of Outline.xml shadows exist, but no crosshatching.

-------------------------

green-zone | 2019-04-01 07:45:55 UTC | #99

Forward without Outline
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/f/fc45d18aafe5014f921a10553dcac053f64ad222.jpeg'>
Forward with Outline
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/7/701d9bec713fdc92d10c5c0d60c4ddb472579280.jpeg'>
Deferred without Outline
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/16a74744ab1e119b705f40ededb871249292a552.jpeg'>
Deferred with Outline
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/6/69160147a31dc9a6be493af7a9321b3eb7a327a5.jpeg'>
With small (default character demo) 
Camera SetFarClip distance (for Forward and Deferred):
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/1164facaaf753a83a1ae4773f016667339312add.jpeg'>

-------------------------

GoldenThumbs | 2019-04-01 17:02:11 UTC | #100

Some of these issues are because I was calculating normals from the depth map in the outline shader. Using deferred (well, prepass now because I was having a few small issues with deferred. Could probably figure it out.) I have access to an ACTUAL normal buffer. That makes calculating outlines way easier and less buggy.

-------------------------

GoldenThumbs | 2019-04-01 17:04:16 UTC | #101

Also: Did you convert the outlines to a post effect? Outline.xml is a modified forward renderpath.

-------------------------

GoldenThumbs | 2019-04-01 17:13:53 UTC | #102

And the outline material wouldn't work with deferred because (as far as I'm aware) deferred calculates lighting inside the renderpath instead of inside the material. I made that material for forward since (at the time) I didn't want crosshatching on everything. since I am now using a prepass renderpath (which still calculates lighting in the renderpath) I now am also doing the crosshatching in the renderpath.

-------------------------

green-zone | 2019-04-01 17:26:37 UTC | #103

[quote="GoldenThumbs, post:101, topic:2431"]
outlines to a post effect?
[/quote]
Added to renderpath that by default (Forward, Deferred) like posteffect.
Now I replaced default (Forward, Deferred) renderpath with Outline.
He looks as "Forward with Outline" (see screen above)

-------------------------

