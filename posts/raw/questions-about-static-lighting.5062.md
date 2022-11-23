GodMan | 2019-04-02 03:24:09 UTC | #1

I have a scene were the map or "world" uses lightmaps, and the dynamic objects are using a direction light. If I don't set the light mask for the map ,and the map uses the difflightmap technique. Does that dynamic light in the scene still affect the map even though it is using static lighting?

Some of my test appear to show that it is still affected.

-------------------------

Modanung | 2019-04-02 16:01:13 UTC | #2

I have no personal experience with this but I do know there is at least one topic about this which I could look up later.
Might make a nice wiki page. [spoiler]hintz0rs[/spoiler]

-------------------------

GodMan | 2019-04-02 16:15:06 UTC | #3

I believe the static meshes are still affected. If I turn of shadows for the static meshes it helps, because the shadows are in the lightmaps. But like in another topic on the forums dynamic objects can no longer cast a shadow on the static mesh. 

I feel like having the lightmaps is kinda pointless, because the dynamic lights are still affecting the static meshes.

-------------------------

Dave82 | 2019-04-02 17:36:38 UTC | #4

Lightmapped meshes are affected by lights by default. You have to use lightmasks to disable lighting.
Note : Once you disable lighting you automatically disable dynamic shadows too.

-------------------------

GodMan | 2019-04-03 02:50:10 UTC | #5

I have light mask set now. The only down side is that the character shadows no longer work on the light mapped mesh.

-------------------------

Dave82 | 2019-04-03 07:13:22 UTC | #6

Yes. As i said above you can't have dynamic shadows on lightmapped meshes. You can hack out some shadows by baking indirect lighting only and use dynamic lights for direct lighting. It requires a bit extra work to sync light intensity/radius/color to match your lightmap.

Edit : Here's how i did it. Only the GI and AO are baked , the direct lights are dynamic.
https://www.youtube.com/watch?v=xXQ3rJjRxCo

-------------------------

GodMan | 2019-04-03 15:45:31 UTC | #7

What is the point though? Your mesh would still be affected by dynamic lights other than a flash light I suppose. Just seems like the benefits of the light mapping would be lost.

-------------------------

GodMan | 2019-04-03 16:35:23 UTC | #8

What if I just use one directional light. Then just use baked shadows for the level. Then disable the level shadows.

-------------------------

Dave82 | 2019-04-03 17:31:09 UTC | #9

[quote="GodMan, post:7, topic:5062"]
What is the point though?
[/quote]
If you don't want any dynamic object to cast shadows on your lightmapped level then nothing.
Hovewer this will look absolutely bad and unrealistic (the players will look like they're floating in the air , physics driven dynamic objects won't fit in the environment without shadows)

[quote="GodMan, post:7, topic:5062"]
Just seems like the benefits of the light mapping would be lost
[/quote]
A lighmapped levels are completely useles because you loose : dynamic shadows , specular mapping , normal mapping , etc. If you don't need dynamic effects then it's fine , but if you want some of these effects then you must use the method i described in my previous post.

 

[quote="GodMan, post:8, topic:5062"]
Then disable the level shadows.
[/quote]
If you disable shadows the level will be still affected by your directional light.

-------------------------

GodMan | 2019-04-03 18:07:13 UTC | #10

I know if I disable the shadows for the static level, but still keep the one directional light, and use the baked shadows. Would this not cut some of the performance cost on the directional light on the level mesh.

-------------------------

GodMan | 2019-04-03 18:48:37 UTC | #11

I wonder how they did it in halo 2?? That game ran on the original xbox. They have character shadows on light mapped meshes.

![halo%202%20lightmaps|665x500](upload://ZGf11xKLHkInPVzquwgQSemjSN.png)

-------------------------

Dave82 | 2019-04-03 21:38:42 UTC | #12

[quote="GodMan, post:10, topic:5062"]
if I disable the shadows for the static level, but still keep the one directional light, and use the baked shadows
[/quote]

Unfortunately that will ruin your baked shadows. Elements that were casting shadows in your lightmapping process won't cast shadow by your directional light so the light will override all you baked shadows in the scene and your brighter areas will become even more bright (due the light's additive pass)
The only solution is as i described above. Bake indirect lighting and use dynamic lights for direct lighting.
There are no other options in Urho right now. AFAIK unity suffers from the same problem.
Another options would be projectors but Urho currently does not support projectors. You can turn lights into some basic projectors but they will have some issues which pretty much makes them unusable in complex scenarios

