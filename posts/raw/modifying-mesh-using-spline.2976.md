slapin | 2017-04-04 05:04:17 UTC | #1

Hi, all!

I have a tiny mesh piece (a small section) and a spline.
I want to extrude this mesh section over spline so it becomes solid mesh (so it should be
properly compressed / inflated on spline turns).
Any ideas how to approach this?

Thanks!

-------------------------

smellymumbler | 2017-04-08 00:17:45 UTC | #2

Like a road mesh, or a bridge?

-------------------------

slapin | 2017-04-08 20:48:28 UTC | #3

Like a road mesh and/or bridge

-------------------------

jmiller | 2017-04-09 04:23:24 UTC | #4

There are some algos and ideas out there.
http://gamedev.stackexchange.com/questions/23151/how-do-i-generate-a-3d-race-track-from-a-spline

As for Urho specifically, the RibbonTrail class implements Geometry in a roughly similar way, so maybe it will be helpful?

-------------------------

Sinoid | 2017-04-09 05:15:56 UTC | #5

The terms you're looking for to help with googling are "lofting" and "parallel curves"/"parallel transport."

Assuming you had a spline and planar mesh to extrude the process is:

- For each vertex compute the planar coordinates on the constrained axes (signed distance from 0,0 on XY where Z is the extrusion axis)
- March along the spline, at each step build an orthonormal basis system
- Emit vertices as SplinePositionTd + OrthonormalBasisX * SignedDistanceX + OrthoNormalBasisY * SignedDistanceY
- Rotate vertex normals by minimal twist quat between the previous and next direction vector
    - That means knowing where you came from and where you will be next
- Deal with UVs however you choose to
- Repeat until done
- Emit index buffers
- Recompute tangents (you cannot rely on rotating tangents)

It's relatively simple for extruding a 2d polygon, but it's a nightmare to loft an arbitrary mesh as that's full of edge of cases.

-------------------------

godan | 2017-04-09 19:29:40 UTC | #6

IOGRAM has a bunch of geometry related functions for this. Here is the [source](https://github.com/MeshGeometry/IogramSource/blob/master/Geometry/Geomlib_PolylineLoft.cpp), and this is what I mocked up in the editor in about ~5min (try the [live version here](https://dl.dropboxusercontent.com/u/69779082/IogramDemos/Loft/Loft/IogramPlayer.html), and get [project files](https://www.dropbox.com/sh/357tf0cpus559ht/AACbpaEJmMGLZ7556A0VQ8SDa?dl=0) here):

[img]http://iogram.ca/wp-content/uploads/2017/04/loft.gif[/img]

-------------------------

darkirk | 2017-04-29 20:42:04 UTC | #7

Hello! I'm trying to create something like this: 

https://www.youtube.com/watch?v=H7SJI_HFHNA

With Urho. I've did this before in UE4's Blueprint (as seen here https://docs.unrealengine.com/latest/INT/Resources/ContentExamples/Blueprint_Splines/), but it way more difficult in Urho. Could anyone help me out with some tips?

-------------------------

slapin | 2017-04-30 00:31:04 UTC | #8

Well, with Urho a general approach is to do everything manually.
I currently work on the same thing (roadmap generation algorithm + building road mesh structure),
the code is a bit messy and unfinished, but I'd like share what I found.

The basic structure is road intersection. [b]We consider close half of each road to be belonging to intersection.[/b] The center of intersection is considered (0, 0) and we use 2D vectors for all calculations at this stage. We sort roads by angle using Atan2 and split by pairs.
Example: intersecting roads ABCD. After sorting by angle CABD. Split by pairs - CA, AB, BD, DC.
For each pair we draw spline through points on outer road edge and plain lines through middle
points of roads. Also we add extra geometry for sidewalks/borderstones.
After we got 2D geometry we project it to the ground. I project all road itersection coordinates to
terrain and then smooth-out roads using Spline. And then correct the landscape to prevent it being
higher than the road. That is basic idea. Hope that helps.
Some people suggest using shader magic to build roads directly using terrain itself, but the solution is too complex and have too many limitations.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/781750ca33129aa2901d5e914876295ade0c6e54.png" width="287" height="500">

-------------------------

