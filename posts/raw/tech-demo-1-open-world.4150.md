Don | 2018-04-06 05:41:23 UTC | #1

Hello all,

After about a year of meddling with Urho, @RCKraken and I have some progress to show on our project. We have been testing the capabilities of Urho to provide a high performance multiplayer experience with a large world. Though some modification was necessary, we have found it very well suited to our needs. This is the general overview of what has been changed from stock Urho:

-Terrain shading with normals
-Modified vegetation shader for fitting large models
-Automatic imposters for LOD purposes
-SSR based water shading
-Day/Night cycled skybox based on ProcSky (thanks @jmiller)
-Custom level caching for networking

Thanks to the whole community for answering our dumb questions, and special thanks to those whose code we modified for use in our project. (ProcSky, JTippetts level editor)

We hope to work on features such as chunk based AI, SSAO, high level simulation, and vehicles as we move forward in our project. We'll keep this topic updated as improvements come forth.

Best,
Don & Orion

https://youtu.be/2GJMwNylmZ4

-------------------------

slapin | 2018-04-06 09:52:41 UTC | #2

Hi,
Your project looks really cool!
Could you please elaborate on how you implement automatic impostors?
Thanks!

-------------------------

Eugene | 2018-04-06 11:33:03 UTC | #3

Great, I'm happy to see that somebody succeeded with open world demo.
Some dumb questions:

1. Do you animate LODs swtiching?

