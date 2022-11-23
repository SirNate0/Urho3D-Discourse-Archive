Commandor | 2017-01-02 01:15:16 UTC | #1

[u]CrowdAgent must set the movement through RigidBody.[/u] Because for the gameplay you need to game object contained both CrowdAgent and RigidBody and CollisionShape.
[b]Without this it is impossible to build a logic game based on physics and NavigationMesh.[/b]
 :exclamation:

-------------------------

cadaver | 2017-01-02 01:15:17 UTC | #2

I don't necessarily think the navigation components should try to do this on their own. It's non-obvious how they should do it. Applying forces? Applying velocity? Depending on the properties of the objects and the "feel" you are after, this might be done differently.

For kinematic rigidbodies, the node position update that the CrowdAgent does by itself should be already good to go.

You could try turning off auto position update from CrowdAgent (see CrowdAgent::SetUpdateNodePosition) and handle updates just in the manner you want by subscribing to E_CROWD_AGENT_REPOSITION event from the scene node owning the CrowdAgent.

However you'll have to note that there are two completely separate simulations (crowd and physics) and they don't feed information to each other, so they may not operate very smoothly. From what I remember Unity had similar problems with simultaneous navigation and physics.

Also you could consider just doing pathfinding queries and having your own steering system that acts according to the results.

-------------------------

Commandor | 2017-01-02 01:15:17 UTC | #3

[quote="cadaver"]

For kinematic rigidbodies, the node position update that the CrowdAgent does by itself should be already good to go.

[/quote]


Thank you, I'm just trying to "Is Kinematic". This works, [b]but missing a collision with objects whose mass is equal to 0.[/b]

-------------------------

Nerrik | 2017-01-02 01:15:17 UTC | #4

have you tryed 
body->SetTrigger(true);
and
agent->SetUpdateNodePosition(false);
?
There are some more calls to handle that
~with agent->GetTargetVelocity you also can make a ~body->ApplyImpulse and so on if you need 100% bullet.
2 extern libarys are as good as some coder can merged. :stuck_out_tongue:

-------------------------

Commandor | 2017-01-02 01:15:17 UTC | #5

[quote]body->SetTrigger(true);[/quote]
It will not work, because an object with the mass 0 is a wall, for which the object should not go.

[quote]2 extern libarys are as good as some coder can merged. :stuck_out_tongue:[/quote]
Unreal Engine not have this problem, bun they use both librarys.  :wink: 


I was faced with another problem: if I need a game bonus that can only collision with the player and not bots or collision with a tree on which runs into the bot, and it falls, they are also involved in the construction of the grid. Probably it is necessary to add to the Node or RigidBody or CollisionShape option, which excludes construction of the navigation mesh for the game object. Note: for bonuses I set body->SetTrigger(true);  :wink:

-------------------------

Eugene | 2017-01-02 01:15:17 UTC | #6

[quote]Unreal Engine not have this problem, bun they use both librarys.[/quote]
Did you investigated how do they achieve this and what limitations do they have?

-------------------------

Commandor | 2017-01-02 01:15:17 UTC | #7

No, I did not examine their code for details. For most tasks UE4 is very big.
It would be very convenient if some useful features from UE4 would be implemented in Urho3D.  :slight_smile: 

By the way, I noticed that the NavArea in Urho3D works differently, not like in UE4. In UE4 I can set the height of the volume in which to build a navigation mesh. In Urho3D it does not work.

-------------------------

Nerrik | 2017-01-02 01:15:17 UTC | #8

Without some source its hard to help :wink:

-------------------------

