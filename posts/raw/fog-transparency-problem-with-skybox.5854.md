dev4fun | 2020-01-30 07:10:48 UTC | #1

Hello,

I am trying to add skybox into my scene, but looks the Zone fog is buggy. Its always opaque, that doesnt makes sense for me, coz the result is very ugly.

![](https://puu.sh/F5dtZ/9dee70ed20.png)

As you can see, the distance fog isnt setting a transparency. I already tried to set Fog color for 0,0,0,0, but didnt work. I already tried to change the pixel shader part, but when I set some alpha value, didnt work too.

How I can solve this problem? I am using OpenGL, already tried with Directx, same issue.
Thanks.

-------------------------

Eugene | 2020-01-30 08:28:07 UTC | #2

[quote="dev4fun, post:1, topic:5854"]
that doesnt makes sense for me
[/quote]
How "transparent fog" is supposed to work from technical point of view? You cannot magically transform opaque material into transparent one. And even if all your materials are transparent, transparent fog color will _not_ look like what you want.

If you want to get "skybox-colored" fog, you have to sample skybox texture in every single shader and use this sampled value instead of fog color.

Or you have to run separate post-processing and blend final image into skybox basing on depth.

Both options are not cheap at all. I don't know any game engine that has transparent fog as you described.

-------------------------

dev4fun | 2020-01-30 19:10:06 UTC | #3

On forward rendering I expected the sky box it's the latest thing being drawn, this way, if I set some alpha value on any object at pixel shader color, I thought that alpha should be applied on scene, but isn't. (Something like DiffAlpha).

What I said about transparency fog is something like I did on my rendering engine:
https://puu.sh/F5mYC/6295b385d7.png

As you can see, objects that r far away, an alpha value is applied on pixel shader. I do this on this way:

	//Shaded Color
	float4 shadedColor = textureColor + specular;
	float transparency = DiffuseColor.a - ApplyDistanceFade(input.viewPosition, FogEnd);
	
	//Apply Diffuse Color
	shadedColor *= DiffuseColor;
	
	#ifdef REFLECTION	
		shadedColor.rgb += reflectionColor * 0.4f;
	#endif
	
	return float4(shadedColor.rgb,transparency);

For this I asked if its possible on Urho, in my opinion, it's much more beautiful.

-------------------------

Eugene | 2020-01-31 08:48:10 UTC | #4

[quote="dev4fun, post:3, topic:5854"]
What I said about transparency fog is something like I did on my rendering engine
[/quote]

And here is the reason why it's not viable
![image|505x500](upload://NXEc1l27xwHQON9m1bWDm9e2hl.jpeg)

Do you see how objects are ghosting and visible thru each other?
It is unavoidable artifact of transparent fog color.
That's probably the reason why no game engine supports it.

[quote="dev4fun, post:3, topic:5854"]
On forward rendering I expected the sky box it’s the latest thing being drawn, this way, if I set some alpha value on any object at pixel shader color, I thought that alpha should be applied on scene
[/quote]
I don't get how it should work.
Object alpha color determines how much the object will blend into already rendered objects.
If skybox is the latest thing rendered, object cannot blend into skybox regardless of object's alpha.
You need to render skybox first if you want to blend into it.

-------------------------

SirNate0 | 2020-01-31 14:26:48 UTC | #5

What about doing it through a post processing pass by reading the depth buffer to determine the fog (skybox) weight in the scene? Then you would still draw everything normally before that and shouldn't run into the ghostly looking objects (other than that they blend with the sky)

-------------------------

Modanung | 2020-01-31 15:15:28 UTC | #6

Maybe it would look best if objects faded to a fog color first (up until, let's say, approximately three quarters the fog distance) only mixing in the sky beyond that point?

-------------------------

dev4fun | 2020-01-31 18:56:43 UTC | #7

Hm ye, that artifact sucks, but I still prefer this way haha.

Btw I am not familar to Urho rendering yet, but later 'll try something, I dont know what's the best way to follow, if it's hard etc.

-------------------------

Eugene | 2020-01-31 20:50:50 UTC | #8

I think you are trying to solve the problem from wrong end.
It's much simpler to change skybox so it has constant (e.g gray-ish) color near the horizon than to blend objects.

-------------------------

QBkGames | 2020-02-01 08:54:26 UTC | #9

This is the solution I've adopted for may game, however, the problem with it is if you have tall objects or mountains in the landscape which stick out of the horizon, then the illusion breaks up.

-------------------------

QBkGames | 2020-02-01 09:02:59 UTC | #10

I think you might be able to achieve the effect you want by modifying the Skybox fragment shader to render a mix of the skybox texture and the geometry already rendered. You need to read the depth buffer and then set the skybox transparency inversely proportional to the depth value, so that the skybox is completely transparent close by and opaque far away and a range in between. This means you don't need the Fog effect build in Urho and should disable it.

The problem with this is that the skybox is rendered last (I think) in the opaque pass, so the effect will not work for transparent objects which are rendered afterwards.

-------------------------

dev4fun | 2020-02-02 02:45:23 UTC | #11

Hmm good solution, thanks for idea. Have you implemented this idea?

-------------------------

QBkGames | 2020-02-03 01:28:47 UTC | #12

No, the exact algorithm only occurred to me as I was reading through this thread :slight_smile: , however, I did, in the past, want to do something like what you want to achieve, a blend between the skybox and world objects, but I just couldn't come up with the right solution at the time.

-------------------------

dev4fun | 2020-04-11 02:19:28 UTC | #13

I solved the problem using the technique with Alpha pass and setting the depthwrite for true. On shaders I just needed to change the out color of Pixel Shader to use diffColor.a * fogFactor.

For now is working very well, if I feel something is wrong and get worse, probably I will back to the old way...

https://puu.sh/FvXOK/99c7e55849.png

-------------------------

SirNate0 | 2020-04-11 04:24:13 UTC | #14

[quote="dev4fun, post:13, topic:5854"]
using the technique with Alpha pass
[/quote]

By this you're talking about on the skybox, or on every object's material in the game? If it's the latter I feel like that might have a performance impact. Though I'm glad you got it working, it looks pretty nice in that image!

-------------------------

dev4fun | 2020-04-11 17:38:44 UTC | #15

On every object's material, I believe would have a performance impact ye, but for now, isn't a really problem. Probably I will come back to this issue in the future for a better solution.

-------------------------

Eugene | 2020-04-11 17:42:27 UTC | #16

Is it acceptable that the fog is basically wallhack that let players see thru the objects?

-------------------------

dev4fun | 2020-04-11 17:45:15 UTC | #17

Hmm for this type of game yes, we r talking about MMORPG, so doesnt really matters this problem.

-------------------------

