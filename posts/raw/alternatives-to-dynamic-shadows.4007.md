Dave82 | 2018-02-11 22:43:57 UTC | #1

Hi ! After a hard work on horror style baked lightmapping i came to a conclusion that it is absolutely hard or impossible to match dynamic lights and static baked lights in a scene. In some cases works but in 90% of the situations standard lights (spot , point and directional) can't reproduce the dark ambience of a horror game level.The best way of lightmapping a dark horror level is using baked GI + AO + Object lights.(cylinder , plane shapes) and use dynamic lights only on dynamic objects.The  dynamic shadows should be faked by either a projected blob or some sort of stencil shadows.(For references see Resient Evil outbreak levels) 

1.Blob shadows. Unity has a component called Projector which projects a texture on a level  (There are tons of tutorials how to set up blob shadows for characters)
2., Use shadow casting lights. As i already mentioned in an another topic there should be a way of using lights for just cast subtractive shadows. In theory (maybe i'm totally wrong) it could be implemented as screen space shadows.

What you (Urho3d devs) think about this ? Is it doable ? i would be happy with solution 1 but i'm really interested in your opinion on the 2nd solution.? Any idea suggestion/help is welcome.

-------------------------

Sinoid | 2018-02-12 02:52:14 UTC | #2

> 1.Blob shadows. Unity has a component called Projector which projects a texture on a level (There are tons of tutorials how to set up blob shadows for characters)

I looked into this for deferred decals.

**A)** Unless it's already been changed the only obstacle there is just that the renderpath execution assumes there's only ever 1 *forwardlights* or 1 *lightvolumes* pass so there's nothing to match Lights up to different techniques (*a projector is just a light with different shading*).

Solutions are debatable. Multiple light passes? Lights with a *material* and sort-order key? Now what about `litalpha`?

> As i already mentioned in an another topic there should be a way of using lights for just cast subtractive shadows

-- insert pedantic *you do not subtract, because specular and stuff* bit here --

> 2., Use shadow casting lights.

**B)** If you wan't the light to still be a real light but don't want to render the shadow-map constantly you could tweak Light to be able to store and reuse a shadowmap instead of rerendering it every frame. 

**C)** Or just do the render from within the editor, invert the shadowmap, and save to a bitmap to use as a gobo for the light if it's a spot-light. The cubemap rendering in the editor already does the sort of work you'll need to do before you render and that's all automatable. Zero the edges of the image so there's no chance of leaks, ie. nuke seams from orbit. Bias might be problematic.

You'd have pretty good control either of those ways when it comes to rerendering the shadow map for changes (AMFP suddenly appearing pig masks, etc).

@sabotage3d might have already done the 1-time only render thing IIRC.

