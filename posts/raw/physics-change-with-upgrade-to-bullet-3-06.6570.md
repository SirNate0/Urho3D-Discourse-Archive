SirNate0 | 2020-11-25 16:25:29 UTC | #1

I recently upgraded to the latest master from a copy a couple months old, and with the upgrade to Bullet 3.06 (commit 4d4030e3ca348e663b5700fc3d3cd7c75b962064 and a few before it) the jumping behavior of my characters has changed. I'm using a physics-based character controller, and the characters are now jumping about half as high as before.

I use `body->ApplyImpulse(Vector3::UP * JUMP_FORCE);` to jump, which I believe is the same approach taken by Sample 18_CharacterDemo.

Any idea what could be causing this change in behavior?

**Edit:** After further investigation, it seems to be a difference in how gravity works. If I disable gravity and manually apply a `9.81f*Vector3::DOWN` force I get the same behavior as before the upgrade. Or if I halve gravity I also get the same result as before.

-------------------------

1vanK | 2020-11-26 18:13:51 UTC | #2

I think I found the problem, wait for the commit

EDIT: Can you test fix?

-------------------------

SirNate0 | 2020-11-26 18:13:48 UTC | #3

Looks like it worked. Thank you.

-------------------------

