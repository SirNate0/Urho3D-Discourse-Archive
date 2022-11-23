ghidra | 2017-01-02 01:02:09 UTC | #1

I was looking at the Screenspace.glsl and the Uniforms.glsl, but nothing is jumping out at me as a potential uniform for the viewport dimension.
If I am rendering full screen on a 1920x1080 monitor, I need to get the values of 
[code]
float xdim = 1.0/1920.0;
float ydim = 1.0/1080.0; 
[/code]
For now I am hard coding it, but it would be good to be a little more flexable.
I tried plugging in a few built in functions and uniforms, but not getting what I am expecting.

Thank you.

-------------------------

cadaver | 2017-01-02 01:02:09 UTC | #2

Look at the uniform "cGBufferInvSize". It's not only for deferred rendering, but all viewports.

Note that this is the size of the final rendertarget in your renderpath. If you're using other intermediate rendertargets, for example one that is named "MyTexture" then the renderpath processing will attempt to set an uniform "cMyTextureInvSize" (which should be defined by your shader) to contain the inverse size of that rendertarget.

-------------------------

ghidra | 2017-01-02 01:02:10 UTC | #3

cool, that seems to have done it.
Inverse is always confusing to me. Looked it up, and it can either mean:
[code]-x[/code]
or
[code]1/x[/code]
When I plugged in that uniform, it did exactly what I needed, so it is the latter. 
[code]
float xdim = cGBufferInvSize.x;
float ydim = cGBufferInvSize.y; 
[/code]
Thank you.

-------------------------

