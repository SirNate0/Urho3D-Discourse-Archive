artgolf1000 | 2018-12-13 10:21:29 UTC | #1

Hi,

I'm studying how to implement a good SSAO shader, the core code is ported from: [url]https://github.com/jsj2008/Zombie-Blobs/blob/278e16229ccb77b2e11d788082b2ccebb9722ace/src/postproc.fs[/url]

The original shader always generates thick shadow on the background, I added a threshold to check if it is in this case, and I added some clear comments.

The result is fine enough, no need to add a blur pass, I make it a post process, it only support forward lighting now.

If you have any alpha layers, please merge ssao.xml and Forward.xml as one render path, and make sure all about alpha is after ssao pass.

Edit: It support mobile devices now, the performance is good, CPU increases 2% on my iPad mini retina.

C++:
```
ResourceCache* cache = GetSubsystem<ResourceCache>();
GetSubsystem<Renderer>()->GetViewport(0)->GetRenderPath()->Append(cache->GetResource<XMLFile>("PostProcess/ssao.xml"));

Vector2 screenSize(GetSubsystem<Graphics>()->GetWidth(), GetSubsystem<Graphics>()->GetHeight());
GetSubsystem<Renderer>()->GetViewport(0)->GetRenderPath()->SetShaderParameter("ScreenSize", screenSize);
```

ssao.xml:
```
<renderpath>
    <rendertarget name="depth" sizedivisor="1 1" format="lineardepth" />
    <command type="clear" color="1 1 1 1" depth="1.0" stencil="0" output="depth" />
    <command type="scenepass" pass="depth" output="depth" />
    <command type="quad" tag="ssao" vs="ssao" ps="ssao">
        <parameter name="ScreenSize" value="1024 768" />
        <texture unit="diffuse" name="viewport" />
        <texture unit="emissive" name="depth" />
    </command>
</renderpath>
```

ssao.glsl:
```
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

varying highp vec2 vScreenPos;

#ifdef COMPILEVS

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
}

#endif


#ifdef COMPILEPS
uniform highp vec2 cScreenSize;

// Port from: https://github.com/jsj2008/Zombie-Blobs/blob/278e16229ccb77b2e11d788082b2ccebb9722ace/src/postproc.fs

// see T M?ller, 1999: Efficiently building a matrix to rotate one vector to another
mat3 rotateNormalVecToAnother(vec3 f, vec3 t) {
    vec3 v = cross(f, t);
    float c = dot(f, t);
    float h = (1.0 - c) / (1.0 - c * c);
    return mat3(c + h * v.x * v.x, h * v.x * v.y + v.z, h * v.x * v.z - v.y,
                h * v.x * v.y - v.z, c + h * v.y * v.y, h * v.y * v.z + v.x,
                h * v.x * v.z + v.y, h * v.y * v.z - v.x, c + h * v.z * v.z);
}

vec3 normal_from_depth(float depth, highp vec2 texcoords) {
    // One pixel: 0.001 = 1 / 1000 (pixels)
    const vec2 offset1 = vec2(0.0, 0.001);
    const vec2 offset2 = vec2(0.001, 0.0);
    
    float depth1 = DecodeDepth(texture2D(sEmissiveMap, texcoords + offset1).rgb);
    float depth2 = DecodeDepth(texture2D(sEmissiveMap, texcoords + offset2).rgb);
    
    vec3 p1 = vec3(offset1, depth1 - depth);
    vec3 p2 = vec3(offset2, depth2 - depth);
    
    highp vec3 normal = cross(p1, p2);
    normal.z = -normal.z;
    
    return normalize(normal);
}

void PS()
{
    const float aoStrength = 1.0;
    
    highp vec2 tx = vScreenPos;
    highp vec2 px = vec2(1.0 / cScreenSize.x, 1.0 / cScreenSize.y);
    
    float depth = DecodeDepth(texture2D(sEmissiveMap, vScreenPos).rgb);
    vec3  normal = normal_from_depth(depth, vScreenPos);
    
    // radius is in world space unit
    const float radius = 1.0;
    float zRange = radius / (cFarClipPS - cNearClipPS);
    
    // calculate inverse matrix of the normal by rotate it to identity
    mat3 InverseNormalMatrix = rotateNormalVecToAnother(normal, vec3(0.0, 0.0, 1.0));
    
    // result of line sampling
    // See Loos & Sloan: Volumetric Obscurance
    // http://www.cs.utah.edu/~loos/publications/vo/vo.pdf
    float hemi = 0.0;
    float maxi = 0.0;
    
    for (int x = -2; x <= 2; ++x) {
        for (int y = -2; y <= 2; ++y) {
            // make virtual sphere of unit volume, more closer to center, more ambient occlusion contributions
            float rx = 0.3 * float(x);
            float ry = 0.3 * float(y);
            float rz = sqrt(1.0 - rx * rx - ry * ry);
            
            highp vec3 screenCoord = vec3(float(x) * px.x, float(y) * px.y, 0.0);
            // 0.25 times smaller when farest, 5.0 times bigger when nearest.
            highp vec2 coord = tx + (5.0 - 4.75 * depth) * screenCoord.xy;
            // fetch depth from texture
            screenCoord.z = DecodeDepth(texture2D(sEmissiveMap, coord).rgb);
            // move to origin
            screenCoord.z -= depth;

            // ignore occluders which are too far away
            if (screenCoord.z < -zRange) continue;

            // Transform to normal-oriented hemisphere space
            highp vec3 localCoord = InverseNormalMatrix * screenCoord;
            // ralative depth in the world space radius
            float dr = localCoord.z / zRange;
            // calculate contribution
            float v = clamp(rz + dr * aoStrength, 0.0, 2.0 * rz);

            maxi += rz;
            hemi += v;
        }
    }

    float ao = clamp(hemi / maxi, 0.0, 1.0);

    gl_FragColor = vec4(texture2D(sDiffMap, vScreenPos).rgb * ao, 1.0);
}

#endif
```

