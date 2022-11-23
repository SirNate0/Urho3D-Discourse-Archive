TikariSakari | 2017-01-02 01:04:07 UTC | #1

I am trying to make a tactical turn based rpg-like game such as fire-emblem, and when I select an unit, it would be nice to somehow show the selcted unit. I was thinking the blender-like approach of drawing outlines to the unit would probably be the best way to go.

I tried searching internet and it seems there are several kinds of answers to this. One would be making a copy and scaling the object along its faces normals, then flip the faces, and another one seems to be some sort of shader magic. Probably same thing but just done in shaders.

Now I was wondering would it make a difference if I make a mobile game? I am only planning on having one object selected at time. Shader thing if I ever figure out how to do it, seems more generic, but would there be a lot of impact in terms of performance compared to just duplicating the mesh and making it solid color then flipping normals? I guess the shaders at least are guaranteed to work on all the devices that the urho game engine works with?

-------------------------

GoogleBot42 | 2017-01-02 01:04:07 UTC | #2

I would be inclined to think the shader is better... but I don't know.  It probably depends on what you are doing exactly.  Could you post a link because I am also interesting in this too.  :slight_smile:

-------------------------

TikariSakari | 2017-01-02 01:04:07 UTC | #3

[quote="GoogleBot42"]I would be inclined to think the shader is better... but I don't know.  It probably depends on what you are doing exactly.  Could you post a link because I am also interesting in this too.  :slight_smile:[/quote]

Here is the link on possible techniques how to achieve the outline. [url]http://gamedev.stackexchange.com/questions/68401/how-can-i-draw-outlines-around-3d-models[/url]

-------------------------

thebluefish | 2017-01-02 01:04:08 UTC | #4

[quote="TikariSakari"][quote="GoogleBot42"]I would be inclined to think the shader is better... but I don't know.  It probably depends on what you are doing exactly.  Could you post a link because I am also interesting in this too.  :slight_smile:[/quote]

Here is the link on possible techniques how to achieve the outline. [url]http://gamedev.stackexchange.com/questions/68401/how-can-i-draw-outlines-around-3d-models[/url][/quote]

Someone actually provided their shader source in that link. Maybe it's time to look into how to do shaders :wink:

-------------------------

TikariSakari | 2017-01-02 01:04:10 UTC | #5

Got some progress on glsl shader:
[code]
#include "Uniforms.glsl"
#include "Transform.glsl"

uniform vec4 cOutlineColor;
uniform float cOutLineThickness;


void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);

    worldPos += GetWorldNormal( modelMatrix ) * cOutLineThickness;
    gl_Position = GetClipPos(worldPos);
   
}

void PS()
{
    gl_FragColor = cOutlineColor;
}
[/code]

The problem is that I really cannot figure out how the passes work. Like I would want this shader to be rendered on CW culling, then on top of this a normal diffuse-technique with normal CCW-culling.

This is the technique I have:
[code]
<technique vs="Outline" ps="Outline" >
    <pass name="base" />
</technique>
[/code]

And when I make material like this:
[code]
?xml version="1.0"?>
<material>
	<cull value="cw" />
	<technique name="Techniques/Outline.xml" />
	<cull value="ccw" />
	<technique name="Techniques/Diff.xml" />

	<texture unit="diffuse" name="urhotesti3/beardiff.png" />
	<parameter name="OutlineColor" value="0.8 0.8 0.2 1" />
	<parameter name="OutLineThickness" value="0.05" />

	<parameter name="MatDiffColor" value="1.0 1.0 1.0 1" />
	<parameter name="MatVertColor" value="0.6 0.6 0.0 1" />
	
	<parameter name="MatSpecColor" value="0.1 0.1 0.1 115" />
	<parameter name="MatEmissiveColor" value="0 0 0 1" />
</material>
[/code]

This doesn't exactly work like I would prefer it to work, but to just give a better idea what I am trying to achieve. The topmost technique in material is the one that gets used, like if I set outline on topmost, it uses only the outline-technique and if I put diff on topmost it completely ignores the outline-technique.


Edit: After thinking about this a bit more, I just thought adding a new model with just the outline texture. It might not be perfect solution, but at least it works somewhat for now. It does have some glitches here and there though.

[url]http://i.imgur.com/USdG9Mg.png[/url]

Also if objects are on front of the outlined object, the thing will not be visible.

-------------------------

ghidra | 2017-01-02 01:04:11 UTC | #6

I have been working on that myself. This is some preliminary shader work i did

[nervegass.blogspot.com/2014/12/u ... ction.html](http://nervegass.blogspot.com/2014/12/urho-shaders-edge-detection.html)

It kind of goes over the render pipeline a little and how to get a decent looking outline. What I have these days is not much different from that.

-------------------------

GoogleBot42 | 2017-01-02 01:04:12 UTC | #7

Thanks!  I might use this later in my minecraft clone (when school eases up a bit) to highlight blocks and other models.   :smiley:

-------------------------

