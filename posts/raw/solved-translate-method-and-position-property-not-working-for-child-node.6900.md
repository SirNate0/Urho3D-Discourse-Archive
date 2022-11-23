Jens | 2021-06-24 09:27:34 UTC | #1

Hi -

I'm using the c# wrapper, so I suppose this may not be an issue with Urho3d.

Actually, I'm not even sure it's an issue with Urhosharp, and may well be intended behaviour. In any case, there is a model object that moves as expected if its node position property is set:
```
 shieldNode.Position = new Vector3(-2f, 2f, 0f);
 Scene.AddChild(shieldNode);
```
However, if added to another model object's node, rather than the scene, the shieldNode model does not budge from zero:
``` 
shieldNode.Position = new Vector3(-2f, 2f, 0f);
 otherModelNode.AddChild(shieldNode);
```
The node Position property is filled correctly, but as stated, the actual model does not move at all. This also occurs with Translate() in local or parent space, though translate works in world space. Rotation and SetWorldPosition() also work.

I would've thought that the .Position property should work within parent space - it does not. It would be great if there was an explanation for this behaviour.

-------------------------

throwawayerino | 2021-06-23 18:33:47 UTC | #2

I'm not sure how the position property is implemented, but it's supposed to be based on the node's origin I think. Try attaching the node to a parent before transforming?

-------------------------

Jens | 2021-06-23 19:35:44 UTC | #3

[quote="throwawayerino, post:2, topic:6900, full:true"]
I’m not sure how the position property is implemented, but it’s supposed to be based on the node’s origin I think. Try attaching the node to a parent before transforming?
[/quote]

Unfortunately, it makes no difference.

-------------------------

Jens | 2021-06-24 09:43:56 UTC | #4

The problem was scaling. The model was scaled by 0.02 and the sub node model by a further 0.25. It seems that the parent space is also scaled which would make sense.
Am still confused in that the dimensions need *around* 100 multipliers to move roughly as expected with no scaling. I would of thought that multiplying by 4 would be enough for the sub node model.
Still, the position/translate do work in parent/local space, so this is considered solved.

-------------------------

