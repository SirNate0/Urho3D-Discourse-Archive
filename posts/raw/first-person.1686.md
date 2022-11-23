sovereign313 | 2017-01-02 01:09:28 UTC | #1

Hi,

What is the concept behind a first person shooter (I mean, in the code wise).  For example, how do you keep the gun in the camera?  Do you create the gun on the camera node, or is there an anchor like method to anchor the gun the there?  I'm just trying to figure out how you would keep the object there.  Perhaps 2 cameras?  One to view the terrain, and one to see the arm/gun?

-------------------------

Enhex | 2017-01-02 01:09:29 UTC | #2

You can attach it to the camera node.
You'd also want to render as overlay (after the main scene is rendered) to avoid intersections.

There are other approaches like ArmA, where the weapon is actually part of the world model and animations are used to position it.

-------------------------

sovereign313 | 2017-01-02 01:09:29 UTC | #3

Thank you very much for the response :slight_smile:

-------------------------

