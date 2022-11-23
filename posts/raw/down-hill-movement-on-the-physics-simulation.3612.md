ext1 | 2017-09-27 15:55:42 UTC | #1

Hello,

I'm trying to understand why the physics simulation reacts in a certain way.
I've made this diagram trying to illustrate it:
![o8a9Sf7|400x300](upload://2EGK7P69a4qaUyFoowpYwLibjrm.png)
When I apply a permanent constant forward impulse to a rigid body on the top of a slope, it "jumps" forward until it fall on the slope (point A) and then continues down.

Does anyone know why there are no other jumps after point A?
Considering I'm still applying the constant forward impulse.

Best regards.

-------------------------

godan | 2017-09-27 16:30:29 UTC | #2

If you shot a gun at the top of a hill, would you expect it to roll down like a ball?

Just set up gravity and a collider for the hill, and let it happen.

-------------------------

Eugene | 2017-09-27 16:41:54 UTC | #3

Just physics.

At the start, you have zero vertical velocity. When you push the body, it moves horizontally and starts to fall.
When the body hits the slope, it has non-zero vertical velocity. When you push the body, it moves diagonally.

-------------------------

ext1 | 2017-09-27 16:44:48 UTC | #4

Thank you very much!
Vertical velocity was exactly what I was missing.

-------------------------

Lumak | 2017-09-27 16:52:40 UTC | #5

Bounciness of a physics object is affected by [b]restitution[/b] as demonstrated in this video:
[https://www.youtube.com/watch?v=fn_xanuLJiE](https://www.youtube.com/watch?v=fn_xanuLJiE)

-------------------------

ext1 | 2017-09-27 16:58:49 UTC | #6

Thanks for the video, that helps a lot.

-------------------------

