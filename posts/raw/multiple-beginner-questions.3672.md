Sean221 | 2017-10-19 19:28:05 UTC | #1

Hi im very new to using this engine and i have a few simple questions that i hope you can help me with.

First how does saving and loading scenes work? To get me started can you tell me how to save and load a cube that moves randomly in a scene.

This also leads onto how do i switch between scenes?

How do i add my own models into the game? 

Finally ow do i apply my own textures to a cube? I tried trying to modify an xml file and replacing the texture it references but that did not work.

If anyone can help answer some of these questions i would be very thankful.

-------------------------

Eugene | 2017-10-19 19:47:18 UTC | #2

[quote="Sean221, post:1, topic:3672"]
First how does saving and loading scenes work?
[/quote]

`Scene::Load` and `Scene::Save`. Please, elaborate the question.

[quote="Sean221, post:1, topic:3672"]
how do i switch between scenes?
[/quote]
Change active scene and camera for your `Viewport`(s)

[quote="Sean221, post:1, topic:3672"]
How do i add my own models into the game?
[/quote]
Use AssetImporter tool or Blender plugin to convert your model into Urho format.

[quote="Sean221, post:1, topic:3672"]
Finally ow do i apply my own textures to a cube?
[/quote]
This is done in Material. Take some standard material and put your own textures.
If it doesn't work, check paths and/or provide more information.

-------------------------

Modanung | 2017-10-19 22:48:17 UTC | #3

Are you aware of the dozens of [_samples_](https://github.com/urho3d/Urho3D/tree/master/Source/Samples) that come with the engine? They are well commented and may answer many of your questions, along with the [documentation](https://urho3d.github.io/documentation/HEAD/).

[quote="Sean221, post:1, topic:3672"]
How do i add my own models into the game?
[/quote]

The Blender exporter @Eugene mentioned can be found [here](https://github.com/reattiva/Urho3D-Blender).

And welcome to the forums! :confetti_ball:

-------------------------

