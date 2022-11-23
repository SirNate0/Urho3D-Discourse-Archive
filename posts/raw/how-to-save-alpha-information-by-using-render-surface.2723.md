cftvgybhu549 | 2017-03-18 02:07:58 UTC | #1

Please help me.
I want to use a camera to render a texture2D, which will be used in borderimage.
but this texture miss alpha information.
ps: the zone Color I set the fog color is Color(0,0,0,0) . but it's no use.

-------------------------

Eugene | 2017-01-19 09:49:42 UTC | #2

What renderpath do you use?

This worked fine for me:

    <renderpath>
        <rendertarget name="stub1" sizedivisor="1 1" format="rgba" />
        <rendertarget name="stub2" sizedivisor="1 1" format="rgba" />
        <rendertarget name="depth" sizedivisor="1 1" format="readabledepth" />
        <command type="clear" color="0 0 0 0" depth="1.0" stencil="0" depthstencil="depth" />
        <command type="scenepass" pass="deferred" marktostencil="true" vertexlights="true" metadata="gbuffer" depthstencil="depth">
            <output index="0" name="viewport" />
            <output index="1" name="stub1" />
            <output index="2" name="stub2" />
        </command>
    </renderpath>

-------------------------

cftvgybhu549 | 2017-01-20 08:58:36 UTC | #3

the pass I use is forward, what render path should I use. plz~

-------------------------

Eugene | 2017-01-20 09:34:10 UTC | #4

Probably something in Forward path breaks alpha channel after scene rendering.
You have to write your own renderpath that doesn't break alpha (like I did before).

-------------------------

cftvgybhu549 | 2017-01-23 07:56:02 UTC | #5

    <renderpath>
        <command type="clear" color="fog" depth="1.0" stencil="0" />
        <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
        <command type="forwardlights" pass="light" />
        <command type="scenepass" pass="postopaque" />
        <command type="scenepass" pass="refract">
            <texture unit="environment" name="viewport" />
        </command>
        <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
        <command type="scenepass" pass="postalpha" sort="backtofront" />
    </renderpath>

I use the default forward render path. how should I do to modify it. I am not clear about render path, plz help.

-------------------------

cftvgybhu549 | 2017-01-23 16:07:06 UTC | #6

sry, I make a mistake.
I didn't use GetRGBAFormat(), I used GetRGBFormat()
- -

-------------------------

Eugene | 2017-01-23 11:37:33 UTC | #7

Huh. Does it work now?

-------------------------

cftvgybhu549 | 2017-02-06 06:49:23 UTC | #8

yes~ thank you  guy~~

-------------------------

