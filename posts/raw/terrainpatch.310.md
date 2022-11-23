jorbuedo | 2017-01-02 00:59:32 UTC | #1

Hi, is there any explanation somewhere about TerrainPatch? I don't get it with just the API. Looks like a Terrain should be composed of linked TerrainPatches. And only TerrainPatch is Drawable. But still the examples use only Terrain, and it can be rendered without the patches. 

Also, is there any way to change the height without reloading a full heightmap image?

-------------------------

rasteron | 2017-01-02 00:59:32 UTC | #2

Hi jorbuedo, 

TerrainPatch is indeed part of Terrain. If I remember correctly, the older versions of the Editor used to display the TerrainPatch node but I think it's not necessary anymore. You can check out or manipulate it by code though. [urho3d.github.io/documentation/a00352.html](http://urho3d.github.io/documentation/a00352.html)

-------------------------

jorbuedo | 2017-01-02 00:59:32 UTC | #3

That doesn't help much  :frowning: 
Why is there? What can it do that normal Terrain can't? How do I use it?

From the API I deduce that it's there to create larger terrains using small portions linked together. But then it doesn't make sense that you can simply skip them and render Terrain directly. Terrain is not even Drawable and thus can't be hit by raycast (don't know why it can be rendered however).

[code]    -- Create heightmap terrain
    terrainNode = scene_:CreateChild("Terrain")
    terrainNode.position = Vector3(0.0, 0.0, 0.0)
    local terrain = terrainNode:CreateComponent("Terrain")
    terrain.patchSize = 64
    terrain.spacing = Vector3(2.0, 0.5, 2.0) -- Spacing between vertices and vertical resolution of the height map
    terrain.smoothing = true
    terrain.heightMap = cache:GetResource("Image", "Textures/HeightMap.png")
    terrain.material = cache:GetResource("Material", "Materials/Terrain.xml")
    -- The terrain consists of large triangles, which fits well for occlusion rendering, as a hill can occlude all
    -- terrain patches and other objects behind it
    terrain.occluder = true

    local body = terrainNode:CreateComponent("RigidBody")
    body.collisionLayer = 2 -- Use layer bitmask 2 for static geometry
    local shape = terrainNode:CreateComponent("CollisionShape")
    shape:SetTerrain()


    local terrainPatchNode = scene_:CreateChild("TerrainPatch")
    terrainPatchNode.position = Vector3(0.0, 0.0, 0.0)
    local terrainPatch = terrainNode:CreateComponent("TerrainPatch")
    terrainPatch.coordinates = IntVector2(0,0)
    terrainPatch.owner = terrain
    terrainPatch.material = cache:GetResource("Material", "Materials/StoneTiled.xml")
    terrainPatch.boundingBox = BoundingBox(-10000.0, 10000.0)[/code]

That code gives the following ERROR: Null index buffer and no raw index data, can not define indexed draw range

What's wrong with it?

-------------------------

rasteron | 2017-01-02 00:59:32 UTC | #4

Have you tried running the Lua demos first?

I have not tested the Lua code version, but in angelscript and c++ samples it works fine (Water/Vehicle demo)


* comparing your code with the sample, try putting "local" in your first line so it reads [code]local terrainNode = scene_:CreateChild("Terrain")[/code]

-------------------------

jorbuedo | 2017-01-02 00:59:32 UTC | #5

The problem isn't with Terrain, that works fine. What doesn't work is with TerrainPatch, and non of the examples uses it.
In lua 'local' just refers to the scope of the variable, it's not relevant in the code.

-------------------------

rasteron | 2017-01-02 00:59:32 UTC | #6

Ok I see where you're getting at but apparently the engine takes care of the terrain patch and this component has been rarely discussed. 

So you can refer to the old forum post (Lasse's reply) which coincidentally I have asked before:

[quote]
Terrain is the "master" component, which isn't a drawable component by itself, instead it creates child nodes with TerrainPatch components which actually are drawable, and which can change LOD individually (but while still obeying certain stitching rules to avoid holes). TerrainPatches contain no editable attributes and should be generally be left alone, as the Terrain component manages them.
[/quote]

[b]Original Google group forums message link:[/b]

[groups.google.com/d/msg/urho3d/ ... copsSfkDYJ](https://groups.google.com/d/msg/urho3d/KUtXrZo2LJs/vVcopsSfkDYJ)

-------------------------

jorbuedo | 2017-01-02 00:59:32 UTC | #7

Ok, that makes sense.

-------------------------

