dtrq | 2017-01-02 00:59:09 UTC | #1

Hello.
Since shadowmaps look ugly with toon shading I'm going to use, I wonder if it's possible to modify LibSolid to get simple stencil shadows without modifying the engine itself. I don't need doom3 level of robustness and optimization, just simple sharp shadows for dynamic objects, blending nicely with toon shading.

-------------------------

cadaver | 2017-01-02 00:59:09 UTC | #2

If you render shadows into the stencil buffer, then you'll need to just use the non-shadowed variation of the shader, and the stencil buffer will tell where to apply the light. But naturally you have to modify the engine C++ code to actually draw/extrude the shadow casters into the stencil buffer first.

The stencil is already being used to limit the light influence to the light's geometric shape (same as the light volume in deferred rendering.)

-------------------------

dtrq | 2017-01-02 00:59:10 UTC | #3

AFAIK it's possible to extrude shadow volumes with geometry shader ([http.developer.nvidia.com/GPUGem ... _ch11.html](http://http.developer.nvidia.com/GPUGems3/gpugems3_ch11.html)), but I have no idea how shaders interact with stencil buffer.

-------------------------

