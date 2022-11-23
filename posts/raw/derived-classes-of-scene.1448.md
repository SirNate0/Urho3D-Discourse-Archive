1vanK | 2017-01-02 01:07:47 UTC | #1

C++ still hard for me, and I can not solve the following problem

I want to complicate the class Scene:

[code]
class Level : public Scene
{
    URHO3D_OBJECT(Level, Scene);

public:
    Level(Context* context);
    Camera* camera_ = nullptr;
    void Show();
    void HandleUpdate(StringHash eventType, VariantMap& eventData);
};

Level::Level(Context* context) : Scene(context)
{
    SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(Level, HandleUpdate));
}

void Level::Show()
{
    if (!camera_)
        camera_ = GetChild("Camera")->GetComponent<Camera>();

    Renderer* renderer = GetSubsystem<Renderer>();
    Viewport* viewport = renderer->GetViewport(0);
    viewport->SetScene(this);
    viewport->SetCamera(camera_);
}

void Level::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    // some actions
}
[/code]

And using it in game:

[code]
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Level* level1 = new Level(context_);
    scene->LoadXML(*cache->GetFile("Scenes/1.xml"));
[/code]

The level is loaded from a file, but the physics does not work. As far as I understand, the reason for this is the overriding handler of update.

In XNA handlers were determined as protected, and users can call functions of base class, but in Urho3D all private. Any ideas?

-------------------------

1vanK | 2017-01-02 01:07:47 UTC | #2

I found a workaround. Just manually call Update function:

[code]
void Level::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    using namespace Update;
    Update(eventData[P_TIMESTEP].GetFloat());

    // some actions
}
[/code]

-------------------------

Dave82 | 2017-01-02 01:07:47 UTC | #3

Thats not the best way. You have to call Scene's HandleUpdate inside Your Level class

[code]void Level::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    Scene::HandleUpdate(eventType , eventData);

    // some actions
}
[/code]
Also if you planning to use networking and the serialization the code may lead to problems .
As we already discussed this here :

[topic1487.html](http://discourse.urho3d.io/t/whats-the-proper-way-to-register-a-custom-node-method/1436/1)

-------------------------

1vanK | 2017-01-02 01:07:47 UTC | #4

HandleUpdate is private

-------------------------

Dave82 | 2017-01-02 01:07:47 UTC | #5

Ahh i see in that case thats the only solution ! Still this is a pretty bad workaround because "private" means that the member function is only used by the class.If the developers add some other things inside Scene::HandleUpdate()  you're doomed. Also HandleUpdate isn't virtual so thats another sign why you shouldn't declare your own version of it.

private non virtual functions and members are a "don't touch this ever" kinda signs.

-------------------------

