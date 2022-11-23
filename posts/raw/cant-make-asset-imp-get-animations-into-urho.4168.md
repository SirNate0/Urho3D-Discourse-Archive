johnnycable | 2018-04-11 09:51:35 UTC | #1

I'm getting problems at importing animations in Urho using asset importer. I've made a dead fish animation

![25|690x405](upload://8gYIF8C2y7LydmPbSMYDFLRBLrS.png)

Can someone give it a try? [the blend](https://drive.google.com/open?id=1Yg85tqVhLQSDu7QG90WhIJsimkFK0AQd)

-------------------------

Modanung | 2018-04-11 21:11:33 UTC | #2

Have you tried using the [exporter](https://github.com/reattiva/Urho3D-Blender)?

-------------------------

johnnycable | 2018-04-12 08:09:53 UTC | #3

Yes, the exporter works well, except for cameras and framing; I have multiple cameras and wasn't able to export them, just one is exported. Anyway, apart from this is ok for animation and the rest.
I've tried assimp over and over and I've got to think there's a bug in it. The assimp library itself has the same problem, so I think I'll have to open a bug there and then notify it in our bug list. Just wanted some confirmation about it before I do...
I'm pretty sure asset imported worked in 1.6 (that is, in that assimp version), but at the moment I'm unable to set it up...

-------------------------

