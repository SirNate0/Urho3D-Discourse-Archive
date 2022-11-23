1vanK | 2017-01-02 01:12:08 UTC | #1

[github.com/1vanK/Urho3DOpenWorld](https://github.com/1vanK/Urho3DOpenWorld)

This is first small test, so source is dirty. If you want to see how are created and destroyed chunks, decrease CHUNK_SIZE and turn off a fog.
At the moment I don't know how will work a phisics.

Perhaps together we can find a good approach for creating games with an open world.

-------------------------

horvatha4 | 2017-01-02 01:13:05 UTC | #2

Hi!

Its a very good idea! Would be nice if we found a common place to share the experiences and codes in Big/Infinity/Super Large Worlds.
Damu start wrote a "Super Large Worlds" article on WIKI.[url]https://github.com/urho3d/Urho3D/wiki/Super%20Large%20Worlds[/url]

I have read your code and get some idea, but currently I use another approach.
Because the World is rarely flat ( :wink: ) I think - we need some terrains on chunks.
[video]https://youtu.be/48uyUfDVeoo[/video]

Arpi

-------------------------

Lumak | 2018-05-01 14:52:15 UTC | #3

Some of us have similar ideas.  I was testing loading terrain in a background thread to see if it was possible and to see how much lag will be attributed to an in-game character to see if it was visibly noticeable.

Here is a video of my testing.  I load two separate terrains in the video. One at the beginning and the other mid way.  Frame rate is shown during the load while I continue to move the character during the loading.

vid
[video]https://youtu.be/2F0-A4Fs7A4[/video]

-------------------------

horvatha4 | 2017-01-02 01:13:05 UTC | #4

@Lumak:
What way have you choosed to background loading? WorkQueue or something other?

-------------------------

Lumak | 2017-01-02 01:13:06 UTC | #5

I didn't use WorkQueue, used the Thread class instead.  Background terrain loading requires several loading stages. For my testing I brought Terrain.cpp and CollisionShape local, and I execute some Terrain processes in the foreground and some in the background. Look through the Terrain class and process things that changes VertexBuffer/IndexBuffer Size()/Data() in the foreground, i.e. E_UPDATE, and process everything else in a background thread.

-------------------------

horvatha4 | 2017-01-02 01:13:58 UTC | #6

@Lumak: How much worth your code? :slight_smile:

I made some experiments around this thema.
A 3x3 Terrain matrix what I use and if maps widths are no more than 64 units then there is no or minimal FPS drop at driving thru map's border.
The cam is always repositioned closer to origin and all map regenerated. All map have a phisics component. My car roll smootly from one map to another.

Arpi

-------------------------

Lumak | 2017-01-02 01:13:58 UTC | #7

My code is worthless  :wink:.  It was just a quick and dirty test code, a proof of concept to load terrain in the background -- loading 257x257 maps, nothing cached.

It's cool that you got smooth loading with your implementation!

-------------------------

horvatha4 | 2017-01-02 01:13:59 UTC | #8

There is nothing special, it can run on any computer. Currently with my program, I can travel virtually my whole country (Hungary). Of course there is no vegetation, clouds, buildings, roads. Nothing there, just the "geo colored" terrain and one car.

Here and on other forum threads was a question: how handle Urho the physics at map switch. It seems excellent :slight_smile:

I recommend again a separated thread or place or anything for Huge/Big/Infinity etc. worlds to collect all infos about this thema.
Almost every game-programmer need level-streaming, procedural sky, clouds, vegetation and so on.

@Lumak: its good to hear that :wink:
Arpi

-------------------------

horvatha4 | 2017-01-02 01:14:06 UTC | #9

Hi Forum!

Here is my solution. Not perfect, but works.
What important is for me and some technical details:
-SRTM3 datas pull in to the program as terrain. 64x64 unit wide terrains in a 5x5 matrix. 90 m is the distance between two terrain sample. 90x64=5760 m one terrain, 5x5760 / 2 = 14400 ~ 14,5 km. 14400 x 1.4142 = ~ 20.3 km
-High visibility distance. Currently 20 km.
-The camera's position is always remapped to near the origin. All terrain then recreated with Phisics. Vehicle moved too.
-I use 'big maps' to hold the actual nearest geo and tex data. These bigmaps updated in a separated thread. The bigmaps generated/prepared from SRTM3 datas before the program start runing. They are generated only once with an another program. They are 1201x1201 pixel wide .png images.
One bigmap is created from four png image into a 2x2 matrix. One geo/tex pair for the actual running program, and one geo/tex pair for the reading thread like a back buffer.
-The program render/update the visible terrains only at the actual frame, and the invisibles at the next frame!  
-Width this technique if I drive over the subborder, I can sense a few frame drop. The total process is about 1/4 s.
The most time expensive function is : terrain_[it]->SetHeightMap(terrainGeoSubImg). 25 ms in my computer.

Sorry but I don't follow the "conventional" Urho code (and other reasons) I give code slices only. So, here is my code!
[code]
//#define START_LATITUDE 45
//#define START_LONGITUDE 16
#define TERRAIN_PATCH_SIZE 8
#define mapW 64//128//256//16//
#define mapWx2 128//256//512//32//
#define mapWp2 32//64//128//8//
#define imgW 1200
#define imgWp2 600
#define imgWp10 120
#define imgWp20 60
#define imgWx2 2400
// = 6372,797 km * 2 * PI = 40041,4644760 km / 360 = 111,2262902 / 1200 = 0,0926885 km = 92.6885 m
//#define EARTH_PERIMETER_360 111226.2902f
#define ONE_MAPCELL_LENGHT 90.0f//92.6885f
#define DELETE_NULL(x)      { if (x) delete x; x = NULL; }
#define FAR_CLIP 20000//15000//11400
#include <Urho3D/...
class BigmapLoader : public Thread, public RefCounted
{
public:
	BigmapLoader(ResourceCache* rc) : Thread() , RefCounted()
		, cache_(rc)
		, fLoadingBigmap_(1.0f)
		, geoBigimg_(0)
		, texBigimg_(0)
		, bigMapExt_Lat(-1)
		, bigMapExt_Lon(-1)
		, centerChanged(false)
	{}
	void ThreadFunction()
	{
		if (!centerChanged)
			return;
		fLoadingBigmap_ = 0.0f;
		for (int zlat = -1; zlat < 1; zlat++)
		{
			for (int xlon = -1; xlon < 1; xlon++)
			{
				String preFilename = "Terrain/", geofilename, texfilename;
				geofilename = "N";
				geofilename += (bigMapExt_Lat + zlat);
				geofilename.Append("E");
				if (bigMapExt_Lon + xlon < 100) geofilename.Append("0");
				geofilename += (bigMapExt_Lon + xlon);
				texfilename = geofilename;
				geofilename.Append("_geo.png");
				texfilename.Append(".png");
				SharedPtr<Image> oneGradGeoImg = cache_->GetTempResource<Image>(preFilename + geofilename);
				SharedPtr<Image> oneGradTexImg = cache_->GetTempResource<Image>(preFilename + texfilename);
				if (oneGradGeoImg && oneGradTexImg) 
				{
					for (int y = 0; y < imgW; y++)// <= ??? 1201
					{
						for (int x = 0; x < imgW; x++)
						{
							unsigned geocol = oneGradGeoImg->GetPixelInt(x, y) & 0x0000FFFF;
							unsigned texcol = oneGradTexImg->GetPixelInt(x, y);
							int px = x + imgW * (1 + xlon), py = y - imgW * zlat;
							geoBigimg_->SetPixelInt( px, py, geocol);
							texBigimg_->SetPixelInt( px, py, texcol);
						}
					}
				}
				else
				{
					for (int y = 0; y < imgW; y++)
					{
						for (int x = 0; x < imgW; x++)
						{
							int px = x + imgW * (1 + xlon), py = y - imgW * zlat;
							geoBigimg_->SetPixelInt( px, py, 0);
							texBigimg_->SetPixelInt( px, py, 0);
						}
					}
				}
				fLoadingBigmap_ += 0.24f;
			}
		}
		fLoadingBigmap_ = 1.0f;
	}
	void UpdateBigMapExt(double newlat, double newlon)
	{
		int	new_bigMapExt_Lat = (int)(newlat / imgW + 0.5),
			new_bigMapExt_Lon = (int)(newlon / imgW + 0.5);
		if (new_bigMapExt_Lon == bigMapExt_Lon && new_bigMapExt_Lat == bigMapExt_Lat)
		{
			centerChanged = false;
			return;
		}
		bigMapExt_Lon = new_bigMapExt_Lon; bigMapExt_Lat = new_bigMapExt_Lat;
		centerChanged = true;
	}
	float			fLoadingBigmap_;
	Image*		geoBigimg_;
	Image*		texBigimg_;
protected:
	ResourceCache*	cache_;
	bool			centerChanged;
	int			bigMapExt_Lat, bigMapExt_Lon;
};

class yourApp : public Application
{
public:
...
	void UpdateTerrainNodes()// called from App's HandleUpdate
	{
		last_lat_ = (int)(carto_lat_ / imgW);// just for UI controll
		last_lon_ = (int)(carto_lon_ / imgW);// just for UI controll
		Vector3 cam_position = cameraNode_->GetPosition();

		if (cam_position.z_ > subborder_)
			//move north
		{
			diff_on_bigmap_lat_ -= mapW;
			carto_lat_ += mapW;
			if (diff_on_bigmap_lat_ < imgW - imgWp2)
			{
				add_this_at_mapchange_lat_ = imgW;
				bMapNeedChange_ = true;
			}
			cameraNode_->Translate(Vector3::BACK * mapW * ONE_MAPCELL_LENGHT, TS_WORLD);
			vehicle_->GetNode()->Translate(Vector3::BACK * mapW * ONE_MAPCELL_LENGHT, TS_WORLD);
			vehicle_->MoveWheelNodes(Vector3::BACK * mapW * ONE_MAPCELL_LENGHT);
			bNodeNeedUpdate_ = true;
		}
		if (cam_position.z_ < -subborder_)
			//move south
		{
			diff_on_bigmap_lat_ += mapW;
			carto_lat_ -= mapW;
			if (diff_on_bigmap_lat_ > imgW + imgWp2)
			{
				add_this_at_mapchange_lat_ = -imgW;
				bMapNeedChange_ = true;
			}
			cameraNode_->Translate(Vector3::FORWARD * mapW * ONE_MAPCELL_LENGHT, TS_WORLD);
			vehicle_->GetNode()->Translate(Vector3::FORWARD * mapW * ONE_MAPCELL_LENGHT, TS_WORLD);
			vehicle_->MoveWheelNodes(Vector3::FORWARD * mapW * ONE_MAPCELL_LENGHT);
			bNodeNeedUpdate_ = true;
		}
		if (cam_position.x_ >  subborder_)
			//move east
		{
			diff_on_bigmap_lon_ += mapW;
			carto_lon_ += mapW;
			if (diff_on_bigmap_lon_ > imgW + imgWp2)//
			{
				add_this_at_mapchange_lon_ = -imgW;
				bMapNeedChange_ = true;
			}
			cameraNode_->Translate(Vector3::LEFT * mapW * ONE_MAPCELL_LENGHT, TS_WORLD);
			vehicle_->GetNode()->Translate(Vector3::LEFT * mapW * ONE_MAPCELL_LENGHT, TS_WORLD);
			vehicle_->MoveWheelNodes(Vector3::LEFT * mapW * ONE_MAPCELL_LENGHT);
			bNodeNeedUpdate_ = true;
		}
		if (cam_position.x_ < -subborder_)
			//move west
		{
			diff_on_bigmap_lon_ -= mapW;
			carto_lon_ -= mapW;
			if (diff_on_bigmap_lon_ < imgW - imgWp2)
			{
				add_this_at_mapchange_lon_ = imgW;
				bMapNeedChange_ = true;
			}
			cameraNode_->Translate(Vector3::RIGHT * mapW * ONE_MAPCELL_LENGHT, TS_WORLD);
			vehicle_->GetNode()->Translate(Vector3::RIGHT * mapW * ONE_MAPCELL_LENGHT, TS_WORLD);
			vehicle_->MoveWheelNodes(Vector3::RIGHT * mapW * ONE_MAPCELL_LENGHT);
			bNodeNeedUpdate_ = true;
		}
		if(bMapLoadRunning_ && bigmapLoader_->fLoadingBigmap_ == 1.0f)// back work finish?
		{
			bigmapLoader_->Stop();
			bMapLoadRunning_ = false;
			ShiftBigTerrainMaps();
			bMapNeedChange_ = false;
		}
		if (bMapNeedChange_)// in the next few frame the bigmaps must change/update/reload
		{
			ReadBigTerrainData();
			bMapLoadRunning_ = true;
		}
		if (bUpdateInvisibleTerrain_)
		{
			BuildInvisibleTerrainNodes();
			bUpdateInvisibleTerrain_ = false;
		}
		if (bNodeNeedUpdate_)
		{
			BuildVisibleTerrainNodes();
			bNodeNeedUpdate_ = false;
			bUpdateInvisibleTerrain_ = true;
		}
	}
...
	bool InitTheWorld()
	{
...
		//*************************************************
		//******** Zone
		//*************************************************
...
		zone->SetFogStart(FAR_CLIP*0.8f);
		zone->SetFogEnd(FAR_CLIP);
		zone->SetBoundingBox(BoundingBox(-6000.0f, 6000.0f));
		//*************************************************
		//******** Camera / Viewport
		//*************************************************
		cameraNode_ = scene_->CreateChild("Camera");
		Camera *cam = cameraNode_->CreateComponent<Camera>();
		cameraNode_->GetComponent<Camera>()->SetFarClip(FAR_CLIP);
		cameraNode_->SetRotation(Quaternion(0, 0, 0.0f));
		cameraNode_->SetPosition(Vector3(0, 300.0f, 0));
		Renderer* renderer = GetSubsystem<Renderer>();
		SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
		renderer->SetViewport(0, viewport);
		renderer->SetShadowQuality(ShadowQuality::SHADOWQUALITY_SIMPLE_24BIT);
		//*************************************************
		//******** Light / Sky
		//*************************************************
		// Create a directional light with cascaded shadow mapping
		Node* lightNode = scene_->CreateChild("MyLightNode");
		lightNode->SetDirection(Vector3(0.3f, -0.5f, 0.425f));
		Light* light = lightNode->CreateComponent<Light>();
		light->SetLightType(LIGHT_DIRECTIONAL);
		light->SetCastShadows(true);
		light->SetSpecularIntensity(0.5f);
		light->SetShadowBias(BiasParameters(0.0f, 0.5f));
		light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));
...
		//*************************************************
		//******** Big Terrain Image
		//*************************************************
		terrainGeoBigImg_[0] = new Image(context_);
		terrainGeoBigImg_[0]->SetSize(imgWx2, imgWx2, 3);
		terrainGeoBigImg_[1] = new Image(context_);
		terrainGeoBigImg_[1]->SetSize(imgWx2, imgWx2, 3);

		terrainTexBigImg_[0] = new Image(context_);
		terrainTexBigImg_[0]->SetSize(imgWx2, imgWx2, 3);
		terrainTexBigImg_[1] = new Image(context_);
		terrainTexBigImg_[1]->SetSize(imgWx2, imgWx2, 3);

		act_BigImg_ = 0,	backBigImg_ = 1;

		for (int y = 0; y < imgWx2; y++)
		{
			for (int x = 0; x < imgWx2; x++)
			{
				terrainGeoBigImg_[act_BigImg_]->SetPixelInt(x, y, 0);
				terrainTexBigImg_[act_BigImg_]->SetPixelInt(x, y, 0);
			}
		}
		bigmapLoader_ = new BigmapLoader(rCache_);
		return true;
	}
	bool BuildTheWorld()
	{
...
		//*************************************************
		//******** Terrain
		//*************************************************
		for (int z = 0; z < 5; z++)
		{
			for (int x = 0; x < 5; x++)
			{
				int it = z * 5 + x;
				float space = mapW * ONE_MAPCELL_LENGHT;
				Vector3 center = Vector3((x - 2)*space, 0, (2 - z)*space);
				terrainNode_[it] = scene_->CreateChild();
				terrainNode_[it]->SetPosition(center);

				terrain_[it] = terrainNode_[it]->CreateComponent<Terrain>();
				terrain_[it]->SetOccluder(true);
				terrain_[it]->SetSpacing(Vector3(ONE_MAPCELL_LENGHT, 256.0f, ONE_MAPCELL_LENGHT));
				terrain_[it]->SetPatchSize(TERRAIN_PATCH_SIZE);

				bBox_[it] = BoundingBox(Sphere(Vector3(center), mapWp2 * ONE_MAPCELL_LENGHT));
			}
		}

		diff_on_bigmap_lat_ = imgW - imgWp10 * last_d_lat_ - imgWp20 + (last_d_lat_ / 5) * imgW;
		diff_on_bigmap_lon_ = imgW + imgWp10 * last_d_lon_ + imgWp20 - (last_d_lon_ / 5) * imgW;

		backBigImg_ = 0;
		ReadBigTerrainData();
		while (bigmapLoader_->IsStarted() && bigmapLoader_->fLoadingBigmap_ < 1.0f)// initial loading. this must wait till finish
			int z = 0;
		bigmapLoader_->Stop();
		backBigImg_ = 1;
		bNodeNeedUpdate_ = true;
		bMapNeedChange_ = false;
		bMapLoadRunning_ = false;
		bUpdateInvisibleTerrain_ = false;
		UpdateTerrainNodes();
...
		CreateVehicle();
		return true;
	}
	void ShiftBigTerrainMaps()
	{
		act_BigImg_ = ++act_BigImg_ & 0x00000001;
		backBigImg_ = ++backBigImg_ & 0x00000001;
		diff_on_bigmap_lat_ += add_this_at_mapchange_lat_;
		diff_on_bigmap_lon_ += add_this_at_mapchange_lon_;
		add_this_at_mapchange_lat_ = add_this_at_mapchange_lon_ = 0;
	}
	void ReadBigTerrainData()
	{
		bigmapLoader_->UpdateBigMapExt(carto_lat_, carto_lon_);
		bigmapLoader_->geoBigimg_ = terrainGeoBigImg_[backBigImg_];
		bigmapLoader_->texBigimg_ = terrainTexBigImg_[backBigImg_];
		bigmapLoader_->Run();
		bigmapLoader_->SetPriority(0x000000FF);
	}
	void BuildVisibleTerrainNodes()
	{
		BoundingBox camBB(cameraNode_->GetComponent<Camera>()->GetFrustum());
		int it = 0;
		for (int z = -2; z < 3; z++)
		{
			for (int x = -2; x < 3; x++)
			{
				if (Intersection::OUTSIDE == camBB.IsInside(bBox_[it]))
				{
					node_out_now_[it] = true;
				}
				else
				{
					node_out_now_[it] = false;
					BuildTerrainNodesCommon(x,z,it);
				}
				it++;
			}
		}
	}
	void BuildInvisibleTerrainNodes()
	{
		int it = 0;
		for (int z = -2; z < 3; z++)
		{
			for (int x = -2; x < 3; x++)
			{
				if (node_out_now_[it] == true)
				{
					BuildTerrainNodesCommon(x,z,it);
				}
				it++;
			}
		}
	}
	void BuildTerrainNodesCommon(int x, int z, int it)
	{
		Image *terrainGeoSubImg, *terrainTexSubImg;
		int
			le = diff_on_bigmap_lon_ + x * mapW - mapWp2,
			to = diff_on_bigmap_lat_ + z * mapW - mapWp2,
			//le = diff_on_bigmap_lon_ + x * mapW - mapW - mapWp2,
			//to = diff_on_bigmap_lat_ + z * mapW - mapW - mapWp2,
			ri = le + mapW + 1, bo = to + mapW + 1;
		terrainGeoSubImg = terrainGeoBigImg_[act_BigImg_]->GetSubimage(IntRect(le, to, ri, bo));
		terrain_[it]->SetHeightMap(terrainGeoSubImg);// <---------------------------- ca. 25ms if mapW is 64;
		terrainTexSubImg = terrainTexBigImg_[act_BigImg_]->GetSubimage(IntRect(le, to, ri, bo));
		SharedPtr<Material> mat = context_->CreateObject<Material>();
		mat->SetTechnique(0, rCache_->GetResource<Technique>("Techniques/Diff.xml"));
		SharedPtr<Texture2D> tex2d = context_->CreateObject<Texture2D>();
		tex2d->SetData(terrainTexSubImg);
		mat->SetTexture(TU_DIFFUSE, tex2d);
		terrain_[it]->SetMaterial(mat);

		CollisionShape* cs = terrainNode_[it]->CreateComponent<CollisionShape>();
		cs->SetTerrain();
		RigidBody* body = terrainNode_[it]->CreateComponent<RigidBody>();
		body->SetCollisionLayer(2);
	}
