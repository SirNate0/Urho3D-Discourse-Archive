krokodilcapa | 2017-01-02 01:12:06 UTC | #1

Hi!

I've tried to replicate ragdolls, but on the client side it doesn't work. How can I replicate manual controlled bones?
Thanks!

-------------------------

Enhex | 2017-01-02 01:12:06 UTC | #2

Just a side note - games usually make ragdolls a client-side effect because they're expensive to network.

-------------------------

krokodilcapa | 2017-01-02 01:12:06 UTC | #3

I know, but in my case there wouldn't be too lot ragdolls - only a few one in one time. By the way, there are ways to optimize networked physics: for example send  body orientations and positions only when it changed since the last time, and also give a treshold of changes (so send message only if a body moved more than 5cm since the last message)
I don't know yet if Urho already using this kind of optimizations, I just wanted to know first that why don't it working while simple bodies seems to works online, like a simple box with rigid body, or the ball in the Scene Replication sample.
Anyway, I've took a small look on the code, and found "Create bones as local, as they are never to be directly synchronized over the network" so maybe the reason why the way of ragdoll in the CreateRagdoll sample not working online, because I creating the ragdoll bodies to only server side node's child?
I have to dig more into the Urho code of course, but I hoped that this question will save some time for me, maybe I just didn't noticed a function what enables manually controlled bone replication?

-------------------------

rku | 2017-01-02 01:12:06 UTC | #4

What Enhex said. Is replicating ragdoll state essential to gameplay? If not - you dont have to go through pains to synchronize it because it really is pointless.

-------------------------

cadaver | 2017-01-02 01:12:07 UTC | #5

For API completeness it could make sense to optionally allow the skeleton bones to be created replicated, with the caveat that you're likely making a bad decision regarding bandwidth use.

Another possibility is that you write your own network message to manually sync a skeleton and you simply send that from the server periodically according to your own update logic.

-------------------------

krokodilcapa | 2017-01-02 01:12:07 UTC | #6

Thanks Lasse, I planned the second possibility, what you've wrote, but I wanted make sure if I just missed some enable/disable function for that bone replication or not. 
Anyway, as I know Bullet has a possibility to set the physics calculation to fix on server and client side too, so it should be the same (at least very closely) results on both sides. The base replication (like the balls in the Scene Replication sample) uses this way, or server sends the body positions/rotations to the client side object's "fake" physics body? And if the second one used, then can you confirm if there are this kind of optimizations what I've wrote before - change threshold, and message only on non-sleeping bodies?

-------------------------

cadaver | 2017-01-02 01:12:07 UTC | #7

There is no change threshold, so any time the position or rotation changes even slightly, a message is sent on the next network "frame". Sleeping bodies don't change the transform so they also don't generate messages.

You have the option to create rigidbody / collisionshape as local on the server to avoid creating the body on client (in this case linear/angular velocities don't have to be replicated to client, saving some bandwidth) But by default the rigidbody is just as "real" on the client, and I'd suspect that for ragdolls physics you need that.

-------------------------

krokodilcapa | 2017-01-02 01:12:08 UTC | #8

Allright, my final (sor far) concept will be the next:
I'll keep the bones as local, and when ragdoll is active, the server will send only the current moving ragdoll bone's position and rotation to the clients (using flags so client will know which bone need to update from the message). I will use a small threshold for positions and rotations too, and also a slow rate for the message sending, but the client side ragdoll bones will interpolate between the latest positions, so I avoid the spectacular lagging.
Then I'll see how much I hit the data traffic  :stuck_out_tongue: But as I said there won't be too much ragdolls in one time...

-------------------------

