nickwebha | 2021-07-10 18:10:43 UTC | #1

I am trying to change the terrain size of *23_Water* as an experiment for another project. I noticed that if I change the dimensions of *HeightMap.png* the terrain does indeed change width/height but the textures themselves stay the same size and centered. I have also changed *TerrainWeights.png* to match the width/height of *HeightMap.png* (stretching it).

How does one set the size of the terrain plus its textures?

**Edit 1**
I just realized that if I zoom in close enough everything works fine. If I zoom out too far then the outline turns to black.

What could be causing this?

![Screenshot at 2021-07-10 13-43-53|690x388](upload://8VJHNHyTL7Im8UglrbRd1A66vly.png)
![Screenshot at 2021-07-10 13-44-25|690x388](upload://ohChjSk1cWTp3bYvZYXtMncMVW0.png)

**Edit 2**
For anyone looking for this answer:
After playing around with the code I identified `zone->SetBoundingBox()` as the culprit. I have no idea why. I need to read up more on what this does.

-------------------------

JTippetts1 | 2021-07-11 21:11:51 UTC | #2

The mesh resolution of the terrain is dependent upon the image dimensions of the input height map. There is a requirement that the image dimensions be an odd number, which is why the sample height map is sized 1025x1025. If you use an even number, the last row or column will be snipped off. The terrain component essentially builds a mesh with the image pixels defining the elevations of the corners of each quad in mesh. The size of these individual quads is determined by the x_ and z_ components of the Vector3 parameter passed to Terrain::SetSpacing, which by default are both equal to 1.0f. This means that each terrain quad will be sized 1.0 in X and Y directions. Texture coordinates are calculated from this, meaning that with default spacing the terrain textures will tile on quad boundaries. Each quad will receive the entire terrain texture, which will repeat across the terrain.

If you use a different value for spacing, this will change both the size of the terrain quads and the size of the tiling space of the textures, making the quads smaller in 3D space and making the textures tile across a larger area of the terrain. For example, a terrain with spacing x=0.5 y=0.5 would occupy half the size in world space in X and Y, and the textures would tile across it half as many times.

For the zone problem, if you zoom out such that your camera flies out of the XY bounds of the zone, and there is not a zone defined for the new area, weirdness can result. Zone settings such as fog are obtained from the zone the camera currently occupies, with some optional blending with nearby zones, but if no zone is defined for where the camera lies then it defaults fog color settings.

-------------------------

Modanung | 2021-07-12 18:54:54 UTC | #3

Note that the default zone _can_ be accessed - and modified - with `Renderer::GetDefaultZone()`.

-------------------------

nickwebha | 2021-07-14 16:47:24 UTC | #4

[quote="JTippetts1, post:2, topic:6917"]
There is a requirement that the image dimensions be an odd number, which is why the sample height map is sized 1025x1025.
[/quote]
The web compile does not like non-powers of two. Guess I am just going to have to take into account a row and column missing.

I am not sure if this is related or not but my shadows only appear if the camera is really close to the object/node. I am using *box.mdl* which itself has shadows on it but it does not cast them onto the terrain unless I get real close. I am using `object->SetCastShadows( true )` on the node itself as well as `light->SetCastShadows( true )` (from the samples).

-------------------------

Modanung | 2021-07-14 20:44:49 UTC | #5

Have a look at the `SetShadow...` [functions](https://urho3d.io/documentation/HEAD/class_urho3_d_1_1_light.html). Sounds like you might want to increase the fade distance.

-------------------------

nickwebha | 2021-07-14 20:53:22 UTC | #6

I tried playing with `SetShadowBias()` and `SetShadowCascade()` (taken from the samples). I tried changing the numbers, I tried commenting out the lines. Other than the names of the functions themselves they seem to be undocumented so I have no idea what they do.

-------------------------

Modanung | 2021-07-14 20:55:18 UTC | #7

Did you try `SetShadowFadeDistance()`?

-------------------------

nickwebha | 2021-07-25 19:33:07 UTC | #8

[quote="Modanung, post:7, topic:6917, full:true"]
Did you try `SetShadowFadeDistance()` ?
[/quote]
Just did. No go. :frowning:

Here is the-- what I think is-- relevant code:

```
auto* lightNode = this->scene_->CreateChild( "Light" );
lightNode->SetDirection( Urho3D::Vector3( 0.6f, -1.0f, 0.8f ) );
auto* light = lightNode->CreateComponent< Urho3D::Light >();
light->SetLightType( Urho3D::LIGHT_DIRECTIONAL );
light->SetCastShadows( true );
light->SetShadowBias( Urho3D::BiasParameters( 0.00025f, 0.5f ) );
light->SetShadowCascade( Urho3D::CascadeParameters( 10.0f, 50.0f, 200.0f, 0.0f, 0.8f ) );
light->SetSpecularIntensity( 0.5f );
light->SetColor( Urho3D::Color( 1.0f, 1.0f, 1.0f ) );
```

-------------------------

nickwebha | 2021-07-25 19:59:00 UTC | #9

![Screenshot 2021-07-25 15:57:02|690x388](upload://sMwelzyMicHmTi4WwptaXdPzbQ4.jpeg)
![Screenshot 2021-07-25 15:57:31|690x388](upload://6rTxRVc9Sg9A7QZOvdSxTtpkdgm.jpeg)

Can not figure this out. I have tried every function with "shadow" in the name.

-------------------------

