Eugene | 2019-05-23 13:20:01 UTC | #1

I'd like to introduce support of sparse navigation meshes with dynamically streamed tiles.

Urho3D branch with this feature and two samples is available here:
[https://github.com/eugeneko/Urho3D/tree/navmesh-streaming](https://github.com/eugeneko/Urho3D/tree/navmesh-streaming)

It's a kind of sketch, so I would be happy if someone test and/or review it.

![49_CrowdNavigationStreaming_d 2017-08-04 01-06-50-290|666x500](upload://uC5SbDshAdBnljj2cz66HERsvuC.jpg)
### Guide

First of all, `NavigationMesh::Allocate()` shall be used instead of `NavigationMesh::Build()`:

```
navMesh->Allocate(boundingBox, maxTiles);
```

The bounding box of the entire area is almost unlimited (I hope), but it shall be somehow computed on the user side. Then, user shall provide the limit for simultaneously loaded mesh tiles.

Then, navigation mesh shall be built. It is actually fine to use `NavigationMesh::Build()` first time and `NavigationMesh::Allocate()` other times, but huge areas may cause `out of memory`. 

`NavigationMesh::Build(fromTile, toTile)` could be used to build few tiles in the rectangular area specified.
Then, these tiles could be received via `NavigationMesh::GetTileData(x, z)` and e.g. saved onto disk.
To build next bucket of tiles, do `NavigationMesh::RemoveAllTiles()` first.

The simplest example:
```
for each tile
{
    navMesh->Build(tile, tile);
    tileData = navMesh->GetTileData(tile.x, tile.y);
    SaveToDisk(tileData);
    navMesh->RemoveAllTiles();
}
```

Stored tiles could be added to and removed from navigation mesh via `NavigationMesh::AddTile(tileData)` and `NavigationMesh::RemoveTile(x, z)`.

### Known issues

~~`Obstacle`s shall be re-added on the user side once `AddTile` is called in order to be correctly rendered into navigation mesh.~~

~~`CrowdAgent`s linked to removed chunks become invalid and stuck. This shall be handled somehow at the user side.~~

~~`OffMeshConnection` sometimes doesn't work properly.~~
`OffMeshConnection` sometimes doesn't work properly even without streaming.

`CrowdAgent` may behave strangely if its path lays through removed tile.

Any streaming logic shall be implemented on the user side.

-------------------------

slapin | 2017-08-04 07:00:56 UTC | #2

Ah, this is so cool!
How do you display this debug geometry?
Also would you like to handle obstacles and agents in a way so it would be more transparent
(or more or less clear what to do about them)?

-------------------------

cadaver | 2017-08-04 07:45:24 UTC | #3

Didn't look in any detail, but concept is very cool!

-------------------------

Eugene | 2017-08-04 08:34:34 UTC | #4

[quote="slapin, post:2, topic:3416"]
How do you display this debug geometry?
[/quote]

I draw all tiles currently added to the navmesh.

[quote="slapin, post:2, topic:3416"]
Also would you like to handle obstacles and agents in a way so it would be more transparent

(or more or less clear what to do about them)?
[/quote]
Oh, I definently would like to do something. I just don't know what.
`49_CrowdNavigationStreaming` contains workaround for these issues, but it's not the best way of doing things...

My changes now has zero cost: user don't pay for streaming neither CPU nor memory if he doesn't use it. I don't know how to keep zero cost and fix the issues simultaneously.

Huh... I can send some event from the navmesh and somehow handle it in `CrowdAgent`s and `Obstacle`s...

-------------------------

Mike | 2017-08-04 11:56:47 UTC | #5

Works great :grinning:
Just noticed that the character doesn't move with a 9 tiles grid (streamingDistance_ set to 1).

-------------------------

Eugene | 2017-08-04 19:43:41 UTC | #7

I fixed the problem with Obstacles. They are automatically re-added if `AddTile` was called for the tile intersected with the obstacle. `CrowdAgent`s are harder to handle...

-------------------------

Eugene | 2017-08-04 20:33:28 UTC | #8

I fixed `CrowdAgent`s. They still just stuck when become out-of-mesh, but they are re-added (and so repaired) once the underlying tile is added to the navigation mesh. IMO this is enough.

@cadaver I found some strange logic in navmesh transform calculations... Does navmesh really support node transform or not? E.g. look at NavigationMesh::CollectGeometries.
NavigationGeometryInfo bounding boxes for geometry are stored in the node space...
But right below the boxes for NavArea and OffMeshConnection are stored in the world space o_o
Obstacles are also added to the mesh in the world space.

-------------------------

slapin | 2017-08-05 11:36:35 UTC | #9

Thank you so much! This feature is great addition.

-------------------------

Eugene | 2017-08-07 13:24:16 UTC | #10

Since it seems pretty stable, I'll start to work on PR.

-------------------------

cadaver | 2017-08-07 14:08:53 UTC | #11

Yes, there are comments that FindPath() et al. expect the navmesh data to be in the navmesh node's local space. There may be various brainfarts so feel free to fix them as you encounter them. Multiple people have also worked on it.

Or alternatively, if you find this unnecessary you're also just as free to transform the whole system to work in global space, I don't have objections to this, as it's a quite crazy usecase to move a whole navigation mesh.

-------------------------

slapin | 2017-08-07 15:25:19 UTC | #12

Will it be possible then to build navmesh parts on demand? And have multiple navmeshes for various kinds of agents?

-------------------------

Eugene | 2017-08-07 18:39:38 UTC | #13

[quote="cadaver, post:11, topic:3416"]
it’s a quite crazy usecase to move a whole navigation mesh
[/quote]

I've just added something like 
```
    rootNode = scene_->CreateChild();
    rootNode->SetPosition(Vector3(10, 0, 0));
    rootNode->SetRotation(Quaternion(0, 15, 0));
```
to CrowdNavigation sample and navigation got completely broken.
So I'll remove any stuff that handles node-to-global space converstion for navigation since it's verbose, redundant and don't work properly now. I'll also add porting note just in case.

[quote="slapin, post:12, topic:3416"]
Will it be possible then to build navmesh parts on demand?
[/quote]
It's possible now if you have already built the whole mesh.
It will be possible to build parts without building whole mesh, but some uncaught bugs may hide there, beware.

[quote="slapin, post:12, topic:3416"]
And have multiple navmeshes for various kinds of agents?
[/quote]
It's not supported by `CrowdManager` now and I am not going to change anything here in the nearest future.

-------------------------

slapin | 2017-08-07 19:13:45 UTC | #14

This is nice feature UE4 has, so I;d look into it in future.

Thanks for your work!

I think navmesh moving can be implemented after cleanup. The use case is movable platforms (UE4 has support for this kind of thing too), probably interesting feature to have.

-------------------------

