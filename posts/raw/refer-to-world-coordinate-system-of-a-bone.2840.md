akilarandil | 2017-03-02 08:30:18 UTC | #1

Hello All,
 
I have a skinned biped human model. I want to rotate a particular bone using the World coordinate system rather than using the local coordinate system of the bone. How can I proceed with this issue?

Thanks in advance.

-------------------------

slapin | 2017-03-02 09:02:28 UTC | #2

You need to convert world coordinates to local coordinates using subsequent parent bone transforms.

-------------------------

slapin | 2017-03-02 09:03:35 UTC | #3

Probably Urho should have this mechanism for bones, otherwise it is not really friendly accessible feature.

-------------------------

cadaver | 2017-03-02 09:18:33 UTC | #4

You should be able to use SetWorldPosition() / SetWorldRotation() on the bone node, which does the reverse transform for you. Note however you need to set the bone under manual control or it will reset next time animations are updated. See the 18_CharacterDemo sample, which does this for the head node.

-------------------------

slapin | 2017-03-02 09:33:16 UTC | #5

The problem happens when you need to have both animations and bone corrections.
Something which is based on initial bone position is needed and something which alllws not using bone nodes.
I.E. for IK setup you need to calculate distances between several bones (you can IK 2 or more bones as 1 to save time),
using initial pose, and that is not possible using nodes which can be affected by animation, but you still need an animation
to blend together with.

-------------------------

akilarandil | 2017-03-02 09:38:52 UTC | #6

@slapin @cadaver  
I don't have any animations set.
Basically, I used a biped model using 3ds Max. And I have a simulation app which rotates bones based on quaternion data given from outside. The problem I encountered is that the biped bones have different local coordinates and I need to change it to the world coordinate system I'm using.

-------------------------

slapin | 2017-03-02 09:38:49 UTC | #7


Well, explanation - one have ragdoll setup and wants to blend it back to animation - you need to lerp pose into
animation pose but still have ragdoll affecting it for some time.
Another case is IK where you need to blend from animation correcting it, i.e. for handshake the arms should touch each other regardless of height of characters (to some limits).

-------------------------

akilarandil | 2017-03-02 10:16:31 UTC | #8

I don't use any sort of animations. Just using the model and rotating the bones :slight_smile:

-------------------------

slapin | 2017-03-02 10:19:01 UTC | #9

Then do as cadaver suggested. Don't forget to disable animation on the bones if you will want to add animation. If you just modify a few, just disable animation on them. See ragdoll example for reference.

-------------------------

