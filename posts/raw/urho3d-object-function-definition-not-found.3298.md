ppsychrite | 2017-07-01 21:06:38 UTC | #1

Currently trying to make a LogicComponent but it doesn't seem to be working. In the logs when I create it it gives me 

    ERROR: Could not create unknown component type 383225A1

The header and source for it is basic enough and seems fine to me 
Header:

    class Player : public LogicComponent {
	URHO3D_OBJECT(Player, ur::LogicComponent);
	public:

		Player(ur::Context *context);
		static void RegisterObject(ur::Context *context);
		virtual void Start();
		virtual void FixedUpdate(float deltaTime);

	private:
    };



Source:

    #include "Player.hpp"
    Player::Player(ur::Context *context) : ur::LogicComponent(context) {
	context->RegisterFactory<Player>();
    }

    void Player::RegisterObject(ur::Context *context) {
	
    }

    void Player::Start() {

    }

    void Player::FixedUpdate(float deltaTime) {

    }

What's causing it I believe is URHO3D_OBJECT, let me link what it's complaining about: http://prntscr.com/fqf2vo
Quite strange. :thinking:
Has anyone else encountered this happening before and found any solutions?

-------------------------

KonstantTom | 2017-07-01 21:06:30 UTC | #2

So, you should register your component factory in `RegisterObject`, for example:
```c++
context->RegisterFactory <Player> (/*component category*/);
```
And then, you should call this static function on application startup.
Also, in this function you should register object attributes (if you need it, of course). Attributes can be automatically serialized and replicated over network. Attribute registration example:
```c++
URHO3D_MIXED_ACCESSOR_ATTRIBUTE ("War Hash", GetWarHash, SetWarHash, Urho3D::StringHash, Urho3D::StringHash::ZERO, Urho3D::AM_DEFAULT);
```
PS. Don't write namespace names to URHO3D_OBJECT macro. So it should look like:
```c++
URHO3D_OBJECT(Player, LogicComponent)
```

-------------------------

1vanK | 2017-07-01 16:53:04 UTC | #3

move context->RegisterFactory<Player>(); to RegisterObject() and call before using class

-------------------------

ppsychrite | 2017-07-01 17:12:08 UTC | #4

Aha! It works fine now! :slight_smile:
I guess I didn't look over the AnimatedScene example thoroughly

-------------------------

