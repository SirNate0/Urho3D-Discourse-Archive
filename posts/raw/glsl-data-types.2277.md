Bananaft | 2017-01-02 01:14:28 UTC | #1

In my inhumane shader experiments I stumbled into weird behavior, when some data types didn't worked as Uniform or Varying. Namely:

Uniform Integer and Varying mat3, no compilation errors, but no result either. First one I fixed by using float, second by using mat4.

Standard shades not using any of this, so I'm not sure if it is a bug, or it's just not implemented as being unnecessary?

-------------------------

cadaver | 2017-01-02 01:14:28 UTC | #2

Varyings should have nothing to do with the engine (just the GLSL compiler and GPU driver).

Int uniforms are not supported in the engine due to historically being difficult to support on Direct3D(9), and to therefore keep feature parity (lowest common denominator). They should be supportable on D3D11 though, so OpenGL support would make sense too.

-------------------------

cadaver | 2017-01-02 01:14:28 UTC | #3

Ints should now work as uniforms on OpenGL in the master branch (Also definable in the material editor.)

-------------------------

Bananaft | 2017-01-02 01:14:29 UTC | #4

Whoa, thank you.

-------------------------

