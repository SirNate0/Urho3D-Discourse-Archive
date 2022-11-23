jmiller | 2017-01-02 01:06:56 UTC | #1

A zoom blur postprocess shader with user-defined strength and center.

[url=http://postimg.org/image/9f2j3ogbh/][img]http://s30.postimg.org/9f2j3ogbh/Zoom_Blur_01.jpg[/img][/url]

Can produce nausea when animated.  :smiley:
Center is normalized screen coordinates (-0.5 - 0.5)
Strength can be negative.
The cSamples constant in the shader code controls the amount of sampling.

[code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#line 5

varying vec2 vScreenPos;

void VS() {
  mat4 modelMatrix = iModelMatrix;
  vec3 worldPos = GetWorldPos(modelMatrix);
  gl_Position = GetClipPos(worldPos);
  vScreenPos = GetScreenPosPreDiv(gl_Position);
}

#if defined(COMPILEPS)
uniform vec2 cZoomBlurCenter;
uniform float cZoomBlurStrength;
const float cSamples = 40.0;

float RandomOffset(vec3 scale, float seed) {
  return fract(sin(dot(gl_FragCoord.xyz + seed, scale)) * 43758.5453 + seed);
}
#endif

void PS() {
  vec4 color = vec4(0.0);
  float total = 0.0;
  vec2 toCenter = cZoomBlurCenter - vScreenPos;
  float offset = RandomOffset(vec3(12.9898, 78.233, 151.7182), 0.0);
  for(float t = 0.0; t <= cSamples; t++) {
    float percent = (t + offset) / cSamples;
    float weight = 4.0 * (percent - percent * percent);
    vec4 sample = texture2D(sDiffMap, vScreenPos + toCenter * percent * cZoomBlurStrength);
    sample.rgb *= sample.a;
    color += sample * weight;
    total += weight;
  }
  gl_FragColor = color / total;
  gl_FragColor.rgb /= gl_FragColor.a + 0.00001;
}
[/code]

[code]
<renderpath>
  <command type="quad" enabled="true" tag="ZoomBlur" vs="ZoomBlur" ps="ZoomBlur" output="viewport">
    <texture unit="diffuse" name="viewport" />
    <parameter name="ZoomBlurStrength" value="0.15" />
    <parameter name="ZoomBlurCenter" value="0.5 0.5" />
  </command>
</renderpath>
[/code]

-------------------------

1vanK | 2017-01-02 01:06:57 UTC | #2

Nice!

-------------------------

Bananaft | 2017-01-02 01:06:57 UTC | #3

Now feed Z-Buffer as Strength and camera velocity projection as vector, and you will get linear motion blur.

-------------------------

jmiller | 2017-01-02 01:06:57 UTC | #4

Z-buffer use would be a definite improvement.
The screenshot app uses velocity as strength and computes center from direction.

Even more interesting, per-object motion blur - [john-chapman-graphics.blogspot.c ... -blur.html](http://john-chapman-graphics.blogspot.co.uk/2013/01/per-object-motion-blur.html)

-------------------------

Bananaft | 2017-01-02 01:06:57 UTC | #5

[quote="carnalis"]Z-buffer use would be a definite improvement.
The screenshot app uses velocity as strength and computes center from direction.

Even more interesting, per-object motion blur - [john-chapman-graphics.blogspot.c ... -blur.html](http://john-chapman-graphics.blogspot.co.uk/2013/01/per-object-motion-blur.html)[/quote]

Oh, there actually this project from a year ago:  [topic433.html](http://discourse.urho3d.io/t/motion-blur/438/1)

Also, in my opinion, there are very few games, that really need per object motion blur. For racing/flying game, for example, you can just mask out your vehicle and blur linearly the rest of the scene.

-------------------------

rasteron | 2017-01-02 01:06:57 UTC | #6

Cool carnalis. Thanks for sharing!

-------------------------

