jarjar | 2017-01-02 01:13:26 UTC | #1

How do you properly align a Sprite onto a TileMap2D?  I have been trying different ways but nothing is working. If I align the sprite via a fixed position offset alignment to tile 0,0.  When the sprite goes to tile 24,0 it is misaligned by a few pixels regardless.

The tilemap used is from the Urho3D samples. I simply switched it to an orthogonal and disabled the isometric camera to see if that was the problem. The misalignment occurs on both ortho and iso.

Here is an image of the example and some relevant code.

[img]http://i.imgur.com/MfGJwKf.png[/img]

[code]        public static uint CreateSprite(Client client, string name, int x, int y)
        {
            var spriteNode2 = GameState.cur_tileMap.GetLayer(0).GetTileNode(24,24).CreateChild("AnimatedSprite2D");
            //Hardcoded alignment
            spriteNode2.Position = new Vector3(0.32f, 0.20f, 0f);

            AnimatedSprite2D animatedSprite = spriteNode2.CreateComponent<AnimatedSprite2D>();
            // Set animation
            animatedSprite.AnimationSet = GetAnimationSet2D(client, name);
            animatedSprite.SetAnimation("move_up_left", LoopMode2D.Default);
            animatedSprite.Layer = 10;

            return spriteNode2.ID;
        }
[/code]

-------------------------

Mike | 2017-01-02 01:13:29 UTC | #2

The tileset used in sample #36 is not well suited for your purpose, as it uses an offset of 16 pixels, with some tiles designed as 'occluders' and others as 'occludees'.

It becomes obvious when you swap top and bottom tiles (uisng shif+click) and draw debug geometry:

[img]http://imgur.com/t3Mfx2C.jpg[/img] [img]http://imgur.com/1P5n41h.jpg[/img]

You can notice that grass tiles are perfectly aligned, while water tiles are not (leaving some gaps), as they are not offset in the tileset.

Note that sprite hot spot is always bottom-left. Animated sprites position = tile position = tile hot spot.
[b]
In summary, no alignment issue here.[/b]

I cannot reproduce your 'invisible' issue, can you post steps or a sample to reproduce.

-------------------------

