lebrewer | 2021-10-18 15:13:01 UTC | #1

Is there a built-in engine solution for streaming or lazy-loading terrain tiles? I've created a few terrain tiles, and even though they don't align perfectly on the seams, I managed to hide those with static meshes like rocks, trees and grass. Now, the only challenge left is finding a way of lazy loading those tiles based on where the player is on the map. 

Is there a built-in engine solution for this? Or should I raycast my way into this?

-------------------------

vmost | 2021-10-18 15:22:22 UTC | #2

You may want to look into Townforged, my vague recollection is they lazy load terrain...

-------------------------

lebrewer | 2021-10-18 19:59:00 UTC | #3

This? https://git.townforge.net/townforge/townforge

-------------------------

vmost | 2021-10-18 20:24:51 UTC | #4

Yeah they build on Urho3d: https://git.townforge.net/townforge/Urho3D

-------------------------

JSandusky | 2021-10-18 20:59:57 UTC | #5

It's pretty involved but the core update of my tiling scene management is:
```
for (auto c : cells_)
{
    // any async raw-data loads completed?
    if (c->loaded_ == LS_STREAMING && c->fileDataLoaded_) //JS: fixme
    {
        c->node_->Load(c->loadData_);
        c->fileDataLoaded_ = 0;
        c->loaded_ = LS_LOADED;
        c->loadData_.Clear();
    }
}

for (auto cell : cells_)
{
    // reminder, position and these distances are in tile-space
    const auto posDiff = position_ - cell->position_;
    const auto diffX = Abs(posDiff.x_);
    const auto diffY = Abs(posDiff.y_);
    const auto dist = Max(diffX, diffY);

    // avoid any risk of atomic divergence in tests
    const auto loadState = cell->loaded_.load();
    if (dist <= distance_)
    {
        if (loadState != LS_STREAMING && loadState != LS_LOADED)
            LoadCell(cell, anyLoaded && !isTeleport);
    }
    else
    {
        if (loadState == LS_LOADED || (loadState == LS_PERSISTING && dist > persistDistance_))
        {
            UnloadCell(cell); // queues persistance if LS_LOADED
        }
    }
}
```

where a cell is:
```
struct Cell {
    // Octree only applied because I refactored scene management, doesn't apply if no floating origin where there's an octree per tile
    SharedPtr<Octree> octree_;
    SharedPtr<Node> node_; // root for the cell, named Tile_X_Y
    IntVector2 position_; // in tile space
    std::atomic<LoadStatus> loaded_; // state
            
    VectorBuffer loadData_; // temp buffer async load is written into
    std::atomic<int> fileDataLoaded_; // 0 or 1 bool marker for the above data
};
```

There's a lot going on behind the scenes for the async load, but it's basically just a file read stuffed into a special thread that manages the loads and persistence. Atomics track status and when ready the actual Node::Load is done against the read data (which is fast enough for reasonably sized tiles).

Persistence is tricky so there's a threshold distance before a persisting cell is genuinely cleared of the loaded nodes (it's immediately orphaned from the scene, but not released so it can be reattached in a hurry) to avoid ping ponging tile loads/unloads and allows to lazily write out save-state.

Teleporting is hard. I do it the janky way and delay the load for 2 frames so renderpaths can be switched to draw a load screen. It mostly works, but it's jank.

Octree per cell weirdness is related to floating origin, that's a giant nightmare. Shifting every root-level node murders the octree so instead everything gets shifted without marking dirtiness. It's easier to shift a whole Octree but not as easy to just shift Octants as that involves treadmills and exchanging contents which is more headache than I wanted. If not shifting origin then none of that matters.

-------------------------

lebrewer | 2021-10-18 22:53:54 UTC | #6

Do you check that on every movement of the camera (to get the distance)? Also, at which moment do you actually create the node and the component?

```
Node* terrainNode = scene_->CreateChild("Terrain");
auto* terrain = terrainNode->CreateComponent<Terrain>();
```

-------------------------

JSandusky | 2021-10-18 23:53:47 UTC | #7

I check once at the beginning of frame and again whenever the camera is teleported, unless teleporting any camera movement during the frame is meaninglessly small (in my case at least).

The nodes for the tile are created via `Node::Load(...)` from a serialization of the tile. The tile contents themselves are created at design time only (technically, ignoring dynamic elements that are game logic specific). Scene/prefab format is modified to support embedded resources so the heightmaps for terrains in the tile are stored in there with with the scene contents (only heightmaps and genuinely 1-off bespoke models are embedded [e.g. Namsan Tower]).

I strongly suggest you work out whatever your tiling scheme is first and let it blocking load before you start to approach moving it to async. There's lots of headaches in async beyond just loading but also saving/restoring dynamic things, other state, etc.

-------------------------

Naros | 2021-10-19 15:53:40 UTC | #8

[quote="lebrewer, post:6, topic:7012"]
Do you check that on every movement of the camera (to get the distance)?
[/quote]

In our engine's implementation, while we track the camera movement on each frame, we only do terrain updates as the camera position crosses specific boundaries.

We split the terrain into two types of grids.  

The top-level grid system splits the actual terrain files into parts that represent the world map in 533.3333 x 533.3333 world units.  Each tile provides the engine with all the static map references such as the height-map, texture blend maps, static shadow maps, model references, etc.

The second-level grid system splits the actual individual tiles into sub-sections we refer to commonly as either cells or chunks.  We do this as it allows us to provide a way to render chunks closest to the player in higher fidelity than those farther away so that we can keep memory budgets in check.

In terms of loading, we follow a similar practice to what JSandusky has described.

In our engine we define 3 values

- View distance (configured by the user)
- Persistence distance (a value slightly beyond the view distance for cache/pre-load)
- Low-polygon transition distance (a value between the player and view distance)

Our terrain exporter generates a file that the engine can use to draw the terrain with very low polygon counts, which allows us to draw very distant terrain with little cost.  This terrain is drawn without texturing and is meant to provide mostly mountain-like silhouettes.  Since this mesh data is very small compared to each of the tile's vertex data, we can easily load this into memory at map load, so its never streamed.

The configured view distance paired with the persistence distance controls when tiles are streamed in/out.  As the camera moves across a cell / chunk boundary in the smaller grid structure, we re-calculate the persistence distance based on the camera's current position and trigger load / unload of tiles.

The loading is done in a set of worker threads that interact with the main thread to load the tile's data across multiple frames to avoid any type of frame stutter.  

Whenever a player teleports in the game, we obfuscate the rendering artifacts by showing a map load screen to the user while again the persistence and preparation happens across multiple frames.  Once the tiles within the view distance have been loaded, we remove the load screen and render the world.

-------------------------

lebrewer | 2021-10-19 19:32:43 UTC | #9

I really appreciate the detailed answer, that is really helpful. I also find your use of a "LOD" terrain mesh very creative.

-------------------------

Naros | 2021-10-19 21:45:59 UTC | #10

[quote="lebrewer, post:9, topic:7012"]
I also find your use of a “LOD” terrain mesh very creative.
[/quote]

For completeness, we also use the high fidelity calculation to derive how we render which pieces of the terrain.  For example, the closest 5x5 cells, which can scale up to 8x8 at max view distance, are drawn using real-time texture splatting.  For the cells and tiles that are beyond that distance, we use different shaders to render the terrain using a composite texture and that allows us to then easily batch those distant portions of the terrain into a single larger buffer per tile and gain extra render performance with lower and faster draws.

-------------------------

