najak3d | 2020-08-26 21:00:51 UTC | #1

I'm getting this mysterious error in UrhoSharp for my GLSL shaders:

"Error: uniform cColor specified with different precision in different shaders"

I get this for all of my uniforms.

   uniform vec4 cColor;

Is how it's specified.

-------------------------

Eugene | 2020-08-27 02:42:56 UTC | #2

1) Try to set uniform precision explicitly.
Keep in mind that `highp` may be unsupported in pixel shader, so stick with `meduimp` or `lowp`.

2) Try to explicitly guard out uniforms that are used only in one shader (vertex or pixel) with `#ifdef COMPILEVS`/`#ifdef COMPILEPS`

-------------------------

najak3d | 2020-08-27 01:24:27 UTC | #3

Eugene, that advice was perfect, thank you!   It solved my problem completely.

I didn't have the #ifdef COMPILEVS (or PS), and I also added the 'mediump' specifiers to be more explicit.

-------------------------

