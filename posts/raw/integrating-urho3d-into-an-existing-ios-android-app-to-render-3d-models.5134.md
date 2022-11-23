jptsetung | 2019-05-01 13:40:33 UTC | #1

Hello. I'm having hard time to find a cross platform 3D engine that could integrate into an existing native ios (Xcode) / android (Android studio) app. I would like at one point in the app to present a 3D view developed with Urho3D. Thanks for any help.

-------------------------

Modanung | 2019-05-01 05:08:51 UTC | #2

Hi @jptsetung, and welcome to the forums! :confetti_ball: :slightly_smiling_face:

Although it should be technically possible, could you more specifically describe what you're looking to accomplish as well as any obstacles you may see ahead or have already encountered?

-------------------------

jptsetung | 2019-05-01 09:51:03 UTC | #3

I have an app which is not a 3D app, it show classic user interface views for iOS and android. At some point in the app, I want to launch a 3D view (full screen), and I wanted to study the possibility to use a 3D engine like Urho3D to do this. All utotirlas I read are based on cmake which build a whole app using the 3D engine, but didn't see any tutorial about integrating the engine in an existing app.

-------------------------

Modanung | 2019-05-01 12:11:49 UTC | #4

Maybe you could use [Edddy](https://gitlab.com/luckeyproductions/Edddy) as an example, or @aster2013's [particle editor](https://discourse.urho3d.io/t/qt-based-2d-particle-editor-for-urho3d/327), which has a quite similar approach.

-------------------------

