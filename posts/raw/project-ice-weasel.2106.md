TheComet | 2017-01-02 01:13:07 UTC | #1

I finally feel comfortable enough using Urho3D to begin working on a game with a team. We've envisioned a multiplayer first person shooter with a kind of cyber-punk, perhaps "surreal" atmosphere at times.

One unique feature of this game will be "localized gravity". I've modded the editor to allow placement of "gravity probes", which can be seen in the following screen shot as blue arrows:

[img]http://i.imgur.com/05yOOri.png[/img]

Each probe defines a directional vector and a multiplier. The scene can be queried for gravitational forces at any location in 3D space. The system is very rough right now (I search for the closest probe and just directly use its direction and force, so transitions are very jagged), but I was thinking about building a tetrahedral mesh out of the probes and use some form of spacial partitioning to decrease lookup time. That way you can query in which tetrahedron you're in and interpolate the gravity parameters between its 4 vertices, and transitioning between probes would be smooth and unnoticeable.

With this system it will be possible to create things a l? [url=http://artdiscovery.info/wp-content/uploads/2013/07/3-IMG_1871.jpg]M.C. Escher[/url], but most likely we'll be going for something less drastic and less confusing. Having half of the map at a 90? angle could open some interesting tactics for snipers, as they'd be able to shoot across half of the map.

Here is a video:

[video]https://www.youtube.com/watch?v=-wMe3Bp2b0A[/video]

-------------------------

hdunderscore | 2017-01-02 01:13:07 UTC | #2

Wow that's a really cool concept ! The projectiles will follow localized gravity too?

-------------------------

TheComet | 2017-01-02 01:13:07 UTC | #3

[quote="hd_"]Wow that's a really cool concept ! The projectiles will follow localized gravity too?[/quote]

If I choose to simulate projectiles with bullet, then yes! The physics engine will also use localized gravity instead of the PhysicsWorld gravity. Things like actual bullets might be too fast to be noticeably affected, but I can imagine throwing grenades could be interesting!

-------------------------

Enhex | 2017-01-02 01:13:08 UTC | #4

Have you thought about a system that will automatically handle gravity direction instead of gravity probes?
Probes add a lot of work to the level designer and human error is possible.

-------------------------

gawag | 2017-01-02 01:13:10 UTC | #5

Cool.
Reminds me of the gravity generators in SpaceEngineers: [youtu.be/x2aI_yQc6do?t=2m13s](https://youtu.be/x2aI_yQc6do?t=2m13s)
They have two types of generators by now. One has a box shaped field (with independebly adjustable height, width and depth as shown in the video) and pulls everything in this box with a specific force (adjustable between -10G and 10G or something).
The other is sphere shaped with a custom radius.
Both have a gravity which is range independent (the gravity has the same strength everywhere in the field) and the radius has a maximum of 50 meters or something like that.
If an object is inside multiple fields the vectors simply get added. If a player is in multiple fields he will be rotated towards the resulting direction vector (so if two fields are 90? to each other the player would be 45? between).

By now SpaceEngineers does also have planets with gravity and there the sphere shaped gravity "field" actually gets weaker depending on the distance until a certain distance with 0G is reached (in reality an objects gravity does stretch infinitely but can usually be neglected at some distance). 

For performance reasons you could divide your world into big 3D chunks that are bigger as the maximum size for a gravity field (for example 100x100x100 meters). Then you query all fields in the current chunk and the directly adjacent chunks, that should be all fields that could influence that object. Then you could also summarize all gravity strengths.
Your idea with the tetrahedral "mesh" with interpolation would have weird properties as only the four closest "fields" would [b]somehow[/b] influence the object though a fifth field could still be close by. Also the strengths would depend on the space between the points which would also be odd.

-------------------------

Modanung | 2017-01-02 01:13:10 UTC | #6

[quote="gawag"]Your idea with the tetrahedral "mesh" with interpolation would have weird properties as only the four closest "fields" would [b]somehow[/b] influence the object though a fifth field could still be close by. Also the strengths would depend on the space between the points which would also be odd.[/quote]
Somehow I think using a mesh's normals would be ideal to determine the gravity's direction since you could split edges to avoid interpolation on top of smooth detail with ease. Simply look for the closest normal and its direction. The mesh could contain gaps. When split up into separate meshes these could each be enabled and disabled to create - for instance - walkways that can be activated and deactivated.
My skullgut tells me this would best be implemented as a GravityMesh component. Or better even a SetMesh function within the GravityProbe.

-------------------------

TheComet | 2017-01-02 01:13:12 UTC | #7

Thanks for the feedback!

I was able to implement the Bowyer-Watson algorithm for the Delaunay triangulation of 3D points into a tetrahedral mesh:

[img]http://i.imgur.com/cbXLa1f.png[/img]

I also [url=https://github.com/TheComet93/iceweasel/blob/master/doc/interpolating-values-using-a-tetrahedral-mesh/interpolating-values-using-a-tetrahedral-mesh.pdf]started writing a paper[/url] to document all of the math and stuff. There's quite a bit more to it than meets the eye. The paper is very incomplete and a WIP, but it will improve in time.

[quote="gawag"]Your idea with the tetrahedral "mesh" with interpolation would have weird properties as only the four closest "fields" would [b]somehow[/b] influence the object though a fifth field could still be close by. Also the strengths would depend on the space between the points which would also be odd.[/quote]

4 is all you need. In the real world where you can derive a continuous function for mapping position->gravitational vector, you only need 1 directional vector at any point in space. The infinite number of other vectors don't "influence" you, no matter how far or close they are to you.

Remember, this is a [i]vector field[/i], meaning that it is the solution to the differential equations created by multiple bodies of mass. Since it's not possible to have an infinite number of vectors, I have to create a discrete vector field and interpolate (read the introduction to my paper, I think it explains it pretty well).

I too could approximate the vector field a planet's gravitational field would create by spacing the gravity vectors at inverse proportional distances from the planet. It might look something like this: [url]http://i.imgur.com/2fOVpxa.png[/url]

[quote="Modanung"][quote="gawag"]Your idea with the tetrahedral "mesh" with interpolation would have weird properties as only the four closest "fields" would [b]somehow[/b] influence the object though a fifth field could still be close by. Also the strengths would depend on the space between the points which would also be odd.[/quote]
Somehow I think using a mesh's normals would be ideal to determine the gravity's direction since you could split edges to avoid interpolation on top of smooth detail with ease. Simply look for the closest normal and its direction. The mesh could contain gaps. When split up into separate meshes these could each be enabled and disabled to create - for instance - walkways that can be activated and deactivated.
My skullgut tells me this would best be implemented as a GravityMesh component. Or better even a SetMesh function within the GravityProbe.[/quote]

Using normals isn't going to cut it for what we have planned. We have lots of cases where gravity won't be collinear with the face's normal vector. That's why I've created a system where you can arbitrarily define gravity, no matter what the mesh looks like.

-------------------------

godan | 2017-01-02 01:13:12 UTC | #8

Nice work with the tet mesh implementation. It's definitely not a trivial algorithm.

As for interpolating gravity - have you considered multi-variate interpolation? [en.wikipedia.org/wiki/Inverse_d ... _weighting](https://en.wikipedia.org/wiki/Inverse_distance_weighting). It's a great way to interpolate n-dim vectors associated with m-dim points (in this case, 3d gravity vectors associated to 3d position points). The nice thing is that you don't have to care about the structure of the points, nor do you need to interpolate a function over the tet regions. And you are always guaranteed to have at least one nearest neighbor, so the base case of a single gravity defining point works nicely. Note that with this technique, it is not the magnitude of the gravity vector that responds to the inverse distances, rather it is the value.

I used it a while ago to try to make mesh shapes respond to 3d position and time....[vimeo.com/23699024](https://vimeo.com/23699024)

-------------------------

TheComet | 2017-01-02 01:14:04 UTC | #9

Progress is slow. I've mostly been working on the character controller (walk, run, crouch, jump) and on a menu.

[video]https://www.youtube.com/watch?v=u0jRHnz7NJU[/video]

[quote="godan"]Nice work with the tet mesh implementation. It's definitely not a trivial algorithm.

As for interpolating gravity - have you considered multi-variate interpolation? [en.wikipedia.org/wiki/Inverse_d ... _weighting](https://en.wikipedia.org/wiki/Inverse_distance_weighting). It's a great way to interpolate n-dim vectors associated with m-dim points (in this case, 3d gravity vectors associated to 3d position points). The nice thing is that you don't have to care about the structure of the points, nor do you need to interpolate a function over the tet regions. And you are always guaranteed to have at least one nearest neighbor, so the base case of a single gravity defining point works nicely. Note that with this technique, it is not the magnitude of the gravity vector that responds to the inverse distances, rather it is the value.

I used it a while ago to try to make mesh shapes respond to 3d position and time....[vimeo.com/23699024](https://vimeo.com/23699024)[/quote]

I'll give it a look! I don't think inverse distance weighting is a good approach for this problem though. Also keep in mind that it will take longer to find the relevant tetrahedrons if you want to do fancier interpolation. With linear interpolation you only need to find one tetrahedron and you're done.

-------------------------

Lumak | 2017-01-02 01:14:05 UTC | #10

lol at the finger! Nice  :slight_smile:

-------------------------

TheComet | 2017-01-02 01:14:32 UTC | #11

The third person controller is basically done. The animation controller is WIP but it already looks fairly decent. It can be fine-tuned by introducing some secondary movement (e.g. move the ears and tail depending on acceleration, or bend the back when leaning into a corner) or by adding some IK for some finer control.

[video]https://www.youtube.com/v/54numkwW_u8[/video]
([url]https://www.youtube.com/v/54numkwW_u8[/url])

If you are interested in seeing more about the kangaroo, you can find a video with all of the animation loops on our forums: [url]http://iceweasel.forumatic.com/viewtopic.php?f=14&t=22[/url]
I also talk a bit about how the character was rigged.

Next up I'll be working on swimming. Our game is a little bit more complicated due to the whole local gravity feature, so the method I will use for water is to define [b]water mesh volumes[/b]. Swimming mode will be activated when you enter the volume and deactivated when you exit the volume.

I have created a simple "pond" model with which I will be testing this feature:

[img]http://i.imgur.com/i6r4Caz.jpg[/img]

-------------------------

sabotage3d | 2017-01-02 01:14:40 UTC | #12

Nice reminds me of Overgrowth.

-------------------------

