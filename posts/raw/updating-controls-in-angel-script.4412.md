Bananaft | 2018-07-26 22:43:22 UTC | #1

So in NinjaSnowWar.as controls are updated during Update and then assigned to a player controlled ninja. Ninja.as uses this controls during FixedUpdate.

What if I want to use some controls in regular update? For example mouse look is better to be handled during regular update. How can I ensure that main script will be updated before any other objects? Because otherwise there will be one frame lag.

Is there other good ways to handle controls in script?

Also, I just noticed that Ninja Snow War uses:
`SubscribeToEvent(gameScene, "SceneUpdate", "HandleUpdate");`
While all other samples use:
`SubscribeToEvent("Update", "HandleUpdate");`
Why it's so? And what is the difference?

-------------------------

jmiller | 2018-07-27 00:42:10 UTC | #2

Hi Bananaft,

[url=https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Core/Object.h#L113]SubscribeToEvent() has overloads[/url] to subscribe to events sent by a specific [code]Object[/code], e.g.
[code]SubscribeToEvent(node_, E_NODECOLLISION, URHO3D_HANDLER(Character, HandleNodeCollision));[/code]

E_UPDATE is the application-wide variable timestep update event you know.
On E_UPDATE, the Scene sends E_SCENEUPDATE (Urho3D/Scene/SceneEvents.h) only if the scene is enabled.

*edit: I have a CameraController that sets controls in E_UPDATE while CharacterController sets them in E_SCENEUPDATE. Maybe not the best way if there could be a frame lag?

HTH

-------------------------

Bananaft | 2018-07-27 11:30:54 UTC | #3

Hi, thank you for reply, @jmiller.
 
I did some tests with frame number logging. Fascinating finding, If my main game script subscribes to plain update, it happens last in the frame, after all other objects already updated. If it subscribes to scene update, just like Ninja Snow War does, update happens first in the frame. But I'm not sure If I can rely on this order, since I was able to squeeze player's update before it, by creating player object before subscribing game script to this events, also disabling and reenabling components changes this order.
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/400612b4801cd1739523b295ccf70d469812302a.png'>

[quote="jmiller, post:2, topic:4412"]
*edit: I have a CameraController that sets controls in E_UPDATE while CharacterController sets them in E_SCENEUPDATE. Maybe not the best way if there could be a frame lag?
[/quote]
Are they query input subsystem both by they own or doing something like NinjaSnowWar? If first, there can be no lag.

-------------------------

jmiller | 2018-07-27 13:57:54 UTC | #4

Ah, yes, my Controller objects are replicated like NSW. Thanks for the findings.

-------------------------

