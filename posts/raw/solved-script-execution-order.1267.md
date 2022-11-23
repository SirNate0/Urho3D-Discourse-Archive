1vanK | 2017-01-02 01:06:30 UTC | #1

I try to using Unity3D-style for my project (many small scripts that are attached to their objects). How do I determine the order of the scripts?
For example, a hero has a script that moves the character by pressing a keys. And a camera has a script which set its position relative to the hero.
How to force to execute the camera script after the hero script?

-------------------------

cadaver | 2017-01-02 01:06:30 UTC | #2

In general the event handling order is unspecified and you shouldn't assume anything about it. There isn't a similar "script execution order" concept as in Unity.

Instead use different events for things you want to happen in sequence during the frame. NinjaSnowWar follows the principle of updating camera in PostUpdate. Look at the main loop documentation page: [urho3d.github.io/documentation/1 ... _loop.html](http://urho3d.github.io/documentation/1.4/_main_loop.html)

If necessary, you can invent your own events, and raise them at some point during the frame. For example a "CameraUpdate" event.

-------------------------

1vanK | 2017-01-02 01:06:30 UTC | #3

Thank you. If someone has a similar task, here's a small example:

[spoiler]Game.as
[code]
...
void CreateScene()
{
    ...
    heroNode.CreateScriptObject("Scripts/HeroScript.as", "HeroScript");
    ...
    cameraNode.CreateScriptObject("Scripts/CameraScript.as", "CameraScript");
    ...
}
...
[/code]
HeroScript.as
[code]
class HeroScript : ScriptObject
{
    void Update(float timeStep)
    {
        const float MOVE_SPEED = 20.0f;
        
        if (input.keyDown['W'])
            node.Translate(Vector3(0.0f, 0.0f, 1.0f) * MOVE_SPEED * timeStep);
        if (input.keyDown['S'])
            node.Translate(Vector3(0.0f, 0.0f, -1.0f) * MOVE_SPEED * timeStep);
        if (input.keyDown['A'])
            node.Translate(Vector3(-1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);
        if (input.keyDown['D'])
            node.Translate(Vector3(1.0f, 0.0f, 0.0f) * MOVE_SPEED * timeStep);

        VariantMap eventData;
        eventData["HeroPosition"] = node.position;
        SendEvent("UpdateCamera", eventData);
    }
}
[/code]
CameraScript.as
[code]
class CameraScript : ScriptObject
{
    void Start()
    {
        SubscribeToEvent("UpdateCamera", "HandleUpdateCamera");
    }

    void HandleUpdateCamera(StringHash eventType, VariantMap& eventData)
    {
        Vector3 heroPosition = eventData["HeroPosition"].GetVector3();
        node.position = heroPosition + Vector3(10.0f, 10.0f, 10.0f);
    }
}
[/code][/spoiler]

-------------------------

