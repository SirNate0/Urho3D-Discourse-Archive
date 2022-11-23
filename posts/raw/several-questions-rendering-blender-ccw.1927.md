vivienneanthony | 2017-01-02 01:11:36 UTC | #1

Hello,

I ran into several issues trying to get good FPS on a game client. There was numerous issues with shadowmaps and questions about culling. I'm going shoot some questions maybe someone has some input.

1) Does anyone have experience with Blender? Natively I don't think it outputs optimized models for CCW or CW but general vertices. Do anyone know how to get exported models in CCW form so it's easier on Urho3D?

2) OpenGL have additional Culling parameters. Have anyone used it before?

3) Turning off rendering of unseen models decreasing vertices counts. Do anyone know how to turn off rendering of unseen models from the camera? Also disabling rendering of unseen models.

For a example, a wall has 10 objects behind it but the camera can't see it. So, making Urho3D account for vertices in front of the wall but not behind.

Sorry about the loaded questions. If you are wondering why I am asking.

[youtube.com/watch?v=PvcaAQnSUAw](https://www.youtube.com/watch?v=PvcaAQnSUAw)

[youtube.com/watch?v=895t1mzVGS4](https://www.youtube.com/watch?v=895t1mzVGS4)
[youtube.com/watch?v=VlugiYVOZxQ](https://www.youtube.com/watch?v=VlugiYVOZxQ) (Originally low but after much optimization we are doing about 194 fps on my computer, and his a bit above 60)
[youtube.com/watch?v=r4gcA_GKlQw](https://www.youtube.com/watch?v=r4gcA_GKlQw)


Vivienne

-------------------------

rasteron | 2017-01-02 01:11:36 UTC | #2

For the Blender part #1, I have not tested the exporter completely, but it works great so far when creating meshes with lightmaps. You can always try the included AssetImporter. I would suggest using the command line so you could toggle and experiment with some options.

-------------------------

Bananaft | 2017-01-02 01:11:36 UTC | #3

[quote="vivienneanthony"]1) Does anyone have experience with Blender? Natively I don't think it outputs optimized models for CCW or CW but general vertices. Do anyone know how to get exported models in CCW form so it's easier on Urho3D?
[/quote]
You are refering to face normals and backface cullung? Triangles is always either CCW or CW, and if I recall correctly in blender they are always CounterClockWise by default, but that may change during exporting. You can choose which side of a face to cull in Urho material settings.

[quote="vivienneanthony"] Turning off rendering of unseen models[/quote]

There are two techniques for that:

1) Frustum culling. Will hide all models, which bounding box is not toching camera frustrum. Works by default.

2) Occlusion culling. Will hide all models, that are behind special occluders. It works like this: You create a very low poly proxy geometry of your level, set it as an occluder, then the engine will render it's low resolution depth buffer on CPU before each frame, then it will use it to cull unseen models.

If you have a huge meshes, you should cut them to smaller chunks. Having a lot of lights with dynamic shadows is fine as long as they are culled, and not rendered simutaniously.

Also, what lighting technique you are using?

-------------------------

