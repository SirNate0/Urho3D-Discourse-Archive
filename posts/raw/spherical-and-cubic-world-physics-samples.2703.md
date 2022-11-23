Lumak | 2017-01-18 03:29:37 UTC | #1

Just another video of something else possible with the engine.

Have a great weekend :slight_smile:

edit: repo https://github.com/Lumak/Urho3D-Spherical-World

https://youtu.be/9h2AygIzFMQ

edit2: added square world physics sample
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/71743ca5b1f6b41833d20fe29334dd2ce695ca72.jpg[/img]

-------------------------

HeadClot | 2017-01-15 06:31:41 UTC | #2

How did you accomplish this? 

Can you talk about the techniques that you used?

-------------------------

Lumak | 2017-01-15 16:22:28 UTC | #3

Sure. It's not complicated as it seems, but I did come across some odd behaviors.
First, you'll need to calculate the char's direction to center of the sphere which becomes new gravity and apply:
> body->SetGravityOverride(dirToCenterOfSphere * 9.81f);

every frame.  The 
> dirToCenterOfSphere * -1.0f

becomes char's normal, and from this you can derive the forward and right vectors which then provide the orientation for the character, i.e. Quaternion(right, up, forward).

Some odd behaviors that I'm seeing are that if you use inertia bounding box derived from a capsule, physics wants to pull the body back up to the top (like a magnet) ,and second is that there seems to be some odd acceleration going on when the char is 1/4 and 3/4 way down the sphere, something I'm still trying to figure out.

*edit: err, I shouldn't say acceleration at 1/4 and 3/4 because char doesn't move if I stop moving. It's more like no braking is applied at those areas.

-------------------------

Lumak | 2017-01-16 03:47:36 UTC | #4

added a link to the repo - see the1st post.

-------------------------

Lumak | 2017-01-17 22:53:53 UTC | #5

fixed the jump force error, and added a square world

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/71743ca5b1f6b41833d20fe29334dd2ce695ca72.jpg[/img]

-------------------------

Lumak | 2017-01-18 03:31:06 UTC | #6

A couple more changes:
-corrected rotation calc. on surface
-renamed to cubic world

That should be the last of it. Let me know if you find any problem. Thx.

-------------------------

rku | 2017-01-19 13:25:29 UTC | #7

This is awesome. How does character behave when you jump over the edge of the cube?

-------------------------

Lumak | 2017-03-26 18:59:15 UTC | #8

It transitions properly.
Here's a vid:

https://youtu.be/QPoIplaT-ZA

edit: provided a url
edit2: something weird is going on with youtube and I can't provide a viewable link.

-------------------------

Eugene | 2017-01-19 15:31:47 UTC | #9

I can't consider this blinking as truly 'properly transition'
It seems that character movement (I mean, orientation) is not smooth. Is it hard to fix?

-------------------------

Lumak | 2017-01-19 16:05:19 UTC | #10

I'm not sure how else to transition it, but sounds like you've seen it done differently some where. Can you provide a video link?

edit: not sure if smoothing out the camera or character orientation or both would be required, or if attempting this smooth transition would be harder on the eyes. I'd like to see an example.

-------------------------

Eugene | 2017-01-19 16:25:18 UTC | #11

Portal 2 has pretty nice transition when UP is changed.

-------------------------

Modanung | 2017-01-24 15:25:30 UTC | #12

Cylindrical gravity for the edges and spherical for the corners would give the transitions there a more natural feel, I think.

-------------------------

Lumak | 2017-01-20 19:10:08 UTC | #13

@Eugene @Modanung

Okay, thanks for the info. I've seen the Portal2 vid and see that the dynamics on surface changes are treated as a cylindrical surface, where the character sticks to the surface as it transitions from one surface to the other. But that's not the dynamics that I'm looking to achieve.  What I'm looking for is that when a character steps off an edge, I want it to actually fall and use physics to transition to a new surface gravity.  I did add a few frames to lerp the character's orientation opposed to a single frame transition.  It looks better.

-------------------------

mizahnyx | 2017-01-24 05:43:53 UTC | #14

Thanks for the info! I was really curious of it. Keep the great work!

-------------------------

