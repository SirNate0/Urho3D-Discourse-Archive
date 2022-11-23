GodMan | 2019-05-11 00:09:19 UTC | #1

I'm thinking maybe it's best to let the physics part of the node accomplish this, but I'm not to sure. I'm trying to setup a basic melee system for AIs. Also thinking I may need to account if the AI is also facing the other node as well.

Thoughts??

-------------------------

Leith | 2019-05-11 04:34:55 UTC | #2

Hi, GodMan!
I will answer your question in several posts, because this is one of the most important questions anyone can ever ask in gamedev. I am super happy to be both able, and qualified, to answer it!

The cheapest test is to calculate the (magnitude of) square of the distance between the two positions, and compare it to the (magnitude of) square of the radius. Note that we don't need to use square root, which is what makes this version of the classic point-in-sphere (or circle, for 2d) test so cheap...

To compute the squared distance between the two positions, use DotProduct as follows:
[code]
/// Compute distance between two points
Vector3 deltaPos = Node->GetWorldPosition() - SphereOrigin;
/// Compute magnitude of distance squared
float dotResult = deltaPos.DotProduct(deltaPos);
[/code]
Now compare the result of the dotproduct to (radius*radius).

If the length of radius squared is greater or equal to the dot result (distance between points squared), then the node origin is inside the radius.
But if length of radius squared is less than dot result, then there is no intersection - point is outside sphere (or circle).

This logic can be easily extended to test for intersection of two spheres (or circles) of any radius.

