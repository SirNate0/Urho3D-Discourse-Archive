sabotage3d | 2017-01-02 01:06:44 UTC | #1

Hi,
I am having some issues with the Navigation mesh. It doesn't cover the hills on the ground properly and the agents go inside. I used the default settings from the example I tried changing some of them but none of them made much difference.
[img]http://i.imgur.com/WybWB2t.png[/img]
[img]http://i.imgur.com/03exrwT.png[/img]

-------------------------

Enhex | 2017-01-02 01:06:44 UTC | #2

You can try to move the characters physically so they collide with the ground if you use physics.
Otherwise try to fiddle with the navmesh's settings like cell height, max climb, max slope, etc to generate more precise mesh.

-------------------------

sabotage3d | 2017-01-02 01:06:44 UTC | #3

Thanks man. What would be the option to increase the resolution of the navigation mesh ? Can we generate navigation mesh from a polygon mesh in another software and use it directly ?

-------------------------

sabotage3d | 2017-01-02 01:06:45 UTC | #4

Thanks a lot Sinoid. I think some of the options doesn't work at all but I will need to investigate further.

-------------------------

