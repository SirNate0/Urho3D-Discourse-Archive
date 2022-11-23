George | 2017-01-02 01:06:32 UTC | #1

Hi, when adding child node to parent, the engine is not defaulting the child node to the position of the parent node. I can set the local position to zero to fix this but that is not a good solution.

If the above is a feature, then there is the problem below. If I have child node that offset from a parent after sometimes it changes the parent. The child node position is no longer correct and seems to also offset. 

Regards
George

-------------------------

cadaver | 2017-01-02 01:06:32 UTC | #2

There are two ways to add a child as a parent, the first should do what you want.

parent->AddChild() - retains the child's previous local position. If it was 0,0,0 before, it should stay 0,0,0 after.
child->SetParent() - this retains the child's previous world position (calls AddChild() and sets a new position)

About the second issue (child affecting parent) I don't have a clue. Are rigidbodies involved? Please post code that demonstrates the issue.

-------------------------

George | 2017-01-02 01:06:33 UTC | #3

The parent.addchild behaviour is ok.
The child setparent may has bug.


Here is a small example: Conveyor is a component. My original code has bounding box and other check. I have removed them from this example.

[code]
SharedPtr<Conveyor> conveyor = CreateConveyor("Conveyor1", Vector3(0,0,0));

       //Add 100 Jacks nodes onto Conveyor1
	for (int i = 0; i < 100; ++i)
	{
		ResourceCache* cache = GetSubsystem<ResourceCache>();
		SharedPtr<Node> jackNode(scene_->CreateChild("Jack"));
		jackNode->SetPosition(pos + Vector3(0,0, -i*4.0f));

		
		AnimatedModel* modelObject = jackNode->CreateComponent<AnimatedModel>();

		modelObject->SetModel(cache->GetResource<Model>("Models/Jack.mdl"));
		Material *mat = cache->GetResource<Material>("Materials/Jack.xml");

		modelObject->SetMaterial(mat);
		modelObject->SetCastShadows(true);
		jackNode->CreateComponent<AnimationController>();
		conveyor->AddNode(jackNode);
	}


SharedPtr<Conveyor> conveyor2 = CreateConveyor("Conveyor2", Vector3(20, 0, 20));
conveyor->ConnectTo(conveyor2);
	

 SharedPtr<Conveyor> NVuDuMain::CreateConveyor(String name, Vector3 pos)
{

	ResourceCache* cache = GetSubsystem<ResourceCache>();
	SharedPtr<Node> node(scene_->CreateChild("Jack"));

	SharedPtr<AnimatedModel> modelObject (node->CreateComponent<AnimatedModel>());
   SharedPtr<Conveyor> conveyor(  node->CreateComponent<Conveyor>());
   node->SetPosition(pos);
   node->SetName(name);
	modelObject->SetModel(cache->GetResource<Model>("Models/Jack.mdl"));    //Conveyor is a jack :).
	//	modelObject->SetMaterial(cache->GetResource<Material>("Materials/Jack.xml"));
	modelObject->SetCastShadows(true);
	
	VariantVector lstInputs;
	VariantVector lstOutputs;
	Conveyor* mainComponent;
	node->SetVar(VAR_INPUTS, lstInputs);
	node->SetVar(VAR_INPUTS, lstOutputs);

	return conveyor;
}


void Conveyor::Update(float timeStep)
{
	float length = 10.0f;
	Vector3 mPos = node_->GetPosition();
	Vector3 delta = (Vector3::FORWARD*timeStep * speed_);

	//node_->SetRotation(node_->GetRotation()*Quaternion(0, timeStep * 10, timeStep * 10));
	Node* previousNode;
	BoundingBox preBound;
	
	for (int i = 1; i < node_->GetNumChildren(); ++i)
	{
		Node *n = node_->GetChild(i);

		Vector3 childLocalPos = n->GetPosition();
	
		previousNode = node_->GetChild(i - 1);
		Vector3 previousNodePos = previousNode->GetPosition();

		//String modelType = n->GetComponents()[0]->GetTypeName();
					
			if (length_ - childLocalPos.z_ - delta.z_ >= 0)
			{
				n->Translate(delta);
				status_ = Status::Travel;
			}
			else
			{
				n->Translate((Vector3::FORWARD*length_ - childLocalPos));
				this->MoveToNext(n);    //This calls    n->SetParent( conveyor2Node)
			}
		

	}
}[/code]

-------------------------

cadaver | 2017-01-02 01:06:33 UTC | #4

Please show the MoveToNext() function as well, or at least relevant parts of it.

Note that reparenting a child can throw off your child iteration loop, as the child is removed from the child vector and the indices change. To fix, you shouldn't increment the loop index when you reparent a child, but rather run the loop again with the same index.

-------------------------

George | 2017-01-02 01:06:33 UTC | #5

The move to next is below.

[code]bool Element::MoveToNext(Node *node)  //node would be a part can be static or dynamic.
{
	if (this->lstOutput.Size() > 0)
	{
		node->SetParent(lstOutput[0]->GetNode());
		//lstOutput[0]->GetNode()->AddChild(node);
		//node->SetPosition(Vector3(0, 0, 0));
		return true;
	}
	return false;
}[/code]

The Conveyor component inherit the Element class.
You can remove the Element part of the function.
Regards,
George.

-------------------------

cadaver | 2017-01-02 01:06:33 UTC | #6

Verified that SetParent() works as advertised, retains the child node's current world position.

I suggest you investigate the Translate() before SetParent(), does it position the child node where intended, considering that SetParent() shouldn't effectively move it at all? (For example leave out the reparenting and simply stop the child node to its final position)

-------------------------

George | 2017-01-02 01:06:33 UTC | #7

Thanks,
My logic has error. Because I'm using the conveyor logic, which suppose to set the precomputed position of the child when transfer over to the next conveyor.

I think I should make a different control with different logic for transferring the child node over so that it retain the position correctly.

Regards,
George

-------------------------

