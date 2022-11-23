GodMan | 2020-04-04 01:07:57 UTC | #1

Is there a way to detect if a rigidbody is falling? Checking to see how long a node is not on the ground does not work that well.

-------------------------

SirNate0 | 2020-04-04 02:25:43 UTC | #2

What do you mean by falling, and what have you tried that doesn't work well/what is the issue with that?

I think there are several possible approaches, that may need to be combined:
SphereCast/RayCast to see if you're on the ground.
Check that velocity.y_ is negative (or negative and greater than some magnitude). Check that there is/is not a contact (collision) with the ground.

-------------------------

GodMan | 2020-04-04 02:33:46 UTC | #3

Just checking to see. In Irrlicht there was a method called isFalling(). It basically had the logic to check if a node was falling.

-------------------------

SirNate0 | 2020-04-04 03:06:51 UTC | #4

Pretty sure there isn't one, but I think since of the samples have an IsOnGround (or something like that function) you could take if you wanted to. The meaning of whether or not a node is falling is pretty game-dependent, so it's probably better to put inside a character controller class anyways.

-------------------------

GodMan | 2020-04-04 03:32:34 UTC | #5

Yeah the character demo has an in air timer if the character is no longer making contact with the ground. Only problem is lets say the character jumps in a gravity lift that propels them somewhere. Since they dont make contact with the ground for a predetermined amount of time. Boom dead.

-------------------------

Dave82 | 2020-04-04 11:05:14 UTC | #6

You should handle gravity lifts separately. While in gravity lift , don't update the ground contact part of the code.

-------------------------

GodMan | 2020-04-04 23:29:31 UTC | #7

Only issue with that is a gravity lift as far as halo is concerned just propels you on somewhat of an arc through the air your not really standing on anything. 

I just wondering what would be a good addition to the in-air timer.

-------------------------

SirNate0 | 2020-04-04 23:46:19 UTC | #8

I would suggest in whatever is altering the gravity/applying the force manually reset the in-air timer.

-------------------------

Modanung | 2020-04-05 01:25:46 UTC | #9

Wouldn't that turn any lift into a lifesaving bug?
I think in-air-timers are error prone. For example when engaging in seemingly non-lethal piggybacking, or when landing on a descending elevator that *should* break your fall. I'm inclined to suggest using the _impulse_ value of the relevant contact included with the `NodeCollisionStart` event instead.

-------------------------

GodMan | 2020-04-05 01:32:17 UTC | #10

That's what I've been saying. You could use the gravity lift and similar things to disable fall damage.

-------------------------

GodMan | 2020-04-05 19:03:52 UTC | #11

@Modanung Do you have more details on this approach?

-------------------------

Modanung | 2020-04-05 20:00:21 UTC | #12

1. Read impulse (see sample 18)
2. Impulse too big? -> Ouch!

> **[F = m * a](https://en.wikipedia.org/wiki/Newton's_laws_of_motion#Newton's_second_law)**

...where F represents the impulse in this case.
Questions? :slightly_smiling_face:

This should also work when launched into a ceiling or wall, when disregarding the contact's normal.

-------------------------

GodMan | 2020-04-05 20:13:37 UTC | #13

Okay sound great thanks man.

-------------------------

