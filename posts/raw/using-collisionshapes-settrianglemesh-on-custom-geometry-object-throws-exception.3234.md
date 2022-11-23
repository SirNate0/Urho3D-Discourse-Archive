ppsychrite | 2017-06-09 22:38:50 UTC | #1

So I've been trying to give physics to objects made with Custom Geometry (Same as DynamicGeometry sample) but when I do 

    node->CreateComponent<ur::RigidBody>()->SetMass(1.0f);
	ur::CollisionShape *shape= node->CreateComponent<ur::CollisionShape>();

	shape->SetTriangleMesh(object->GetModel(), 0);

It throws an exception, around the shape->SetTriangleMesh part. 
I've also tried using the actual model variable but that throws an exception, too.

Here's how the model is made
    
	ur::SharedPtr<ur::Model> model(new ur::Model(context_));
	ur::SharedPtr<ur::VertexBuffer> vb(new ur::VertexBuffer(context_));
	ur::SharedPtr<ur::IndexBuffer> ib(new ur::IndexBuffer(context_));
	ur::SharedPtr<ur::Geometry> geom(new ur::Geometry(context_));

	ur::PODVector<ur::VertexElement> elements;
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR3, ur::SEM_POSITION));
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR3, ur::SEM_NORMAL));
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR3, ur::SEM_COLOR));
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR2, ur::SEM_TEXCOORD));
	elements.Push(ur::VertexElement(ur::TYPE_VECTOR4, ur::SEM_TANGENT));
	
	vb->SetShadowed(true);
	vb->SetSize(numVertices, elements);
	vb->SetData(vertexData);

	ib->SetSize(36, false);
	ib->SetData(indexData);

	geom->SetVertexBuffer(0, vb);
	geom->SetIndexBuffer(ib);
	geom->SetDrawRange(TRIANGLE_LIST, 0, numVertices);

	model->SetNumGeometries(1);
	model->SetGeometry(0, 0, geom);
	model->SetBoundingBox({min, min + max});
	
Any clue?

-------------------------

slapin | 2017-06-10 03:34:49 UTC | #2

Could you please provide backtraces?
Also isn't there SetCustomTriangleMesh()?

-------------------------

ppsychrite | 2017-06-10 14:32:53 UTC | #3

SetCustomTriangleMesh() is only for the CustomGeometry class, and I don't find it necessary having to manually convert every custom object into CustomGeometry JUST for an easier solution. :sweat_smile:

Here's the stack trace.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/09df77ec3f6ef5fb70525375a25ea9b9e07d5aab.png" width="690" height="134">

-------------------------

Eugene | 2017-06-10 14:54:30 UTC | #4

It would be great if you publish model and example to help others investigate the problem

-------------------------

ppsychrite | 2017-06-10 15:32:58 UTC | #5

Alright.
Here's the full code of how to make a custom geometry
https://hastebin.com/ibekukubow.go

-------------------------

Eugene | 2017-06-10 17:58:29 UTC | #6

Reproduced.
Will investigate it.

-------------------------

Eugene | 2017-06-14 06:29:42 UTC | #7

`IndexBuffer` must be shadowed too.

Probably Urho need better error reporting somewhere around `TriangleMeshData`

-------------------------

ppsychrite | 2017-06-10 18:12:04 UTC | #8

Thank you, that worked. I got rid of it because it would throw a ton of exceptions randomly and occasionally. Thought I didn't need it.

Guess I did :yum:

-------------------------

ppsychrite | 2017-06-12 23:05:49 UTC | #9

Is there some reason for 

    ib->SetShadowed(true);
	ib->SetSize(36, false);

Randomly throwing exceptions?
It seems to have no pattern and happens sometimes.

-------------------------

Eugene | 2017-06-13 11:02:54 UTC | #10

It's hard to say anything without callstack.

-------------------------

ppsychrite | 2017-06-13 16:57:08 UTC | #11

Found it. Happens pretty rarely so took me a few tries.
Exception: http://prntscr.com/fjc1xm
Call Stack: http://prntscr.com/fjc27u

-------------------------

Eugene | 2017-06-13 18:23:35 UTC | #12

Do you use OpenGL build of Urho?

-------------------------

Eugene | 2017-06-14 06:29:42 UTC | #13

Why do you say `numVertices = 36` if you have only 8 vertices?

-------------------------

ppsychrite | 2017-06-13 18:29:51 UTC | #14

Yes I used the OpenGL Build.

