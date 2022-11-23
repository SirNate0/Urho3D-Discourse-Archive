rogerdv | 2017-01-02 01:01:45 UTC | #1

I have been looking for some way to automatize entity creation and any other task that I could from inside editor itself. For example, my first approach to entities was to have another file describing the NPCs in a scene, and perhaps weather. But thats quite crude. My second guess was to use an special naming for NPC nodes, like "entity_NPC FULLNAME", and then load the NPCs from the scene, saving me the hassle of specifying coordinates, etc, which is just marginally less crude. Perhaps attaching ScriptInstances to nodes could be a better solution?
I would like to hear some suggestions  about this issue, so I can improve a bit my design.

-------------------------

hdunderscore | 2017-01-02 01:01:45 UTC | #2

I guess the question is 'why' are you doing it like that?

If you want your NPCs to have NPC behaviour, create a NPC script that handles their behaviour? If you want to be able to take one generic NPC node + components, save the node and instantiate it like a prefab.

-------------------------

rogerdv | 2017-01-02 01:01:46 UTC | #3

the problem is that there are NPCs and NPCs. Some of them are generic, like guards. Others, are unique because they are traders or relevant to quests.

-------------------------

codingmonkey | 2017-01-02 01:01:47 UTC | #4

i think what the best solution is using prefabs, with user vars or(and) scriptinstances. 
at first you create your prefabs (few types) then you just place they on world map.

in prefabs you may place additional nodes-helpers, they may used in scripts. Example: i'm use nodes called "waypoints" for AIBotLogic, bot check these nodes for player.
but if you use helpers sometimes you won't need to move it for some reason, therefore helpers-nodes are not child of active unit-node they places in same layer of hierarchy in some common node for unit and for helpers.

<>prefabNode (origin: is static always)
<><>helpers (origin: in most causes is also static)
<><>characterNode (origin: dynamic)
<><><>Components<...>
<><><>StaticModel<>
<><><>Collisionshape<>
<><><>dynamicHelpers

-------------------------

rogerdv | 2017-01-02 01:01:47 UTC | #5

If I associate an ScriptInstance to a node, this script has access to my app data declarations and variables? I mean, can I access game info created in the app from this script?

-------------------------

codingmonkey | 2017-01-02 01:01:47 UTC | #6

I do not use scripts (I use C ++), but I recently ran into the same problem.

I came up with to make a structure which describes all the objects of the scene that we have to somehow interact. And I'm going to pass this structure in scripts. Thus they will see the whole scene and all objects.

example of my world struct
[code]
typedef struct GameWorld 
{
	struct  
	{
		SharedPtr<Node> node_;
		WeakPtr<Character> character_;
		

	} player;

	struct 
	{
		SharedPtr<Node> node_;
		SharedPtr<Node> TPCNode_;
		WeakPtr<Camera> camera_;
		SharedPtr<Viewport> viewport;
		SharedPtr<RenderPath> effectRenderPath;

		Plane waterPlane_;
		Plane waterClipPlane_;
		SharedPtr<Node> reflectionCameraNode_;

	} camera;


	struct  
	{
		SharedPtr<Node> node_;
		PODVector<Node*> aiWaypoints_;
		SharedPtr<SplinePath> botSplinePath_;
	} flyingBot;


	struct  
	{
		SharedPtr<Node> shipNode_;
		WeakPtr<ScriptShipAI> shipScript_;
		SharedPtr<Node> shipNode2_;
		WeakPtr<ScriptShipAI> shipScript2_;
	
	} flyingShips;

	struct  
	{
			SharedPtr<XMLFile> prefabHitFx1_;
		
	} prefabs;

	struct 
	{
		SharedPtr<Node> node_;
		WeakPtr<ScriptR2Bot> logic_;
	} R2Bot;

} GameWorld; 
[/code]

