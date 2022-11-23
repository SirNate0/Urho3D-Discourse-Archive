scorvi | 2017-01-02 00:57:48 UTC | #1

hey ho
how can i pick a billboard in a BillboardSet ? 
i created a galaxy with billboards and now i have to pick one star to zoom in ... 
should i just create a bounding sphere for every star ?

[spoiler][url]http://postimg.org/image/52frygms7/[/url][/spoiler]

-------------------------

cadaver | 2017-01-02 00:57:48 UTC | #2

Per-billboard picking is not supported because the final orientations of the billboards are only known on the GPU in the vertex shader, and it would require replicating that calculation on CPU side. Therefore I recommend making interactable objects separate. Basically two options:

- Make the star a separate StaticModel and use Octree raycast
- Create a RigidBody + CollisionShape for the star, set the RigidBody to phantom mode so it doesn't actually collide or apply forces, then use PhysicsWorld raycast to pick it.

As long as we're not talking about very large amounts of stars (10000+) visible at once, the amount of objects in the scene should not be an efficiency factor. StaticModels will also be automatically instanced when they use the same mesh + material. In fact making the stars separate objects is better for culling, because a BillboardSet will always be drawn in its entirety if its bounding box overlaps the camera frustum even a little.

EDIT: making billboards individually pickable (at least by some manner of approximation like having them represented as spheres) would be possible, it just has to be remembered that it's potentially very CPU-heavy, comparable to raycast into complex meshes.

-------------------------

cadaver | 2017-01-02 00:57:48 UTC | #3

There is now a sphere approximation for individual billboards when the RAY_TRIANGLE level raycast is used. You get the billboard index in the subObject variable of the ray query.

-------------------------

scorvi | 2017-01-02 00:57:48 UTC | #4

wow thx for the quick reply !!! 

i will try the new implementation out. 

but i have a question about version controll with github:  
 i have downloaded the source code few weeks ago and compiled it. is there now a easy way to update my source files with the new updateds on github ? so that my changes should not be overwritten .... How do you all handle version control with github ?

-------------------------

friesencr | 2017-01-02 00:57:48 UTC | #5

Here is your answer to the git question:

[help.github.com/articles/syncing-a-fork](https://help.github.com/articles/syncing-a-fork)

git remote add upstream [github.com/urho3d/Urho3D.git](https://github.com/urho3d/Urho3D.git)

then every time you want to update

git fetch upstream
git merge upstream/master

naturally you will have to resolve merge issues

-------------------------

Azalrion | 2017-01-02 00:57:49 UTC | #6

I prefer a rebase merge instead of plain merge for keeping my modifications on top of the urho updates. Keeps the history cleaner as well.

-------------------------

