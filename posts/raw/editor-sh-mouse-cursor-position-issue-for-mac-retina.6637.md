CE184 | 2020-12-28 04:59:31 UTC | #1

When I run Editor.sh on mac (latest OS) with retina, apparently there is a bug about mouse cursor position. I believe the editor interprets the mouse position to be (x/2, y/2) while the real mouse cursor is showing at (x, y). For this reason, I cannot click anything under the mouse cursor, but have to move the mouse cursor to a different place. Also I cannot click anything > (width/2, height/2) on the screen.

Any quick solution?

I vaguely remember I used Editor.sh once sometime ago (probably one year ago). I don't recall any issue like this. So maybe new issue after updating OS?

Also, why it automatically uses fullscreen when running Editor.sh? anyway to run it for window mode?

-------------------------

jmiller | 2020-12-28 07:28:58 UTC | #2

Editor.sh essentially does `Urho3DPlayer <script> <options>` and details are found in [Running Urho3D player application](https://urho3d.github.io/documentation/HEAD/_running.html) (windowed: '-w').

-------------------------

1vanK | 2020-12-29 00:51:25 UTC | #3

We fixed this not long ago. Are you using the latest version of the engine? https://github.com/urho3d/Urho3D/pull/2678

-------------------------

johnnycable | 2020-12-28 16:02:03 UTC | #4

Had same problem until some time ago, but was then fixed. Be sure to use latest.

-------------------------

elix22 | 2020-12-28 16:30:21 UTC | #5

I rarely follow the discussions here .
But once in while I take a glance ...
@1vanK ,  your commit looks wrong to me .
I have written and using my own reference 3D editor , works fine on any HDPI/Retina monitor 
Division by uiScale_ is necessary , specifically when uiScale_ != 1.0
Please note that the default value  of uiScale_ = 1.0 , regardless of the type of the monitor been used.
Just my 2 cents ....

-------------------------

1vanK | 2020-12-28 22:23:51 UTC | #6

I don't have a retina display. A owner of this display sent PR and I merged it. But you can discuss the correct approach with the PR's author.

-------------------------

CE184 | 2020-12-29 00:53:07 UTC | #7

just to confirm here that I don't have the issue anymore with the latest repo, although the UI is slow responsive on mac :) 
as for the PR, I'll let you guys figure out.

-------------------------

