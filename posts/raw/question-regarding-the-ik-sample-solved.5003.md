Leith | 2019-03-10 06:58:58 UTC | #1

I was staring at a piece of code in my foot ik solution, which was essentially copied verbatim from the IK Sample. The more I looked at it, the less I understood how it was even working:

[code]
        float footOffset = leftFoot_->GetWorldPosition().y_ - jackNode_->GetWorldPosition().y_;
        leftEffector_->SetTargetPosition(result.position_ + result.normal_ * footOffset);
[/code]

We measure the Y-Offset from the character root to the foot. When the character is standing straight on level ground, that is something like the length of the entire leg - agreed?

(lets pretend we're on a 45 degree slope now)
We cast a ray in the direction of the surface normal, and note the point of intersection on the terrain.
Next, we compute the new position for the foot ik target, by starting at the point of intersection, and casting back along the normal, by the Y-Offset, which puts our ik target somewhere near the pelvis!
The more I look at that code, the less I understand how the IK solver is not exploding!

It seems to me, the best place to put that target, would be to start at the point of intersection, and cast back along the surfacenormal by a very small amount equivalent to the height of the ankle (which is where the foot bone begins) !! (I refer to the animated height of the foot,  of course).

What am I missing here?

-------------------------

Modanung | 2019-03-07 07:49:40 UTC | #2

Maybe @TheComet could (best) answer this question?

-------------------------

lezak | 2019-03-08 06:01:20 UTC | #3

IK is unexplored part of of the engine for me so I won't be able to help a lot with it, but from what I can see the thing that You are missing here is the fact that 'jackNode_' is the node that model is attached to, so it's position is same as the origin of the model. When character is standing on a level ground offset would be 0 or close to it (difference between ground level and foot bone height), to get length of the entire leg You would need to use pelvis bone. Obviously I'm assuming that model's origin is set to 0,0,0 like it should be (and like jack model has).

-------------------------

Leith | 2019-03-08 01:14:49 UTC | #4

Ah! You're suggesting that the root node of the Jack model is not the pelvis, but rather a point on the groundplane and between the foot bones, is that correct? That would make a whole lot of sense!
Like the sample, I've been passing in the character root node - not the "root bone" per se - From what I've seen in Blender, the origin of my models is indeed at ground level and between the feet, which would explain why the IK solver has not been exploding :)
Thank you for taking the time to explain and point out location of the model origin :)

-------------------------

