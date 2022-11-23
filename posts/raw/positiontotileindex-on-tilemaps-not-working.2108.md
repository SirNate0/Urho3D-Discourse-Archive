GaioGiulioPatrizio | 2017-01-02 01:13:08 UTC | #1

Hi to all,

i have some issues with the function PositionToTileindex on tilemaps...

Here is the code i'm trying to get to work:

[code]

void Urho2DTileMap::HandleControlClicked(StringHash eventType, VariantMap& eventData)
{
	
	Vector3 hitPos;
	Drawable* hitDrawable;
	Graphics* graphics = GetSubsystem<Graphics>();
	Input* input = GetSubsystem<Input>();
	
	IntVector2 pos = input->GetMousePosition();
	Camera* camera = cameraNode_->GetComponent<Camera>();

	Ray cameraRay = camera->GetScreenRay((float)pos.x_ / graphics->GetWidth(), (float)pos.y_ / graphics->GetHeight());
	// Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
	PODVector<RayQueryResult> results;
	RayOctreeQuery query(results, cameraRay, RAY_TRIANGLE, 1000, DRAWABLE_GEOMETRY);
	scene_->GetComponent<Octree>()->RaycastSingle(query);
	if (results.Size())
	{
		RayQueryResult& result = results[0];
		hitPos = result.position_;
		hitDrawable = result.drawable_;

		// Set camera's position
		const TileMapInfo2D& info = tileMap->GetInfo();
		

		int xp = 0;
		int yp = 0;

		
		Vector2 posf = { (hitPos.x_ - tileMap->GetNode()->GetWorldPosition().x_),
			   -((hitPos.y_ - tileMap->GetNode()->GetWorldPosition().y_) ) } ;


		if (!tileMap->PositionToTileIndex(xp, yp, posf))
			return;
		

		for (int i = 0; i < tileMap->GetNumLayers(); i++)
			if (tileMap->GetLayer(i)->GetTileNode(xp, yp) != NULL)
			{
				tileMap->GetLayer(i)->GetTileNode(xp, yp)->Remove();
			}
		return;
	}

}
[/code]

Simply talking, this function is called on a click event that intersects a tilemap. I have used the tilemap example in the urho3d distribution. 
The event fires perfectly and all is working fine until i get to this line..

[code]
if (!tileMap->PositionToTileIndex(xp, yp, posf))
			return;
[/code]

This seems to not convert properly what i pass as arguments. 

posf vector is correctly valorized. 
For the downmost tile (which is the (49.49) on a 50x50 tilemap) posf is about  (63.9 , 068). Map dimension is 128x64 units in Urho.

But function result is "false" and xp and yp variables are -48 and -48 respectively....

If i point something in the middle of the map like tile (24,24) posf is like (65,33) but PosToTileIndex returns false, xp=-22 and yp = -22

at first i thought it was a sign error but clicking on something like tile (0,49) which is the one on leftmost(on screepos (1,32) ) i get again false and xp=-47 and yp=-47 

so this seems not to be a sign problem...

Any idea?
Maybe i'm missing some origin point conversion or convention?


 :confused:

-------------------------

Mike | 2017-01-02 01:13:08 UTC | #2

Have a look [url=https://github.com/urho3d/Urho3D/issues/631]here[/url] for a rough fix. This is not pixel perfect so I've let it as is as a reminder.

-------------------------

GaioGiulioPatrizio | 2017-01-02 01:13:14 UTC | #3

Tried but nothing worked...

I came up with this mathematical solutions that works perfectly. I post it here so if anyone has same problems can find a decent workaround  :laughing: 



Basically i take a mouse click event, get local click position for the tile map and then i project back those local coords to the tile grid to find the specific clicked cell.

[code]


void Urho2DTileMap::HandleControlClicked(StringHash eventType, VariantMap& eventData)
{
	
	Vector3 hitPos;
	Drawable* hitDrawable;
	Graphics* graphics = GetSubsystem<Graphics>();
	Input* input = GetSubsystem<Input>();
	
	IntVector2 pos = input->GetMousePosition();
	Camera* camera = cameraNode_->GetComponent<Camera>();



	Ray cameraRay = camera->GetScreenRay((float)pos.x_ / graphics->GetWidth(), (float)pos.y_ / graphics->GetHeight());
	// Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
	PODVector<RayQueryResult> results;
	RayOctreeQuery query(results, cameraRay, RAY_TRIANGLE, 1000, DRAWABLE_GEOMETRY);
	scene_->GetComponent<Octree>()->RaycastSingle(query);
	if (results.Size())
	{
		RayQueryResult& result = results[0];
		hitPos = result.position_;
		hitDrawable = result.drawable_;

		// Set camera's position
		const TileMapInfo2D& info = tileMap->GetInfo();
		

		int xp = 0;
		int yp = 0;

		
		Vector2 posf = { (hitPos.x_ - tileMap->GetNode()->GetWorldPosition().x_ - info.GetMapWidth() /2 ),
			   ((info.GetMapHeight() - (hitPos.y_ - tileMap->GetNode()->GetWorldPosition().y_) ) ) } ;


		xp = (posf.x_ / (info.tileWidth_/2) + posf.y_ / (info.tileHeight_/2)) / 2;
		
		yp = (posf.y_ / (info.tileHeight_/2) - (posf.x_ / (info.tileWidth_/2))) / 2;
		


		

		for (int i = 0; i < tileMap->GetNumLayers(); i++)
			if (tileMap->GetLayer(i)->GetTileNode(xp, yp) != NULL)
			{
				tileMap->GetLayer(i)->GetTileNode(xp, yp)->Remove();
			}
		return;
	}


[/code]

-------------------------

Mike | 2017-01-02 01:13:15 UTC | #4

PositionToTileIndex() fixed in master and now featured in sample #36.

-------------------------

