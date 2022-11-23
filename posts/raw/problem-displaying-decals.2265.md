vudugun | 2017-01-02 01:14:23 UTC | #1

Hello,
I am trying to mark target points in a tile-based puzzle game. The tiles are beveled cubes exported from Blender with diffuse + normal textures applied.

I have copied some code from the Decals sample (Raycast() and PaintDecal() functions), but when I click on the tiles I am getting inconsistent results:

[img]http://i64.tinypic.com/34reyl1.png[/img]

The crosshair is a 128x128 image with white circles on black background. I created the material from the material editor:
[code]<?xml version="1.0"?>
<material>
	<technique name="Techniques/DiffAdd.xml" quality="0" loddistance="0" />
	<texture unit="diffuse" name="Textures/crosshair2.png" />
	<parameter name="UOffset" value="1 0 0 0" />
	<parameter name="VOffset" value="0 1 0 0" />
	<parameter name="MatDiffColor" value="1 1 0 0.5" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="0 0 0 1" />
	<parameter name="Roughness" value="0.5" />
	<parameter name="Metallic" value="0" />
	<cull value="ccw" />
	<shadowcull value="ccw" />
	<fill value="solid" />
	<depthbias constant="0" slopescaled="0" />
	<renderorder value="128" />
</material>
[/code]

HandleLeftMouseDown():
[code]
    void App::HandleLeftMouseDown(StringHash eventType, VariantMap& eventData)
    {
        Vector3 hitPosition;
        Drawable* hitDrawable;

        if (Raycast(64.0f, hitPosition, hitDrawable))
        {
            Node* targetNode{ hitDrawable->GetNode() };
            DecalSet* decals{ targetNode->GetComponent<DecalSet>() };
            if (decals)
                return;
            ResourceCache* cache{ GetSubsystem<ResourceCache>() };
            decals = targetNode->CreateComponent<DecalSet>();
            decals->SetMaterial(cache->GetResource<Material>("Materials/Crosshair.xml"));
            Vector3 position{ targetNode->GetPosition() };
            position.y_ = hitPosition.y_;
            Quaternion rotation{ 90, 0, 0 };
            decals->AddDecal(hitDrawable, position, rotation, 0.5f, 1.0f, 1.0f,
                Vector2::ZERO, Vector2::ONE);
        }
    }
[/code]

** EDIT:
I just tried changing the size parameter in AddDecal from 0.5f to 1.0f and it kinda works:
[img]http://i68.tinypic.com/28jlmpu.png[/img]

-------------------------

1vanK | 2019-09-21 10:33:11 UTC | #2

```
<depthbias constant="0.0" slopescaled="-2.000" />
```

in material

-------------------------

vudugun | 2017-01-02 01:14:23 UTC | #3

Thanks Ivan, I finally solved with this:
[code]<depthbias constant="-0.00001" slopescaled="0" />[/code]

This is the same as the Decals sample, but it didn't work before. I probably changed something else along the way(?)

-------------------------

