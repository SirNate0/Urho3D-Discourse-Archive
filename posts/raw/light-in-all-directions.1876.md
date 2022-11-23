Hevedy | 2017-01-02 01:11:00 UTC | #1

All directions light, something like a directional light but that give light without shadows in all sides of the meshes.
Is this possible ?

-------------------------

hdunderscore | 2017-01-02 01:11:00 UTC | #2

You can use the built in ambient light settings for that, or just use unlit materials.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:00 UTC | #3

I believe Zones's have an ambient light property that will increase the ambient color of the scene this would be a light in all direction. Although when you day directional light without shadow this is also possible by default as you have to enable the shadows per light and mesh within the scene therefore by default there will be no sadow

-------------------------

Hevedy | 2017-01-02 01:11:00 UTC | #4

But is there a way to affect in sphere/box shapes to map zones, without the need of the camera is in the zone to see the colors/light ? Because the ambient light only affect to the zone where you're I need something like a light or color injection to mask

-------------------------

dragonCASTjosh | 2017-01-02 01:11:00 UTC | #5

you could make the materials slightly emissive or increase the diffuse color on these materials

-------------------------

Hevedy | 2017-01-02 01:11:01 UTC | #6

Nono, I will show you I made a simulation in UE4 about what I talking about:

[img]https://dl.dropboxusercontent.com/u/28070491/UE/Slack/General/GIFExample.gif[/img]

-------------------------

Shylon | 2017-01-02 01:11:02 UTC | #7

It is point-light.

-------------------------

Hevedy | 2017-01-02 01:11:02 UTC | #8

[quote="Shylon"]It is point-light.[/quote]

That is the idea but no, this give color/light to all sides of the surfaces in that area and don't cast shadows.
Is part of a system I made to simulate GI

-------------------------

Shylon | 2017-01-02 01:11:02 UTC | #9

Ah, using point light as an Ambient light, now I got it, I do not think it is possible in editor, u should use custom shader, the way light works here is use surface of mesh's normal to make mesh brighter in light direction, so in custom shader you should skip the normal calculation or something, also on deferred shading the scenario may be a little different.

-------------------------

Hevedy | 2017-01-02 01:11:02 UTC | #10

I made that in UE4 is injected in the materials with 8 different spheres at time. Using masks in the materials.

-------------------------

1vanK | 2017-01-02 01:11:02 UTC | #11

[url=http://savepic.ru/9003242.htm][img]http://savepic.ru/9003242m.png[/img][/url]

-------------------------

Shylon | 2017-01-02 01:11:02 UTC | #12

OF course it is possible with more than 1 light and turning of shadow, for example 1 light for front 1 for back.

-------------------------

1vanK | 2017-01-02 01:11:02 UTC | #13

[quote="Hevedy"][quote="Shylon"]It is point-light.[/quote]

That is the idea but no, this give color/light to all sides of the surfaces in that area and don't cast shadows.
Is part of a system I made to simulate GI[/quote]

[url=http://savepic.ru/9027823.htm][img]http://savepic.ru/9027823m.png[/img][/url]

[code]
#ifdef COMPILEPS
float GetDiffuse(vec3 normal, vec3 worldPos, out vec3 lightDir)
{
    ...
        #else
            return texture2D(sLightRampMap, vec2(lightDist, 0.0)).r;
        #endif
    #endif
}[/code]

-------------------------

1vanK | 2017-01-02 01:11:02 UTC | #14

U can also dont increase Brightness but set Ramp (Attenuation texture) for sharp border of light

-------------------------

Hevedy | 2017-01-02 01:11:03 UTC | #15

*Can you give me a better example, no idea where you changed that code.

How expensive is this ?

There should be a way to have more shapes as (Box/Cylinder/Sphere/Capsule)

-------------------------

1vanK | 2017-01-02 01:11:03 UTC | #16

[quote="Hevedy"]*Can you give me a better example, no idea where you changed that code.
[/quote]

CoreData\Shaders\GLSL\Lighting.glsl

-------------------------

Hevedy | 2017-01-02 01:11:03 UTC | #17

[quote="1vanK"][quote="Hevedy"]*Can you give me a better example, no idea where you changed that code.
[/quote]

CoreData\Shaders\GLSL\Lighting.glsl[/quote]

Thanks you looks like work nice.

So since this is possible,why no add in the default engine a new light with this preferences ? a type of pointlight, should be cool too add something to control the lights from editor, better than from a texture, and got light shapes.

*A way or solution to simulate the box/cube light and capsules will be awesome.

-------------------------

dragonCASTjosh | 2017-01-02 01:11:03 UTC | #18

[quote="1vanK"]A way or solution to simulate the box/cube light and capsules will be awesome.[/quote]

This is coming as part of my PBR work

-------------------------

Hevedy | 2017-01-02 01:11:03 UTC | #19

[quote="dragonCASTjosh"][quote="1vanK"]A way or solution to simulate the box/cube light and capsules will be awesome.[/quote]

This is coming as part of my PBR work[/quote]

Oh so cool, thanks.

*You have a fork or repo to see atm ?

-------------------------

dragonCASTjosh | 2017-01-02 01:11:04 UTC | #20

[quote="Hevedy"]You have a fork or repo to see atm ?[/quote]

The fork i have only has the sphere lights in directx forward rendering at the moment. but im adding to it daily and pushing whenever things are usable

-------------------------

