nickwebha | 2021-08-13 18:50:57 UTC | #1

I am trying to add homing rockets to my tank game. So far I have:
```
rigidBody->SetUseGravity( false );
rigidBody->SetLinearVelocity( Urho3D::Vector3( sin( objectNodeRotation * M_PI / 180 ), 0, cos( objectNodeRotation * M_PI / 180 ) ) * WEAPON_HOMINGROCKET_SPEED );
...
void WeaponHomingRocket::Update( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData ) {
	auto* physicsWorld = scene->GetComponent< Urho3D::PhysicsWorld >();
	for ( auto i = this->projectiles_.begin(); i != this->projectiles_.end() ; i++ ) {
		auto position = i->node_->GetPosition();
		Urho3D::PhysicsRaycastResult hitResults;
		Urho3D::Ray ray( position, Urho3D::Vector3::ONE );
		physicsWorld->SphereCast( hitResults, ray, WEAPON_HOMINGROCKET_HOMING_DISTANCE, WEAPON_HOMINGROCKET_HOMING_DISTANCE, LayerFlagsPlayer );

		Urho3D::RigidBody* resultBody{ hitResults.body_ };
		if ( resultBody ) {
			auto* resultNode = resultBody->GetNode();
			auto* resultPlayer = resultNode->GetComponent< Player >();

			if ( playerComponent->GetId() != resultPlayer->GetId() ) {
				auto resultPosition = resultNode->GetWorldPosition();

				i->node_->LookAt( resultPosition );

				i->objectNodeRotationCurrent_ = i->node_->GetRotation().YawAngle();

				auto* rigidBody = i->node_->GetComponent< Urho3D::RigidBody >();
				rigidBody->ApplyForce( Urho3D::Vector3( sin( i->objectNodeRotationCurrent_ * M_PI / 180 ), 0, cos( i->objectNodeRotationCurrent_ * M_PI / 180 ) ) * WEAPON_HOMINGROCKET_HOMING_SPEED );

				#ifdef __DEBUG__
					auto* debugRenderer = scene->GetComponent< Urho3D::DebugRenderer >();
					Urho3D::Sphere sphere( resultPosition, WEAPON_HOMINGROCKET_HOMING_DISTANCE );
					debugRenderer->AddSphere( sphere, Urho3D::Color::RED );
				#endif
			}
		}
	...
	}
}
```
and it works pretty well.

My problem is `SphereCast()`. None of the samples use it and I can not find it explained in the wiki or on the forums. That along with `Urho3D::Ray` which I have no idea how to use. It half works with this code but often does not track any targets or only does for a brief moment.

At the moment I do not care if it crashes into walls on its way to the target. Once I better understand `Urho3D::Ray` I can probably figure that part out on my own.

So how is `SphereCast()` used with `Urho3D::Ray`?

-------------------------

throwawayerino | 2021-08-13 19:21:30 UTC | #2

Physics `SphereCast()` internally does a bullet "sweep cast", where it moves a sphere from A to B as defined by `ray` and `distance` and returns first hit. You probably want to set `radius` to 3 or something similar because I think the sphere you're creating is massive
This tests for rigidbodies, octree queries test for drawables in case you want something simpler.
Also I think people prefer sphere casts more than straight ray casts, can't remember why.

-------------------------

nickwebha | 2021-08-13 19:25:07 UTC | #3

[quote="throwawayerino, post:2, topic:6967"]
You probably want to set `radius` to 3 or something similar
[/quote]
Here are my defines:

```
#define WEAPON_HOMINGROCKET_SPEED			25
#define WEAPON_HOMINGROCKET_DISTANCE		5000
#define WEAPON_HOMINGROCKET_DAMAGE			500
#define WEAPON_HOMINGROCKET_DELAY			2500
#define WEAPON_HOMINGROCKET_HOMING_SPEED	50
#define WEAPON_HOMINGROCKET_HOMING_DISTANCE	3
```

Now that `WEAPON_HOMINGROCKET_HOMING_DISTANCE` is 3 the rocket has to get awfully-- I mean very-- close to a target to detect it. Still, however, my problem is this only detects a nearby object ~50% of the time with everything in the same position (I fire multiple shots without moving anything).

-------------------------

throwawayerino | 2021-08-13 19:36:18 UTC | #4

It's supposed to return the first `rigidbody` it finds. Is it detecting the ground or something, or is it just straight up returning null pointers?
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Physics/PhysicsWorld.cpp#L484

-------------------------

nickwebha | 2021-08-13 19:42:29 UTC | #5

I have layers and masks setup so it only detect players. I am checking for `null` (which is most of it returns).

The
```
#ifdef __DEBUG__
...
#endif
```
is helping me see what it is returning. When I first started playing with it it was detecting the terrain but I fixed that with the layers/masks (notice the `LayerFlagsPlayer`).

Here is an example:
https://www.youtube.com/watch?v=EWntSGDTehM

Notice how it works at the start but does not work towards the end in this case.

-------------------------

throwawayerino | 2021-08-13 20:16:42 UTC | #6

Now I'm just going to start throwing suggestions around until someone better than me shows up.
* The problem showed up after the new tank was spawned in(?). Maybe the rigidbody is getting deactivated or maybe is set up different. 

* Note that the ray you're casting will always point to **(1,1,1)**. `direction` is relative to origin so put in `GetWorldDirection()`
* Another option is to ditch physics altogether and use Octree queries instead. The closest thing it has to sphere sweep casts is the box query though and you would have to redo the detection code.

-------------------------

nickwebha | 2021-08-13 20:54:20 UTC | #7

Thanks for the assist. I appreciate it.

* I thought of something happening to the rigidbody after respawn. However I can still collide with it with the other players and it still some times works. I can confirm it not working after respawn in the video was a coincidence.
* I changed to `GetWorldDirection()`. That was a good catch, thanks for that. I changed `Urho3D::Vector3::ONE` to `Urho3D::Vector3::FORWARD` for giggles (I still do not grasp why it should be one or the other).
* This whole physics-based approach is what used to ditch the old approach. The "old way" was way too cumbersome doing it all manually myself.

I am betting that `GetWorldDirection()` change was important.

I changed
`Urho3D::Ray ray( i->node_->GetPosition(), Urho3D::Vector3::ONE )`
to
`Urho3D::Ray ray( i->node_->GetWorldPosition(), i->node_->GetWorldDirection() );`

It seems to be working a lot better now. I will have to spend some more time playing with it and report back.

-------------------------

throwawayerino | 2021-08-13 21:05:32 UTC | #8

Good luck mate. One last thing, try visualizing the sphere cast (and any others) with a debug cylinder if you could.

-------------------------

nickwebha | 2021-08-18 17:40:47 UTC | #9

`Urho3D::Ray ray( i->node_->GetWorldPosition(), i->node_->GetWorldDirection() )` was the key.

Working great now.

Thanks for your help!

-------------------------