protected:
...
	const float								subborder_ = mapWp2 * ONE_MAPCELL_LENGHT;
	bool									bMapNeedChange_, bNodeNeedUpdate_, bMapLoadRunning_, bUpdateInvisibleTerrain_;
	int									last_lat_, last_lon_, last_d_lat_, last_d_lon_,
										diff_on_bigmap_lon_, diff_on_bigmap_lat_,
										add_this_at_mapchange_lat_, add_this_at_mapchange_lon_,
										cam_zoom_faktor_;
	float									cam_yaw_, cam_pitch_;
	double								carto_lat_, carto_lon_;
	SharedPtr<Node>						cameraNode_;
	SharedPtr<Input>						input_;
	SharedPtr<TSVehicle>					vehicle_;
	SharedPtr<Scene>						scene_;
	SharedPtr<Image>						terrainGeoBigImg_[2], terrainTexBigImg_[2];
	SharedPtr<Terrain>						terrain_[25];
	SharedPtr<Node>						terrainNode_[25];
	BoundingBox							bBox_[25];
	bool									node_out_now_[25];
	SharedPtr<BigmapLoader>					bigmapLoader_;
	ResourceCache*							rCache_;
	Log*									log_;
};
URHO3D_DEFINE_APPLICATION_MAIN(yourApp)

[/code]

Arpi

*EDIT: I forget the 'bigmap loader' and some important constant and variant to give. Now it is corrected.

-------------------------

Lumak | 2017-01-02 01:14:30 UTC | #10

@horvatha4
Just so you know, the [b]HelperThread class[/b] is what I used for the background terrain loading. The BackgroundProcess() function is written differently for the loader and is state driven, though. That class is in my Urho3D Ocean Sim repository on github.

-------------------------

horvatha4 | 2017-01-02 01:14:32 UTC | #11

@Lumak: Thanks a lot! I will check it!

-------------------------

monkeyface | 2017-01-02 01:15:27 UTC | #12

Did anyone get any further with this? I am going to need something like this soon...

-------------------------

