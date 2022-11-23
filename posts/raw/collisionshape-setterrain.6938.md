nickwebha | 2021-07-30 12:47:04 UTC | #1

*I am sure this is answered somewhere in the forums but I could not find it. Sorry if (when) this is a repeat.*

I have been re-jiggering my entire approach to the architecture of my game. I decided to rely more on the built-in/Bullet engine.

I have:

```
this->terrainNode_ = this->scene_->CreateChild( Terrain );
this->terrainNode_->SetPosition( Urho3D::Vector3::ZERO );
auto* terrain = this->terrainNode_->CreateComponent< Urho3D::Terrain >();
terrain->SetPatchSize( 64 );
terrain->SetSpacing( Urho3D::Vector3( 5.0f, 1.0f, 5.0f ) );
terrain->SetSmoothing( true );
terrain->SetHeightMap( cache->GetResource< Urho3D::Image >( Textures/HeightMap.png ) );
terrain->SetMaterial( cache->GetResource< Urho3D::Material >( Materials/Terrain.xml ) );
terrain->SetOccluder( true );

auto* rigidBody = this->terrainNode_->CreateComponent< Urho3D::RigidBody >();
auto* collisionShape = this->terrainNode_->CreateComponent< Urho3D::CollisionShape >();
collisionShape->SetTerrain();
```
for my terrain.

