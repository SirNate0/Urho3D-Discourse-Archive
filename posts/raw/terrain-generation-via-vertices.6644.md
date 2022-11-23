evolgames | 2020-12-29 16:52:16 UTC | #1

Didn't see a thread on this, just other terrain generation techniques.
I'd like to create a terrain by feeding vertices via code. I did this in another engine with some gaussian noise maths and it worked, but that was creating a basic 3d model, not a terrain object or heightmap.
In U3d, is there any way to make the terrain object besides the heightmap?
Would it make sense to generate in code the heightmap image data from my vertex generation function?
Or, would it make more sense to create a custom geometry object from the vertices and use that object as the terrain? (Not sure if there is a performance difference between a large custom geometry model and terrain)
Terrain will be large, around 2000x2000 or so.
Which method makes sense for this?

-------------------------

Eugene | 2020-12-29 23:56:10 UTC | #2

[quote="evolgames, post:1, topic:6644"]
In U3d, is there any way to make the terrain object besides the heightmap?
[/quote]
Nope, unless you rewrite `Terrain`.
I would suggest to make array of custom StaticModel-s if you want to make terrain from scratch yourself.
You will have to handle LODs on your own tho.

-------------------------

evolgames | 2020-12-30 18:57:52 UTC | #3

Cool, good to know. I'll give that a try, thanks.

-------------------------

