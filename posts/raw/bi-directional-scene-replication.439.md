thebluefish | 2017-01-02 01:00:23 UTC | #1

Here's something that I've wanted for a while now, but I haven't studied enough on networking to really implement.

Currently we have one-directional scene replication, meaning the server is the ultimate authority. For basic demos, this is fine and all. However by sending controls to the server and waiting for it to update, we're essentially stuck in the Quake days. Now practically any major game incorporates some form of client-side prediction. Some games will let the client be the ultimate authority on the player's character, while other games will attempt to "predict" where the client should be while still adhering to the server's authority.

I would like to have additional options available within the scene to allow client control of certain nodes. I think the way it could work is that a node could have one of 3 states:

[*]NoControl - The same as it currently exists. The server has ultimate authority and this cannot be changed by the client.
[*]SoftControl - Allow the client to update the character locally. The server will still have ultimate authority, and can make corrections to the client-side as necessary.
[*]HardControl - Allow the client to update the character locally. These updates are then sent to the server to propagate to the other clients.

The only downside to this is we would need some way of implementing client-side prediction, keeping track of Scene states and keeping all of the clients up-to-date.

-------------------------

izackp | 2017-01-02 01:00:23 UTC | #2

When you have the client make the decisions you're going to lead into 'conflicts'. Let's say you have 8 different people connected to the server and 2 of them decide the opposite outcome then you end up with a 'conflict'. At this point, they must be resolved which can take some time and extra communication between clients. 

