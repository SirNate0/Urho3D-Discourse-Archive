nergal | 2017-12-04 07:58:55 UTC | #1

What's the fastest type to draw with Urho3D? Is it one triangle or is it possible to draw "points" such as ThreeJS with its points material?  (https://threejs.org/docs/#api/materials/PointsMaterial)

So If I want to create a point cloud, what type should I use?

-------------------------

Modanung | 2017-12-04 10:54:33 UTC | #2

Have you heard of [Euclideon](https://en.wikipedia.org/wiki/Euclideon)?
Apparently sorting and indexing the point cloud data combined with a proper single-result search algorithm is the 'secret' to fast rendered point clouds. 

Urho3D does have the `FILL_POINT` fill mode and (square) `Billboards`. I'm not sure if the point fill mode is flexible enough in your case.

-------------------------

nergal | 2017-12-04 13:41:49 UTC | #3

Yeah I've seen Euiclidon, pretty cool. I will look into that "FILL_POINT" style, thanks!

-------------------------

