Enhex | 2017-04-26 18:39:15 UTC | #1

Having a billboard with a constant size in screen space, size that doesn't change with distance from the camera, is useful for things like indicators of 3D positions.

While it should be possible to use WorldToScreenPoint() to get screen position, and then either position a 2D sprite or use ScreenToWorldPoint() to get a 3D position for a billboard, it requires manual updating and culling, and should be less efficient than having the billboard render directly with constant size, and the depth and parent node information is lost (unless manually saved and accessed).

If I recall correctly, in OGRE3D it was possible to achieve that with:
Ogre::BillboardSet::setPointRenderingEnabled()
[ogre3d.org/docs/api/1.9/clas ... 1bbd8cf3b6](http://www.ogre3d.org/docs/api/1.9/class_ogre_1_1_billboard_set.html#a417ba29ab7894f7ba4fda41bbd8cf3b6)

-------------------------

cadaver | 2017-01-02 01:12:29 UTC | #2

Should be doable. Note that for proper culling this would be best done on CPU side, which means it will have to keep adjusting the size and updating the vertex buffer as the camera moves.

-------------------------

yushli | 2017-01-02 01:12:30 UTC | #3

That sounds like a nice feature to have. Waiting for it to appear in the master branch...

-------------------------

Victor | 2017-01-02 01:12:30 UTC | #4

This does sound a pretty cool feature! At some point I know I will definitely need to use such a feature.

-------------------------

Enhex | 2017-01-02 01:12:30 UTC | #5

Another problem that constant billboard size can solve is handling multiple cameras.

-------------------------

cadaver | 2017-01-02 01:12:31 UTC | #6

Screen size billboards have been added to master branch. See BillboardSet::SetFixedScreenSize(). In this mode the billboard size corresponds to pixels (for easy use of specifically-sized textures as markers), but node scale can affect it too.

It occurred to me that Text3D would benefit from the same option, and after programming it once it's easier to do again.

-------------------------

Victor | 2017-01-02 01:12:31 UTC | #7

Wow thanks man! This is awesome!

-------------------------

Enhex | 2017-01-02 01:12:33 UTC | #8

Gave it a try. Works with single viewport, but with multiple viewports only one of the viewports scale is used, so the billboards render with incorrect scale in all the other viewports.

The problem can be replicated in the multiple viewports sample:
- set both cameras to look at the same direction (remove rear's rotation)
- use authographic on one of the cameras to make the effect more noticable
-    - setting main cam to ortho causes the rear cam to have regular size billboards
-    - setting rear cam to ortho causes the rear cam to have shrinking billboards as u get closer

Perhaps moving the size updating into a BeginViewUpdate event handler would solve it.

-------------------------

cadaver | 2017-01-02 01:12:33 UTC | #9

The problem is that all BeginViewUpdate's for all viewports are called before rendering happens, so drawables would need to store per-view information, or recalculate the information right before actual rendering. In general this is not a trivially solvable problem, because for efficiency we'd rather not interleave view update and rendering, and in some cases (e.g. mirror views which use a RTT) we would need to recurse into view preparation+rendering right in the middle of view preparation, which also could cause unexpected code interactions. I believe this case is solvable by some hack code but a general good solution is hard to achieve.

-------------------------

cadaver | 2017-01-02 01:12:33 UTC | #10

Should be fixed in master branch. Text3D had also a similar issue in relation to both screen scaling & face camera mode, which also was fixed.

-------------------------

