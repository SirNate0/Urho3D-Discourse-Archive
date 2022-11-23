att | 2017-01-02 00:58:32 UTC | #1

Recently I create a driving car demo like the sample vehicle demo.
But the car is not good.
So I think the engine maybe need support bullet raycastvehicle. :smiley:

-------------------------

cadaver | 2017-01-02 00:58:32 UTC | #2

The heightfield and trimesh collision in Bullet are not nice, they will generate broken normals which will indeed cause jitter of a physical (wheels are rigidbodies) vehicle.

It should be possible to integrate the btRaycastVehicle: it could be a component. However the API is inflexible compared to Urho's own components; you're expected to provide all tuning parameters when constructing the object, so something like editing the parameters will mean constantly deleting and recreating it (not a problem in normal game usage)

Another option would be to replicate the functionality of btRaycastVehicle without actually using its code. Casting rays downward and moving a rigidbody manually each physics frame is already possible.

-------------------------

