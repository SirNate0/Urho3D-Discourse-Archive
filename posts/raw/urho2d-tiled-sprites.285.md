Mike | 2017-01-02 00:59:23 UTC | #1

A simple question, how to make the sprites tiled (repeating texture), for example for a background.

-------------------------

jmiller | 2017-01-02 00:59:24 UTC | #2

Hi Mike,

Sprite2D::SetRectangle? [urho3d.github.io/documentation/a00341.html](http://urho3d.github.io/documentation/a00341.html)
Default texture addressing mode is repeat.
Tiled * 10, centered
[code]
  Sprite2D@ bgs = cache.GetResource("Sprite2D", "Urho2D/Aster.png");
  bgs.rectangle = IntRect(0, 0, bgs.rectangle.width * 10, bgs.rectangle.height * 10);
  Node@ bgNode = scene_.CreateChild("StaticSprite2D");
  bgNode.position = Vector3(0.0f, 0.0f, 0.0f);

  StaticSprite2D@ bgStaticSprite = bgNode.CreateComponent("StaticSprite2D");
  bgStaticSprite.sprite = bgs;
[/code]

-------------------------

aster2013 | 2017-01-02 00:59:24 UTC | #3

@carnalis  Sprite2D::SetRectangle is used to set region in texture.

@ Mike:
Current you can create many StaticSprite as tiled background.
When tile-map added, you can use tile-map to create tiled background.

-------------------------

