mds | 2017-01-02 01:15:04 UTC | #1

Hi guys!
I am newbie in game development and have some questions about tiled support in Urho3d.
I create example with map like this
[img]https://vgy.me/1KE56R.png[/img]
Ant want to implement Y-sorting to fix issue 
[img]https://vgy.me/KFxLDT.png[/img]

But I found some limitations in Urho.
Sprite2D can be ordered in layer, so I cannot sort objects from different layers use only Sprite2D. And cannot find better approach from objects used to implement tiled support.
As possible solution I can get all nodes object and sort them by Y and set order to Z coordinate.
It's okay?

version: 1.6
Thanks.

-------------------------

Mike | 2017-01-02 01:15:04 UTC | #2

I don't know if this is the right approach, but this is how I currently handle it:
- I put my occluders (trees, walls...) on a separate layer in Tiled. You could also use 'Tile' objects for this purpose
- This allows the characters to pass behind the occluders

Now, the characters will always be occluded, which is not good when they stand in front of an occluder. To handle this:
- I put my characters on the same layer as the occluders (layer 10 if using 2 layers, 20 if 3...) : StaticSprite2D::SetLayer(10)
- When the character is moving, I update its order in layer (StaticSprite2D::SetOrderInLayer(10)) to match the current tile's order in layer, which equates to:
y * TileMapLayer2D::GetWidth() + x (x and y are retrieved using TileMapInfo2D::PositionToTileIndex())

-------------------------

miz | 2017-01-02 01:15:19 UTC | #3

The way I'm currently doing this is to have tree tops on their own layer above the player and tree bases on a layer below the player. As long as you put the collision box for the tree in an appropriate place you prevent any visibility of the tree top and bottom being on different layers.

Similarly to Mike, for non tile map sprites i want to pass both in front of and behind each other I do a SetOrderInLayer(100.0-Yposition) in the update loop for each of these sprites.

-------------------------

