slapin | 2017-01-02 01:15:46 UTC | #1

Hi, all!

How to speed-up navmesh generation over terrain?
For me it takes minutes, which sucks :frowning:

-------------------------

Victor | 2017-01-02 01:15:47 UTC | #2

How are you generating the NavMesh (dynamically at runtime or statically)? If your terrain will remain static, you may want to seek a way to store the mesh data in a file so you can quickly load it back up. Perhaps GetNavigationDataAttr/SetNavigationDataAttr would allow you to load the vertex data. I'm new to NavMesh, so this advice my be incorrect, but that's how I would initially approach the problem.

If you're creating a procedural world however, you may have to be more clever. Splitting the world into parts/chunks might be best; then generate the navmesh for each part dynamically in a background thread.

-------------------------

Mike | 2017-01-02 01:15:47 UTC | #3

Try to tweak cell size (0.8 should be enough, default is 0.3). The higher the cell size, the lower the granularity and build time.
Increase cell size as long as navMesh granularity (accuracy) is acceptable.

-------------------------

slapin | 2017-01-02 01:15:47 UTC | #4

Thanks a lot! Now navmesh build is very quick with increased cellSize!

-------------------------

