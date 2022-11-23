TikariSakari | 2017-01-02 01:03:40 UTC | #1

I noticed that when I import the scene from dae file to urho, the lights seem to point exactly the wrong way. When I opened the xml-file in the editor view, it adds Light which has rotation of 180 degrees on Y-axis. When I turn it to 0, the light points the same way as in blender. I was mostly wondering if this will remain same way in the future, so that I should do the change in blender/exporting dae to urho, or might this be changed in urhos scene loader?

Edit: I guess easiest temp fix would be just to search all the lightnodes from the scene and change their rotation to 0.

-------------------------

thebluefish | 2017-01-02 01:03:40 UTC | #2

AFAIK there is no set roadmap, so who knows what each dev is working on. Urho3D is based on support from contributors, such as yourself, providing this kind of information. If possible, please submit a [bug report]([github.com/urho3d/Urho3D/issues](https://github.com/urho3d/Urho3D/issues)) to ensure that this issue gets the attention it needs.

-------------------------

TikariSakari | 2017-01-02 01:03:40 UTC | #3

hmm I think its something with the collada to blender thing. Seems that the rotation attribute is always same regardless what direction the light is pointing. The node the light is attached to, seems to point correct way though.

-------------------------

gwald | 2017-01-02 01:03:41 UTC | #4

I thought collada was outdated, and a legacy format?
Why not just use the .blend file?

-------------------------

cadaver | 2017-01-02 01:03:41 UTC | #5

Unfortunately Assimp's Blender loading code is in worse shape than its Collada loading code, at least what it comes to lights. This specific issue regarding the direction was fixed (by modifying the Assimp copy in Urho's repo); I used a test scene with a couple of boxes and a spot light and the results were following:

- Collada: light type & direction imported correctly (after the fixes)
- Blender: Assimp misinterprets the light as a point light
- FBX: Assimp gets the light direction and range wrong

-------------------------

TikariSakari | 2017-01-02 01:03:41 UTC | #6

Thanks for the quick fix, now the collada seems to be working perfectly for importing scenes.

As for the why I use collada, I tried using the blender exporter and but I liked more the structure of the xml that the collada to urho has. In the xml, I actually can see the position and rotation of each object in the scene, unlike if I used the blender exporter inside blender. It just poofs that data completely from the xml-file. It might actually have that data in the mdl-files but I prefer having structure where the node and model location is set on the scene. Also for lights, there is no positional information at all where the lights are set.

-------------------------

