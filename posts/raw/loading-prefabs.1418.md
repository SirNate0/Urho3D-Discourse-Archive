sabotage3d | 2017-01-02 01:07:37 UTC | #1

Hi guys,
What is the recommended way of loading prefabs? I have a simple prefab containing AnimatedModel, RigidBody and AnimationController. I am trying to assign it to a player class. Ideally I would like to access the prefab inside the player class by initiating it inside the init function and using the update function to move it around. At the moment I am loading it like this:
[code] Urho3D::WeakPtr<Urho3D::Node> playerNode = _scene->CreateChild("Player");
 Player* player = playerNode->CreateComponent<Player>();
 player->Init();
 player->SubscribeToEvents();

 XMLFile *sceneFile = cache->GetResource<XMLFile>("Prefabs/player.xml");
 playerNode->LoadXML(sceneFile->GetRoot());[/code]

-------------------------

codingmonkey | 2017-01-02 01:07:37 UTC | #2

also you may try - Instantiate() preloaded prefabs (XMLfiles)

// on app starting load prefabs
[code]	struct
	{
		HashMap<StringHash, SharedPtr<XMLFile>> objectsMap;

		SharedPtr<XMLFile> prefabHitFx1_;
		SharedPtr<XMLFile> prefabSmokeFx_;
		SharedPtr<XMLFile> prefabBlackSmokeFx_;
		SharedPtr<XMLFile> prefabFireFx_;
		SharedPtr<XMLFile> prefabBoomFx_;
		SharedPtr<XMLFile> prefabAutogunBullet_;


	} prefabs;

void GameMain::LoadPrefabs() 
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	world.prefabs.prefabHitFx1_ = cache->GetResource<XMLFile>("Objects/hitfx1.xml");
	world.prefabs.prefabSmokeFx_ = cache->GetResource<XMLFile>("Objects/SmokeFx.xml");
	world.prefabs.prefabBlackSmokeFx_ = cache->GetResource<XMLFile>("Objects/BlackSmokeFx.xml");

	world.prefabs.prefabFireFx_ = cache->GetResource<XMLFile>("Objects/prefabFireFx.xml");
	world.prefabs.prefabBoomFx_ = cache->GetResource<XMLFile>("Objects/boom.xml");
	world.prefabs.prefabAutogunBullet_ = cache->GetResource<XMLFile>("Objects/AutogunBullet.xml");

	/*world.prefabs.objectsMap["HIT"] = cache->GetResource<XMLFile>("Objects/hitfx1.xml");
	world.prefabs.objectsMap["SMOKE"] = cache->GetResource<XMLFile>("Objects/SmokeFx.xml");
	world.prefabs.objectsMap["FIRE"] = cache->GetResource<XMLFile>("Objects/prefabFireFx.xml");
	world.prefabs.objectsMap["BOOM"] = cache->GetResource<XMLFile>("Objects/boom.xml");*/
}[/code]

// and then is needed create instance and components for it
[code]		Node* gilza_ = GetScene()->InstantiateXML(gameworld_->prefabs.prefabAutogunBullet_->GetRoot(), pos, quat, LOCAL);
		gilza_->SetWorldScale(Vector3(0.11f, 0.11f, 0.11f));
		LifeTime* lt = gilza_->CreateComponent<LifeTime>();
		lt->SetLifeTime(5.0f)[/code]

-------------------------

sabotage3d | 2017-01-02 01:07:37 UTC | #3

GetScene() gives me null inside my Player class.

-------------------------

jmiller | 2017-01-02 01:07:37 UTC | #4

I have code that goes something like this. In app init:
[code]
  String charTemplateName("Objects/Robot.xml");
  charNode_->LoadXML(cache_->GetResource<XMLFile>(charTemplateName)->GetRoot());
  // Set template name on node.
  charNode_->SetVar("template", charTemplateName);
  character_ = charNode_->CreateComponent<Character>();
  charNode_->CreateComponent<CharacterController>();
[/code]
[code]
void Character::OnNodeSet(Node* node) {
  if (!node) return;

  // Template-specific setup can use this.
  const String templateName(node_->GetVar("template").ToString());

  ResourceCache* cache(GetSubsystem<ResourceCache>());
  PhysicsWorld* physicsWorld(GetScene()->GetComponent<PhysicsWorld>()); // GetScene() works at this point
  // ....
}
[/code]

-------------------------

sabotage3d | 2017-01-02 01:07:37 UTC | #5

Ok so I need to set my Init() to accept reference for the player node in order to use GetScene()? That is the only more apparent difference I can see from my code.

-------------------------

jmiller | 2017-01-02 01:07:37 UTC | #6

I'm using OnNodeSet(), an overridden virtual method of Component base, called automatically when a component is added to a node.
At that point, node_ is already stored, and Component::GetScene() is just { return node_ ? node_->GetScene() : 0; }
In that method one can create other components, subscribe to events, etc., though whether it's an appropriate time for you depends...

-------------------------