The other options are pretty out there though, like [LotF style accumulation buffers](https://www.slideshare.net/philiphammer/the-rendering-technology-of-lords-of-the-fallen) or tiled cone-tracing (Last of Us).

-------------------------

Dave82 | 2018-02-14 16:18:36 UTC | #3

[quote="Sinoid, post:2, topic:4007"]
insert pedantic you do not subtract, because specular and stuff bit here
[/quote]
That's not how horror level design should work..How will the player (and enemies) cast shadows in a dark corner which is only lit by indirect ligting bounced off of a wall from the other side of a room ? In old horror games (all resident evil games and silent hill games) was done by the player having a blob shadow under his feet or a subtractive shadow projected constantly from a certain direction.Absolutely independently of any dynamic lights in the scene.Even RE Remastered use this trick.
I'm really curious how this was done and how could be implemented in Urho3d ?

-------------------------

Dave82 | 2018-02-18 16:34:16 UTC | #4

Ok.So i have an idea how to do this : 
1. Create a projector component with similar properties like a light that renders the character into an image from the projector's point of view (a black background and a color value between 1.0f - 0.0f used for the character color)

2. When the whole scene is rendered , project this texture onto the level again from the projector's point of view using subtractive blending.

The problem with this i have no idea where to start because i still not familiar with the lower level of the engine.I could implement a projector component but there are few things that are unclear : 
   1 how to implement this into the renderpath so i get the best performance (clearly my solution takes one extra pass to render the whole scene.Hw skinning and instancing will be handled automatically if possible ?
   
The reason i'm asking this because without this i can't do proper shadows.Just look at the scene below.How i suppose to simulate lights like this with dynamic lights ? Even if i hack out something , in the dark areas where are no lights the dynamic objects won't have shadow.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/6/638d6bb5af53ed7e08e94743b28e3fc0e8ff78ee.jpg[/img]

-------------------------

Dave82 | 2018-02-21 01:35:17 UTC | #5

It seems that i can't work out any usable solution in a short time.Tried to draw a blob plane with alphamap on top of everything but that looks like crap if you're standing behind an obstacle. Is there a way to simply turn a spotlight into a projector (subtract the shape texture instead of add ?) I tried to modify the LitSolid shader in every possible way but i always end up in artifacts or no light at all.I want something like this.(shadow under player's feet)

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/4ab1d9dca43a5b5c3ad281bd317a6d511419a7b8.jpg[/img]

-------------------------

Sinoid | 2018-02-21 03:18:38 UTC | #6

> Is there a way to simply turn a spotlight into a projector (subtract the shape texture instead of add ?) 

Use a negative brightness multiplier, also use lightmask to keep it off things you don't want it on and don't let any highlight producing lights near it - negative brightness will use subtract mode. Has to use shadowmaps if you don't want it to cast past a box.

If hightlights touch it they'll get *sandblasted* into looking awful and there will be cut-off halos around the edges since it's a subtract blend. You still need to remove L of your lightmaps if you don't want the negative light to burn nonsensical shadows.

If you must mix with highlight producing lights, then tweak it to use a multiplying blend mode of the *One-minus* family (for 1-L instead of L) so the hightlights sharpen instead of being sandblasted down into a muddy gray mess of gross.

-------------------------

Dave82 | 2018-02-21 03:28:11 UTC | #7

Yes , yes , yes ! It works ! That's exactly what i was looking for.And without any engine modification ! Thanks man.You have no idea how much you helped :D And the coolest thing it could be conveniently combined with shadows and lights (masks).It may have some drawbacks but at first look it is perfect. 

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/0/0c3cf9895ab293c850c7c4afd89ea17245e95168.jpg[/img]

-------------------------

Sinoid | 2018-02-21 04:34:50 UTC | #8

Sorry about that, I didn't realize that all you wanted was a blobby drop shadow, I thought you were mentioning them just as a reference.

---

The code for negative lights happens in `Batch::Prepare()` for forward and `View::SetupLightVolumeBatch()` for deferred if you should end up needing to know where it all happens.

The drawbacks should be fairly moot if you're not using PBR, legacy specular is usually kind of muddy anyways so it won't be too noticeable there. For your uses you might not really care at all.

-------------------------

Dave82 | 2020-01-01 22:54:34 UTC | #9

After a long work and studying how Urho3d's renderpath/shaders and graphic things work i was able to hack out some cool things that may be useful to other people searching solutions for problems described above and lot more.
[b]1. The Depth only pass.[/b] 
It was an inveresting discovery that we can render objects into the depthbuffer only, Fake 3d depth in front of a pre rendered 2d background so parts of dynamic objects are overlapped by these invisible walls giving an illusion that the pre-rendered 2d shapes are really there . 
here's the result : (The whole scene including that shiny teapot in the middle is a pre rendered 2d image. The character is the only 3d element in the scene)
![image|690x413](upload://k2eheBvEVuUSgvPThPQwNbrfCJd.jpeg) 

However the solution i used only works with the extended prepassHWDepth renderpath and there are still some things that i don't understand why it works like it does, but in general , it works. 

[b]2. The projected shadows[/b]
It is actually a hack and a slight modification of the LitSolid shader to make this work, but finally it is WORKING ! Playing with shadow and light masks we can finally get perfect dynamic shadows in a pre rendered game. Let's see Unity does this :D So years of testing and practicing brought us this : 

![image|690x412](upload://vI4SFmPsPxMsmr48cC3tkfBfyUQ.jpeg) 

It is simply a trick using a light pass that has a multiplicative blending and in LitSolid shader i use a constant float3(0,1,0) (the normal passed in  GetDiffuse() ) vector to have the same light intensity on all faces so it doesn't ruin the prerendered lighting in the 2d background.

Why is this cool ? 
1. It perfectly fits in the existing renderpath. NO extra cameras , NO extra RTT !
2. It's not a cheap projector ! Woks fine with all light sources ! (Well there are some obvious problems with NON directional lights but can be fixed)
3. Very small amount of extra passes needed.
4. Shadows will look exactly how Urho renders them.
5. Very slight engine modification is needed (lights need extra shader param to know when to use contant normal vector).

Nice way to start the new year !
Happy new year everybody !

-------------------------

GodMan | 2020-01-02 16:59:59 UTC | #10

So you only got it working on deferred? Have you tried your changes on an environment that is better illuminated? I did something similar with multiplicative as well.

-------------------------

Dave82 | 2020-01-02 17:20:54 UTC | #11

My solution is working with prepassHWDepth only.

[quote="GodMan, post:10, topic:4007"]
Have you tried your changes on an environment that is better illuminated?
[/quote]
In that case the shadows would be brighter as it is expected. But since this is a 100% Urho compatible solution you can change the shadow intensity for darker or brighter shadows. The above image uses 0.5f for shadowIntensity

-------------------------

GodMan | 2020-01-02 17:56:38 UTC | #12

Let us know when you upload. I would like to test it for you.

-------------------------

GoldenThumbs | 2020-01-02 19:30:09 UTC | #13

> in 90% of the situations standard lights (spot , point and directional) can’t reproduce the dark ambience of a horror game level.

I disagree. Look at Doom 3. I feel it pulls off a horror atmosphere wonderfully and it only uses dynamic lights.

-------------------------

Sinoid | 2020-01-02 22:15:18 UTC | #14

`Dark ambience != dark`. The cabin above the shark-tank in the RE remake comes to mind as dark-ambience, it's lit but more gloomy glow than DOOM3's hard edges everywhere.

---

@Dave82 how fat is a single view (color + depth, etc)? Really love prerendered backgrounds, would love to see retro in the style become a thing.

-------------------------

Dave82 | 2020-01-03 00:41:04 UTC | #15

There are really no pre rendered engines out there at least no free, open source ones so this might be interesting toy for other old school enthusiast out there. And could bring in more Urho users/developers sooner or later. 

[quote="Sinoid, post:14, topic:4007"]
how fat is a single view (color + depth, etc)
[/quote]
Well if by fat you mean how much passes/layers are used , well there are a lot but with a standard (prepass / deferred etc) shading models there are no other solutions. At least i didn't found so far. Performance wise i didn't experienced any slowdowns even on an old GT 430 it runs perfectly fine

The rendering looks like this : 
after the base pass i render the occluders (z pass only) if the occluders can cast shadow there is an extra shadow pass (without a light pass) for each occluder so they can cast shadows on characters and other dynamic objects but not receive any light. 
Then there is a shadow caster light which only casts shadow on invisible occluders and use multiplicative blending  (this time dynamic objects use only a shadow pass but no light pass) Finally there is yet another light (same position and direction as the shadow caster but this affect only dynamic objects by illuminate them and cast shadow on each other)
The best thing is that i was affraid of how this will work with alpha passes ? Well , it works perfectly 

Even mixng the scene with additive lights is possible (imagine a flickering light like a fireplace or a short circuit illuminate and cast shadow in a pre rendered background scenario... it would be a really cool effect).

-------------------------

Sinoid | 2020-01-03 01:55:54 UTC | #16

I meant the prerendered backgrounds themselves in regards to fatness of storage, like if you're doing sliced layers, keeping a full Z-buffer from the pre-render, if each background is basically a full g-buffer, etc. 

I wouldn't expect rendering them to be a problem at all but storing and streaming them would probably get pretty interesting.

-------------------------

