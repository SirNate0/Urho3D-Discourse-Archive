Lys0gen | 2020-12-08 23:36:17 UTC | #1

Hello,
I hope someone can give advice on how to best create pie charts that integrate in the UI system.

Creating an extremely basic pie chart is not the issue. While probably not as great for performance as creating a 3D geometry visualization, my idea so far is rather simple: just generate an Urho3D::Image for each pie share and stack them on top of each other in the UI as BorderImages (same position and resolution).

**My problem arises from the fact that I want every share to have a separate tooltip**.

Now as far as I can see it there is no option to have transparent parts of the image *not* trigger tooltips (i.e. like a view mask), so as it is it would always show the tooltip of the last element.

Are there any parameters that I overlooked, to change that behaviour without going into the engine source code? Or a better way to do this that is not too much effort? Perhaps someone already made custom UIElements that go into the direction of being more interactive, e.g. for displaying graphs or other charts?

Thanks!

-------------------------

evolgames | 2020-12-09 03:53:47 UTC | #2

So the image's transparent sections are overlapping the ones underneath and messing up your tooltip hover? That's what I understood here.
Care to post a pic? Why are you using images for pie chart sections?

If I were you I would do sprites to build the pie charts and use raycasts on them. Shouldn't be that hard to manipulate 1x1 pixel white image squares into what you need via scale and color. Then (by node name) you can easily grab what section was hovered over with a raycast. Custom UI would be better and more elegant but that's what I would do and I can confirm it would work.

Also I guess depends what kind of precision youre doing with the chart. If 1%, for example, is the smallest unit (no decimals, or you will round down in visual representation) then you can just make a 1% sliver sprite and clone it 99 times with the correct colors and names. Urho wouldn't flinch.

-------------------------

throwawayerino | 2020-12-10 23:52:31 UTC | #3

I would say that you generate the pie chart as an image with some quick maths and project that onto a UIElement. Find mouse position on screen and calculate angle between that point and center of the UIElement and use that angle to find the category selected.

-------------------------

evolgames | 2020-12-09 07:17:48 UTC | #4

Oh thats a good idea

-------------------------

Lys0gen | 2020-12-10 23:52:26 UTC | #5

Thanks for the suggestions.
What I have actually done now:
* Generate a single Image, put it on an UIElement with a ToolTip child
* Save the UIElement pointer with OnHoverBegin event on the UIElement
* Have a function that checks the mouse position in relation to the chart every frame*; maps the position to actual data values and updates the tooltip text
* Remove the pointer when mouse is out of bounds of the chart

*That's what I hoped to avoid initially, having a function that is run every frame and instead just rely on events. Anyway it's not that expensive in the end, so no big deal.

Thanks again!

-------------------------

