TikariSakari | 2017-01-02 01:03:28 UTC | #1

Hello, I am using angel script the chapter 06, and modified it to use my own custom model with animation. For some reason the model gets distorted when using modelnode.position. I defined the models position like this:

[code]

    const uint UNITS_IN_ROW = 31;
    const uint UNITS_IN_COL = 31;
    const uint NUM_MODELS = UNITS_IN_COL * UNITS_IN_ROW;
    for (uint i = 0; i < NUM_MODELS; ++i)
    {
        Node@ modelNode = scene_.CreateChild("Jack" + NUM_MODELS);
        modelNode.position = (Vector3( 3 * ((NUM_MODELS - i - 1) / UNITS_IN_ROW) , 0.0f, 3 * ((NUM_MODELS - 1 - i)%UNITS_IN_ROW) ) );

[/code]

I tested if changing the order from adding last one first would make a difference, but it seems to be positional related thing, but it seems to be more positional thing. I am using blender 2.73, and fbx 7.4 exporter. When the position is 0,0, everything looks ok, but when I set the position for example (150,150) it is quite distorted. I feel like this is something to do with same as when trying to apply armature scaling in blender, my mesh might become completely distorted, and the armatures local coorinate is not 0,0 after the set position. I tried to add an empty in blender and make it a parent, but it doesn't seem to help in urho3d.

Here is a picture of the bear at 0,0
[img]http://i.imgur.com/sayoqMR.png[/img]

And here at (31*3, 31*3)
[img]http://i.imgur.com/20eR03J.png[/img]

The number on the screen is fps.

Any idea what could be the cause for this?

-------------------------

jmiller | 2017-01-02 01:03:28 UTC | #2

When models move but some vertices stay at origin, it can be a bone/weights problem.

You might try the Blender-Urho plugin, which exports directly to Urho .mdl
[github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender)

-------------------------

TikariSakari | 2017-01-02 01:03:28 UTC | #3

[quote="carnalis"]When models move but some vertices stay at origin, it can be a bone/weights problem.

You might try the Blender-Urho plugin, which exports directly to Urho .mdl
[github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender)[/quote]

Ty carnalis, I got it fixed. I used some of those normalize all vertex/set number of weights per vertex, etc. buttons. After clicking them randomly and then trying to export again it did seem to come out perfectly. Also I tried the blender to urho plugin, and it did seem to create smaller model-file, than blender->fbx->urho, so I guess that is the preferred way to go. Also I tried to go with the fbx route, and it also seems to work perfectly now.

-------------------------

