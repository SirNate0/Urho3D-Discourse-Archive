Enhex | 2017-01-02 01:10:24 UTC | #1

External library for integrating [url=https://github.com/ocornut/imgui]imgui[/url] with [url=https://github.com/urho3d/Urho3D]Urho3D[/url]. No forks to switch to and maintain.

Check the Github page for more info: [github.com/Enhex/Urho3D_imgui](https://github.com/Enhex/Urho3D_imgui)

[img]http://i.imgur.com/LMpD6GO.jpg[/img]

-------------------------

ghidra | 2017-01-02 01:10:25 UTC | #2

This is cool! Show the node graph!

-------------------------

Enhex | 2017-01-02 01:10:25 UTC | #3

[quote="ghidra"]This is cool! Show the node graph![/quote]

Graph example: 
[img]http://i.imgur.com/liQa3JO.png[/img]

-------------------------

weitjong | 2017-01-02 01:10:25 UTC | #4

The node graph thingy is really neat.

-------------------------

thebluefish | 2017-01-02 01:10:25 UTC | #5

Is there a reason you're using GLEW directly? We can use imgui within Urho3D's rendering system directly, thus making it a single port instead of a port for each graphics back-end.

-------------------------

vivienneanthony | 2017-01-02 01:10:25 UTC | #6

[quote="Enhex"][quote="ghidra"]This is cool! Show the node graph![/quote]

Graph example: 
[img]http://i.imgur.com/liQa3JO.png[/img][/quote]

Wow. That's pretty cool. Me need to play with IMGUI more. :slight_smile:

-------------------------

Enhex | 2017-01-02 01:10:25 UTC | #7

[quote="thebluefish"]Is there a reason you're using GLEW directly? We can use imgui within Urho3D's rendering system directly, thus making it a single port instead of a port for each graphics back-end.[/quote]
I tried that first but it doesn't work well. It requires copying the buffers, increasing the vertex coordinates from 2d to 3d, the UI elements come out misaligned, it requires extra shaders, and my attempt was bugged.

Instead I took the renderer that comes with imgui's ogl3 sample. It works flawlessly, no extra overhead, and officially maintained by imgui.
imgui also has d3d 9/11 renderers, but I didn't try to include them.

-------------------------

sabotage3d | 2017-01-02 01:10:26 UTC | #8

Quite cool for node based stuff. Do you know if it supports a spline ramp editing? 
Similar to this one.
[img]https://support.solidangle.com/download/thumbnails/8388821/ramp_float.jpg[/img]

-------------------------

Enhex | 2017-01-02 01:10:26 UTC | #9

[quote="sabotage3d"]Quite cool for node based stuff. Do you know if it supports a spline ramp editing? 
Similar to this one.
[img]https://support.solidangle.com/download/thumbnails/8388821/ramp_float.jpg[/img][/quote]
Someone made an implementation:
[github.com/ocornut/imgui/issues ... -162375868](https://github.com/ocornut/imgui/issues/123#issuecomment-162375868)
[img]https://cloud.githubusercontent.com/assets/153526/11616512/72a94084-9c7d-11e5-8ad5-b71a53bdac01.gif[/img]
Note that imgui's API is abstracted from the integration implementation, so imgui code should work regardless of what it was made for.

You can check out the Gallery section here: [github.com/ocornut/imgui](https://github.com/ocornut/imgui)
And the screenshots thread here: [github.com/ocornut/imgui/issues/123](https://github.com/ocornut/imgui/issues/123)

-------------------------

rasteron | 2017-01-02 01:10:26 UTC | #10

nice!

-------------------------

godan | 2017-01-02 01:12:07 UTC | #11

So, I've managed to create implement Urho's Cmake build system with your excellent Imgui implementation and it now builds happily on OSX. 

However, I'm running in to that problem where the Retina frame buffer size is larger than the screen coords. This results in tiny ui elements: 

[img]https://dl.dropboxusercontent.com/u/69779082/UrhoImguiProblem.png[/img].

This issue was apparently fixed for ImGui's GLFW bindings: [github.com/ocornut/imgui/issues/441](https://github.com/ocornut/imgui/issues/441). And I can verify that it works on my mac. In this Urho_imgui implementation, I tried manually setting the FrameBufferScale to (2,2), but this yield a UI elements that were placed off the screen dimensions. Also, I checked what ImGui thinks the frame buffer size is by default and it comes up as (1,1).

Any ideas on how to fix this?

-------------------------

godan | 2017-01-02 01:12:07 UTC | #12

Also, this implementation won't work with Emscripten - possibly a GLEW issue?

I'd be happy to sure my CMake build system if anyone is interested.

-------------------------

godan | 2017-01-02 01:12:08 UTC | #13

Progress!

So, it looks like on Retina screens, Urho thinks that the screen size is twice the specified resolution, and the frame buffer scale is 1:1. On the other hand, ImGui maintains the original resolution, but has a 2:2 frame buffer scale. I'm not sure what is the better approach.

Nonetheless, for any another OSX imgui-urho users, the fix is set:

[code]
		io.DisplaySize = ImVec2(0.5f * (float)graphics->GetWidth(), 0.5f *(float)graphics->GetHeight());
		io.DisplayFramebufferScale = ImVec2((float)2.0f, (float)2.0f);
[/code]

when compiling to retina devices (or other devices with none 1:1 screen to frame buffer scale).

-------------------------

Enhex | 2017-01-02 01:12:09 UTC | #14

[quote="godan"]Also, this implementation won't work with Emscripten - possibly a GLEW issue?

I'd be happy to sure my CMake build system if anyone is interested.[/quote]
I've used the renderer from IMGUI's OGL3 example, so it makes sense it wouldn't work with Emscripten out of the box.
That renderer is tiny (~120 lines), and Emscripten can use specific versions of openGL (mainly mapping to webGL or ES 2.0 emulation):
[kripken.github.io/emscripten-sit ... pport.html](http://kripken.github.io/emscripten-site/docs/porting/multimedia_and_graphics/OpenGL-support.html)

If you'd like to contribute your CMake support that's be great. Make a pull request on the project's GitHub.

-------------------------

arcanosam | 2017-01-02 01:13:13 UTC | #15

hi!

I'm interesting in use [b]imgui [/b]with [b]Urho3d [/b]thinking in future to use with [b]emscripten [/b]toolchain.

Any tips to I try this integration on on windows (version 8.1 in my job and 10 in my home)? 

Some tutorial or wiki do you recommend?

thanks in advanced.

-------------------------

arcanosam | 2017-01-02 01:13:13 UTC | #16

[quote="Enhex"][quote="godan"]Also, this implementation won't work with Emscripten - possibly a GLEW issue?

I'd be happy to sure my CMake build system if anyone is interested.[/quote]
I've used the renderer from IMGUI's OGL3 example, so it makes sense it wouldn't work with Emscripten out of the box.
That renderer is tiny (~120 lines), and Emscripten can use specific versions of openGL (mainly mapping to webGL or ES 2.0 emulation):
[kripken.github.io/emscripten-sit ... pport.html](http://kripken.github.io/emscripten-site/docs/porting/multimedia_and_graphics/OpenGL-support.html)

If you'd like to contribute your CMake support that's be great. Make a pull request on the project's GitHub.[/quote]

if I adapted this IMGUI's OGL3 example to use SDL, so it's possible that when build with emscripten works outside of the box?

-------------------------

Enhex | 2017-01-02 01:13:13 UTC | #17

[quote="arcanosam"]
if I adapted this IMGUI's OGL3 example to use SDL, so it's possible that when build with emscripten works outside of the box?[/quote]
I don't know because I never tried it. Just try it yourself and see if it works. If it doesn't work you can use Urho's GUI so it isn't that critical.
Keep in ind that imgui is mainly designed as a tools' GUI, so it may lack some features you may want.

-------------------------

arcanosam | 2017-01-02 01:13:14 UTC | #18

thanks.

recommend some cmake for beguinners? (Seems it I will need it...) I don't know nothing about cmake....

-------------------------

godan | 2017-01-02 01:13:14 UTC | #19

Just to add my .02$ - I played around with IMGUI quite a bit and was seriously considering it for a project. In the end, I found it MUCH easier to work with Urho's native UI. I admit, all the XML files and the sprite sheets and the somewhat verbose code is a bit confusing at first. After a while, though, it really pays off - especially if you need to do more than tweak a bunch of sliders.

-------------------------

arcanosam | 2017-01-02 01:13:14 UTC | #20

thanks godan. it's really good to know it. I'm really happy when I see that Urho already has a support to make GUI. 

yesterday when I build with samples for the first time using emscripten toolchain and see in the end the html and asmjs working was awesome!

And I have a prefference to using only the resources of a framework and not give easy to third party

p.s.: sorry for my bad english.

thanks guys

-------------------------

SirNate0 | 2021-01-23 06:06:44 UTC | #21

Sorry to revive the old topic, but I figured out how to get the integration working on Emscripten. The issue proved to be the draw call silently failing because of a lack of GL3 support. Simply not specifying the baseVertexIndex resulted in it working. See below for more info:

https://github.com/Enhex/Urho3D_imgui/issues/3

-------------------------

