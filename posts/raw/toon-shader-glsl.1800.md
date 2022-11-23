rasteron | 2017-03-16 01:59:02 UTC | #1

This is the version that I have originally discussed and posted a while back in this [thread](http://discourse.urho3d.io/t/toon-shader-wip/1564/1) and appreciate all the versions that you have came up with guys! awesome :slight_smile:

https://gist.github.com/291babc3700a57f3777c
https://gist.github.com/e69f642970b78d413811

Demo video below also includes Urho3D's LOD feature.

https://www.youtube.com/watch?v=B6TJJs33d4A


..rough version so just tweak the parameters in the shader for variation.

-------------------------

Lumak | 2017-01-02 01:10:19 UTC | #2

Awesome! Thank you for sharing this.

-------------------------

STeeL | 2017-01-02 01:12:13 UTC | #3

Thanks for posting this shader.
HLSL:
[code]
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "Lighting.hlsl"

void VS(float4 iPos : POSITION,
    out float2 oScreenPos : TEXCOORD0,
    out float4 oPos : OUTPOSITION) {	
  float4x3 modelMatrix = iModelMatrix;
  float3 worldPos = GetWorldPos(modelMatrix);
  oPos = GetClipPos(worldPos);
  oScreenPos = GetScreenPosPreDiv(oPos);
}

void PS(float2 iScreenPos: TEXCOORD0, out float4 oColor : OUTCOLOR0) {
  float ResS = 720.;
  float ResT = 720.;
  float MagTol = .5;
  float Quantize = 10.;
	
  float3 irgb = Sample2D(DiffMap, iScreenPos).rgb;
  float2 stp0 = float2(1./ResS, 0.);
  float2 st0p = float2(0., 1./ResT);
  float2 stpp = float2(1./ResS, 1./ResT);
  float2 stpm = float2(1./ResS, -1./ResT);
	
  float3 W = float3(0.2125, 0.7154, 0.0721);
  float i00 =   dot(Sample2D(DiffMap, iScreenPos).rgb, W);
  float im1m1 =	dot(Sample2D(DiffMap, iScreenPos-stpp).rgb, W);
  float ip1p1 = dot(Sample2D(DiffMap, iScreenPos+stpp).rgb, W);
  float im1p1 = dot(Sample2D(DiffMap, iScreenPos-stpm).rgb, W);
  float ip1m1 = dot(Sample2D(DiffMap, iScreenPos+stpm).rgb, W);
  float im10 = 	dot(Sample2D(DiffMap, iScreenPos-stp0).rgb, W);
  float ip10 = 	dot(Sample2D(DiffMap, iScreenPos+stp0).rgb, W);
  float i0m1 = 	dot(Sample2D(DiffMap, iScreenPos-st0p).rgb, W);
  float i0p1 = 	dot(Sample2D(DiffMap, iScreenPos+st0p).rgb, W);
	
  //H and V sobel filters
  float h = -1.*im1p1 - 2.*i0p1 - 1.*ip1p1 + 1.*im1m1 + 2.*i0m1 + 1.*ip1m1;
  float v = -1.*im1m1 - 2.*im10 - 1.*im1p1 + 1.*ip1m1 + 2.*ip10 + 1.*ip1p1;
  float mag = length(float2(h, v));
	
  if(mag > MagTol){
    oColor = float4(0., 0., 0., 1.);
  }else{
    irgb.rgb *= Quantize;
    irgb.rgb += float3(.5,.5,.5);
    int3 intrgb = int3(irgb.rgb);
    irgb.rgb = float3(intrgb)/Quantize;
    oColor = float4(irgb, 1.);
  }
}
[/code]

-------------------------

rasteron | 2017-01-02 01:12:14 UTC | #4

Sure thing STeel. Awesome work with the HLSL version, thanks for sharing.

-------------------------

Miegamicis | 2017-01-02 01:13:02 UTC | #5

You guys are awesome! Will try this out myself!

-------------------------

rasteron | 2017-01-02 01:13:03 UTC | #6

Great, hope you find it useful! :slight_smile:

-------------------------

