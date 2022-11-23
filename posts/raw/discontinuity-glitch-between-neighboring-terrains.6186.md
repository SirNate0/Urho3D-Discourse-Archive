UrhoIsTheBest | 2020-05-31 07:43:00 UTC | #1

There are very few posts discussing about multiple terrains neighboring each other (e.g. a very old [post](https://discourse.urho3d.io/t/terrain-stitching/2191?u=urho)).

# Problem
Now I am trying to make two terrains adjacent to each other. 
I found there are very small glitches (narrow gaps) at the boundary. 
For example:
![Screen Shot 2020-05-31 at 00.22.13|629x500](upload://a70dlHokMNaWqIuTHHoOCYTVsdS.jpeg) 
and  
![Screen Shot 2020-05-31 at 00.25.30|629x500](upload://2htdnRL7iyquXnnxT1yyl6qtK8I.jpeg) 

I don't think it's a simple shift due to wrong coordinates.
If set camera to FILL_WIREFRAME mode
```
  camera->SetFillMode(FILL_WIREFRAME);
```
I also noticed the mesh seems not continuous.
![Screen Shot 2020-05-31 at 00.27.14|629x500](upload://dXhJDo3bXjuAuGbNDGVRnvev7Lw.png) 

# Code
My sample code:
```
 Node* terrain_node_center = scene_->CreateChild("TerrainCenter");
  Terrain* terrain_center = terrain_node_center->CreateComponent<Terrain>();

  const float size = 204.8;
  Node* terrain_node_east = scene_->CreateChild("TerrainEast");
  terrain_node_east->SetPosition(Vector3(size, 0, 0));
  Terrain* terrain_east = terrain_node_east->CreateComponent<Terrain>();

  Node* terrain_node_west = scene_->CreateChild("TerrainWest");
  terrain_node_west->SetPosition(Vector3(-size, 0, 0));
  Terrain* terrain_west = terrain_node_west->CreateComponent<Terrain>();

  Node* terrain_node_north = scene_->CreateChild("TerrainNorth");
  terrain_node_north->SetPosition(Vector3(0, 0, size));
  Terrain* terrain_north = terrain_node_north->CreateComponent<Terrain>();

  Node* terrain_node_south = scene_->CreateChild("TerrainSouth");
  terrain_node_south->SetPosition(Vector3(0, 0, -size));
  Terrain* terrain_south = terrain_node_south->CreateComponent<Terrain>();

  std::vector<Terrain*> terrains{terrain_center, terrain_east, terrain_west, terrain_north, terrain_south};
  for (auto* terrain : terrains) {
    terrain->SetSpacing(Vector3(0.1, 0.2, 0.1));
    terrain->SetSmoothing(true);

//    terrain->SetMaterial(cache->GetResource<Material>("Materials/Terrain.xml"));
    terrain->SetCastShadows(true);
    terrain->SetOccluder(true);
  }

  terrain_center->SetHeightMap(cache->GetResource<Image>("Textures/TestTerrainCenter.png"));
  terrain_east->SetHeightMap(cache->GetResource<Image>("Textures/TestTerrainEast.png"));
  terrain_west->SetHeightMap(cache->GetResource<Image>("Textures/TestTerrainWest.png"));
  terrain_north->SetHeightMap(cache->GetResource<Image>("Textures/TestTerrainNorth.png"));
  terrain_south->SetHeightMap(cache->GetResource<Image>("Textures/TestTerrainSouth.png"));

 // I tried both setting and not setting neighbor, no difference.
  terrain_center->SetEastNeighbor(terrain_east);
  terrain_east->SetWestNeighbor(terrain_center);

  terrain_center->SetNorthNeighbor(terrain_north);
  terrain_north->SetSouthNeighbor(terrain_center);
```
# Heightmap
My heightmap is 2049*2049 (2^n + 1).
I also made sure the edge pixels of two images are the same (e.g. 2049 pixel for 2048 size).
Also attached example heightmaps:
TestTerrainCenter.png
![TestTerrainCenter|500x500](upload://3zp6gqTCHu6OeV0QhZTARPVlzli.jpeg) 
TestTerrainNorth.png
![TestTerrainNorth|500x500](upload://jjRIhEJsLF0SIEJY3ysou7ZJ4Dj.jpeg) 


# Any help?

-------------------------

Eugene | 2020-05-31 08:07:45 UTC | #2

I’m not sure that “smoothing” was ever tested with neighbor terrains. Use it at your own risk.

-------------------------

UrhoIsTheBest | 2020-05-31 08:31:15 UTC | #3

hmm... that explains it.
No glitch when I disable the smoothing.
Any plan to support that?

-------------------------

JTippetts | 2020-06-01 11:32:39 UTC | #4

Terrain supports heightmaps that encode height in the Red and Green channels (whole part in red, fractional in green). If you use this type of heightmap, smoothing is not necessary and it should work with neighbor terrains. Otherwise, you would need to write your own smoothing code that is 'aware' of the neighboring terrains, in order to correctly smooth across boundaries.

-------------------------

lebrewer | 2020-06-01 17:47:45 UTC | #5

How do you export those channels with stuff like WorldMachine?

-------------------------

JTippetts1 | 2020-06-01 18:27:58 UTC | #6

Not sure since I dont use World Machine, but I suspect it can export 16 bit PNGs. While Urho can't import 16 bit PNG, you could maybe write a converter to take the R channel and split it into 8bit R and G channels.

-------------------------

UrhoIsTheBest | 2020-06-03 01:07:26 UTC | #7

I played with 16 bit heightmap a little bit, somehow I found the smoothing is still valuable given my original heightmap data has 1 meter resolution with 0 ~ 7k meter range. I could use 3rd party tools to refine that heightmap but that would be another topic.

Anyway, I was thinking to write a custom Terrain class for my own use. For example, I need the terrain on a spherical surface, but not the whole planet. So it's easier, I can just map from 2D coordinates into curved surface if I only need a small part on that spherical surface.

The best plan for me is: keep the whole Urho folder untouched, so I can check in newest repo easily. Then have a folder for all my own custom classes.

**Now my question is: what is the best practice to write our own custom components?**
* I could directly inherent from ```Component``` can duplicate most code from ```Terrain``` class, which I don't like.
* Or I can inherent from ```Terrain``` class but I need to change the ```private``` section into ```protected```. By the way, why most classes in Urho are using ```private``` instead of ```protected```, to avoid inherent?

-------------------------

SirNate0 | 2020-06-03 05:04:24 UTC | #8

I can't answer for "best practice", but I can say that this is what I would do:
[quote="UrhoIsTheBest, post:7, topic:6186"]
directly inherent from `Component` can duplicate most code from `Terrain` class
[/quote]
Specifically, I'd copy the Terrain.{cpp,h} files, then refactor (or just find and replace) all Terrain references to SphereTerrain, then modify the class as needed. This was the route I took when I needed some extra features for particle effects, but I'll probably switch to Spark or Effekseer rather than finishing what I was working on.

If you want to go the other route, remember that you'd also probably need to make some additional methods virtual. And if there was no particular reason for forbidding such inheritance (I can't tell you either way), then I'd add that a PR would always be welcome!

-------------------------

