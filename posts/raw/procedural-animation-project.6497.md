SirNate0 | 2020-11-02 19:56:44 UTC | #1

I've been working on a procedural animation system for the past 6 months, and I thought it has reached a point where it's nice enough to make a video showing the progress in it.

https://youtu.be/ASXHdcHXkwQ

The basic approach is to create a series of (custom, not Urho3D) IK components for the legs and arms. A controller can then take info about the change in position and angle and character state (jumping, etc.) to decide a position for the hands and feet. The basic shape of the stride is an ellipse, and on top of that I have implemented foot-planting (only on the right foot at present to compare the two). Adding in a few more parameters, like some swaying and/or height-change based on where we are at in the stride (left foot extended, crossing, right extended, etc.) and some swaying based on the character's acceleration results in a rather decent looking animation based on only a few parameters.

This allows for quick animation of a character with a similar bone hierarchy to another, in contrast to (my experience, at least) 3D modeling/animation software like Blender, where animations are typically key-frame based, so adjusting something like the stride length between two similar characters becomes a much more involved and time-consuming process than just editing a number. As I'm working on a project that will have 100+ models with a variety of skeletal structures, and it's just my brother and I doing all the modeling and animation, a quick way to get decent animations was necessary.

The basis for the project was initially attempting to implement Wolfire's Procedural Animation in Urho. However, their approach did not satisfy me, as they still required a number of poses to be created by hand for the characters (particularly when attacks are added in). It certainly seems more efficient than creating a series of animations by hand, but most of the poses that would be required could still be created (at least for an initial attempt) with a bit of programming and IK components. But at that point, I saw little reason to finish implementing their approach in blending (with fancier curves than just LERP/SLERP) rather than just using the IK for the actual animation.

Later on I'll come back and provide more updates on the project, and maybe add something like a features list and/or road map.

-------------------------

Eugene | 2020-11-02 20:35:39 UTC | #2

As a person who spent many months of free time on procedural animation without any satisfying output, I can only appreciate the effort.

Have you tried "semi-procedural" animation?
I implemented something like that with moderate success.
I parse real animation, extract feet trajectory and exact bone movement and then remap it on top of plain procedural aniamtion.
So I can have procedural animation with more complicated bone behavior, which is important for creatures with real feet.
I never finished it, but it looked good... occasionally.

-------------------------

SirNate0 | 2020-11-02 22:15:09 UTC | #3

So far I've not tried anything asking those lines. I might later if I've unsatisfied with the results after trying it with more of the characters.

I'm not aiming for a particularly realistic appearance, just something that looks tolerable, so I'm hoping it won't be necessary (I'm not that great of an animator with the normal approach, so I'm not sure I could do that much better on my own if it does end up that way).

-------------------------

evolgames | 2020-11-07 00:39:48 UTC | #4

Wow @SirNate0 this is awesome!
I'm very curious on the implementation. Are you simple feeding the IK angle change goals in rotation over a period of time? If I recall correctly, the IK sample merely snaps the feet to the floor, and didn't exhibit this type of custom movement. Maybe it did, I don't know. So I'm wondering how this works exactly.

-------------------------

SirNate0 | 2020-11-07 04:01:06 UTC | #5

Thank you @evolgames! 

I did not use Urho's IK components for this. If I remember correctly, I had issues getting them to work well with the physics-based character controller, and it is simple enough to re-implement 1 or 2 bone IK. In fact, I think this was actually my second time doing that, as I think I had written a very basic 2-bone solver in AngelScript before the IK components were merged into Urho.

[quote="evolgames, post:4, topic:6497"]
Are you simple feeding the IK angle change goals in rotation over a period of time?
[/quote]

To answer your question, though, I don't think this is how I am doing it. It's a mix of different things that give it nice looking motion. The character has a master phase, if you will, within it's walk cycle (a value between 0 and 1). The phase is normally updated (i.e. not while jumping/falling) by another component that keeps track of the position change in the world and has some scale factor relating the distance traveled to the phase change (a value that is based off of the length of the stride, which for now is fixed). On top of that, there's an angular factor added, so that it will "walk" while turning, and the lengths of the stride of the left and right foot are altered so that the one on the inside of the turn travels a shorter distance (or backwards if the turn is sharp enough).

