lukadriel | 2017-01-02 01:12:02 UTC | #1

Hello everyone, I am new here and I just built Urho3d from source and I am trying to run it but I end up getting an error at the line of "URHO3D_DEFINE_APPLICATION_MAIN(MyApp)"
here is the code :

[code]#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/InputEvents.h>
using namespace Urho3D;
class MyApp : public Application
{
public:
	MyApp(Context* context) :
		Application(context)
	{
	}
	virtual void Setup()
	{
		// Called before engine initialization. engineParameters_ member variable can be modified here
	}
	virtual void Start()
	{
		// Called after engine initialization. Setup application & subscribe to events here
		SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(MyApp, HandleKeyDown));
	}
	virtual void Stop()
	{
		// Perform optional cleanup after main loop has terminated
	}
	void HandleKeyDown(StringHash eventType, VariantMap& eventData)
	{
		using namespace KeyDown;
		// Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
		int key = eventData[P_KEY].GetInt();
		if (key == KEY_ESC)
			engine_->Exit();
	}
}
URHO3D_DEFINE_APPLICATION_MAIN(MyApp)[/code]

I just want to make sure I built it correctly. Here is a screenshot. Thank you in advance
[img]http://i.imgur.com/uGIgxc4.png?1[/img]

-------------------------

1vanK | 2017-01-02 01:12:02 UTC | #2

class
{
..
}; <-----------

-------------------------

lukadriel | 2017-01-02 01:12:02 UTC | #3

Hello Ivank, thank you for replying. I had forget to put it back. Actually it does get rid of the two errors about myApp and return but I still have 6 errors. When I comment out the 
URHO3D_DEFINE_APPLICATION_MAIN(MyApp) and create a main function it works with no problems. I suppose the problem is with the macro

-------------------------

JTippetts | 2017-01-02 01:12:02 UTC | #4

Be sure to #include <Urho3D/Urho3D.h>

Strike that. Add a semicolon after URHO3D_DEFINE_APPLICATION_MAIN(Urho3DPlayer)

-------------------------

lukadriel | 2017-01-02 01:12:03 UTC | #5

Hi, I tried to do all of that but it doesn't change anything

-------------------------

rku | 2017-01-02 01:12:03 UTC | #6

HINSTANCE is windows thing so include Windows.h. Then you are missing URHO3D_OBJECT(MyApp, Application) (very fist thing in class body).

-------------------------

lukadriel | 2017-01-02 01:12:03 UTC | #7

Thank you, i added the Windows.h and the URHO3D_OBJECT but I Still have some errors.
[img]http://i.imgur.com/kKIURob.png[/img]
If somebody could give me a tested and working minimal code just to open a window I would be so greatful

-------------------------

rku | 2017-01-02 01:12:03 UTC | #8

From names of symbols it seems that is windows stuff. Not sure what that is, i did not have any experience with new windows SDKs. If you want solid example then use [url=https://github.com/urho3d/Urho3D/tree/master/Source/Samples]samples[/url]. All you need to do is grab Sample.h, Sample.inl and files from one sample folder and put in your project. That should work. Did same thing myself, had no problems there.

-------------------------

1vanK | 2017-01-02 01:12:04 UTC | #9

Your code works fine for my. Maybe you incorrectly created the project

-------------------------

lukadriel | 2017-01-02 01:12:04 UTC | #10

hey, I think the problem was me using the debug  configuration. it works in release. Is there a particular reason for that ?

-------------------------

1vanK | 2017-01-02 01:12:04 UTC | #11

if you build debug version of engine after creating of game project, you need recreate game project (delete cache and cmake again)

-------------------------

