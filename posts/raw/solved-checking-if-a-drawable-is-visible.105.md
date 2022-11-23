Mike | 2017-01-02 00:58:01 UTC | #1

I' wondering what function(s) to use to check if a drawable is visible in a viewport.

-------------------------

weitjong | 2017-01-02 00:58:01 UTC | #2

The drawable has a IsInView() method. Is that what you are looking for? That method is exposed rather nicely for AngelScript API and becomes 'inView' property. The same cannot be said for Lua API which exposed the method as it is, that requires the frameNumber parameter.

-------------------------

Mike | 2017-01-02 00:58:01 UTC | #3

Yes, I have trouble with the IsInView for lua (I think that's the function I need).
I've tried to get frameNumber using Time:GetFrameNumber() but I end up with a segmentation fault.

-------------------------

weitjong | 2017-01-02 00:58:01 UTC | #4

I have made a commit to change how the Drawable::IsInView() method is exposed in LuaScript API. I now wrap the Drawable::IsInView() method in a convenient static function, and then bind that static function to a readonly property called 'inView' (similar to how it is done in AngelScript API). You should be able to use the property directly to check whether a drawable is in viewing frustum. Something like this:
[code]local model = characterNode:GetComponent("AnimatedModel")
debugHud:SetAppStats("Model is in view", Variant(model.inView))[/code]

-------------------------

Mike | 2017-01-02 00:58:01 UTC | #5

Many thanks for commit and detailed explanations. :wink: 

However it doesn't exactly work as expected (maybe that's the normal behavior): for example, if I instantiate a Ninja in sample #18, it gets visible in a 180? range, so it returns true even if Ninja is not visible in my viewport. If this is the intended behavior of inView, how can we tweak to match camera visibility?

-------------------------

cadaver | 2017-01-02 00:58:01 UTC | #6

The drawable should be "in view" when it's bounding box is even partially visible in the camera frustum. Check with debug geometry drawing to verify.

-------------------------

weitjong | 2017-01-02 00:58:01 UTC | #7

How do you define "camera visibility"? If the character is standing in front of the camera but behind a big box which occludes the character, the character is not [i]visible[/i] from the camera's point of view but still the character's drawable is considered as "in view". Right?

-------------------------

cadaver | 2017-01-02 00:58:02 UTC | #8

I'll have to check, if the object is an occludee and it's completely obscured by an occluder in the software occlusion system then it shouldn't be marked in view, even though it's inside the frustum. Otherwise, if the object is occluded by actual rendering only (but not by the occlusion system) it will be marked "in view" even though nothing is visible.

EDIT: there is somewhat of a bug. The IsInView() function should by default check visibility in the viewport only, and not in shadow maps. However, what happens is that when shadows are on, the drawable will report visible even when occluded. With shadows off it works correctly.

EDIT2: Fixing this is not trivial, because the drawable only keeps memory of the last view rendered from. Better solution, with some overhead would be to change drawables to keep a set of cameras they have been rendered from last frame, so you could ask IsInView(camera).

-------------------------

Mike | 2017-01-02 00:58:02 UTC | #9

Thanks for checking.

-------------------------

