peter | 2019-05-06 01:42:35 UTC | #1

Hello. I have a project I mainly worked on last year, using Urho3D commit 7b4dab378381d9cd960aef23048e3a74fbac59d9 (latest at the time I started). I've now updated Urho3D and have run into this problem:

SubscribeToEvent(node, E_INTERCEPTNETWORKUPDATE, URHO3D_HANDLER(MyComponent, HandleInterceptNetworkUpdate));
node->SetInterceptNetworkUpdate("Network Position", true);
node->SetInterceptNetworkUpdate(...)
// ...
// void MyComponent::HandleInterceptNetworkUpdate(...) {
String name = event_data[P_NAME].GetString();
// name.Length() == 0

This worked fine before, (name == "Network Position" / "Network Rotation"), now it's not working anymore. Not sure what the problem is. Any advice?

Update: Not sure what was wrong, switched back to version 1.7 instead.

-------------------------

Leith | 2019-04-01 07:42:59 UTC | #2

Although Urho has had its networking updated, this event is sent from Serializable.cpp, line 854.
We can see the attribute name is being set in the event data, so this is quite strange.
The P_SERIALIZABLE field of the event should point to the serializable object in question - you can try casting that to Serializable, and then calling GetAttributeDefault method of that object, passing in the P_INDEX event field to identify which attribute you want. Finally, you can get the name directly from the attribute (name_ member). This is the long way, but it should work.
The only odd thing I can see in your code, which is bothering me, is in the SubscribeToEvent line, you passed in "node", while generally we would pass in "node_", indicating the owner node for the component.

-------------------------

