Don | 2017-06-03 19:44:31 UTC | #1

Good Afternoon,

I am trying to write a shader using the refract pass that compares the depth at a given screen position with the depth at the same screen position from the previous passes. The goal being that I find the difference in depth between the object I am rendering and all others in the scene. Currently, this is what I am trying to do.

```
//this retrieves the previous depth at location
texture2D(sDepthBuffer, vScreenPos.xy).r;
//this retrieves the depth at the current fragment (this is done in the vertex and interpolated to the fragment)
GetDepth(gl_Position);
```
Perhaps this is not the correct way to achieve this. Could someone point me in the right direction? Thanks!

-------------------------

Don | 2017-06-07 03:34:22 UTC | #2

Just bumping this thread.

-------------------------

Eugene | 2017-06-07 09:49:53 UTC | #3

> The goal being that I find the difference in depth between the object I am rendering and all others in the scene.

You need to have two depth textures. One is input as texture, the second is destination buffer for rendering,

-------------------------

Don | 2017-06-08 01:44:24 UTC | #4

That would make sense, given that OpenGL does not allow buffers to written to and read in the same pass. Could you show me how I would structure a render path or technique to accomplish this? I still don't quite understand how shaders/materials/render paths/techniques work together.

-------------------------

jmiller | 2017-06-21 15:58:23 UTC | #5

Hello,

cadaver explained depth rendering in more detail: https://discourse.urho3d.io/t/how-xml-rendering-framework-works-to-get-depth/80/3

Until more specific info comes to the thread, there are a number of [url=https://discourse.urho3d.io/search?q=texture+depth]depth texture threads[/url] that may be informative.

(other than, of course, the docs on [url=https://urho3d.github.io/documentation/HEAD/_rendering.html]Rendering[/url] that links to the subjects you mention)

HTH

-------------------------

