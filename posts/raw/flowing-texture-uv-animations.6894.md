Naros | 2021-06-14 01:34:18 UTC | #1

Hi all, so I have a texture that is 16x64 and what I'm trying to do is animate the UV coordinates such that the texture flows across the v-coordinate space over a set amount of time to give the illusion that the texture is _flowing_.

So far I defined the geometry's vertex buffer such that the uv coordinates are within the 16x16 coordinate space so where u goes from 0..1 and v goes from 0..0.25 (which is 1 / 4).  Next I defined the value animation as follows:

```
auto *animation = new ValueAnimation( context_ );
animation->SetKeyFrame(  0.f, Vector4( 0.f, 0.00f, 0.f, 1.f ) );
animation->SetKeyFrame(  2.f, Vector4( 0.f, 0.25f, 0.f, 1.f ) );
animation->SetKeyFrame(  4.f, Vector4( 0.f, 0.50f, 0.f, 1.f ) );
animation->SetKeyFrame(  8.f, Vector4( 0.f, 0.75f, 0.f, 1.f ) );
```

My understanding is then after 8 seconds, the texture will have flowed from the first 16x16 portion to the last 16x16 portion and will then loop to the first 16x16 frame portion.

Next I defined my material as follows and assigned the animation:

```
auto *mat = new Material( context_ );
mat->SetTechnique( 0, GetResource<Material>( "Techniques/DiffUnlitAlpha.xml" ) );
mat->SetTexture( TU_DIFFUSE, GetResource<Texture2D>( "Textures/WaterFlow.png" ) );
mat->SetVertexShaderDefines( "DIFFMAP VERTEXCOLOR" );
mat->SetPixelShaderDefines( "DIFFMAP VERTEXCOLOR" );
mat->SetScene( scene_ );
mat->SetShaderParameterAnimation( "VOffset", animation );
```

~~It's my understanding that both `cUOffset` and `cVOffset` are built-in animation uniforms and are applied when the VS calls `GetTexCoord` on the incoming UV coordinates and so there shouldn't be any other code necessary to get this to work afaict.~~

~~If I don't apply the animation, I get the first frame, first 16x16 portion of the water flow strip.  But when I apply the animation, I don't see anything being animated nor can I make out any portion of the texture that looks like any of the 16x16 frames.~~

So after some debugging, I found that the value for the offset needs to be provided as a Vector4 and not as a Vector2 as I originally thought.  Making that change, I now see the animations; however they are not transitioning as I would have thought.  Instead it appears it transitions as if no uvs are set, the blue water vertex color and then the texture animates in 1 pixel per frame until the original 16x16 texture is there if I were not applying any uv animations and then loops.  

What I actually wanted here is to take my 16x64 texture, initially render the bottom part of the strip at 16x16 and then adjust the uv coordinates so that I move down the strip with each key frame until I reach the final 16x16 portion at the other end before I repeat.  

This is clearly a UV keyframe issue now but I'm not sure what I did wrong.

-------------------------

weitjong | 2021-06-14 01:41:55 UTC | #2

From what I recall of how this thing works, I think the mistake is you didn’t close the loop. That is, the last key frame should have the same value as your initial key frame.

-------------------------

Naros | 2021-06-14 01:51:16 UTC | #3

The quad is animating such that the texture animations in from the -Z plane but I never see it animate off the +Z plane so it gives this unusual artifact when you have neighboring quads of water planes that the water isn't animating as a single cohesive unit.

What you mentioned makes sense but can you clarify if the key frame offsets I provide are additive to the UV coordinates specified in the vertex buffer or should these be seeded with the initial values from the 16x16 bottom portion of the water texture strip?

-------------------------

Naros | 2021-06-14 03:01:07 UTC | #4

After a bit more tweaking, finally found the solution.  In case others are interested, I setup the keyframes as follows:

```
animation->SetKeyFrame( 0.f, Urho3D::Vector4( 1.f, 0.f, 0.f, 0.f ) );
animation->SetKeyFrame( 2.f, Urho3D::Vector4( 1.f, 0.f, 0.f, 1.f ) );
animation->SetKeyFrame( 0.f, Urho3D::Vector4( 1.f, 0.f, 0.f, 0.f ) );
```

This moves the texture and gives the illusion that the water is flowing.  I honestly expected the key frames to be more complicated for what I wanted but seems to work nonetheless.

@weitjong, if I wanted to provide a _sparkling_ approach rather than this _flowing_ where again I take this 16x64 texture and I split the uv-coordinates into 4 groups:

```
+---------+
| 16x16 A |
+---------+
| 16x16 B |
+---------+
| 16x16 C |
+---------+
| 16x16 D |
+---------+
```

Then for 2 seconds I would display the A slice, after 2 seconds I would display the B slice and so on so that I cycle through each slice every few seconds and repeat.  The idea is that rather than the concept of moving the texture as if it were flowing, I would be shifting what portion of the texture is rendered periodically.  

Is there a way to do this out-of-the-box?  Would this rely on the `EventFrame` concept on the animation to fire and event and the drawable would adjust the UV coordinates in the vertex buffer?

-------------------------

George1 | 2021-06-14 05:28:30 UTC | #5

Lumak demos have some effects.  E,g flowing larva and water.  Maybe you can convert it to new version.

https://discourse.urho3d.io/t/basic-material-effects-for-rendering/2953/38

-------------------------

Naros | 2021-06-14 09:29:57 UTC | #6

Hi @George1, thanks for the link.  So it looks like what Lumak did for this use case is designed a special pipeline (shader / technique) to be used in materials and effectively has a `LogicComponent` that adjusts a special shader parameter to control the row / column within the texture to render.  The shader then uses these values to set the UV coordinates according to the row / column pattern.  

I'm curious if this can be done using `InterpMethod::IM_NONE` on a `ValueAnimation` but so far I have not been able to get this to work as I would have expected.  

If a `LogicComponent` is the only way, so be it but I feel that's precisely what `ValueAnimation` is meant to provide without having to introduce the extra scene component to do it.

-------------------------

weitjong | 2021-06-14 15:12:09 UTC | #7

I just quickly look at the relevant code. I don't think currently there is a way to easily do the animation swap like you described out of the box. Except, by defining the a single more elaborated ValueAnimation that eventually going through all the 4 slices before you close the animation loop.

-------------------------

