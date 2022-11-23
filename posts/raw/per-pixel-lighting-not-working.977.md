thebluefish | 2017-01-02 01:04:34 UTC | #1

Hey all,

I've recently noticed an issue with lights. With forward/deferred rendering, lights don't seem to work unless I specify Per-Vertex lighting (Directional lights apparently don't use per-pixel anyways?). I noticed this when I implemented scorvi's editor, although I'm sure there must be something I'm doing wrong.

-------------------------

cadaver | 2017-01-02 01:04:34 UTC | #2

It appears that at least spotlights are currently broken on GL3 + Intel. NVidia is OK. As a temporary workaround until fixed, you should be able to force OpenGL2 using the -gl2 switch.

-------------------------

thebluefish | 2017-01-02 01:04:34 UTC | #3

I'm experiencing this problem in DX9 currently. I can't test DX11, or OpenGL currently because of a bug. Both spotlights and point lights don't work unless I set Per-Vertex lighting. Directional lights do make a difference with per-vertex. Here's a GIF showing the behavior:

[url=http://i.imgur.com/zvU4n9A.gif][img]http://i.imgur.com/zvU4n9Am.gif[/img][/url]

-------------------------

cadaver | 2017-01-02 01:04:34 UTC | #4

Check that you don't have stale .pak files around, and also try clearing the shader cache directory Bin/CoreData/Shaders/HLSL/Cache. Otherwise D3D9 rendering should be pretty much foolproof on any semi-modern GPU.

-------------------------

thebluefish | 2017-01-02 01:04:34 UTC | #5

Interesting... I copied the CoreData from an older build of Urho3D (17/3/2015), and built my application against it, and lighting works. I then copied the CoreData from my most current build (3/4/2015), and built against it, and lighting is still broken. I then pulled the latest branch of Urho3D (Downloaded ZIP from Github), built it, copied the CoreData folder, and built my application against it. Suddenly now it's working. There weren't any errors in the log either.

That was weird.

-------------------------

cadaver | 2017-01-02 01:04:34 UTC | #6

During the work with the render-refactor branch there were simultaneous changes in the rendering code and shaders, including D3D9, that require the build & data directory to match. So you probably had a mismatch or a bad revision.

-------------------------