-------------------------

GodMan | 2019-04-03 23:12:00 UTC | #13

Well that's unfortunate. This makes me not want to port my radiosity normal mapping shader to urho3d that I made for Irrlicht3d a few years ago. 

@Dave82 How did they do this in the halo games ??

-------------------------

Dave82 | 2019-04-04 13:19:30 UTC | #14

[quote="GodMan, post:13, topic:5062"]
How did they do this in the halo games ??
[/quote]
I have no idea. Unfortunately i'm struggling with the same problem since the beginning so i absolutely understand what you feel... I did a lot of research about these things but there's no clear answer. AFAIK older PS2 games had some basic volume shadows which were projected onto static scene by subtracting the shadow color from the pixels they affect. This method is really great because shadows doesn't depend on light pass. Wherever you walk in your level , even in the darkest parts which are not reachable by any lightsources your chartacters/ dynamic objects will always cast shadows (since they are subtractive). 

The problem is : I have no clue how to implement something like this. I'm still very unfamiliar with urho's rendering pipeline. I wrote some basic shaders but for something like this we need someone who knows urho to it's bones and knows exactly how and where are lights/shadows calculated.

The topic was already discussed long time ago and there were no solutions since then.
https://discourse.urho3d.io/t/problems-with-lightmaps-dynamic-lights/1073


Also here's some info on projectors in Unity. Maybe someone could add something like this to urho3d.
https://assetstore.unity.com/packages/tools/particles-effects/dynamic-shadow-projector-35558

-------------------------

GodMan | 2019-04-04 15:17:20 UTC | #15

I'm going to look into this some more and see if I can come up with a working solution. I had looked into light probes, but I read that light probes don't handle shadows.

-------------------------

Dave82 | 2019-04-04 16:22:15 UTC | #16

Also here is some working solution someone made in irrlicht.
https://www.youtube.com/watch?v=NgFxZX7saTQ

-------------------------

GodMan | 2019-04-04 17:12:25 UTC | #17

I'm not so sure that will work? It does not say if the mesh behind the character is using static lighting. When I get time I am going to try some of these ideas. Can you find me some more info on the shadow volumes you mentioned above. I believe in the documentary on Halo 2 they mentioned the pelican generating massive shadow volumes. If I can get just shadows for the character I would be okay with just that.

-------------------------

Dave82 | 2019-04-06 12:49:40 UTC | #18

[quote="GodMan, post:17, topic:5062"]
It does not say if the mesh behind the character is using static lighting.
[/quote]

Yes it does. That is a lightmapped quake3 level. The only thing he should do is disable dynamic shadows on the level and it should work. The character would cast a subtractive shadow on the lightmapped level.
To implement something like this would require to rewrite the whole engine to it's core so i don't think anyone will do it.

-------------------------

GodMan | 2019-04-06 16:34:46 UTC | #19

Well I was hoping to just modify some shaders, and change some passes, but if it really requires a engine rewrite then I suppose I want bother then.

-------------------------

Dave82 | 2019-04-06 21:19:42 UTC | #20

Well all i can do is add some advice about this.(This is how i would do if i knew the engine)
1. Draw everything that is static (with all default urho passes no modifications needed)
2. Draw dynamic objects from your "shadows only light" point of view using a RTT with black color as background and a shadow color as the object diffuse.
3. Repeat this process for all your "shadows only lights" in the scene.
4. Transform these RTT's into your camera's current frame (Pretty much the same way as Urho's light work) Use the depth buffer to project the RTT onto the scene using subtractive blending.
5. Draw dynamic objects.

This way static lightmaps should be untouched but still have projected shadows. I don't know how to do something like this but maybe it is possible with some renderpath and built-in shader modifications.

EDIT : This could be a pretty fast process since you don't need depth buffers for stage 2 and "shadow only lights" do not need to render the static scene which would be a extreme speedup...

-------------------------

GodMan | 2019-04-07 16:38:02 UTC | #21

![Screenshot_Sun_Apr_07_11_12_32_2019|690x291](upload://jIvxyTYpNqQRKVxoraMy7zj97hy.jpeg) 

Bloom seems to ruin the darkness from the shadows.
Maybe be the sRGB doing this.

-------------------------

