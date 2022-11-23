ikeda | 2020-10-08 01:16:36 UTC | #1

I'm using UrhoSharp.

I installed the camera in the center of the sphere and ran RaycastSingle towards the sphere, but I can't get any results.
If you move the camera out of the sphere and run it, you will get a RayQueryResult.

What steps do I need to take to run RaycastSingle from the center of the sphere and get results?

-------------------------

SirNate0 | 2020-10-08 10:39:45 UTC | #2

Hello @ikeda, welcome to the forum!

I believe your issue has to do with the cull direction of the sphere's material - see here for a bit more of an explanation:
https://discourse.urho3d.io/t/sphere-inner-surface-customgeometry/4635

-------------------------

ikeda | 2020-10-08 10:39:43 UTC | #3

Thank you @SirNate0 .

I created a sphere that was inverted with Blender.
I placed the inverted sphere on the outside of the original sphere.
RaycastSingle was able to receive a RayQueryResult for the outer sphere.

-------------------------

