mike7e | 2017-01-02 01:12:42 UTC | #1

Hi,
So I am making a map editor for my game, I am using the following code:

Under HandleUpdate
[code]
	if (input->GetKeyPress(KEY_H)) {
		PaintBrush(Vector3::LEFT, 5);
	}[/code]

the function

[code]void CharacterDemo::PaintBrush(Vector3 center, int radius) {
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	Color pixel = cache->GetResource<Image>("Textures/MAP.png")->GetPixel(1, 1);
	float lightness = pixel.Lightness();
	Color newColor = Color(217, 217, 217);
	cache->GetResource<Image>("Textures/MAP.png")->SetPixel(1000, 1000, Color(500,0,0));

	
	Terrain* terrain = terrainNode->GetComponent<Terrain>();
	terrain->ApplyHeightMap();
	
}[/code]

terrainNode is a public shared pointer
but whenever I press H I get the assertion failed error.
Does anyone know of a way to do this?

Many thanks!

-------------------------

Modanung | 2017-01-02 01:12:42 UTC | #2

Are the terrain Node and Terrain Component created somewhere? Somewhere in your code you should have [i]terrainNode = scene->CreateChild("Terrain")[/i] as well as [i]terrainNode->CreateComponent<Terrain>()[/i]
Also does the log say anything about resources not found? Does you debugger tell you what causes the trouble?

EDIT: It might also be that you cannot set pixels that way.

-------------------------

mike7e | 2017-01-02 01:12:42 UTC | #3

[quote="Modanung"]Are the terrain Node and Terrain Component created somewhere? Somewhere in your code you should have [i]terrainNode = scene->CreateChild("Terrain")[/i] as well as [i]terrainNode->CreateComponent<Terrain>()[/i]
Also does the log say anything about resources not found? Does you debugger tell you what causes the trouble?

EDIT: It might also be that you cannot set pixels that way.[/quote]
The terrain node and component are created in CreateScene(). However if I create the terrain every time I press H, then I can set the pixels that way. So setting the pixels definitely works

-------------------------

Modanung | 2017-01-02 01:12:42 UTC | #4

[quote="mike7e"]So setting the pixels definitely works[/quote]
Right, I think the other case was with a Texture2D not an Image. I am at a loss.

-------------------------

Lumak | 2017-01-02 01:12:42 UTC | #5

[quote]cache->GetResource<Image>("Textures/MAP.png")->SetPixel(1000, 1000, Color(500,0,0));[/quote]

That looks suspicious. The pixel index of 1000 -- is your texture size over 1000? Also,  the Color(500,0,0) eventually gets turned into UInt() and will correct that erroneous value of 500 but the rgb values should be from 0.0f to 1.0f.
By the way, changing the MAP.png image as you're doing has no effect on the terrain.

Edit: damu (I forgot his user name on the forum) wrote up a wiki on terrain - [url]https://github.com/urho3d/Urho3D/wiki/Terrain[/url]

-------------------------

