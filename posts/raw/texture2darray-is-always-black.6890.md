Naros | 2021-06-12 01:02:26 UTC | #1

So I'm having some trouble with a custom material, technique, and GLSL shader.  I've stripped this down to the bare minimum here and despite having done so, the sampling of the texture array is always black.

Materials/Test.xml
```
<material>
  <technique name="Techniques/Test.xml" quality="2" loddistance="0" />
  <texture unit="0" name="Textures/Test.xml" />
</material>
```

Techniques/Test.xml
```
<technique vs="Test" ps="Test">
  <pass name="base" />
  <pass name="material" depthtest="equal" depthwrite="false" blend="add" />
</technique>
```

Textures/Test.xml
```
<texturearray>
  <layer name="Textures/ground.png" />
  <layer name="Textures/grass.png" />
</texturearray>
```

Shaders/GLSL/Test.glsl
```
#include "Uniforms.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"

#ifdef GL3
#define texture2D texture
#define texture2DProj textureProj
#define texture3D texture
#define textureCube texture
#define texture2DLod textureLod
#define texture2DLodOffset textureLodOffset
#endif

#ifdef COMPILEPS
uniform sampler2DArray sDiffArrayMap;
#endif

varying vec2 vTexCoord1;
varying vec4 vWorldPos;

void VS()
{
  mat4 modelMatrix = iModelMatrix;

  vec3 worldPos = GetWorldPos( modelMatrix );
  gl_Position = GetClipPos( worldPos );

  vTexCoord1 = GetTexCoord( iTexCoord );   

  vWorldPos = vec4( worldPos, GetDepth( gl_Position ) );
}

void PS()
{
  // Sample the second texture in the array
  gl_FragColor = texture( sDiffArrayMap, vec3( vTexCoord1.x, vTexCoord1.y, 1.0 ) );
}

```
In the code, I'm obtaining the material as:
```
auto *material = cache->GetResource<Urho3D::Material>( "Materials/Test.xml" );
model->SetMaterial( material );
```
When I adjust the code to use a `sampler2D` and a single texture rather than the texture array, the model is rendered with the single texture.  I've checked the logs and there is no compiler error or warnings about resources being unavailable, so it must be something in the shader code?

I'm not entirely sure what I might have done wrong here, does anyone have any ideas?

-------------------------

Naros | 2021-06-12 01:11:58 UTC | #2

Looks like my problem was the fact that I was defining the uniform as:
```
uniform sampler2DArray sDiffArrayMap;
```
However there must be a definition somewhere that requires me to define it as:
```
uniform sampler2DArray sDiffMap;
```
Changing that the `Texture2DArray` sampling works as I expected.

-------------------------

JTippetts1 | 2021-06-13 13:20:40 UTC | #3

In the [documentation for Shaders](https://urho3d.io/documentation/HEAD/_shaders.html) it states "In GLSL shaders it is important that the samplers are assigned to the correct texture units. If you are using sampler names that are not predefined in the engine like sDiffMap, just make sure there is a number somewhere in the sampler's name and it will be interpreted as the texture unit." Your shader works with sDiffMap because sDiffMap is one of the pre-defined texture units. sDiffArrayMap is not, so you need to incorporate the assigned texture slot number into the name sDiffArrayMap. eg, sDiffArrayMap0.

-------------------------

