SuperVehicle-001 | 2020-08-17 06:31:50 UTC | #1

I'm trying to make a really basic platformer. So far, I can make the player character move just fine using RigidBody and ApplyImpulse, and I can also make camera orbit around the player. However, I'm struggling with making the character's movement follow the angle of the camera. I want to move in the direction of the camera by pressing forward (W), move in a direction 90° to the right of wherever the camera's pointing when I press right (D), move directly towards the camera by pressing back (S) and so on.

For reference, [here's a pastebin with all the code I have so far](https://pastebin.com/xqUvQzcp).

Sorry if this is too obvious of a thing to ask about - as you may be able to tell from my code, I'm an absolute beginner :smiley:

-------------------------

Lys0gen | 2020-08-17 14:52:37 UTC | #2

Instead of moving along the fixed world axes you should take the rotation of the camera node into account.

Check out example 18 (Character Demo), if I have understood you correctly it should do exactly what you want to achieve (except maybe locking the character to the camera. But that shouldn't be hard to change).

-------------------------

SuperVehicle-001 | 2020-08-17 18:40:04 UTC | #3

The movement code I'm using comes from the Character Demo, actually! So it's not quite what I want, as it still moves the RigidBody relative to the *character*'s direction as opposed to the *camera*'s. (the Character Demo forces the character to always face in the direction of the camera, but I want to avoid doing that)

-------------------------

SirNate0 | 2020-08-21 17:27:52 UTC | #4

Would using `cameraNode->GetWorldDirection()` and such as the direction of your impulse give you what you want?

-------------------------

SuperVehicle-001 | 2020-08-23 22:28:03 UTC | #5

After ramming my head against the wall for a while, I finally managed to come up with something. [You can check it out here](https://pastebin.com/dxaNYx1Q) (this pastebin only includes the changed parts). It's a very *caveman* solution that may have to be completely rewritten whenever I get around to analog controller support but hey, for now it works and that's what matters.

-------------------------