sabotage3d | 2017-01-02 01:07:38 UTC | #7

Thanks a lot man I was missing the OnNodeSet(Node* node) it works like a charm now.

-------------------------

sabotage3d | 2017-01-02 01:07:41 UTC | #8

I am getting one weird problem after loading the prefab I can't move the node directly:

I load the prefab inside the OnNodeSet
[code]Urho3D::WeakPtr<Urho3D::Node> _playerNode;
 XMLFile *sceneFile = cache->GetResource<XMLFile>("Prefabs/player.xml");
_playerNode = GetScene()->InstantiateXML(sceneFile->GetRoot(), Vector3(0,0,0), Quaternion(0, 0, 0), LOCAL);

[/code]
I can't set the position of the node like this:
[code]_playerNode->SetPosition(Vector3(0,0,5));[/code]

but I can set it like this:
[code]GetScene()->GetChild("player")->SetPosition(Vector3(0,0,5));[/code]

-------------------------

TikariSakari | 2017-01-02 01:07:41 UTC | #9

I am not sure if this is prefab, since it is whole scene but I have loaded the scene like this:

[code]
	Urho3D::ResourceCache* cache = GetSubsystem<Urho3D::ResourceCache>();
	Urho3D::XMLFile* file = cache->GetResource<XMLFile>(mapName);

	SharedPtr<Node> nod = SharedPtr<Node>(scene_->InstantiateXML(file->GetRoot("scene"), Urho3D::Vector3::ZERO, Quaternion()));

[/code]

Then my xml-file is like this
[code]
<?xml version="1.0"?>
<scene id="1">
	<attribute name="Name" value="" />
	<attribute name="Time Scale" value="1" />
	<attribute name="Smoothing Constant" value="50" />
	<attribute name="Snap Threshold" value="5" />
	<attribute name="Elapsed Time" value="0" />
	<attribute name="Next Replicated Node ID" value="2" />
	<attribute name="Next Replicated Component ID" value="4" />
	<attribute name="Next Local Node ID" value="16777266" />
	<attribute name="Next Local Component ID" value="16777265" />
	<attribute name="Variables" />
	<attribute name="Variable Names" value="" />
	<component type="PhysicsWorld" id="1" />
	<component type="Octree" id="2" />
	<component type="DebugRenderer" id="3" />
	<node id="16777216">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="Scene" />
		<attribute name="Position" value="0 0 -0" />
		<attribute name="Rotation" value="0.707107 0.707107 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables" />
          ...
   </node>
</scene>
[/code]

So I am only loading the node information from the xml-file. I am not sure if this would be same for the prefab though. Sadly though the rotation becomes wrong, so I need to manually rotate the object. Edit: after removing the getchild("node"), the rotation also gets loaded from the xml-file.

-------------------------

sabotage3d | 2017-01-02 01:07:41 UTC | #10

Loading the prefab is not a problem anymore the problem is modifying the node position inside a player class.
Currently I have to use it like this as a temp solution: [code]_player = GetScene()->GetChild("player");[/code]

-------------------------

TikariSakari | 2017-01-02 01:07:41 UTC | #11

Is the Node that you get from the initialize valid as in is it non-null value, because if I remember correctly, unless I gave specificly the Node that I wanted to initialize from the xml, it returned some weird stuff from the initialize.

Since you can get the node from the scene with getchild, it is highly likely that the node you get from the initialize is not the same.

Another thing, well since I am not sure how C++ handles, but there would be implicit conversion from raw pointer to weakptr, which I honestly myself have no idea what it does? Basically you have:

[code]
Urho3D::WeakPtr<Urho3D::Node> playerNode = Urho3D::Node*
[/code]
vs what you want to have is to initialize the weakpointer with the raw pointer:
[code]
Urho3D::WeakPtr<Urho3D::Node> playerNode =  Urho3D::WeakPtr<Urho3D::Node>( Urho3D::Node* )
[/code]
I am not sure does these 2 lines evaluate the same way.

So you could try using raw pointer as the playerNode and see how it works if the life expectation allows it + this way you could actually make sure that the Node* returned is not null. And even if it is null, does the Node have a child that is named player, because for me unless I told the xml-file to initialize the correct node-tag from the xml-file.

Edit2: I think it would help a bit for trying to find what is wrong if you could paste the xml-file or at least some contents from the xml-file to figure out what/where things go wrong. For me, it took me a while to not realize that I actually had another octree from the initialize until I only gave the node-part of my xml to the initialize-function.

-------------------------

sabotage3d | 2017-01-02 01:07:42 UTC | #12

Ok this seems to work now is that the best pactice?
[code]
SharedPtr<XMLFile> sceneFile;
sceneFile = cache->GetResource<XMLFile>("Prefabs/player.xml");
_playerNode  = GetScene()->InstantiateXML(sceneFile->GetRoot(), Vector3(0,0,0), Quaternion(0, 0, 0), LOCAL);
_playerNode->SetParent(GetNode());
_player = GetNode();
[/code]

-------------------------