Urho3D does have some canned functionality for this kind of thing, but I have not looked inside to see how optimized it is (or isn't).
[code]
                // Define a theoretical Sphere around the current Zombie
                Sphere sensor(zombiePos, 5.0f);

                // Perform a proximity test of the zombie sphere and player's position
                Intersection i = sensor.IsInside(playerPos);

                // If player is close to zombie, set zombie's target to player character
                if(i == INSIDE)
                    (*it)->target_ = character_;
                // else clear the zombie's target
                else
                    (*it)->target_ = nullptr;
[/code]

-------------------------

Leith | 2019-05-11 03:21:01 UTC | #3

To account for the Facing Direction of your AI, we can again use a DotProduct - only this time we will hand in two Normalized Direction Vectors... 
Dotproducts are one of the most powerful and useful tools in a game programmer's toolbox.
One of the most common things we use them for is to compare two (unit-length) direction vectors to see how similar they are (or aren't). I use DotProducts in AI Steering Behaviours (eg chase, evade) all the time, but they can be applied to many kinds of problems (ask me about the relationship between dotproduct and the plane equation...)
[code]
/// Find the Direction from Enemy to Player:
Vector3 targetDirection = (PlayerWorldPos - EnemyWorldPos).Normalized();
/// Find the Direction that the enemy is facing
Vector3 facingDirection = EnemyNode.GetWorldDirection();
/// Compare the two normalized direction vectors
float dotResult = targetDirection.DotProduct(facingDirection);
[/code]
Now we examine the dot result - since we used two Normalized vectors, the dot result is going to be a value between -1 and +1 ... we can derive some meaning from the result.
+1 indicates that the Enemy is facing directly toward the target.
(Values near +1 indicate that the Enemy is almost facing the target)
-1 indicates that the Enemy is facing directly away from the target!
(Values near -1 indicate that the Enemy is facing almost directly away...)
0 indicates that Target is perfectly on the left or right hand side of the enemy, ie at 90 degrees, with respect to Enemy Facing Direction)

So to limit the AI's vision from a full sensor sphere to a half-sphere (which faces the same way as the AI agent), we merely need to check that the dot result is positive (well, >=0, and also, that target is within range of the sensor radius).
If we want to reduce the AI's vision to a Cone, we need to make sure our dot result is not only positive, but relatively close to 1... and we still need to check if the target is within range.
[code]
if(dotResult > 0.7f)
   // target is within angular limits of enemy's viewing cone ... now check the distance...
else
  // target is outside of the viewing cone, so do something else, or do nothing.
[/code]

-------------------------

Leith | 2019-05-11 04:37:59 UTC | #4

Finally, if we want to limit the viewing cone to a specific cone angle?
https://www.mathsisfun.com/algebra/vectors-dot-product.html

We see that one way to express the dot product (which is not the first one I learned) is:
dotResult = |A| * |B| * Cos(Theta)
where Theta is the angular difference between the two input vectors, and the other two terms are "magnitude of vector" A and B... length of A, * length of B, * cos angle, is our dot result...

Given that magnitude of A and B are both 1 (since we used normalized direction vectors), that means that:
dotResultCutoff = Cos(Theta)

where Theta is the desired inclusive angle of the cone, in Radians.

Therefore,

if(dotResult >= dotResultCutoff) ...

I know, all this maths stuff can seem daunting if you're new to it, I guess my point is that you don't need to really deeply understand how the maths works in game coding, you just need to be able to recognize which "common" math tools might be leveraged to solve a specific problem (if it involves vectors, then dot and cross product operators are likely to be involved in optimizing the solution).
Actually understanding what happens inside mystical math functions is definitely useful too, as it helps your ability to determine which math tools can be retargetted to most efficiently solve your problem at hand, but it's not vitally important to know what goes on under the hood, as efficiency in game development is generally measured in development time, and not runtime performance.
For the record, I failed math at high school (private school, on a scholarship), because I was bored, because I saw no way to apply it.

Very closely related to the 3D "plane equation".
Our dot result is effectively the solution of the D term in the plane equation.

This information is out of scope of your original question, but I wanted to reinforce that actually understanding the math leads to ways to solve new problems using old solutions - as opposed to just fighting each problem on its own terms.

-------------------------

GodMan | 2019-05-11 21:12:06 UTC | #5

Great post @Leith

Thanks

-------------------------

jmiller | 2019-05-12 00:05:40 UTC | #6

Similar questions and a variety of approaches.

https://discourse.urho3d.io/t/object-within-radius/3252

https://discourse.urho3d.io/t/how-can-i-detect-the-object-nearby/4532

-------------------------

GodMan | 2019-05-12 00:14:17 UTC | #7

Odd I did a search, but it did not bring those results up.

-------------------------

Leith | 2019-05-12 05:49:59 UTC | #8

I should have clarified : when I mentioned cones, I was talking about conical sections of a sphere, as projected from its origin... not true cones, but in the context of sphere/circle tests I hoped that would be self-evident. Anyway, consider it clarified.

Now, the stuff I presented works in all cases, not just for things that "have physics".
But if things do have physics, then yes, we can leverage the physics engine to accelerate our "spatial query", and one of the most important parts of doing that, is to properly implement "collision filter masks" (think of it like a selection filter). If you wish to accelerate your sphere intersection tests using physics, I'll have to write a separate response. It's totally valid to leverage the physics engine to accelerate spatial queries, but not everything "has physics" so we can't rely on that for general queries.

Basically, the stuff I presented can be applied for pairwise testing, but it can't tell us "what stuff the sphere is touching" or provide us with a way to quickly determine what might be, let alone what is touching the test sphere.

I use physics sphere testing to gather a list of nearby candidate stuff. It's a valid method.

-------------------------

Leith | 2019-05-14 04:54:16 UTC | #9

In order to accelerate sphere proximity queries using Bullet Physics, I think the best option is btPairCachingGhostObject. Note that there is no Urho3D wrapper for that particular class, but we can still access it and use it in our C++ code. This is a specialized kind of trigger object, and we can provide any of the usual candidate Shape objects, not just spheres. I just happen to know that the code for sphere testing is well optimized, so there is no harm in taking advantage of existing code.
 Like regular trigger objects, ghost objects do not play any part in collision responses, just collision detection. But unlike regular bullet physics objects, this "pair caching" version of a collision object, keeps a list of all the other physics objects that intersect its volume. This means that instead of performing a bunch of pairwise collision tests on your scene objects, you can just ask the ghost object what it's touching.

[quote]
when i meet a new math tool, i fall in love with it, its a hammer, i can use it everywhere, i dont need a screwdriver, i have a magic hammer! but then after a while i get jaded, and its just another old tool in my old tool box
[/quote]

-------------------------

Modanung | 2019-05-13 12:11:41 UTC | #10

[quote="Leith, post:9, topic:5144"]
...and its just another old tool in my old tool box
[/quote]
Until you discover chiselling by combining your old hammer and screwdriver into something that feels like a new tool altogether. :)

-------------------------

Leith | 2019-05-14 05:03:54 UTC | #11

man, that tool sounds cool, i want one right now, and i am happy to advertise them

I've mentioned that I failed math at high school, I was bored and saw no way to apply it.
The only part of math that captured my interest, was trigonometry.
I fell in love with curves, with tangents, and with the simplicity of the math.

When I was 19, and wanted to become a toolmaker and precision engineer, I was tested on my math. My understanding of trig got me into my first trade apprenticeship. I would become a robotics programmer for the big guns in that industry. I would run rings around the oldschool engineers with my amazing trig skills. But in truth, although I had mastered geometry and algebra, my math skills were still quite ordinary, and I still saw no way to apply a lot of the math I had touched on, like hamiltonian equations, matrix math in general, set theory, it was all Greek to me - Hell, I could not read Greek Notation, I was happy to be able to read CamelCase.

When I met her (Maths), I was not immediately attracted.
It took a long time for me to learn to love her.
She is beautiful, and I am a fool for not noticing her beauty earlier in my life.

-------------------------

Jens | 2022-10-13 10:48:05 UTC | #12

```
float distance = Vector3.Subtract(raySend.Origin,sphereRes.Position).Length;

```

-------------------------

