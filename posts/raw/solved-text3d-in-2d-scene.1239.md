xotonic | 2017-01-02 01:06:19 UTC | #1

I am trying to draw text over sprite.
Code:
[code]
   SharedPtr<Node> spriteNode(scene_->CreateChild("StaticSprite2D"));
	spriteNode->SetPosition2D(Vector2(0.0f, 0.0f));

	StaticSprite2D* staticSprite = spriteNode->CreateComponent<StaticSprite2D>();
	staticSprite->SetBlendMode(BLEND_ALPHA);
	staticSprite->SetLayer(1);
	staticSprite->SetSprite(sprite);

	Node* textNode = spriteNode->CreateChild();
	textNode->SetPosition2D(Vector2(0.f, 0.f));
	Text3D* titleText = textNode->CreateComponent<Text3D>();
	titleText->SetText("name");
	titleText->SetFont(cache->GetResource<Font>("Fonts/BlueHighway.sdf"), 24);
	titleText->SetColor(Color::WHITE);
[/code]
But nothing happens. I tryed set face camera mode (with all params), text not drawing. 
How to set text in 2d scene correctly?

UPD: I moved node along Z axis. 
[code]
textNode->SetPosition(Vector3(0.f, 0.f, -0.1f));
[/code]
Now text dissappears after camera move :
[spoiler][img]http://i62.tinypic.com/28meemo.gif[/img][/spoiler]

-------------------------

xotonic | 2017-01-02 01:06:20 UTC | #2

I`m stupid. I forgot [code]SetOrthographic(true)[/code]  :smiley: 

Now it`s ok.

-------------------------

