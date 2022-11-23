claudeHasler | 2020-03-15 13:43:04 UTC | #1

Ive downloaded the Prebuilt binaries (Urho3D-1.7.1-MinGW-64bit-SHARED) and am trying to include then into a simple example project but I'm getting tons of compiler errors:

What ive done:

add env variable URHO3D_DIR :
 "C:\Dev\CppLibs\urho3d\urho3d_1.7.1_64"

add Additional include directories: 
$(URHO3D_DIR)\include

add Additional library directories:
$(URHO3D_DIR)\bin

now id like to link to the dll, but i dont have a .lib file. 

Do i have to build urho from scratch to get this .lib file?

-------------------------

claudeHasler | 2020-03-15 14:11:54 UTC | #2

Update: Ive now built the project from source, and now have a the .lib. 

Now im getting errors pertaining to SDL:

Severity	Code	Description	Project	File	Line	Suppression State
Error	C1083	Cannot open include file: 'SDL/SDL_joystick.h': No such file or directory	Examples_Urho_Minimal	C:\Dev\CppLibs\urho3d\Urho3d-1.7\include\Urho3D\Input\InputEvents.h	27

-------------------------

Miegamicis | 2020-03-15 14:43:17 UTC | #3

You should try building straight from master. 1.7 is very old release and a lot of things have been added and fixed since then.

-------------------------

claudeHasler | 2020-03-15 15:00:02 UTC | #4

I can now compile against Urho3d library. The solution was to add additional include directories:
$(URHO3D_DIR)\include\Urho3D\ThirdParty\Lua
$(URHO3D_DIR)\include\Urho3D\ThirdParty\Bullet
$(URHO3D_DIR)\include\Urho3D\ThirdParty\
$(URHO3D_DIR)\include

Now im trying to start the engine manually in my main:

[Code]

void main() {

	Context* context = new Context();
	Engine engine(context);
	VariantMap variantMap;

	engine.Initialize(variantMap);

	//MyApp myApp(context);

	while (true) {
		engine.RunFrame();
	}
	
	
}
[/Code]

This compiles just fine, but crashed immediately with:
 ERROR: Failed to add resource path 'Data', check the documentation on how to set the 'resource prefix path'


Is there an example of how to manually start the engine, and set the necessary parameters anywhere? All examples i can find use the

URHO3D_DEFINE_APPLICATION_MAIN(MyApp)

directive to start.

-------------------------

claudeHasler | 2020-03-15 15:07:37 UTC | #5

[Code]
void main() {

	Context* context = new Context();

	MyApp myApp(context); //Inherits Application
	 
	myApp.Run();

	while (true) {
		Sleep(1000);
	}
	
}
[/Code]


This code, along with adding a Data and CoreData Folder in the executable directory worked.

-------------------------

Modanung | 2020-03-15 16:48:07 UTC | #6

If you don't want to use the Data and CoreData folders it's better not to use them.
```
engineParameters_[EP_RESOURCE_PATHS] = "";
```

-------------------------

