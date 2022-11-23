practicing01 | 2017-01-02 01:05:30 UTC | #1

Hello I've added NavigationMesh and Navigable components to a scene and called NavigationMesh->Build().  I get the error: Could not build navigation mesh tile data.  I set the bounding box padding to (0, 100, 0).  The scene has a few models, I want the navmesh for the building.  Perhaps the character models are interfering.  Any ideas?

[img]http://img.ctrlv.in/img/15/06/08/5575a4120f2e3.png[/img]

-------------------------

Mike | 2017-01-02 01:05:30 UTC | #2

It's important to call NavigationMesh->Build() at the right time and to make only static objects participate in the navigation mesh build.

If your characters are AnimatedModels then they are discarded for buiding the navigation mesh. On the other hand, if they are StaticModels then they will become part of the navMesh (unless the build is called before they are added to the scene).

-------------------------

