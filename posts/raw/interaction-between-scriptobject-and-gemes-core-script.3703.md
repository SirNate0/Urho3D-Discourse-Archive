Bananaft | 2017-11-01 08:00:58 UTC | #1

In Ninja Snow core script, [NinjaSnowWar.as](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/NinjaSnowWar.as) checks in every frame if player node is still here, to know when player is dead. to ask for restart.

Let's say, I want to add some more complex interaction between player, or other objects and core script. Can I access core script's variables or functions? Is there any message system or custom events? What is the neat way of doing it?

-------------------------

Modanung | 2017-11-01 13:46:52 UTC | #2

Yes, you can define custom events. The SceneReplication sample (nr. 17) has a custom ClientObjectID event.

I think the reason NinjaSnowWar checks every frame is to keep the code simple while focusing on scene replication. You could add custom events and/or statemachines for this purpose.

-------------------------

