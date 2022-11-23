slapin | 2017-01-02 01:15:33 UTC | #1

Hi all!

What tools can be used to create Terrain node data?

Thanks a lot!

-------------------------

jmiller | 2019-05-18 17:40:31 UTC | #2

Height and weight map texture generation tools:
http://discourse.urho3d.io/t/free-terrain-editors/1790

Samples/19_VehicleDemo creates  a Terrain and does this:
[code]    terrain->SetHeightMap(cache->GetResource<Image>("Textures/HeightMap.png"));
    terrain->SetMaterial(cache->GetResource<Material>("Materials/Terrain.xml"));
[/code]
Materials/Terrain.xml assigns Textures/TerrainWeights.dds which determines how the detail textures blend.

-------------------------

