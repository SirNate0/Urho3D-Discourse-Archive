GodMan | 2020-03-01 18:01:35 UTC | #1

I have a rocket that has a simple physics capsule on it. I have been testing ray casting to understand it. For my rocket since it is slow moving I would like to check if it comes into contact with something and then ApplyImpulse to that nodes physics body.

-------------------------

Modanung | 2020-03-01 18:54:22 UTC | #2

When your `Explosion` is positioned, it could use a physics sphere cast to select the `RigidBody`s it should affect, followed by some ray casting to deselect the objects that are obscured by walls. Then you could iterate over these and apply an impulse inversely proportional to their distance from the explosion.

If you're looking for mayhem, create exploding barrels. Explosions could deal damage to trigger them.

-------------------------

GodMan | 2020-03-01 18:37:12 UTC | #3

That sounds pretty good to me. I tried to iterate over some nodes to get their rigidbodies, but never got it to work correctly.

-------------------------

GodMan | 2020-03-01 21:42:13 UTC | #4

So this is what I'm doing to see if nodes are with a sphere radius.
```
PODVector<Node*> nodes;
for (PODVector<Node*>::Iterator it = nodes.Begin(); it != nodes.End(); it++)
{
    Node* otherNode = (*it);
    Intersection i = sphere.IsInside(otherNode->GetWorldPosition());

    if (i == INSIDE)
    {
        //Do something
    }
}
```
Left this line out: 	    `Node* ownNode;`
    	`ownNode->GetScene()->GetChildrenWithComponent<Node>(nodes, true);`

-------------------------

Modanung | 2020-03-01 22:15:41 UTC | #5

Apart from the fact that a `Node` is not a `Component`, it would be more efficient to take this route:
```C++
auto* const physicsWorld = GetScene()->GetComponent<PhysicsWorld>();
PODVector<RigidBody*> hitResults{};
physicsWorld->GetRigidBodies(hitResults, Sphere{ center, radius }, mask);

for (RigidBody* b: hitResults)
    b->ApplyImpulse(...);
```

-------------------------

GodMan | 2020-03-01 21:59:20 UTC | #6

I tried to follow the code for ninja snow wars and learn it myself. I'll try what you recommend.

-------------------------

