thebluefish | 2017-01-02 01:00:34 UTC | #1

So I'm not 100% sure on this, thought I would ask everyone's opinion.

The client connection takes a single Scene to receive the replication. On a server where this scene can be anything from a lobby to a map, what's the best way to handle client-specific logic?

My thought here is to have an attribute on the Scene that tells us the scene type, then the client could read the attribute and assign components to the scene based off its type.

Another idea is to assign "shell" components to the scene that do nothing on the server. Then on the client I register the same components with the full logic. This means that the components act more like an interface on the server, and the client is just filling out the interface. Would this work properly?

Currently I'm handling this by using certain "reserved names" to filter out desired scenes. I like the second idea better because it means less overhead in the client logic (no need to have a special subsystem to handle "loading" local components), but the first may be simpler to implement.

Edit: So I've went with the second idea and the concept seems to be working. I defined a LobbyComponent in my server and the same component in my client. Both have their own independent logic. However I'm a bit puzzled about how information is transferred, I thought the attributes were used to transfer data across. I've defined the following line in both client/server components:

[code]ATTRIBUTE(LobbyComponent, Urho3D::VAR_VARIANTVECTOR, "Rooms", _rooms, Urho3D::VariantVector(), Urho3D::AM_DEFAULT || Urho3D::AM_LATESTDATA);[/code]

I also populated it with some sample data. When I debug the server, it shows the proper elements listed. However the client doesn't appear to be getting the data. If I debug the client, it shows the 1 attribute listed with its proper name. However no data regarding this attribute seems to be propogating from server to client, even if I mark the network update on the server afterwards. On my client, I'm checking this with:

[code]Urho3D::VariantVector vec = this->GetAttribute("Rooms").GetVariantVector();
Urho3D::VariantVector vec2 = this->GetAttribute(0).GetVariantVector();

for (Urho3D::VariantVector::Iterator itr = _rooms.Begin(); itr != _rooms.End(); itr++)[/code]

Yet all 3 show 0 elements. Is this the intended behavior or am I missing something?

-------------------------

cadaver | 2017-01-02 01:00:34 UTC | #2

I can't say what is going wrong in this specific situation, but generally I would reserve the use of Urho3D scenes to the actual gameplay levels/maps. Something like a lobby is probably best implemented with explicit network messages.

EDIT: the AM_LATESTDATA flag is meant for constantly streaming data like positions and velocities. Using it has no other advantage than being able to override/discard older updates even before sending them, but this usually is relevant only for something that changes 10+ times per second.

-------------------------

thebluefish | 2017-01-02 01:00:34 UTC | #3

The reason I used components in this case is due to the way that scene replication is setup.

Given the scenario that a server handles multiple scenes, one for each room/map/etc. I can assign a connection to a new scene to begin replicating that scene over the connection. On the client, there's only 1 scene to receive replication. There's no events or a clear-cut way to know on the client when the server has transitioned the client to a new scene to be replicated.

I'd also prefer to use components for logic because it makes sense that a component handles in-scene logic. I don't see a reason to externally handle the logic when all the data is within the scene already.

-------------------------

izackp | 2017-01-02 01:00:35 UTC | #4

[i]deleted[/i]

I completely misread what you wrote lol. It was a long day yesterday.

-------------------------

thebluefish | 2017-01-02 01:00:35 UTC | #5

I realize the implication of replicating user-specific information. This is purely for scene-wide replicated information. Any user-specific information is already handled via RemoteEvents.

The idea in this case is to have a component attached directly to the Scene to facilitate handling the scene over-all. In this case I have a general LobbyComponent for the sole purpose of synchronizing lobby-wide information.

In your example, I wouldn't even be creating the HUD on the server (why does the server need to know?). Instead I would set attributes on the player nodes such as health that can be read by each client. What I would instead be doing is have a GameComponent to facilitate the actual gameplay. On the server-side, it would simply be there to synchronize general information such as map name, etc..., while on the client the component would be used to tell us "hey this scene is now for gameplay".

How else would you suggest handling a sudden transition from one replicated scene to another? There's no events to tell us "hey the scene is being switched to a new scene". I could rely on my own custom RemoteEvent to tell the client, but how should the client handle that period where a scene is there with suddenly new information but has not yet received the RemoteEvent telling us? We can rely on the information getting there in order, but can't guarantee it.

-------------------------

thebluefish | 2017-01-02 01:00:35 UTC | #6

[quote="cadaver"]I can't say what is going wrong in this specific situation,[/quote]

There appears to have been some sort of bug.

- I pulled the latest version of Urho3D and compiled it.
- I cleaned my projects and compiled them, linking to the latest Urho3D.
- I verified the issue was still there
- I defined a local string variable, and set the attribute on both client and server:
[code]
ATTRIBUTE(LobbyComponent, Urho3D::VAR_STRING, "RoomName", _roomName, "", Urho3D::AM_DEFAULT);
[/code]
- I populated this on the server with mock data
- Suddenly the original non-working attribute started working
- I completely removed the mock string attribute, original attribute is still working

I have no idea why it suddenly started working, especially since I completely cleaned the project after pulling it from Git. However the important thing is that it's working great.

-------------------------

izackp | 2017-01-02 01:00:36 UTC | #7

[quote="thebluefish"]My thought here is to have an attribute on the Scene that tells us the scene type, then the client could read the attribute and assign components to the scene based off its type.?

"hey the scene is being switched to a new scene". I could rely on my own custom RemoteEvent to tell the client, but how should the client handle that period where a scene is there with suddenly new information but has not yet received the RemoteEvent telling us? We can rely on the information getting there in order, but can't guarantee it.
[/quote]

I completely misread what you wrote yesterday. Just ignore everything I said lol

I believe the best way the handle this is to give each scene an unique id then when a player transitions you can say 'player x went to scene 12304'.   Any new information it receives should just sit there until it is needed.  I don't know if urho3d was designed to handle running and replicating multiple scenes, but if it does, then it probably already assigns some form of a unique id to the scene in order for it to figure out what it needs to replicate.

-------------------------

cadaver | 2017-01-02 01:00:36 UTC | #8

Urho doesn't use id's for scenes, rather a client connection is bound to a specific scene simply by pointer. The assumption is that the client is always connected to one scene at a time, therefore there are no scene id's or such transmitted in the replication messages themselves, only a one-time message telling the client (optionally) that it should load a specific scene file. But having different clients in different scenes should be absolutely fine.

-------------------------

thebluefish | 2017-01-02 01:00:37 UTC | #9

It's working beautifully now. By using replicated components, the server is effectively able to handle the state of the client. The server sets the scene component to tell us which state we're in, and the client's component definition then actually handles the states.

In my game example (which I will be releasing freely once finished) has 3 states: login menu, lobby, and game. I use a Subsystem called "Session" which manages the Connection and replicated Scene. It is also responsible for bringing up the login menu if we get disconnected, or removing the login menu if we've connected. A LobbyComponent and GameComponent handles the states when connected to the server. The server-side logic makes sure to update the scene, while the client component handles all user interactions and UI work.

I'm currently working on a fairly unique card game as practice for working with the client-server stuff. I'm hoping to have a solid demo available for everyone in the next few weeks.

-------------------------

