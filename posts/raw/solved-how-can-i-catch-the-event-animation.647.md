codingmonkey | 2017-01-02 01:01:51 UTC | #1

Hi,  folks!

I've got a enemy bot and it runs along the ground.
I want to make the effect of the dust particles when it comes feet on the ground.

How can I catch the event animation "run" on the frame:
1. The left leg on the ground (frame = 5)
2. The right foot on the ground (frame = 15)
Running is one whole animation, length of 20 frames

In frames 5 and 15 i'm going Instantiate dustfx prefab in world position of foot-helpers;

-------------------------

Mike | 2017-01-02 01:01:51 UTC | #2

This is demonstrated in NinjaSnowWar. I'l elaborate more on this when I'll get home.

-------------------------

codingmonkey | 2017-01-02 01:01:52 UTC | #3

Actually I did something strange and without events.
I translated the frames into the time.
And check the current time of anim state walk.

if enemy bot in anim_walk_state it call this proc

[code]
void ScriptR2Bot::CheckForEmmitFootSteps(float timeStep) 
{
	static bool emmitFootL = false;
	static bool emmitFootR = false;
	float walkTime = animWalk_->GetTime();

	float timeL = 15.0f / 24.0f;
	float timeR = 5.0f / 24.0f;
	
	if (walkTime > timeL && walkTime < timeL+0.1f) 
	{
			emmitFootL = true;
			emmitFootR = false;
	}

	if (walkTime > timeR && walkTime < timeR+0.1f) 
	{
			emmitFootL = false;
			emmitFootR = true;
	}

	if (timeFromLastFootStep > 0.3f) // delay
	if (emmitFootL == true | emmitFootR == true) 
	{
		Node* camera = gameWorld_->camera.node_;
		Vector3 pos;

		if (emmitFootL)
			pos = footL_->GetWorldPosition();
		else
			pos = footR_->GetWorldPosition();
		
		Vector3 camPos = gameWorld_->camera.node_->GetWorldPosition();
		Quaternion quat;
		quat.FromRotationTo(pos, camPos);
		SharedPtr<Node> smokeFX_ = SharedPtr<Node>(GetNode()->GetScene()->InstantiateXML(gameWorld_->prefabs.prefabSmokeFx_->GetRoot(), pos, quat, LOCAL));
		ScriptSmokeFx* script = smokeFX_->CreateComponent<ScriptSmokeFx>();
		//smokeFX_->SetWorldScale(Vector3::ONE * 0.05f);
		script->SetOrientationToNode(camera);

		timeFromLastFootStep = 0.0f;

	}

	timeFromLastFootStep +=timeStep;	
}
[/code]

-------------------------

weitjong | 2017-01-02 01:01:52 UTC | #4

If you are looking for "animation trigger" example, look at FootSteps.as and Ninja_Walk.xml.

-------------------------

codingmonkey | 2017-01-02 01:01:52 UTC | #5

thanks
i'm loking these examples.
and for fire state i'm trying to make trigger animation like in ninja example - with events.

i'm create file for R2_FIRE.ani name is R2_FIRE.xml
with this text
[code]<animation>
    <trigger time="0.6" type="String" value="RUKA.L.001" />
</animation>[/code]

remark : 0.6 = 15(in this frame must be event) / 25 (all frames in anim fire)

[code]void Start() 
{
...
SubscribeToEvent(node_, E_ANIMATIONTRIGGER, HANDLER(ScriptR2Bot, HandleAnimationTrigger));
...
}

void ScriptR2Bot::HandleAnimationTrigger(StringHash eventType, VariantMap& eventData) 
{
	using namespace AnimationTrigger;
	//EVENT(E_ANIMATIONTRIGGER, AnimationTrigger)
	//{
	//	PARAM(P_NODE, Node);                    // Node pointer
	//	PARAM(P_NAME, Name);                    // String
	//	PARAM(P_TIME, Time);                    // Float
	//	PARAM(P_DATA, Data);                    // User-defined data type
	//}

	AnimationState* as = animModel_->GetAnimationState(StringHash(eventData[P_NAME].GetString()));
	if (as) 
	{
		String name = eventData[P_DATA].GetString();
		Node* bone = node_->GetChild(StringHash(name), true);
	}	
}
[/code]

but in first time this not work, I've been thinking why? And then I thought of why.
At the node to which I Subscribe the event there is no component AnimationMesh

I corrected this place :
SubscribeToEvent([b]GetNode(), [/b]E_ANIMATIONTRIGGER, HANDLER(ScriptR2Bot, HandleAnimationTrigger));
to
SubscribeToEvent([b]node_, [/b]E_ANIMATIONTRIGGER, HANDLER(ScriptR2Bot, HandleAnimationTrigger));

and now everything seems working well

-------------------------

