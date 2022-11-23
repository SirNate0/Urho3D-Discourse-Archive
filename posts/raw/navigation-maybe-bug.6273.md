wieszak17 | 2020-07-17 18:10:01 UTC | #1

First some info (some of that probably is important):
I have Terrain object and some plane as water. Part of Terrain is of course underwater. Terrain and plain have parent node which also have DynamicNavigationMesh. Just above water sits AreaNav with id 0 so no walking in/on water. Terrain is runtime modifiable - i change something in heightmap, call rebuild terrain, then build new Navmesh(some boundingbox). 
Now: after few modifications to terrain program gots segfault - gdb said that problem is in dtTileCache::removeTile. Few more test show that:
(/Source/ThirdParty/DetourTileCache/source/DetourTileCache.cpp)

        // Remove tile from hash lookup.
        const int h = computeTileHash(tile->header->tx,tile->header->ty,m_tileLutMask);

tile->header is null, so tile->header->tx access invalid place. I put before that line:

    if (!tile->header) return DT_FAILURE | DT_INVALID_PARAM;

and it seems everything works ok. But maybe ther should be more investigation by someone who knows how it should work? Maybe problem is in DynamicNavigationMesh somehow trying for e.g. remove already removed tile? I'm very new to urho so i don't know if that is bug, some strange case on my side or something else...

-------------------------

