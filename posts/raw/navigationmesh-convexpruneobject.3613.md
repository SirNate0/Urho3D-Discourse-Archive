Lumak | 2017-09-27 17:48:45 UTC | #1

Just for show.

I finally got around to using NavigationMesh on the project that I'm working on, and for the most part, functionalities that I need are there.  However, I added a few enhancements.

First enhancement was adding a ConvexPruneObject class which as the name suggests prunes nav tiles as untraversable, as shown by the magenta tiles shown in fig 1 and fig 2. This came about after observing that creating a huge Obstacles lacked features that I needed. Querying for nearest path inside an obstacle (position of the white box shown in fig 2) returned a tile inside the obstacle.  By pruning the unwanted tiles, the nearest position is acquired outside the convex object.

Second enhancement was loading nav tiles from file and load them in a single contiguous memory instead of building the nav mesh at load time.  In my simple scene, it takes about 1.4 seconds to build the navmesh and it takes less than 1 msec. to load tiles from file and rebuild it.

Third simple enhancement - for navmesh to ignore nodes with "ignore" tag used for thing as trigger boxes, small debris, and far off mountains that'll never get traversed.

fig 1.
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ee5246e7947a12bbe7c67f6c2b1e3bd7055d49df.jpg[/img]

fig 2.
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/191b06478df261ce8816391a9a6b3659f958e711.jpg[/img]

-------------------------

Lumak | 2017-09-28 17:00:13 UTC | #2

For anyone new to DynamicNavigationMesh, let me clarify that creating a huge Obstacle was just a test and should not be created for your game levels.  Obstacles should be small and are meant to be dynamic, which can potentially be removed at runtime.

-------------------------

