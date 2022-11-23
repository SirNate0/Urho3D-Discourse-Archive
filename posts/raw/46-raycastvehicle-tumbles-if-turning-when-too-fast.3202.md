smellymumbler | 2017-06-03 20:24:05 UTC | #1

Did anyone notice that if you accelerate a lot with the vehicle and then press left or right, the vehicle tumbles? How would you fix that? Following a more arcade-ish physics theory, it should just be harder to turn. Kinda like this: 

http://www.edy.es/dev/vehicle-physics/demo/

Should i just add more weight? Is there any good documentation on the Bullet side of things? Like tweaking, etc.

-------------------------

slapin | 2017-06-03 20:43:48 UTC | #2

That is intentional. It should turn over.
You have control over this. Check SetWheelRollInfluence.

-------------------------

slapin | 2017-06-03 20:45:08 UTC | #3

There is very little docs on Bullet, that is nature of the library. Just ask here. Also you can consult source code,
it helped me a lot. But some things are confusing yet, and nothing can be done about it.

-------------------------

slapin | 2017-06-03 20:53:41 UTC | #4

As for making harder to turn, you could implement this by adding extra forces, like side forces depending on torque. Or something. Bullet RaycastVehicle doesn't support that. All I did was wheel rotation logic, I wanted to do the rest of missed things, but was feeling that will never end. But you can implement all stuff.
After reading og RaycastVehicle code in Bullet I think the far distant goal would be to implement fully featured car for Urho, having all needed effects, one can base off Bullet RaycastVehicle, but extend some things.

There are great articles like this which might help you on the path.
http://www.asawicki.info/Mirror/Car%20Physics%20for%20Games/Car%20Physics%20for%20Games.html

-------------------------

smellymumbler | 2017-06-04 00:25:38 UTC | #5

Thanks a lot for the info. I'll try to make some adjustments and keep posting if i get stuck. :)

-------------------------

