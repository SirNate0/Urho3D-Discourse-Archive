1vanK | 2017-01-02 01:06:13 UTC | #1

How to make a transparent material with visible specular (not reflections like water) and refraction? Is there a standard feature in engine for this, or is need to write a shader?

-------------------------

1vanK | 2017-06-07 15:32:49 UTC | #2

i tried so:
GlassTechnique.xml
[code]
<technique vs="LitSolid" ps="LitSolid" vsdefines="NOUV" >
    <pass name="litalpha" depthwrite="false" blend="addalpha" />
</technique>
[/code]

glass.xml
[code]
<?xml version="1.0"?>
<material>
	<technique name="Techniques/GlassTechnique.xml"/>
	<parameter name="MatDiffColor" value="0.2 0.2 0.2 1"/>
	<parameter name="MatSpecColor" value="1 1 1 300"/>
</material>
[/code]
[details=Screenshot][img]http://s010.radikal.ru/i313/1508/30/6fdded943229.jpg[/img][/details]
[code]
<?xml version="1.0"?>
<material>
	<technique name="Techniques/GlassTechnique.xml"/>
	<parameter name="MatDiffColor" value="0.0 0.0 0.0 1"/>
	<parameter name="MatSpecColor" value="1 1 1 300"/>
</material>
[/code]
[details=Screenshot][img]http://s019.radikal.ru/i641/1508/0a/d1a5f45178c3.jpg[/img][/details]

but without refraction it look nonrealistic.

-------------------------

1vanK | 2017-01-02 01:06:13 UTC | #3

Another question. It is possible in Urho mix (blending) two materials? Like [youtube.com/watch?v=OlxfJlNK1RM](http://www.youtube.com/watch?v=OlxfJlNK1RM)

-------------------------

boberfly | 2017-01-02 01:06:13 UTC | #4

Hi,

Sure but you need to source refraction from somewhere:
[url]https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/RenderPaths/Forward.xml[/url]
Pretty sure the water shader grabs the environment texture unit from this pass.
[url]https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Techniques/Water.xml[/url]
[url]https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Shaders/GLSL/Water.glsl[/url]
Yep. But I think it's an inverted camera matrix maybe, so it's only good for perfectly flat horizontal water. You might need to re-jig the renderpath to just source the whole framebuffer result into a texture and then distort it with the normals of the sphere, yay refraction.

For reflection you'll need some cube map, maybe bound to the zone's texture unit slot.

-------------------------

1vanK | 2017-06-07 09:09:20 UTC | #5

I combined water and specular and receive interesting result

GlassTechnique.xml
[code]
<technique vs="Water" ps="Water" >
    <pass name="refract" />
    <pass name="litalpha" depthwrite="false" blend="addalpha" vs="LitSolid" ps="LitSolid" vsdefines="NOUV" />
</technique>
[/code]
Glass.xml
[code]
<?xml version="1.0"?>
<material>

    <parameter name="NoiseSpeed" value="0 0" />
    <parameter name="NoiseTiling" value="50" />
    <parameter name="NoiseStrength" value="0.02" />
    <parameter name="FresnelPower" value="5" />
    <parameter name="WaterTint" value="1 1 1" />

    <parameter name="MatDiffColor" value="0.12 0.12 0.12 1"/>
    <parameter name="MatSpecColor" value="1 1 1 300"/>

    <technique name="Techniques/GlassTechnique.xml"/>

</material>
 [/code]
[img]http://s019.radikal.ru/i640/1508/91/079df0dff77c.jpg[/img]

But there is a strange bug: when near on front scene is object with water material refraction switched off

http://s011.radikal.ru/i318/1508/22/ca1b007632d2.jpg
http://s020.radikal.ru/i700/1508/c9/9e390784a732.jpg

-------------------------

1vanK | 2017-06-07 09:04:48 UTC | #6

I fix the problem: necessarily need to set any empty normal texture:

Glass.xml
[code]
<?xml version="1.0"?>
<material>

    <texture unit="normal" name="Textures/UrhoDecalAlpha.dds" />
    <parameter name="NoiseSpeed" value="0 0" />
    <parameter name="NoiseTiling" value="50" />
    <parameter name="NoiseStrength" value="0.02" />
    <parameter name="FresnelPower" value="5" />
    <parameter name="WaterTint" value="1 1 1" />

    <parameter name="MatDiffColor" value="0.12 0.12 0.12 1"/>
    <parameter name="MatSpecColor" value="1 1 1 300"/>

    <technique name="Techniques/GlassTechnique.xml"/>

</material>
[/code]

Edit: The glass object can not be seen through the other glass object
http://s018.radikal.ru/i525/1508/48/06560a3801a9.jpg

-------------------------

codingmonkey | 2017-01-02 01:06:14 UTC | #7

Oh, my bad dream - RenderPath, i'm still do not know how it all works.
But try this tech
glassTech.xml
[code]
<technique vs="Water" ps="Water" >
    <pass name="postopaque" depthwrite="false" blend="addalpha" />
    <pass name="light" depthwrite="false" blend="addalpha" vs="LitSolid" ps="LitSolid" vsdefines="NOUV" />
    <pass name="refract" />    
</technique>
[/code]

[url=http://savepic.ru/7667801.htm][img]http://savepic.ru/7667801m.png[/img][/url]

* You are also must to play with alpha value in matDiffColor in material

-------------------------

1vanK | 2017-01-02 01:06:14 UTC | #8

It seems that this technique refract specularity
[url=http://savepic.su/5922426.htm][img]http://savepic.su/5922426m.jpg[/img][/url]

Without light sources look strange
[url=http://savepic.ru/7721054.htm][img]http://savepic.ru/7721054m.jpg[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:06:14 UTC | #9

I got the same effect if normal map are was missed in slot, you need put to normal texture unit some texture maybe with 1x1 pixel with one flat normal vector within. Just for right calculations in shader.
I'm bake a simple flat normal map, try it (normal 128x128 )
[rghost.net/66hYYljNC](http://rghost.net/66hYYljNC)

Also I found if you try create copy of these glass-objects they are all missing at once from camera view. 
So to solve this you may turn-off the "dynamic instancing" in editor preferences. I don't know but I guess this some kind of render bug.

-------------------------

1vanK | 2017-01-02 01:06:14 UTC | #10

But then the refraction does not work

[url=http://savepic.su/5914239.htm][img]http://savepic.su/5914239m.jpg[/img][/url]

1x1 texture with color (132, 158, 247)

[url=http://savepic.ru/7674961.htm][img]http://savepic.ru/7674961m.jpg[/img][/url]

texture is white pixel - the same artifact

-------------------------

Modanung | 2017-06-07 16:02:02 UTC | #11

4 posts were split to a new topic: [Non-moderators editing posts](/t/non-moderators-editing-posts/3223)

-------------------------

