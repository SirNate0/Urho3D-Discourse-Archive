umen | 2017-01-02 00:59:01 UTC | #1

Hello all
i modeled  simple model with size y:1000 meter x:1000 meter 
when i load it to the Editor or via code i need to scale it like that : Vector3(100.0f, 1.0f, 100.0f)
so that the model will look right and with the current aspect ratio

[code]Node* planeNode = scene_->CreateChild("Plane");
planeNode->SetScale(Vector3(100.0f, 1.0f, 100.0f));  // Here X and Z scaled 
StaticModel* planeObject = planeNode->CreateComponent<StaticModel>();
planeObject->SetModel(cache->GetResource<Model>("Models/GroundPlane.mdl"));[/code]

what is the logic in Urho3d so i need to scale the model ?

-------------------------

thebluefish | 2017-01-02 00:59:02 UTC | #2

Scale has nothing to do with aspect ratio. Scale is entirely relative to other objects in the scene. I could have a 1x1x1 box, and a 1000x1000x1000 box, and they would look the same depending on where my camera is positioned to them.

It may also be possible that your 3d modelling program is using different units. For example, 3ds max allows a user to specify both system units and display units. If your system units were kilometers and your display units were meters, it would result in a model much too small.

-------------------------

umen | 2017-01-02 00:59:02 UTC | #3

Im using blender and set up meter units

-------------------------

Mike | 2017-01-02 00:59:02 UTC | #4

Did you apply scale in Blender ( are all the scales equal in the scale panel)?

-------------------------

umen | 2017-01-02 00:59:02 UTC | #5

well as i written before , i set scale but i don't understand why i need to scale .
isn't it supposed to load the model as i modeled it and not with distorted scale

-------------------------

thebluefish | 2017-01-02 00:59:02 UTC | #6

How exactly are you loading the model in Urho3D?

If you scale the model itself, that scale only affects the model if you're loading it in a scene. The model itself will be exported with scale 1x1x1. If necessary, try scaling it back down, and scaling all the vertices instead.

-------------------------

umen | 2017-01-02 00:59:03 UTC | #7

Thanks for your answers
i did have scaling in blender and it translate me via the exporter to see it right in the editor

-------------------------

