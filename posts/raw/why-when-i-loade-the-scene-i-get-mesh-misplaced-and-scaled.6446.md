mohamed.chit | 2020-10-20 18:23:41 UTC | #1

I have a scene exported from Blender as fbx file.

I use the tool AssetImport and I get an XML scene.

I loaded in the test application, I get really strange results, I thought there is an error in fbx file, or in blender, to my surprise when I loaded the scene in Urho3D Editor, everything look normal.

What I do in the test application, I just load the scene and use standard rendering path "Forward.xml", which come with Urho3d, here is what I do:


    Urho3D::SharedPtr<Urho3D::ResourceCache> ps_cache(pr_application->GetSubsystem<Urho3D::ResourceCache>());

    Urho3D::SharedPtr<Urho3D::Renderer> ps_renderer(pr_application->GetSubsystem<Urho3D::Renderer>());


    ps_cache->AddResourceDir("urho/simple_objects");

    pr_scene->CreateComponent<Urho3D::Octree>();
    pr_scene->CreateComponent<Urho3D::DebugRenderer>();

    auto ps_scene_file = ps_cache->GetFile("simple_objects.xml");

    if(pr_scene->LoadXML( *ps_scene_file ) == false ) {
        throw std::runtime_error("could not load the scene");
    }

    auto pr_context = pr_application->GetContext( );

    // camera settings
    Urho3D::SharedPtr<Urho3D::Node> camera_node( pr_scene->GetChild("Camera", true) );
    if( camera_node == nullptr ) {
        camera_node = pr_scene->CreateChild("Camera");
    }


    Urho3D::Camera* pr_camera = camera_node->CreateComponent<Urho3D::Camera>( );

    Urho3D::SharedPtr<Urho3D::Viewport> viewport(new Urho3D::Viewport(
                                                                pr_context, 
                                                                pr_scene, 
                                                                pr_camera));


    auto ps_render_path_file = ps_cache->GetResource<Urho3D::XMLFile>("RenderPaths/Forward.xml");

    Urho3D::SharedPtr<Urho3D::RenderPath> render_path ( new Urho3D::RenderPath( ) );

    render_path->Load( ps_render_path_file );

    viewport->SetRenderPath( render_path );

    ps_renderer->SetViewport(0, viewport);

-------------------------

SirNate0 | 2020-10-20 15:01:33 UTC | #2

Could you share the scene file? My guess is it's something with that, though I'm very unsure about it.

-------------------------

Modanung | 2020-10-20 21:38:53 UTC | #3

A screenshot showing the maltransformation may also shed some light.

-------------------------

mohamed.chit | 2020-10-21 01:35:48 UTC | #4

i did post some screenshot already, I found how to solve the problem, I do not fully understand how the probem really happens, but i can say, there are CoreData folder in the scene, and another Core Data folder at the root, when i made a single CoreData, it worked correctly.

I am kind of person  that i do not like to put everything in one place, but it seems it is the save way to do so in Urho3D

-------------------------

SirNate0 | 2020-10-21 01:40:38 UTC | #5

[quote="mohamed.chit, post:4, topic:6446"]
there are CoreData folder in the scene, and another Core Data folder at the root
[/quote]

Can you explain what you mean by this? My guess is you had something like
```
Data/MyScene/CoreData
CoreData/
```
I would expect this to fail, as the engine looks for the folders to add to the resources cache to look for resources, but I don't think it looks for more than one (once it finds a matching CoreData, it stops looking for others). But you could add the other folders you want manually.

-------------------------

