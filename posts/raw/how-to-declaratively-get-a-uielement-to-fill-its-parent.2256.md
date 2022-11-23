russ | 2017-01-02 01:14:18 UTC | #1

Hi,

I'd like to have a UIElement "dock" to the bottom of the screen, with a fixed height and horizontally fill from the left to right edges.  I know that I can do this by watching the parent's size in event handlers (or subclassing a UIElement, I guess), but I'm wondering if this is possible to do declaratively?  Something like SetHorizontalAlignment(HA_FILL)?

Thanks,
Russ

-------------------------

cadaver | 2017-01-02 01:14:18 UTC | #2

Currently you can't. This pull request however should hopefully go in in the near future:
[github.com/urho3d/Urho3D/pull/148](https://github.com/urho3d/Urho3D/pull/148)

-------------------------

russ | 2017-01-02 01:14:18 UTC | #3

Yeah that looks perfect, thanks!  You dropped the last number from the link, it should be [github.com/urho3d/Urho3D/pull/1486](https://github.com/urho3d/Urho3D/pull/1486)

-------------------------

cadaver | 2017-01-02 01:14:19 UTC | #4

Thanks for the correction.

-------------------------

