ucupumar | 2017-01-02 00:59:17 UTC | #1

I'm trying to reconstruct position using linear depth by using [url=http://mynameismjp.wordpress.com/2009/03/10/reconstructing-position-from-depth/]this[/url] technique. From the article, he render linear depth by using z (in view space) divide by FarClip. 
[code]float4 DepthPS(in float in_fDepthVS : TEXCOORD0) : COLOR0
{
    // Negate and divide by distance to far-clip plane
    // (so that depth is in range [0,1])
    // This is for right-handed coordinate system,
    // for left-handed negating is not necessary.
    float fDepth = -in_fDepthVS/g_fFarClip;
    return float4(fDepth, 1.0f, 1.0f, 1.0f);
}[/code]
Urho already had function to render linear depth but using dot product of clipPos.zw and DepthMode.zw. As seen on this Transform.glsl
[code]float GetDepth(vec4 clipPos)
{
    return dot(clipPos.zw, cDepthMode.zw);
}[/code]
My question is: What actually the use of DepthMode? Is that any difference from that article implementation?

-------------------------

cadaver | 2017-01-02 00:59:17 UTC | #2

DepthMode is basically just a dot product selector for whether the real Z-value is in the Z or W coordinate. It changes based on whether the camera is orthographic or perspective. You get a value between 0 (nearclip plane) and 1 (farclip plane) from calling GetDepth() in the VS, so you can just pass the value directly to PS.

-------------------------

ucupumar | 2017-01-02 00:59:20 UTC | #3

Thanks for the answer. 
I'm still confused about depth mode but after hours of trying, I found out I can simply reconstruct view space position using linear depth by multiplying linear depth to farPlane. The article's technique is works on Urho linear depth data.
Here's the code:
[code]// Screen Position
vec2 screenPos = vScreenPos.xy / vScreenPos.w; //vScreenPos is GetScreenPos(gl_Position) on vertexshader
vec2 nScreenPos = screenPos * 2.0 - 1.0;

// Get far plane position at View Space
vec3 farPlane = vec3(vFrustumSize.xy * nScreenPos, vFrustumSize.z); // vFrustumSize is cFrustumSize on vertexshader

// Get linear depth
vec3 linearDepth = DecodeDepth(texture2D(sDepthBuffer, screenPos).rgb);
    
// Reconstruct view space position by using linear depth
vec3 viewPosition = linearDepth * farPlane;
[/code]

-------------------------

