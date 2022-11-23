najak3d | 2020-12-09 01:30:59 UTC | #1

I realize that there was an experimental branch created for this a few years ago.

We could really use Geometry Shaders for our mapping project.   The most important geometry shader would translate a simple sequence of points into the geometry to make smooth/anti-aliased lines that also have an outline.

We currently accomplish this on the CPU by translating lines into Triangles, but would prefer this be done in a Geometry shader instead.

Are there any plans to make put Geometry Shader support into the main Urho3D release?

-------------------------

JSandusky | 2020-12-09 06:28:55 UTC | #2

There's a [closed pull for RBFX](https://github.com/rokups/rbfx/pull/203) containing GS, HS, DS, and CS (limited to structured-buffers as far as that zoo goes). Though IIRC the CS interface needs to get fixed up for dispatch counts, I write so much OpenCL that I'm 100% sure I goofed that. It's w/e, anyone can pick that up / port it over - doesn't matter to me. I'm all about that sweet sweet variable-rate-shading anyways.

Also never got rid of the old stuff (only GS, HS, DS - RBFX PR includes lessons learned), though it's just a [zip-ball now](https://github.com/JSandusky/Urho3D) and probably not pleasant to merge into the current Urho.

-------------------------

1vanK | 2020-12-09 07:12:29 UTC | #3

There are several implementations (by CodingMonkey for example). It's just not enough to add some code and say good luck with it. This code needs to be maintained. For example, the current state of PBR shaders is a very sad sight.

-------------------------

najak3d | 2020-12-09 07:56:20 UTC | #4

JSandusky - those acronyms are gibberish to me - GS, HS, DS, CS - what do those mean?

IIRC, you were the one who hacked in Geometry Shaders into an Urho branch a few years ago, right?

We're only interested in getting Geometry Shaders if they are incorporated into the main branch, and become a legitimate part of Urho3D.   Then we can wrap this functionality for UrhoSharp (which is what we use).

If it's only going to remain on a branch, then we're not really interested in it, and will stick with our current methods of building the geometry using the CPU, and having larger vertex/index buffers.

Do you think there's much of a chance that Geometry Shaders will be incorporated into the main branch of Urho3D?

-------------------------

JSandusky | 2020-12-09 10:12:44 UTC | #5

Geometry shader, Hull shader, Domain shader, Compute shader. The only "hack" was that I refused to "hack" in binding-point remapping to account for OpenGL being junk so GS/HS/DS had to share their binds with the VS, naturally I aggressively warn should there be mismatches.

There's no way I'll ever port the RBFX stuff over and I'm happy with my fork, so unless someone picks it up to port over or starts up something new it'll never happen.

-------------------------

najak3d | 2020-12-09 10:13:22 UTC | #6

Thanks for the honest answer.   We'll need to stick with Urho3D main branch.

-------------------------

