extobias | 2018-12-11 04:01:03 UTC | #1

I have a model with 2 geometries and a skeleton, which I load in an AnimatedModel. When the skeleton is created
the associated nodes are generated, from the editor I can modify them and I see that each
one is associated with a part of the geometry. Is it possible to hide this part of the geometry?
I was able to create a child node, and a StaticModel component with another mesh, but I can not
hide the part that already comes in the original model.
I hope you understand
regards!

-------------------------

orefkov | 2018-12-11 05:34:44 UTC | #2

Try to set scale 0 for this node.

-------------------------

Modanung | 2018-12-11 10:22:42 UTC | #3

If you mean hiding one of the two geometries, you could make a transparent material for this purpose.

-------------------------

extobias | 2018-12-11 14:21:52 UTC | #4

That was the first thing I tried, but some vertices of the model were
distorted, what I did was
<code>
if(bone->name_ == "Bip01 Head")
{                     
bone->animated_ = false;
bone->node_->SetScale(0.0f);
Node* childHead = bone->node_->CreateChild("head-adjust") ;
StaticModel* headModel = childHead->CreateComponent<StaticModel>();
}
</code>

The main idea would be to have a single skeleton and different meshes for the body parts of the character

-------------------------

extobias | 2018-12-11 14:24:47 UTC | #5

The problem is that the bone node is not associated with a geometry but with a part of it. Try to find how the nodes created by the skeleton influence that geometry but I did not find it.

-------------------------

Modanung | 2018-12-11 14:28:16 UTC | #6

I think my remark may be irrelevant to what you mean.

-------------------------

extobias | 2018-12-11 16:05:55 UTC | #7

I applied the GreenTransparent material to geometry one. Im trying to hide only the head, which is only part of the geometry.
is this what you suggest? let me know if this is correct

![fb2b785ee9ce|320x320](upload://s87v7UQj5hORjL9Kiw1Ko2t8lak.gif)

-------------------------

Sinoid | 2018-12-11 19:41:52 UTC | #8

The renderer doesn't understand enough to *discard* rendering a fully transparent geometry - it'll still draw it, so using transparency to remove something isn't a good idea outside of a transition period where it's fading/dissolving away or such.

> Im trying to hide only the head, which is only part of the geometry.

By head do you mean the helmet or the head inside of the helmet?

**If you mean the head inside of the helmet:** no, you can't do that - you'll need have your head as a separate model and use multiple models to put your character together (they can use the same skeleton rig).

**The same would apply if you mean the helmet**, but since the helmet is presumably a separate geometry you can also make engine changes to deal with it in that case rather than using multiple models.

-------------------------

extobias | 2018-12-11 21:48:09 UTC | #9

I mean the helmet only. What I have are these two geometries in a model.

![untitled|690x388](upload://Aiv6cEjfL5XhuC6I2HZqUVw583j.png) 

What I would like is to replace parts, like the original helmet, with others customized like this

![untitled2|690x388](upload://ngNS0LEyh5QhReUgcNUaoeWjFmi.png) 

From what I understand is not possible without modifying the engine? I should create a model
with the body of the original character and the new helmet?

-------------------------

orefkov | 2018-12-19 18:11:42 UTC | #10

Split the original mesh into several separate parts. Use them as separate components on one node, first AnimatedModel become "master-model". When part of the mesh is not needed - disable this component.
Or if hiden part is separate geometry - try set for it empty vertex buffer.

-------------------------

Sinoid | 2018-12-11 22:23:47 UTC | #11

[quote="extobias, post:9, topic:4729"]
From what I understand is not possible without modifying the engine? I should create a model
with the body of the original character and the new helmet?
[/quote]

Just a model of the helmet with the skeleton still connected. In `AnimatedModel` the first `AnimatedModel` on a node serves as the **master**, all other `AnimatedModel` on the same node with the same skeleton layout will be matched to the animation (don't think it actually checks layout though) the master model is playing. First model is boss. Make sense?

-------------------------

extobias | 2018-12-19 18:13:40 UTC | #12

It works perfect, I had to split the original model and add the new helmet with the skeleton.

-------------------------

