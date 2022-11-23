slapin | 2018-02-22 19:01:07 UTC | #1

Well, I need to implement 2 systemic animations. Systemin in sence that they work from any open game situation. Character should be able to open door. Basically if there is a door close enough (i,e, up to 10m to a door), character should get to that door, then get to one of appropriate locations, then open it. There are 2 situations - normal door and vehicle door.

So basically, we can split this into 3 phases - approach a door, ???. open door.

The actual door open animation is quite simple - it just swings or slides. The problem is animating actual character model. I'm too lazy (or failed as animator) to create every possible animation for this. So I want procedural approach. Is there existing papers, vidoes, any information about creating such interactions? I have no mocap access though,
so I still need to animate...
@Sinoid please heeeelp!

-------------------------

Sinoid | 2018-02-22 23:03:21 UTC | #2

I've got nothing for this.

-------------------------

SirNate0 | 2018-02-23 00:38:34 UTC | #3

Just throwing it out there, but depending on how realistic it must be you could try just using IK and attaching the hand to the knob/handle for some portion of the door opening animation. Maybe add some different cases like turn knob vs just pull/push handle.

-------------------------

Lumak | 2018-02-23 21:48:57 UTC | #4

I'll provide something that you can play with soon, but wow! This turned out to be more difficult than what I expected.  Animation is easy part, but trying to export vehicle skeletal system as nodes but them have it as AnimatedModel just be able to animate it turns out to be little tricky.

-------------------------

Lumak | 2018-02-24 00:49:20 UTC | #5

@slapin, If you still want help with this, pm me your email address and I'll send you the zipfile of the working sample - just the entering the vehicle interaction, no exit.

-------------------------

