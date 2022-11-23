Elendil | 2018-12-13 11:31:50 UTC | #1

1. How to make collision for camera, to not go through objects?

My idea is, create physic - add CollisionShape sphere and RigidBody. It is good idea use Bullet for that?

After I do that, my CollisionShape was attached in to camera, but when I moving with camera, collision not working, only when I add Mass(value more then 0).  But then camera start fall down.

Maybe I need control CollisionShape instead Camera? Or PhysicBody? What is right control for that?

2. All collisions are made with Bullet or is there some simple physics? I want create spaceship which can be controlled only above ground. It can hit objects, shoot missiles and enemies can hit player spaceship to make damage. Isn't Bullet too much for that? I found Bullet prety fast when I run PhysicStres Demo, but it was only simple cubes.

3. Can be physic object animated? For example in some old platform games, there was some moving platforms which will interact with player character.

4. Can have physics animated bones? For instance, I animate some object which can be twisted to another shape which affect collisions. Can Urho3D do that?
Maybe better example is giant character with character collisionShape. That means physics object for giant will be character mesh not capsule, sphere or box.

-------------------------

Modanung | 2018-12-13 18:45:56 UTC | #2

1. You can cast a ray from the target towards the camera and move the camera closer if it hits anything. Does that seems like a solution you'd feel comfortable with? If you're going to use `RigidBody`s and `CollisionShape`s you should not move the `Node` directly, but instead apply forces to the body.

-------------------------

Elendil | 2018-12-13 18:58:44 UTC | #3

[quote="Modanung, post:2, topic:4741"]
You can cast a ray from the target towards the camera and move the camera closer if it hits anything. Does that seems like a solution you’d feel comfortable with?
[/quote]

No. 
I have sample from wiki tutorial where user control camera as first person character and fly around scene with boxes. I apply physics for boxes and camera and now I want camera not move through boxes. It's looks like your second sentence is how to do it. But maybe there are other solutions?

-------------------------

jmiller | 2018-12-27 20:15:34 UTC | #5

Bullet is general and configurable enough to serve a wide range of use cases
  https://urho3d.github.io/documentation/HEAD/_physics.html

 [url=https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_rigid_body.html]RigidBody[/url] has some possibly useful methods including
     RigidBody::SetUseGravity (bool enable)
     RigidBody::SetGravityOverride (const Vector3 &gravity)

-------------------------

