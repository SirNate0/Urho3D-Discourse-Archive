TrevorCash | 2017-10-12 15:17:11 UTC | #1

Hello, I'm having trouble getting the Save and Load methods in script instances to run.

I have a ScriptInstance component attached to a node I call the "Game Mode Node".  This node is a child of the scene.

From the c++ side I want to call save and load on the "Game Mode Node" and have the Save and Load Methods in the ScriptObject to be called - however they are not.  


C++:
> 	File outFile(context_, "GreatGameTestSave.ggs", FILE_WRITE);
> 	Serializer& serializer = dynamic_cast<Serializer&>(outFile);
> 	
> 
> 	pGameScriptNode->Save(serializer);

Creating the node and script instance:
> pGameScriptNode = scene_->CreateChild();
> 	pGameScriptInstance = pGameScriptNode->CreateComponent\<ScriptInstance>();
> 	pGameScriptInstance->SetScriptFile(context_->GetSubsystem\<ResourceCache>()->GetResource\<ScriptFile>("Scripts/GreatGame/GreatGame.as"));
> 	pGameScriptInstance->SetClassName("GreatGame");

GreatGame.as: (Attached as ScriptInstanceComponent to pGameScriptNode)
>     void Save(Serializer@ serializer){
>         Print("GreatGame Save..");
>         GameMode::Save(serializer);
>     }
>     void Load(Deserializer@ deserializer){
>         Print("GreatGame Load..");
>         GameMode::Load(deserializer);
>     }

-------------------------

weitjong | 2017-10-12 15:21:43 UTC | #2

You may want to study 21_AngelScriptIntegration sample closely as it demonstrates how to execute a script object's method from the C++ side.

-------------------------

TrevorCash | 2017-10-12 15:44:10 UTC | #3

Is there a way that the save and load are invoked automatically in the same way for example Update() and FixedUpdate() are?  From the documentation it sounds as if they should be called automatically from the component serialization event.  

I want to have a node hierarchy below my game script node where if any child node has a script instance, its save/load will be called as a result of the root node's save/load method call.  In tandem with Node.save().

-------------------------

cadaver | 2017-10-12 16:20:35 UTC | #4

Check your Load & Save function signatures to make sure they're what the engine expects. Refer to 18_CharacterDemo & 19_VehicleDemo, which demonstrate saving the camera angle pitch / yaw by the script object.

-------------------------

TrevorCash | 2017-10-12 16:33:12 UTC | #5

Silly Me, The signatures were excepting a handle instead of a reference to the serializer and deserializer.

Should Be:
> void Save(Serializer& serializer){
>     Print("GreatGame Save..");
>     GameMode::Save(serializer);
> }
> void Load(Deserializer& deserializer){
>     Print("GreatGame Load..");
>     GameMode::Load(deserializer);
> }

Thanks Guys.

-------------------------

