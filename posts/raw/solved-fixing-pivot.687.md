sabotage3d | 2017-01-02 01:02:08 UTC | #1

Hello ,

It is currently possible to fix the pivot from already transformed meshes in Urho3D  ?
For example if I have this mesh:
And my transform in Urho3D is at 0,0,0  ,but my mesh is transformed at -1.80, 2.25, 0
I know that BulletPhysics has some helper functions is there something similar in Urho3D ?

[img]http://i.imgur.com/HS8CMql.png[/img]

Is there a way to fix it according to boundingbox maybe ?
I know that BulletPhysics has some helper functions.
This should be the correct pivot .

[img]http://i.imgur.com/ayp41sL.png[/img]

Thanks in advance,

Alex

-------------------------

cadaver | 2017-01-02 01:02:08 UTC | #2

Urho3D does not provide functions to fix a model's pivot after the fact, so the best option is to fix it in the input data. You could use additional scene node hierarchy to reposition the model, but generally I'd recommend against that.

-------------------------

friesencr | 2017-01-02 01:02:08 UTC | #3

[quote="cadaver"]Urho3D does not provide functions to fix a model's pivot after the fact, so the best option is to fix it in the input data. You could use additional scene node hierarchy to reposition the model, but generally I'd recommend against that.[/quote]

Most of my spectacular Urho moments have been from ignorantly mixing nested nodes, scale and rotation.

-------------------------

sabotage3d | 2017-01-02 01:02:09 UTC | #4

In this specific case I am trying to calculate the pivot of a fractured geometry created at runtime. I know there are some helper utils in Bullet physics like best fit object oriented bounding box or a simple obb.

[github.com/bulletphysics/bullet ... uilder.cpp](https://github.com/bulletphysics/bullet3/blob/d347bca2bad80420869217282535fb4ff919e8b5/Extras/ConvexDecomposition/ConvexBuilder.cpp)

[github.com/bulletphysics/bullet ... stfitobb.h](https://github.com/bulletphysics/bullet3/blob/d347bca2bad80420869217282535fb4ff919e8b5/Extras/ConvexDecomposition/bestfitobb.h)

[github.com/bulletphysics/bullet ... fitobb.cpp](https://github.com/bulletphysics/bullet3/blob/d347bca2bad80420869217282535fb4ff919e8b5/Extras/ConvexDecomposition/bestfitobb.cpp)

Any chance we can get this exposed in Urho3D ? 

I think object oriented bounding box it is already calculated when we create a convex hull in Bullet or I am wrong  ?

-------------------------

cadaver | 2017-01-02 01:02:09 UTC | #5

I thought you were talking about fixing the pivot of imported models. For something that's generated at runtime using math, it's OK to use whatever methods to get the result you want, including scene node composition.

Your best bet is to expose the functions you need and make a pull request.

-------------------------

sabotage3d | 2017-01-02 01:02:11 UTC | #6

I found it confusing to implement it in the engine. I did simple centroid solution in my project, seems to be fine for fractured bodies.

-------------------------