I assumed the numVertices was the number of indices, not vertices. Should it be vertices?

-------------------------

Eugene | 2017-06-13 18:36:12 UTC | #15

[quote="ppsychrite, post:14, topic:3234"]
I assumed the numVertices was the number of indices, not vertices. Should it be vertices?
[/quote]

I assume that numVertices is the number of vertices ;)

-------------------------

ppsychrite | 2017-06-13 18:45:12 UTC | #16

Looks like that solved it, you're a lifesaver!
All that's bugging me is the Cubes glitching together.

https://gyazo.com/32f1272a65c80821102bb4de884cb431

-------------------------

Eugene | 2017-06-13 18:59:39 UTC | #17

No chance to help without related code

-------------------------

ppsychrite | 2017-06-13 19:06:20 UTC | #18

Alright, alright. Should've known :stuck_out_tongue:
Here's the same function but improved used to make Cubes: https://hastebin.com/sutewulome.php 
Here's where I define the Bricks: https://hastebin.com/xatuvodevu.php ("data" is a struct containing Scene, Context and so on)

    scene_->CreateComponent<ur::PhysicsWorld>();
is declared, too.

-------------------------

Eugene | 2017-06-13 19:51:30 UTC | #19

Triangle meshes are not allowed to be movable. Use convex hull or other primitives.

-------------------------

ppsychrite | 2017-06-13 19:56:00 UTC | #20

Didn't know convex hulls were valid, thanks! It works now!

https://www.youtube.com/watch?v=Ekv7pEWhlko&feature=youtu.be

Just a tad bit glitchy, which is fine for now I guess.

-------------------------

Eugene | 2017-06-13 20:18:24 UTC | #21

This is crazy. I re-watched this video ten times trying to understang logic of this physic.
Try to draw PhysicsWorld debug geometry to ensure that physical colliders are the same as drawables.
My test app works fine: Editor with two cubes and plane.

-------------------------

ppsychrite | 2017-06-13 20:20:07 UTC | #22

Here: 
https://www.youtube.com/watch?v=rz0zQxz_Y3I&feature=youtu.be

From what it looks like a few lines appear to disappear and reappear randomly.

-------------------------

Eugene | 2017-06-13 20:36:38 UTC | #23

This physics make me headache.

Just a random thought.
AFAIK, Bullet interprets (0, 0, 0) as the center of mass of the body.
Your boxes don't contain (0, 0, 0) and this _may_ make Bullet insane. But I am not sure. Try to use boxes that contain zero point.

-------------------------

ppsychrite | 2017-06-13 20:47:19 UTC | #24

I'm going to try the Model's SetGeometryCenter() function and see if that helps.

EDIT: I don't believe that works as neither

    model->SetGeometryCenter(0, {min + (max / 2)});

or

    model->SetGeometryCenter(0, {max / 2});

help at all.
Having it freeze like this: http://prntscr.com/fjf244 is a bit interesting through.

-------------------------

Eugene | 2017-06-13 20:51:39 UTC | #25

[quote="ppsychrite, post:24, topic:3234"]
I'm going to try the Model's SetGeometryCenter() function and see if that helps.
[/quote]

I've checked code right now. It looks like `Set/GetGeometryCenter` logic isn't used by Urho _at all_. It literally does nothing.

-------------------------

ppsychrite | 2017-06-13 20:56:24 UTC | #26

Well that's strange :confused:
Don't know of any other way to set the origin/center of the model.

-------------------------

Eugene | 2017-06-13 21:01:40 UTC | #27

Try to fix cube's vertices first to make 'em contain (0,0,0). If it works, think about nicer solution.

-------------------------

ppsychrite | 2017-06-13 21:11:10 UTC | #28

I attempted to move the plane 20 down the y axis and make the red rectangle have 0,0,0 in it
The blue cube was on it, fell off, and did a bowling pin strike on it and knocked the red rectangle down.
Extremely bizarre.

https://youtu.be/OeiHTqlO_eU

-------------------------

Eugene | 2017-06-13 21:17:38 UTC | #29

You still have _bad_ physic shapes.
Let me show.
Red brick has its center of mass at the _edge_ of box, 5 units from the top.
Blue brick still has out-of-shape center of mass.
Both variants are physically meaningless. There is no valid way to simulate such bodies. Center of mass must lay inside the body.

-------------------------

ppsychrite | 2017-06-13 21:22:05 UTC | #30

Okay! I think I got what you mean.
I'll try to find a function to set the center of mass or origin point.

