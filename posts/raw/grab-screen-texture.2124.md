szamq | 2017-01-02 01:13:17 UTC | #1

I'm working on OpenVR. The one way communication is done - I can get rotation and position of person wearing the oculus.
Now is time to send the visuals to the hmd. I already have the stereo rendering implemented, but it goes on the screen/ monitor like here [gnometech.com/torque/images/ ... dering.jpg](http://www.gnometech.com/torque/images/blog-2013-04-11/2013-04-11-StereoRendering.jpg)
What I wold like to do is to copy the screen as a texture, so I could send it to the vr googles.

I tried to do it like that. But it is upside down and It stops to render on screen

            renderTexture = Texture2D();
            renderTexture.SetSize(1920, 1080, GetRGBFormat(), TEXTURE_RENDERTARGET);
            renderTexture.filterMode = FILTER_BILINEAR;

            RenderSurface@ surface = renderTexture.renderSurface;
	    surface.updateMode=SURFACE_UPDATEALWAYS;
            surface.viewports[0] = renderer.viewports[0];
	    surface.viewports[1] = renderer.viewports[1];

Is there a better way to grab, what's on screen and have that as a texture(that is accesible by glBindTexture..)?
edit:
Ok just noticed that the upside down view of the texture is not caused by urho but by OpenVR, I'm wondering why

-------------------------

cadaver | 2017-01-02 01:13:17 UTC | #2

We intentionally render to textures flipped on OpenGL so that the UV addressing is same as in resource textures & D3D rendertargets. If you want to change that you need special case engine code to not flip for VR.

I'm not sure of the performance you will get if capturing the backbuffer vs. rendering directly to a texture, but take a look here [opengl.org/discussion_board ... -a-texture](https://www.opengl.org/discussion_boards/showthread.php/171930-How-to-copy-backbuffer-contents-into-a-texture) . This needs you to implement that in C++ code, existing functionality for this isn't there now.

-------------------------

