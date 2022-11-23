kostik1337 | 2018-01-10 07:26:53 UTC | #1

Hello everybody, I am trying to load and display simple orthogonal timlemap, the problem is there are seams between same tiles. Picture below illustrates the problem
![Selection_006|665x500](upload://bPqFi2l7QzsHXwgAiPKGAmGQ6DI.png)
And here is minimalistic sample
https://www.dropbox.com/s/br391ke4pabrimq/test.zip?dl=0
As you can see in sample, those seams desappear and appear again, when you move camera (with wsad). It looks like texture coordinates are moving a bit when you moving camera.
So, I'd like to know, why does this happen and how can I avoid it? One obvious solution is to add 1px border to each tile with the same color as tile, but this looks like hack, and probably won't fix the problem fundamentally.

-------------------------

Modanung | 2018-01-10 10:51:05 UTC | #2

This doesn't work? ;)
https://discourse.urho3d.io/t/sprite-texture-nearest-neighbour-filtering/3422/4?u=modanung

I'd look at the map and tiles, but I'm not creating a Google account to download a file.

-------------------------

kostik1337 | 2018-01-10 11:03:39 UTC | #3

[quote="Modanung, post:2, topic:3931"]
This doesn’t work? :wink:
[/quote]
Unfortunately, no, this makes no effect. I tried setting different filtering and address modes, they don't seem to effect too.

[quote="Modanung, post:2, topic:3931"]
I’d look at the map and tiles, but I’m not creating a Google account to download a file.
[/quote]
Huh? Dropbox doesn't require you to have google account, just press "No thanks" button at the bottom.

-------------------------

Eugene | 2018-01-10 11:18:36 UTC | #5

If sprite vertices are aligned and texture is good, there shan't be any seams between. I saw similar problems in sample games, will investigate it later.

-------------------------

kostik1337 | 2018-01-10 11:29:40 UTC | #6

Thanks. Also, i forgot to mention - if camera zoom is integer, those seams seem to be constant, moving camera does not affect them.

-------------------------

kostik1337 | 2018-01-10 15:27:15 UTC | #7

I've done some research, and first off, Modanung was right. Changing filtering to nearest really fixed the problem on that map. My apologies, I should've tested it before.

But I've got similar problem on another map, and here it does not helps. More correct, it helps a bit, those seams appear quite rarely, but they are. This is what it looks like:

![image|640x500](upload://m8Mj7Vh32ElICUKl3eZYhmAGbG3.png)

Also, I've updated dropbox archive with new map.

I tried to place sprites on the scene by hand without TileMap, like this:

    Node@ spritesNode = scene_.CreateChild();
    Texture2D@ texture = cache.GetResource("Texture2D", "grass9.png");
    Sprite2D@ sprite = Sprite2D();
    sprite.texture = texture;
    sprite.rectangle = IntRect(32, 32, 64, 64);
    Sprite2D@ sprite2 = Sprite2D();
    sprite2.texture = texture;
    sprite2.rectangle = IntRect(128, 32, 160, 64);

    for (int r = 0; r< 50; ++r) {
        for (int i = 0; i< 50; ++i) {
            Node@ spriteNode = spritesNode.CreateChild("StaticSprite2D");
            spriteNode.position2D = Vector2(i * 32 * PIXEL_SIZE, r * 32 * PIXEL_SIZE);

            StaticSprite2D@ staticSprite = spriteNode.CreateComponent("StaticSprite2D");
            staticSprite.sprite = (r+i)%6 < 3 ? sprite : sprite2;
        }
    }
and problem stayed, so I believe, vertices are aligned and texture is OK.

Is there anything I should try?

-------------------------

Eugene | 2018-01-10 15:32:18 UTC | #8

[quote="kostik1337, post:7, topic:3931"]
More correct, it helps a bit, those seams appear quite rarely, but they are. This is what it looks like:
[/quote]

_This_ looks like bad texture. You just have dirty brown tile data.
Are these seams 100% visible?

-------------------------

kostik1337 | 2018-01-10 15:37:57 UTC | #9

Can you elaborate, please? What do you mean at bad texture - a broken texture?
And what do you mean at 100% visible, you mean they are not transparent?

-------------------------

Eugene | 2018-01-10 15:44:02 UTC | #10

[quote="kostik1337, post:9, topic:3931"]
Can you elaborate, please? What do you mean at bad texture - a broken texture?
[/quote]

I mean that this "seam" isn't program defect. It's the defect of sprite data. The leftmost column of pixels of brown sprite is grass.

[quote="kostik1337, post:9, topic:3931"]
And what do you mean at 100% visible, you mean they are not transparent?
[/quote]
I mean you always see these seams regardless of camera position, resolution and so on.

-------------------------

kostik1337 | 2018-01-10 16:19:39 UTC | #12

> The leftmost column of pixels of brown sprite is grass.

No, the brown sprite size is exactly 32x32 pixels, grass belongs to another tile. In Tiled tilemap looks OK.

> I mean you always see these seams regardless of camera position, resolution and so on.

No, they appear sometimes, rather infrequently, when you move camera.

-------------------------

Eugene | 2018-01-10 16:27:11 UTC | #13

[quote="kostik1337, post:12, topic:3931"]
No, they appear sometimes, rather infrequently, when you move camera.
[/quote]

That sucks...
If you have fixed and valid sprite texture coords, it _must_ look the same regardless of camera position. Could you scale it e.g. twice? To ensure that all texels are shown as 2x2 pixels.

-------------------------

Modanung | 2018-01-10 17:11:26 UTC | #14

[quote="Eugene, post:13, topic:3931"]
Could you scale it e.g. twice?
[/quote]

The line glitches stay visible here after dividing the camera's ortho size by two, doubling it's zoom or scaling the map's node.
To me they do seem part of the neighbouring tiles (in the set) though. Using the `-tf 0` option, btw.

-------------------------

orefkov | 2018-01-11 17:02:31 UTC | #15

Do you see https://discourse.urho3d.io/t/cannot-get-rid-of-lines-around-staticsprite2d/3798/6 ?
Perhaps it is the same problem and solution.

-------------------------

Eugene | 2018-01-12 09:04:00 UTC | #16

I inveestigated your issue.
`Sprite2D` has tune parameter `edgeOffset_` that is used to avoid edge bleeding.
Tile map doesn't use it in any way, but it definetely should.
Unfortunatelly, `Sprite2D` is _resource_ and `TmxFile2D` that creates it is resource too.
So you couldn't just add new paramter to some component.

Solutions:

- Hard-code constant in `TmxFile2D`
- Put some extra data into `TmxFile2D`
- Add an ability to change the constant at the level of `StaticSprite2D` and so expose it into `TileMap2D`

-------------------------

kostik1337 | 2018-01-12 09:09:05 UTC | #17

Wow! Works perfectly, big thanks!
I've googled a bit about texture bleeding, and as I can see, edgeOffset of 0.5 is perfect. So, my temporary workaround is:

    void SetTextureEdgeOffsetRecursively(Node@ n) {
        Node@[]@ children = n.GetChildren();
        for (uint i=0; i < children.length; ++i) {
            if (children[i].HasComponent("StaticSprite2D")) {
                StaticSprite2D@ staticSprite = children[i].GetComponent("StaticSprite2D");
                staticSprite.sprite.textureEdgeOffset = 0.5;
            }
            SetTextureEdgeOffsetRecursively(children[i]);
        }
    }

I think, I'll put extra data into TmxFile2D an make a PR

-------------------------

