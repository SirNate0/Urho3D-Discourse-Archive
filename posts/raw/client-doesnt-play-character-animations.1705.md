krokodilcapa | 2017-01-02 01:09:36 UTC | #1

Hello Urho3D community!

I'm new to this engine, I just started to playing around with it a few days ago. I have a problem, and I can't solve it since two long nights without sleep, so I hope somebody can help me. As the topic title says, I can't play character animations on client side, only on server side plays. First I tried to create a project based on NinjaSnowWar (but I work with C++), everything worked except the anims, but after that I tried something simplier, to combine SceneReplication sample with the CharacterDemo. I don't paste code yet, because I don't think its needed, I just changed the ball to the Character class from CharacterDemo, and also changed the controls of it of course. AnimationController is not local, and created right after AnimatedModel, and in the same node. Controls works fine, so client send it to the server, and Jack is also moving, but without walk :smiley:.

-------------------------

rasteron | 2017-01-02 01:09:36 UTC | #2

Welcome to the forums krokodilcapa! :slight_smile:

If you like to check out scorvi's port of NinjaSnowWar in C++ and maybe compare it with your project. Here's the repo, along with other useful stuff:

[github.com/scorvi/Urho3DSamples](https://github.com/scorvi/Urho3DSamples)
[github.com/scorvi/Urho3DSamples ... njaSnowWar](https://github.com/scorvi/Urho3DSamples/tree/master/07_NinjaSnowWar)

Hope that helps.

-------------------------

krokodilcapa | 2017-01-02 01:09:37 UTC | #3

Thanks rasteron! I'll take a look on the code, and see what was I missing!

-------------------------