My height map is as so:
![HeightMap|500x500](upload://p7vu0aCcmVm9RzdL3Fn8FUaRAYi.png)

I have for my player creation:
```
for ( short int i = 0 ; i < PLAYER_COUNT ; i++ ) {
	this->players_[ i ] = this->scene_->CreateChild( "Player" );
	Urho3D::Vector3 position( effolkronium::random_static::get( -1000, 1000 ), 0.0f, effolkronium::random_static::get( -1000, 1000 ) );
	position.y_ = this->terrainNode_->GetComponent< Urho3D::Terrain >()->GetHeight( position ) + 50.0f;
	this->players_[ i ]->SetPosition( position );
	this->players_[ i ]->SetScale( Urho3D::Vector3( 100.0f, 50.0f, 100.0f ) );
	auto* object = this->players_[ i ]->CreateComponent< Urho3D::StaticModel >();
	object->SetModel( cache->GetResource< Urho3D::Model >( "Models/Box.mdl" ) );
	object->SetMaterial( cache->GetResource< Urho3D::Material >( "Materials/Stone.xml" ) );
	object->SetCastShadows( true );

	auto* rigidBody = this->players_[ i ]->CreateComponent< Urho3D::RigidBody >();
	rigidBody->SetMass( 5.0f );
	rigidBody->SetFriction( 1.0f );
	rigidBody->SetCollisionEventMode( Urho3D::COLLISION_ALWAYS );
	auto* collisionShape = this->players_[ i ]->CreateComponent< Urho3D::CollisionShape >();
	collisionShape->SetBox( Urho3D::Vector3::ONE );

	this->players_[ i ]->CreateComponent< Player >();
...
}
```

I have for my player movement:
```
for ( short int i = 0 ; i < PLAYER_COUNT ; i++ ) {
	auto position = this->players_[ i ]->GetPosition();
	position.x_ += this->players_[ i ]->GetComponent< Player >()->GetX();
	position.z_ += this->players_[ i ]->GetComponent< Player >()->GetZ();
	this->players_[ i ]->SetTransform( position, Urho3D::Quaternion( Urho3D::Vector3( 0.0f, 1.0f, 0.0f ), this->terrainNode_->GetComponent< Urho3D::Terrain >()->GetNormal( position ) ) );
}
```
for my players.

At the 90° wall, instead of stopping/not being allowed to pass, the player just clips through the wall (after some jittering). Even at the 45° angle (up the hill) the player eventually just falls through the floor. I have tried using `ApplyForce()` instead but it does not seem to do anything.

I am pretty sure I am supposed to be using `ApplyForce()` instead of manipulating the position myself but I can not make it work. I have been studying *19_VehicleDemo* but what works there does not seem to work for me.

If I add `position.y_ = this->terrainNode_->GetComponent< Urho3D::Terrain >()->GetHeight( position ) + 25.0f` to the player movement it solves my clipping problem but I lose physics (obviously). Plus the player can now climb vertical walls (obviously, again).

How am I supposed to be moving the player around or is Bullet just not good with this kind of thing?

-------------------------

nickwebha | 2021-08-01 23:16:31 UTC | #2

https://youtu.be/eRQhoxFbItY

I got the player moving around (it was me being dumb) using:
```
for ( short int i = 0 ; i < PLAYER_COUNT ; i++ ) {
	const auto& player = this->players_[ i ];
	auto* playerComponent = player->GetComponent< Player >();
	auto* rigidBody = player->GetComponent< Urho3D::RigidBody >();

	rigidBody->ApplyForce( Urho3D::Vector3( 1, 0, 0 ) * playerComponent->GetX() );
	rigidBody->ApplyForce( Urho3D::Vector3( 0, 0, 1 ) * playerComponent->GetZ() );
...
}
```

Now it no longer goes through walls (my bad) but flips and spins uncontrollably almost like a top. It also does not have the "pep" it used to have (takes a few moments to get going and stop) which is not desirable.

-------------------------

evolgames | 2021-07-31 18:04:20 UTC | #3

Set angular factor vector to prevent unwanted rotations. In your case, you probably want only Y-axis rotations. So SetAngularFactor(Vector3(0,1,0))

-------------------------

nickwebha | 2021-08-02 00:05:45 UTC | #4

[quote="evolgames, post:3, topic:6938"]
Set angular factor vector to prevent unwanted rotations.
[/quote]
Ooohhh, now I understand how it all fits together. Thank you, that was the bit I was missing in my head.

My code now looks like:

```
for ( short int i = 0 ; i < PLAYER_COUNT ; i++ ) {
	const auto& player = this->players_[ i ];
	auto* playerComponent = player->GetComponent< Player >();
	auto* rigidBody = player->GetComponent< Urho3D::RigidBody >();
	auto* node = rigidBody->GetNode();

	const auto playerXVelocity = playerComponent->GetX();
	const auto playerZVelocity = playerComponent->GetZ();

	const auto velocity = rigidBody->GetLinearVelocity();
	if ( playerXVelocity == 0 && playerZVelocity == 0 )
		rigidBody->SetLinearVelocity( Urho3D::Vector3( 0, velocity.y_, 0 ) );
	else
		rigidBody->SetLinearVelocity( Urho3D::Vector3( playerXVelocity, velocity.y_, playerZVelocity ) );

	node->SetRotation( Urho3D::Quaternion( Urho3D::Vector3( 0.0f, 1.0f, 0.0f ), this->terrainNode_->GetComponent< Urho3D::Terrain >()->GetNormal( node->GetPosition() ) ) );
...
}
```
It allows me to move with the gamepad precisely while still working within the physics system. I use `ApplyForce()` in other places (like for a jumping power-up).

https://www.youtube.com/watch?v=HKnlFtOUDJo
(In the video I am always holding the stick is some direction. It just refuses to move some of the time. I wiggle it a lot and that seems to help.)

Now I am running into this issue where (with and without `ApplyForce()` instead of `SetLinearVelocity()`) the player seems to get stuck on the ground a little. You can see in the video it mostly happens when moving up or right, less so-- but still-- down or left. I ruled out issues with the gamepad.

When I look for `E_NODECOLLISIONSTART` events I see lots of them. The player is moving across flat ground but triggering repeated collisions with the terrain. I assume this is due to gravity but I am not sure if it is related to my problem.

-------------------------

evolgames | 2021-08-02 01:15:39 UTC | #5

What's your gravity set at? Default should be fine though I use slightly stronger. You shouldn't set linear velocity to move a character. Same as you wouldn't set position of rigid bodies as it messes with the physics.
Does the issue happen with apply force too?
What collision shape is on your character? Try a capsule.

-------------------------

nickwebha | 2021-08-03 12:47:18 UTC | #6

[quote="evolgames, post:5, topic:6938"]
What’s your gravity set at?
[/quote]
Now it is `physicsWorld->SetGravity( Urho3D::Vector3::DOWN * LEVEL_GRAVITY );	// LEVEL_GRAVITY = 1.5`.

It was 1,000 which I did not even realize. Thank you for that. Not sure how that happened; I must have been trying to change some other value and accidentally changed that one.

A problem with the default gravity-- or near to it-- is that players do not fall nearly quickly enough. The top of the slightest ramp sends them slowly flying into space or very, very slowly falling towards the ground after running off a ledge. I have tried playing with higher mass values (5-25) but then they climb 45° ramps very, very slowly if at all and I still have the flying-into-space problem.

[quote="evolgames, post:5, topic:6938"]
You shouldn’t set linear velocity to move a character.
[/quote]
That is unfortunate because it was the type of movement I wanted for the player. I am aiming for a *Smash TV*/classic twin-stick shooter kind of movement (responsive right away and there is no "floatyness" or "lag" in the movement). I want the player to be able to move on a dime regardless of currently velocity in any direction. `ApplyForce()` simply does not give me that as far as I can see.

[quote="evolgames, post:5, topic:6938"]
What collision shape is on your character? Try a capsule.
[/quote]
I am experimenting with `SetCapsule()` but honestly not seeing any difference.

Thank you for your help in this. There are so many values to play with that getting the right combination on my own is proving suuuper difficult. I tried finding a tutorial in addition to the documentation, source, and samples but no luck there.

**Edit**
Once I get everything working right enough I am going to come back to these old threads and write some blogs about "the right way" to do these things. Maybe someone else does not have to experiment as much I as I am right now in the future.

-------------------------

evolgames | 2021-08-03 12:37:20 UTC | #7

Well, for responsiveness you could definitely try low mass, higher forces, and then messing with linear damping and setting velocity limits (so they have a max speed). My gravity is like -25 for Y.
What is your friction set for the player and the terrain? And mass for player?

By limiting velocity I mean using setlinearvelocity to an upper limit if the player exceeds it, though usually damping is enough.

Basically, low mass and a high force will move the body quickly, then a good damping will stop it when you let go of the control. Should be possible to get it how you want. I think the curve of the capsule helps it to not get stuck on things, especially slopes, so try that again at the same time.

-------------------------

nickwebha | 2021-08-03 17:40:27 UTC | #8

Thanks to you the players are moving around nearly perfectly (some tweaks here and there but I will get to that in the polish stage).

[quote="evolgames, post:7, topic:6938"]
What is your friction set for the player and the terrain? And mass for player?
[/quote]
Terrain friction is `SetFriction( 0.0f )`. Player mass is `SetMass( 1.0f )`. Player friction is `SetFriction( 0.0f )`. I have my gravity set to -25.

My players look like this:
```
auto* rigidBody = player->CreateComponent< Urho3D::RigidBody >();
rigidBody->SetMass( 1.0f );
rigidBody->SetFriction( 0.0f );
rigidBody->SetLinearDamping( 1.0f );
rigidBody->SetAngularFactor( Urho3D::Vector3::ZERO );
```

Everything is looking great except for one thing: The gravity/player mass combination results in falling happening very, very, *very* slowly (even driving down a ramp the player clears the whole thing with tons of room to spare without ever touching it). If I increase the players mass too much then it will not move no matter how much force I apply. If I increase the gravity then the players start getting stuck on the terrain.

I am toying with the idea of some additional logic: If the player should be falling temporarily set `SetGravityOverride()` to something high. That seems hacky as hell though and there must be a better way.

-------------------------

evolgames | 2021-08-03 15:48:46 UTC | #9

Glad it's starting to work.
What size is this player?
So, try a lower linear damping. At 1 it's going to seriously slow down the player, even fighting gravity. Basically, think of it as "drag," and put it at like .2 or so.

1 would basically reduce almost all linear velocity every frame, which is why it's slowing down like crazy.

-------------------------

nickwebha | 2021-08-03 18:34:31 UTC | #10

[quote="evolgames, post:9, topic:6938"]
What size is this player?
[/quote]
`SetScale( Urho3D::Vector3( 100.0f, 50.0f, 100.0f ) )`. This will eventually be replaced by an actual model. It has a turret on top with `SetPosition( Urho3D::Vector3( 0, .5, .5 ) )` and `SetScale( Urho3D::Vector3( .25, .5, 1 ) )` but there is no `RigidBody` on the turret.

I am going to spend-- probably alot of-- time playing with the variables and taking notes. Thank you for your help so far!

-------------------------

evolgames | 2021-08-03 21:31:31 UTC | #11

Oh that's huge. That and the other reasons are why it would fall slowly. Imagine a skyscraper falling over. I mean, you *can* do that, but seriously just make your character between 1-3 units tall.
Have you seen the character demo sample? Might be easy to start with that as a template.

-------------------------

nickwebha | 2021-08-03 22:22:34 UTC | #12

[quote="evolgames, post:11, topic:6938"]
Oh that’s huge.
[/quote]
Is it? I will have to rejigger the terrain and heightmap sizes and camera placements. Come to think of it, I have to readjust the scale and speed of everything.

This is going to take me a little while. Be back later.

**Note to self for later**
Include scale notes in future blog posts.

-------------------------

nickwebha | 2021-08-03 23:20:15 UTC | #13

So I shrunk *everything* down.

The player is now at `SetScale( Urho3D::Vector3( 3.0f, 1.5f, 3.0f ) )`. The terrain is at *257*x*257*, `SetSpacing( Urho3D::Vector3( 1.0f, 0.05f, 1.0f ) )` (1/4th its original size). The camera went from *3000* units away to *150* units away. Gravity is *1*, players are at *1* mass, *1* friction, and *0.2* linear damping.

https://www.youtube.com/watch?v=ur3RWV3M4NQ

The players are hopping all the time. I tried different gravity and mass and linear damping but they always hop.

-------------------------

evolgames | 2021-08-03 23:42:08 UTC | #14

That should be good with gravity at Vector3(0, -25, 0). Hmm
Can I see the whole set up?

-------------------------

nickwebha | 2021-08-04 00:09:18 UTC | #15

[quote="evolgames, post:14, topic:6938"]
Can I see the whole set up?
[/quote]
At *-25* it both gets stuck *and* hops. A little adorable. Adorable or I am losing my mind.

Creating the players:
```
for ( short int i = 0 ; i < PLAYER_COUNT ; i++ ) {
	this->players_[ i ] = this->scene_->CreateChild( "Player" );
	const auto& player = this->players_[ i ];

	Urho3D::Vector3 position( effolkronium::random_static::get( -50, 50 ), 0.0f, effolkronium::random_static::get( -50, 50 ) );
	position.y_ = this->terrainNode_->GetComponent< Urho3D::Terrain >()->GetHeight( position ) + 1.0f;
	player->SetPosition( position );
	player->SetScale( Urho3D::Vector3( 3.0f, 1.5f, 3.0f ) );
	auto* object = player->CreateComponent< Urho3D::StaticModel >();
	object->SetModel( cache->GetResource< Urho3D::Model >( "Models/Box.mdl" ) );
	object->SetMaterial( cache->GetResource< Urho3D::Material >( "Materials/Stone.xml" ) );
	object->SetCastShadows( true );

	auto* rigidBody = player->CreateComponent< Urho3D::RigidBody >();
	rigidBody->SetMass( 1.0f );
	rigidBody->SetFriction( 1.0f );
	rigidBody->SetLinearDamping( 0.2f );
	rigidBody->SetAngularFactor( Urho3D::Vector3::ZERO );
	rigidBody->SetCollisionEventMode( Urho3D::COLLISION_ALWAYS );

	auto* collisionShape = player->CreateComponent< Urho3D::CollisionShape >();
	collisionShape->SetSphere( 1 );
...
}
```

Updating the player each tick:
```
for ( short int i = 0 ; i < PLAYER_COUNT ; i++ ) {
	const auto& player = this->players_[ i ];
	auto* playerComponent = player->GetComponent< Player >();
	auto* rigidBody = player->GetComponent< Urho3D::RigidBody >();
	auto* node = rigidBody->GetNode();

	rigidBody->ApplyForce( Urho3D::Vector3( 1, 0, 0 ) * playerComponent->GetX() );
	rigidBody->ApplyForce( Urho3D::Vector3( 0, 0, 1 ) * playerComponent->GetZ() );

	node->SetRotation( Urho3D::Quaternion( Urho3D::Vector3( 0.0f, 1.0f, 0.0f ), this->terrainNode_->GetComponent< Urho3D::Terrain >()->GetNormal( node->GetPosition() ) ) );
...
}
```

Playing with gravity anywhere from *-1* to *-25*.

I have been staring at this since 6:00AM and it is now 8:00PM. Going to get some sleep and pick up in the morning... are water and food still a thing?

-------------------------

evolgames | 2021-08-04 04:17:35 UTC | #16

Maybe it's the rotation. Why are you setting the node's rotation to the terrain normal? To me it seems unnecessary if you're using physics. If I were making a game without physics for the player, I would do something like that (to keep the player *on* the ground in the right way), and I would also set the player's Y height to the terrain height as you did initially because you *can* manually set positions without physics. Well you can try to do it with physics, but you shouldn't.

If you have gravity and collision shapes on the player and terrain the rotation will be correct by the physics alone. I'm not sure if that's why, but I would try commenting that out.

Gravity at -1 I would expect that they would be floaty. What kind of game is this going to be? Also, try commenting out the player friction (for now). Maybe it's bumping a lip in the terrain or something.

Do you use the debug renderer? I always have mine set up so that I can toggle it with a key and check everything mid-game.

Sleep helps!

-------------------------

nickwebha | 2021-08-06 14:00:26 UTC | #17

[quote="evolgames, post:16, topic:6938"]
Why are you setting the node’s rotation to the terrain normal?
[/quote]
I think that was just an old line from when I was not using the physics engine at first and I just never removed it. Gone now.

[quote="evolgames, post:16, topic:6938"]
What kind of game is this going to be?
[/quote]
Think [Smash TV](https://www.youtube.com/watch?v=WIPn7RZJ4vg&t=300s) except PvP with four players and competitive. Many particles effects, many weapons and power-ups. Just mindlessly shooting at each other. This is my first game so I would like to shoot a little higher than Pong but not as high as my dream project. So far I am happy with the results, as difficult as they are proving.

I have been planning to play with the `DebugRenderer` but never got around to it. I think I will dedicate some more time to that today.

-------------------------

grokko | 2021-08-10 02:52:26 UTC | #18

You can set the normal for your players rotation Quaternion to be the terrains direction cosines...

        float acosA = acos(norm.x_);
		float acosB = acos(norm.y_);
		float acosC = acos(norm.z_);
            
		float _x = acosA*180/3.14 - 90;
		float _y = acosB*180/3.14 - 90;
		float _z = acosC*180/3.14 - 90;
        
        Vector3 spine = Vector3(_x,_y,_z);
        Quaternion _ion;
	    _ion.FromAngleAxis(angle, spine);		
	    pNode()->SetRotation(_ion); 

That should oriient your player on top of the terrain all the time directed along angle...

Michael

-------------------------

nickwebha | 2021-08-11 11:25:48 UTC | #19

[quote="grokko, post:18, topic:6938"]
You can set the normal for your players rotation Quaternion to be the terrains direction cosines
[/quote]

How does this differ from something like:
```
auto position = this->players_[ i ]->GetPosition();|
position.x_ += this->players_[ i ]->GetComponent< Player >()->GetX();|
position.z_ += this->players_[ i ]->GetComponent< Player >()->GetZ();|
this->players_[ i ]->SetTransform( position, Urho3D::Quaternion( Urho3D::Vector3( 0.0f, 1.0f, 0.0f ), this->terrainNode_->GetComponent< Urho3D::Terrain >()->GetNormal( position ) ) );|
```
?

(Besides also setting the position).

**Edit**
I do not have the math background. I need to learn more about quaternions.

-------------------------

George1 | 2021-08-11 03:31:35 UTC | #20

I think you need to use impulse or velocity to control physics entity.  Otherwise the physics engine is overriding your manual position control.

-------------------------

grokko | 2021-08-11 16:21:41 UTC | #21

> this->players_[ i ]->SetTransform( position, Urho3D::Quaternion( Urho3D::Vector3( 0.0f, 1.0f, 0.0f ),

The Quaternion has to have a spine vector wherein the character places his feet on the surface, 90 degrees from the ground plane.

-------------------------

