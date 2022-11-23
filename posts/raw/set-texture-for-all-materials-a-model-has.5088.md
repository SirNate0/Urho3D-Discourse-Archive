GodMan | 2019-04-08 00:11:27 UTC | #1

I was trying to figure the best way to set a texture for all materials on a model.

I know you can get one material, and set it like so.

	`Texture2D* concretebubble = cache->GetResource<Texture2D>("Textures/concrete_bubble.tga");`
	`Material* tutorialGround = `cache->GetResource<Material>`("Materials/foun_concrete_orangestripe.xml"); // Was tutorial ground material`
	`tutorialGround->SetTexture(TU_DETAIL, concretebubble);`

But what is the best method, for setting the detail texture for all materials without declaring each material.

-------------------------

Modanung | 2019-04-13 14:42:28 UTC | #2

You could wrap a for-loop into a function that uses the model's `GetNumGeometries()` as the range of the loop along with a naming convention for easy generalisation.

-------------------------

GodMan | 2019-04-13 17:00:09 UTC | #3

Sounds like a good idea. Thanks

-------------------------

