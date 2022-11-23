SteveU3D | 2017-02-21 09:44:39 UTC | #1

Hi,
I can play a live video from a camera in a texture of a plane object. But I would like to have that on the viewport's background (like a skybox for example but only the "front face"). I found some posts in which it's suggested to change the renderpath in xml file to have a static texture as background but it cannot be applied to the video case as the texture is dynamic.

So how can I put that video texture in the background?

Thanks.

-------------------------

1vanK | 2017-02-21 14:10:02 UTC | #2

2 viewports one above the other:
first - plane with video
second - scene with tranparent backgound (diable clear)

-------------------------

SteveU3D | 2017-02-21 15:05:00 UTC | #3

Thanks,
Meanwhile, I found the following post which corresponds to what you suggest :
http://discourse.urho3d.io/t/how-to-layer-scenes/740/4
It works but the "problem" is that the objects in scene2 could go behind the video plane.
I think that I just have to put the farClip of the viewport with video greater than the farClip of the viewport with objects, and put my video plane between those two farClip values.
Does that seem ok?

-------------------------

1vanK | 2017-02-21 20:08:54 UTC | #4

just clear depth (but not clear color) in renderpath of layer 2

-------------------------

SteveU3D | 2017-02-22 09:20:29 UTC | #5

It doesn't work or I may do it the wrong way.
Here is what I do : 

    scene_=new Scene(context_); //scene for objects
    scene2_=new Scene(context_); //scene for video plane in background
    ...
    cameraNode_=scene_->CreateChild("Camera"); //camera for objects
    Camera* camera=cameraNode_->CreateComponent<Camera>();

    cameraNode2_=scene_->CreateChild("Camera"); //camera for video plane
    Camera* camera2=cameraNode2_->CreateComponent<Camera>();
    ...
    //create objects in each scene
    //video screen in scene2_ for the background
    Node* screenNode = cameraNode2_->CreateChild("Screen");
    screenNode->SetPosition(Vector3(0.0f, 0.f, 20.f));
    screenNode->SetRotation(Quaternion(-90.0f, 0.0f, 0.0f));
    screenNode->SetScale(Vector3(20.0f, 0.0f, 15.0f));
    StaticModel* screenObject = screenNode->CreateComponent<StaticModel>();
    screenObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));

    //a teapot in scene_ with my objects
    //Teapot
    teapotNode_=scene_->CreateChild("TeaPot");
    teapotNode_->SetPosition(Vector3(0,2,25.f)); //I put it on Z=25, it's not an error
    teapotNode_->SetScale(Vector3(5,5,5));
    StaticModel* teapotObject=teapotNode_->CreateComponent<StaticModel>();
    teapotObject->SetModel(cache->GetResource<Model>("Models/Teapot.mdl"));
    teapotObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
    teapotObject->SetCastShadows(true);
    
    Renderer* renderer=GetSubsystem<Renderer>();

    //the viewports
    //viewport for objects in scene_
    mViewport = new Viewport(context_,scene_,cameraNode_->GetComponent<Camera>());
    SharedPtr<Viewport> viewport(mViewport);

    //viewport with video plane in background
    mViewport2 = new Viewport(context_,scene2_,cameraOrthoNode_->GetComponent<Camera>());
    SharedPtr<Viewport> viewport2(mViewport2);

    //renderpath that I have to change for scene_ with objects?
    SharedPtr<RenderPath> renderPathViewport = SharedPtr<RenderPath>(new RenderPath());
    renderPathViewport->Load(cache->GetResource<XMLFile>("RenderPaths/ForwardNoDepth.xml"));
    mViewport->SetRenderPath(renderPathViewport2);

    renderer->SetNumViewports(2);
    renderer->SetViewport(0,viewport2); //with video plane in background
    renderer->SetViewport(1,viewport); //with objects ahead of video plane

ForwardNoDepth.xml : 

    <renderpath>
        <command type="clear" color="fog" depth="1.0" stencil="0" />
       <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
       <command type="forwardlights" pass="light" />
       <command type="scenepass" pass="postopaque" />
       <command type="scenepass" pass="refract">
           <texture unit="environment" name="viewport" />
       </command>
       <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
       <command type="scenepass" pass="postalpha" sort="backtofront" />
    </renderpath> 

So, like that, the teapot on Z=25 isn't visible as it is behind the video plane on Z=20.
If I do what you suggest, if I understood well, in ForwardNoDepth.xml, I have to write : 

    <command type="clear" depth="1.0" stencil="0" /> //without color field

But the teapot doesn't appear and is still behind the video plane.

-------------------------

1vanK | 2017-02-22 10:51:32 UTC | #6

```
cameraNode_=scene_->CreateChild("Camera"); //camera for objects
cameraNode2_=scene_->CreateChild("Camera"); //camera for video plane
```
both nodes in first scene, so when you Node* screenNode = cameraNode2_->CreateChild("Screen");
video plane also in first scene

-------------------------

