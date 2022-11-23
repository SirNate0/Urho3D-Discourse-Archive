Aramis | 2017-01-02 01:03:39 UTC | #1

Hello,

I'm having a difficult time trying to figure out how to make a simple program with Urho using the old "main() entry point".
I have already compiled it from source, used it to make a new project through CMake too. (As explained int the urho3d.github.io/documentation/1.32/_using_library.html)

Now I just want to "recreate" the HelloWorld example but Instead of using the WinConsole, and the Application class thing, use "simple" and clean main() entry point and control the main loop 

iteration manually.

I have tryed to figure out through the Classes diagram and the documentation how to create it myself, but I really don't ubderstand how it would work. I also tried to find a example on Google 

and on this forum's search engine, but all I get is something about the Main.h (Part of the engine), Classes named Main and the whole DEFINE_APPLICATION_MAIN thing...

I admit I'm not familiar with the level of Urho's C++ and the only expiriend I have with using game/graphic engines was with Irrlicht..

I'm using Visual Studio 2012, and I'm aware that I need to change the project Linker/System/SubSystem from [b]Windows [/b]to [b]Console [/b]in order to work with the main entry point. What I 

dont know is how to code a this simple example.

Sorry for my silliness, but this WinConsole thing is new to me... I'm used to program with "main(){}". Is it too bad to use the old main() style instead of the WinMain and the Urho's classes 

that control this?


What I want to do is something like:
[code]#include <irrlicht.h>

using namespace irr;

int main()
{
	
	IrrlichtDevice *device = createDevice( video::EDT_SOFTWARE, dimension2d<u32>(640, 480), 16, false, false, false, 0);

	guienv->addStaticText(L"Hello World!", rect<s32>(10,10,260,22), true);

	while(device->run())
	{
		driver->beginScene(true, true, SColor(255,100,101,140));

		smgr->drawAll();
		guienv->drawAll();

		driver->endScene();
	}

	device->drop();

	return 0;
}[/code]

Kind regards,

Aramis

-------------------------

OvermindDL1 | 2019-07-20 13:46:11 UTC | #2

The default way would be to subclass Urho3D::Application and instance it with DEFINE_APPLICATION_MAIN(MyApplicationClassName), but if you really want to do it manually then just set up a main as normal:
[code]
int main(int argc, char** argv)
{
    Urho3D::ParseArguments(argc, argv);  // Parse arguments so they are usable.
    Urho3D::Context* context = new Urho3D::Context(); // Always need a default context
    MyApplicationClassName* application = new MyApplicationClassName(context); // Create you Application subclass, this is of course optional
    return application->Run(); // Run your application class
}
[/code]

And of course if you do not want to subclass Urho3D::Application then feel free to look in Application.cpp to see what it does.

DO NOTE:  By not using the proper macros then your system will only work properly locally, do not expect to be able to compile it for other systems, especially mobile.  You really should use the macros.

-------------------------

Aramis | 2019-07-20 13:46:10 UTC | #3

That did it perfectly.

Thank you.

-------------------------