it define in app class and used
[code]
class GameMain : public Application
{
	OBJECT(GameMain);

public:
	GameMain(Context* context);
	virtual void Start();

protected:
	GameWorld world;
	SharedPtr<Scene> scene_;
...
[/code]

and code of how i initialize this struct
[code]
void GameMain::OtherSetup()
{
	Graphics* graphics = GetSubsystem<Graphics>();
	Renderer* renderer = GetSubsystem<Renderer>();
	ResourceCache* cache = GetSubsystem<ResourceCache>();

	world.player.node_ = scene_->GetChild("playerNode", true);
	world.player.character_ = world.player.node_->CreateComponent<Character>();
	world.camera.TPCNode_ = scene_->GetChild("cam", true);
	world.camera.TPCNode_->CreateComponent<ThirdPersonCamera>();

	//booms
	PODVector<Node*> objects; 
	scene_->GetChildrenWithComponent<StaticModel>(objects, true);
	for (int i=0; i< objects.Size(); ++i)
	{
		Variant name_ = objects[i]->GetVar("type");
		if (name_.GetString() == "boom") 
		{
			ScriptBoom* ns = objects[i]->CreateComponent<ScriptBoom>();
		}
	}

	// botty
	world.flyingBot.node_ = scene_->GetChild("botty", true);
	world.flyingBot.botSplinePath_ = world.flyingBot.node_->GetComponent<SplinePath>();

	Node* aiNode_ = scene_->GetChild("AI", true);
	aiNode_->GetChildren(world.flyingBot.aiWaypoints_);
	for (int i = 0; i < world.flyingBot.aiWaypoints_.Size(); i++) 
	{
		world.flyingBot.botSplinePath_->AddControlPoint(world.flyingBot.aiWaypoints_[i]);
	}

	world.flyingBot.botSplinePath_->AddControlPoint(world.flyingBot.aiWaypoints_[0]);
	world.flyingBot.botSplinePath_->SetSpeed(1.0f);
	world.flyingBot.botSplinePath_->SetControlledNode(world.flyingBot.node_);

	//Ship
	world.flyingShips.shipNode_ = scene_->GetChild("shipNode", true);
	world.flyingShips.shipScript_ = world.flyingShips.shipNode_->CreateComponent<ScriptShipAI>();
	world.flyingShips.shipScript_->SetTarget(world.player.node_);

	world.flyingShips.shipNode2_ = scene_->GetChild("shipNode2", true);
	world.flyingShips.shipScript2_ = world.flyingShips.shipNode2_->CreateComponent<ScriptShipAI>();
	world.flyingShips.shipScript2_->SetTarget(world.flyingBot.node_);
	world.flyingShips.shipScript2_->SetMaxSpeed(5.0f);

	// setup r2bot
	world.R2Bot.node_ = scene_->GetChild("R2Model", true);
	world.R2Bot.logic_ = world.R2Bot.node_->CreateComponent<ScriptR2Bot>();

[/code]

-------------------------

rogerdv | 2017-01-02 01:01:47 UTC | #7

Thanks a lot for sharing your code, I will study it carefully this weekend. Currently the approach Im planning to use, based on your suggestions, is to have "marker" nodes in the scenes, each one having vars with actual entity Id. After loading scene I iterate through nodes, looking for markers, and getting the Ids to let entity manager class create the entities and introduce some randomization in skills and stats for each NPC.

-------------------------

rogerdv | 2017-01-02 01:01:50 UTC | #8

The distintion is in their behaviour. Basic NPCs just wander around or watch a place, relevant NPCs have full dialogs, assign quests, etc. What Im looking for now is some way to assign each one the corresponding set of AI scripts.

-------------------------

thebluefish | 2017-01-02 01:01:50 UTC | #9

I would approach this by creating a Component to handle the entity information.

Say I have an ComponentNPC and ComponentInteractive. The first would store information related to the NPC itself, and would facilitate the AI decision tree, equipment, etc... The latter would store information with regards to interacting with the NPC such as dialog options. If you create these components and attach them to a node that defines your NPC, they can handle all local control of the NPC itself. Components can definitely use fellow components, so these components would compliment your mesh, animations, etc... Basically acting as the "brains".

If you wanted to extend it further, you could add even more components such as the character's inventory. By restricting the information to the component's internal attributes, you can easily serialize/deserialize entire NPCs or other complex entities without some external special handlers. It would also make your code very portable, and you could even compile various components into a central library to be used for various behaviors.

-------------------------

hdunderscore | 2017-01-02 01:01:51 UTC | #10

Another option is to use ScriptInstance/LuaScriptInstance components, which lets you attach scripts as a component directly to a node.

-------------------------

