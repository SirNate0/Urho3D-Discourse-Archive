Sinoid | 2018-09-18 02:15:36 UTC | #1

I've dumped off a bunch of my procedural geometry helpers:

https://github.com/JSandusky/Urho3DProcGeom

Highlights are lofts, lathes, Carve-CSG, and a bunch of miscellaneous helpers ranging from dumping UV chart images to calculating normals.

Even just the basics of working with Carve should be useful for someone.

---

I use it to do stuff like this:

![image|690x368](upload://uR41MoVNdPtx57DDcdF7v2dne02.png) 

![image|690x368](upload://cewdMUCuwooMAkmAzMc3YwIv78L.png) 

In those images I'm using `LoftSpine` and `Lathe` to take the 2d half-edge of a [UDMF](http://doom.wikia.com/wiki/UDMF) map (Doom2 Map01 here) and refine it. These are just old test shots so they're naive (seam issues).

---

Laplace stuff is a WIP, wasn't as easy to port over as I'd hoped (rigidly defined vs undefined vertex structure). There's a [CGA](https://cehelp.esri.com/help/index.jsp?topic=/com.procedural.cityengine.help/html/manual/cga/basics/toc.html)-like volume grammar that I'm sorting out the license issues with which I'll toss in there later if that goes well.

The dependencies (ParShapes, Carve, LibIGL, and Eigen) aren't included in the repo and it's assumed you'll know how to set them up as a litmus test. It's really all just *dump-code* that you can lift as desired though.

IGL and Eigen aren't strictly required.

If something doesn't work, or you can't figure out how to set it up to build, ask away.

-------------------------

JTippetts | 2018-09-19 23:24:05 UTC | #2

Thanks for this. I've been getting an itch to do some more procedural building gen, so this'll give me a jumping off point.

-------------------------

Sinoid | 2018-09-20 03:52:41 UTC | #3

@JTippetts, I wouldn't trust anything too much. I'm not sure how much I've hacked on what since the last time I tested any of it (a lot of my proc-gen I do in monogame and then export). Everything should be *close* when it doesn't work though.

I'm hoping to get around to making sure everything still does what it says it does this weekend.

---

Bone-weight calculation is almost finished, just need to finalize what to do with the calculated weights and then verify the port works.

Can do [Pinnochio heat-weights](http://www.mit.edu/~ibaran/autorig/index.html) and [Bone-Glow](https://web.cse.msu.edu/~cse872/papers_files/BoneGlowImprovedWeightAssignment.pdf) which treats bones like a light-filament.

If you're curious how not-crazy that is:

https://github.com/JSandusky/Urho3DProcGeom/blob/master/ProcGeom/Laplace.cpp

Speed-wise, my other implementation takes ~2 seconds to compute weights for a 5k vertex mesh (includes C++/CLI overhead and converting all data from MonoGame -> MathGeoLib and-back) - bone-glow is 6x slower (or more if the iteration steps are changed).

No idea what anyone else would ever use it for (Spore-clones and jacked-up-character-designers I guess) but it's a handy tool to have around, bone-weighting some voxel seaweed or something so it can sway.

-------------------------

Sinoid | 2018-09-27 22:49:18 UTC | #4

Minor additions of late:

- [DX UV-Atlas tex-coord generation and planar coords](https://github.com/JSandusky/Urho3DProcGeom/blob/master/ProcGeom/TexCoords.cpp)
    - Requires Windows (DirectX math + a lot of the windows specific macros for usage specification and SDLC that are spread throughout the library)
- [Malfunctioning marching triangles](https://github.com/JSandusky/Urho3DProcGeom/blob/master/ProcGeom/MarchingTriangles.h)
    - roughly based on Araujo: http://www.cs.toronto.edu/~brar/blobmaker/ISpoligonization.pdf
    - Probably will replace with Delaunay, vertex instead of edge based seems to have tons of problems with folding triangles over each other ... bummer because it's so fast emitting up to 5 triangles per pass
    - Or replace with an advancing front of voxel-like cells, some sort of manifold version of surface nets
- More general helpers
    - general pre/UV transformation
    - centroid / normal extraction
    - make triangles unique
    - conversion of vertex data formats (still manual, helpers just take out the routine)
- [UDMF-like](https://zdoom.org/wiki/UDMF) loading of 2d half-edge mesh from exported data
    - Processing utilities depend on MathGeoLib for polygon and line (triangulation and *motorcycle shrinking*)
    - intended as template data for refinement / lofting, not for use as a final form
    - not actual UDMF yet, relies on export to XML from a fork of GZDoomBuilder

-------------------------

Sinoid | 2018-09-28 06:39:28 UTC | #5

Meh, apparently I called it "*malfunctioning marching triangles*" too soon, just required a couple of tests to explicitly force it to close an angle.

Marching Triangles:
![image|604x500](upload://gf5Gy5ardfVXp6Hw6gn8A48lrIm.png) 

Advancing Front and it's family (marching triangles, 3D Delaunay) are basically never encountered, outside of CGAL there really aren't any implementations available to look at (aside from a PCL version, but it walks a point-cloud not an arbitrary function) so here's a summary for anyone not wanting to read a header file's comments:

- Uses a surface walking algorithm to walk across an arbitrary signed-distance function, emitting vertices and edges along an advancing front-line (like a historic battle map)
- **Pros over voxels:**
    - All steps advance the surfacing
        - No prestorage step for filling a volume / hermite data
    - Fairly regular triangles, no marching cubes and manifold-dual method skinny triangles
        - Resulting surface is thus more suitable for bone-weighting and animation than those with skinny triangles
    - Tweakable to vary edge length based on function curvature
    - **Manifold** provided the surface can properly mate, the single most important part, non-manifolds are hell in geometry processing
        - Naive surface nets and dual-contouring are not manifold
        - Extended-Marching Cubes, Dual Marching Cubes, and Manifold Dual-Contouring are manifold (and expensive)
    - Shape control is more intuitive, edge length vs. cell-size
        - The exact placement in a voxel cell effects final edge length + cell configuration and thus mesh density
    - Modest memory requirements
        - Does not require storing heaps of data  like a 2048^3 voxel volume does
        - Data storage is entirely for the *front lines* of the surface progression and the emitted geometry
        - Voxel methods can surface walk though, just at higher SDF evaluation cost
    - Modest execution requirements
        - Compare to storing the sampling of the 8 edges of a cell for hermite voxel data
    - Vertex-sharing is trivial and natural
    - Can mesh into arbitrary geometry, provided they have an open-loop and the SDF will approach a suitable proximity
        - Can seed from the loop of an arbitrary mesh
- **Cons over voxels:**
    - Not easily parallelized
        - Only really suitable for OpenMP loop parallelization
        - Because a voxel volume is not stored you can't split it up to evaluating the volume on the GPU and surfacing on the CPU
    - Risk of the surface never closing, extreme incoherence in the SDF function could result in a front never connecting with another-front, causing it to loop over the surface again and again until a triangle limit is hit
    - Seeding issues
        - Independent surfaces need to be surfaced independently, *floating balls* are not a *one-and-done* because the surfaces are not connected and thus cannot be walked in a single pass
        - Seed point selection can result in the algorithm walking the inside of a CSG-subtraction shape instead of the outside of the desired shape additive shape
            - Resolvable, but non-trivial (requires metadata about the SDF shapes to chose raycast locations)
    - Thrashes the heap more than voxel methods, fronts are split, merged, and destroyed at a fairly constant frequency and vertices are pretty short-lived

Sort of odd that there really isn't much out there aside from research on the general technique. Sticking this guy in the repo under MIT-lic. makes it basically the only open one in existence.

Papers referenced when I implemented:

- [Curvature Dependent Polygonization of Implicit Surfaces](http://www.cs.toronto.edu/~brar/blobmaker/ISpoligonization.pdf)
    - This is the core of how I approached it, vertex based rather than edge based
- [Adaptive Implicit Surface Polygonization using Marching Triangles ](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.6409&rep=rep1&type=pdf)
- [An Advancing front Delaunay Triangulation Algorithm](http://www.dtic.mil/dtic/tr/fulltext/u2/a257277.pdf)
- [Marching Triangles: Delaunay Implicit Surface Triangulation](http://fab.cba.mit.edu/classes/S62.12/docs/Hilton_marching_triangles.pdf)
- [Edge-constrained Marching Triangles](http://homepages.inf.ed.ac.uk/rbf/PAPERS/EdgeConstMT.pdf)
- [ Marching Generation of smooth structed and hybrid meshes based on metric identity](https://imr.sandia.gov/papers/imr14/wild.pdf)

---

Omission of regular voxel methods from the repo is deliberate, you can practically copy + paste them these days.

Edit: the final form won't appear in the repo, I'm okay with the core of it being there, just not a working case given how hard I was downvoted in /r/proceduralgeneration when I presented the solution to the infinite iteration problem.

Some days, I swear I'm surrounded by idiots.

-------------------------

