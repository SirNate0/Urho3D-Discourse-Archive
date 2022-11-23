urnenfeld | 2019-01-27 17:18:49 UTC | #1

Hello,

I had a videogame idea in my head for a long time, and ended up choosing Urho3D. I am very new to the engine, but explored the code of the examples for some days.

Unfortunately, none of the examples give me a good base for starting point of what I had in mind and I miss some gamedev insights. Therefore I need a guide to not make catastrophic mistakes right in the begining.

For starting:

- I need to place the players (StaticModel?) inside a Room (StaticModel/box.mdl?) Am I in the good direction?

- A very newbie concept I am missing: How do I apply the texture(SetMaterial?) to the inside of the box? (always that I navigate with the camera inside a box object it becomes transparent)

- Assuming the player will float in the 3 axis inside the room, What's reference/example to look at if I want it to avoid him going out of the room?

- Which examples/classes/links should I look at to accomplish this first step?

Thanks a lot for your time!

-------------------------

Modanung | 2019-01-27 18:34:50 UTC | #2

Hi @urnenfeld, and welcome to the forums! :confetti_ball: :slightly_smiling_face:

The answers to your questions depend on your project, and even then there are often many ways to approach similar goals.   
But firstly, did you manage to set up some sort of empty project that compiles and runs?

-------------------------

urnenfeld | 2019-01-27 18:55:05 UTC | #3

Hi @Modanung in fact any path that is not totally wrong will do for me :smile: Thanks for welcome!

I compiled the whole engine, so currently I am playing/modifying over one of the examples(10_RenderToTexture). I understand in the future (among other things) I will need to pay attention to the Sample class and change it to fit my needs.

I know is not the cleanest way to start a project, but that gave me a fast way to make modifications add things and see its efects. So yes we can say I have a working environment for learning.

Regards

-------------------------

I3DB | 2019-01-27 19:29:34 UTC | #4

[quote="urnenfeld, post:1, topic:4871"]
I need to place the players (StaticModel?) inside a Room (StaticModel/box.mdl?) Am I in the good direction?
[/quote]

From one newbie to another.

Probably not. A box is an object inside your Scene. The Scene is the box you're thinking of. Everything will be in it.

[quote="urnenfeld, post:1, topic:4871"]
A very newbie concept I am missing: How do I apply the texture(SetMaterial?) to the inside of the box? (always that I navigate with the camera inside a box object it becomes transparent)
[/quote]

I think this is done with normals. If you reverse the normals, you'll see the material on the inside, and it will be transparent when looking into the box, and visible when inside the box. But, refer back to your first question, you probably don't want to create a game or scene, with a box.mdl as your game container.

[quote="urnenfeld, post:1, topic:4871"]
Assuming the player will float in the 3 axis inside the room, What’s reference/example to look at if I want it to avoid him going out of the room?
[/quote]

The skeletal animation sample turns the model when it hits limits. In c# that little bit of code looks like this:
```
// If in risk of going outside the plane, rotate the model right
				var pos = Node.Position;
				if (pos.X < Bounds.Min.X || pos.X > Bounds.Max.X || pos.Z < Bounds.Min.Z || pos.Z > Bounds.Max.Z)
					Node.Yaw(RotationSpeed * timeStep, TransformSpace.Local);
```

[quote="urnenfeld, post:1, topic:4871"]
Which examples/classes/links should I look at to accomplish this first step?
[/quote]

How about the 'static scene' sample. If you spend most of your time initially going through the samples, the rest of your time will be better spent. Then as you create your game, create your own simple, basic samples of each feature you add into your game. As @slapin wrote:

[quote="I3DB, post:12, topic:4869"]
That will make your
learning less frustrating.
[/quote]

-------------------------

urnenfeld | 2019-01-27 23:19:29 UTC | #5

Hi @I3DB ! 
[quote="I3DB, post:4, topic:4871"]
The Scene is the box you’re thinking of. Everything will be in it.
[/quote]

So how would I put walls to this Scene?
I saw the StaticScene example places all the mushrooms in a plane (and this node is direct child from the scene...) 
> Node* planeNode = scene_->CreateChild("Plane");
> planeNode->SetScale(Vector3(100.0f, 1.0f, 100.0f));
> auto* planeObject = planeNode->CreateComponent<StaticModel>();
> planeObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));

May I create 6 planes?

Thanks for the other References!

-------------------------

I3DB | 2019-01-27 23:34:09 UTC | #6

Try a skybox. The water feature sample uses one.

https://github.com/urho3d/Urho3D/wiki/Skyboxes

-------------------------

Leith | 2019-01-28 05:41:28 UTC | #7

Urho3D's Scene object is basically providing a Root Node for a Scene Hierarchy, consisting of Nodes which may or may not have Components attached to them. Nodes have transforms which are relative to their parents, but the root node of a scene generally has identity transform (no rotation, no translation, so position is <0,0,0>, and scale of <1,1,1>)
Scene hierarchies are pretty common to all game engines, so I would start by finding out what they are for. 

It is notable for Urho3D that Components do not have a Transform (like Unity), but instead they derive their transform from their immediate parent node. The implication is that if you attach multiple Model components to the same Node, they all have the same Transform.
Therefore, you should have a unique Node for each Plane, and set the orientation for each Node to suit yourself.

It is also notable for Urho3D that multiple scenes can exist at the same time (unlike Unity), which can be useful for games that load content on demand, as each scene can represent a connected subspace, or even be used to contain stuff separate to the game itself (menus, gamestates, whatever).
This is a very flexible system in my opinion, it can be (ab)used in many wonderful ways.

-------------------------

guk_alex | 2019-01-28 09:10:21 UTC | #8