-------------------------

sabotage3d | 2017-01-02 01:15:08 UTC | #2

Nice! Some screens?

-------------------------

dragonCASTjosh | 2017-01-02 01:15:08 UTC | #3

Any plan for a hlsl version

-------------------------

artgolf1000 | 2017-01-02 01:15:09 UTC | #4

SSAO:
[img]http://www.mesh-online.net/ssao1.jpg[/img]
Original:
[img]http://www.mesh-online.net/ssao2.jpg[/img]
Original+SSAO:
[img]http://www.mesh-online.net/ssao3.jpg[/img]

-------------------------

rasteron | 2017-01-02 01:15:11 UTC | #5

Nice work but quickly checking the original+ssao results, I don't see any much difference. Maybe do a side by side comparison? :wink:

-------------------------

Dave82 | 2018-12-12 22:17:54 UTC | #6

So , did anyone worked out a hlsl version of this ? it seems quite interesting.

-------------------------

GoldenThumbs | 2018-12-12 22:56:39 UTC | #7

Not as far as I can tell. Sorry.

-------------------------

ab4daa | 2019-06-15 07:10:31 UTC | #8

I just make a [HLSL version](https://github.com/ab4daa/PostProcess_attempt/blob/master/bin/CoreData/Shaders/HLSL/ssao.hlsl).

![](https://raw.githubusercontent.com/ab4daa/PostProcess_attempt/master/ssao.png)

-------------------------

GoldenThumbs | 2021-01-08 22:55:24 UTC | #9

I modified this shader a bit. Moved the effect to it's own deferred renderpath so it can be blended with the ambient term, a bunch of other changes as well.
[The Render Path](https://github.com/GoldenThumbs/Urho3D/blob/gld_dev/bin/CoreData/RenderPaths/DeferredSSAO.xml#L13-L17)
[The Shader](https://github.com/GoldenThumbs/Urho3D/blob/gld_dev/bin/CoreData/Shaders/GLSL/SSAO.glsl)

![image|641x500](upload://2xAOLlgS97ipUXSXPWy1lu71t4F.jpeg)

-------------------------

JSandusky | 2021-01-09 04:33:42 UTC | #10

That's some pretty extreme dithering.

-------------------------

GoldenThumbs | 2021-01-09 16:38:13 UTC | #11

Yeah, it is. I'm working on a solution. Currently using a single pass blur using two textureGather calls

-------------------------

