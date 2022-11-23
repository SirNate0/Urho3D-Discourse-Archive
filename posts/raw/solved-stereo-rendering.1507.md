codder | 2017-01-02 01:08:11 UTC | #1

Hello,

Does Urho3D supports 3D anaglyph (red/cyan) out of the box? And if no, any tips to implement it?

-------------------------

thebluefish | 2017-01-02 01:08:11 UTC | #2

It's not supported out of the box, but it shouldn't be difficult to implement. We'd need to find a shader for it, then it could be implemented as a Post Process effect.

-------------------------

codder | 2017-01-02 01:08:11 UTC | #3

I have the shader but I miss the rest...

[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"

#ifdef COMPILEPS
uniform sampler2D sLeftEye;
uniform sampler2D sRightEye;
#endif

varying vec2 vScreenPos;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

void PS()
{
    vec3 leftRGB = texture2D(sLeftEye, vScreenPos).rgb;
    vec3 rightRGB = texture2D(sRightEye, vScreenPos).rgb;

    leftRGB = vec3(1.0, leftRGB.g, leftRGB.b);
    rightRGB = vec3(rightRGB.r, 1.0, 1.0);

    gl_FragColor = vec4(leftRGB * rightRGB, 1.0);
}

[/code]

-------------------------

1vanK | 2017-01-02 01:08:11 UTC | #4

U need 2 viewports, render it to textures and sent to shader. See example [github.com/MonkeyFirst/Urho3DPo ... ssFXPortal](https://github.com/MonkeyFirst/Urho3DPostProcessFXPortal)

-------------------------

codder | 2017-01-02 01:08:12 UTC | #5

Great!! Thanks!

-------------------------

