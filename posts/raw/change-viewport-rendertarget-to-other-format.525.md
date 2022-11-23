ucupumar | 2017-01-02 01:01:06 UTC | #1

Hello Urhoheads!  :mrgreen: 
How to change default viewport rendertarget to HDR(rgba16f) format? 

I tried to use this xml snippets.
[code]<replace sel="/renderpath/rendertarget[@name='viewport']/@format">rgba16f</replace>[/code] It's copied from PrepassHDR renderpath, but I changed the name from 'light' to 'viewport'.
Unfortunately, it doesn't work.

Anyone know why?

-------------------------

cadaver | 2017-01-02 01:01:07 UTC | #2

You cannot change the backbuffer format. Instead, you would need to render all scene passes to a high bitdepth intermediate buffer, and finally blit that result to the backbuffer.

Something like this (I don't guarantee that this works)

[code]
<renderpath>
    <rendertarget name="hires" sizedivisor="1 1" format="rgba16f" />
    <command type="clear" color="fog" depth="1.0" stencil="0" output="hires" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" output="hires" />
    <command type="forwardlights" pass="light" output="hires" />
    <command type="scenepass" pass="postopaque" output="hires"/>
    <command type="scenepass" pass="refract" output="hires">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" output="hires" />
    <command type="scenepass" pass="postalpha" sort="backtofront" output="hires" />
    <command type="quad" vs="CopyFrameBuffer" ps="CopyFrameBuffer" output="viewport">
        <texture unit="diffuse" name="hires" />
    </command>
</renderpath>
[/code]

-------------------------

ucupumar | 2017-01-02 01:01:08 UTC | #3

Thanks for the answer! 
But there's two problem using your solution. 

The first one, MSAA won't work. After searching on the internet, I think this was common problem of HDR rendering. I guess I can use postprocess AA.  :unamused: 

The second issue is copyframebuffer won't work in Linux. I don't know why, but it will display just black on Linux. It's okay when I'm on Windows.
I tested using Ubuntu 12.04 with Geforce 460 (blob driver v331).
Do you know about this issue?

-------------------------

cadaver | 2017-01-02 01:01:08 UTC | #4

Can you reproduce the problem on a Windows OpenGL build?

-------------------------

ucupumar | 2017-01-02 01:01:08 UTC | #5

I've tested and this issue didn't happen on Windows OpenGL.
Do you know something about this?

-------------------------

cadaver | 2017-01-02 01:01:08 UTC | #6

It may mean two things: the Linux driver has a bug, or Urho is using the float rendertarget somehow incorrectly, which the Windows driver lets pass, but the Linux driver properly errors out.

-------------------------

ucupumar | 2017-01-02 01:01:09 UTC | #7

I'll do another test and investigate the real problem on my linux box. I just haven't got chance to do it, but I'll eventually try it again maybe tonight.  :unamused:

-------------------------

ucupumar | 2017-01-02 01:01:09 UTC | #8

I found the problem. This is because of common case sensitive problem between OS. Post process refer to CopyFrameBuffer, but the filename is CopyFramebuffer.glsl/hlsl. 
It's okay on Windows, but it's a problem on Linux.

I created simple pull request to fix this problem: [url]https://github.com/urho3d/Urho3D/pull/515[/url]

-------------------------

