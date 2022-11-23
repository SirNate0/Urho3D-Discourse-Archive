pirogronian | 2019-08-28 13:55:26 UTC | #1


I wrote simple app based on web sample and realized it doesnt detect keyboard input (I didn't tested mouse and touch yet). Simplest code I made:
```
class Sim3D : public Application
{
    Scene *scene_;
    Node *cameraNode_;
public:
    Sim3D(Context *c) : Application(c) {}
    void Setup() override
    {
        engineParameters_["Fullscreen"] = false;
        engineParameters_["WindowWidth"] = 1024;
        engineParameters_["WindowWidth"] = 720;
        engineParameters_["WindowResizable"] = true;
    }

    void OnKeyDownDebug(StringHash evType, VariantMap &evData)
    {
        int key = evData[KeyDown::P_KEY].GetInt();
        String name = GetSubsystem<Input>()->GetKeyName(key);
        URHO3D_LOGINFO(name);
    }

    void Start() override
    {
        SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(Sim3D, OnKeyDownDebug));
    }
};

URHO3D_DEFINE_APPLICATION_MAIN(Sim3D)
```
Above is a test code I wrote after realizing GetKeyDown, called inside E_UPDATE handler, always return false. Handler itself was called properly.
No matter what I press, there is no output into console, except standard startup infos.

My CMakeLists.txt:

    cmake_minimum_required(VERSION 3.0)

    if (COMMAND cmake_policy)
        # Libraries linked via full path no longer produce linker search paths
        cmake_policy (SET CMP0003 NEW)
        # INTERFACE_LINK_LIBRARIES defines the link interface
        cmake_policy (SET CMP0022 NEW)
        # MACOSX_RPATH is enabled by default
        cmake_policy (SET CMP0042 NEW)
        cmake_policy (SET CMP0063 NEW)
    endif ()

    project(Sim3D)

    set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)

    include (UrhoCommon)
    # Define target name
    set (TARGET_NAME Sim3D)
    # Define source files
    define_source_files (main.cpp)
    # Setup target with resource copying
    setup_main_executable ()

-------------------------

Modanung | 2019-08-28 14:00:03 UTC | #2

I think the problem is a missing `URHO3D_OBJECT(Sim3D, Application)` in the class declaration.

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

pirogronian | 2019-08-28 14:38:25 UTC | #3

Thank You for fast reply. Indeed, documentation mentiones it, but sample I used no.
The good news are there is no errors.
The bad nes are there is also no result... :cry:
Could it be related to SDL configuration or something?

Edit: I run Urho3DPlayer. It clearly reacts on keyboard input, so it's not system issue.

-------------------------

Modanung | 2019-08-28 15:16:13 UTC | #4

[quote="pirogronian, post:3, topic:5523"]
but sample I used no.
[/quote]
All samples derive from the `Sample` class:
https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.h#L55

-------------------------

pirogronian | 2019-08-28 15:45:37 UTC | #5

