8Observer8 | 2021-02-18 11:30:05 UTC | #1

It is so simple to set up Urho3D-1.7.1 in Qt Creator IDE on Windows 10:

1. Download and install Open Source Qt MinGW: https://www.qt.io/download-open-source
1. Download and unzip " [Urho3D-1.7.1-MinGW-SHARED.zip](https://sourceforge.net/projects/urho3d/files/Urho3D/1.7.1/Urho3D-1.7.1-MinGW-SHARED.zip/download)", for example, to "E:/Libs" folder
1. Run Qt Creator and create a new project: "File" > "New File or Project" > "Other Project" > "Empty qmake Project" > click the "Choose..." button > type a name of project, for example: Urho3D_QtCreator > click "Next" > "Next" > "Finish"
1. Create a "main.cpp" file and copy this code to it:
```c++
#include <Urho3D/Engine/Application.h>
#include <iostream>

class MyApp : public Urho3D::Application
{
public:
    MyApp(Urho3D::Context * context) : Urho3D::Application(context)
    {
    }

    virtual void Setup()
    {
        std::cout << "Setup" << std::endl;
    }
};

URHO3D_DEFINE_APPLICATION_MAIN(MyApp)
```
5. Copy these settings to the .pro file:

Urho3D_QtCreator.pro

```
CONFIG += c++11

INCLUDEPATH += "E:\Libs\Urho3D-1.7.1-MinGW-SHARED\include\Urho3D\ThirdParty"

INCLUDEPATH += "E:\Libs\Urho3D-1.7.1-MinGW-SHARED\include"
LIBS += -L"E:\Libs\Urho3D-1.7.1-MinGW-SHARED\lib\Urho3D"
LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -lSetupapi -ladvapi32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -lopengl32 -liphlpapi

SOURCES += \
    main.cpp
```
6. Run the project by pressing on the green triangle button in left bottom corner (or Ctrl + R). You will see this error:
![image|626x156](upload://57OQnW3a9mmMjqY5oqXtIvbRdIo.png) 
7. ~~To solve this error you need to open the "debug" folder where your .exe is located and add two empty folders: "CoreData" and "Data".~~ To solve this error you need to copy two folders "CoreData" and "Data" from here “E:\Libs\Urho3D-1.7.1-MinGW-SHARED\share\Urho3D\Resources” to the "debug" folder where your .exe is located
8. Run the project again and it works.

-------------------------

8Observer8 | 2021-02-16 14:43:21 UTC | #2

**Note.** The unzipped Urho3D-1.7.1-MinGW-**SHARED** folder requires **only 245 MB** on your hard disk. But Urho3D-1.7.1-MinGW-**STATIC** requires **724 MB**.

Happy learning of Urho3D in Qt Creator! You can use Qt Creator on Window, Linux and macOS.

-------------------------

SirNate0 | 2021-02-16 14:45:22 UTC | #3

Do not use two empty folders to solve the resource path issue. At the very least, copy the CoreData folder from the Urho3D download's bin folder. That contains the shaders and techniques you will almost certainly be using. You probably also want to copy the Data folder, though that has a bunch of stuff you probably won't use that are used in the samples.

-------------------------

8Observer8 | 2021-02-16 15:17:26 UTC | #4

The `CoreData` and `Data` folders are in this folder: `E:\Libs\Urho3D-1.7.1-MinGW-SHARED\share\Urho3D\Resources`

-------------------------

8Observer8 | 2021-02-16 15:59:50 UTC | #5

I published the instruction on the GameDev.net forum in the blog section: https://www.gamedev.net/blogs/entry/2271331-how-to-set-up-urho3d-shared-mingw-in-qt-creator-ide/ I think a lot of people will read it and it will help them to start learning Urho3D and programming in Qt Creator.

-------------------------

8Observer8 | 2021-02-17 09:25:54 UTC | #6

I tried to implement closing a full screen window like in the first code example in the tutorial: https://darkdove.proboards.com/thread/30/urho-flow-1 But I got this error:

![image|255x18](upload://8lOhUuT4VJmHErUEPek46cY2pfI.png) 

To solve this error ~~you need to download [SDL2 for MinGW](https://www.libsdl.org/download-2.0.php), unzip it to some folder and add the "include" folder to the .pro file like this:~~ just add this path to .pro file:

```
INCLUDEPATH += "E:\Libs\Urho3D-1.7.1-MinGW-SHARED\include\Urho3D\ThirdParty"
```

~~INCLUDEPATH += "E:\Libs\SDL2-2.0.12-mingw-32bit\include"~~

~~Click on the error text and rename these lines in "InputEvents.h":~~

```c++
#include <SDL/SDL_joystick.h>
#include <SDL/SDL_gamecontroller.h>
#include <SDL/SDL_keycode.h>
#include <SDL/SDL_mouse.h>
```
~~to these:~~
```c++
#include <SDL2/SDL_joystick.h>
#include <SDL2/SDL_gamecontroller.h>
#include <SDL2/SDL_keycode.h>
#include <SDL2/SDL_mouse.h>
```

Your window will be closed by Escape key:

main.cpp

```c++
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/Input.h>

using namespace Urho3D;

class TutorialApp : public Application
{
    URHO3D_OBJECT(TutorialApp, Application);

public:
    TutorialApp(Context* context)
        : Application(context)
    {
    }

    virtual void Setup()
    {
    }

    virtual void Start()
    {
        SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(TutorialApp, HandleKeyDown));
    }

    virtual void Stop()
    {
    }

    void HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {
        using namespace KeyDown;
        // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
        int key = eventData[P_KEY].GetInt();
        if (key == KEY_ESCAPE)
        {
            engine_->Exit();
        }
    }
};

URHO3D_DEFINE_APPLICATION_MAIN(TutorialApp);
```

-------------------------

SirNate0 | 2021-02-17 02:12:52 UTC | #7

I'm pretty sure Urho includes the SDL stuff. I think you probably just need to add it to the include path (from the include/ThirdParty directory, I'm pretty sure). This sort of thing is why I would recommend using CMake and not trying to roll your own build setup for the downstream project.

-------------------------

8Observer8 | 2021-02-17 09:59:12 UTC | #8

Thanks! SDL is here:

![image|532x238](upload://ufahyHFc73zfRRJUh1qHXR5Y9A7.png) 

I added this path to .pro file:
```
INCLUDEPATH += "E:\Libs\Urho3D-1.7.1-MinGW-SHARED\include\Urho3D\ThirdParty"
```
And it works without renaming SDL to SDL2.

I added this path to the tutorial.

I published the tutorial on Qt forum in GameDev section: https://forum.qt.io/topic/123884/tutorial-how-to-set-up-urho3d-shared-mingw-in-qt-creator-ide

-------------------------

