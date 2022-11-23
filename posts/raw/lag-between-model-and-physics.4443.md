extobias | 2018-08-08 19:47:49 UTC | #1

Hi, there
I'm doing a simple physics test with a RigidBody, applying an impulse on forward direction. 
I used 19_VehicleDemo sample to implemented. Does anyone have any hint about why is going on? 
I am aware that there is already a vehicle implemented with raycast. but I'm doing these tests to better understand how it works.
Thanks 

![Screenshot%20from%202018-08-08%2016-36-25|690x431](upload://hlIg89xwcrwSEeYiLX8lkga6GFV.png)

-------------------------

Modanung | 2018-08-08 20:23:36 UTC | #2

It's hard to tell from the screenshot alone what's going on.
This could be due to interpolation (and be normal) or mispositioned components...
But since you're applying a constant force - I presume - it's better to use `ApplyForce(force * timeStep)` instead of `ApplyImpulse(force)`. Also it's best to apply forces during the `FixedUpdate` event.
If that doesn't help, sharing some code will.

-------------------------

Bananaft | 2018-08-09 14:11:08 UTC | #3

I'm sure it's normal physics interpolation, given it's a car sized object moving at 135 KmH, and in such tiny window it's probably renders at 200fps.

You can make it go away by enabling vsync or setting max fps to 60. But it's not a bug, and you should check how your physics work on vastly different fps values.

-------------------------

extobias | 2018-08-09 11:23:13 UTC | #4

I have reset the values ​​of fps in 30, both of the engine and of the simulation.
I will try with the vsync option

-------------------------

extobias | 2018-08-08 21:41:52 UTC | #5

Im using ApplyImpulse(force * timeStep) in FixedUpdate. From what I see its the way btRaycastVehicle is doing it. I dont have the code now but I will share it.

-------------------------

Modanung | 2018-08-08 21:48:00 UTC | #6

https://gamedev.stackexchange.com/questions/34069/what-is-the-difference-between-an-impulse-and-a-force-related-to-a-physics-engin#34071
> An impulse is applied instantly, so it does not depend on the time step. You would use an impulse when you want to give a fixed boost of speed to something, or the physical action happens too quickly (ex. bullets/gun ricochet, collisions, jumps, instant speed ups).
Meanwhile a force changes the speed directly proportional to the time step. You use it for things that have an over time effect (ex. gravity, long springs, air resistance).

But that's just another place in the web. ;)

-------------------------

