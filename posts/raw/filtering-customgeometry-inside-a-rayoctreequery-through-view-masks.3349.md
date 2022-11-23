greyWiz | 2017-07-13 21:17:50 UTC | #1

Hi, I have a CustomGeometry mixed with a set of StaticModels in my scene and I want to raycast the StaticModels without taking the CustomGeometry into account. One solution that I was considering would be setting the CustomGeometry to a different view mask than StaticModels, but even by doing it the raycast still would find the CustomGeometry.

Then, I decided to make a different test: I've set the camera's view mask to different values which gave me these results:

- When I set the camera's view mask to match the CustomGeometry's mask, the StaticModels are correctly masked out.
- When I set the camera's view mask to match the StaticModels' mask, the CustomGeometry is NOT masked out.
- When I set the camera's view mask to any other value, the StaticModels are correctly masked out, but not the CustomGeometry.

To sum up the question: should a CustomGeometry model be set up differently so it can be correctly masked out by mask views?

Thanks in advance!

-------------------------

cadaver | 2017-07-14 09:58:59 UTC | #2

The camera's viewmask doesn't affect raycasts, only the raycast query's own viewmask does. Did you take this into account? Otherwise it would sound weird that viewmask would behave differently for different geometry classes, since this property is in the Drawable base class.

-------------------------

greyWiz | 2017-07-14 11:32:58 UTC | #3

Hi cadaver,

Yes, I took that into account, the camera example was just to show that something weird was going on with my CustomGeometry, since it refused to be masked out by view masks. My reasoning was that, since it was happening, maybe I should first understand the CustomGeometry-and-Camera issue and make sure that I was able to make it work correctly (and make sure that the view masks were, in fact, working in that case) before blaming the raycast operation.

-------------------------

