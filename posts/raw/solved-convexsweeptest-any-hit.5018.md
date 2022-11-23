QBkGames | 2019-03-13 07:34:20 UTC | #1

This is more of a Bullet physics internal question rather than Urho, but if anyone knows the answer I appreciate it. I've already posted it on the Bullet support forum, but I haven't got any answers yet.

*What do you pass to the btCollisionWorld::convexSweepTest to get the "any hit" query?*

I just want a fast and efficient way of determining if there is something there, I don't care about what or where or any collision data, just if there are any physics bodies being overlapped by the sweep. I'm guessing you have to override the ConvexResultCallback somehow to get this result, but I cannot figure out how (the documentation on this topic is non existent). I was hoping an appropriate override would be included with the Bullet library (just like ClosestConvexResultCallback is), but no such luck.

And I don't want to use the ClosestConvexResultCallback because it would be horribly inefficient for my purpose, as the query would have to get all overlapping bodies and order them by distance to the sweep origin and return the closest one. I just want the sweep algorithm to stop as soon as it finds something, anything.

-------------------------

Leith | 2019-03-11 03:35:19 UTC | #2

Let's review the arguments for this method:

[quote]
void btCollisionWorld::convexSweepTest (|const btConvexShape *  castShape,
const btTransform &  from,
const btTransform &  to,
ConvexResultCallback &  resultCallback,
btScalar  allowedCcdPenetration = btScalar(0) 
) const
[/quote]

The ConvexResultCallback has two members you need to set up in order to perform a proper collision query:  m_collisionFilterGroup, and m_collisionFilterMask. By default, I expect both to be -1, which means "Everything".

Without lecturing you on how Bullet Collision Filtering works, if we check the Bullet docs for ConvexResultCallback, we can see that it derives from ClosestConvexResultCallback. Essentially, this method is only equipped to return the first, closest object that was hit (and which passed the filtering test).
https://pybullet.org/Bullet/BulletFull/structbtCollisionWorld_1_1ConvexResultCallback.html

-------------------------

QBkGames | 2019-03-12 02:41:00 UTC | #3

From I could gather from the code, ConvexResultCallback is an abstract base class that has the pure virtual function addSingleResult. My guess (without looking much deeper into the Bullet code) is that the algorithm used in the implementation of this function determines whether the result is: "first hit, all hits or any hit" (quote from comment above the convexSweepTest function).
ClosestConvexResultCallback implements the "first hit" algorithm, but nothing implements "all hits" or "any hit" and it's not clear how you would go about implementing it yourself (short of looking deep into the Bullet code and trying to understand it under the hood, which is not what a library user should be expected to have to do).

-------------------------

Leith | 2019-03-12 07:50:41 UTC | #4

Oh, I can explain this! This works for most situations in Bullet, but not a universal solution...

For collision filtering:
You need to derive a new class from ClosestConvexResultCallback (or whatever the query uses) - lets call it MyClosestConvexResultCallback - and override a virtual method called "needsCollision". If you wish to also support the usual bullet groups (layers) and masks, just call the base class method (of the same name) and use its result in your logic as you see fit.

For collecting multiple results:
Add a container (vector, array, list, whatever) to your derived class.
Override the virtual addSingleResult to collect the results (which passed already your filter, if you did that too).

When performing a query, hand in an instance of your derived result container, instead of the default bullet result container. After the query, your container instance holds the results. 
Oh, and I forgot to mention, the result order will usually seem arbitrary, you might want to sort the results.

-------------------------

QBkGames | 2019-03-13 07:34:04 UTC | #5

Thanks Leith, that clarifies things a bit.

-------------------------

Leith | 2019-03-13 07:39:10 UTC | #6

It's not a perfect question, given that Bullet queries use a variety of result container types - so the answer was generalized to deal with more than one use-case... hope it was helpful :)

-------------------------

