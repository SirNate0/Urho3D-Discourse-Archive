valera_rozuvan | 2017-01-02 01:09:38 UTC | #1

Hi all!

Recently I stumbled upon an interesting YouTube demo of an Urho3D program. Here it is:

[video]https://www.youtube.com/watch?v=yNIsJa_RqB8[/video]

I have followed the author's link to the source code of the demo, and tried compiling it. It turned out that the demo is about a year old, and it uses a previous version of Urho3D. From the start, it refused to compile. But after tinkering with it for a bit, I managed to compile it, and get a runnable executable. But the result was not what I expected:

[img]https://raw.githubusercontent.com/valera-rozuvan/stuff/master/images/strange-urho3d-behavior_x640.png[/img]

Here's the code that I have got so far: [github.com/valera-rozuvan/UrhoB ... urho3d_1_5](https://github.com/valera-rozuvan/UrhoBotTest/tree/migrate_to_urho3d_1_5)

While the code compiles, and I can execute it, there are several errors/warnings in the console: [pastebin.com/3DX8ckjX](http://pastebin.com/3DX8ckjX)

Some things from that console log:

[ul]
[li]warning C7555: 'attribute' is deprecated, use 'in/out' instead[/li]
[li]error C7616: global variable gl_ClipVertex is removed after version 140[/li]
[li]warning C7555: 'varying' is deprecated, use 'in/out' instead[/li]
[li]ERROR: Failed to compile vertex shader Shadow(SKINNED):[/li]
[li]ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT INSTANCED NORMALMAP PERPIXEL SHADOW):[/li]
[li]ERROR: Failed to compile pixel shader LitSolid(AMBIENT DIFFMAP DIRLIGHT NORMALMAP PERPIXEL SHADOW SPECMAP SPECULAR):[/li]
[li]error C7616: global function shadow2DProj is removed after version 140[/li]
[li]warning C7533: global variable gl_FragColor is deprecated after version 120[/li]
[li]ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT NORMALMAP PERPIXEL SHADOW):[/li]
[li]... (see full listing of console output for more)[/li][/ul]

I am sure that eventually I will fix all of these errors, but maybe someone can help me? Pull requests against branch [b]migrate_to_urho3d_1_5[/b] [url]https://github.com/valera-rozuvan/UrhoBotTest/tree/migrate_to_urho3d_1_5[/url] are very welcome! = )

-------------------------

boberfly | 2017-01-02 01:09:38 UTC | #2

Hi valera_rozuvan,

Urho3D 1.5 had a big change under the hood for rendering on GL3 (and the option for DX11). For a quick fix, replace bin/CoreData with the one found in 1.5, notably the shader code has changed quite a bit to accommodate these APIs with preprocessor defines.

The higher-level technique/material code shouldn't need any tweaks, hopefully.

-------------------------

valera_rozuvan | 2017-01-02 01:09:38 UTC | #3

[quote="boberfly"]For a quick fix, replace bin/CoreData with the one found in 1.5[/quote]

Did that. Still something weird going on:

[img]https://raw.githubusercontent.com/valera-rozuvan/stuff/master/images/strange-urho3d-behavior-2_x640.png[/img]

Pushed updated code to [b]migrate_to_urho3d_1_5[/b] branch at  [github.com/valera-rozuvan/UrhoB ... urho3d_1_5](https://github.com/valera-rozuvan/UrhoBotTest/tree/migrate_to_urho3d_1_5) .

The console output is basically the same: [pastebin.com/hpaxUSsJ](http://pastebin.com/hpaxUSsJ)

Help me = )

-------------------------

valera_rozuvan | 2017-01-02 01:09:38 UTC | #4

I believe that I have found the original author of this Urho3D example. It's [b]codingmonkey[/b] = )

-------------------------

valera_rozuvan | 2017-01-02 01:09:38 UTC | #5

It turns out I messed while updating/replacing the Data/* and CoreData/* files. Will update the GitHub repository soon. In the meantime, a quick video demonstrating the project [b]MonkeyFirst/UrhoBotTest[/b] running in Urho3D v1.5:

[video]https://www.youtube.com/watch?v=_hgL3sfR-yc[/video]

-------------------------