Hi. If you not familiar with common gamedev concepts then it's time to start investigate it. There are a lot of tutorials you can find on youtube (most of them can use some popular engines like Unity and Unreal - don't hesitate to look into it too, because concepts are pretty much the same in every engine; their documentation contains general stuff too). 

Also, consider to get more familiar with 3d modelling (it is actually very fun to get familiar with) - Blender tutorials could be the good point to start (you'll know some basic stuff about vertex, edges, faces, normals, textures and materials; and then you could easily create some own easy assets without finding or buying it on the web) - you will know that box.mdl is not intended to be viewed from inside (but with basic modelling knowledge you can fix it in a few seconds), and you need different model or use scaled boxes/planes as a walls and floor.

So, I wish you good luck in your beginnings!

-------------------------

urnenfeld | 2019-01-28 10:50:29 UTC | #9

Hi @Leith @guk_alex 

[quote="Leith, post:7, topic:4871"]
Nodes have transforms which are relative to their parents, but the root node of a scene generally has identity transform (no rotation, no translation, so position is &lt;0,0,0&gt;, and scale of &lt;1,1,1&gt;)
[...]

It is notable for Urho3D that Components do not have a Transform (like Unity), but instead they derive their transform from their immediate parent node. The implication is that if you attach multiple Model components to the same Node, they all have the same Transform.
[/quote]

Thanks! these are very relevant theoretic concepts.

[quote="guk_alex, post:8, topic:4871"]
If you not familiar with common gamedev concepts then it’s time to start investigate it. There are a lot of tutorials you can find on youtube. There are a lot of tutorials you can find on youtube
[/quote]

I see lots of tutorials, but all I find are focusing in the teaching a specific engine, and going to the practical part without explaining the actual theoretic concepts behind, which as mentioned I hope to be common in all engines. Let me know if you would recommend any.

[quote="guk_alex, post:8, topic:4871"]
and you need different model or use scaled boxes/planes as a walls and floor.
[/quote]

In fact that is how I started, by placing _6 flat boxes_ afterwards I though that could be done with only 1 box... then decided to jump here :blush:

Thanks! I think I will be able to start something from here.

-------------------------

guk_alex | 2019-01-28 11:17:49 UTC | #10

If you wish to learn real "deep" in how rendering works there is an excellent tutorial for openGL (rendering, shaders, etc.) it is easy too follow and provide real great results and knowledge witch you can apply to any engine : https://learnopengl.com/

Previous link is only about rendering stuff, but to create an actual game you also need structural logic (scene, hierarchy, component system, etc). Actually you can start right away and find info you need during the process, but when you want to create something that is little bit bigger then example scene then it is time people actually start getting frustrated.

If somebody have some good gamedev sources (about logic and structural stuff, or how to start game development in "right" way, maybe some patterns) - please, share.

We could actually start a different thread for this kind of links, or make a dedicated page in tutorials. To create a real game engine knowledge is not enough.

-------------------------

urnenfeld | 2019-01-28 14:13:09 UTC | #11

[quote="guk_alex, post:10, topic:4871"]
If somebody have some good gamedev sources (about logic and structural stuff, or how to start game development in “right” way, maybe some patterns) - please, share.
[/quote]

Well if you mention software patterns then I have something to contribute: http://www.gameprogrammingpatterns.com

Is a free online book, It focuses in the logics. I have read most of this book.  It could be useful even if you don't plan to develop a game, and just learn about how & where to apply software pattens. ...Although I think the level in this forum is higher.

-------------------------

Modanung | 2019-01-30 12:02:29 UTC | #12

@urnenfeld Any progress? If you've been experimenting a bit I bet some of your questions were answered in the process, and maybe new ones arised?

Might you be interested in [templates](https://discourse.urho3d.io/t/wrench-class-and-project-wizards-for-qtcreator/2076), btw?

-------------------------

urnenfeld | 2019-01-30 18:49:58 UTC | #13

Hi @Modanung some progress of course, questions are too many I'll keep them to the strictly necessary.

On the way, I saw in the source code there is some sample of materials/textures/etc, but very few... 
Is there a larger catalog of materials somewhere else?

Regards!

-------------------------

Leith | 2019-01-31 10:10:31 UTC | #14

Materials are usually made by artists, and we Export them to Urho3D, via the AssetExporter, and most materials can be defined by the standard set of shaders that Urho3D provides - but we can always modify materials, and we can provide custom shaders too - I'm getting there quickly.
I can code shaders, but I don't know Urho3D well enough to make magic just yet... it will happen soon.

-------------------------

Modanung | 2019-01-31 11:25:35 UTC | #15

I generally use the editor to create materials. You may want to get to grips with writing your own shaders for more control. Although the provided _techniques_ can get you a long way when combined with some nice textures.

-------------------------

Leith | 2019-01-31 10:37:38 UTC | #16

I generally dont use the editor yet, but materials associated with models tend to come from the artist, not the coder - I'll try again on the editor issue soon, at this stage its nice enough for me to make things work![zombiecop|690x194](upload://e9M0nY2ciBYAX7CpfyASG12Bz0j.jpeg)

-------------------------

Modanung | 2019-01-31 10:41:53 UTC | #17

[quote="Leith, post:16, topic:4871"]
materials associated with models tend to come from the artist, not the coder
[/quote]

I'm both... or neither, depends how you look at it. :stuck_out_tongue:

Which I expect to be more common in indie game development as opposed to the industry.

-------------------------

Leith | 2019-01-31 10:42:03 UTC | #18

we load a model, we apply a set of materials to it .. its not really relevant where the art came from until it comes to selling your product, or showing it in public, thats the thing they don't teach until the bachelor year, the legal issues, like what is plagiarism, and what does an NDA mean to you

-------------------------

