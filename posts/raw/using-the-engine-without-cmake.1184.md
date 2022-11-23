Kain | 2017-01-02 01:05:56 UTC | #1

Hello!

I'm trying to use Urho3D without CMake (on Windows 7 x64), and here is step-by-step, how I'm doing this:
[ul]
[li] Download "Urho3D-1.4-Windows-SHARED.zip" and unpack it;[/li]
[li] Copy "include/Urho3D" and "lib/Urho3D/libUrho3D.dll.a" to "include" and "lib" of my MinGW installation;[/li]
[li] Copy "bin/Urho3D.dll" to my project folder;[/li]
[li] Create "main.cpp" with the following content:
[code]
#include <Urho3D/Urho3D.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/Math/StringHash.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/UI.h>

using namespace Urho3D;

class Game : public Application
{
    OBJECT(Game);

public:
    Game(Context* Context) : Application(Context)
    {
        
    }

    void Setup()
    {
        engineParameters_["FullScreen"] = false;
    }

    void Start()
    {
        SubscribeToEvent(E_KEYDOWN, HANDLER(Game, OnKeyDown));

        SharedPtr<Text> text(new Text(context_));
        text->SetColor(Color::WHITE);
        text->SetFont(GetSubsystem<ResourceCache>()->GetResource<Font>("Fonts/Cinzel Bold.otf"), 42);
        text->SetHorizontalAlignment(HA_CENTER);
        text->SetText("Okay, it's working now.");
        text->SetVerticalAlignment(VA_CENTER);

        GetSubsystem<UI>()->GetRoot()->AddChild(text);
    }

    void Stop()
    {
        
    }

private:
    void OnKeyDown(StringHash Event, VariantMap &Data)
    {
        engine_->Exit();
    }
};

DEFINE_APPLICATION_MAIN(Game)
[/code][/li]
[li] Build "main.cpp":
[code]
g++ main.cpp -o game.exe -Wpedantic -Wall -Wextra -lmingw32 -lUrho3D -static-libgcc -static-libstdc++
[/code][/li]
[li] Launch output through debugger:
[code]
gdb game.exe
[/code][/li][/ul]

After all this steps, I'm always getting segfault: "0x6bd98200 in Urho3D::StringHash::Calculate(char const*) () from ...".

So, I have two simple questions:
[ul]
[li] Am I doing anything wrong?[/li]
[li] Is this possible to use this engine without CMake?[/li][/ul]

P. S.: sorry for my bad English. :stuck_out_tongue:

-------------------------

cadaver | 2017-01-02 01:05:56 UTC | #2

Welcome.

It should be perfectly possible to use the engine that way, however we're talking about a C++ codebase, so difference in compiler or compiler options can result in there being mismatches in the ABI, which practically means crashes as soon as you start using C++ objects from inside the library.

There is no easy solution to that so I'm starting to doubt if the pre-built binary library downloads should even exist. This would rather force people to build Urho library using the compiler they intend to use. Furthermore, as Urho library can be configured in various ways through the CMake build settings there's no "right" or canonical configuration.

-------------------------

Kain | 2017-01-02 01:05:56 UTC | #3

Thanks for answer!

So, to avoid this segfault, I have to build Urho3D.dll and libUrho3D.dll.a myself, right?

[b]Added:[/b]
And here goes another question: can I build the engine on Windows without DirectX (which, IIRC, is required to build SDL)?

-------------------------

cadaver | 2017-01-02 01:05:57 UTC | #4

Yes, you should at least try it to see if it fares better.

When compiling with MinGW on Windows, there is no way around that you need to have the DirectX headers and libs, even for an OpenGL build. Search for "If using MinGW to compile" from [urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.4/_building.html)

-------------------------

Kain | 2017-01-02 01:05:57 UTC | #5

Thanks a lot! It works perfectly now! ^_^

-------------------------

