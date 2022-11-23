evolgames | 2021-11-07 02:50:50 UTC | #1

I have a weird problem. Somehow, these npcs I made are invisible through a semi-transparent material (glass). The shadow shows. I don't have any bias or special material settings. Anyone experience something similar?
![Screenshot_2021-11-06_22-43-17|690x388](upload://8UZFfC7vl0McFouA4BCAqwZYIv7.png)

-------------------------

GoldenThumbs | 2021-11-07 02:54:24 UTC | #2

What technique(s) are you using for the npcs' materials? What renderpath is this using?

-------------------------

evolgames | 2021-11-07 03:42:31 UTC | #3

Render Path
```
	viewport = Viewport:new(scene_, cameraNode:GetComponent("Camera"))
	renderer:SetViewport(0, viewport)
	renderer:SetTextureFilterMode(FILTER_ANISOTROPIC)
```
Material for NPC limb (really just some primitives connected to animations). col is a local random table for random color assignment
```
	local material=Material:new()
	material:SetShaderParameter("MatDiffColor",Variant(Vector4(col[1],col[2],col[3],1)))
    object:SetMaterial(material)
```

My Glass.xml
```
<?xml version="1.0"?>
<material>
	<technique name="Techniques/NoTextureAlpha.xml" />
	<parameter name="MatDiffColor" value="0.6 .8 1 .7" />
</material>
```

-------------------------

GoldenThumbs | 2021-11-07 04:07:28 UTC | #4

Is the glass set to be an occluder?

-------------------------

evolgames | 2021-11-07 04:58:41 UTC | #5

Ah yeah that was it, thanks. I didn't suspect at first because apparently shadows don't get occluded? So it looks like I ought to separate the glass from the wall model then.

-------------------------

