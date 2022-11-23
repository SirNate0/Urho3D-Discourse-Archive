Naros | 2020-11-08 19:18:38 UTC | #1

I'm noticing some very odd inconsistencies with `BLEND_ALPHA`.  It very well could be something I am doing incorrectly, so any help would be appreciated.

The model defines 4 `Geometry` and `Material` instances.  The first 3 materials are defined using the default `BLEND_REPLACE` mode.  These materials and associated geometries are drawn first and render things such as the model's head, body, hands, feet, etc.  The last material is drawn last and it uses the `BLEND_ALPHA` mode.  This part of the model is meant to draw a cape that has transparent areas that are meant to allow various parts of the underlying model's body to be visible.

Sometimes the rendered model renders those underlying body areas correctly, meaning I can see the parts of the side of the face, the feet & legs, arms through the transparent sections of the cape.  Most times however, the transparent areas are drawn using the background color instead, as if the model is being rendered such that the cape is drawn before the body.  I've confirmed however that the cape is indeed the last geometry to be rendered, so I'm curious if there is a reason for this behavior?

-------------------------

Naros | 2020-11-08 19:47:12 UTC | #2

To add to my prior post, it would seem that the pass where I use `BLEND_ALPHA` seems to also require that specify alpha-to-coverage as `true` rather than the default of `false`.  I'm still quite new to some of this, can someone explain why that would be necessary?

-------------------------

Eugene | 2020-11-08 19:55:40 UTC | #3

What exactly material is used for `BLEND_ALPHA` geometry?
What technique is used?

-------------------------

Naros | 2020-11-08 20:05:39 UTC | #4

I simply create the `BLEND_ALPHA` material as follows:
```
auto *material = context_->CreateObject<Material>();

auto *technique = context_->CreateObject<Technique>();

auto *pass = technique->CreatePass( "base" );
pass->SetIsDesktop( true );
pass->SetVertexShader( "CharacterModel" );
pass->SetPixelShader( "CharacterModel" );
pass->SetPixelShaderDefines( "DIFFMAP" );
pass->SetBlendMode( BLEND_ALPHA );
pass->SetAlphaToCoverage( true );
pass->SetCullMode( CULL_NONE );

material->SetTexture( TU_DIFFUSE, texture );
material->SetTechnique( 0u, technique, HIGH_QUALITY );
```

-------------------------

Eugene | 2020-11-08 20:16:06 UTC | #5

`base` pass is for solid geometry. Check samples to see how to make transparent materials.

-------------------------

