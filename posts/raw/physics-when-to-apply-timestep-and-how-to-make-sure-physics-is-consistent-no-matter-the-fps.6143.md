NessEngine | 2020-05-06 18:13:55 UTC | #1

Hi all,

In Urho update methods we get timestep value which is used as a factor to make sure speed is consistent no matter the fps. In addition, the physics engine in Urho works with its own update loop and uses timestep internally for its calculations.

Maybe I missed it in the docs, but what are the rules to when I'm supposed to apply timestep and when not, **when dealing with physics**?

Right now my rule of thumb is that if the action I do is based on time measured by the timestep, I use it, while if not - I don't use it.

For example if I need to apply a single impulse on a rigid body I won't use timestep. But if I apply a constant force for 10 seconds, which I measure using the timestep, I will apply the timestep factor on every frame I apply the force.

Is that a correct approach? Are there any pitfalls I should be worried about when dealing with physics / timestep?

Also while on this subject - if I use this option to limit FPS to emulate what would happen if a weak computer runs my game:

https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_engine.html#a1b10f802e6954fa8409cd5398aae9060

Will that be a reliable simulation? Or does it always add the delay at the last frame or something like that and there's a better method to emulate inconsistent low FPS? Ofc I can always run lots of CPU eating apps in the background, but I prefer a cleaner approach if there's one.

Thanks.

-------------------------

SirNate0 | 2020-05-06 18:45:30 UTC | #2

Force vs impulse determines whether you should multiply by the timestep or not. ApplyImpulse expects the vector to be multiplied by the timestep. ApplyForce will multiply by the timestep for you. This helped me work out how it works (it's been a while since I took an introductory physics course).

https://gamedev.stackexchange.com/questions/34069/what-is-the-difference-between-an-impulse-and-a-force-related-to-a-physics-engin

-------------------------

NessEngine | 2020-05-06 18:55:11 UTC | #3

@SirNate0 thanks for the link, but I wouldn't say the conclusion from it is that impulse must be multiplied by timestep. For example if I use impulse for jumping, I would want the result velocity to be the same no matter the FPS, right? So since I only apply the impulse once per jump, it shouldn't be multiplied by timestamp.

> ApplyForce will multiply by the timestep for you. This helped me work out how it works (it’s been a while since I took an introductory physics course).

This is very useful, thanks!

-------------------------

SirNate0 | 2020-05-06 19:09:24 UTC | #4

Remember that the physics timestep is supposed to be basically a constant. You are right to say that you don't need to multiply by the timestep, though. Glad I could help, though.

-------------------------

NessEngine | 2020-05-06 19:15:01 UTC | #5

[quote="SirNate0, post:4, topic:6143"]
Remember that the physics timestep is supposed to be basically a constant.
[/quote]

What do you mean, is it not based on FPS?
Thanks!

-------------------------

SirNate0 | 2020-05-06 20:30:19 UTC | #6

Correct (with some exceptions, see the link for details).
> The physics simulation has its own fixed update rate, which by default is 60Hz. When the rendering framerate is higher than the physics update rate, physics motion is interpolated so that it always appears smooth.
-- https://urho3d.github.io/documentation/HEAD/_physics.html

-------------------------

