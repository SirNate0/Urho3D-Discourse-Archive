I3DB | 2019-01-06 10:22:50 UTC | #1

Is there a preferred way to convert an image to a decal?

If I use Material.FromImage("Urho2D/Aster.png") (an image from the 2D Sprite feature sample) the resulting decal flickers (using the Decals Feature sample code).

When using the Feature Samples decal material (Materials/UrhoDecal.xml) everything is fine.

I'm not experienced enough with materials and such to know if there is an easy way to fix Material.FromImage to make it more palatable to the eye, or how to create decals.

-------------------------

I3DB | 2019-01-05 03:41:54 UTC | #2

[quote="I3DB, post:1, topic:4796"]
Material.FromImage(“Urho2D/Aster.png”)
[/quote]

on other platforms I tested doesn't crop the image but also doesn't flicker,and the flicker is only on hololens.

-------------------------

Modanung | 2019-01-06 10:22:39 UTC | #3

This flickering is commonly called [z-fighting](https://en.wikipedia.org/wiki/Z-fighting) and can be solved by adding a slight depth bias to your decal material, just like the UrhoDecal material has:
```
<depthbias constant="-0.00001" slopescaled="0" />
```

-------------------------

I3DB | 2019-01-05 16:40:27 UTC | #4

@Modanung Yes, that mostly took care of the flickering.

If using this `ResourceCache.GetMaterial("Materials/UrhoDecal.xml")` it never flickers.
If using the code below, then it doesnt flicker unless the decal is on top of another decal, then it flickers, so if the `Material.FromImage("Urho2D/Aster.png")` decal is put on top of `ResourceCache.GetMaterial("Materials/UrhoDecal.xml")` then it will flicker.

But `ResourceCache.GetMaterial("Materials/UrhoDecal.xml")` on top itself never flickers.

Also, the resulting decal is uncropped and paints as a rectangle rather than showing up as a flower, for instance in the 2D Sprites Feature sample where the Aster.png gets cropped to just the petals of the flower. 

```
var decal = targetNode.CreateComponent\<DecalSet\>();
var decalMaterial = Material.FromImage("Urho2D/Aster.png");
decal.Material = decalMaterial.Clone("");
decal.Material.SetShaderParameter("MatDiffColor", new Color(NextRandom(1.0f), NextRandom(1.0f), NextRandom(1.0f), 1));
decal.Material.DepthBias = new BiasParameters(-0.00001f,0f);
```

-------------------------

I3DB | 2019-01-05 16:39:39 UTC | #5

```
decal.Material.DepthBias = new BiasParameters(NextRandom(-0.0001f,-0.00001f), 0f);
```

No more flickering. But still don't know how to crop the image.

-------------------------

Modanung | 2019-01-05 16:43:11 UTC | #6

[quote="I3DB, post:5, topic:4796"]
But still don’t know how to crop the image.
[/quote]

Sounds like something you could do by setting the material's UV offset.

-------------------------

I3DB | 2019-01-05 17:24:42 UTC | #7

Using code like this makes no change. Is it a setting on the texture?
```
 decal.Material.SetShaderParameter("UVOffset",new Color(.1f,.2f,.3f,.4f));
```

-------------------------

Modanung | 2019-01-05 17:31:34 UTC | #8

There's two material parameters for that, namely `UOffset` and `VOffset`. Both are `Vector4`s.

-------------------------

I3DB | 2019-01-05 17:55:01 UTC | #9

```
var uoffset = decal.Material.GetShaderParameter("UOffset");
var voffset = decal.Material.GetShaderParameter("VOffset");
```

returns 1,0,0,0 and 0,1,0,0

What new UVOffsets would hide the background of the .png?

-------------------------

Modanung | 2019-01-05 17:55:37 UTC | #10

[quote="I3DB, post:9, topic:4796"]
What new UVOffsets would hide the background if the .png.
[/quote]

You mean how to use the alpha transparency of the image?

-------------------------

I3DB | 2019-01-05 23:24:52 UTC | #11

![Aster|64x64](upload://breupsLfE3PSVpZMYdXNKWr16PM.png) 

When painted as a decal produces a rectangle. I just want the flower and no background rectangle.

UVOffset adjustment just moves the actual flower around within the rectangle. But has no effect on transparency.

I"m not experienced with materials or textures, so just trying to get up from the deep water here to the surface to see what's happening.

-------------------------

Modanung | 2019-01-05 18:15:13 UTC | #12

For transparency to show up your material will need to use an _Alpha_ technique.

-------------------------

I3DB | 2019-01-05 23:24:59 UTC | #13

This works ...

```
decalMaterial.SetTechnique(0, ResourceCache.GetTechnique("DiffAlpha.xml"));
```

-------------------------