2. Are you going to do smth with these funny artifacts? I am 73% sure there are some fallback algorythms that are less conspicuous...
![image|146x168](upload://3DxCxLOE7q3y8lWJ8AG83A4bSzQ.jpg)

3. What about wind animation?

-------------------------

Don | 2018-04-06 14:53:18 UTC | #4

I'll do my best here.

[quote="Eugene, post:3, topic:4150"]
Are you going to do smth with these funny artifacts? I am 73% sure there are some fallback algorythms that are less conspicuous…
[/quote]

SSR was a relatively new addition to this project, and it's not entirely polished off yet. I'm not aware of any method that can be used to patch holes in the reflections, but I will do some research on it if you think it's doable. A fading effect at the edges of the screen-space is also in the works.

[quote="Eugene, post:3, topic:4150"]
What about wind animation?
[/quote]

Right now we are just using the default animation on the grass and nothing on the trees. I hope to remedy both of these in the near future. For trees, I was thinking something along the lines of [Crytech vertex painting](https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_ch16.html), but with reduced complexity and features.

[quote="slapin, post:2, topic:4150"]
Could you please elaborate on how you implement automatic impostors?
[/quote]

The system we use right now is an extension of the BillboardSet class. Imposter billboards are first created wherever the objects are in the scene manually. On scene load, the component automatically renders images of the object from a multitude of directions with both diffuse only and normal only shaders.

![E4C0DC1C_albedo|400x150](upload://mWLn6jvfSUHHugfQt423Y1sepsF.jpg)
![E4C0DC1C_normal|400x150](upload://sLipRV4mdUJcvasgXEPsXbSBkCN.png)

These textures are then used by the imposter shaders to render a passable copy by blending the textures based on direction and running the standard lighting calculation.

[quote="Eugene, post:3, topic:4150"]
Do you animate LODs swtiching?
[/quote]

The only real animation is between the real model and the imposter. This is done by having a fade shader on both objects, but in reversed directions. The fade effect just layers a perlin noise threshold image over the object, and fades over the course of several meters based on it. Here's an older picture that sort of shows the process.

![Screenshot%20from%202017-11-05%2020-13-03|690x388](upload://rwmWkX1wnkVGb5Ma66nuBS7Od6f.jpg)

You can see that the tree is partially transparent, and so is the billboard.

-Don

-------------------------

franck22000 | 2018-04-06 15:35:45 UTC | #5

@Don very interested by the billboard technique. I have sent you a PM.

-------------------------

Enhex | 2018-04-06 16:15:41 UTC | #6

Do you deal with input lag and/or prediction with your networking?

-------------------------

Don | 2018-04-06 16:29:31 UTC | #7

Nay; we haven't really noticed an issue with it as of yet. Do you have any recommendations regarding that?

-------------------------

Enhex | 2018-04-06 16:40:41 UTC | #8

if you're using kinematic controller I have an old repo for client side prediction (it doesn't work with physical bodies since that requires re-stepping the whole physics world because Bullet doesn't allow adding time on individual bodies). This implementation is quite old and only tested with a simple demo.
https://github.com/Enhex/Urho3D-CSP

Other than that I'm experimenting with new approach for CSP which involves full prediction of the game state (not only player's character movement), and it will be implemented on top of Urho's scene replication (so it benefits from its optimizations). This approach is more work intensive since it requires running several frames when predicting, and it will be very high quality.
By high quality I mean that games that don't do full prediction still suffer from latency for other things.
For example waiting for the server when opening a door.

if you want to keep it simple, client authority (client telling the server the player's poisition) is the way to go.
for simulating network conditions I recommend Clumsy:
https://jagt.github.io/clumsy/

-------------------------

Eugene | 2018-04-06 20:34:16 UTC | #9

[quote="Don, post:4, topic:4150"]
Right now we are just using the default animation on the grass and nothing on the trees. I hope to remedy both of these in the near future. For trees, I was thinking something along the lines of Crytech vertex painting, but with reduced complexity and features.
[/quote]

FYI, I've "ported" Unity wind system for Urho.
Both global and local wind zones are supported, instancing-friendly.
It works for generated trees with additional metadata, could be ported for classic models...

[details="Details"]
Shader:
 https://github.com/eugeneko/Urho3D-Sandbox-Dirty/blob/master/Asset/Architect/Shaders/HLSL/StandardCommon.hlsl
 https://github.com/eugeneko/Urho3D-Sandbox-Dirty/blob/master/Asset/Architect/Shaders/HLSL/StandardShader.hlsl

Wind system code:
 https://github.com/eugeneko/Urho3D-Sandbox-Dirty/blob/master/Source/FlexEngine/Graphics/Wind.cpp

Tweaked static model:
 https://github.com/eugeneko/Urho3D-Sandbox-Dirty/blob/master/Source/FlexEngine/Graphics/StaticModelEx.cpp

https://youtu.be/WuDGsA88eWI?list=PL2nDMBpXYaqHfWRmWS_rRTo9UIKcbO29Q
[/details]

-------------------------

slapin | 2018-04-06 21:49:17 UTC | #10

Do you procedurally generate foilage? Could you explain how you do it?

-------------------------

Don | 2018-04-07 01:14:43 UTC | #11

[quote="Eugene, post:9, topic:4150"]
FYI, I’ve “ported” Unity wind system for Urho.
Both global and local wind zones are supported, instancing-friendly.
It works for generated trees with additional metadata, could be ported for classic models…
[/quote]

Thanks, that's a huge help for wind. I'll take a look at that repo as soon as I have the time. Is the performance good for large scenes?

[quote="Enhex, post:8, topic:4150"]
Other than that I’m experimenting with new approach for CSP which involves full prediction of the game state (not only player’s character movement), and it will be implemented on top of Urho’s scene replication (so it benefits from its optimizations). This approach is more work intensive since it requires running several frames when predicting, and it will be very high quality.
[/quote]

Any idea when this new system will be complete and stable? I'd love to use it.

[quote="slapin, post:10, topic:4150, full:true"]
Do you procedurally generate foilage? Could you explain how you do it?
[/quote]

Sort of. The trees and grass models are all the same as of now, and are pre-made. At server startup, these models are placed randomly throughout the map. There isn't really an intelligent spawning system in place right now...

-------------------------

dev4fun | 2018-04-07 04:14:21 UTC | #12

I really liked this, congratz :smiley: 

@ U have made a modification on ProcSky? I see that have some textures on the sky, looks amazing.

-------------------------

Enhex | 2018-04-07 07:51:37 UTC | #13

[quote="Don, post:11, topic:4150"]
Any idea when this new system will be complete and stable? I’d love to use it.
[/quote]

I got some tasks related to Hellbreaker before I can get back to work on it.
It should be soon (~less then a month) unless there are any surprises.

-------------------------

Eugene | 2018-04-07 11:23:51 UTC | #14

[quote="Don, post:11, topic:4150"]
Is the performance good for large scenes?
[/quote]

Meh, I didn't really tested it. It should be as efficient as possible with current Urho architecture and component design. Unless you want to make 1k of local wind zones.

-------------------------

RCKraken | 2018-04-10 03:27:56 UTC | #15

Yes, I made the ProcSky changes. The night time sky is just a texture, and the day time sky is standard ProcSky with variables that are dependent on time. Both are interpolated based on a function of game time:

(atan(8 * sin(cTimeOfDay)) + 1.5) / 3

This function seemed to work quite well^

Also, I'm looking forward to adding clouds :grinning:

Orion

-------------------------

monkeyface | 2018-04-17 09:19:54 UTC | #16

Is this staying closed source then? It looks like there's a lot of awesome stuff in there that could be added to the open source engine or shared as extensions...

-------------------------

Don | 2018-04-17 19:19:11 UTC | #17

Thanks for asking. Yes, this project will be closed source since the end goal is a commercial product. With that said, we plan to PR many of the features that people would like in upstream Urho. This will likely include things such as the auto imposters, SSR ocean, and SSAO. It is simply the case right now that these features are not mature and I do not have the time to PR them at the moment. Sorry.

However, I am more than willing to answer any questions about implementations.

-Don

-------------------------

