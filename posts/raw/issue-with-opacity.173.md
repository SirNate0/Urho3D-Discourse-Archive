GIMB4L | 2017-01-02 00:58:38 UTC | #1

I have a post-process shader that's supposed to emulate bleedout, like in Call of Duty. It samples from this texture here:

[url]http://puu.sh/7NDhG.png[/url]

However, when sampling in-game all I see is this:
[url]http://puu.sh/7NDjC.jpg[/url]

As you can see a lot of detail is missing. Is this a blend issue? This is the same result in the editor as well.

While I'm on this, I should say I had to put this texture into the normal map as I couldn't get multiple textures going. I understand you need to name them correctly, but how exactly do you specify which texture to use?

-------------------------

cadaver | 2017-01-02 00:58:38 UTC | #2

Please post the shader and renderpath; color resolution shouldn't be an issue if the shader is working correctly.

To assign textures into texture units in the renderpath, you can either use unit numbers directly or the following strings, which start from unit 0 (ie. unit="0" would be same as unit="diffuse"):

[code]
    "diffuse",
    "normal",
    "specular",
    "emissive",
    "environment",
    "lightramp",
    "lightshape",
    "shadowmap",
    "faceselect",
    "indirection",
    "depth",
    "light",
    "volume"
[/code]

-------------------------

GIMB4L | 2017-01-02 00:58:38 UTC | #3

Here's the shader. You'll notice i'm trying to do a distance check from some threshold and apply the other texture then, but at the end I'm just sampling from the texture to make sure it's working.

[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying vec2 vTexCoord;

uniform vec2 cScreenCenter;

uniform vec2 cThreshold;

void VS()
{
	mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetQuadTexCoord(gl_Position);
}

void PS()
{
	vec2 relativeTexcoord = vTexCoord - cScreenCenter;
	
	float sqDist = dot(relativeTexcoord, relativeTexcoord);
	
	vec4 diffuse = texture2D(sDiffMap, vTexCoord);
	
	if (sqDist > cThreshold.x * cThreshold.x)
	{	
		vec4 effect = texture2D(sNormalMap, vTexCoord);
		
		gl_FragColor = mix(diffuse, effect, sqDist);
	}
	else
	{
		gl_FragColor = diffuse;
	}
	
	gl_FragColor = texture2D(sNormalMap, vTexCoord);
}[/code]

Renderpath is as follows:

[code]<renderpath>
	<command type="quad" tag="EyeEffect" vs="PostProcessEyeEffect" ps = "PostProcessEyeEffect" output = "viewport">
		<texture unit="diffuse" name="viewport"/>
		<texture unit="normal" name="Textures/RedOut.png"/>
		<parameter name="Threshold"/>
		<parameter name="ScreenCenter"/>
	</command>
</renderpath>[/code]

-------------------------

