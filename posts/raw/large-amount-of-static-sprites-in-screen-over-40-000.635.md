Hevedy | 2017-01-02 01:01:47 UTC | #1

Best way to spawn over 200x200(40000) sprites in screen like a map for 2d map like in terraria for example ?
Because the instances not work with the sprites, and no idea in 2d how create this amount of sprites without fps drop.
I see a user resources en the forum "SpriteBatch" but no idea if this is what i need.

-------------------------

aster2013 | 2017-01-02 01:01:47 UTC | #2

Current Render2D component will combine all Drawable2D objects with same material together, But the fill rate is a problem.
You can do a test in Urho2DSprite sample by changing the number to 40000.

-------------------------

Hevedy | 2017-01-02 01:01:47 UTC | #3

[quote="aster2013"]Current Render2D component will combine all Drawable2D objects with same material together, But the fill rate is a problem.
You can do a test in Urho2DSprite sample by changing the number to 40000.[/quote]

Wow fast reply, yes i tested with that i get 55-57fps but i need about ~80fps a realistic amount is about (120x100)*2 layers ~25.000 sprites 16x16 pixels.
The color change affect to the sprites with same material ?
And have performance difference between use a spritesheet or different sprites, are a atlas generated at runtime ?
*I tested this with 25k and got ~100fps this have nice performance.

I need test to create a grid(voxel?) based map some like read from a txt or map or image(with pixels colors) file with 1.000 x 1.000 sprites and no idea because don't see a tutorial in internet about this, the frustum occlusion work fine but no idea about how manage that size of map and the max sprites in screen are that about 25.000.

Have a tutorial or web or something about read from image or txt or json or xml to generate/load into game ?

-------------------------

Hevedy | 2017-01-02 01:01:48 UTC | #4

I created this for test at first:
[code]	
        Array<Node@> spriteNodes;
        const int nChunks = 8;
        Sprite2D@ sGround_a = cache.GetResource("Sprite2D", "Urho2D/World/Ground_a.png"); //16x16 texture
	Sprite2D@ sGrass_a = cache.GetResource("Sprite2D", "Urho2D/World/Grass_a.png");
        if (sGround_a is null)
           return;
        if (sGrass_a is null)
          return;
        int cID = 0;
	for (int cz = 0; cz < nChunks; ++cz)
	{
		for (int cx = 0; cx < nChunks; ++cx)
		{
			cID = cz + cx;
			//Chunk
			for (int z = -16; z < 16; ++z)
			{
				for (int x = -16; x < 16; ++x)
				{
				    Node@ spriteNode = scene_.CreateChild("StaticSprite2D");
					spriteNode.position = Vector3( ((cx * 16) + x) * 0.16f, ((cz * 16) + z) * 0.16f, 0.0f);
					StaticSprite2D@ staticSprite = spriteNode.CreateComponent("StaticSprite2D");
					// Set sprite
					staticSprite.sprite = sGround_a;
					spriteNodes.Push(spriteNode);
				}
			}
		}
	}[/code]
Chunks of (32x32)*(8x8).
I got 50fps without view all sprites

-------------------------

codingmonkey | 2017-01-02 01:01:48 UTC | #5

>i get 55-57fps but i need about ~80fps 
for saving pixel fillrate you need customize geometry for each type of sprite. 
for example: if sprite(image) is like a star with alpha transparency, you needed flat geometry almost like star.
as the result your get more fps then you use sprites with alpha.

-------------------------

Hevedy | 2017-01-02 01:01:48 UTC | #6

[quote="codingmonkey"]>i get 55-57fps but i need about ~80fps 
for saving pixel fillrate you need customize geometry for each type of sprite. 
for example: if sprite(image) is like a star with alpha transparency, you needed flat geometry almost like star.
as the result your get more fps then you use sprites with alpha.[/quote]

I using a simple box without alpha 16x16 pixels at the moment with xml for view pixels
[code]<texture>
    <filter mode="nearest" />
</texture>[/code]
i need config something more ?
And using x2 or x3 zoom, what give best results use a 32x32 textures or use x2 of zoom ?

-------------------------

aster2013 | 2017-01-02 01:01:51 UTC | #7

You can use custom material to render all sprites. Disable alpha blend in custom material. It may be faster.

-------------------------

Hevedy | 2017-01-02 01:01:53 UTC | #8

[quote="aster2013"]You can use custom material to render all sprites. Disable alpha blend in custom material. It may be faster.[/quote]

How or where ? example please.

-------------------------

Hevedy | 2017-01-02 01:02:00 UTC | #9

Today i created a map in Tiled with 4.000x4.000 blocks of 16x16 without alpha and the engine crash at load using the tiled example, and if load a map with 1.000x1.000 blocks load but get about 4-5FPS looks like is calling all without culling.

-------------------------

aster2013 | 2017-01-02 01:02:01 UTC | #10

I have do something make 2d more faster. Now in my PC, Urho2DSprite with 20000 spriters run at FPS 150.
[img]https://raw.githubusercontent.com/aster2013/Readme/master/images/Urho2DSprite.png[/img]

-------------------------

Hevedy | 2017-01-02 01:02:02 UTC | #11

[quote="aster2013"]I have do something make 2d more faster. Now in my PC, Urho2DSprite with 20000 spriters run at FPS 150.
[/quote]
Yep you are the boss. I post here the github [url]https://github.com/urho3d/Urho3D/issues/567[/url]
Now run up to 100.000 sprites at 60 fps
But i need a best documentation because not find the values of variables or some variables of source code for shaders, textures, materials...
And like in the github post add a some type of batch or chunks or some thing of manager for large tmx maps or a how to tutorial.

-------------------------

