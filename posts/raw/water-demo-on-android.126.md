Mike | 2017-01-02 00:58:14 UTC | #1

Playing with Water demo (example #23) on Android and lowering waterNode position to 2 (instead of 5), second camera appears to be misaligned (cubes are fully immersed on Android instead of being only partly immersed on desktop).
It's like if second camera rotation doesn't follow first one.

-------------------------

cadaver | 2017-01-02 00:58:14 UTC | #2

OpenGL ES does not support clip planes like desktop GL or D3D9, so the water example will not work fully. This is documented in the API differences section of the documentation.

-------------------------

Mike | 2017-01-02 00:58:14 UTC | #3

OK, thanks, hoped that there was a turnaround for this.

-------------------------

