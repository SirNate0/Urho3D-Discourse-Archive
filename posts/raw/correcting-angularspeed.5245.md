urnenfeld | 2019-06-23 09:37:58 UTC | #1

Hello,

I have a RigidBody object, impacting against another. After the collision I leave the RigidBody free spinning for a while(2s).

Afterwards I start correcting the Angular velocity so that when it stops it does in a specific target rotation.

I am doing this corrections in the FixedUpdate() call.

I observe 2 things which are breaking the algorithm:

* When set a specific speed Vx, given the friction I expect on the next FixedUpdate() this Vx to be lower. But it happens to be higher.

* Even forcing Vx to 0, if there is a speed in Vy or Vz, Vx does not stick to 0, but something close to 0.

Then like there is still some inertia movement inherited... which I need to get rid off.

There is an API which I am missing, I am not making the corrections in the correct place(FixedUpdate?)... or there is any physics effects that I am missing.

How should I go if I want to avoid these two effects?

-------------------------

Modanung | 2019-06-23 19:24:53 UTC | #2

When using rigid bodies one should avoid setting transforms or velocities directly. Instead forces should be applied.

When forcing things to stop after all, try adding `RigidBody::ResetForces()`.

-------------------------

Leith | 2019-06-24 07:11:47 UTC | #3

The reason that Vy and Vz have an effect on Vx is because the three axes, X Y and Z, are locked together. Effectively, we have rotation in the XY, ZY and XZ planes.
Let us assume that rotation around the Y axis is in fact rotation in the XZ plane. Naturally, if we rotate about Y, it will change the orientation of the X and Z axes.  This is true of all the axes - rotating any one of them will affect the other two. This is completely expected behavior.

As for the increase in velocity? I'd have to first confirm your results and second dig deep into Bullet to give you a genuine answer - but know that you have more than Friction to use to make bodies "lose energy over time". There is linear and angular damping - these are how you simulate "drag". There are also some secondary "additional damping" constants to play with. Also, there is not merely "friction": there is linear, angular, rolling and spinning friction (the last one is new, and Urho does not yet support it). All these ways can be used to make sure that objects cannot "gain energy" without being influenced by external forces or internal motors.

-------------------------

urnenfeld | 2019-06-24 18:29:49 UTC | #4

[quote="Modanung, post:2, topic:5245"]
Instead forces should be applied.
[/quote]

