GaioGiulioPatrizio | 2017-01-02 01:13:35 UTC | #1

Hi to all again.

i'm having troubles to get/set tiles and decorators in a tilemap.

TILED editor permits to add specific tile decorators on multiple layer(like houses on a terrain) but i can't figure out how to modify them.

In the very specific i'm trying to assign an "house" to a specific cell, but till now i have only succeded in modifying the underlining terrain.

I'll load he tmx file so all can understand(you can use the TileMap Example to open it).

i just want to be able to change houses/farms/rivers on tiles and to know a bit more on how i'm supposed to modify the terrain in a multilayer environment (Documentation is very little on this thing)

Thank to all :slight_smile:


LOADED:
[drive.google.com/file/d/0B4tu5v ... sp=sharing](https://drive.google.com/file/d/0B4tu5vObJ6MkSHJxOXRKR0oxc1E/view?usp=sharing)

-------------------------

Mike | 2017-01-02 01:13:35 UTC | #2

Modifying tiles is now demonstrated in sample #36.
Get the appropiate layer (for example, "Tile Layer 1 (decor)" is on layer #1) and set which sprite you want to draw by selecting the right gid.

-------------------------

GaioGiulioPatrizio | 2017-01-02 01:13:35 UTC | #3

Ok, i see that all elements resides on nodes, but still missing 2 points  :cry: 

1) My map has two tileset textures, but gid allows me to map only on the first one. How can i access the second texture tileset to get sprites?

2) It seems that if the actual layer cell did not already exist, i need to create the actual cell before i can do a sprite assign. How to do that?

to be more precise i'll explain with code, breaking the actual linne of code in parts 

[code]

// this first line gets my actual "decorator tile layer #1" which is correct
map->GetLayer(1)->  
//this line fails if tile was not already containing some "decorators" like for instance an house
                             GetTileNode(x,y)->
// "map->GetTmxFile()->GetTileSprite(1)" seems to be able to access only first tileset texture elements(so terrain, but no decorators)
                                                        GetComponent<StaticSprite2D>()->SetSprite(map->GetTmxFile()->GetTileSprite(1));

[/code] 


Thanks to all, i really appreciate this engine this far  :smiley:

-------------------------

Mike | 2017-01-02 01:13:35 UTC | #4

1) gid is global, it means tilesets are summed. For example if your first tileset has 24 sprites, first sprite of second tileset is gid 26. Actually you don't access textures but sprites in a virtual mega tileset. 
2) yes, nodes are created only if the cell exist in the tmx file. To create new tiles, create a node and assign the appropriate sprite to it

-------------------------

GaioGiulioPatrizio | 2017-01-02 01:13:35 UTC | #5

Perfect
Solved, thanks a lot mike  :smiley:

-------------------------

GaioGiulioPatrizio | 2017-01-02 01:13:35 UTC | #6

Hi again,
i can't find how to add Nodes to a tilemap...
Based on Engine code, it's not possible, i need to add a specific Setter for this precise role in the tilemapLayer2D.

Any idea?

-------------------------

Mike | 2017-01-02 01:13:35 UTC | #7

Don't forget that layer #0 is 100% filled, which means you already have a node for each tile, you just have to change its sprite and set its Urho layer above the highest Tiled layer.

-------------------------

GaioGiulioPatrizio | 2017-01-02 01:13:35 UTC | #8

problem is that i can't access the "nodes_" vector inside tilemapLayer2D to add a newly created node, and as i can undesrtand this is necessary.
At least i can't figure out...
Can you be more specific? :slight_smile:

-------------------------

Mike | 2017-01-02 01:13:36 UTC | #9

You don't need to create a new node, do this in Tiled :
- either use a layer that is 100% filled as I mentioned previously
- or in the layers that you want to modify on-the-fly, create transparent tiles (your 2 tilesheets contain a few empty slots, use them to paint empty tiles):
	* in every empty tile (empty tiles are tiles where you didn't paint anything)
	* or selectively, that way you can control what areas are modifiable or accessible
- then in URHO use GetTileNode() at mouse/touch position and you will find a node, as your tileset is now 100% filled

If you still prefer to create a new node by yourself and push it to nodes_, then yes, you will have to create a setter for this.

-------------------------

