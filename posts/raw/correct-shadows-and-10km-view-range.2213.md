horvatha4 | 2017-01-02 01:13:58 UTC | #1

Hi Forum!

How can I get correct shadows if I set the cam's far clip to 10km ? ( one unit = 1m )

[img]http://www.pts-club.com/static/HORVATHA4/pics/vl21.png[/img]


If I set the far clip to 500 the shadow is ok.

[img]http://www.pts-club.com/static/HORVATHA4/pics/vl22.png[/img]

I use one zone, one directional light, one cam. Zone's BB -6000,6000

Arpi

-------------------------

jmiller | 2017-01-02 01:13:58 UTC | #2

Hi Arpi,

Maybe some of the methods the sample apps use could help.

// Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
light->SetShadowBias(BiasParameters(0.00025f, 0.5f));
light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));

There may be other useful methods I have not tried, like SetShadowDistance().
[urho3d.github.io/documentation/ ... mbers.html](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_light-members.html)
[urho3d.github.io/documentation/ ... eters.html](https://urho3d.github.io/documentation/HEAD/struct_urho3_d_1_1_cascade_parameters.html)

HTH

-------------------------

horvatha4 | 2017-01-02 01:13:58 UTC | #3

Hi carnalis!
The code is exactly same as stay in the sample programs. This is why I think, I must something more to set up.
[code]
		//*************************************************
		//******** Scene
		//*************************************************
		scene_ = new Scene(context_);
		scene_->CreateComponent<Octree>();
		scene_->CreateComponent<PhysicsWorld>();
		//*************************************************
		//******** Zone
		//*************************************************
		// Create static scene content. First create a zone for ambient lighting and fog control
		Node* zoneNode = scene_->CreateChild("Zone");
		Zone* zone = zoneNode->CreateComponent<Zone>();
		zone->SetAmbientColor(Color(0.15f, 0.15f, 0.15f));
		zone->SetFogColor(Color(0.7f, 0.7f, 0.7f));
		zone->SetFogStart(8000.0f);
		zone->SetFogEnd(10000.0f);
		zone->SetBoundingBox(BoundingBox(-6000.0f, 6000.0f));
		//*************************************************
		//******** Camera / Viewport
		//*************************************************
		cameraNode_ = scene_->CreateChild("Camera");
		Camera *cam = cameraNode_->CreateComponent<Camera>();
		cameraNode_->GetComponent<Camera>()->SetFarClip(10000);
		cameraNode_->SetRotation(Quaternion(0, 0, 0.0f));
		cameraNode_->SetPosition(Vector3(0, 300.0f, 0));
		Renderer* renderer = GetSubsystem<Renderer>();
		SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
		renderer->SetViewport(0, viewport);
		//renderer->SetShadowQuality(ShadowQuality::SHADOWQUALITY_VSM);
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
		light->SetShadowBias(BiasParameters(0.00025f, 0.5f));
		light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));

		procSky_ = new ProcSky(context_);
		Node* procSkyNode = new Node(context_);
		procSkyNode->SetName("ProcSkyNode");
		procSkyNode->AddComponent(procSky_, 4000, Urho3D::CreateMode::LOCAL);
		procSky_->SetLightNode(lightNode);
		procSky_->Initialize();
		procSky_->Update();
		scene_->AddChild(procSkyNode);
[/code]
I tuned some parameters, but currenly I found that, just the cam's clip distance matter.

By the way, thanks the reply!

Arpi

-------------------------

krstefan42 | 2017-01-02 01:14:01 UTC | #4

Maybe the problem is a lack of z-buffer precision. If that's the case, you could try:

-Increasing the camera near clip as much as possible (in general you want the ratio farClip/nearClip to be as small as possible to get good z-buffer precision)
-Adjusting the bias parameters

Otherwise I don't know. It seems weird that increasing the camera far clip would cause the shadows to bug out like that.

-------------------------

cadaver | 2017-01-02 01:14:01 UTC | #5

In recent master there was a bug (brought by the custom projection matrix) that would manifest in deferred rendering, and cause shadow inaccuracy. It's fixed now, so if you were using deferred rendering, I suggest re-testing now.

-------------------------

horvatha4 | 2017-01-02 01:14:03 UTC | #6

Thanks the replies!
The master branch( Urho3D-1.6-Windows-64bit-STATIC-3D11.zip ) is not the same as what is in the github?
I use the github, an I think this is always "fresh"...

Arpi

-------------------------

cadaver | 2017-01-02 01:14:03 UTC | #7

In Urho github project master branch is always the latest development, and releases are tags (and thus already older). If you're already on master and pull frequently you've got the newest code.

-------------------------

horvatha4 | 2017-01-02 01:14:04 UTC | #8

I use github - master branch.  :frowning:

-------------------------

horvatha4 | 2017-01-02 01:14:04 UTC | #9

Please someone make a test for me!
In the standard 19_VehicleDemo sample, set the cam's far clip to 10000 or 15000. The shadow is correct or not?
At me is not:
[img]http://www.pts-club.com/static/HORVATHA4/pics/vl2016090601.png[/img]

Thx

Arpi

-------------------------

cadaver | 2017-01-02 01:14:04 UTC | #10

Not correct in current master. It looks like it's using too much depth bias, or the shadow depth is too inaccurate, which makes the shadow disappear once the vehicle is on the ground. Can check if this is something simple, like incorrect bias auto adjustments.

EDIT: because the clip distance is long, the light "looks" at the scene from very far away (because it must in theory be prepared for 10km long shadow casters) and the depth bias values have a different scale. Try reducing the constant depth bias, or even setting it to zero at first.

-------------------------

cadaver | 2017-01-02 01:14:04 UTC | #11

If you check the master branch now, I added a shadow max. extrusion parameter for directional lights. It defaults to 1000 to prevent large main view far clip from causing bad shadow depth resolution, however it can be increased if you have long shadow distance or tall shadowcasters.

-------------------------

horvatha4 | 2017-01-02 01:14:04 UTC | #12

Thank you very much cadaver!

I set the  constant depth bias to zero and wow! Looks better:

[img]http://www.pts-club.com/static/HORVATHA4/pics/vl2016090602.png[/img]

[code]		light->SetShadowBias(BiasParameters(0.0f, 0.5f));
[/code]

Now there are stripes just around the lights.

Arpi

-------------------------

horvatha4 | 2017-01-02 01:14:06 UTC | #13

To set the render parameter:
[code]
renderer->SetShadowQuality(ShadowQuality::SHADOWQUALITY_SIMPLE_24BIT);
[/code]
give more precise shadows. At the moment this is enought for me.

Another idee is for one light for the terrain and one spotlight for the car (with light masks). Not tested yet.


Arpi

-------------------------

