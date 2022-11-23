thebluefish | 2017-01-02 01:00:41 UTC | #1

I'm not sure if this intentional, but it seems that all of the Get functions return const. This makes it impractical to modify the data within the Variant. For example, I store a VariantMap within a VariantVector so that I can transfer arbitrary data between server and client automatically via an Attribute. In order to actually modify the data, I'm forced to run a const_cast. This is ugly and goes against the entire purpose of marking the return call const. Here's the relevant function (that works with const_cast) to give you an idea of how I'm trying to work with it:

[code]
void LobbyComponent::HandlePlayerJoinedRoom(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
{
	using namespace PlayerJoinedRoom;

	Urho3D::Connection* connection = static_cast<Urho3D::Connection*>(eventData[P_CONNECTION].GetPtr());
	Urho3D::Scene* scene = static_cast<Urho3D::Scene*>(eventData[P_ROOM].GetPtr());

	for (Urho3D::VariantVector::Iterator itr = _rooms.Begin(); itr != _rooms.End(); itr++)
	{
		// Ugly const_cast
		Urho3D::VariantMap& map = const_cast<Urho3D::VariantMap&>(itr->GetVariantMap());

		if (map[ATTR_ROOM_ID].GetStringHash() == scene->GetNameHash())
		{
			map[ATTR_NUM_PLAYERS] = scene->GetChild(N_PLAYERS)->GetNumChildren();

			break;
		}
	}

	MarkNetworkUpdate();
}
[/code]

Is there any better ways to do this?

-------------------------

cadaver | 2017-01-02 01:00:42 UTC | #2

I'll take a look if there are ill effects for returning non-const data.

EDIT: There is one. Upon type mismatch the functions return an empty/zero value, which is static. Non-const return value allows to "pollute" this static value if the user goes on modifying it.

-------------------------

cadaver | 2017-01-02 01:00:42 UTC | #3

Turns out Urho3D is so large I don't even remember all the functionality that has already been written :slight_smile:

There already is available non-const access to buffer, variant map and variant vector inside a Variant, but these operate by pointers and they return null on type mismatch. Take a look at:

Variant::GetBufferPtr()
Variant::GetVariantMapPtr()
Variant::GetVariantVectorPtr()

-------------------------

thebluefish | 2017-01-02 01:00:43 UTC | #4

I'm a bit ashamed that I didn't see that. It's pretty much asking for trouble to be using pointers when working with remote events and attributes, so I didn't even consider that as an option.

-------------------------

weitjong | 2017-01-02 01:00:43 UTC | #5

[quote="thebluefish"]It's pretty much asking for trouble to be using pointers when working with remote events and attributes, so I didn't even consider that as an option.[/quote]

Why you think so? When I look at the Variant class header file, I can see those three pointer variants are implemented not much differently than their const <T>& counterparts. The underlying VariantValue is being transmitted similarly either ways.

-------------------------

cadaver | 2017-01-02 01:00:44 UTC | #6

After you nullcheck the returned pointer, you can turn it to a reference with the * operator if you like.

-------------------------

thebluefish | 2017-01-02 01:00:44 UTC | #7

[quote="weitjong"][quote="thebluefish"]It's pretty much asking for trouble to be using pointers when working with remote events and attributes, so I didn't even consider that as an option.[/quote]

Why you think so? When I look at the Variant class header file, I can see those three pointer variants are implemented not much differently than their const <T>& counterparts. The underlying VariantValue is being transmitted similarly either ways.[/quote]

I've ran into problems trying to use pointers with Variants. It's likely that I just need to be careful that I'm transferring the data instead of the pointer, but I've found it easier to work with them as just the data. Personal problem I suppose.

[quote="cadaver"]After you nullcheck the returned pointer, you can turn it to a reference with the * operator if you like.[/quote]

That's what I'm doing so that I can still access the [] operator, otherwise it just doesn't feel as "clean" to be working with VariantMaps differently than how I would in Events.

-------------------------

