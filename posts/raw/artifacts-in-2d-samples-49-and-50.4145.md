Dimous | 2018-04-03 12:33:35 UTC | #1

![artifacts|690x350](upload://nPVUziv1G0DkiQdoIVKznUpi72y.jpg)

Is something wrong with spritesheet atlas, my hardware or urho?

-------------------------

Eugene | 2018-04-03 14:56:58 UTC | #2

This is known (but forgotten) issue.
I think that it'd be fixed by calling `TmxFile2D::SetSpriteTextureEdgeOffset` everywhere after loading `TmxFile2D`.

-------------------------

Dimous | 2018-04-03 13:16:46 UTC | #3

That's good to know, thanks!

-------------------------

