cqrtxwd | 2022-07-18 19:01:06 UTC | #1

```
  auto octree =  scene_->GetComponent<Octree>();
  Vector<Drawable*> result;
  auto search_sphere = Sphere(bob->GetNode()->GetWorldPosition(), 10000.0);
  SphereOctreeQuery query(result, search_sphere, DRAWABLE_ANY);
  octree->GetDrawables(query);
```  
here is my code, I add several node in scene, I try to use GetDrawables() to get objects near my character，but nomatter what I try, GetDrawables() only return one result, and it's "Renderer2D".
This function can't find StaticSprite2D nor AnimatedSprite2D.
Did I misuse this function? can't find any example in samples

-------------------------

JSandusky | 2022-07-18 19:09:32 UTC | #2

`Renderer2D` **is** the Drawable for all downstream `Drawable2D`s. You'll have to add query functions to `Renderer2D` to do stuff like a `GetDrawables(AABB, ...)` etc. Then you first get your `Renderer2D` and call those query functions.

If you have `RigidBody2D` on stuff then you can query through `PhysicsWorld2D` if that will work for your needs.

-------------------------

cqrtxwd | 2022-07-18 19:29:15 UTC | #3

[quote="JSandusky, post:2, topic:7297"]
You’ll have to add query functions to `Renderer2D` to do stuff like a `GetDrawables(AABB, ...)` etc
[/quote]

Could you please be more specific about adding query functions to `Renderer2D`？Let's say If I wan't to find all the  StaticSprite2D around my character，how do I add query function to  `Renderer2D`?

-------------------------

JSandusky | 2022-07-18 23:34:10 UTC | #4

You add a function that loops over the list of `drawables_` in `Renderer2D` and checks if they are contained within a circle/box/polygon (whatever you want). If you want to restrict them to a specific type then you can do that through templates (`drawable->GetType() == T::GetTypeStatic()`) or an explicit StringHash (`drawable->GetType() == typeHash`), etc.

You just do whatever you want. Maybe you need it to be fast and you add in some quad-tree maintenance or something - it's literally w/e you want to do because there is nothing there.

-------------------------

Eugene | 2022-07-19 11:32:43 UTC | #5

[quote="JSandusky, post:2, topic:7297"]
`Renderer2D` **is** the Drawable for all downstream `Drawable2D`s
[/quote]
Technically, Drawable2D is still Drawable, except it's not rendered directly. So it *could* support raycast queries, if only Drawable2D provided OnWorldBoundingBoxUpdate...
Wait, it does. So it sould work, no?
![image|690x230](upload://4kt53MvCSoOEdE6tFiHkeZTlVvj.png)

-------------------------

cqrtxwd | 2022-07-19 15:48:07 UTC | #6

It seems that I have to change the source code of Urho3D
You mentioned I can use PhysicsWorld2D, but I only found a RayCast() funtion, Is there any funtion like SphereCast() which I found in PhysicsWorld.h

-------------------------

JSandusky | 2022-07-20 01:36:39 UTC | #7

Like a circle? No, there is only `GetRigidBodies(...)` that takes a Rectangle. Adding a circle or other shape query isn't trivial and involves changes going all the way down into Box2D's guts (unless brute force testing every body then that can be done Urho side - again you have to modify sources).

-------------------------

SirNate0 | 2022-07-20 03:18:43 UTC | #8

If you can get all of the bodies within a rectangle, it's probably efficient enough to just use that and then filter the resulting list with a simple distance check against the radius of your circle (better, radius squatted, as you save the sqrt call). Even doing a 2d capsule (convex hull between the two circles forming start and end points of the sphere) cast doesn't get that much more complicated, though once you start adding long casts along diagonals instead of just a circle you start having to filter out most of the results instead of keeping most of them in the rectangle, assuming the rectangle must be axis aligned.

-------------------------

JSandusky | 2022-07-20 05:17:38 UTC | #9

You could probably take the union of 3 rectangle queries and call that good enough (one tall, one wide, one median - forming a crude raster circle). 

While you can filter (that's really the ideal approach), the general problem is that if you're already leery about changing source code - the work required to filter RigidBody2D's contained CollisionShape2D's is probably too much once you account for add in accounting for offsets and the like.

-------------------------

