codingmonkey | 2017-01-02 01:00:52 UTC | #1

hi folks, i'm trying to understand - trigger system in urho3d, how it works and how i should use triggers in cpp code?
i made some primitive dungeon level with some kind of walls or floors and two lights in scene. (also scene have a player node with camera...)
[img]http://savepic.org/6335952.jpg[/img]

at last my trying i add a mushrooms to scene, and in mushroom node (gribNode) i also add rigidbody with trigger mark - on,
Now my question, how i can get events or something else like that in code then player hit collision with mushrooms ?

-------------------------

Mike | 2017-01-02 01:00:52 UTC | #2

Hi and welcome,

Depending on your game logic, you can either subscribe your gribNode or your player to "NodeCollision" event. Then in your handler function, you will have access to colliding RigidBodies/Nodes and to the Bullet manifold.
You can check sample #18 for a thorough demonstration.

-------------------------

codingmonkey | 2017-01-02 01:00:53 UTC | #3

Thanks, [b]Mike[/b]! 
I think something happened to make) 
[video]https://www.youtube.com/watch?v=-NdRz8kHmWM[/video]

Also thanks [b]cin[/b] for sample code.
i'am somewhat reworked it and that's what happened

[code]
void UrhoQuickStart::Start()
{
        //other code before
	gribNode_ = scene_->GetChild("GribNode", true);
	SubscribeToEvent(gribNode_, E_NODECOLLISION, HANDLER(UrhoQuickStart, HandleNodeCollision));	
        //and other code behind
}

void UrhoQuickStart::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
{
	using namespace NodeCollision;

	Node* contact_node = (Node*)eventData[P_OTHERNODE].GetPtr();
	VectorBuffer contacts = eventData[P_CONTACTS].GetBuffer();
	Vector3 pos = contacts.ReadVector3(); // ????? ????????????
	Node* cube = scene_->GetChild("Cube", true);
	RigidBody * r = cube->GetComponent<RigidBody>();
	
	r->SetLinearVelocity(Vector3(0,1,0));
	//cube->SetWorldPosition(Vector3(0,2,0));
	

}
[/code]

-------------------------

