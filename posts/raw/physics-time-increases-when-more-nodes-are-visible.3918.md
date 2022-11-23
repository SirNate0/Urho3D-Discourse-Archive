TrevorCash | 2018-01-06 23:29:39 UTC | #1

I am a bit confused as to why I time spent in UpdatePhysics (in the profiler) changes with respect to how many nodes are visible.  Below is the same scene with different camera zoom levels:

Is it because something about the draw calls actually happen in the physics update?

Zoomed Out (many nodes visible):
![image|690x387](upload://20TPOg9jIaArgfsspifbtXi1UQB.jpg)

Zoomed In (very few nodes visible):
![image|690x386](upload://q0Odxwh2HO9QZM7ZWHMrruGXgbS.jpg)

-------------------------

Eugene | 2018-01-07 09:26:43 UTC | #2

The less your FPS is, the more frame time is taken by physics computation (because physics FPS is always fixed). Don't let your FPS go below 60 to prevent it.

-------------------------

TrevorCash | 2018-01-08 17:06:40 UTC | #3

Thanks Eugene - After looking at the source a bit I can see this now.

-------------------------

