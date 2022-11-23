godan | 2017-01-02 01:12:20 UTC | #1

Can Emscripten (or WebGL) handle the new PBR shaders? I've trying to get something set up, but I'm getting nothing.

I've a got a working scene running in Chrome that renders some spheres with a basic grey material. When I switch this material to a PBR one, the objects are not visible (although the do get created and added to the scene). Also, this exact code with the PBR materials renders beautifully on desktop builds.

I've also noticed that you can't add a TextureCube to a Zone component when compiling for the web.

-------------------------

Bananaft | 2017-01-02 01:12:23 UTC | #2

[i]WebGL is based on the OpenGL ES 2.0 specification[/i], so it's much closer to what you get on mobile.

[khronos.org/webgl/wiki/WebG ... ifferences](https://www.khronos.org/webgl/wiki/WebGL_and_OpenGL_Differences)

-------------------------

godan | 2017-01-02 01:12:23 UTC | #3

Thanks for the link, I'll dig in to it.

However, before I do, does anyone know if the differences between WebGL and OpenGL affect the PBR shaders? Has anyone managed to get PBR working with a web build?

-------------------------

