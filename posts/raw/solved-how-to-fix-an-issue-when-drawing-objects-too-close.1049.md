TikariSakari | 2017-01-02 01:05:03 UTC | #1

Hello, I am kind of having a problem when I try to create planes on top of my map. It is most likely not the best way to do things, but I am kind of creating a tiled map on top of ground for showing the area where the unit can move. It looks normal and fine on desktop (both windows and linux), but the problem is my phone. This same thing even happens on the sample: 10_RenderToTexture.

Here is the picture [url]http://i.imgur.com/Q8rX41q.png[/url] the whole area should consist blue planes of same size, like tiles.

I know that the cause is that the plane is too close to the object behind it. I set the planes to be 0.1f higher, and I also noticed that if I set the camera closer to the planes, they appear without the lines, so it is somehow distance based thing.

This thing also sometimes seems to happen even with the decals at least on my phone, which makes me wonder if this is mostly something to do with my phone (Nexus 5 + lollipop 5.1), or does it also happen on other opengles systems?

Something that I noticed is, that the lines always appear to be horizontal line. Also the width of a single line seems to be the same. Considering that the blue area consists of 11 different planes, it is interesting how it actually creates the lines horizontally regardless from what angle the camera is.

Also for some reason depending on what angle from the ground I am watching, the lines appear to be wider, same goes depending how far the camera is from the planes. If I set the camera close enough, the blocks are shown completely and there is no "lines" at all.

Pictures to compare camera angle:
[url]http://i.imgur.com/06IkRGx.png[/url] vs
[url]http://i.imgur.com/ldiV5uE.png[/url]

I guess one way to fix it would be to simply just set the distance further away from the ground, or maybe I can set the height of the tiles higher if the camera is further away from the ground.

Edit: Also this thing has been on the urho as long as I have been dabbling with urho (at least 3 months), so it is not something that has appeared in recent patches.

-------------------------

cadaver | 2017-01-02 01:05:03 UTC | #2

This is caused by too low depth buffer resolution, which depends on the device. You can play around with the depth buffer bitdepth request in OGLGraphics.cpp, which is actually skipped for GLES completely (ifdef'ed out) but it may be that if you don't get as much depth bits as you request OpenGL fails to initialize at all. Not sure of this.

Other than that, you can use more distance, or constant depth bias in the material. Also setting a smaller far clip value to the camera should help.

-------------------------

TikariSakari | 2017-01-02 01:05:04 UTC | #3

[quote="cadaver"]This is caused by too low depth buffer resolution, which depends on the device. You can play around with the depth buffer bitdepth request in OGLGraphics.cpp, which is actually skipped for GLES completely (ifdef'ed out) but it may be that if you don't get as much depth bits as you request OpenGL fails to initialize at all. Not sure of this.

Other than that, you can use more distance, or constant depth bias in the material. Also setting a smaller far clip value to the camera should help.[/quote]

Setting this like you mentioned for the GL_ES_VERSION_2_0 seems to work on my phone.
[code]        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);
[/code]
But if as you said this might crash on some systems, it might not be the best solution.

Edit: I tried using the depth bias for material, maybe I did something wrong, but the whole material became invisible if I set  the constant to anything other than 0. For example I tried this on the grass material:
[code]
<material>
	<technique name="Techniques/NoTexture.xml" />
	<parameter name="MatDiffColor" value="0.01 0.1 0 1" />
 <depthbias constant="1" />
</material>
[/code]
Maybe this is not the way it is supposed to be used. Also this was invisible on my desktop as well (linux + opengl, didn't try with directx), or I need to enable something to use the depth bias. I also tried to use values between 0 and 1.

-------------------------

cadaver | 2017-01-02 01:05:04 UTC | #4

Constant depth bias 1 means pushing it all the way to the far plane, so the units you'd use are typically small like 0.00001.

-------------------------

TikariSakari | 2017-01-02 01:05:04 UTC | #5

[quote="cadaver"]Constant depth bias 1 means pushing it all the way to the far plane, so the units you'd use are typically small like 0.00001.[/quote]

Thank you, it seems that using the bias with really small number seems to do the trick. I used negative number for the tiles material to pull it slightly.
[code]<material>
    <technique name="Techniques/NoTextureUnlit.xml" />
    <parameter name="MatDiffColor" value="1 0 0 1" />
<depthbias constant="-0.00002" />
</material>[/code]

-------------------------

