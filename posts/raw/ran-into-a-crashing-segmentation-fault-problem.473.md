vivienneanthony | 2017-01-02 01:00:41 UTC | #1

Hello

So, I created a client. It runs but with some new additional code it's noticeably crashing. I am looking through the code but I am having no luck resolving. Do anyone have a idea of whats going on or suggestion?

I placed the main code at [sourceforge.net/projects/proteu ... tenceApps/](https://sourceforge.net/projects/proteusgameengine/files/Existence/Source/ExistenceApps/)

The following functions might be the culprit.
[b]void ExistenceClient::CreatePlayerScreenUI() in ExistenceClient.cpp[/b]
[b]void ExistenceClient::MainScreenUIHandleClosePressed(StringHash eventType, VariantMap& eventData)[/b] in ExistenceClient.cpp
[b]int ExistenceClient::loadplayerMesh(Node * playermeshNode, int alienrace, int gender, int mode)[/b] in ExistenceClient.cpp
[b]void ExistenceClient::HandleMouseReleased(StringHash eventType, VariantMap& eventData) [/b]in ExistenceClient.cpp

[video]https://www.youtube.com/watch?v=4Iew3dWrlX0[/video]

Vivienne



[code](gdb) run
Starting program: /media/home2/vivienne/Existence/Bin/ExistenceClient 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[Tue Oct  7 23:15:41 2014] INFO: Opened log file /home/vivienne/.local/share/urho3d/logs/ExistenceClient.log
[New Thread 0x7ffff3069700 (LWP 23680)]
[New Thread 0x7ffff2868700 (LWP 23681)]
[New Thread 0x7ffff2067700 (LWP 23682)]
[Tue Oct  7 23:15:41 2014] INFO: Created 3 worker threads
[Tue Oct  7 23:15:41 2014] INFO: Added resource path /media/home2/vivienne/Existence/Bin/CoreData/
[Tue Oct  7 23:15:41 2014] INFO: Added resource path /media/home2/vivienne/Existence/Bin/Data/
[Tue Oct  7 23:15:41 2014] INFO: Set screen mode 1440x900 fullscreen
[Tue Oct  7 23:15:41 2014] INFO: Initialized input
[Tue Oct  7 23:15:41 2014] INFO: Initialized user interface
[Tue Oct  7 23:15:41 2014] INFO: Initialized renderer
[New Thread 0x7fffead2d700 (LWP 23683)]
[New Thread 0x7fffea52c700 (LWP 23684)]
[Tue Oct  7 23:15:41 2014] INFO: Set audio mode 44100 Hz stereo interpolated
[Tue Oct  7 23:15:42 2014] INFO: Added resource path /media/home2/vivienne/Existence/Bin/Resources/
[Tue Oct  7 23:15:44 2014] INFO: Loading scene from /media/home2/vivienne/Existence/Bin/Resources/Scenes/charactercreationroom1.xml
[Tue Oct  7 23:15:44 2014] WARNING: Forcing top alignment because parent element has vertical layout
[Tue Oct  7 23:15:49 2014] INFO: Loading scene from /media/home2/vivienne/Existence/Bin/Resources/Scenes/charactercreationroom1.xml
[Tue Oct  7 23:15:49 2014] WARNING: Forcing top alignment because parent element has vertical layout
[Tue Oct  7 23:15:52 2014] INFO: Loading scene from /media/home2/vivienne/Existence/Bin/Resources/Scenes/charactercreationroom1.xml
[Tue Oct  7 23:15:53 2014] WARNING: Forcing top alignment because parent element has vertical layout
[Tue Oct  7 23:15:56 2014] INFO: Loading scene from /media/home2/vivienne/Existence/Bin/Resources/Scenes/charactercreationroom1.xml
[Tue Oct  7 23:15:56 2014] WARNING: Forcing top alignment because parent element has vertical layout
[Tue Oct  7 23:16:01 2014] INFO: Loading scene from /media/home2/vivienne/Existence/Bin/Resources/Scenes/charactercreationroom1.xml
[Tue Oct  7 23:16:01 2014] WARNING: Forcing top alignment because parent element has vertical layout
[Tue Oct  7 23:16:05 2014] INFO: Loading scene from /media/home2/vivienne/Existence/Bin/Resources/Scenes/charactercreationroom1.xml
[Tue Oct  7 23:16:05 2014] WARNING: Forcing top alignment because parent element has vertical layout
[Tue Oct  7 23:16:10 2014] INFO: Loading scene from /media/home2/vivienne/Existence/Bin/Resources/Scenes/charactercreationroom1.xml
[Tue Oct  7 23:16:10 2014] WARNING: Forcing top alignment because parent element has vertical layout

Program received signal SIGSEGV, Segmentation fault.
0x000000000059ccf0 in ExistenceClient::MainScreenUIHandleClosePressed(Urho3D::StringHash, Urho3D::HashMap<Urho3D::ShortStringHash, Urho3D::Variant>&) ()
(gdb) quit
A debugging session is active.

        Inferior 1 [process 23676] will be killed.

Quit anyway? (y or n) y
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:42 UTC | #2

One error I found so far.

GDB
[code]#0  0x00007ffff69f54e7 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00000000006d7c5f in Urho3D::String::operator== (this=0x9bf05f0, rhs=0xc60198 "exitButton")
    at /media/home2/vivienne/Existence/Source/Engine/Container/Str.h:261
[/code]

My Code

[code]/// Main screen user interface handle close pressed
void ExistenceClient::MainScreenUIHandleClosePressed(StringHash eventType, VariantMap& eventData)
{
    /// Set ui state to UI_CHARACTERSELECTIONINTERFACE
    ExistenceGameState.SetUIState(UI_CHARACTERSELECTIONINTERFACE);

    /// Get control that was clicked
    UIElement* clicked = static_cast<UIElement*>(eventData[UIMouseClick::P_ELEMENT].GetPtr());

    /// Check for a click and which button
    if(clicked)
    {

        if(clicked->GetName()=="newcharacterButton")
        {
            /// remove child nodeAddItem (UIElement *item)
            scene_->GetChild("playerMesh",true)->Remove();

            /// Clear screen
            eraseScene();

            /// Create a player UI
            CreatePlayerScreenUI();

            Console* console = GetSubsystem<Console>();

            console -> SetVisible(false);

            ExistenceGameState.SetConsoleState(UI_CONSOLEOFF);

            /// Enable OS cursor
            GetSubsystem<Input>()->SetMouseVisible(true);
        }

        if(clicked->GetName()=="exitButton")
        {
            engine_->Exit();
        }
    }


    return;
}
[/code]

-------------------------

thebluefish | 2017-01-02 01:00:43 UTC | #3

What IDE are you using? Have you tried to debug the code as it crashes?

-------------------------

vivienneanthony | 2017-01-02 01:00:43 UTC | #4

[quote="thebluefish"]What IDE are you using? Have you tried to debug the code as it crashes?[/quote]

I use Codeblocks with GDB debugging runtime. Also, console GDB runtime debugging.

Before, I wasn't using it. Now I do.  I posted a video of it. The content is lacking detail and lighting but the code is working for what I added.

-------------------------

gwald | 2017-01-02 01:00:46 UTC | #5

Hi,
If you want people to read text on youtube you need to drop your screen resolution or make the font bigger.
Good progress on your game too!

-------------------------