In terms of the strides themselves, they are simply an ellipse, which the phase determines the position on (so `(0,a*Sin(360*phase),b*Cos(360*phase)`) as a vector) with translations and rotations applied to that ellipse.

The directions of the strides (i.e. do the feet move forwards and back or diagonally or to the side, or equivalently which direction is the ellipse pointing in relative to the up axis) are based on the direction traveled in the world (averaged over a number of frames so it is not too jerky based on small movements). If the direction is backwards, the phase advances backwards instead of forwards so it appears to walk backwards. For the side, there's a threshold angle such that if it was walking forwards and then walks sideways, the walk cycle will continue moving forward, but if it was walking backwards it will continue moving backwards. If you were controlling it with a joystick, it will flip after you go about 15 degrees past horizontal, so to get it to flip back you'd have to change the angle by about 30 degrees.

To get the bending in the feet I actually have a sort-of 3-bone IK solution, which is really just a 2-bone IK with a fixed angle for the foot after that (and thus a calculable offset from the target that the 2-bone system can then solve). Similarly, the toe just has an angle specified for it. Averaging the foot angle being fixed (the IK solution) with the foot angle remaining from the original pose (the FK solution) gives a surprisingly decent bending to the toes, leaving the foot largely horizontal but with some swing in it as it goes through the stride.

The arms largely re-use the leg setup, except instead of travelling around the ellipse, it bounces back and forth on one portion of it (a C shape, if you will).

The body/spine/neck has some sway applied to it based on the phase, as well as the whole body bouncing up and down a little. Mixing these together and adding in appropriate phase shifts between feet and the body and the arms gives what you saw.

[quote="evolgames, post:4, topic:6497"]
If I recall correctly, the IK sample merely snaps the feet to the floor, and didn’t exhibit this type of custom movement. Maybe it did, I don’t know.
[/quote]

Given that I'm somewhere around 4000 lines for this, I certainly hope the sample doesn't have as good motion, otherwise I just wasted 6 months of free time ;)

-------------------------

evolgames | 2020-11-07 22:59:17 UTC | #6

Very interesting. Thanks so much for the write up. It's inspiring to see this kind of work done. It's complicated but in the end provides an awesome system for applying animations to your creatures in your game.

-------------------------

Modanung | 2020-11-08 14:28:16 UTC | #7

@SirNate0 Are you making _Eugene: The Game_? :wink:

[![eu|50x50](upload://odlJ2cUJSO8P1Lw3cjkRmGlEf0.png)](https://www.youtube.com/watch?v=Lixm0ajWCi8&disable_polymer=true)

-------------------------

SirNate0 | 2020-11-12 15:52:50 UTC | #8

It looks like someone else had many of the same ideas as me, and has turned it in to a product (well, alpha release at present):

https://www.kestrelmoon.com/creature3D/index.html

-------------------------

Modanung | 2020-11-12 20:11:30 UTC | #9

I wouldn't call that UI-enriched glitch a product. :smirk:

-------------------------

elix22 | 2020-11-13 08:51:48 UTC | #10

Looks absolutely awesome !!
Some links with full documentation and source code that might provide some inspiration

http://guillaumeblanc.github.io/ozz-animation/samples/two_bone_ik/
http://guillaumeblanc.github.io/ozz-animation/samples/look_at/
http://guillaumeblanc.github.io/ozz-animation/samples/foot_ik/

-------------------------

glebedev | 2021-04-01 15:58:15 UTC | #11

Is the source code available?

-------------------------

SirNate0 | 2021-04-02 04:27:28 UTC | #12

Not yet. I haven't yet decided if I will release it or not, as I think it's one of the few things I've done that could have some commercial potential. That said, I haven't decided I won't release it, and I'm certainly open to releasing parts of it, as a large part of it is rather common things (math things like breezier curves, 2 bone IK, etc). At this point it's also not really finished and certainly not polished code, so it's somewhat questionable that people would want to look at the code.

-------------------------

