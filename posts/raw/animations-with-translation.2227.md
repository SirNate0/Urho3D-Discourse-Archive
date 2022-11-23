JTippetts | 2017-01-02 01:14:02 UTC | #1

I've been talking to some artist friends of mine, who all say that when creating an animation sequence for, say, a walk cycle they like to compose the animation in their 3D modeler of choice with the translations per frame "baked in". That is, they synchronize the translation of the skeleton to animate the forward motion of the character throughout the duration of the cycle, in order to more tightly control pacing and motion. For an example, see this worm:

[imgur.com/MmGKaSM](http://imgur.com/MmGKaSM)

See how as the animation progresses, the bones translate forward leaving the origin behind.

I currently don't do it this way in my game. Things like walk cycles, I animate forward by a constant speed in the game. However, I am finding that animating with translation in the modeler is much nicer for things such as having my guy step forward, climb up a ledge, then stand up at the top. Or for things like a lunge attack or shield bash, animations that don't have a constant forward translation for the entire duration.

I am trying to figure out the best way of handling this, though. In this scheme, the key is to keep the node stationary and play back the animation, then at the end of the sequence, change the node's position to correspond with the position of the final frame of the animation. Done correctly, it works pretty smoothly. The problem is that it creates a disconnect between the visual position of the object and the actual position represented by the node. If there are other components attached to the node, such as collision shapes, they're going to think that the node is stationary throughout the duration of the animation, and that it suddenly jumps to another location at the end.

Is there an "industry standard" method for handling this? Some people have suggested that when the animation is exported, "subtract out" the forward translation and output a motion curve so that the node itself can be animated from this motion curve while the animation plays. I also have experimented with nesting the animated model in a sub-node, manually querying the animation for the translation of the root bone, then translating the sub-node by the inverse of this translation, while at the same time translating the parent node forward by the translation. However, this is clunky in that it requires a custom component to coordinate it all.

I am using the Blender exporter for my animations, and I don't really see any options in there to export a motion track for the root bone. Anyone got any suggestions?

-------------------------

Sir_Nate | 2017-01-02 01:14:03 UTC | #2

I don't know about an "Industry standard", but to deal with the collision shapes and such you could always have them parented to a sub-root (e.g. the hips bone).

-------------------------

Lumak | 2017-01-02 01:14:04 UTC | #3

[quote]I've been talking to some artist friends of mine, who all say that when creating an animation sequence for, say, a walk cycle they like to compose the animation in their 3D modeler of choice with the translations per frame "baked in". That is, they synchronize the translation of the skeleton to animate the forward motion of the character throughout the duration of the cycle, in order to more tightly control pacing and motion.[/quote]

What you're describing is called "Root Motion." Unity has this feature to enable translation in-game, but unfortunately, we don't have it.
You can, however, implement it. I described it here, [url]http://discourse.urho3d.io/t/character-animation-and-movement-test/1852/1[/url] sometime ago.

Gist of how to do it: 
1) acquire (or dump) Transform (key) animations, i.e. translation, rotation, and scale every frame.
2) at run time, retain previous and current Transform(T)
3) interpolate and find delta T for current time in the animation from previous and current T and calculate linearVelocity = dT/timeStep
4) apply linearVelocity to your rigid body (opposed to applying impulse or force).

Hope this helps.

-------------------------

Lumak | 2017-01-02 01:14:04 UTC | #4

er, 4) should be -- set new linearVelocity, not apply.

One thing to note is that for constant movements such as walk and run, it's better to calculate the average dT for the entire animation duration opposed to dT per frame to reduce jitter in the movement.

Edit: the two videos shown in the linked thread applies average dT for the run animation.

-------------------------

