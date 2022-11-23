smellymumbler | 2017-06-04 20:41:01 UTC | #1

I'm using real rigidbody projectiles in my game. First, because it allows the code to be simpler, and second because i want bullets to drop and everything. Unfortunately, i've been stuck with a problem: since some bullets travel really fast, they miss their targets completely. 

Am i missing something?

-------------------------

slapin | 2017-06-03 20:31:12 UTC | #2

I' would better not do bullets using rigidbody on fast periods of the trajectory, I'd spawn it at very last moment so it hits
and falls dramatically. For the rest I'd use raycasts.

-------------------------

KonstantTom | 2017-06-03 20:39:30 UTC | #3

Have you tried `RigidBody::SetCcdMotionThreshold` and `RigidBody::SetCcdRadius`? It can fix your problem, but it slows down your game performance.

-------------------------

slapin | 2017-06-03 20:41:19 UTC | #4

For bullets I really doubt that will help, as it doesn't help even with ragdolls.
I think raycast-based logic will work much much better.

-------------------------

smellymumbler | 2017-06-04 00:24:40 UTC | #5

How would i make a bullet drop with a raycast? Several raycasts and lerp?

-------------------------

slapin | 2017-06-04 05:19:04 UTC | #6

I think I would do like this:

With raycast I would find a point of impact, i.e. a wall.
Then I would spawn RigidBody at that place and using some good velocity, so it won't fall flat
Then I would use mesh/billboard + rigidbody and simulate the fall.
Something like this...

For actual bullet flight I would just use particle or billboard.

-------------------------

hdunderscore | 2017-06-04 05:55:02 UTC | #7

Continuous collision detection will work for it. Doing it with raycasts can also work, you just have to handle the logic over several steps in FixedUpdate, otherwise you'll end up with a "hit-scan"/instant bullet type deal.

-------------------------

slapin | 2017-06-04 06:09:28 UTC | #8

CCD is tough beast. I don't think it is worth it for bullets.
I get 1fps on i7 when enable ccd for ragdolls. to prevent ground penetration.
They still penetrate (no visual difference), but eat all CPU. Not worth enabling in any situation I think.

-------------------------

hdunderscore | 2017-06-04 10:09:05 UTC | #9

For something like a projectile, it should perform quite well. CCD is good for when the rigid bodies are expected to move faster in one step than their size. In that case you can expect collisions to not be detected. You'd turn on CCD for that. The downside of CCD is that it uses sphere collision shape only, so you wouldn't use it for something like a rag doll.

-------------------------

Lumak | 2017-06-04 17:24:02 UTC | #10

if a bullet drops 1 meter per 1000 meter distance, then to find how much is drops per given distance is:
1/1000 = ydrop/distance
distance/1000 = ydrop

example: 
original ray = something you know how to calculate
original ray distance = 200
ydrop = distance * 1/1000 = 200/1000;

deviant ray = Vector3(originalray.x, originalray.y - ydrop, originalray.z).Normalized();

And only requires a single raycast, unless you're applying this to something like self guided missile.
edit: drop would indicate it drops in negative y

Let me also add: i don't know if you ever shot a rifle from long range, but you typically adjust your scope to account for the drop in distance.

-------------------------

slapin | 2017-06-04 19:55:30 UTC | #11

I think for added realism you'd use precalculated trajectory for large distances, not straight line.

-------------------------

