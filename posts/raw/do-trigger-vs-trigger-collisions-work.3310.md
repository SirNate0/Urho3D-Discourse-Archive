Alex-Doc | 2017-07-02 11:37:10 UTC | #1

Hi, I'm experiencing an issue with two triggers colliding with each other and I'm having troubles to find out why. 
They should be calling the collision start and end events, but doesn't seems they are.

Can anyone confirm if Trigger vs Trigger collisions do work out of the box?

-------------------------

Lumak | 2017-07-02 20:12:31 UTC | #2

As far as I can remember, trigger vs trigger collision does not work because bullet expects triggers to be static and static objects, as the name implies, do not move.

-------------------------

Alex-Doc | 2017-12-27 11:05:52 UTC | #3

Thanks!

If anyone else is having the same issue, this was my solution:

```
bool Weapon::IsCollidingWith( Node* other )
{
   if( !other )
      return false;

   CollisionShape* col = node_->GetComponent<CollisionShape>();
   if( col )
   {
      CollisionShape* otherCol = other->GetComponent<CollisionShape>();
      if( otherCol )
      {
         Intersection collision = col->GetWorldBoundingBox().IsInsideFast( otherCol->GetWorldBoundingBox() );
         return ( collision & ( Intersection::INSIDE | Intersection::INTERSECTS ) );
      }
   }
   return false;
}
```

Not sure about how fast it is, but it seems to work.

-------------------------

