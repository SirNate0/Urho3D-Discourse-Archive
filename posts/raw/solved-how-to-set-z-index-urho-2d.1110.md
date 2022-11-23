amit | 2017-01-02 01:05:31 UTC | #1

I Have few static sprite setup like
[code]     Sprite2D* bks = cache->GetResource<Sprite2D>("Urho2D/robot_shuttel.jpg");
    SharedPtr<Node> bksn(scene_->CreateChild("bk"));
    StaticSprite2D* bkss = bksn->CreateComponent<StaticSprite2D>();
//    bkss->SetBlendMode(BLEND_ALPHA);
//    bksn->SetPosition(Vector3(0.0, 0.0, 1));
    bkss->SetSprite(bks);[/code]

and also few animated.

some how z index in not as per order of creation. Any particular way to set z-index

-------------------------

amit | 2017-01-02 01:05:32 UTC | #2

[quote="Sinoid"]Use SetLayer and SetOrderInLayer.[/quote]
works. Thanks

-------------------------

