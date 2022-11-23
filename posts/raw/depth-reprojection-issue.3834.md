Don | 2017-12-11 02:54:20 UTC | #1

Good evening,

Recently I've been working on an SSAO implementation. One of the most integral parts of this shader is the ability to convert from screen space to world space and back. Finding screen space is simple since there is already a function in place. For the opposite conversion, I copied the code used to find position in the deferred shaders. To test this, I set up a post-process that takes the point of a fragment, converts it to world space, and then reprojects it back to the screen. It seems to work perfectly, except for the depth.

When comparing the raw depth buffer value and the depth after both conversions, they are slightly different. Both are [0, 1], but the reprojected one is always lower.

https://imgur.com/a/3cdEi

Why are these values different? What function can I use to map these values to the ones in the depth buffer? (I am already using ReconstructDepth) Thanks in advance to anyone who knows about the underlying processes here. I can post code if it would be helpful.

-Don

-------------------------

Don | 2017-12-19 03:23:54 UTC | #2

I figured out that the way to do this is to use ToScreenPos instead of ToScreenPosPreDiv in order to convert back. However, you have to look at the w component divided by the far clip instead of the z component.

SSAO is almost working now!
![Screenshot from 2017-12-18 18-38-47|690x366](upload://fNcUS3rEbmniMZ6ourwmV2i37SA.jpg)

-------------------------

