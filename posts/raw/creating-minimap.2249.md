slapin | 2017-01-02 01:14:15 UTC | #1

Hi, all!

I want to create minimap for my city so a character can move and in small map it is possible to see
the neighborhood.
I do this:
[code]
    Node@ minimap_cam_node = Node();
    Camera@ minimap_camera = minimap_cam_node.CreateComponent("Camera");
    minimap_camera.farClip = 600.0f;
    minimap_camera.orthographic = true;
    minimap_camera.zoom = 0.3;
    minimap_cam_node.position = Vector3(0.0, 500.0f, 0.0);
    minimap_cam_node.LookAt(Vector3(0.0, 0.0, 0.0));
[/code]

And update when character moves like this:
[code]
minimap_cam_node.position = Vector3(headNode.worldPosition.x, minimap_cam_node.position.y, headNode.worldPosition.z);
[/code]

Also I have my normal camera and Zone set up like this:
[code]
Node@ cam_node = Node();
Camera@ camera = cam_node.CreateComponent("Camera");
camera.farClip = 300.0f;
renderer.numViewports = 2;
renderer.viewports[0] = Viewport(sc, camera);
renderer.viewports[1] = Viewport(sc, minimap_camera, IntRect(graphics.width * 2 / 3, 32, graphics.width - 32, graphics.height / 3));

Node@ zoneNode = sc.CreateChild("Zone");
Zone@ zone = zoneNode.CreateComponent("Zone");
zone.boundingBox = BoundingBox(Vector3(-1000.0f,-10000.0, -1000.0f), Vector3(1000, 499, 1000));
zone.ambientColor = Color(0.15f, 0.15f, 0.15f);
zone.fogColor = Color(0.5f, 0.5f, 0.7f);
zone.fogStart = 100.0f;
 zone.fogEnd = 300.0f;
[/code]

The problem:
[b]The minimap camera is affected by Zone fog setting[/b] How can I avoid camera view being clipped by for for minimap,
but still have proper fog on main camera? Maybe there is more interesting approach to make realtime minimap?
How can I limit rendering quality and frame rate on minimap to make it consume less resources?

Thanks a lot!

-------------------------

jmiller | 2017-01-02 01:14:15 UTC | #2

re-suggesting things, but may help others hitting this thread...

One way is to create a different renderpath (like based on CoreData/RenderPaths/Forward.xml) to give the minimap viewport.
You can clear="r g b a" instead of clear="fog".
[urho3d.github.io/documentation/ ... paths.html](https://urho3d.github.io/documentation/HEAD/_render_paths.html)
A rendertarget sizedivisor="4 4" would give you 1/4 resolution.

For limiting updates of a texture rendertarget, assign a tag to your commands and you can enable/disable them when you want.
checking interval: [github.com/carnalis/ProcSky/blo ... ky.cc#L222](https://github.com/carnalis/ProcSky/blob/master/ProcSky.cc#L222)
queue render: [github.com/carnalis/ProcSky/blo ... ky.cc#L288](https://github.com/carnalis/ProcSky/blob/master/ProcSky.cc#L288)
unqueue: [github.com/carnalis/ProcSky/blo ... ky.cc#L297](https://github.com/carnalis/ProcSky/blob/master/ProcSky.cc#L297)

Another relevant thread, [topic756-10.html](http://discourse.urho3d.io/t/how-to-layer-scenes/740/1)

Maybe someone can correct/expand or offer other ideas?

-------------------------

