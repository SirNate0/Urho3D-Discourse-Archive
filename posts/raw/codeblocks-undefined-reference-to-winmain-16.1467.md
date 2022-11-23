itisscan | 2017-01-02 01:07:54 UTC | #1

I have builded Urho3D library through CMake and get Urho3D.a file. Then I create my own Codeblocks GUI project and link Urho3D.a file. After this I add Urho3D includes, MyProgramApp.cpp and MyProgramApp.hpp file. In the file MyProgramApp.hpp I write MyProgram class, that is inherited from Urho3D::Application and write DEFINE_APPLICATION_MAIN(HangarsClientApp) after it, like this :

[code]class MyProgramApp : public Application
{
	OBJECT(MyProgramApp)
public:
	// Constructors
	MyProgramApp(Context* context);
	virtual ~MyProgramApp();

public:
	// Application class overrided functions
	virtual void Setup();
	virtual void Start();						// Called after engine initialization. Setup application & subscribe to events here
	virtual void Stop();						// Perform optional cleanup after main loop has terminated
};

DEFINE_APPLICATION_MAIN(MyProgramApp)[/code]

In the result, I get undefined reference to `WinMain@16'|

Platform : Win32. Compiler: gcc 5.2.0 (i686-posix-dwarf-rev0, Built by MinGW-W64 project)

How I can fix it ?

-------------------------

jmiller | 2017-01-02 01:07:55 UTC | #2

Hi [b]itisscan[/b],

You will probably want to use a "Custom Makefile" project, not a GUI project.
You can generate your project's build tree(s) using the same cmake_* scripts used to build Urho.

To do this, you will need some things in your source tree (like CMakeLists.txt and CMake/* scripts):
[urho3d.github.io/documentation/1 ... brary.html](http://urho3d.github.io/documentation/1.4/_using_library.html)

Each of the generated build trees (debug/release/whatever) will have their own makefile. Specify these in your IDE's project configurations and they should build.

Hope that helps.

-------------------------

Bluemoon | 2017-01-02 01:07:55 UTC | #3

The project is most likely set as console application on CodeBlocks. Try the following:
[ul]- Go to the Project Menu and Select "Build options..."[/ul]
[ul]- Below the "Selected Compiler" drop-down you will see sets of tabs. Select the Compiler Setting tab[/ul]
[ul]- Under the tabs below it select "#defines" [/ul]
[ul]- Add the WIN32 AND _WINDOWS one per line[/ul]

[img]http://i.imgur.com/tK3vbGw.png[/img]

-------------------------

jmiller | 2017-01-02 01:07:55 UTC | #4

It's certainly possible to use cmake generators other than the 'makefile' I described.
I just noticed cmake_codeblock.bat, which should generate a CodeBlocks project for you, which you might find preferable.

On MSWin platform, DEFINE_APPLICATION_MAIN() uses WinMain entry point by default (a "GUI" app). This behavior can be changed with the cmake option URHO3D_WIN32_CONSOLE:
[urho3d.github.io/documentation/H ... lding.html](http://urho3d.github.io/documentation/HEAD/_building.html)

-------------------------

