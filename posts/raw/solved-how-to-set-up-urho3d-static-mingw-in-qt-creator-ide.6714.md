8Observer8 | 2021-02-18 14:02:57 UTC | #1

Hi, all

I try to set up Urho3D (Static, MinGW) in Qt Creator IDE. I use Qt 5.15.2 MinGW. I tried to set up:

-  [Urho3D-1.7-MinGW-STATIC.zip](https://sourceforge.net/projects/urho3d/files/Urho3D/1.7/Urho3D-1.7-MinGW-STATIC.zip/download)
- [Urho3D-1.8.ALPHA-MinGW-STATIC.tar.gz](https://sourceforge.net/projects/urho3d/files/Urho3D/1.8-ALPHA/Urho3D-1.8.ALPHA-MinGW-STATIC.tar.gz/download)

But every time I get these errors (848 issues for Urho3D-1.8 and 780 issues for Urho3D-1.7):

For Urho-1.7:
![image|504x263](upload://zOUE5o6gDVXBGqsEjqbNey3ruLX.png) 

For Urho-1.8:
![image|503x259](upload://jFgACBgmrGVyPA36jIpehFz8bCr.png) 

As you can see the first errors are the same for Urho-1.7 and Urho-1.8.

I thought may be it is because Qt 5.15 uses "mingw81_32" that is not compatible with Urho MinGW.

I try to write an instruction for beginners. These are my step:

**How to set up Urho3D (Static, MinGW) in Qt Creator IDE**

It is so simple to setup Urho in Qt Creator IDE on Windows 10:

1. Download and install Open Source Qt MinGW: https://www.qt.io/download-open-source
1. Download and unzip " [Urho3D-1.7-MinGW-STATIC.zip](https://sourceforge.net/projects/urho3d/files/Urho3D/1.7/Urho3D-1.7-MinGW-STATIC.zip/download)", for example, to "E:/Libs" folder
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

INCLUDEPATH += "E:\Libs\Urho3D-1.7-MinGW-STATIC\include"
LIBS += -L"E:\Libs\Urho3D-1.7-MinGW-STATIC\lib\Urho3D"
LIBS += -lUrho3D -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -lSetupapi -ladvapi32 -lwinmm -limm32 -lversion -lws2_32 -ldbghelp -lopengl32

SOURCES += \
    main.cpp
```
6. Run the project by pressing on the green triangle button in left bottom corner (or Ctrl + R). You will see an empty window created by Urho3D.

-------------------------

8Observer8 | 2021-02-16 14:18:34 UTC | #2

I download [Urho3D-1.7.1-MinGW-SHARED.zip](https://sourceforge.net/projects/urho3d/files/Urho3D/1.7.1/Urho3D-1.7.1-MinGW-SHARED.zip/download) It works with my instruction above. In addition to my instruction you need to create two folders: "CoreData" and "Data" in your "debug" folder (where .exe is located) because of this error:
![image|626x156](upload://57OQnW3a9mmMjqY5oqXtIvbRdIo.png)

-------------------------

8Observer8 | 2021-02-16 14:17:53 UTC | #3

But I think my information will be useful for developers of Urho3D.

-------------------------

S.L.C | 2021-02-16 15:09:26 UTC | #4

[quote="8Observer8, post:2, topic:6714"]
You need to create two folders: “CoreData” and “Data” in your “debug” folder
[/quote]

**I don't think you only need to create those. But rather you need to copy the core engine assets.** Like shaders and stuff. Because you'll end up having the same error message but for those files.

As for static linking. There's a variety of MinGW distributions out there. I honestly suggest [msys2](https://www.msys2.org/). The usual MinGW-w64 from SF died around 8.x version years ago. If you look closely the last release was in 2018-05-24.

And because the MinGW that was used to build the engine might not be the same as yours I'm not entirely sure it will successfully link against each other. Depending on how MinGW libs themselves were linked to the engine.

At this point I suggest building the engine yourself. Every dependency is bundled in and you don't need anything extra installed other than the compiler. It's just a mater of installing CMake, pointing it to the source folder and hitting configure/generate. It's just that easy.

-------------------------

8Observer8 | 2021-02-16 15:12:33 UTC | #5

[[Tutorial] How to set up Urho3D (Shared, MinGW) in Qt Creator IDE](https://discourse.urho3d.io/t/tutorial-how-to-set-up-urho3d-shared-mingw-in-qt-creator-ide/6715)

-------------------------

8Observer8 | 2021-02-17 12:35:11 UTC | #6

I built Urho3D from source using CMake-GUI to a static version. But I have the same errors like above but now it is only 132 issues:

![image|567x310](upload://vo7E38V3ANqW3pHz1q7Sl9H6X8P.png)

-------------------------

8Observer8 | 2021-02-17 13:46:39 UTC | #7

`MINGW_SYSROOT` has a value: `C:/Qt/Tools/mingw810_32/i686-w64-mingw32` because I use Qt. A static version does not work for me even I build from source.

If STATIC does not want to work for me then I will try to build to SHARED: https://discourse.urho3d.io/t/problems-with-building-urho3d-to-shared-version-from-source/6718

-------------------------

S.L.C | 2021-02-17 14:09:55 UTC | #8

Don't you need `URHO3D_STATIC_DEFINE` somewhere?

-------------------------

8Observer8 | 2021-02-18 11:05:22 UTC | #9

To build the STATIC version of Urho3D for Qt Creator MinGW 8.1.0 you need to use the `master` branch of Urho3D. The `-liphlpapi` key is required to avoid this error: ![image|296x17](upload://ipeiaC6K7ABzlLQ4TFXk72jaS27.png)

-------------------------

