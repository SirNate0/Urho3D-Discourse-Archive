nickwebha | 2021-07-26 14:17:27 UTC | #1

I seem to have painting myself into a corner.

I have a number of classes such as:
`Game`
`Level`
`Player`
`Creates`
`Weapon`
`Activated`

The gist of it goes `Game` is my `class Game : public Urho3D::Application { ... }`. Within `Game` exists `Level`. Within `Level` is `Player` and `Crates`. Within `Player` is `Weapon` and `Activated`.

To put it another way:

`Game`
--> `Level`
--> --> `Player`
--> --> --> `Weapon`
--> --> --> `Activated`
--> --> `Crates`

This design allows data to flow "down the chain" (from `Game` to `Level` to `Player` to `Weapon`, for example) but not back up. I have some collision events in there that allow "free-flowing data" but they only know about the nodes themselves, not the class that own them. For example, if a player is hit by another players bullet the event only tells me the two nodes involved (the player node and the bullet node), not the player that fired it. This allows me to assign damage to the player hit but not who fired the bullet.

How can I solve this using Urho3D primitives? I see something called tags but that also deals with nodes, not the owning class/player (unless I am missing something). Is there something that allows me to attach points to events, for example (or is that bad practice)? Maybe I could somehow attach a `this` pointer to a node who I know who is who?

I have my players running around the level, shooting each other, tracking health, but no way to, for example, keep score about who damaged who.

-------------------------

SirNate0 | 2021-07-25 22:44:07 UTC | #2

I would just add a `WeakPtr<Player> owner_` to the Bullet class. Then when the two collide you can access who owns (fired) the bullet from the Node containing the Bullet component. I'm assuming in that that both the Player and the Bullet are components so that you can access them from the Node.

-------------------------

nickwebha | 2021-07-27 11:01:17 UTC | #3

I think I designed this in a not very Urho3D-friendly way. I have:

```
class Weapon : public Urho3D::Object {
	protected:
...
		Urho3D::SharedPtr< Urho3D::Terrain > terrain_;
		Urho3D::SharedPtr< Urho3D::Node > playerTurrentNode_;

		std::list< Projectile > projectiles_;

	public:
		virtual void Start( void );
		virtual void Stop( void );
		virtual void Update( Urho3D::StringHash, Urho3D::VariantMap& ) = 0;
...
};
```
```
class WeaponCannon : public Weapon {
	public:
		using Weapon::Weapon;

		void Update( Urho3D::StringHash, Urho3D::VariantMap& );
};
```
```
class Player : public Urho3D::Object {
	private:
...
		std::unique_ptr< Weapon > weapon_;
		std::unique_ptr< Activated > activated_;
		std::unique_ptr< Passive > passive_;

	public:
		void Update( Urho3D::StringHash, Urho3D::VariantMap& );
...
};
```
```
class Level : public Base {
	private:
...
		std::unique_ptr< Player > players_[ PLAYER_COUNT ];
		std::unique_ptr< Crate > crates_[ CRATE_COUNT ];

	public:
		using Base::Base;

		void Update( Urho3D::StringHash, Urho3D::VariantMap& );
...
};
```

Cannon balls, for example, are created like this in `WeaponCannon::Update` (this is just to prototype):
```
auto objectNodePosition = this->playerTurrentNode_->GetWorldPosition();
auto objectNodeRotation = this->playerTurrentNode_->GetRotation().YawAngle();

auto* cache = GetSubsystem< Urho3D::ResourceCache >();

auto* node = this->scene_->CreateChild( "CannonBall" );
node->SetPosition( Urho3D::Vector3( objectNodePosition.x_ + sin( objectNodeRotation * M_PI / 180 ) * 75, this->terrain_->GetHeight( objectNodePosition ), objectNodePosition.z_ + cos( objectNodeRotation * M_PI / 180 ) * 75 ) );
node->SetScale( Urho3D::Vector3( 25, 25, 25 ) );
node->Rotate( Urho3D::Quaternion( Urho3D::Vector3( 0.0f, objectNodeRotation, 0.0f ) ) );

auto* staticModel = node->CreateComponent< Urho3D::StaticModel >();
staticModel->SetModel( cache->GetResource< Urho3D::Model >( "Models/Sphere.mdl" ) );
staticModel->SetMaterial( cache->GetResource< Urho3D::Material >( "Materials/Stone.xml" ) );

auto* rigidBody = node->CreateComponent< Urho3D::RigidBody >();
rigidBody->SetMass( 0.25f );
rigidBody->SetFriction( 1.0f );
rigidBody->SetCollisionEventMode( Urho3D::COLLISION_ALWAYS );
auto* shape = node->CreateComponent< Urho3D::CollisionShape >();
shape->SetSphere( 1.0f );

auto* sound = cache->GetResource< Urho3D::Sound >( "Sound/WeaponCannon.ogg" );
auto* soundNode = this->scene_->CreateChild();
auto* soundSource = soundNode->CreateComponent< Urho3D::SoundSource >();
soundSource->Play( sound );
soundSource->SetGain( 0.25f );
soundSource->SetAutoRemoveMode( Urho3D::REMOVE_NODE );

Projectile projectile( Urho3D::SharedPtr< Urho3D::Node >( node ), objectNodeRotation );
this->projectiles_.push_back( projectile );
```

