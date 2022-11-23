JulyForToday | 2017-01-02 01:05:57 UTC | #1

I know this is pretty basic, but I can't seem to figure out how to get it working. I created a simple room mesh in blender with different materials (each having it's own texture) for the walls, floor, and ceiling. I'm using the [url=https://github.com/reattiva/Urho3D-Blender]Urho3D-Blender Exporter[/url] to export and generate an .mdl for the room's mesh, and it generates materials and textures for the room.

If I only use one I can get the material/texture to work. If I use more than one, only material is visible (the ceiling) and the rest of the mesh is the blank default material. Not sure what I'm doing wrong. Or if I'm making an incorrect assumption in thinking a single .mdl can have multiple materials.

-------------------------

JulyForToday | 2017-01-02 01:05:57 UTC | #2

Ah, I attempted to do as you asked, and I found the problem: the attribute inspector was too small, and only the first material was visible. I didn't realize there was a scrollbar and there would be a list of settable materials for each part of the mesh. I knew it had to be some simple thing I was missing. Thanks :slight_smile:

-------------------------

