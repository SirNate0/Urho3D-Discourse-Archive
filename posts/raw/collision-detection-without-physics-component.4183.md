ChunFengTsin | 2018-04-18 02:05:27 UTC | #1

![Screenshot%20from%202018-04-18%2009-44-04|690x386](upload://oYqWJmQGmReezgAii6YT1PW7evA.png)

Hello, 
when I add shooter to the scene, I have a question about collision detection.

Before , there are no physics in scene , I adjust the position and rotation of character by simple calculation.
And hit cube by Ray-cast from camera.

But now I want to shoots bullets, how I to detection the collision between bullet and other character.
Do I have to use physics component ?

-------------------------

SirNate0 | 2018-04-18 02:34:48 UTC | #2

I'm pretty sure you could just use a raycast for that as well (I couldn't tell you exactly how, but it should be the same as finding the cubes).

-------------------------

ChunFengTsin | 2018-04-18 03:04:09 UTC | #3

yes , the raycast can find node . but the bullet is fly , I want know when the bullet hit on the character.

-------------------------

SirNate0 | 2018-04-18 03:20:08 UTC | #4

If you want to avoid using physics you can just calculate the bullets trajectory for that frame and repeat each frame, updating the position accordingly (basically doing your own physics calculations for a point particle).

-------------------------

ChunFengTsin | 2018-04-18 03:30:36 UTC | #5

OK, then , for check collision ,  should I check if the bullet's position in the interior of character node every frame?

-------------------------

SirNate0 | 2018-04-22 07:20:06 UTC | #6

No, unless it's traveling very slowly - you also need to catch when the bullet passes fully through the character in one frame, hence the raycast. If you wanted, you could do it just by adding a few trigger physics components to the characters as well, though you might still want to use a ray or sphere cast if the bullets will be covering a lot of ground in one frame. Personally, if probably just use the graphics raycast, though.

-------------------------

ChunFengTsin | 2018-04-18 03:46:59 UTC | #7

Thanks for the help, ^_^

-------------------------

