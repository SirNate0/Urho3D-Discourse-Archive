ChunFengTsin | 2018-03-18 09:18:21 UTC | #1

Hello, everyone,
There a problem about cannot replication my own component  when sceneReplication.
In my game, the client and server are  two independent projects .
What I'm going to do is replication a characterNode with a component writing by myself (name is "Character").

First , start server,:
When a client connected, the server create characterNode and Character Component , un-Local.
Next the server call SendRemoteEvent() to send ID of characterNode .

In client ,
Get the characterNode by ID from server.
Up to now, everything is ok.

But when I call Character chara =  characterNode->GetComponent<Character>();
The chara is NULL...

Note: chara->MarkNetworkUpdate() has been called on  HandlePhysicsPerStep(), server side.

 Is this a typical mistake? 
Or someone know about that.
Thanks.

-------------------------

Sinoid | 2018-03-18 17:05:20 UTC | #2

Is your component registered with the factory system? In more detail: does it have a `MyComponent::Register` static method and are your calling that during engine initialization to register your component type?

If it isn't that'll prevent the other end from being able to deserialize it, though it should give you a torrent of errors.

Components can also be Local only, though the function calls for Node::AddComponent / Node::GetOrCreateComponent prevent goofs.

-------------------------

ChunFengTsin | 2018-03-19 03:55:46 UTC | #3

Thanks, I have registered it , and now it works. :grinning:
But , when I change data of Character Component on server,
The Client haven't change. 
should I use the function:
PrepareNetworkUpdate()
MarkNetworkUpdate()

how to use them correctly, what is the detail of them?

-------------------------

Sinoid | 2018-03-19 04:47:04 UTC | #4

You usually shouldn't need to use those.

Did you also register your component's attributes? Stuff that looks like:

    URHO3D_ACCESSOR_ATTRIBUTE("Is Enabled", IsEnabled, SetEnabled, bool, true, AM_DEFAULT);

You have to fully register everything, first the factory and then the attributes. AM_DEFAULT includes network support.

-------------------------

