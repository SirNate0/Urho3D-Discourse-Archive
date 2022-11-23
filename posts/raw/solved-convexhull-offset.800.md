sabotage3d | 2017-01-02 01:03:00 UTC | #1

Hi guys,

I am getting some weird offset with convexhull. If I change in Sample 11 Physics this line:
[code]shape->SetBox(Vector3::ONE);[/code]
with this one :
[code]
shape->SetConvexHull(cache->GetResource<Model>("Models/Box.mdl"));[/code]

I am getting a gap when the bodies come to rest. Because of this gap it seems that friction is ignored.

That is the hash number of the commit I am using : 401f478abfa0a5957807f0c80b4b994d7d944ff0

[img]http://i.imgur.com/3B6nx1y.png[/img]

-------------------------

codingmonkey | 2017-01-02 01:03:00 UTC | #2

what for are you using ConvexHull on the cubes?) if in CollisionShape exist the box shape.
Maybe you need using more complex models then you switch shape to convexhull ?

-------------------------

cadaver | 2017-01-02 01:03:00 UTC | #3

Bullet has the Collision Margin property in collision shapes for internal reasons. For shapes like boxes it knows automatically how to reduce the shape size to account for the margin, but for convex hulls it doesn't know how to do that. You can try reducing the margin (in CollisionShape component) yourself, or even setting it to zero. This may result in some other issues like interpenetration or physics instability. However like codingmonkey says, don't use a hull when a primitive shape will do.

-------------------------

sabotage3d | 2017-01-02 01:03:00 UTC | #4

Thanks guys I am just showing the issue if I have more complex shapes the issue is more apparent I remember that I didn't have such problem before. Because of this offset all the rigid-bodies are frictionless . 
I will try the Collision Margin and let you know how it goes.

-------------------------

sabotage3d | 2017-01-02 01:03:00 UTC | #5

For the friction issue I might not be collision margin related it might be related to this issue: [github.com/bulletphysics/bullet3/issues/49](https://github.com/bulletphysics/bullet3/issues/49)

-------------------------

cadaver | 2017-01-02 01:03:00 UTC | #6

Thanks for pointing out the potential friction fix, this looks straightforward to apply to Urho3D.

EDIT: Erwin's fix is now in Urho master branch. Please test if it helps.

-------------------------

sabotage3d | 2017-01-02 01:03:01 UTC | #7

Thanks a lot cadaver .
I just tested your friction fix it works perfectly I tested values ranging from 0 to 1 and the behavior looks correct.
I also changed the margin to 0 and it fixed the offset.
[code]CollisionShape* shape2 = node->CreateComponent<CollisionShape>();
shape2->SetMargin(0);[/code]

-------------------------

