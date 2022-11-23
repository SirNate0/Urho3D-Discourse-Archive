1vanK | 2017-01-02 01:15:41 UTC | #1

In c++ I have class
[code]
class URHO3D_API CameraControllerFlowNode : public FlowNode
{
    URHO3D_OBJECT(CameraControllerFlowNode, FlowNode);

public:
    CameraControllerFlowNode(Context* context);
    void Update(float timeStep);

    enum InputPort
    {
        IN_CAMERA_NODE = 0,
        IN_MOUSE_SENSITIVITY = 1
    };
    ...
};
[/code]

What better way to export it enum to angelScript? Do I have to use constants instead?

[code]
class URHO3D_API CameraControllerFlowNode : public FlowNode
{
    URHO3D_OBJECT(CameraControllerFlowNode, FlowNode);

public:
    CameraControllerFlowNode(Context* context);
    void Update(float timeStep);

    static const int IN_CAMERA_NODE = 0;
    static const int IN_MOUSE_SENSITIVITY = 1;
    ...
};
[/code]

-------------------------

cadaver | 2017-01-02 01:15:41 UTC | #2

It's possible AS doesn't support enums inside classes yet, though the author has already talked about it long ago. Most trouble-free option would probably be to just define an enum outside the class, and expose normally.

-------------------------

1vanK | 2017-01-02 01:15:41 UTC | #3

There may be a lot of different types of flounodes (hunderts), so in global namespace it will be a lot of excess

-------------------------

1vanK | 2017-01-02 01:15:41 UTC | #4

Is also impossible to register consts in class for AS?

[code]engine->RegisterObjectProperty("CameraControllerFlowNode", "const int IN_CAMERA_NODE", offsetof(CameraControllerFlowNode, IN_CAMERA_NODE));
[/code]

gives me error :(

-------------------------

cadaver | 2017-01-02 01:15:41 UTC | #5

Offsetof is for normal instance variables within the object's memory block, consts aren't part of that.

-------------------------

1vanK | 2017-01-02 01:15:41 UTC | #6

Mey be is easy way for register some readonly property which just return some digit (I mean without make functions like Return0(), Return1())

-------------------------

slapin | 2017-01-02 01:15:43 UTC | #7

I'd suggest using one of dictionary types.

-------------------------

1vanK | 2017-01-02 01:15:46 UTC | #8

Ok, I found a solution

[github.com/urho3d/Urho3D/issues/1730](https://github.com/urho3d/Urho3D/issues/1730)

-------------------------

slapin | 2017-01-02 01:15:46 UTC | #9

Hi!
Sorry for stupid question - could you please
tell what changed as the result, i.e. what
can be done now what was not possible to do?

-------------------------

1vanK | 2017-01-02 01:15:47 UTC | #10

[code]    RegisterCustomFlowNode<CameraControllerFlowNode>(engine, "CameraControllerFlowNode");
    engine->SetDefaultNamespace("CameraControllerFlowNode");
    engine->RegisterEnum("InputPort");
    engine->RegisterEnumValue("InputPort", "IN_CAMERA_NODE", CameraControllerFlowNode::IN_CAMERA_NODE);
    engine->RegisterEnumValue("InputPort", "IN_MOUSE_SENSITIVITY", CameraControllerFlowNode::IN_MOUSE_SENSITIVITY);
    engine->SetDefaultNamespace("");
[/code]

allows write CameraControllerFlowNode::IN_CAMERA_NODE and CameraControllerFlowNode::IN_MOUSE_SENSITIVITY in AngelScript (enum moved from global name space to class namespace)

-------------------------

slapin | 2017-01-02 01:15:47 UTC | #11

Is it possible to register such values directly in AngelScript or not?

-------------------------

1vanK | 2017-01-02 01:15:47 UTC | #12

[quote="slapin"]Is it possible to register such values directly in AngelScript or not?[/quote]

Yes, [angelcode.com/angelscript/sd ... d2a861af18](http://www.angelcode.com/angelscript/sdk/docs/manual/classas_i_script_engine.html#a4d331153596dd39838f3bed2a861af18)

But for register simple consts (not enums) I not found way (it required pointer)
[angelcode.com/angelscript/sd ... 4812013169](http://www.angelcode.com/angelscript/sdk/docs/manual/classas_i_script_engine.html#aacd32f32b2922b8ffaed204812013169)

-------------------------

