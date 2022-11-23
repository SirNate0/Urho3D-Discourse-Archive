1vanK | 2017-09-10 15:33:44 UTC | #1

First experiments. Any help is welcome

 https://github.com/1vanK/Urho3DKinematicCharacterController

https://youtu.be/MT_KgxlEeMw

-------------------------

Enhex | 2017-09-11 01:31:03 UTC | #2

Looks good.

Try testing things like:
- pushing against corners
- pushing against stacked vertically segmented wall, so you collide with several segments at once
- pushing against downward slopes

-------------------------

1vanK | 2017-09-12 14:37:42 UTC | #3

can you provide scene to reproduce?

-------------------------

Enhex | 2017-09-12 16:52:10 UTC | #4

each segment is a rigid body:
![segments|580x400](upload://ggMaJ9vYbNWl2Vcc7Jw3aIFnHYp.png)
![slope|580x400](upload://iUkwm1lwgUKuXoPiN7bimZLaoND.png)

-------------------------

mazataza | 2017-11-30 06:58:50 UTC | #5

i have a few question about your code ( i have not tested it yet)

why you use  z-axis as up vector?


    bulletController_ = new btKinematicCharacterController(ghostObject_, capsule, 0.3f, btVector3(0, 0, 1));


and later you use DOWN vector here

    btTransform t;
    t = bulletController_->getGhostObject()->getWorldTransform();
    Vector3 newPos = ToVector3(t.getOrigin()) + Vector3::DOWN * height_ * 0.5f;

i would like to understand the mathematic behind it or kinematic ..

from the youtube video it looks promising

-------------------------

1vanK | 2017-11-30 10:12:22 UTC | #6

It does not matter which vector I'm setting. Vertical direction is rewritted when ```bulletController_->setGravity(world->getGravity());```

-------------------------

mazataza | 2017-11-30 10:20:41 UTC | #7

ok thanks,

when i try to run the code "I use clion with cmake" I got SIGSEGV during initialising the Application in

    Game(Context* context) : Application(context)

exactly in the code in Urho3d Timer.cpp

    String Time::GetTimeStamp()
    {
         time_t sysTime;
         time(&sysTime); // here we got SIGSEGV
         const char* dateTime = ctime(&sysTime);
         return String(dateTime).Replaced("\n", "");
    }

which get called when initialisng input and try to Log something

it seems theres some memory damage some where which i don't know

-------------------------

1vanK | 2017-11-30 10:31:47 UTC | #8

Have you copied GameData folder to *.exe dir?

EDIT: and Data+CoreData

-------------------------

mazataza | 2017-11-30 10:31:55 UTC | #9

yes i done ..
but as i said, it does reach the code which setup the game .. it crash on constructor of Game object

-------------------------

1vanK | 2017-11-30 10:36:15 UTC | #10

I'm sorry, I do not have experience with "clion" (and do not even know what it is xD ) I tested this code with VS 2015 and recheck now with VS 2017

-------------------------

mazataza | 2017-11-30 10:37:44 UTC | #11

no problem .. i will try to reconstruct the programm in another code example

-------------------------

mazataza | 2017-11-30 11:07:42 UTC | #12

it seems the issue with global variables and global.cpp
i habe removed global.h and global.cpp and used private variables in Game class and CharacterControl class then the example works.

again thanks for this great simple example

-------------------------

dev4fun | 2020-01-30 04:16:45 UTC | #13

How make this detectable for node collision?

-------------------------

