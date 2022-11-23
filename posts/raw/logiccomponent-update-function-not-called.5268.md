throwawayerino | 2019-06-30 13:10:01 UTC | #1

With or without setting the update mask, no matter what I try the update function is never called. I made sure it's the same signature, I made it public and private, but it just won't run. Subscribing to my own custom HandleUpdate method works, but the inherited virtual function doesn't. Am I missing something?

-------------------------

Lumak | 2019-06-30 14:39:28 UTC | #2

Be sure to set the correct bitmask. There are four types:
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/LogicComponent.h#L31

And each corresponds to specific virtual fn.

Take a look at some samples that make use of LogicComponents: 
https://github.com/urho3d/Urho3D/blob/master/Source/Samples/18_CharacterDemo/Character.cpp#L41

-------------------------

Modanung | 2019-06-30 17:46:31 UTC | #3

Since C++11 you can make sure you're not creating a new base virtual function by appending the `override` keyword instead of prepending `virtual` to a function declaration. This will cause a compiler error when no superclass has a virtual function with a matching signature.
The default update event mask of a **`Logic`**`Component` *should* do.

-------------------------

throwawayerino | 2019-07-01 12:39:16 UTC | #4

I set the bitmask to `USE_UPDATE`  and made sure I was overriding a function. No compiler errors, and the debugger shows that the function is never called

-------------------------

throwawayerino | 2019-07-01 12:50:43 UTC | #5

What's even more annoying is that other components have their virtual functions called normally

-------------------------

Modanung | 2019-07-01 13:09:35 UTC | #6

Is there an `URHO3D_OBJECT(SubClass, SuperClass)` inside your class declaration?
`

-------------------------

throwawayerino | 2019-07-01 13:14:13 UTC | #7

Yes
20 character limit

-------------------------

Modanung | 2019-07-01 13:17:36 UTC | #8

I think I'm out of guesses; could you share some code?

-------------------------

throwawayerino | 2019-07-01 13:21:30 UTC | #9

I can't guess what could be wrong too
Header:
```
class GameManager : public LogicComponent
{
	URHO3D_OBJECT(GameManager, LogicComponent)

public:
	explicit GameManager(Context* context);
	~GameManager() = default;

	static void RegisterObject(Context* context);

	virtual void OnSceneSet(Scene* scene) override;

	virtual void Update(float Timestep) override;
}
```
Cpp file:
```
GameManager::GameManager(Context* context)
	: LogicComponent(context)
{
	// Unsubscribe from all but update
	// For some reason no functions are called
	//SetUpdateEventMask(USE_UPDATE);
	URHO3D_LOGDEBUG("Game manager constructor called");
}

void GameManager::Update(float Timestep)
{
	if (timer->GetMSec(false) >= 500 && CurrentControl != nullptr) {
		URHO3D_LOGINFO(String("500ms have passed!");
		timer->Reset();
	}
}
```
How it's made in main.cpp:
```
GameManage = MainScene->CreateComponent<GameManager>();	
```

-------------------------

Modanung | 2019-07-02 19:39:51 UTC | #10

Prepending `virtual` nullifies the `override` keyword. They should not be used on the same declaration.

Could you try logging the update outside of the timer check? Just to make sure the `if` isn't to blame.

-------------------------

throwawayerino | 2019-07-01 13:33:55 UTC | #11

The `if` is correct, because I've put it in a seperate `HandleUpdate` I made before and it worked. Still, I put it out of the `if` and yet it didn't work
Either way, it's just a little inconvenience. Manually subscribing to Update events works and I can live with it.

-------------------------

Modanung | 2019-07-01 13:48:27 UTC | #12

Also no errors or warnings being logged? Maybe something about a failed instantiation of an unknown component. Though I guess the "Game manager constructor called" should exclude that possibility, does it show up? It just seems strange for a simple setup like this to not work.

-------------------------

throwawayerino | 2019-07-01 13:44:31 UTC | #13

Nothing related to it is logged. Logging from constructor works and I used the component successfuly for other things. Actually, I don't think I need it to be a logic component either way. Thanks for the help

-------------------------

guk_alex | 2019-07-01 14:18:07 UTC | #14

Do you have RegisterObject defined in your cpp code?

-------------------------

lezak | 2019-07-02 10:00:02 UTC | #15

[quote="throwawayerino, post:9, topic:5268"]
virtual void OnSceneSet(Scene* scene) override;
[/quote]

Do You call LogicComponent::OnSceneSet here? Events subscriptions are set in this method, so if You override it, this may be the reason of Your problem.

-------------------------

Lumak | 2019-07-01 16:28:12 UTC | #16

Need to uncomment the line in your ctor:
```
//SetUpdateEventMask(USE_UPDATE);
```

-------------------------

throwawayerino | 2019-07-02 10:00:48 UTC | #17

I can't believe I forgot this. Thanks!

-------------------------

Modanung | 2019-07-02 19:46:52 UTC | #18

That should not be required...
https://discourse.urho3d.io/t/positioning-nodes-in-screen-space/121/6

-------------------------

Lumak | 2019-07-02 20:28:34 UTC | #19

Ha, I forgot that's how it works. I wonder why it's defaulted to calling all four empty functions?
But thx Modanung!

-------------------------

Modanung | 2019-07-03 01:29:47 UTC | #20

I guess it's the more convenient default that makes sure you don't forget setting the right update event mask, instead of leaving you guessing why things don't work as expected? ;)


 > *"97% of the time premature optimization is the root of all evil."* -- Donald Knuth

Alternatively one can use the `Component` class to inherit from. The main difference is that it lacks this update event mask and the associated virtual functions.

-------------------------

