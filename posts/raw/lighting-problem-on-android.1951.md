KonstantTom | 2017-01-02 01:11:45 UTC | #1

I don't know this is it bug or not.
[b]1. This is screenshot from my PC.[/b]
[url=http://hostingkartinok.com/show-image.php?id=55f106ce976db4ef6b280b69f873633a][img]http://s8.hostingkartinok.com/uploads/images/2016/04/55f106ce976db4ef6b280b69f873633a.png[/img][/url]
[b]2. This is screenshot from my tablet (Prestigio Multipad 4 Quantum).[/b]
[url=http://hostingkartinok.com/show-image.php?id=135492be305e74519ccc5c402ea913fe][img]http://s8.hostingkartinok.com/uploads/images/2016/04/135492be305e74519ccc5c402ea913fe.png[/img][/url]

But when I run application on Bluestacks, picture is similar to picture on PC build. On my phone picture is similar to picture from tablet.
Anybody know this problem? How I can fix it? Or this is problem of my tablet and my phone?

-------------------------

cadaver | 2017-01-02 01:11:45 UTC | #2

It's pretty much a fact that shadow quality will be worse on OpenGL ES 2.0 (Android, iOS) as the depth texture may have worse precision, and the GPU doesn't do bilinear filtering of the shadow for you, and you cannot get proper multiple cascade shadows for directional lights. In addition shadows are much performance-heavier on OpenGL ES devices, as the GPU's frown upon texture coordinate calculations in the pixel shader.

I'd recommend not relying on dynamic shadows on mobile devices.

-------------------------

KonstantTom | 2017-01-02 01:11:45 UTC | #3

Ok, thanks for reply. As I understand, on other engines (such as unity) I can get a similar problem?
In this scene I use only 1 directional light. Will I bake shadows on 2048x2048 quality? How I can bake shadow in urho3d?

-------------------------

