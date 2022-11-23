JulyForToday | 2017-01-02 01:06:00 UTC | #1

So I've been making a program the last couple days using the UrhoPlayer and writing the code in angelscript. I wanted to test it on another machine (also a windows PC), and ran [url=https://github.com/urho3d/Urho3D/issues/738]into an issue with d3dcompiler_47.dll[/url]. So I figured I would recompile the UrhoPlayer to use OpenGL (using [b]-DURHO3D_OPENGL[/b] build option). It compiles fine, but when I use the sample scripts with the UrhoPlayer (which all work fine with the DX build) they are completely broken. They start, but the materials are orange/green gradients and the scene is barely constructed, and in odd ways (how depends on the sample, but none of them are created correctly/as expected)

Here is the physics sample, DX on the left (normal scene), OpenGL on the right (blank white screen with a gradient on a quad)
[img]http://i.imgur.com/sR1FKHL.png[/img] [img]http://i.imgur.com/5f3QL64.png[/img]

Not sure what's going on with this.

-------------------------

JulyForToday | 2017-01-02 01:06:00 UTC | #2

Okay.. nevermind.

I'm still not sure what was going on, but I was building Urho from source I pulled from github back in May (5/27 I think). I decided to start from scratch, and download the latest Urho zip file (1.4) and do an OpenGL build from that, and use the samples/assets included with it. And it works exactly as I'd expect, and works on both machines (my original goal).

-------------------------

1vanK | 2017-01-02 01:06:00 UTC | #3

I had the same problem when I used folders Data and CoreData from the old version Urho3D with new sources

-------------------------

weitjong | 2017-01-02 01:06:00 UTC | #4

If you look at the change history or the release notes for 1.4 then this is not surprising.
[quote]Direct3D11 and OpenGL 3 rendering. Shader Model 2 support removed.[/quote]
I remember seeing Lasse making a lot of changes to those shaders in the CoreData directory.

-------------------------

