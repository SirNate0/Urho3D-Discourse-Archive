rogerdv | 2017-01-02 01:01:32 UTC | #1

I was planning to spend my vacations next week coding and I have been thinking how to implement at least changing from one scene to another, but I noticed that I havent seen any engine feature that would allow me to trigger an event when clicking an object or reaching some point in the map. So, I guess Im going to need an extra file describing trigger areas or some other mechanism like that. I would like to hear what experiences have other developers about this topic.
The second question is related to scene change. Seems that if I unload an scene all the nodes are destroyed, do I have to recreate all nodes again in the new scene for all the active creatures in that scene?

-------------------------

OvermindDL1 | 2017-01-02 01:01:32 UTC | #2

I would just post a message to the object clicked on, and if anything happens to be listening to that event on that object then that could be the trigger?  Or use a component to act as the trigger, it listens for the message and does whatever is appropriate.

-------------------------

codingmonkey | 2017-01-02 01:01:33 UTC | #3

about of triggers:

setup in editor:
[url=http://savepic.org/6489698.htm][img]http://savepic.org/6489698m.png[/img][/url]

handle events in code:

[code]
void GameMain::SubscribeToEvents()
{
//other subscribes
	SubscribeToEvent(E_NODECOLLISION, HANDLER(GameMain, HandleNodeCollision));
}
[/code]

[code]
void GameMain::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
{
	// Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
	using namespace NodeCollision;

	Node* contact_node = (Node*)eventData[P_OTHERNODE].GetPtr();
	VectorBuffer contacts = eventData[P_CONTACTS].GetBuffer();
	Vector3 pos = contacts.ReadVector3(); // ????? ????????????


	Variant myAttr = contact_node->GetVar("SceneTrigger");
	
	if ( myAttr.GetString() == "WorldA.xml") 
	{
		StaticModel* model  = contact_node->GetComponent<StaticModel>();
		static bool isHasOwnCopy = false;
		SharedPtr<Material> mat;

		if (isHasOwnCopy) 
		{
			mat = model->GetMaterial(0);
		}
		else 
		{
			mat = model->GetMaterial(0)->Clone("RedMaterial");
			model->SetMaterial(0, mat);
			isHasOwnCopy = true;		
		}
		mat->SetShaderParameter("MatDiffColor", Vector4(1.0f,0.0f,0.0f,0.25f));	
	}
}
[/code]

>Seems that if I unload an scene all the nodes are destroyed, do I have to recreate all nodes again in the new scene for all the active creatures in that scene?
i don't do this, but i think you may call Node.Clone() active (what you wish objects) and add it to some PODVector, then you delete old scene and add new you just add objects to new scene from this PODVector of Nodes saved from previous scene. Or other way save these objects to prefabs/tempfiles and load they in new scene with std metods (InstantiateXML).



>an event when clicking an object

you may create you own events and listerning it global or for special node.

[code]
void GameMain::SubscribeToEvents()
{

	//UI
	SubscribeToEvent(E_UIMOUSECLICK, HANDLER(GameMain, HandleControlClicked));

	// MY EVENTS
	SubscribeToEvent("YouMostResetThis", HANDLER(GameMain, HandleYouMostResetThis));

}

void GameMain::HandleYouMostResetThis(StringHash eventType, VariantMap& eventData)
{
	// we get this event every time then user press the button.
	botSplinePath_->Reset();	
}


void GameMain::HandleControlClicked(StringHash eventType, VariantMap& eventData)
{
	// Get control that was clicked
	UIElement* clicked = static_cast<UIElement*>(eventData[UIMouseClick::P_ELEMENT].GetPtr());

	String name = "...?";
	if (clicked)
	{
		// Get the name of the control that was clicked
		name = clicked->GetName();
		//botSplinePath_->Reset();
		SendEvent("YouMostResetThis");
	}	
}
[/code]

-------------------------

