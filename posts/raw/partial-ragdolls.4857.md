Leith | 2019-01-24 06:51:38 UTC | #1

I'm reworking the Ragdoll code to support the ability to 'break' (and 'repair') animated limbs individually.
The public code assumes that we want the entire skeleton to enter ragdoll mode at once.
It's entirely possible to toggle that state for specific subtrees of the skeleton.
For example, to break the left shoulder, so the entire left arm becomes a ragdoll, but attached to a model that otherwise attempts to provide base animation.

I'll yell in a day or two whether I run into any major problems, but I have already restructured the sample code to create the ragdoll structure in advance, and written the recursive enabler method (with respect to disabling bone animation).

A side effect of this arrangement, is that since our models have rigidbody armatures from the beginning, we can use them to provide more accurate information about collisions between the character (and any attachments), and the big bad world... we can get detailed information about where our sword hit that monster, and possibly use IK to delimit animations in a physically plausible way.

-------------------------

