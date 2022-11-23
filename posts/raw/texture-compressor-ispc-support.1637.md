boberfly | 2017-01-02 01:09:09 UTC | #1

Hi all,

I've had time to do some dev work and managed to get a basic texture compressor to work, and Intel's ISPC files to build with Urho3D/CMake.

Here it is:
[url]https://github.com/boberfly/Urho3D/tree/ispc_texcomp[/url]

Currently it is working (I think), however I'm only doing a raw image dump of the result and not filling out the header info for ktx or dds (yet) or supporting mips or arrays.

This should allow things like transcoding uncompressed images to GPU-compressed formats on the fly, or having a tool in Urho3D to do the conversion instead of relying on a third-party tool.

To build it from my branch, make sure -DURHO3D_ISPC_TEXCOMP is set, and you have the environment variable $ISPC_DIR pointing to where the ispc binary is located. You can get a build of ISPC or build it yourself from here:
[url]https://ispc.github.io/[/url]

More info on the compression library here:
[url]https://software.intel.com/en-us/articles/fast-ispc-texture-compressor-update[/url]

You'll also notice that I'm adding ASTC texture compression support. In another branch I've managed to get OpenGL ES 3.1 to work, but that's for another post.

There's some potential to allow SIMD optimisation in Urho3D by using ISPC files here and there, and combining it with the task worker pool system could have some really big performance wins in some places. It also covers Arm's Neon instruction-set and it will try to use this when building for Arm (the binary release of ISPC from Intel doesn't seem to expose this backend though so I haven't tested it yet). At runtime it will also pick the best instruction set to use based on CPU.

Enjoy
-Alex

-------------------------

sabotage3d | 2017-01-02 01:09:10 UTC | #2

That's great. Can't wait to try it on ES 3.1.

-------------------------

