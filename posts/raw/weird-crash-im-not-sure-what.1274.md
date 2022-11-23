vivienneanthony | 2017-01-02 01:06:32 UTC | #1

Hi

I'm trying to figure out why I'm getting a crash. I think it relates to the render or screen update when switching states. It just started doing it  but I'm not sure if it because it's a opengl problem. A few weeks ago I had to take my video card out my system to use the onboard card.

[imgur.com/a/otDXP](http://imgur.com/a/otDXP)

Vivienne

-------------------------

Lumak | 2017-01-02 01:06:32 UTC | #2

Looks like the call that triggers your crash happens on [b]glTexImage2D()[/b].  Probably the case where the installed video driver is still calling the HW address that doesn't exist anymore. 

You'll need to reconfigure your video driver and get the correct one for the onboard video.

Edit: googled some info on video driver
-to find out which video card that you have installed, type:
 %  lspci | grep VGA

-graphics driver version, type:
  % glxinfo | grep OpenGL

Install the correct video driver:
[url]http://www.nvidia.com/Download/index.aspx?lang=en-us[/url]
[url]http://support.amd.com/en-us/download[/url]
[url]http://www.mesa3d.org/systems.html[/url]

-------------------------

jmiller | 2017-01-02 01:06:42 UTC | #3

According to your log, the crash happens after TextureCube::SetData().

Assuming your 'Skybox.xml' and parameters are correct, there may be a bug?

-------------------------

cadaver | 2017-01-02 01:06:43 UTC | #4

This could be an Urho3D bug (illegal or too small texture data buffer provided for OpenGL), especially if it repeats on another machine with good drivers installed.

However, to debug it we would need the texture/material that causes the crash, and minimal code to reproduce it. I see it's happening related to resource background loading, which is a rarely used feature and therefore it would not be surprising to find errors.

-------------------------

