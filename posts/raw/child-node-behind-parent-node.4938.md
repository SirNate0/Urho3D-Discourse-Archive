Jbonavita | 2019-02-17 21:58:08 UTC | #1

Give the following code, the child node, spinBtn is displaying behind bottomSpriteNode. Any idea why? 

	Node bottomSpriteNode = scene.CreateChild("StaticSprite2D");
	float halfWidth = Graphics.Width * 0.5f * PixelSize;
	float halfHeight = Graphics.Height * 0.5f * PixelSize;

	// Get sprite
	Sprite2D sprite = ResourceCache.GetSprite2D("Urho2D/BottomLine.png");
	if (sprite == null)
		return;
	
	StaticSprite2D staticSprite = bottomSpriteNode.CreateComponent<StaticSprite2D>();
	staticSprite.Sprite = sprite;
	var size = (sprite.Rectangle.Bottom - sprite.Rectangle.Top)  * PixelSize;
	bottomSpriteNode.Position = (new Vector3(0, -(camera.OrthoSize / 2) + (size / 2), 0));
	
	Node spinNode = scene.CreateChild("StaticSprite2D");            
	Sprite2D spinSprite = ResourceCache.GetSprite2D("Urho2D/SpinBtn.png");
	if (spinSprite == null)
		return;

	staticSprite = spinNode.CreateComponent<StaticSprite2D>();
	staticSprite.Sprite = spinSprite;
	bottomSpriteNode.AddChild(spinNode);            
	size = (spinSprite.Rectangle.Right - spinSprite.Rectangle.Left) * PixelSize;

-------------------------

Jbonavita | 2019-02-18 01:58:54 UTC | #2

Not sure what the problem was but I opened the SpinBtn.png in Photoshop, saved it as SpinBtn2.png and now it works.
Weird...

-------------------------

Jbonavita | 2019-02-18 01:58:47 UTC | #3

So now I'm running into the same issue with a different image. Am I doing something wrong by the way I'm adding the nodes? I would think that they would be displayed in the order they're added.

I really don't like when things work sometimes but not others.

-------------------------

