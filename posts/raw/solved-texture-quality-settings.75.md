scorvi | 2017-01-02 00:57:48 UTC | #1

hey,
i have a problem with the Texture quality settings ...  if i edit the settings the background image changes(zooms in or tiled) .... dont know why ? is it a bug or did i do something wrong? 

the background is is created with :
[code]	
       // Create Background sprite and add to the UI layout
	Texture2D* logoTexture = cache->GetResource<Texture2D>("Textures/Background/1_7.png");
	UI* ui = GetSubsystem<UI>();
	backgroundSprite_ = ui->GetRoot()->CreateChild<Sprite>();

	// Set Background sprite texture
	backgroundSprite_->SetTexture(logoTexture);
[/code]
[spoiler][img]http://s4.postimg.org/6ocgjg0qj/screen3.png[/img][/spoiler]

-------------------------

cadaver | 2017-01-02 00:57:48 UTC | #2

UI textures will not react kindly to texture quality settings (mip skipping), as the UI elements define absolute pixel rects which causes the tiling. However, the engine cannot automatically know which textures are used for UI. Put the following parameter XML file alongside your UI image file with just the file extension replaced (for example Textures/Background/1_7.xml), similarly like there exists one for the default UI textures such as Textures/UI.png.

[code]
<texture>
    <mipmap enable="false" />
    <quality low="0" />
</texture>
[/code]

The 'quality low="0"' line tells the engine to never reduce quality.

-------------------------

scorvi | 2017-01-02 00:57:48 UTC | #3

hey,

 thx i will do that ^^

-------------------------

