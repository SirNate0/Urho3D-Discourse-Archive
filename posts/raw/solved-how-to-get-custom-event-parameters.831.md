practicing01 | 2017-01-02 01:03:16 UTC | #1

Edit:  Thanks to Stinkfist from the irc channel for giving me the solution in snippet form, thanks to cadaver for *pointing* me in the right direction:
[code]
SharedPtr<Node> projectile = SharedPtr<Node>(static_cast<Node*>(eventData[P_NODE].GetPtr()));
[/code]

I read [url=http://discourse.urho3d.io/t/solved-how-to-send-my-custom-event-with-sendevent/653/4]this[/url] post but I'm getting a compiler error when trying to get the custom event parameters. Thanks for any help.

[code]
//Defined in a header:

EVENT(E_SCENEOBJECTMOVETOCOMPLETE, SceneObjectMoveToComplete)
{
   PARAM(P_NODE, Node);  //node
}

//Defined in a source file:
...
	VariantMap vm;
	vm[SceneObjectMoveToComplete::P_NODE] = node_; //node_ belongs to a logic component
	SendEvent(E_SCENEOBJECTMOVETOCOMPLETE,vm);
...

//Defined in a source file:
....
	using namespace SceneObjectMoveToComplete;

	SharedPtr<Node> projectile = eventData[P_NODE].Get< SharedPtr<Node> >();
	projectile->SetEnabled(false);
	vectoria_.Push(projectile);

...
[/code]

Compiler Error:
[code]
CMakeFiles/MobileSuitNavitas.dir/SpaceSimulation.cpp.o: In function `SpaceSimulation::OnMoveToComplete(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
SpaceSimulation.cpp:(.text+0x63): undefined reference to `Urho3D::SharedPtr<Urho3D::Node> Urho3D::Variant::Get<Urho3D::SharedPtr<Urho3D::Node> >() const'
collect2: error: ld returned 1 exit status
make[2]: *** [/home/practicing01/Desktop/Programming/MobileSuitNavitas/Bin/MobileSuitNavitas] Error 1
make[1]: *** [CMakeFiles/MobileSuitNavitas.dir/all] Error 2
make: *** [all] Error 2

[/code]

-------------------------

cadaver | 2017-01-02 01:03:17 UTC | #2

There is no Get<> template overload for SharedPtr, so the linker error is expected. Use Variant::GetPtr() which returns a RefCounted pointer safely, by holding a weak pointer to the object internally. The object must be strongly refcounted elsewhere.

-------------------------

