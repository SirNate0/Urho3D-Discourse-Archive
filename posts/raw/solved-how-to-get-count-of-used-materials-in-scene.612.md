codingmonkey | 2017-01-02 01:01:39 UTC | #1

hi folks!

I'am create some hit fx with flare fx and after that smoke fx. 
[video]https://www.youtube.com/watch?v=cruJQ8F-1Ik[/video]

then flare fx end's his life it produce smoke fx. 
and in this smoke fx i'am do - StaticModel.GetMaterial(0).Clone() base material of smoke prefab for private animation state for each instant of smoke fx in scene.
in this case i'm curious how it manages with temporarily cloned material, they also deleted then smoke deleted? ( SmokeNode.Remove() )

for test this i'm want count of all materials in scene then i'm fire(create a lot instances of hit fx)

some code of that

Flare 
[code]
void ScriptHitFx::Start()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	maxLifeTime = 0.25f; // ???????
	currentLifeTime_ = 0.0f;

	scaleAnim_ = SharedPtr<ValueAnimation>(new ValueAnimation(context_));

	float startSize = 0.5f;
	float endSize = 1.0f;

	scaleAnim_->SetKeyFrame(0.0f, Vector3(startSize, startSize, startSize));
	scaleAnim_->SetKeyFrame(0.25f, Vector3(endSize, endSize*2, endSize));
	
	GetNode()->SetScale(startSize);
	GetNode()->SetAttributeAnimation("Scale", scaleAnim_, WM_LOOP);

	prefabSmokeFx_ = cache->GetResource<XMLFile>("Objects/SmokeFx.xml");
	

}

void ScriptHitFx::Update(float timeStep) 
{
	
}

void ScriptHitFx::FixedUpdate(float timeStep)
{
	if (currentLifeTime_ > maxLifeTime) 
	{
		//Node* player = GetScene()->GetChild("playerNode", true);
		
		

		Vector3 pos = GetNode()->GetWorldPosition();
		Vector3 playerPos = player->GetWorldPosition();

		Quaternion quat;
		quat = GetNode()->GetRotation();
		
		
		smokeFX_= SharedPtr<Node>(GetNode()->GetScene()->InstantiateXML(prefabSmokeFx_->GetRoot(), pos, quat, LOCAL));
		smokeFX_->CreateComponent<ScriptSmokeFx>();

		GetNode()->Remove();
	}

	currentLifeTime_ += timeStep;
}
[/code]


Smoke Start Script
[code]

class ScriptSmokeFx : public LogicComponent 
{
	OBJECT(ScriptSmokeFx);
public:
	/// Construct.
	ScriptSmokeFx(Context* context);

	/// Register object factory and attributes.
	static void RegisterObject(Context* context);
	virtual void Start();
	void Update(float timeStep);
	virtual void FixedUpdate(float timeStep);

	float maxLifeTime;

private:
	float currentLifeTime_;
	SharedPtr<ValueAnimation> scaleAnim_;
	SharedPtr<ValueAnimation> factorAnim_;
	SharedPtr<ValueAnimation> colorAnim_;

	SharedPtr<Material> mat_;
};

void ScriptSmokeFx::Start()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	maxLifeTime = 1.0f; // ???????
	currentLifeTime_ = 0.0f;

	scaleAnim_ = SharedPtr<ValueAnimation>(new ValueAnimation(context_));

	float startSize = 1.0f;
	float endSize = 3.0f;

	scaleAnim_->SetKeyFrame(0.0f, Vector3(startSize, startSize, startSize));
	scaleAnim_->SetKeyFrame(maxLifeTime, Vector3(endSize, endSize, endSize));

	GetNode()->SetScale(startSize);
	GetNode()->SetAttributeAnimation("Scale", scaleAnim_, WM_LOOP);

	StaticModel* model = GetComponent<StaticModel>();

#if 1
	mat_ = model->GetMaterial(0)->Clone("");
#else
	mat_ = model->GetMaterial(0);
#endif

	// alpha factor
	factorAnim_ = SharedPtr<ValueAnimation>(new ValueAnimation(context_));
	factorAnim_->SetKeyFrame(0.0f, 0.0f);
	factorAnim_->SetKeyFrame(maxLifeTime / 5.0f, 0.2f);
	factorAnim_->SetKeyFrame(maxLifeTime, 1.0f);
	mat_->SetShaderParameterAnimation("Factor", factorAnim_);
	mat_->SetScene(GetScene());

	// color fade
	colorAnim_ = SharedPtr<ValueAnimation>(new ValueAnimation(context_));
	colorAnim_->SetKeyFrame(0.0f, Vector3(1.0f,1.0f,1.0f));
	colorAnim_->SetKeyFrame((maxLifeTime / 3.0f), Vector3(1.0f,1.0f,1.0f));
	colorAnim_->SetKeyFrame(maxLifeTime, Vector3(0.2f,0.2f,0.2f));
	mat_->SetShaderParameterAnimation("MatDiffColor", colorAnim_);
	mat_->SetScene(GetScene());

	model->SetMaterial(0,mat_);

}
[/code]

-------------------------

codingmonkey | 2017-01-02 01:01:40 UTC | #2

i get count of material like that

[code]
void GameMain::HandleMouseDown(StringHash eventType, VariantMap& eventData)
{
	// ??????? ?????? )
	using namespace MouseButtonDown;
	int key = eventData[P_BUTTON].GetInt();

	if (key == MOUSEB_LEFT) 
	{
		ResourceCache* cache = GetSubsystem<ResourceCache>();
		PODVector<Material*> matVec;
		cache->GetResources<Material>(matVec);
		int i = matVec.Size();
		t->SetText("material count: " + Urho3D::String(i)); // = 26 
	}
}
[/code]

but count of materials does not increase then i'm shuting (create instances of hit fx). it everytime = 26
why? cloned material with metod - material.Clone("new name") does not added to pool of all materials ?

at last, if new cloned material like a ghost for ResourceCache, how i may delete or free this cloned material at the end of life of my hitfx ?

-------------------------

cadaver | 2017-01-02 01:01:41 UTC | #3

Cloned materials don't automatically go to ResourceCache. In this case they will be destroyed when the object using them is destroyed. If you want, you can set a name to the clone and add it to the cache by calling ResourceCache::AddManualResource().

-------------------------

codingmonkey | 2017-01-02 01:01:42 UTC | #4

??, i'm understand.
is this right way to remove the node with components from it's own script ?

i have fx.node with <script> component and other components.
onUpdate event I check lifetime of fx.node in his <script> component,   
and if it alredy old <script> remove self parent object. 
you know it's like a broken logic style or something like that.

[quote]If you want, you can set a name to the clone and add it to the cache by calling ResourceCache::AddManualResource().[/quote]
No, this is not necessary.
cloned material needed only for the time until the effect exists. it's very short time 1-2 sec.
I was afraid that there might be a memory leak, because i'm clone base mat very often.

-------------------------

cadaver | 2017-01-02 01:01:42 UTC | #5

[quote="codingmonkey"]
is this right way to remove the node with components from it's own script ?
[/quote]
When you call Remove() it should in normal case (if there are no strong refs to the node elsewhere) destroy the node and its components immediately, so that's the way to do it, but make sure you exit the function immediately after. After the ScriptSmokeFx component has been destroyed, executing currentLifeTime_ += timeStep is undefined behavior.

-------------------------

codingmonkey | 2017-01-02 01:01:43 UTC | #6

Thank [b]cadaver[/b], I think now the issue is resolved.

-------------------------

