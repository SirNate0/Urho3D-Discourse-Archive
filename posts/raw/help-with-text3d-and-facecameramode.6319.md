btschumy | 2020-08-13 15:49:49 UTC | #1

Once again I'm trying to reproduce some behavior in Urho3D that I have in my SceneKit implementation.

I have various objects labelled onscreen and say I want to have a label centered on a point but use FaceCameraMode.RotateXyz.

I can center the label on a position (0, 0, 100000) by doing something like.

	var size = text3D.BoundingBox.Size * fontScale;
	 textNode.Position = new Vector3(size.X / 2.0f, size.Y / 2.0f, 100000.0f);

This works fine when not using FaceCameraMode.  However, I need the labels to always face the camera.  In this case the label is centered properly when looking down the z axis, but not as you pan around looking a the scene from other directions.

In SceneKit there is a concept of "pivot".  Rather than offsetting the position, you would offset the pivot and then the label would remain centered on the point at all angles.

https://developer.apple.com/documentation/scenekit/scnnode/1408044-pivot

I've also read that setting the pivot is conceptually the same as introducing an intermediated node and translating the intermediate node rather than adjusting the position of the text node.

https://stackoverflow.com/questions/42568420/scenekit-understanding-the-pivot-property-of-scnnode

I've tried the intermediate node solution, but it doesn't seem to work with FaceCameraMode on.

Is there a simple (or even not so simple) solution to this problem?

Thanks again.

-------------------------

Eugene | 2020-08-13 22:04:02 UTC | #2

C++ API has SetHorizontalAlignment/SetVerticalAlignment/SetTextAlignment. Check if these are accessible for you.

-------------------------

btschumy | 2020-08-13 23:11:10 UTC | #3

Eugene,

Thanks.  Yes, those are available and it does seem like they do what I need.

Man, I would never have expected that behavior from those names.  In every UI framework I've used "text alignment" refers to how the text is laid out in the UI element.  Either left justified, right justified or centered in the space.  It didn't occur to me that it had to do with the pivot point.

I find learning Urho3D frustrating because the documentation just says: "Set horizontal alignment."  No discussion of what it really does.  Thank goodness this forum exists and you guys are willing to help me.

I do have another case where I need to offset pivot point arbitrarily.  I have objects where I want to display a label up and to the right of it.  I see there is a HA_CUSTOM and VA_CUSTOM.  Looking at the C++ code, it appear that option works with the pivot value, but that is only exposed in UIElement subclasses which Text3D is not.  Is there a way to use the custom alignment with Text3D?

Bill

-------------------------

Eugene | 2020-08-14 07:50:02 UTC | #4

[quote="btschumy, post:3, topic:6319"]
the documentation just says: “Set horizontal alignment.”
[/quote]
Yeah, I don’t really like it.

However, I doubt that any of Urho users is willing to donate 2k$+ for the sole purpose of documentation, and documentation writing alone will cost that much.

-------------------------

vmost | 2020-08-14 12:51:48 UTC | #5

It would make more sense to have 'continuous improvement' documentation. Clearly this thread identified one small part of the documentation that could be improved. So... go improve it.

-------------------------

Eugene | 2020-08-14 13:25:07 UTC | #6

[quote="vmost, post:5, topic:6319"]
It would make more sense to have ‘continuous improvement’ documentation
[/quote]
It works as long as these are people interested in said continuous improvement of documentation. Maintainers in scope of documentation writing. I don’t happen to see such people at the moment.

-------------------------

