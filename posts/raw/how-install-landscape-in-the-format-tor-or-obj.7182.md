timob256 | 2022-02-03 17:01:32 UTC | #1

 
I want to install a landscape  **Terrain002_1K.obj** or **example.tor** . 
but  I still haven't figured out how to do it
 
```
    // Create heightmap terrain
    Node* terrainNode = scene_->CreateChild("Terrain");
    terrainNode->SetPosition(Vector3(0.0f, 0.0f, 0.0f));
    auto* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(2.0f, 0.5f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);
    terrain->SetHeightMap(cache->GetResource<Image>("Textures/HeightMap.png"));
    terrain->SetMaterial(cache->GetResource<Material>("Materials/Terrain.xml"));
    
     // The terrain consists of large triangles, which fits well for occlusion rendering, as a hill can occlude all
    // terrain patches and other objects behind it
    terrain->SetOccluder(true);
```

**how to install these models(Terrain002_1K.obj or example.tor) in the view of the landscape ??**

 
If this is not possible, how to translate Terrain002_1K.obj or example.tor in the format  HeightMap.png and Terrain.xml ??

-------------------------

SirNate0 | 2022-02-03 19:50:01 UTC | #2

You can import a `.obj` file with the Asset Importer, and then load the terrain as a `StaticModel`.

https://urho3d.io/documentation/HEAD/_tools.html

As to the tor file, I'm not sure what that is. Something like the one mentioned here? 

https://docs.quadspinner.com/Guide/Bridges/Preparing.html

If you can export it as a height map instead you can use that instead of `"Textures/HeightMap.png"`.

-------------------------

timob256 | 2022-02-04 16:28:41 UTC | #3

Thank you @ [SirNate0](https://discourse.urho3d.io/u/SirNate0)

this not work  https://docs.quadspinner.com/Guide/Bridges/Preparing.html

      ---------------------------------------

changed the landscape Terrain002_1K.obj  in   **terrain1** ( **../Materials/DefaultMaterial.xml** and **../Models/Mesher_LOD2.mdl** and **../Textures/** ) 

```
 dima@astra:~/ogre/Urho3D-1.8-ALPHA/build/bin/tool$ ./AssetImporter scene Terrain002_1K.obj terrain1
Reading file Terrain002_1K.obj
Added model ./Models/Mesher_LOD2.mdl
Added node Mesher_LOD2
Writing model Mesher_LOD2
Writing geometry 0 with 1048576 vertices 6279174 indices
Writing scene
Writing material DefaultMaterial
```



     
```
// Create heightmap terrain
    Node* terrainNode = scene_->CreateChild("Terrain");
    terrainNode->SetPosition(Vector3(0.0f, 0.0f, 0.0f));
    auto* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(2.0f, 0.5f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);
//    terrain->SetHeightMap(cache->GetResource<Image>("Textures/HeightMap.png"));
    terrain->SetMaterial(cache->GetResource<Material>("/home/dima/dima_project/Urho-Project-Template6_gold/Materials/DefaultMaterial.xml"));
    terrain->SetModels(cache->GetResource<Model>("/home/dima/dima_project/Urho-Project-Template6_gold/Models/Mesher_LOD2.mdl"));
     // The terrain consists of large triangles, which fits well for occlusion rendering, as a hill can occlude all
    // terrain patches and other objects behind it
    terrain->SetOccluder(true);
```
 
this not work :frowning: 

/home/dima/dima_project/Urho-Project-Template6_gold/L10n.cpp:386: error: ‘class Urho3D::Terrain’ has no member named ‘SetModels’; did you mean ‘SetNode’?
     terrain->SetModels(cache->GetResource<Model>("/home/dima/dima_project/Urho-Project-Template6_gold/Models/Mesher_LOD2.mdl"));
              ^~~~~~~~~

    --------------------------------------- 


```
    // Create heightmap terrain
    Node* terrainNode = scene_->CreateChild("Terrain");
    terrainNode->SetPosition(Vector3(0.0f, 0.0f, 0.0f));
    auto* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(2.0f, 0.5f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);
//    terrain->SetHeightMap(cache->GetResource<Image>("Textures/HeightMap.png"));
    terrain->SetMaterial(cache->GetResource<Material>("/home/dima/dima_project/Urho-Project-Template6_gold/Materials/DefaultMaterial.xml"));
//    terrain->SetModels(cache->GetResource<Model>("/home/dima/dima_project/Urho-Project-Template6_gold/Models/Mesher_LOD2.mdl"));
     // The terrain consists of large triangles, which fits well for occlusion rendering, as a hill can occlude all
    // terrain patches and other objects behind it
    terrain->SetOccluder(true);
```

this work but not right  :frowning: 


![Screenshot_20220204_191752|647x500](upload://pFCYzGFvtIgmIUzSqoAU4iE72O3.png)

     --------------------------------------


```
// Create heightmap terrain
    Node* terrainNode = scene_->CreateChild("Terrain");
    terrainNode->SetPosition(Vector3(0.0f, 0.0f, 0.0f));
    auto* terrain = terrainNode->CreateComponent<Terrain>();
    terrain->SetPatchSize(64);
    terrain->SetSpacing(Vector3(2.0f, 0.5f, 2.0f)); // Spacing between vertices and vertical resolution of the height map
    terrain->SetSmoothing(true);
//    terrain->SetHeightMap(cache->GetResource<Image>("Textures/HeightMap.png"));
//    terrain->SetMaterial(cache->GetResource<Material>("/home/dima/dima_project/Urho-Project-Template6_gold/Materials/DefaultMaterial.xml"));
    terrain->SetMaterial(cache->GetResource<Material>("/home/dima/dima_project/Urho-Project-Template6_gold/terrain1"));

//    terrain->SetModels(cache->GetResource<Model>("/home/dima/dima_project/Urho-Project-Template6_gold/Models/Mesher_LOD2.mdl"));
     // The terrain consists of large triangles, which fits well for occlusion rendering, as a hill can occlude all
    // terrain patches and other objects behind it
    terrain->SetOccluder(true);
```
this work but not right  :frowning: 


![Screenshot_20220204_192645|647x500](upload://2Ebv5MTmMZJ7BiHVDqugw7jSymt.png)

**Please help me ;_;**

-------------------------

Lys0gen | 2022-02-04 16:34:09 UTC | #4

The Urho3D::Terrain class creates a brand new mesh from a *height map*.

If you already have terrain mesh generated from a third party application then you will probably not want to use Urho3D::Terrain.

Try this instead, with a basic node and simple model assigned to it (not tested):
```
    Node* terrainNode = scene_->CreateChild("ImportedTerrain");
    Urho3D::StaticModel* terrainModel = terrainNode->CreateComponent<StaticModel>();
    terrainModel->SetModel(cache->GetResource<Model>("/home/dima/dima_project/Urho-Project-Template6_gold/Models/Mesher_LOD2.mdl"));
    terrainModel->SetMaterial(cache->GetResource<Material>("/home/dima/dima_project/Urho-Project-Template6_gold/Materials/DefaultMaterial.xml"));
```

-------------------------

