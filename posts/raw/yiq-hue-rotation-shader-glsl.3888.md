SirNate0 | 2017-12-28 05:55:17 UTC | #1

Here's code for a YIQ color space based hue rotation post process shader. This isn't an HSL or HSV hue rotation, but for simple effects it should suffice. I really just wanted to see how the effect looked, as I think I will be using the hue rotation locally (write it into a separate shader for use in materials instead of as a post process effect), but I thought someone else might like it. To quickly see it in action, you can replace the Bloom.xml post process file with it (make sure to change the tag to "Bloom" if you do).

`HueRotation.xml`
```
<renderpath>
    <command type="quad" tag="HueRotation" vs="HueRotation" ps="HueRotation" output="viewport">
        <parameter name="Rotation" value="1.75" />
        <texture unit="diffuse" name="viewport" />
    </command>
</renderpath>
```

`HueRotation.GLSL`
```
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

#line 6

varying vec2 vTexCoord;
varying vec2 vScreenPos;

#ifdef COMPILEPS
uniform float cRotation;
#endif

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetQuadTexCoord(gl_Position);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

// From https://gist.github.com/yiwenl/3f804e80d0930e34a0b33359259b556c
vec2 rotate(vec2 v, float a) {
	float s = sin(a);
	float c = cos(a);
	mat2 m = mat2(c, -s, s, c);
	return m * v;
}

void PS()
{
    vec3 rgb = texture2D(sDiffMap, vScreenPos).rgb;
    
    mat3 rgb2yiq = mat3(0.299, 0.596, 0.211,
                        0.587, -0.274, -0.523,
                        0.114, -0.322, 0.312);
    mat3 yiq2rgb = mat3(1, 1, 1,
                        0.956, -0.272, -1.106,
                        0.621, -0.647, 1.703);
    
    vec3 org = rgb2yiq * rgb;
    vec3 rot = org;
    rot.yz = rotate(org.yz, cRotation);
    
    vec3 final = yiq2rgb * rot;
    
    gl_FragColor = vec4(final, 1.0);
}
```

-------------------------