-------------------------

Eugene | 2017-06-13 21:29:00 UTC | #31

AFAIK, there is no such function. Urho probably inherited this Not Very User Friendly intefrace from the Bullet. Generic way is to prepare physic body with center of mass at zero and then use node transforms to move it.

It shan't be very hard to add 'Center of Mass' parameter to RigidBody, but it shall be implemented very carefully since there is a lot of complex logic.

-------------------------

ppsychrite | 2017-06-13 21:39:08 UTC | #32

If I'm understanding you then I should set the transformation of the node to make the position the center?
I'm doing node->SetTransform(-max / 2, {0.0f,0.0f,0.0f}); Which does make the origin point the center, yet that still doesn't work.

-------------------------

Eugene | 2017-06-13 21:43:29 UTC | #33

First of all, you should ensure that zero coordinate is inside of the shape described by vertices.
Tune parameters of your bricks to achieve this.

-------------------------

ppsychrite | 2017-06-13 21:49:47 UTC | #34

Oh my god, thank you! That worked!

https://youtu.be/3CiSn_IsBkw

I think I'm going to make some sort of system of them being spawned at 0,0,0 then moved.
Thank you for your tremendous help!

-------------------------

Eugene | 2017-06-13 21:58:00 UTC | #35

I am glad to hear it.

Try to keep center of mass physically valid. Parameters of `Brick` constructor are the corner and the size of the cube. Your corners contain zero Z coordinate. This means that center of mass is on the top face of the cube. This is still error-prone, because 'valid' physical objects can't have CoM at the surface. This may lead to unnnatural movements. Just beware.

-------------------------

slapin | 2017-06-14 16:30:43 UTC | #36

The funny thing is that you often need to have center of mass out of your body, especially in vehicle simulation cases.
Of physics engines only Havok supports this straight-forward way, as it allows rotational momentum offsets.
BTW, it is not possible to have proper collision AND proper vehicle physics in Urho, i.e. cars will always stand on wheels and never lay on roof. Or you have to use box as collision (which will properly rotate and flip, but will not collide properly). So you can't have different bodies for physics momentum calculations and collisions, which is not nice...
I wonder why so little physics engines do this... It is probably possible to do this in Bullet, but it looks like nobody did this.

-------------------------

Eugene | 2017-06-14 16:41:53 UTC | #37

[quote="slapin, post:36, topic:3234"]
The funny thing is that you often need to have center of mass out of your body
[/quote]

May you explain the physical meaning of such CoM and how it should behave?
It's hard for me to understand.

-------------------------

ppsychrite | 2017-06-14 18:40:12 UTC | #38

Yeah! My system works perfectly.

https://www.youtube.com/watch?v=fAPa-QJoUnM

How it works is that it creates it with 0,0,0 in the center and then moves it to the desired position and sets it's mass.

-------------------------

slapin | 2017-06-15 20:00:58 UTC | #39

You might want to read my whole post.
CoM in Bullet is used for 2 purposes - center of actual mass and a point around which a body rotates.

