umen | 2017-01-02 00:59:01 UTC | #1

i noticed that when i press F5 to save the scene to xml , and then when i load it to the Editor , 
i can't find the camera node .  in the Nodes Hierarchy .
although the view that is presented it is the camera view 
and in the code i do see this comment :
[code]// Create camera and define viewport. We will be doing load / save, so it's convenient to create the camera outside the scene,
    // so that it won't be destroyed and recreated, and we don't have to redefine the viewport on load
    cameraNode_ = new Node(context_);
    Camera* camera = cameraNode_->CreateComponent<Camera>();
    camera->SetFarClip(300.0f);
    GetSubsystem<Renderer>()->SetViewport(0, new Viewport(context_, scene_, camera));[/code]

so if i create it outside the scene how can i test in the editor how the scene will look like in the code ?
Thanks

-------------------------

weitjong | 2017-01-02 00:59:02 UTC | #2

Editor does not care what is inside a scene XML file when it tries to load it. If the scene contains a camera node with a camera component, they will be loaded into the current scene hierarchy in Editor. There is nothing preventing Editor to do that.

Now, whether to put the camera node as part of a scene or not in your app is a matter of your choice. The code from sample app that you quoted below chooses not to for the reason already explained in the code comment. The viewport setup is dependent on the camera component. The viewport would be forced to be setup again each time when the camera component is "recreated" which happens when the camera is part of the scene save/load.

I believe you can actually add any number of cameras in the scene hierarchy after it is being loaded (if it does not have one already). You can position the cameras anywhere you like. When you select the camera in the Hierarchy window, the editor should display what the camera sees in a preview window.

-------------------------

umen | 2017-01-02 00:59:02 UTC | #3

Thanks for your quick answer

-------------------------

