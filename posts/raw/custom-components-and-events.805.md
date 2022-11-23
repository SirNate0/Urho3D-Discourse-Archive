sabotage3d | 2017-01-02 01:03:01 UTC | #1

Hi guys ,
Is there a simple example on how to create custom components and events in C++ . 
For example if I am to send an event "hit" to a group of objects changing their color to red for a few seconds.

-------------------------

jmiller | 2017-01-02 01:03:02 UTC | #2

One example of a custom event:
[topic660.html#p3610](http://discourse.urho3d.io/t/solved-how-to-send-my-custom-event-with-sendevent/653/3)

Sample 13_Ragdolls has a custom component:
[github.com/urho3d/Urho3D/blob/m ... eRagdoll.h](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/13_Ragdolls/CreateRagdoll.h)
[github.com/urho3d/Urho3D/blob/m ... agdoll.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/13_Ragdolls/CreateRagdoll.cpp)

Your component's OnNodeSet() can subscribe to your custom event, etc.

Remember to register your component before trying to instantiate it  :mrgreen: 

That sample does it in the Application's constructor:
context->RegisterFactory<CreateRagdoll>();

-------------------------

sabotage3d | 2017-01-02 01:03:02 UTC | #3

Thanks but I was thinking for a simpler example that shows the combination of components and events .

-------------------------