Imagine the following - you want a van, which is hard to handle, i.e. if you turn in too short radiuses, it will lay on side.
For that to actually work you need to offset the actual center of mass to up of the body (Volition guys do offset center of mass even above the body, which I mention, but I don't insist on it), but it should still turn around middle or bottom.
Otherwise it simulates orbiting planet (which is still good example of having CoM out of body, but that is not important
for my point). This is where bullet is lacking in simulation of vehicles and other things. The offset of CoM is minimum
required thing. You need to specify somehow that top of body is heavier than bottom, even though collision mesh on the above is smaller. This makes it extremely hard to do GTAIII-style vehicle physics I aim for,
The only partial workaround I found was to change collision shape to convex hull if collision happens with anything but ground. Otherwise use box. But this does have a lot of artefacts. For most effects it is easier to just animate thing
in Blender than use physics. Volition guys use Havok, which uses separate bodies for collision and physics calculations. I really want something like this implemented for Urho, but I really don't know enough to even imagine this.

-------------------------

George1 | 2017-06-16 16:16:54 UTC | #40

If you make your vehicle thinner, lighter, higher. Make the wheel spin faster and have the steering wheel to turn faster. Have slightly higher coefficient of friction. If your car run at a fast speed, with a sudden turn, it will roll over like no tomorrow.

I think centre of mass calculation usually assume uniform distributed weight, which is the location of the centroid of the geometry.

-------------------------

slapin | 2017-06-17 14:01:37 UTC | #41

Well, there are poor man tricks for this, like making cars flatter and boxier (like in original GTAIII),
but that is really not something which I want to do. I;d prefer something more life-like without weird tricks.

-------------------------

slapin | 2017-06-17 14:07:49 UTC | #42

Also if you use realistic collision shapes, physics in Bullet makes it not possible for car to not get to wheels.
For some people it is nice and cool, but if you want to make sure car will behave more realistic (i.e. stays on roof or side) it is not possible to do unless you set collision shape as box. So Bullet is wicked and strange. I remember working with some OSS engine which allowed offsetting of center of mass, but I don;t remember the details. The only one I know working regarding this is Havok. Anyway, with Urho we have only Bullet, and it doesn't allow to do adequate vehicle physics.

-------------------------

Modanung | 2017-06-17 14:30:08 UTC | #43

From the [Bullet Forums](http://bulletphysics.org/Bullet/phpBB3/viewtopic.php?f=9&t=1506):
[quote="Erwin Coumans"]
The center of mass is the center of the btRigidBody. So if you want to shift the center of mass, you need to shift the collision shapes, and graphics rendering the opposite way. You can use a btCompoundShape to shift the collision child shapes. Also, you need to correct the center of mass graphically. The motion state has some helper functionality to make this easier.
[/quote]

-------------------------

slapin | 2017-06-17 14:45:54 UTC | #44

I wonder why people here think I can't use Google :)

As I mentioned before, it is necessary to have CoM != CoG != pivot.

The best is to have different collision shapes for collision and momentum calculations (forces calculations).
The minimum - have CoM offset.
Otherwise you make flat/boxy cars, use box collisions and model your graphics knowing you need CoM at center.

-------------------------

Modanung | 2017-06-17 14:50:36 UTC | #45

[quote="slapin, post:44, topic:3234"]
I wonder why people here think I can't use Google :slight_smile:
[/quote]

I wonder why people use Google at all. ;)

-------------------------

slapin | 2017-06-17 14:50:40 UTC | #46

Example: You have van-type vehicle with high CoM. because CoM == pivot, the behavior will be unrealistic.
One can use tricks like shifting geometry + collision at run time in some cases, but not many, in general one have to either animate physics behavior or just exclude vehicle complex behaviors from gameplay.

-------------------------

slapin | 2017-06-17 17:31:52 UTC | #47

For Unity, which doesn't have this problem, they resolve some issues like this:

https://forum.unity3d.com/threads/how-to-make-a-physically-real-stable-car-with-wheelcolliders.50643/

Also it looks like Bullet uses CoG, not CoM for momentum, so moving CoM from CoG using offsets of collision
bodies make physics behave weird. i.e. if I move CoM farther from CoG the body rotates longer and with more energy than if CoG os closer to CoM, which makes me think that rotational momentum is considered so that CoG is forces center, thus body sometimes have explosive rotation. Try long and thin CollisionShapes with CoM offset to one end, and apply torque to them. So if one wants to do cars for Urho3D which behave properly, he will have to be able to override forces so that to have control over CoM and rotational momentum regardless of geometry of collision shapes,
or even make possible to use different bodies for forces and for collisions. That would be very interesting challenge,
too bad I don't have time for it ATM, probably somebody more experienced in physics engines can do it.

-------------------------

slapin | 2017-06-17 18:06:59 UTC | #48

BTW, as I see you use RaycastVehicls stuff in your little game. How the stuff is going? I want to see YOUR cars rolling!
(and siding and other cool stuff like getting in/out of car)...

-------------------------

Modanung | 2017-06-17 18:37:09 UTC | #49

I've been working on other projects. I was pretty content with the driving earlier, but messed up some values - now the cars are all wobbly - and decided to look into it later. Some vehicle editor with built-in test-drive mode would be ideal.
[quote="slapin, post:48, topic:3234"]
I want to see YOUR cars rolling!
[/quote]
Actually I don't think I want functional cars in OGTatt to be able to roll over, for gameplay reasons. Moving their centre of mass down is exactly what I intend to do, maybe with an angle limit before 90 degrees.

-------------------------

slapin | 2017-06-17 20:43:47 UTC | #50

Well, I did the editor for myself but it is heavily attached to my car structure, I don't think it might be used for anything else...
I think you could use just separate scene where you can tweak all values in text file and drive, that is easier than making whole editor and have the same level of usability.

-------------------------

