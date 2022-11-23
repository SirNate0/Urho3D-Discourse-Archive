sabotage3d | 2017-01-02 01:07:22 UTC | #1

Hi,
I have a really small texture 3x6, It works properly on Desktop but it renders black on Android. The log doesn't show any warnings or errors. Is there anything special I need to enable in order to make it work ?
Link to the texture: [i.imgur.com/vJw3sxe.png](http://i.imgur.com/vJw3sxe.png)

-------------------------

friesencr | 2017-01-02 01:07:22 UTC | #2

It might need to be power of 2 to work on mobile.  As far as I know the video card still allocates a power of 2 memory for the image.  This way it can do efficient mipmap filtering and things like that.

-------------------------

sabotage3d | 2017-01-02 01:07:22 UTC | #3

Basically this is a voxel texture it doesn't need any filtering that's why it is so small. Is there a proper way to cheat the power of 2 limitation I read somewhere it shouldn't cause problems if I don't need filtering.

-------------------------

rasteron | 2017-01-02 01:07:22 UTC | #4

Why not just convert it to a power of 2 and do some clipping/resizing if necessary..

Your image now 8x8
[i.imgur.com/cWddzOA.png](http://i.imgur.com/cWddzOA.png)  [img]http://i.imgur.com/cWddzOA.png[/img]

-------------------------

thebluefish | 2017-01-02 01:07:23 UTC | #5

I'd suggest reading up [url=http://aras-p.info/blog/2012/10/17/non-power-of-two-textures/]this article[/url] on NPOT textures. If we get support for OpenGL ES 3.0, it will be a non-issue. However this is going to be a limiting factor on OpenGL ES 2.0 and below. Even if we try to enable the extension, it would only work on [i]some [/i]android devices, and iOS would be out of the question AFAIK.

-------------------------

sabotage3d | 2017-01-02 01:07:24 UTC | #6

I tried resizing the image to power of 2 but it forces me to tweak the UVs with the same scale ratio wich leads to details that will overlap. Does anyone know a better way ?

-------------------------

