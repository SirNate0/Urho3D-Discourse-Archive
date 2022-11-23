nickwebha | 2021-08-24 21:58:57 UTC | #1

I have the following code:
```
this->GetContext()->RegisterSubsystem< Player >();
this->GetContext()->RegisterFactory< PlayerComponent >();

this->GetSubsystem< Player >()->Start();
```
```
void Player::Start( void ) {
...
	auto* level = this->GetSubsystem< Level >();
	this->player_ = level->getScene()->CreateChild( "Player" );
	this->player_->CreateComponent< PlayerComponent >();
...
}
```
```
auto* playerComponent = this->GetSubsystem< Player >()->GetComponent< PlayerComponent >();

if ( input->GetKeyDown( Urho3D::KEY_W ) )
	playerComponent->MoveX( 1 );
if ( input->GetKeyDown( Urho3D::KEY_S ) )
	playerComponent->MoveX( -1 );
if ( input->GetKeyDown( Urho3D::KEY_A ) )
	playerComponent->MoveZ( 1 );
if ( input->GetKeyDown( Urho3D::KEY_D ) )
	playerComponent->MoveZ( -1 );
```
```
void PlayerComponent::MoveX( const float x ) {
	std::cout << this << std::endl;
};
```

When I call `playerComponent->MoveX()` I get `0`. It seems the `PlayerComponent` component is never being initialized.

The full code is on [GitHub](https://github.com/nickwebha/urho3d-architecture/).

-------------------------

Eugene | 2021-08-25 08:13:36 UTC | #2

Why `Player` is derived from `Component` if it's not a component?

-------------------------

SirNate0 | 2021-08-25 12:58:17 UTC | #3

This line is your problem.

```
auto* playerComponent = this->GetSubsystem< Player >()->GetComponent< PlayerComponent >();
```

Since Player is just a subsystem and not actually used as a component, it does not have a node, so GetComponent cannot get the PlayerComponent from the Player's node_, as it does not have one. Either add Player to a Node or make Player an Object instead of inheriting from Component.

---

Some other comments:
* You switched the case of `CoreData` and `Data` to `coreData` and `data`. It's your choice, of course, but why switch from what base Urho3D uses if you are going for a template project?
* It may have just been my setup, or maybe you modified Urho, but I had an issue compiling because Camera was ambiguous between `Urho3D::Camera` and your `Camera` class. I fixed that by changing it to `AppCamera` instead.
* The loading screen crashes if it cannot find the texture. You may want to handle this behavior more gracefully ([`ErrorExit()`](https://urho3d.io/documentation/HEAD/class_urho3_d_1_1_application.html#acfc44f7220002cf6c186e5c84ec036bc), or something, or just continue without the image).

-------------------------

nickwebha | 2021-08-25 17:37:56 UTC | #4

[quote="Eugene, post:2, topic:6977, full:true"]
Why `Player` is derived from `Component` if it’s not a component?
[/quote]
This is an excellent question. Probably a mistake from a copy and paste.

[quote="SirNate0, post:3, topic:6977"]
This line is your problem.
[/quote]
Ooohhh, that make sense. I am going to ask for a review of the overall architecture once it is "complete." I am still pretty new at all this.

[quote="SirNate0, post:3, topic:6977"]
You switched the case of `CoreData` and `Data` to `coreData` and `data` .
[/quote]
This has been a point of confusion for me. Since I never came a across description of which was which I decided that `coreData` is for things that get reused (shaders, fonts, etc) and `Data` is for single-use items (loading screens, terrain, some models, etc). I would love to hear suggestions or the way it "should" be done. What are the original purposes?

[quote="SirNate0, post:3, topic:6977"]
It may have just been my setup, or maybe you modified Urho, but I had an issue compiling because Camera was ambiguous between `Urho3D::Camera` and your `Camera` class.
[/quote]
I commented out `using namespace Urho3D;` in `Urho3DAll.h`. I am planning on fixing that error before release. In my opinion `using` should never have been put there in the first place but that is just my two cents.

[quote="SirNate0, post:3, topic:6977"]
The loading screen crashes if it cannot find the texture.
[/quote]
This is a good point; Probably a few other places, too. I will put it on the TODO list.

-------------------------

SirNate0 | 2021-08-25 18:10:41 UTC | #5

[quote="nickwebha, post:4, topic:6977"]
This has been a point of confusion for me. Since I never came a across description of which was which I decided that `coreData` is for things that get reused (shaders, fonts, etc) and `Data` is for single-use items (loading screens, terrain, some models, etc). I would love to hear suggestions or the way it “should” be done. What are the original purposes?
[/quote]
That's basically how I understand it as well. CoreData is for things that are in some ways internal to the engine - the shaders, the renderpath, the techniques. The Data directory is for everything that is more specific to your game. Arguably the UI texture should also be in CoreData, but since your game will probably have a custom skin in the end it's probably good that it doesn't. Since you can also create your own shaders and techniques, there's not a completely clear distinction. That said, my comment was only about changing the case of the folders, I felt you might want to use the original names.

[quote="nickwebha, post:4, topic:6977"]
I commented out `using namespace Urho3D;` in `Urho3DAll.h` . I am planning on fixing that error before release. In my opinion `using` should never have been put there in the first place but that is just my two cents.
[/quote]
The original reasoning was probably that if you wanted to include that rather than including individual headers you probably wouldn't want to also have to put
`using namespace Urho3D;` in every file. My two cents are that `using namespace` is great and makes the code much more readable. Ambiguous names can be specified if it ends up being an issue, but otherwise I don't need to know that Color is the one from Urho3D, as is the Vector3, etc. Though for a template project at least I could see avoiding it being a good idea.

-------------------------

nickwebha | 2021-08-28 16:49:28 UTC | #6

Not sure how those folders got renamed. I do not remember doing that. I changed it back.

[quote="SirNate0, post:5, topic:6977"]
My two cents are that `using namespace` is great and makes the code much more readable.
[/quote]
Agreed. I just think it belongs in the game code, not the engine headers. For example, imagine the `std` headers did this.

**Edit**
[Here](https://discourse.urho3d.io/t/urho3d-openssl-ui-conflict/6717/8/) is a real-world example.

-------------------------

