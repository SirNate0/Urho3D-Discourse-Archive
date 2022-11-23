sabotage3d | 2017-04-16 14:50:42 UTC | #1

Hi, 
I am getting some artefacts in RibbonTrail. It looks like polygon kinks are causing this. The trail is drawn only using x and y. The trail type is set to TT_FACE_CAMERA and my camera is orthographic. The material is RibbonTrail. Any ideas on how to fix this issue?

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c8eab7c7128ff21e3fd1b6d78ae13f1cd981e425.png'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/28adf0e723637b9517b6213de68efc77deb8c71c.png'>

-------------------------

jmiller | 2017-04-17 00:51:17 UTC | #2

I had noticed the same distortion and increased the number of columns (default 1). Maybe this can help?
/// Set number of column for every tails. Can be useful for fixing distortion at high angle.
void SetTailColumn(unsigned tailColumn);

-------------------------

sabotage3d | 2017-04-17 10:36:42 UTC | #3

I think it does help, but also increase the number of triangles a lot. I am getting it on straight lines as well it is quite apparent in 2D, with higher width. Would it help to change TRIANGLE_LIST to TRIANGLE_STRIP or nudging the triangles not to overlap?

-------------------------

sabotage3d | 2017-05-09 21:31:35 UTC | #4

I am kind of stuck with this issue. It is getting worse if I increase the width and the segments. Is there anything I can do it in the shader or anything else that would help reduce these artefacts? I think it is similar to this topic: https://www.reddit.com/r/gamedev/comments/387pwc/rendering_3d_trails/
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/47ed90a14629a1d73d34610e7e9b037179af788f.png'> 
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/949e00bbd683359d9064f34bcfcd2924bb22da04.png'>

-------------------------

godan | 2017-05-10 01:11:27 UTC | #5

So, from a geometrical point of view, the fact is that offsets are nasty... You simply can't offset using only vertex translations, and a) get a good offset and b) not get intersections.

In my project, [I basically did the same thing](https://github.com/MeshGeometry/IogramSource/blob/master/Components/Graphics_CurveRenderer.cpp) as in the link you posted. The idea is:

- Get the vertices of the path. This is the center line.
- Create a billboard for each edge whose Y direction is parallel to the path edge, whose position is the midpoint of the edge, and has some width. Enable FC_DIRECTION to constraint he billboard to only rotate around the Y axis.
- In a shader, trim back the rendered pixels to avoid the intersections. This is not perfect, since you usually use one value for all edges, which is not good.
- In my implementation. I added another set of billboards at each vertex of the path. These render a circle whose diameter is the same as the width of the edge billboards. Enable FC_ROTATE_XYZ to have this always face the camera. This hides errors in the edges and creates rounded corners.

It's not perfect, but it is substantially better than the ribbon trail...

Here is an example of how this technique looks: https://meshgeometry.github.io/Demos/CurveEdit/IogramPlayer.html

-------------------------

Modanung | 2017-05-10 15:24:08 UTC | #6

I'm still using CodeMonkey's [TailGenerator](https://github.com/MonkeyFirst/urho3d-component-tail-generator) in heXon. Cross-breeding these two components might be what more people are looking for.

-------------------------

sabotage3d | 2017-05-10 21:07:30 UTC | #7

Thanks godan. I tried the demo but the joints are quite visible. Also I am not sure if this technique would work with textures properly and might look segmented. Do you have more demos with ribbons?

-------------------------

sabotage3d | 2017-05-10 21:05:38 UTC | #8

Thanks Modanung. I already tried TailGenerator but it exhibits the same problems as the one in Urho3D is based on this one if I am not mistaken.

-------------------------

Lumak | 2017-05-10 21:29:08 UTC | #9

Not sure if this would be appropriate as I think you're working with 2D not 3D - https://discourse.urho3d.io/t/vehicle-skid-strips/2018

-------------------------

sabotage3d | 2017-05-12 20:29:37 UTC | #10

Thanks Lumak. I think the vehicle skid strips have the same problem. Do you know if there is a way to fake transparency by sorting the polygon strips or a way to handle transparency per trail?

-------------------------

Lumak | 2017-05-12 21:38:10 UTC | #11

No, don't know how to fake transparency.  But in regards to vehicle strip, I think overlaps would occur if distance from segment to segment is relatively short and curved rapidly.  However, the strips are connected from end to end and if the short curving segment causes overlap then it is actually really easy fix. Think about how a plane eqn works; in the strip case, it'd be as easy as checking the dot product of new points with the last segment line.

-------------------------

Leith | 2019-01-17 08:45:20 UTC | #12

Part of my work in robotics programming involved computing 'motion paths', I'm considering taking a closer look at this issue, as I think the current results are unacceptable - the wireframe in particular displays some fundamental issues in the way the tri-strip is being tesselated, including slivers generated by vertices which are very close to others, and rightly should have been 'welded' with some distance threshold, although the overdraw caused by z-fighting overlapping triangles can probably be eliminated by drawing the trail geometry in two passes - the first with depth-writing enabled, as a depth-only pass, and the second as the full pass, with depth-testing enabled.

PS - ugh, they're not even tri-strips, they are quads in our current implementation. I think that a possible solution to the issue of overlaps is to generate two Catmull-Rom splines, and then generate a tri-strip based on sampling the two curves. But using two render passes as mentioned above would likely be more performant.

-------------------------

glebedev | 2019-01-17 15:19:14 UTC | #13

As a workaround you can use checker board "discard" in pixel shader in screen space. It will be consistent on overlapping geometry. The only question is - will the image be acceptable for your case.

-------------------------

WangKai | 2019-02-26 15:35:54 UTC | #14

I once implemented sword rail using triangle strips which means there is no overlaped between quads.
Edit: it is the overlapped part of the quads cause the issue.

-------------------------

Leith | 2019-02-27 10:09:07 UTC | #15

Yeah, I sort of said that too, well I implied it :P

-------------------------

WangKai | 2021-02-22 17:19:41 UTC | #16

What about changing the alpha blend mode?

-------------------------

