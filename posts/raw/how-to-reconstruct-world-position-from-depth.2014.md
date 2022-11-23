1vanK | 2017-01-02 01:12:18 UTC | #1

I have rendered viewport and depth texture:

I try
[code]
void PS()
{
    vec4 depthInput = texture2D(sDepthBuffer, vTexCoord);
    #ifdef HWDEPTH
       float depth = ReconstructDepth(depthInput.r);
    #else
        float depth = DecodeDepth(depthInput.rgb);
    #endif
    
    vec4 H = vec4(vTexCoord.x * 2 - 1, vTexCoord.y * 2 - 1, depth, 1);
    vec4 D = H * cViewProjInv;
    vec4 worldPos = D / D.w;
    
    // TEST - TRANSFORM BACK
    vec4 clipPos = worldPos * cViewProj;
    vec2 textureCoord = vec2(clipPos.x / clipPos.w * 0.5 + 0.5, clipPos.y / clipPos.w * 0.5 + 0.5);

    gl_FragColor = vec4(texture2D(sDiffMap, textureCoord).rgb, 1);
}
[/code]
but it does not works. What is wrong?

[code]    Matrix4 viewProj = camera.projection * camera.view;
    renderPath.shaderParameters["ViewProjInv"] = Variant(viewProj.Inverse());
    renderPath.shaderParameters["ViewProj"] = Variant(viewProj);
[/code]

-------------------------

cadaver | 2017-01-02 01:12:18 UTC | #2

I'd recommend following/copying what the deferred light shaders (DeferredLight, PrepassLight) do.

-------------------------

1vanK | 2017-01-02 01:12:18 UTC | #3

[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"


#ifdef COMPILEPS
uniform mat4 cViewProjInv;
uniform mat4 cPrevViewProj;
uniform mat4 cViewProj;
uniform float cTimeStep;
#endif

varying vec3 vFarRay;
varying vec4 vScreenPos;
varying vec4 vGBufferOffsets;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vScreenPos = GetScreenPos(gl_Position);
    vFarRay = GetFarRay(gl_Position) * gl_Position.w;
    vGBufferOffsets = cGBufferOffsets;
}

#line 0
void PS()
{
    #ifdef HWDEPTH
        float depth = ReconstructDepth(texture2DProj(sDepthBuffer, vScreenPos).r);
    #else
        float depth = DecodeDepth(texture2DProj(sDepthBuffer, vScreenPos).rgb);
    #endif

    vec3 worldPos = vFarRay * depth / vScreenPos.w;
    worldPos += cCameraPosPS;
  
    // TEST - TRANSFORM BACK
    vec4 clipPos = vec4(worldPos, 1.0) * cViewProj;
    vec4 textureCoord = vec4(clipPos.x * vGBufferOffsets.z + vGBufferOffsets.x * clipPos.w,
                             clipPos.y * vGBufferOffsets.w + vGBufferOffsets.y * clipPos.w,
                             0.0, clipPos.w);
    
    gl_FragColor = vec4(texture2D(sDiffMap, textureCoord.xy).rgb, 1);
    //gl_FragColor = vec4(texture2D(sDiffMap, vScreenPos.xy).rgb, 1);
}
[/code]

I copy it, but I still can not restore texture coords after calculation :(

[url=http://savepic.ru/9727912.htm][img]http://savepic.ru/9727912m.png[/img][/url]
[url=http://savepic.ru/9728936.htm][img]http://savepic.ru/9728936m.png[/img][/url]

I need it for motion blur shader [http.developer.nvidia.com/GPUGem ... _ch27.html](http://http.developer.nvidia.com/GPUGems3/gpugems3_ch27.html)

-------------------------

1vanK | 2017-01-02 01:12:19 UTC | #4

Maybe I incorrect declare a parameters for matrix?

[code]<renderpath>
    <command type="quad" tag="MotionBlur" vs="MotionBlur" ps="MotionBlur" output="viewport">
        <texture unit="diffuse" name="viewport" />
        <texture unit="depth" name="depth" />
        <parameter name="ViewProjInv" value="0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0" />
        <parameter name="PrevViewProj" value="0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0" />
        <parameter name="Proj" value="0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0" />
        <parameter name="ViewProj" value="0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0" />
        <parameter name="TimeStep" value="0.0" />
    </command>
</renderpath>
[/code]

I think so because

It works:
[code]
    vec4 worldPos = clipPos * inverse(cViewProj);

    // restore
    vec4 prevClipPos = worldPos * cViewProj;
    vec2 textureCoord = prevClipPos.xy * 0.5 + 0.5;
[/code]

but it does not works
[code]
    vec4 worldPos = clipPos * cViewProjInv;

    // restore
    vec4 prevClipPos = worldPos * cViewProj;
    vec2 textureCoord = prevClipPos.xy * 0.5 + 0.5;
[/code]

-------------------------

cadaver | 2017-01-02 01:12:19 UTC | #5

If you set the renderpath command shader parameter yourself in code later, the value defined in the xml shouldn't matter, but matrix parameter types should be supported anyway in loading.

One thing to remember is that during fullscreen quad rendering in the renderpath the cViewProj uniform is set to an identity matrix, to avoid possible trouble due to transform inaccuracy, and to also allow rendering quad-only renderpaths without any camera.

I'll test this myself and report back.

-------------------------

1vanK | 2017-01-02 01:12:19 UTC | #6

[quote="cadaver"]
One thing to remember is that during fullscreen quad rendering in the renderpath the cViewProj uniform is set to an identity matrix, to avoid possible trouble due to transform inaccuracy, and to also allow rendering quad-only renderpaths without any camera.
[/quote]

Ah, ok. I send viewProj manually and it works!

[code]    vec4 worldPos = clipPos * cViewProjInv;
    
    // test
    vec4 prevClipPos = worldPos * cMyViewProj;
    
    vec2 textureCoord = prevClipPos.xy * 0.5 + 0.5;
[/code]

-------------------------

cadaver | 2017-01-02 01:12:19 UTC | #7

Could add a parameter to the quad command so that the real cViewProj can optionally be used.

-------------------------

