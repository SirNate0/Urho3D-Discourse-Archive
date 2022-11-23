redmouth | 2017-04-27 02:14:13 UTC | #1

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/194f14e18815c85498be6e79de605bfd422c15fb.png" width="645" height="500">

There are **11768** triangles being rendered for only 10 cubic meshes.  Is it able to avoid unnecessary rendering by culling unvisible objects?

-------------------------

1vanK | 2017-04-27 07:37:59 UTC | #2

Rendered UI also increases triangle count

-------------------------

redmouth | 2017-04-27 08:57:17 UTC | #3

The number of triangles for UI should be less than 2000,  there are still ~ 9000 triangles for the cubes.   Many invisible objects are still not culled by the engine.

-------------------------

rasteron | 2017-04-27 09:06:44 UTC | #4

This topic is related: https://discourse.urho3d.io/t/triangles-calculation-in-debughud/2916/3

You also get ~9k for the HelloWorld demo in DebugHUD

-------------------------

1vanK | 2017-04-27 16:05:25 UTC | #6

Every char = 2 triangles
Also every char rendered twice (shadow + letter itself)

-------------------------

