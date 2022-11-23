practicing01 | 2017-01-02 01:06:21 UTC | #1

Edit: Had to specify -frameWidth and -frameHeight for the SpritePacker tool.  Couldn't get the custom material to work though, the following xml was the material.

[code]
<?xml version="1.0"?>
<material>
	<technique name="Techniques/DiffNormal.xml" />
	<texture unit="diffuse" name="Urho2D/cleric/cleric.png" />
	<texture unit="normal" name="Urho2D/cleric/clericN.png" />
	<parameter name="UOffset" value="1 0 0 0" />
	<parameter name="VOffset" value="0 1 0 0" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="1 1 1 16" />
	<cull value="none" />
	<shadowcull value="none" />
	<fill value="solid" />
    	<depthbias constant="-0.00001" slopescaled="0" />
</material>

[/code]

Hello, the following code doesn't crash but I don't see the sprite after loading.  Thanks for any help.
[code]

    clericSheet_ = main_->cache_->GetResource<SpriteSheet2D>("Urho2D/cleric/clericSheet.xml");

    Node* cleric = modelNode_->CreateChild("cleric");

    StaticSprite2D* clericSprite = cleric->CreateComponent<StaticSprite2D>();

    clericSprite->SetSprite(clericSheet_->GetSprite("cleric_0_0"));

    clericSprite->SetCustomMaterial(main_->cache_->GetResource<Material>("Materials/clericMat.xml"));

[/code]

-------------------------