But not sample I used :smile: 
I used [https://github.com/urho3d/Urho3D/wiki/First-Project](https://github.com/urho3d/Urho3D/wiki/First-Project)
and also looked at [https://github.com/damu/Urho-Sample-Platformer/blob/master/main.cpp](https://github.com/damu/Urho-Sample-Platformer/blob/master/main.cpp)

-------------------------

TheComet | 2019-08-28 15:53:27 UTC | #6

[quote="pirogronian, post:1, topic:5523"]
class Sim3D : public Application {
[/quote]

Events can only be received by class instances that inherit from Urho3D::Object and have the URHO3D_OBJECT macro. You need to add this to your sample:

```cpp
class Sim3D : public Application
{
    URHO3D_OBJECT(Sim3D, Application)

    // ...
};```

-------------------------

Modanung | 2019-08-28 16:10:53 UTC | #7

I'm surprised the sample platformer does not contain this.
There is this though:
https://github.com/damu/Urho-Sample-Platformer/blob/master/main.cpp#L140

Could it be related?

-------------------------

pirogronian | 2019-08-29 04:18:56 UTC | #8

I manually changed directory to bin and then called ./Sim3D. But still no result.

Edit I added additional debug checks:
```
auto input = GetSubsystem<Input>();
if (input->HasEventHandlers())
    URHO3D_LOGINFO("Input has handlers.");
else
    URHO3D_LOGINFO("Input has no handlers!");
if (context_ == input->GetContext())
    URHO3D_LOGINFO("Input has the same context.");
else
    URHO3D_LOGINFO("Input has different context!");
VariantMap evdata;
evdata[KeyDown::P_KEY] = KEY_A;
SendEvent(E_KEYDOWN, evdata);
```
But output is as supposed to be:
> [Wed Aug 28 19:55:03 2019] INFO: Input has handlers.
> [Wed Aug 28 19:55:03 2019] INFO: Input has the same context.
> [Wed Aug 28 19:55:03 2019] INFO: A

Edit2:
So far, hacking a bit, I checked that Sim3D is able to receive E_SDLRAWINPUT from  Input object every time key is pressed and released, while E_INPUTBEGIN and E_INPUTEND are sent repeatedly all the time.

-------------------------

Modanung | 2019-08-29 04:21:52 UTC | #9

Did you *try* adding `URHO3D_OBJECT(Sim3D, Application)` to the `Sim3D` class declaration?

-------------------------

pirogronian | 2019-08-30 09:39:19 UTC | #10

> Did you  *try*  adding  `URHO3D_OBJECT(Sim3D, Application)`  to the  `Sim3D`  class declaration?

It was the very first thing I did.

Edit: There are some rumors over the Internet about strange SDL 2.0.5 keyboard handling, what caused problems in Urho3D around 2016. I looked at my Urho3D package release date and it is around 2017, with very first 1.7 version. Maybe It's a already fixed bug. I'll try to build it myself from git master.

-------------------------

Modanung | 2019-08-29 08:24:56 UTC | #11

[quote="pirogronian, post:10, topic:5523"]
I’ll try to build it myself from git master.
[/quote]

Ah yes, this is indeed best (and common) practice. :slightly_smiling_face:

-------------------------

Leith | 2019-08-29 09:30:42 UTC | #12

Oh hi man, did you subscribe to receive the event?
Welcome to the forum!
Don't worry, we can work it out, but you might want to message me privately, and then post your solution back here ;)
SubscribeToEvent(E_KEYDOWN, Urho3D_Handler( classname, methodname ));

-------------------------

Modanung | 2019-08-29 09:36:19 UTC | #13

@Leith The code in the first post contains that line, yes.

-------------------------

Leith | 2019-08-29 09:51:07 UTC | #15

Yeah, something more simple.
Most bugs are simple. This one certainly.
The input system works perfectly.
Thanks, SDL.

-------------------------

pirogronian | 2019-08-30 09:42:37 UTC | #16

Rebuilding whole package from git master fixed the problem.

The only tiny issue I found was need of explicit cast int to Key in GetKeyName(). It should be done more elegant :wink:

-------------------------

Modanung | 2019-08-30 12:35:29 UTC | #17

Could this be your first PR? :wink:

I'm also curious whether `URHO3D_OBJECT(Sim3D, Application)` made any difference in the end.

-------------------------

pirogronian | 2019-08-30 13:50:27 UTC | #18

[quote="Modanung, post:17, topic:5523"]
I’m also curious whether `URHO3D_OBJECT(Sim3D, Application)` made any difference in the end
[/quote]
Yes, it did. My another class, not included in above test code, indeed didnt receive any events without it.

Edit:
[quote="Modanung, post:17, topic:5523"]
Could this be your first PR? :wink:
[/quote]
Maybe, and surely for another topic, because I got very strange behaviour of Variant::Get<>() method...

-------------------------

Leith | 2019-08-31 05:07:21 UTC | #19

Variant is a rubber typed container (basically a Union) - when receiving a variant, always check that the type is not VAR_NONE at minimum, and is your expected type at best.

-------------------------

pirogronian | 2019-08-31 08:28:20 UTC | #20

[quote="Leith, post:19, topic:5523"]
always check that the type is not VAR_NONE at minimum, and is your expected type at best.
[/quote]

Actually my problem was that Get<>() called from non inline function results in undefined reference error. But after some search over the Internet I think it's nit an Urho3D bug but a c++ feature... :slight_smile:

-------------------------

Leith | 2019-08-31 12:50:45 UTC | #21

compilers have their quirks, yep!

-------------------------

