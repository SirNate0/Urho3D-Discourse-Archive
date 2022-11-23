lazypanda | 2017-01-02 01:03:14 UTC | #1

Hi everyone!

I've been looking into the engine and was wondering about the terrain system. Is the terrain geomipmapped automatically because in the editor, I dont see any lod changes. 

Thanks

-------------------------

cadaver | 2017-01-02 01:03:14 UTC | #2

Welcome!

Yes, it's geomipmapped. You should see LOD changes by tweaking the LOD bias attribute of the Terrain component. Though it also depends on the terrain shape; on flat terrain changes are hard to see, unless you enable wireframe view (Ctrl-W).

-------------------------

