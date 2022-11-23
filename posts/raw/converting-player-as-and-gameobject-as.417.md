vivienneanthony | 2017-01-02 01:00:14 UTC | #1

Hello

Did anyone get player.as or gameobject.as to a c++ equivalent? I want to start adding character ability at it simplest health?


1. a) I was thinking of modifying the character to adding relevant information.
    /// Register Character component
    character_ = objectNode->CreateComponent<Character>();
   b) Adding more complexities, like a character can be a AI with a attached script.

2. As for gameobject maybe create a component for that as well.
  With a parent node ID or child. (Aka spaceship exta)

If that makes sense.

Vivienne

-------------------------

scorvi | 2017-01-02 01:00:14 UTC | #2

hey,

i did convert the ninja game example to c++ (with bugs :-/ ) and tried converting the editor to c++ but did not finished it ... 
i can upload it to github if someone wants to see or work with it :slight_smile:

-------------------------

vivienneanthony | 2017-01-02 01:00:14 UTC | #3

[quote="scorvi"]hey,

i did convert the ninja game example to c++ (with bugs :-/ ) and tried converting the editor to c++ but did not finished it ... 
i can upload it to github if someone wants to see or work with it :slight_smile:[/quote]

Yea. That would be cool

-------------------------

vivienneanthony | 2017-01-02 01:00:14 UTC | #4

I modified the Character.h and Character.cpp.

[b]Character.cpp[/b]
[code]
#pragma once

//#include "Player.h"
#include "Controls.h"
#include "LogicComponent.h"
#include "Player.h"

using namespace Urho3D;

const int CTRL_FORWARD = 1;
const int CTRL_BACK = 2;
const int CTRL_LEFT = 4;
const int CTRL_RIGHT = 8;
const int CTRL_JUMP = 16;

const float MOVE_FORCE = 0.8f;
const float INAIR_MOVE_FORCE = 0.02f;
const float BRAKE_FORCE = 0.2f;
const float JUMP_FORCE = 1.0f;
const float YAW_SENSITIVITY = 0.1f;
const float INAIR_THRESHOLD_TIME = 0.1f;

/// Character component, responsible for physical movement according to controls, as well as animation.
class Character : public LogicComponent
{
    OBJECT(Character)

public:
    /// Construct.
    Character(Context* context);

    /// Register object factory and attributes.
    static void RegisterObject(Context* context);

    /// Handle startup. Called by LogicComponent base class.
    virtual void Start();
    /// Handle physics world update. Called by LogicComponent base class.
    virtual void FixedUpdate(float timeStep);

    /// Movement controls. Assigned by the main program each frame.
    Controls controls_;

private:
    /// Handle physics collision event.
    void HandleNodeCollision(StringHash eventType, VariantMap& eventData);

    /// Grounded flag for movement.
    bool onGround_;
    /// Jump flag.
    bool okToJump_;
    /// In air timer. Due to possible physics inaccuracy, character can be off ground for max. 1/10 second and still be allowed to move.
    float inAirTimer_;

    Player CharacterPlayer;
};
[/code]

[b]Character.cpp[/b]
[code]
using namespace std;

Character::Character(Context* context) :
    LogicComponent(context),
    onGround_(false),
    okToJump_(true),
    inAirTimer_(0.0f),
    CharacterPlayer()
{
    // Only the physics update event is needed: unsubscribe from the rest for optimization
    SetUpdateEventMask(USE_FIXEDUPDATE);
}[/code]

This is the error I get when I compile it
[code]||=== Urho3D, all ===|
CMakeFiles/ExistenceClient.dir/Character.cpp.o||In function `Character::Character(Urho3D::Context*)':|
Character.cpp|| undefined reference to `Player::Player()'|
Character.cpp|| undefined reference to `Player::~Player()'|

CMakeFiles/ExistenceClient.dir/Character.cpp.o||In function `Character::~Character()':|
Character.cpp:(.text._ZN9CharacterD2Ev[_ZN9CharacterD5Ev]+0x17)||undefined reference to `Player::~Player()'|

CMakeFiles/ExistenceClient.dir/Character.cpp.o||In function `Character::~Character()':|
Character.cpp:(.text._ZN9CharacterD0Ev[_ZN9CharacterD5Ev]+0x17)||undefined reference to `Player::~Player()'|

CMakeFiles/ExistenceClient.dir/Character.cpp.o||In function `Urho3D::ObjectFactoryImpl<Character>::CreateObject()':|
::CreateObject()]+0x71)||undefined reference to `Player::Player()'|
::CreateObject()]+0xc4)||undefined reference to `Player::~Player()'|
||=== Build finished: 6 errors, 4 warnings ===|
[/code]

So I'm not sure whats wrong. I was thinking of the Chracter object to use a Player class. So I don't have to create major overhead for the GUI part.

Vivienne

-------------------------

scorvi | 2017-01-02 01:00:15 UTC | #5

[quote="vivienneanthony"]
Yea. That would be cool[/quote]

here : -) but it is really hacky :-/  
[url]https://github.com/scorvi/Urho3dEditor[/url]
[url]https://github.com/scorvi/Urho3dNinjaGameExample[/url]

-------------------------

vivienneanthony | 2017-01-02 01:00:15 UTC | #6

[quote="scorvi"][quote="vivienneanthony"]
Yea. That would be cool[/quote]

here : -) but it is really hacky :-/  
[url]https://github.com/scorvi/Urho3dEditor[/url]
[url]https://github.com/scorvi/Urho3dNinjaGameExample[/url][/quote]

I'm trying to figure out should I use the object method Player.h/Player.cpp uses. That would means I would have to do a different CPP/.H for every type of object I make.

Hmmm.

The only difference I see between Character and Player filer is that one uses a object and the other uses a component?

Maybe someone can enlighten me some.

-------------------------

vivienneanthony | 2017-01-02 01:00:15 UTC | #7

Initial post solved.

Still is it the best way to go about it. The character component loads a class for a Player (which has more information) but not necessary to the character component.

-------------------------

vivienneanthony | 2017-01-02 01:02:00 UTC | #8

[quote="scorvi"]hey,

i did convert the ninja game example to c++ (with bugs :-/ ) and tried converting the editor to c++ but did not finished it ... 
i can upload it to github if someone wants to see or work with it :slight_smile:[/quote]

I'm revisitng the code. Basically I stripped the character.cpp/character.h code to a base GameObject component. I am think of looping through a loaded scene and then setting each component lifetime and type base of the node.

I can have a separate class with all gameobjects but that's for future use, maybe to be able to allow looping through objects???

-------------------------

