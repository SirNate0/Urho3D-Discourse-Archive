Kai | 2017-01-02 01:00:38 UTC | #1

Hi,
There is a trick to show the DebugRenderer in the UI element View3D ?
Thanks.

-------------------------

cadaver | 2017-01-02 01:00:38 UTC | #2

Currently debug geometry rendering is limited to backbuffer views. It should be possible to add an API for enabling it in any view.

-------------------------

Kai | 2017-01-02 01:00:38 UTC | #3

Thanks, I will look into it.

-------------------------

cadaver | 2017-01-02 01:00:38 UTC | #4

If you pull the latest master, there is now option to control per viewport ( Viewport::SetDrawDebug() ) whether debug geometry should render, instead of hardcoding to backbuffer views only. Default is true. Naturally, a DebugRenderer component is also required in the scene the viewport is referring to.

-------------------------

Kai | 2017-01-02 01:00:38 UTC | #5

Wow, thanks !
This confirms the right choice I made by switching to Urho3D : you are very attentive.
But I'm sorry to say that I have a problem : the debug geometry is Y axis reversed on UI element View3D.
I use Urho3D 1.31 and OpenGL. Maybe a problem with OpenGL coordinate system ?

-------------------------

cadaver | 2017-01-02 01:00:38 UTC | #6

Good find. Drawing to textures on OpenGL requires special attention (flipping the projection matrix) and in this case the projection is un-flipped too early.

-------------------------

cadaver | 2017-01-02 01:00:38 UTC | #7

Should be fixed now. Additionally, debug geometry rendering in OpenGL deferred mode should be improved now such that the correct depth buffer values (and thus correct depth testing) are used.

-------------------------

Kai | 2017-01-02 01:00:38 UTC | #8

It's fixed, thanks again.

-------------------------