Then I should be using  [ApplyTorque](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_rigid_body.html#a4875a81f3536bd5433ca6dae642518c1)(const [Vector3](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_vector3.html) &torque) to compensate the angular velocity right? Is this method taking N*m?

[quote="Leith, post:3, topic:5245"]
but know that you have more than Friction to use to make bodies “lose energy over time”. There is linear and angular damping - these are how you simulate “drag”. There are also some secondary “additional damping” constants to play with. Also, there is not merely “friction”: there is linear, angular, rolling and spinning friction
[/quote]

Right! taking all this into consideration, I need to rewrite the whole thing again...

Thanks both for your experienced feedback!

-------------------------

Modanung | 2019-06-24 21:54:49 UTC | #5

[quote="urnenfeld, post:4, topic:5245"]
Is this method taking N*m?
[/quote]

For `ApplyTorque`**`Impulse`** it *would* be `F*m`,  in the case of `ApplyTorque` it's `F*m*t`.... but in my experience it yields better results - considering both realism and gameplay - to "eyeball" and fine-tune values like mass and forces in simulated physics environments.

-------------------------

urnenfeld | 2019-07-04 14:46:33 UTC | #6

Hi,

I have been refreshing physics & looking inside the RigidBody class (both urho3d and bullet sides).

In summary to know what is the *Torque* that I need to apply, I would need to calculate the Moment of inertia (*I*), 

- **τ = I * α**

By checking the angular speed, α is known, but as for *I*, looking in the RigidBody API it does not deal with it much. However I can see some methods dealing with it inside  btRigidBody:

* `const btMatrix3x3& getInvInertiaTensorWorld()`

Which I believe is the information I would need...

What do you think?

-------------------------

Modanung | 2019-07-04 18:28:14 UTC | #7

I must admit I'm not certain.

-------------------------

Leith | 2019-07-05 05:33:25 UTC | #8

Torque is a measure of angular force, ie, "as applied to a point at a distance from the center of mass", eg, a lever , and is usually measured in either foot-pounds (pounds of weight applied to a lever one foot long), or newton-meters (newtons of force applied to a lever one meter long). If you imagine you are tightening the wheel nuts on your car with a horizontal lever, and step on the end of it, we can now measure the torque your bodyweight is applying.


You need to consider the mass of the object, where on the object surface the force is applied, and in what relative direction. You need to think in terms of a point on the surface of the object, and how far it is from the center of mass (ie radius)
More information on what you are trying to achieve will help me to help you.

Perhaps it would be more helpful (or not?) to describe what the inertia tensor actually does...

First and foremost, the inertia tensor describes the distribution of mass around the center of mass origin, along the three principle axes... but how we use it at runtime, it's a tool that lets us convert a linear force applied somewhere on the surface of our body at some angle, into a linear and/or angular momentum, depending on where and how we hit the object (think of a snooker ball, and how the result depends on not just how hard but where you hit it) - if we hit something dead in the middle, it tends to move linearly and not want to rotate, but if we hit it off-center, there is leverage, and it wants to rotate

-------------------------

Leith | 2019-07-05 05:31:36 UTC | #9

I find it useful to use the analogy of tightening wheel nuts with a lever, because as we make the lever longer, the same amount of weight applied to the end of it produces more torque force - leverage

-------------------------

Leith | 2019-07-05 05:53:20 UTC | #10

If you want to achieve a desired angular velocity, you can always manipulate angular velocity yourself, or use a motor, which will attempt to achieve and maintain a desired angular velocity (and acts like a torque spring)

-------------------------

urnenfeld | 2019-07-05 10:58:14 UTC | #11

[quote="Leith, post:8, topic:5245"]
You need to consider the mass of the object, where on the object surface the force is applied, and in what relative direction. You need to think in terms of a point on the surface of the object, and how far it is from the center of mass (ie radius)
[/quote]

Yes... but there is no ApplyToque method which takes a ***Vector3 &position***...
I assumed the ApplyToque methods apply to the edge of the pivotal point...

[quote="Leith, post:8, topic:5245"]
First and foremost, the inertia tensor describes the distribution of mass around the center of mass origin, along the three principle axes…
[/quote]

My first approach was to calculate this by myself, but then  I consider we dont need to, as the mass is known, and the shape of the object could come from the CollisionShape.

Additionally (the post is pretty old) the shape could be simplified to a box in any case:
https://pybullet.org/Bullet/phpBB3/viewtopic.php?t=1575

So I think a better aproach is let the physics engine inform me about this than trying to calculate this myself.

[quote="Leith, post:8, topic:5245"]
More information on what you are trying to achieve will help me to help you.
[/quote]

Sorry I thought I was clear.

Having a object rotating given a collision. I want to smoothly stop it by correcting its angular velocity until reach a target rotation (usually but not always the identity quaternion) with Vector3::ZERO speed at that moment.

[quote="Leith, post:10, topic:5245"]
If you want to achieve a desired angular velocity, you can always manipulate angular velocity yourself,
[/quote]

I have not had good experience with that (read initial post) so I am following @Modanung advice:

[quote="Modanung, post:2, topic:5245"]
Instead forces should be applied.
[/quote]

So If my physics background is correct... I should be able to stop the rotation movement in a given amount of time by a simple ApplyTorque... Dragging it is easy, but If I want to stop it in a target rotation, *I need to control de force* and  to dig a bit more into bullet &  physics before :slight_smile:

-------------------------

Modanung | 2019-07-05 20:48:31 UTC | #12

Be sure to take things like damping into account if it is non-zero. Also, for experimentation you may want to use `ApplyTorque`**`Impulse`** instead, leaving out the time step factor. Given the correct force, the rigid body should stop spinning *instantly*.

-------------------------

Lumak | 2019-07-06 02:50:51 UTC | #13

There's a constraint in Bullet called **btGeneric6DofSpring2Constraint** and will do exactly what you describe without having to manually control the torc or angular velocity. All you had to do was configure and specify the limits on which axis you want to stabilize. 

@1vanK submitted a PR for this a long time ago and I did some testing on it and it worked properly from what I can remember.

-------------------------

Leith | 2019-07-06 04:41:43 UTC | #14

Our support for constraint types in Urho is weak - yes you can access third party subsystems and get things done, but tbh our physics implementation is way less than complete

-------------------------

