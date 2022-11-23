Naros | 2019-12-30 03:44:41 UTC | #1

I am wanting to use a texture to pass some data to my vertex shader.  As a proof of concept, I am constructing a simple 64x64 GL_R32F texture where all pixels have the exact as value as follows:
```
Urho3D::PODVector<float> heightData( 64u * 64u, 50.f );

Urho3D::Texture *texture = new Urho3D::Texture( context_ );
texture->SetFilterMode( Urho3D::FILTER_NEAREST );
texture->SetAddressMode( Urho3D::COORD_U, Urho3D::ADDRESS_CLAMP );
texture->SetAddressMode( Urho3D::COORD_V, Urho3D::ADDRESS_CLAMP );
texture->SetSize( 64u, 64u, Urho3D::Graphics::GetFloat32Format() );
texture->SetData( 0u, 0u, 0u, 64u, 64u, heightData.Buffer() );
```

I then bind this texture to my material:
```
material->SetTexture( Urho3D::TU_SPECULAR, texture );
```

Inside my Vertex Shader:
```
// all the normal includes

varying vec2 vTexCoord;
varying vec4 vWorldPos;
varying float vHeight; // added here to see value in renderdoc

#ifdef COMPILEVS
uniform sampler2D sSpecMap;
#endif

void VS()
{
  // Simply pull the r-channel value from the 0,0 index in the float array
  float height = texelFetch( sSpecMap, ivec2( 0, 0 ), 0 ).r;
  vHeight = height;

  mat4 modelMatrix = iModelMatrix;
  vec3 worldPos = GetWorldPos( modelMatrix );
  worldPos.y = height;

  gl_Position = GetClipPos( worldPos );
  vTexCoord = GetTexCoord( iTexCoord );
  vWorldPos = vec4( worldPos, GetDepth( gl_Position ) );
}
```

When I double check the output from the VS inside RenderDoc, I find that `texelFetch` always returns 0.  I've even checked the actual full vec4 returned from `texelFetch` and its always `0,0,0,1`.   

Now if I define `uniform sampler2D sDiffMap` inside the `COMPILEVS` macro and then swap using the `sDiffMap` uniform rather than the `sSpecMap` uniform then i get non-zero values, but these are the expected [0..1] range values for my base diffuse layer texture.

I've checked the float array texture in RenderDoc, its a 64x64 texture, R32_FLOAT format, where all pixels return a value of 50 when I query the texture.

So at this point I'm not sure what exactly I've done incorrectly.  On all accounts it would appear that I have created my float-array texture correctly, its bound to the vertex shader adequately, but for whatever reason _texelFetch_ refuses to return the expected value.

Any thoughts on what I've likely done incorrectly?

-------------------------

