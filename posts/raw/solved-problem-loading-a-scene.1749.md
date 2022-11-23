Kanfor | 2017-01-02 01:09:51 UTC | #1

Hi, urhofans.

My new problem is when I try to load a scene in .xml. I have a black screen.
I created a camera, with light and a pretty tea pot.

[code]XMLFile* sceneFile = cache->GetResource<XMLFile>("Scenes/MiEscena.xml");
scene_->LoadXML(sceneFile->GetRoot());[/code]

Do I need add something else to the proyect?
Thanks!

-------------------------

thebluefish | 2017-01-02 01:09:51 UTC | #2

You created a Camera, but did you bind it to the Viewport?

[code]
Urho3D::SharedPtr<Urho3D::Viewport> viewport(new Urho3D::Viewport(context_, _scene, camera));
GetSubsystem<Urho3D::Renderer>()->SetViewport(0, viewport);
[/code]

-------------------------

Kanfor | 2017-01-02 01:09:51 UTC | #3

[img]https://trabajoestructuras2010.files.wordpress.com/2010/12/23.jpg[/img]

Thank you!  :smiley:

-------------------------

