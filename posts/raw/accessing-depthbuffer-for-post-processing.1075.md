franck22000 | 2017-01-02 01:05:16 UTC | #1

Hello i currently have an issue.

I am trying to access to the depth buffer in a post-process shader (DirectX11 mode). like so: 

[code]float depth = Sample2D(DepthBuffer, iScreenPos).x;[/code]

But as you can see on my video there is a "bleeding" issue. My 3D scene is composed of a terrain with billboards on it and my camera is above the terrain in the video.

[video]https://www.youtube.com/watch?v=XLj1kDrTIcM[/video]

Here is the code i am using to display the depth buffer in the video.

[code]float depth = Sample2D(DepthBuffer, iScreenPos).x;
oColor = float4(depth, depth, depth, 1.0);[/code]

Thank you for your help !

-------------------------

franck22000 | 2017-01-02 01:05:16 UTC | #2

I have fixed my issue by putting: 

[code]<command type="clear" color="1 1 1 1" output="depth" />[/code]

After

[code]<command type="clear" color="fog" depth="1.0" stencil="0" />[/code]

In the "Deferred.xml" RenderPath

Fixed :slight_smile:

-------------------------

