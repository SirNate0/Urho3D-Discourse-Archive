najak3d | 2021-02-20 03:24:34 UTC | #1

We're porting a project, where our 3D view is implemented in pure OpenGL, and for our Vector Lines, we make use of the LineStrip primitiveType.

How do we render LineStrips using Urho3D?  Or if this support doesn't exist, what is the appropriate alternative to get an equivalent effect?

(Meshed Lines is problematic, when the camera orientation is free flying -- can be horizontal, or angled, etc... not a top-down.   We can only use mesh-based lines for the top-down view, but not this free flying 3D view.)

EDIT:  I see that PrimitiveType.LineStrip is exposed.   However, Urho3D doesn't seem to provide a way to set the LineWidth setting.   We set this for OpenGL ES in our current project.

-------------------------

WangKai | 2021-02-20 06:19:02 UTC | #2

I think there are many ways to achieve this. 

You can make up a line with width as a mesh, e.g. using triangles to compose a strip (line with width). And you can also using shader to achieve more on the screen.

-------------------------

najak3d | 2021-02-20 06:21:02 UTC | #3

I see the core reason Urho3D does not support GL.LineWidth -- it was DROPPED from Open GL 3.3 (modern versions of OpenGL).   We enjoyed this feature in our current app, since it was using an much older version of Open GL ES which still had this support.

We are turning now to some of the contorted screen space methods that we see online.  These are far more complex to use, but should do the trick just fine.

-------------------------

