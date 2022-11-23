1vanK | 2017-01-02 01:09:55 UTC | #1

I'm trying to create shell for mesh

[code]
void VS()
{
    float offset = 0.1;
    mat4 modelMatrix = iModelMatrix;
    vec4 pos = iPos + vec4(iNormal * offset, 0.0);
    vec3 worldPos = (pos * modelMatrix).xyz;
    gl_Position = GetClipPos(worldPos);
[/code]

but it works incorrect for sharp angles

[url=http://savepic.ru/8545904.htm][img]http://savepic.ru/8545904m.jpg[/img][/url]

(red mesh - scaled shell, white - original mesh)

How to fix it?

-------------------------

TikariSakari | 2017-01-02 01:09:55 UTC | #2

This is my "outline" code, and it should scale things along normal, but I am not 100% sure if it works with sharp edges either. It inverts normals to give outline though

[code]
#include "Uniforms.glsl"
#include "Transform.glsl"

varying vec3 vNormal;

uniform vec4 cOutlineColor;
uniform float cOutLineThickness;


void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);

    worldPos += GetWorldNormal( modelMatrix ) * cOutLineThickness;
    vNormal = GetWorldNormal(modelMatrix) * - 1.0;
    
    gl_Position = GetClipPos(worldPos);
 
}

void PS()
{
    gl_FragColor = cOutlineColor;
}
[/code]

-------------------------

thebluefish | 2017-01-02 01:09:55 UTC | #3

This is an inherent limitation of that technique. So before we go into potential solutions, let's look at our potential X/Y problem. What are you trying to accomplish?

-------------------------

1vanK | 2017-01-02 01:09:55 UTC | #4

[quote="TikariSakari"]This is my "outline" code, and it should scale things along normal, but I am not 100% sure if it works with sharp edges either. It inverts normals to give outline though

[code]
#include "Uniforms.glsl"
#include "Transform.glsl"

varying vec3 vNormal;

uniform vec4 cOutlineColor;
uniform float cOutLineThickness;


void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);

    worldPos += GetWorldNormal( modelMatrix ) * cOutLineThickness;
    vNormal = GetWorldNormal(modelMatrix) * - 1.0;
    
    gl_Position = GetClipPos(worldPos);
 
}

void PS()
{
    gl_FragColor = cOutlineColor;
}
[/code][/quote]

and where inverned vNormal is used?

-------------------------

OvermindDL1 | 2017-01-02 01:09:55 UTC | #5

Are you actually trying to encase it with something, or are you just trying to colorize it or render it differently without necessarily increasing the size?  If so then you could just apply a shader on the original.

-------------------------

1vanK | 2017-01-02 01:09:56 UTC | #6

[quote="thebluefish"]This is an inherent limitation of that technique. So before we go into potential solutions, let's look at our potential X/Y problem. What are you trying to accomplish?[/quote]

[gamedev.stackexchange.com/questi ... ect-effect](http://gamedev.stackexchange.com/questions/34652/outline-object-effect)

-------------------------

1vanK | 2017-01-02 01:09:56 UTC | #7

Previously, I created
[github.com/1vanK/Urho3DOutline](https://github.com/1vanK/Urho3DOutline)
but bluring is slow, so i try to using another method

-------------------------