Each class just passes whatever is needed down the chain of classes.

I need to re-think this whole thing, the Urho3D way. Plus understand what the Urho3D way is.

**Edit**
In sample *05_AnimatingScene* I see custom components (`context->RegisterFactory<Rotator>()` and `auto* rotator = boxNode->CreateComponent<Rotator>()`). I still study this sample.

-------------------------

Dave82 | 2021-07-27 07:46:08 UTC | #4

You can send custom events. This is how i done in my game. You can send a BULLETHIT event and store the appropriate data in the eventData variant map.
Also i have a ProjectileManager component that handles all the projectiles that exist in the game. The projectiles can be bullets rockets etc (the manager handles what happens if the projectile hits different materials like flesh , transparent objects , wood glass etc) and when the projectile hits something the event is sent (who shot it , what was hit , direction , damage , etc)

-------------------------

nickwebha | 2021-07-27 13:27:48 UTC | #5

I am not understanding custom components. I found [some documentation](https://urho3d.io/documentation/HEAD/_scene_model.html) but it does not explain what I need it to explain.

When I try to add `node->CreateComponent( "Player", Urho3D::LOCAL, 0 )` to a node I get *ERROR: Could not create unknown component type 72A5FDC1*. When I try to add `node->CreateComponent< Player >( Urho3D::LOCAL, 0 )` I get *'GetTypeStatic' is not a member of 'Weapon'* (I assume this is a virtual function I need to overwrite but I do not know the signature(s)).

I am trying to go off the [node documentation](https://urho3d.io/documentation/HEAD/class_urho3_d_1_1_node.html) best I can. I am sure there is another page somewhere explaining what I am missing. I just have not found it yet.

-------------------------

SirNate0 | 2021-07-27 13:55:44 UTC | #6

You need to make your classes inherit from Component to use them as components. In addition, you need to register the class with the Context so it knows how to create them. I believe it's `Context::RegisterFactory<Player>()`. You would also need to add a constructor that takes only a `Context*`. Or, if you don't need to be able to create them on a node, you can leave your constructors and just call AddComponent with a pointer to your component (which must be stored in a SharedPtr).

-------------------------

nickwebha | 2021-07-28 13:44:28 UTC | #7

Right now my `Player` class looks like this:

```
class Player : public Urho3D::Object {
...
	public:
		Player( Urho3D::Context* context, Urho3D::Scene* scene ) : Urho3D::Object( context ) {
			this->context_ = context;
			this->scene_ = scene;
		};
...
};
```
when (I think) I need the `Player::Player` signature to look like this:
`Player( Urho3D::Context* context ) : Urho3D::Object( context ) { ... };`

Is there a way to get an existing scene from a context object alone? I do not see anything in [the documentation](https://urho3d.io/documentation/HEAD/class_urho3_d_1_1_context.html) that might help.

Or am I thinking about this wrong? Should not the entire `Player` class be changed but a more specific class just for just purpose? A `PlayerPointer` class or something (with a better name).

I am also looking into this `AddComponent()` idea but a quick *grep* of the samples turns up nothing. Plus "[Using this function from application code is discouraged...](https://urho3d.io/documentation/HEAD/class_urho3_d_1_1_node.html#a3792a0c2e23b120ac879c2931d6f9dc4)".

Ultimately I just want to get a pointer attached to a node so when a collision event happens I know who is responsible.

-------------------------

lebrewer | 2021-07-28 14:23:05 UTC | #8

Sorry, not wanting to hijack your thread, but I think this type of architectural documentation is what would be useful for Urho newcomers. How to do things the "Urho" way, how to grow projects bigger than a sample. Even if just a "roll a ball" thing, but with proper architecture, game design patterns, etc.

-------------------------

SirNate0 | 2021-08-22 18:15:44 UTC | #9

I'm proposing you change it to inherit from Component instead of from Object:
```
class Player : public Urho3D::Component {
...
	public:
		Player( Urho3D::Context* context ) : Urho3D::Object( context ) {
			this->context_ = context;
			// Scene is set when you add the component to a node
		};
...
};
```

You can have multiple scenes, so while you could register one as a subsystem with the Context, it would probably be better in the long run to not do so, and make it a component within a scene instead.

-------------------------

nickwebha | 2021-07-28 15:50:05 UTC | #10

[quote="lebrewer, post:8, topic:6933"]
How to do things the “Urho” way...
[/quote]
There are many great books on the topic but I agree. Something from the Urho3D community would be Urho3D specific and take a lot of the guess work out of it (which pattern do I use where, etc).

In the-- hopefully not too-distant-- future one of us could write it.

[quote="SirNate0, post:9, topic:6933"]
`Scene is set when you add the component to a node`
[/quote]
I think my whole architecture is just wrong. It has gotten me to a point where I have players running around, shooting each other, doing damage, etc. They just need a way to communicate with each other. Going to have to play with what gets instantiated where (the `scene`, for example).

I will play it with some more and check in later.

-------------------------

Dave82 | 2021-07-29 12:57:53 UTC | #11

You can create your Game class as a Subsystem. This way you can access it everywhere in you code ( even inside UI elements) by calling GetSubsystem<Game>(); Of course in this case the scene, camera and other elements should be created inside this subsystem. You should also expand your Game subsystem with a GetRootScene(); to access the scene and GetMainCamera() by getting the camera etc.

-------------------------

Modanung | 2021-07-31 08:12:53 UTC | #12

[quote="Dave82, post:11, topic:6933"]
This way you can access it everywhere in you code [...] by calling GetSubsystem()
[/quote]

"Through any (subclass of) `Object` within the same `Context`" would be more accurate.

-------------------------

nickwebha | 2021-08-03 13:09:37 UTC | #13

For anyone looking at this thread later here is what I ended up doing:
I turned everything (except the weapons and projectiles) into `Component`s. Once they are part of a node they are really easy to get to during a collision event. For example:

```
void Level::HandleObjectCollisionStart( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	auto* rigidBody1 = static_cast< Urho3D::RigidBody* >( eventData[ Urho3D::NodeCollisionStart::P_BODY ].GetPtr() );
	auto* node1 = rigidBody1->GetNode();
	auto* player1 = rigidBody1->GetComponent< Player >();
	const auto name1 = node1->GetName();

	auto* rigidBody2 = static_cast< Urho3D::RigidBody* >( eventData[ Urho3D::NodeCollisionStart::P_OTHERBODY ].GetPtr() );
	auto* node2 = rigidBody2->GetNode();
	const auto name2 = node2->GetName();

	if ( name2 == "CannonBall" ) {
		if ( player1->TakeDamage( WEAPON_CANNON_DAMAGE ) )
			player1->Respawn( node1, this->terrainNode_->GetComponent< Urho3D::Terrain >() );

		this->PlaySound( "Sound/Hit.ogg" );
	}
	else if ( name2 == "Rocket" ) {
		if ( player1->TakeDamage( WEAPON_ROCKET_DAMAGE ) )
			player1->Respawn( node1, this->terrainNode_->GetComponent< Urho3D::Terrain >() );

		this->PlaySound( "Sound/Hit.ogg" );
	}
	else if ( name2 == "RocketBarrage" ) {
		if ( player1->TakeDamage( WEAPON_ROCKETBARRAGE_DAMAGE ) )
			player1->Respawn( node1, this->terrainNode_->GetComponent< Urho3D::Terrain >() );

		this->PlaySound( "Sound/Hit.ogg" );
	}
	else if ( name2 == "Bullet" ) {
		if ( player1->TakeDamage( WEAPON_MACHINEGUN_DAMAGE ) )
			player1->Respawn( node1, this->terrainNode_->GetComponent< Urho3D::Terrain >() );

		this->PlaySound( "Sound/Hit.ogg" );
	}
	else if ( name2 == "Crate" ) {
		player1->RandomWeapon();

		this->PlaySound( "Sound/PickUp.ogg" );
	}
};
```
(Notice the `GetComponent< Player >()` line for the player, for example.)

Everything else (like who did damage to who) are shoved into the events themselves:
```
void Level::Update( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
...
	eventData[ scene ] = this->scene_;
	eventData[ terrain ] = this->terrainNode_;
	eventData[ playerComponent ] = playerComponent;
	playerComponent->Update( eventType, eventData );
...
}
```
(`playerComponent->Update( eventType, eventData )` calls the update for weapons.)

Remember to pass by reference where appropriate.

It is a little hacky but seems safe to do and is very flexible.

Do not take this as gospel, I am still new to all this.

-------------------------

vmost | 2021-08-03 23:37:44 UTC | #14

You may want to check the `eventType` before accessing the data

```
void Level::HandleObjectCollisionStart( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
    // check eventType
	auto* rigidBody1 = static_cast< Urho3D::RigidBody* >( eventData[ Urho3D::NodeCollisionStart::P_BODY ].GetPtr() );
...
}
```

-------------------------

lebrewer | 2021-08-06 19:43:06 UTC | #15

Thank you for sharing your solution with us. As a beginner, this is pure gold.

-------------------------

nickwebha | 2021-08-22 14:25:01 UTC | #16

I am still working on a "global" example architecture for a blog post; Trying to help people who are new to the engine get their feet wet with some boilerplate. I have run into a strange issue.

When I do:
```
this->GetContext()->RegisterSubsystem< Level >();
this->GetSubsystem< Level >()->Start();
```
everything works great. I get my level and my camera to zoom around with. It even prints "Level" like it should.

When I change it to:
```
this->GetContext()->RegisterSubsystem< Level >();
this->GetSubsystem< Level >()->Start();

this->GetContext()->RegisterSubsystem< Balls >();
this->GetSubsystem< Balls >()->Start();
```
I get:

```
u3da: /home/nick/Urho3D/build.linux/include/Urho3D/Audio/../Core/../Core/../Container/Ptr.h:133: T* Urho3D::SharedPtr<T>::operator->() const [with T = Urho3D::Scene]: Assertion `ptr_' failed.*
*Aborted (core dumped)
```

*Level* is defined as:

```
#pragma once

#include <iostream>

#include <Urho3D/Urho3DAll.h>

#include "constants.hpp"

class Level : public Urho3D::Component {
	private:
		#ifdef __DEBUG__
			bool drawDebug_;

			void HandlePostRenderUpdate( Urho3D::StringHash, Urho3D::VariantMap& );
		#endif

		Urho3D::SharedPtr< Urho3D::Scene > scene_;
		Urho3D::SharedPtr< Urho3D::Node > cameraNode_;
		Urho3D::SharedPtr< Urho3D::Node > terrainNode_;

	public:
		explicit Level( Urho3D::Context* context ) : Urho3D::Component( context ) {
			#ifdef __DEBUG__
				this->drawDebug_ = false;
			#endif
		};

		virtual void Start( void );
		virtual void Stop( void );
		virtual void Update( Urho3D::StringHash, Urho3D::VariantMap& );

		#ifdef __DEBUG__
			void setDebug( const bool );
			bool getDebug( void );
		#endif

		Urho3D::SharedPtr< Urho3D::Scene > getScene( void );
		Urho3D::SharedPtr< Urho3D::Node > getCamera( void );
		Urho3D::SharedPtr< Urho3D::Node > getTerrain( void );

		void rotateCamera( const float, const float );
		void moveCamera( const Urho3D::Vector3& );
};
```
```
#include <level.hpp>

#ifdef __DEBUG__
	void Level::HandlePostRenderUpdate( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
		if ( this->drawDebug_ )
			this->scene_->GetComponent< Urho3D::PhysicsWorld >()->DrawDebugGeometry( true );
	};
#endif

void Level::Start( void ) {
std::cout << "Level" << std::endl;
	this->scene_ = new Urho3D::Scene( this->GetContext() );

	#ifdef __DEBUG__
		this->scene_->CreateComponent< Urho3D::DebugRenderer >();
	#endif

	this->scene_->CreateComponent< Urho3D::Octree >();

	auto* cache = this->GetSubsystem< Urho3D::ResourceCache >();

	auto* physicsWorld = this->scene_->CreateComponent< Urho3D::PhysicsWorld >();
	physicsWorld->SetGravity( Urho3D::Vector3( 0, WORLD_GRAVITY, 0 ) );

	this->cameraNode_ = new Urho3D::Node( this->GetContext() );
	this->cameraNode_->SetTransform( Urho3D::Vector3( 0.0f, 250.0f, 0.0f ), Urho3D::Quaternion( 90.0f, 0.0f, 0.0f ) );
	auto* camera = this->cameraNode_->CreateComponent< Urho3D::Camera >();
	camera->SetFarClip( 500.0f );

	auto* zoneNode = this->scene_->CreateChild( "Zone" );
	auto* zone = zoneNode->CreateComponent< Urho3D::Zone >();
	zone->SetBoundingBox( Urho3D::BoundingBox( Urho3D::Sphere( Urho3D::Vector3::ZERO, 200 ) ) );
	zone->SetAmbientColor( Urho3D::Color( 0.15f, 0.15f, 0.15f ) );
	zone->SetFogColor( Urho3D::Color( 0.0f, 0.0f, 0.0f ) );
	zone->SetFogStart( 400.0f );
	zone->SetFogEnd( 500.0f );

	auto* lightNode = this->scene_->CreateChild( "Light" );
	lightNode->SetDirection( Urho3D::Vector3( 0.8f, -1.0f, 0.8f ) );
	auto* light = lightNode->CreateComponent< Urho3D::Light >();
	light->SetLightType( Urho3D::LIGHT_DIRECTIONAL );
	light->SetCastShadows( true );
	light->SetSpecularIntensity( 1.0f );
	light->SetColor( Urho3D::Color( 1.0f, 1.0f, 1.0f ) );

	auto* skyNode = this->scene_->CreateChild( "Sky" );
	auto* skybox = skyNode->CreateComponent< Urho3D::Skybox >();
	skybox->SetModel( cache->GetResource< Urho3D::Model >( "Models/Box.mdl" ) );
	skybox->SetMaterial( cache->GetResource< Urho3D::Material >( "Materials/Skybox.xml" ) );

	this->terrainNode_ = this->scene_->CreateChild( "Terrain" );
	this->terrainNode_->SetPosition( Urho3D::Vector3::ZERO );
	auto* terrain = this->terrainNode_->CreateComponent< Urho3D::Terrain >();
	terrain->SetPatchSize( 32 );
	terrain->SetSpacing( Urho3D::Vector3( 1.0f, 0.25f, 1.0f ) );
	terrain->SetSmoothing( true );
	terrain->SetHeightMap( cache->GetResource< Urho3D::Image >( "Textures/HeightMap.png" ) );
	terrain->SetMaterial( cache->GetResource< Urho3D::Material >( "Materials/Terrain.xml" ) );
	terrain->SetOccluder( true );

	auto* rigidBody = this->terrainNode_->CreateComponent< Urho3D::RigidBody >();
	rigidBody->SetFriction( 0.1f );
	rigidBody->SetCollisionLayerAndMask( LayerFlagsTerrain, LayerFlagsPlayer );

	auto* collisionShape = this->terrainNode_->CreateComponent< Urho3D::CollisionShape >();
	collisionShape->SetTerrain();

	auto* renderer = this->GetSubsystem< Urho3D::Renderer >();
	Urho3D::SharedPtr< Urho3D::Viewport > viewport( new Urho3D::Viewport( this->GetContext(), this->scene_, this->cameraNode_->GetComponent< Urho3D::Camera >() ) );
	renderer->SetViewport( 0, viewport );

	#ifdef __DEBUG__
		SubscribeToEvent( Urho3D::E_POSTRENDERUPDATE, URHO3D_HANDLER( Level, HandlePostRenderUpdate ) );
	#endif
};

void Level::Stop( void ) {
	#ifdef __DEBUG__
		UnsubscribeFromEvent( Urho3D::E_POSTRENDERUPDATE );
	#endif
};

void Level::Update( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {};

#ifdef __DEBUG__
	void Level::setDebug( bool enable ) {
		this->drawDebug_ = enable;
	};

	bool Level::getDebug( void ) {
		return this->drawDebug_;
	};
#endif

Urho3D::SharedPtr< Urho3D::Scene > Level::getScene( void ) {
	return this->scene_;
};

Urho3D::SharedPtr< Urho3D::Node > Level::getCamera( void ) {
	return this->cameraNode_;
};

Urho3D::SharedPtr< Urho3D::Node > Level::getTerrain( void ) {
	return this->terrainNode_;
};

void Level::rotateCamera( const float pitch, const float yaw ) {
	this->cameraNode_->SetRotation( Urho3D::Quaternion( pitch, yaw, 0.0f ) );
};

void Level::moveCamera( const Urho3D::Vector3& vector3 ) {
	this->cameraNode_->Translate( vector3 );
};
```

*Balls* is define as:
```
#pragma once

#include <iostream>

#include <Urho3D/Urho3DAll.h>

#include "constants.hpp"
#include "level.hpp"

class Balls : public Urho3D::Component {
	private:
		Urho3D::SharedPtr< Urho3D::Node > balls_[ BALLS_COUNT ];

		void HandleObjectCollisionStart( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData );

	public:
		explicit Balls( Urho3D::Context* context ) : Urho3D::Component( context ) {};

		virtual void Start( void );
};
```
```
#include <balls.hpp>

void Balls::HandleObjectCollisionStart( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	auto* rigidBody1 = static_cast< Urho3D::RigidBody* >( eventData[ Urho3D::NodeCollisionStart::P_BODY ].GetPtr() );
	auto* node1 = rigidBody1->GetNode();
	const auto name1 = node1->GetName();

	auto* rigidBody2 = static_cast< Urho3D::RigidBody* >( eventData[ Urho3D::NodeCollisionStart::P_OTHERBODY ].GetPtr() );
	auto* node2 = rigidBody2->GetNode();
	const auto name2 = node2->GetName();

	if ( name2 == "Player" ) {
		UnsubscribeFromEvent( node1, Urho3D::E_NODECOLLISIONSTART );

		node1->Remove();
	}
};

void Balls::Start( void ) {
std::cout << "Balls" << std::endl;
	for ( short int i = 0 ; i < BALLS_COUNT ; i++ ) {
		auto* cache = this->GetSubsystem< Urho3D::ResourceCache >();
		auto* level = this->GetSubsystem< Level >();

		this->balls_[ i ] = level->getScene()->CreateChild( "Ball" );
		const auto& ball = this->balls_[ i ];

		Urho3D::Vector3 position( Urho3D::Random( -50, 50 + 1 ), 0.0f, Urho3D::Random( -50, 50 + 1 ) );
		position.y_ = level->getTerrain()->GetComponent< Urho3D::Terrain >()->GetHeight( position ) + 10.0f;
		ball->SetPosition( position );
		ball->SetScale( Urho3D::Vector3( 10.0f, 10.0f, 10.0f ) );

		auto* object = ball->CreateComponent< Urho3D::StaticModel >();
		object->SetModel( cache->GetResource< Urho3D::Model >( "Models/Sphere.mdl" ) );
		object->SetMaterial( cache->GetResource< Urho3D::Material >( "Materials/Stone.xml" ) );
		object->SetCastShadows( true );

		auto* rigidBody = ball->CreateComponent< Urho3D::RigidBody >();
		rigidBody->SetMass( 1.0f );
		rigidBody->SetFriction( 0.1f );
		rigidBody->SetCollisionLayerAndMask( LayerFlagsBall, LayerFlagsTerrain | LayerFlagsPlayer );

		auto* collisionShape = ball->CreateComponent< Urho3D::CollisionShape >();
		collisionShape->SetSphere( 1, Urho3D::Vector3( 0, .5, 0 ) );

		SubscribeToEvent( ball, Urho3D::E_NODECOLLISIONSTART, URHO3D_HANDLER( Balls, HandleObjectCollisionStart ) );
	}
};
```

I can not find where this issue is. It prints "*Level*" and "*Balls*" but then crashes. Even if I comment out the function bodies (except the `cout`) in *Balls* it still crashes but now with
```
u3da: /home/nick/Urho3D/build.linux/include/Urho3D/Audio/../Core/../Core/../Container/Ptr.h:133: T* Urho3D::SharedPtr<T>::operator->() const [with T = Urho3D::Node]: Assertion `ptr_' failed.*
*Aborted (core dumped)
```

What am I missing?

Maybe there is the possibility of turning this into a Sample one day in the future (after a lot of work and some [convention](https://urho3d.io/documentation/HEAD/_coding_conventions.html) changes.)

-------------------------

vmost | 2021-08-22 15:17:15 UTC | #17

Can you post a minimum reproducible example?

Also, within class member functions, member variables and functions can be accessed without explicitly dereferencing the `this` pointer.

```
class Foo final
{
public:
    int get_x() { return x; }
    //int get_x() { return this->x; }  //equivalent
private:
    int x{5};
};
```

-------------------------

nickwebha | 2021-08-22 16:24:08 UTC | #18

[quote="vmost, post:17, topic:6933"]
within class member functions, member variables and functions can be accessed without explicitly dereferencing the `this` pointer
[/quote]
I know. I just like to be explicit. It is a personal quirk.

[quote="vmost, post:17, topic:6933"]
Can you post a minimum reproducible example?
[/quote]
I created a [GitHub repo](https://github.com/nickwebha/urho3d-architecture). The only relevant files are *world.[hpp/cpp]* and *balls.[hpp/cpp]*. I know it is supposed to be a minimum reproducible example but just ignore the rest of the files (I think).

-------------------------

vmost | 2021-08-22 16:46:28 UTC | #19

Is this a minimum reproducible example? There seems to be a lot of code unrelated to the problem (e.g. does the problem persist if you remove the 'Sky'?).

-------------------------

nickwebha | 2021-08-22 18:06:22 UTC | #20

Still working on a minimum reproducible example. It is proving hard to strip down due to its minimalist nature.

I noticed two odd things.

First, when I add:
```
virtual Urho3D::StringHash GetType( void ) const;
virtual const Urho3D::String& GetTypeName( void ) const;
virtual const Urho3D::TypeInfo* GetTypeInfo( void ) const;
```

```
Urho3D::StringHash Balls::GetType( void ) const {
	return "Balls";
};

const Urho3D::String& Balls::GetTypeName( void ) const {
	static Urho3D::String name( "Balls" );

	return name;
};

const Urho3D::TypeInfo* Balls::GetTypeInfo( void ) const {
	return GetTypeInfoStatic();
};
```
to `Balls` it compiles and runs. `Level` does not require this despite them both inheriting from `Urho3D::Component`.

The second odd thing is *Level* is being printed to the console twice (notice the `cout`'s above) with:
```
this->GetContext()->RegisterSubsystem< Level >();
this->GetSubsystem< Level >()->Start();

this->GetContext()->RegisterSubsystem< Balls >();
this->GetSubsystem< Balls >()->Start();
```

If I comment out `this->GetSubsystem< Balls >()->Start()` it only prints *Level* once.

-------------------------

SirNate0 | 2021-08-22 18:15:44 UTC | #21

I'm pretty sure (after skimming the code, so I might be wrong) that your problem is that you're missing the `URHO3D_OBJECT(Level,Component)` macro call from your classes that tells the library that they are different classes (the macro defines the virtual functions and such that are used to provide the keys for a a HashMap to store the Subsystems and the factories to create objects.

-------------------------

nickwebha | 2021-08-22 18:41:54 UTC | #22

[quote="SirNate0, post:21, topic:6933"]
your problem is that you’re missing the `URHO3D_OBJECT(Level,Component)` macro
[/quote]
That was it. I had no idea that existed. Not sure how, since they are all over the samples. Big oversight on my part.

Thank you so much!

-------------------------

nickwebha | 2021-08-28 17:57:12 UTC | #23

Just wanted to put [this](https://discourse.urho3d.io/t/minimalist-urho3d-architecture-boilerplate/) here.

-------------------------

