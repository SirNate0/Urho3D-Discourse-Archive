Elendil | 2017-09-07 10:56:56 UTC | #1

Hello

I am looking for engine with this possibilities, and have question for Urho

1. Can terrain have holes? Fro creating caves, and entrance for underground areas. This areas will be modeled in some modeling tools like Blender.

2. (I am new with this and maybe don't know proper terminology, then please excuse me.)
It is possible join two or more meshes or objects in to one? For example I have world created completly in Blender and is divided in to pieces, but when lightning is used, it is visible - borders of the objects, it looks like some meshes are not smoothed. And I want connect those pieces looks like one in Urho. It is possible? It is good for LOD system, if some world area is far, then I change model to more low poly.

3. How many textures I can use for object and terran? Can I use around 20 or more textures for one material?

Do you know other engines which support this features? If yes please write which.

-------------------------

Eugene | 2017-09-07 13:27:03 UTC | #2

[quote="Elendil, post:1, topic:3538"]
Can terrain have holes? Fro creating caves, and entrance for underground areas. This areas will be modeled in some modeling tools like Blender.
[/quote]

Semi-transparent material for graphics.

Physics will require tweaking Bullet Physics, but that's easy. I shall probably commit the change into Urho.
Navigation will also require some tweaking.
Thanks for reminding, I shall probably add some support of the holes in the Terrain. However, don't expect this in the nearest future.

> but when lightning is used, it is visible - borders of the objects

Sounds like a content problem. Any screenshots?

> How many textures I can use for object and terran? Can I use around 20 or more textures for one material?

If you are ready to write your own shader that manages those textures, you are limited only with hardware capabilities. However, Urho doesn't have builtin support of multiple textures due to absence of generic solution here. Terrain too.

-------------------------

Elendil | 2017-09-07 14:10:01 UTC | #3

Thanks for answers.
> Sounds like a content problem. Any screenshots?

This is only for example, world will be more complicated then this 9 pieces, but you can see in image it is created with 9 pieces
https://www.dropbox.com/s/p68fsg2tcb0ed80/terrainSplit.jpg?dl=1

and I want in Urho looks like this
https://www.dropbox.com/s/hik51jx0n7tomq4/terrainOne.jpg?dl=1
It is looks like one, but there are 9 pieces. Of course, this is in Blender joined in to one mesh, but it is only for example. I need export world from Blender in pieces for change some pieces as low poly in far distance.

> If you are ready to write your own shader that manages those textures, you are limited only with hardware capabilities. However, Urho doesn’t have builtin support of multiple textures due to absence of generic solution here. Terrain too.

But in the end it is possible (Create and use this my own shader in Urho)? And how hard is create own shader for beginer? I never created any shader before.

And what about disable one or more chunks in terrain for make holes? If I am right, Urho use GeoMipMap, which divide terrain in to chunks, and disable selected chunks to create hole is interesting idea, but this chunks must not be big.

-------------------------

Eugene | 2017-09-07 14:43:13 UTC | #4

[quote="Elendil, post:3, topic:3538"]
It is looks like one, but there are 9 pieces. Of course, this is in Blender joined in to one mesh, but it is only for example. I need export world from Blender in pieces for change some pieces as low poly in far distance.
[/quote]

I see that both images are made in Blender. So if you have the problem with divided model in the Blender, you should fix it there.

[quote="Elendil, post:3, topic:3538"]
But in the end it is possible (Create and use this my own shader in Urho)? And how hard is create own shader for beginer? I never created any shader before.
[/quote]

Urho allows you to do almost whatever you want. Only the effort is varying. I couldn't estimate anything for you. Urho doesn't make obstructions for you, but shaders could be very complicated algorithmically.

> And what about disable one or more chunks in terrain for make holes? 

Try to play with enabling/disabling TerrainPatch-es. But I don't know whether it helps.

-------------------------

lezak | 2017-09-07 15:20:54 UTC | #5

[quote="Elendil, post:3, topic:3538"]
This is only for example, world will be more complicated then this 9 pieces, but you can see in image it is created with 9 pieces
[/quote]

There's nice blender <a href=https://github.com/fedackb/yavne> addon </a> that may help You with that.

-------------------------

Elendil | 2017-09-07 15:27:34 UTC | #6

Thanks, for all but I think we are not understand each other. I don't want make 9 pieces looks like one in Blender, I want to do it in Urho engine and if it is possible. Imagine you have World created with this 9 pieces, with different textures, but texture on edges will be same as near next block. And it is look ok when there is no lightning. Problem is when lightning is used, it is looks like on image 1. And I want it looks like in image2 and world will be still divided in to pieces.

-------------------------

Eugene | 2017-09-07 15:31:56 UTC | #7

Did you tried neighbor terrains?

-------------------------

Elendil | 2017-09-07 15:33:43 UTC | #8

No, I am just asking before I decide use Urho.

-------------------------

Eugene | 2017-09-07 15:50:59 UTC | #9

[quote="Elendil, post:6, topic:3538"]
Problem is when lightning is used, it is looks like on image 1.
[/quote]
Huh... I am confused a bit.
Is the problem with lighting in Blender or Urho?

-------------------------

Elendil | 2017-09-07 17:07:52 UTC | #10

Hmm, maybe I am not describe it clear, I apologize for that. 
Lightning is not problem. Problem is when world or objects are created with separated pieces as in image one, I expect it will looks same (like on image one) whether in Blender, Urho or any other 3D rendering engine (because vertexes are not joined and smoothed with next object vertexes). This is unwanted effect (for me). 
And therefore I asking if Urho have possibilities for joint or make this separated pieces looks like one (join all separated vertexes with next object and smooth them). Like on second image. I am writing "join all separated vertexes", but this is only for describe what I want to do, in reality it is called maybe different or it is completely different technique (in Urho).

-------------------------

hdunderscore | 2017-09-07 17:56:01 UTC | #11

Can you merge models into one in urho? Yes, but there is another solution that is more common for your problem.

What you want is to make sure the normals are set up properly in Blender on your split models. What happens is that when you split your model in blender, the edge normals are no longer the same as when it was one big piece. Blender supports custom/split normals (and the Urho-Blender exporter respects them), so you can use the normal/data transfer modifiers to transfer the normals from the big mesh onto the small mesh pieces.

-------------------------

Eugene | 2017-09-07 18:27:25 UTC | #12

Thanks, I got it!
I don't recommend you to rely onto the engine here (either Urho or whatever you choose).
Normals is a content, so its always better to prepare them on the content side and don't touch in the engine. This is the most stable and reliable way of doing things.

-------------------------

Elendil | 2017-09-07 18:54:47 UTC | #13

Thanks all for answers.

hdunderscore this was very informative. Thanks for it.

-------------------------

