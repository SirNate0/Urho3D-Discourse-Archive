Enhex | 2017-01-02 01:08:31 UTC | #1

I'm using shadows causes performance problem because it creates tons of batches.

~25,000 batches, shadows enabled, direct lighting, 124ms frame on a users machine:
[i.imgur.com/pfDEx7j.jpg](http://i.imgur.com/pfDEx7j.jpg)

[b][u]on my machine:[/u][/b]
~29,000 batches, shadows enabled, direct lighting:
[i.imgur.com/tDY1CD4.jpg](http://i.imgur.com/tDY1CD4.jpg)
~4,400 batches, shadows [b]disabled[/b], direct lighting:
[i.imgur.com/TRu1ot8.jpg](http://i.imgur.com/TRu1ot8.jpg)
179 batches, shadows [b]disabled[/b], [b]deferred[/b] lighting:
[i.imgur.com/gU4BaYD.jpg](http://i.imgur.com/gU4BaYD.jpg)

I'm using CustomGeometry to create the level models, could it be related to the lack of batching?
It seems like it creates a batch for every visible triangle.

Any idea what might cause it?

-------------------------

cadaver | 2017-01-02 01:08:33 UTC | #2

If you have shadow casting point lights, they will render 6 shadow map faces, so your batch count will explode, particularly if the lights have large radii. Also in forward mode, each object affected by each light (in addition to the first one which is rendered with LitBase) will be a batch.

You can try playing with light and shadow masks in case your lights are "bleeding" to unnecessary objects. But in general, large number of dynamic lights will be a performance loss and you might have to look into some kind of precalculated lighting instead.

If you had models instead of customgeometries, for example 10 nodes each having the same model, same material and LOD, they could be instanced to 1 batch when in the same view (this applies to all of: main camera view, shadow map face, or an additive lighting pass)

Also, try to have as few customgeometries as possible, and within each, as little subgeometries as possible. Do not start a new subgeometry per triangle if it has a different material than the previous, but rather group together the triangles with the same material into the same subgeometry (in case you're not already doing this..)

-------------------------

