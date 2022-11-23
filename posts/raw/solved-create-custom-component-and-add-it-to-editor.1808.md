Lichi | 2017-01-02 01:10:20 UTC | #1

Hi, I need to create a component that i can add to some node and edit the parameters in editor. How i can do it?
(I'm read something about angelscript component but i don't know if it's the same as a node component)
Thanks.
PS: sorry for my english.

-------------------------

thebluefish | 2017-01-02 01:10:21 UTC | #2

Create your Component in C++:

[code]
class Player : public Urho3D::Component
[/code]
-or-
[code]
class Player : public Urho3D::LogicComponent
[/code]

Register it with Urho3D with a category:
[code]
void Player::RegisterObject(Urho3D::Context* context)
{
	context->RegisterFactory<Player>("Game");
}
[/code]

and compile this Component into Urho3D player. Then when you run the modified player, it will be available to edit. Any attributes that you register with the component will show in the attribute panel unless you specify AM_NOEDIT for the attribute.

-------------------------

Lichi | 2017-01-02 01:10:21 UTC | #3

[quote="thebluefish"]Create your Component in C++:

[code]
class Player : public Urho3D::Component
[/code]
-or-
[code]
class Player : public Urho3D::LogicComponent
[/code]

Register it with Urho3D with a category:
[code]
void Player::RegisterObject(Urho3D::Context* context)
{
	context->RegisterFactory<Player>("Game");
}
[/code]

and compile this Component into Urho3D player. Then when you run the modified player, it will be available to edit. Any attributes that you register with the component will show in the attribute panel unless you specify AM_NOEDIT for the attribute.[/quote]

Thanks! :slight_smile:
 I added my custom component to the Urho editor, but when i try to add it to a node i'm get this error: "Could not create unknown component type"

-------------------------

thebluefish | 2017-01-02 01:10:23 UTC | #4

Means you didn't register it.

-------------------------

1vanK | 2017-01-02 01:10:23 UTC | #5

You need component on AngelScrip or C++ ?

-------------------------

Lichi | 2017-01-02 01:10:23 UTC | #6

[quote="thebluefish"]Means you didn't register it.[/quote]
I copied the ragdoll component sample and register it in Urho Player using this line:
[code]context_->RegisterFactory<CreateRagdoll>("Physics");[/code]
I have to add another line?

[quote="1vanK"]You need component on AngelScrip or C++ ?[/quote]
Angelscript i think it's, because i have to be able to edit it in the editor

-------------------------

thebluefish | 2017-01-02 01:10:23 UTC | #7

[quote="Lichi"][quote="thebluefish"]Means you didn't register it.[/quote]
I copied the ragdoll component sample and register it in Urho Player using this line:
[code]context_->RegisterFactory<CreateRagdoll>("Physics");[/code]
I have to add another line?
[/quote]

You need to register your own class. If your Component is named "Test", then it would look like:

[code]
context_->RegisterFactory<CreateRagdoll>("Physics");
[/code]

This needs to be called before the script is loaded. Probably should include it as the very first call in Urho3DPlayer::Setup().

[quote="Lichi"]
[quote="1vanK"]You need component on AngelScrip or C++ ?[/quote]
Angelscript i think it's, because i have to be able to edit it in the editor[/quote]

The editor is made in AS but can use components in C++. It doesn't need to be made in AS.

-------------------------

Lichi | 2017-01-02 01:10:23 UTC | #8

Thanks!!! :smiley:
The error was that you said :slight_smile:

-------------------------

1vanK | 2017-01-02 01:10:23 UTC | #9

[quote="Lichi"]
Angelscript i think it's, because i have to be able to edit it in the editor[/quote]

See Rotator.as. You can connect it to node, and it will rotade

-------------------------