Here's a few things you should definitely read about client prediction:
[developer.valvesoftware.com/wik ... Networking](https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking) (see Lag compensation)
[developer.valvesoftware.com/wiki/Prediction](https://developer.valvesoftware.com/wiki/Prediction)

Overall, what you do is continue the game as normal (if the npc's x velocity is 5 then move the npc by 5) until the server sends you what actually happened. Once you get what happened from the server you need to retroactively apply it to the entity.  This can cause the npc to 'jump'. You can fix this problem by having two separate locations stored for each entity: A graphical location (on screen), and a logical location (where it actually is). The logical location will match the server as best as possible while the graphical location will interpolate the best it can with the logical location.

There is also another technique called command/event/or input buffering.. Where the user's input or (game events) gets placed into a buffer to execute at a future time. The hope is that the delayed execution will give the clients time to read it before it needs it to minimize de-synchronization.

As for how to accomplish this with Urho3D.. I don't know yet. I'm still in the process of reading through the code base.

-------------------------

cadaver | 2017-01-02 01:00:24 UTC | #3

Long ago I experimented with having client control over objects over the network. However, there were following downsides:
- Collision resolution between two player controlled objects is not going to work well on its own
- It opens up possibilities of cheating

There also used to be client prediction in an earlier version of Urho3D, when it used a different physics engine. It actually created a private physics world for rewinding just the local player and applying server corrections over your latest input. But this is not a performance-scalable solution and I don't think it can be done well with Bullet. The reason why the Source and Unreal engines can rather easily perform client prediction is because the player characters don't move using rigid body dynamics, rather they use a "character controller" which essentially moves against a completely static world. In that case rewinding and applying server corrections is easier.

I believe you should be able to implement client->server character updates using remote events or custom network messages; at the moment I'm not convinced Urho should do it for you. I'm definitely aware that lack of client prediction makes Urho's networking system quite not what you'd expect of a professional-grade game engine, however if you figure out how to perform client prediction & rewinds performantly in a rigid body-simulated world, please do tell me :wink:

-------------------------

weitjong | 2017-01-02 01:00:24 UTC | #4

Thanks for the links. After reading the first one, two questions come to my mind.
[ol]
[li] I understand why the server needs to have the authoritative role in maintaining the critical game states to prevent any cheating. What I don't understand is, why does it have to do it alone without taking the advantage of the computing power of the networked clients? For example, can't the server just validating a "hit" claimed by a client as oppose to validating each shoot event/message sent by all the clients to see if they "hit". The bogus "hit" sent by a cheating client would still got caught while the server doesn't have to do that much work. That way, it should not cause serious calculation lags when lots of people are shooting at the same time, right? Not unless they are all cheaters claiming hits all the times :slight_smile:.[/li]
[li] On the flip side of the coin, it briefly mentioned "man-in-the-middle" attack is being foiled by not letting client to alter critical game state. But what if there is a technically inclined cheater who can create a "cheat proxy" that actually listens to all the events/messages in the game world, and in the split second can calculate the precise position of the other player in the cheater vicinity, and send a network package stating the cheater shot in that calculated position. Now, how would the server know the difference and prevent such attack?[/li][/ol]

-------------------------

izackp | 2017-01-02 01:00:24 UTC | #5

I don't fully understand you first question.. If any calculation is done on the client it is exploitable and harder to sync.

In reference to your second question, I believe valves code works something like this (I haven't read the article in a long time):

[code]Client:
shootMessage.startTime = current_frame;
server.send(shootMessage);

Server:
if (shootMessage.startFrame < minimalFrame)
    shootMessage.startFrame = minimalFrame;

Context* thePast = rewindTime(shootMessage.startFrame);
bool successfulHit = thePast.simulateShot(shootMessage.player);
return successfulHit;[/code]

You can send player positions and velocities of where and when the shot occurred. However, you would be letting the client send sensitive data which would need to be checked and verified.

By not sending any sensitive data you turn your client into a 'remote controller'. Where the user executes commands (UP, Down, A, B, Shoot, Move_Left, ect) and the server carries it out.

-------------------------

weitjong | 2017-01-02 01:00:24 UTC | #6

Let's use some some number to explain my first question. Let's say there are 100 clients sending a shoot message. The articles implies the Source engine would need to rewind the time 100 times to check if those shots hit or not. What I am asking is, why not the client also have same same piece of code to perform the same rewind time (to a lesser extend or no need at all as it is close to real time) and check for the hit in a distributed manner. The client's hit result is, of course, non-authoritative and need to be verified by the server again. So, say, 1 out these 100  clients, claims "hit". The server only need to perform the rewind time and check for the hit for this one message only. If the claim is true after validation, the game state is changed otherwise the server sends the correction message to the client. Is there any technical drawback from doing so?

You still do not answer my second question. In this scenario, I imagine a cheater could create a cheat proxy that behaves like a normal client or a 'remote controller' using your own word. It's just that, some of the data that it sends are computer aided. The server must update the world data to all the clients so the client could render every players position. So, the player's position data is easy to come by and the proxy could use that information to make all the fire shot from cheater a bull's eye hit.

-------------------------

cadaver | 2017-01-02 01:00:24 UTC | #7

Yeah, an aimbot or wallhack (render wireframe/transparent) is always a possibility even when using a controller mechanism, but some cheats such as speedhack or shooting infinite times should become impossible. For the first category of cheats, prevention mechanisms exist, but are hard:

- Checksum client's executable and data files for modification. This may become a "hacking arms race" you will likely lose unless you're not a triple-A developer with large resources to spend just on the cheat protection. And if the cheat is a proxy program sitting on another machine, not even checksumming the game client is going to help.
- Do not send the client information it should not have, for example do an occlusion check on server and do not send position for an opponent behind a wall. This naturally takes up processing resources on the server and may not be feasible with higher player counts.

-------------------------

izackp | 2017-01-02 01:00:24 UTC | #8

[quote="weitjong"]Let's use some some number to explain my first question. Let's say there are 100 clients sending a shoot message. ... So, say, 1 out these 100  clients, claims "hit". The server only need to perform the rewind time and check for the hit for this one message only.[/quote]

There wouldn't be 100 clients sending the shoot message (in a client / server architecture). Only the client that is shooting will send the shoot message to the server, then the server essentially forwards it to the other clients, and they try to retroactively apply it.

Cadaver answered your second question.  :smiley:

-------------------------

weitjong | 2017-01-02 01:00:24 UTC | #9

[quote="izackp"][quote="weitjong"]Let's use some some number to explain my first question. Let's say there are 100 clients sending a shoot message. ... So, say, 1 out these 100  clients, claims "hit". The server only need to perform the rewind time and check for the hit for this one message only.[/quote]

There wouldn't be 100 clients sending the shoot message (in a client / server architecture). Only the client that is shooting will send the shoot message to the server, then the server essentially forwards it to the other clients, and they try to retroactively apply it.[/quote]

You are missing my point still. I get that each client sends one message. On the server, there are in total 100 messages that it needs to perform hit test process before updating the game state and sync them to all other clients. My point is why server is designed to carry out the hit test process centrally instead of distributing the test to each client (but, non-authoritatively). Using my example above, isn't it much more efficient to validate just one potential hit claimed by the client instead of doing it 100 times?

@cadaver, thanks for your time to answer my second question.

-------------------------

izackp | 2017-01-02 01:00:24 UTC | #10

Ok I see what you're saying, you want to use the clients to cull out all of the unsuccessful shots and use the server to verify that successful shots were successful once found.

This isn't done because its extremely slow, and would result in laggy gameplay, and complex code.  Extremely slow because the server needs to wait for a response from the client which can take >100 ms. It would be laggy because shots now require extra time. The code will be complex because there would be more edge cases (what happens if you tell the client to calculate x but the user disconnects). 

This would also allow cheating.. the client could just report all shots against him as 'missed'.

This [b]might[/b] be understandable for calculations that take > 1 second.

-------------------------

thebluefish | 2017-01-02 01:00:24 UTC | #11

[quote="izackp"]When you have the client make the decisions you're going to lead into 'conflicts'. Let's say you have 8 different people connected to the server and 2 of them decide the opposite outcome then you end up with a 'conflict'. At this point, they must be resolved which can take some time and extra communication between clients. [/quote]

TBH this isn't the hardest part to solve. When a physics engine is 100% deterministic (like Box2D for instance), then all clients which are regularly synchronized with the main server should see the exact same events play out. This is how AAA games like Halo and Call of Duty are able to get away with player-to-player collision.

In my game project, I don't even need player-to-player collision so long as I can have multiple players interacting with the environment. I might try digging around the original implementation this afternoon and see if I can't come up with some form of a client-controlled node.

The idea for a client-controlled Node comes more-so from the MMO aspect. Games like WoW or Guild Wars give the client player complete freedom, there's a reason why in Guild Wars 2 it used to be trivial to "explore" all areas since there were teleport hacks from day 1 (swtor had the same teleport issue even over a year after release). In these examples, it's significantly cheaper to allow clients to call the shots and to simply enforce some light constraints such as whether the player moved too fast, whether a move hit an enemy, etc...

-------------------------

weitjong | 2017-01-02 01:00:25 UTC | #12

Finally! You understand my question. I am beginning to doubt my English  :laughing: .

I have no prior experience of Source Engine. I expect there must be a technical difficulty or drawback that I am not aware of in designing it as I described. Hence I am asking the question. Since I have no prior experience, what it am about to say next may be just nonsense. I am agree with you that the hit test calculation could be complex but it should not be more complex than the same test carried out on the server (which could do them many times and still manages to keep the game ticks). If I could do it my way then the shot is fired, client could check for potential hit locally in real time, send a package to server containing the shoot message + a "hit" message (if client claims it). These two messages could arrive in just one network package. When I referred to distributed computing earlier, I didn't mean another round trip communication between server and client. So I believe this extra hit test on the client side could be done much faster than what you stated.

As for the cheating scenario you are afraid of, it won't happen because the shoot message is sent by user firing the shot which is more eager to claim a hit rather than not. Obviously, server does not care what the user being shot at says  :wink: .

-------------------------

thebluefish | 2017-01-02 01:00:25 UTC | #13

If a client just sends a "hit" shot, then there's not much for the server to check. It might be better for the client to create a bullet "object" and send this to the server for a given tick. Then the server can do a check to see that, if this bullet was created at tick X, does it *really* hit the dude at tick Y. Since the client and server would ideally be using the same logic for the bullet, the implementation could be as simple or as complex as you want it.

-------------------------

izackp | 2017-01-02 01:00:25 UTC | #14

[quote="thebluefish"]
TBH this isn't the hardest part to solve. When a physics engine is 100% deterministic (like Box2D for instance), then all clients which are regularly synchronized with the main server should see the exact same events play out. This is how AAA games like Halo and Call of Duty are able to get away with player-to-player collision.
[/quote]

With a deterministic set up, you still need 1 authority server to resolve timing issues. (Player A shot at 153 and killed Player B, Player B shot Player A at 154). Of course Player B will have thought he won the fight until everything syncs. Unless you do a lockstep method, but then your game will be like Age of Empires II where if one person lags then everyone lags.


Side note: The only way to have a deterministic engine is if everyone has the same exact processor when using floats/doubles. If you use Fixed Point Integers then you don't have this constraint. 

Another Note: [gafferongames.com/networking-for ... terminism/](http://gafferongames.com/networking-for-game-programmers/floating-point-determinism/) This site has very good info in regards to networking and physics.

Side Note 2.0:
If it were up to me I would use a deterministic engine, keep track of the entire game state for (2 seconds), use input/event buffering, and if there is a desync then you can roll back the client (up to 2 seconds). If there is a D/C then you can serialize the game state and send it to client. This is actually what I'm planning on doing with my game/engine. However, it's more complex then it seems.

-------------------------

thebluefish | 2017-01-02 01:00:25 UTC | #15

[quote="izackp"][quote="thebluefish"]Side note: The only way to have a deterministic engine is if everyone has the same exact processor when using floats/doubles. If you use Fixed Point Integers then you don't have this constraint. 
[/quote][/quote]

As long as everyone constrains to IEEE standards, which can be enforced, then it will still be deterministic. Previous to this, I played around with a 2D game engine that used Box2D and was able to keep everything working over the network.

From [gafferongames.com/networking-for ... terminism/](http://gafferongames.com/networking-for-game-programmers/floating-point-determinism/)

[quote]I work at Gas Powered Games and i can tell you first hand that floating point math is deterministic. You just need the same instruction set and compiler and of course the user?s processor adheres to the IEEE754 standard, which includes all of our PC and 360 customers. The engine that runs DemiGod, Supreme Commander 1 and 2 rely upon the IEEE754 standard. Not to mention probably all other RTS peer to peer games in the market. As soon as you have a peer to peer network game where each client broadcasts what command they are doing on what ?tick? number and rely on the client computer to figure out the simulation/physical details your going to rely on the determinism of the floating point processor.

At app startup time we call:

_controlfp(_PC_24, _MCW_PC)
_controlfp(_RC_NEAR, _MCW_RC)

Also, every tick we assert that these fpu settings are still set:

gpAssert( (_controlfp(0, 0) & _MCW_PC) == _PC_24 );
gpAssert( (_controlfp(0, 0) & _MCW_RC) == _RC_NEAR );[/quote]

There's plenty of documentation available online regarding client-side prediction and methods available for it. Currently I'm WAY too swamped to get familiar enough to make the necessary changes, but I'm hoping a solution might crop up  :slight_smile:

-------------------------

izackp | 2017-01-02 01:00:25 UTC | #16

Awesome.  :nerd:

Using floats is still scary though lol

-------------------------

izackp | 2017-01-02 01:00:25 UTC | #17

[quote="thebluefish"]
[*]HardControl - Allow the client to update the character locally. These updates are then sent to the server to propagate to the other clients.
[/quote]

Actually, I don't see why you can't just tell your peers 'I'm here, I'm doing this to this'. Theoretically, desycronization won't matter because you will be updating everyone as to what you're doing and your peers will force make the changes to their own client. It would be pretty simple. Client prediction won't matter on the Player's side because everything happens in real time, and as long as you send data that helps your peers guess what you are doing (or where you are going; x, y, and velocity) it shouldn't matter much on that side either.

Assuming we don't care at all about cheating.. I would be interested in seeing a demo game of this.

-------------------------

thebluefish | 2017-01-02 01:00:25 UTC | #18

I would rather stray away from P2P if possible. Big thing is that the server can then choose to do server-side enforcement to prevent cheating. This is especially true once you want to have a player interacting with the server world.

[quote="izackp"]Using floats is still scary though lol[/quote]

Still not quite sure how this is going to work on mobile, mobile processors are an entirely different beast to contend with.

-------------------------

izackp | 2017-01-02 01:00:25 UTC | #19

[quote="thebluefish"]I would rather stray away from P2P if possible.[/quote]

I Agree.

[quote="thebluefish"]Big thing is that the server can then choose to do server-side enforcement to prevent cheating. This is especially true once you want to have a player interacting with the server world..[/quote]

Though, Once you add server-side enforcement Hard Control becomes Soft Control:

[quote="thebluefish"][*]SoftControl - Allow the client to update the character locally. The server will still have ultimate authority, and can make corrections to the client-side as necessary.[/quote]

Bleh I should get back to work o.o lol

-------------------------

thebluefish | 2017-01-02 01:00:25 UTC | #20

[quote="izackp"][quote="thebluefish"]Big thing is that the server can then choose to do server-side enforcement to prevent cheating. This is especially true once you want to have a player interacting with the server world..[/quote]

Though, Once you add server-side enforcement Hard Control becomes Soft Control[/quote]

I think of "hard control" vs "soft control" a bit different, maybe I explained it weird. Essentially with soft control, you have the server running the same exact simulation as the client, but the client performs client-side prediction which is synchronized with the server. Meanwhile with hard control, the server does not simulate the client interactions. Instead the client performs its interactions, sends it to the server, and propagates to other clients. In this case, server-side enforcement would be a set of rules that runs separately to keep the client within defined constraints (limited client speed, teleportation detection, interaction distance, etc...), without running the entire simulations.

-------------------------

izackp | 2017-01-02 01:00:26 UTC | #21

Ok it seems like you're talking about, kind of, how PSO 2 and Maple Story does their networking.

I believe the server doesn't keep track of positions or physics or do any kind of simulation. All the server is responsible for is monster spawns, damage calculated when a monster is attacked, damaged calculated when you are attacked, how much XP was acquired when defeating the monster, and what items are dropped by the monster. It also acts as a 'forwarder' for everything else such as position updates. Then there is a set a rules which when broken results in a ban, disconnect, correction, ect.

I believe you can accomplish this with just messages (events) instead of a special replication system. All you need is:
 Player X attacked Monster Y. 
 Player X entered Area Z.

Once you send those to the server it responds appropriately:
 Monster Y takes 23 Damage
 Spawn Monsters A, B, C(Rare) in Area Z

I suppose in this example the player is a 'hard control' node. I'm not entirely sure how you would accomplish this without 'events' and only through replication. I've tried picturing a few scenarios.. but I can't think of a scenario that works.  All of this is just pure speculation anyways  :laughing: .

[quote="cadaver"]The reason why the Source and Unreal engines can rather easily perform client prediction is because the player characters don't move using rigid body dynamics, rather they use a "character controller"[/quote]

I like how Source and Unreal use character controllers over rigid bodies.. Having npc/players actually be physical objects is weird if you think about it. Players usually can do things that are physically impossible such as: teleportation, really high jumps, over-exaggerated punches, and run super fast. Making them part of the simulation means you're working [b]against[/b] the physics engine. Though your characters will probably have to implement their own physics interactions.

I once ran into a problem using Box2D where I had almost everything perfect for a platform game. Slopes, hanging on walls, ducking, ect. But then I tried implementing jump-through platforms and teleportation... it didn't work out well. Especially with multiple players. However, that was a long time ago and I don't know if Box2D has been updated to make this easier or what constraints bullet imposes so this is just more speculation xD.

-------------------------

cadaver | 2017-01-02 01:00:27 UTC | #22

Yes, there are pros/cons to both rigidbodies and character controllers. Like you said, using controllers means implementing almost every physics interaction manually: pushing objects, riding on moving platforms etc. 

In regard to networking and physics, many design choices taken in Urho equal to taking something that is suboptimal, but works in a predictable and mostly correct way without game-specific tweaks. Why is this? Well, we don't have the manpower of Unreal or Source :wink: When making a specific game and finding that Urho's ready solution falls short of your goals, you can always proceed to substitute your own (assuming that you have the skill.) The documentation should probably stress this more. Unfortunately, in many cases this may require tearing down existing subsystem code & practically making a fork.

-------------------------

thebluefish | 2017-01-02 01:00:27 UTC | #23

[quote="izackp"]I once ran into a problem using Box2D where I had almost everything perfect for a platform game. Slopes, hanging on walls, ducking, ect. But then I tried implementing jump-through platforms and teleportation... it didn't work out well. Especially with multiple players. However, that was a long time ago and I don't know if Box2D has been updated to make this easier or what constraints bullet imposes so this is just more speculation xD.[/quote]

Box2D actually does quite well with jump-through platforms, though my implementation of it felt "hack-ish". Teleporting is now a trivial thing to do, too.

My question at this point then is what's the difference between a character controller and a rigidbody? Ideally I would want to implement a character controller since it sounds like that's the best way to go.

Good news: I've gotten character-controlled nodes mostly working, but I had to make some edits to some components. Essentially on the server I'm setting a flag on each node. Then on each update the server sends to the client, the client sends a RemoteEvent back to the server for each client-controlled node with this flag. It works, but again seems "hack-ish" and I've no idea what kind of security risk this poses.

I've since reverted the changes I made to Urho3D, and instead I'm now looking for better ways to work with this using a local node and remote events. I wonder if I can just send the entire local node via a remote event, will have to check when I get back home.

-------------------------

cadaver | 2017-01-02 01:00:27 UTC | #24

Character controller is usually implemented as a collision shape that you tell exactly how it should move. When it moves, it checks for static world collisions so that it doesn't go through walls.

Bullet has its own implementation of a controller, called btCharacterController. Though I'm not exactly sure of its maturity. Here's some discussion, it seems like tuning the controller to work in all situations is a bit of an art:
[code.google.com/p/bullet/issues/detail?id=198](https://code.google.com/p/bullet/issues/detail?id=198)

What might be useful for prediction / client control implementations (reduce amount of Urho hacking needed) would be a component that basically stores the last transform & velocity values from the server and prevents applying them directly to the Node & RigidBody. With this component, it would be the programmer's responsibility how (and when) to deal with the received values.

-------------------------

thebluefish | 2017-01-02 01:00:48 UTC | #25

I've began to take steps to implement client-controlled objects. I've done some hacking through Urho3D's system and I've managed to get client-to-server mostly working, but it needs to be cleaned up a bit. I'm estimating I'll have enough time something this coming week to clean things up and properly test different scenarios.

As far as how it works, current there are 2 modes:

- Scene-enforced: Same as current Urho3D's current behavior.
- Client-controlled: Scene assigns nodes to a client Connection, that client (and ONLY that client) can make changes which will replicate to everyone else. This system is then very similar to MMOs such as WoW, Guild Wars 2, Star Wars The Old Republic, etc...

It currently works off a Node's owner Connection. Any Node that has an owner is treated as client-controlled. The Node on the client automatically has its owner set to the server's Connection, indicating which nodes the client is free to control. A scene-wide attribute is used to tell us which mode (ServerEnforced, ClientControlled) we are operating in.

Currently there are required changes to the following Urho3D classes:

Node
Scene

Is there any interest in making this a core feature of Urho3D? If so, are there any changes to the behavior that would be preferred?

-------------------------

cadaver | 2017-01-02 01:00:49 UTC | #26

I believe this is OK to include as long as only the server has the authority to switch the mode, and there's prevention for rogue attempts to control an object from the client side. Basically, you're deciding that possible client side cheating is OK for your game, but not allowing any hacked client to switch the mode in any Urho-based game.

We do need the concept of "owned" object that still is only server-authoritative, so the mode shouldn't be tied to the owner only.

Probably will not make it into the upcoming release, but can be merged afterward. Ideally Node & Scene should know as little of networking as possible, so those changes will be scrutinized most.

-------------------------

thebluefish | 2017-01-02 01:00:50 UTC | #27

I have made some drastic changes over the weekend to streamline the process, and I rolled back most of my original changes to existing Urho3D classes. I use attributes to control which mode the scene is in, and to assign a "controller connection" to a given node (so that the SetOwner/GetOwner can be changed without affecting this system). The server automatically refuses replication that isn't explicitly allowed such as a Connection trying to replicate a Node it isn't assigned to, or all replication when the server is in "ServerReplicated" mode (aka the classic Urho3D way of doing it). That ensures that the server maintains ultimate authority over what it allows to come in.

However I'm still running into some problems with my implementation, so I'm going to have to spend more time on it.

-------------------------

