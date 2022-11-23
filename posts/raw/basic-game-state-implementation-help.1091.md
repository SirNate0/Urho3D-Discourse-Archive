vivienneanthony | 2017-01-02 01:05:23 UTC | #1

Hello,

I have  been trying to get a state manner working for Existence.  I spent 24 hours+ working on it and I got it to the point of the black screen of death. 

When running the executable it crashes when calling a function in the GameStateHandler which is making no sense to me because the code is almost a copy of another code which works..

The obvious problems I see is that and trying to change the state because createState inputs a string and it converts it to a state using a dynamic cast creating a component. (Which I will not do)

The code is based on [topic43.html#p195](http://discourse.urho3d.io/t/managing-game-state/66/1)

My work around to move away from the node state is a API level logiccomponennt.

The GitHUB is [github.com/vivienneanthony/Urho ... -Existence](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence)

The related files are the files starting with Game at [github.com/vivienneanthony/Urho ... enceClient](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/tree/development/Source/ExistenceApps/ExistenceClient).

Also I have to expand the event signal to send more argument info and somehow force Enter() and Exit() on    each state change possibly a HandleUpdate() and FixedUpdate();

Photos of problem areas

[imgur.com/h3bOglh,Ag4sVr2](http://imgur.com/h3bOglh,Ag4sVr2)

-------------------------

vivienneanthony | 2017-01-02 01:05:24 UTC | #2

All related files.  There are errors of course been cranking the conversion full speed. Coffee.

[github.com/vivienneanthony/Urho ... ponent.cpp](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/blob/development/Source/ExistenceApps/ExistenceClient/GameStateComponent.cpp)
[github.com/vivienneanthony/Urho ... omponent.h](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/blob/development/Source/ExistenceApps/ExistenceClient/GameStateComponent.h)
[github.com/vivienneanthony/Urho ... andler.cpp](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/blob/development/Source/ExistenceApps/ExistenceClient/GameStateHandler.cpp)
[github.com/vivienneanthony/Urho ... eHandler.h](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/blob/development/Source/ExistenceApps/ExistenceClient/GameStateHandler.h)
[github.com/vivienneanthony/Urho ... teEvents.h](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/blob/development/Source/ExistenceApps/ExistenceClient/GameStateEvents.h)

[github.com/vivienneanthony/Urho ... Client.cpp](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/blob/development/Source/ExistenceApps/ExistenceClient/ExistenceClient.cpp)
[github.com/vivienneanthony/Urho ... ceClient.h](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/blob/development/Source/ExistenceApps/ExistenceClient/ExistenceClient.h)

Additoinally, I just tried adhocing it.

Creating a pointer in the Game State Handler code header to a point. Then setting the pointer from the main code to set the Game State Hanger coded pointer.

Basically, pointing the code to the memory address of itself. That idea did not work.

Argh!!!!

Updated on github.

-------------------------

vivienneanthony | 2017-01-02 01:05:24 UTC | #3

Just a FYI.

The SetConsoleState in the GameStateHandler class works before I switch a state after deffining it.

I am thinking once the new state is loaded. ExistenceGameState loses it context or the State does not have access to the data. I tried movign the shared  pointer all the way to the base class but it still not working.

-------------------------

vivienneanthony | 2017-01-02 01:05:24 UTC | #4

Here are some changes with the code and results.

1.Befriended derived class. Okay. No major results.
2.Use the scene node setup similiar to the original source from Carlomaker..  
 
Result 
State changes seems to happen but crashes.

3. The Login code is started and when finished. It goes back to the Game State Handler calling a Unknown state.

4. The ExistenceGameState  functions can be called, but if it tries to change information like Console. It crashes also.

Result
Derived classes do not get full access to the class functon ExistenceGameState creating a crash. The following code is a example.

[code]
nt GameStateHandler::SetUIState(int flag)
{

    uistate = flag;

    return 1;
}[/code]

Conclusion

Other problem
I don't see the login window appear or Existence logo.  I'm not certain if I have to create a loop in that specific subclass.

-------------------------

vivienneanthony | 2017-01-02 01:05:24 UTC | #5

Resources

CoreData and Resources Folder

It includes scenes, models, textures, UI needed, and everything else other then the build files on GitHub.

[dropbox.com/s/whwwioz5ahjpu ... s.zip?dl=0](https://www.dropbox.com/s/whwwioz5ahjpucx/ExistenceResources.zip?dl=0)

The primary Idea is a derived class from ExistenceClient class part of the App that is for each class ExistenceClientStateXXXX.cpp then other function in relation to a specific takes like ExistenceClientConsole.cpp or ExistenceClientFile.cpp for general used functions among the derived class.

As for as input, I am thinking one HandleUpdate and HandleInput for everything but it can detect states and do the appriopriate action.

At least for the time being.

-------------------------

vivienneanthony | 2017-01-02 01:05:25 UTC | #6

If any code is not clear of purpose. FYI me. I need a getCurrentState function each make a continous loop in each state if a overall exit out on state change or possible timeout in game mode if no input maybe after a day

-------------------------

vivienneanthony | 2017-01-02 01:05:26 UTC | #7

So, I got the code to switch code based on a state using a signal event or command. The problem I have the graphics and UI go awry when I change to a derived class. I eventually have to take out the words friendly class in the client header but any insight would be help. I added some dummy functions when a Client/Server framework can be done it would be easier.

Really. I got this thing 80% running but stuck at that last 20%.


Header
[code]#ifndef GAMESTATEHANDLER_H
#define GAMESTATEHANDLER_H


#define         UI_NONE                             0
#define         UI_LOGININTERFACE                   1
#define         UI_ACCOUNTCREATIONINTERFACE         2
#define         UI_CHARACTERCREATIONINTERFACE       3
#define         UI_CHARACTERSELECTIONINTERFACE      4
#define         UI_PROGRESSINTERFACE                5
#define         UI_GAMECONSOLE                      6

#define         STATE_NONE                          10
#define         STATE_MAIN                          11
#define         STATE_GAME                          12

#define         UI_CONSOLEOFF                     0
#define         UI_CONSOLEON                      1

#define         CAMERAMODE_DEFAULT                  0
#define         CAMERAMODE_FIRSTPERSON              1
#define         CAMERAMODE_FLY                      2

#include "GameStateComponent.h"


using namespace Urho3D;

/// fw declaration
class ExistenceClient;
class ExistenceClientStateSingleton;

class GameStateHandler : public Urho3D::Object
{
    OBJECT(GameStateHandler);
public:
    ///costructor
    GameStateHandler(Context * context);
    /// Destruct.
    virtual  ~GameStateHandler();
    /// start point
    void Start(void);
    // handler events
    void onStateChange(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData );
    /// Get last state
    String getCurrentState(void);
    // Register object factory and attributes.
    static void RegisterObject(Context* context);

    /// Function to access other states
    int GetConsoleState(void);
    int SetConsoleState(int flag);

    int GetUIState(void);
    int SetUIState(int flag);

    int GetCameraMode(void);
    int SetCameraMode(int flag);

    int GetDebugHudMode(void);
    int SetDebugHudMode(int flag);

private:

    /// register all states
    void RegisterGameStates();
    /// create  state  classname
    void createState( Urho3D::String newState );
    /// change state
    void changeState(GameStateComponent * state);
    void changeState2(ExistenceClientStateSingleton * State);
    /// exit and remove last state.
    void RemoveLastState();

    /// Not used at the moment
    /// holder
    ExistenceClientStateSingleton * GameState;

    /// Not used at the moment
    /// states container
    Urho3D::Vector<GameStateComponent*> mStates;

    /// Not used at the moment
    /// Kept node just in case
    Urho3D::SharedPtr<Urho3D::Node> mainNode;

    /// Vector Array - Derived States
    std::vector<ExistenceClient *> myDerivedSates;

/// Added flags
    int consolestate;
    int uistate;
    int cameramode;
    int debughud;


};

#endif // GAMESTATEHANDLER_H
[/code]
[code]//
// Copyright (c) 2008-2014 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#include <Urho3D/Urho3D.h>

#include "../../../Urho3D/Core/CoreEvents.h"
#include "../../../Urho3D/Engine/Engine.h"
#include "../../../Urho3D/UI/Font.h"
#include "../../../Urho3D/Input/Input.h"
#include "../../../Urho3D/Core/ProcessUtils.h"
#include "../../../Urho3D/UI/Text.h"
#include "../../../Urho3D/UI/UI.h"
#include "../../../Urho3D/Scene/Scene.h"
#include "../../../Urho3D/Graphics/StaticModel.h"
#include "../../../Urho3D/Graphics/Octree.h"
#include "../../../Urho3D/Graphics/Model.h"
#include "../../../Urho3D/Graphics/Material.h"
#include "../../../Urho3D/Graphics/Camera.h"
#include "../../../Urho3D/Resource/ResourceCache.h"
#include "../../../Urho3D/Graphics/Renderer.h"
#include "../../../Urho3D/Graphics/Camera.h"
#include "../../../Urho3D/UI/Window.h"
#include "../../../Urho3D/UI/Button.h"
#include "../../../Urho3D/UI/LineEdit.h"
#include "../../../Urho3D/UI/UIElement.h"
#include "../../../Urho3D/Math/BoundingBox.h"
#include "../../../Urho3D/UI/UIEvents.h"
#include "../../../Urho3D/Graphics/DebugRenderer.h"
#include "../../../Urho3D/IO/File.h"
#include "../../../Urho3D/IO/FileSystem.h"
#include "../../../Urho3D/Resource/XMLFile.h"
#include "../../../Urho3D/Resource/XMLElement.h"
#include "../../../Urho3D/IO/Deserializer.h"
#include "../../../Urho3D/UI/Cursor.h"
#include "../../../Urho3D/IO/FileSystem.h"
#include "../../../Urho3D/UI/ListView.h"
#include "../../../Urho3D/Engine/Console.h"
#include "../../../Urho3D/Physics/RigidBody.h"
#include "../../../Urho3D/Physics/CollisionShape.h"
#include "../../../Urho3D/Physics/PhysicsWorld.h"
#include "../../../Urho3D/Graphics/Animation.h"
#include "../../../Urho3D/Graphics/AnimatedModel.h"
#include "../../../Urho3D/Graphics/AnimationController.h"
#include "Character.h"
#include "../../../Urho3D/Graphics/Terrain.h"
#include "../../../Urho3D/Engine/EngineEvents.h"
#include "../../../Urho3D/Graphics/Zone.h"
#include "../../../Urho3D/IO/Log.h"
#include "../../../Urho3D/Graphics/Skybox.h"
#include "../../../Urho3D/UI/Sprite.h"
#include "../../../Urho3D/Graphics/StaticModelGroup.h"
#include "../../../Urho3D/Graphics/BillboardSet.h"
#include "../../../Urho3D/Math/Random.h"
#include "../../../Urho3D/Graphics/RenderPath.h"
#include "../../../Urho3D/Math/Color.h"

#include "GameStateHandler.h"
#include "GameStateEvents.h"
#include "GameStateComponent.h"
#include "GameObject.h"
#include "EnvironmentBuild.h"
#include "Manager.h"
#include "../Account.h"

#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <locale>
#include <ctime>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <iostream>
#include <utility>
#include <algorithm>

#include "../../../Urho3D/Procedural/Procedural.h"
#include "../../../Urho3D/Procedural/ProceduralTerrain.h"
#include "../../../Urho3D/Procedural/RandomNumberGenerator.h"

#include "ExistenceClient.h"


///using namespace std;
using namespace Urho3D;

GameStateHandler::GameStateHandler(Context * context):
    Object(context)
    ,consolestate(0)
    ,uistate(0)
    ,debughud(0)
    ,cameramode(0)
{

    /// Set defaults
    uistate=UI_NONE;
    consolestate=UI_CONSOLEOFF;
    cameramode=CAMERAMODE_DEFAULT;
    debughud=false;

    /// Subscribe to event state change
    SubscribeToEvent(G_STATES_CHANGE, HANDLER(GameStateHandler, onStateChange));

    /// Register states
    RegisterGameStates();
}

GameStateHandler::~GameStateHandler()
{
    /// Remove last state
    RemoveLastState();

    /// Destroy component
    LOGINFO("Destroyng GameComponent" );
}


void GameStateHandler::RegisterGameStates()
{
    /// .... all states here
    context_->RegisterFactory<ExistenceClientStateSingleton>();
    context_->RegisterFactory<ExistenceClientStateAccount>();
    context_->RegisterFactory<ExistenceClientStateGameMode>();
    context_->RegisterFactory<ExistenceClientStateLogin>();
    context_->RegisterFactory<ExistenceClientStatePlayer>();
    context_->RegisterFactory<ExistenceClientStateProgress>();
    context_->RegisterFactory<ExistenceClientStateMainScreen>();

}


/// Register Object
void GameStateHandler::RegisterObject(Context* context)
{
    context->RegisterFactory<GameStateHandler>();
}

void GameStateHandler::Start(void)
{

    ///mainNode = scene->CreateChild("Main");
    createState(ExistenceClientStateLogin::GetTypeNameStatic());

}

/// Temporary
String  GameStateHandler::getCurrentState(void)
{
    /// Not Used
    String stateString = String("test") ;

    //String stateString = mStates.Back().GetType();
    return stateString;
}

void GameStateHandler::onStateChange( Urho3D::StringHash eventType, Urho3D::VariantMap& eventData )
{
    /// intercept state event
    GameStates newState=  static_cast<GameStates>(eventData[GameState::P_CMD].GetInt());

    LOGINFO("New State " +  (String)((int)newState)) ;


    switch (newState)
    {
    case GAME_STATE_SINGLETON:
        createState(ExistenceClientStateSingleton::GetTypeNameStatic());
        break;
    case GAME_STATE_LOGIN:
        createState(ExistenceClientStateLogin::GetTypeNameStatic());
        break;
    case  GAME_STATE_ACCOUNTCREATE: //called from button on GameMainMenuSample form
        createState(ExistenceClientStateAccount::GetTypeNameStatic());
        break;
    case  GAME_STATE_PROGRESS:
        createState(ExistenceClientStateProgress::GetTypeNameStatic());
        break;
    case GAME_STATE_PLAYERCREATE:
        createState(ExistenceClientStatePlayer::GetTypeNameStatic());
        break;
    case GAME_STATE_MAINMENU:
        createState(ExistenceClientStateMainScreen::GetTypeNameStatic());
        break;
    case GAME_STATE_GAMEMODE:
        createState(ExistenceClientStateGameMode::GetTypeNameStatic());
        break;
    default:
        ErrorExit("Unkown State " + (String)(int) newState );
        break;
    }
}

void GameStateHandler::createState( String newState )
{
    /// switch states
    if(newState=="ExistenceClientStateSingleton")
    {
        myDerivedSates.push_back(new ExistenceClientStateSingleton(context_));
    }
    else if(newState=="ExistenceClientStateLogin")
    {
        myDerivedSates.push_back(new ExistenceClientStateLogin(context_));
    }
    else
    {
        ErrorExit("Unkown GameState ");
    }
}


/// Not used at the moment
void GameStateHandler::changeState( GameStateComponent* state )
{
    /*LOGINFO("Adding state" + state->GetTypeName());
    //exit from old state
    RemoveLastState();
    //enter  new state
    mStates.Push(state);
    mStates.Back()->Enter();*/

}

/// Not used at the moment
void GameStateHandler::changeState2(ExistenceClientStateSingleton * State)
{
    LOGINFO("Adding state" + State->GetTypeName());

    //exit from old state
    //RemoveLastState();
    //enter  new state
    //mStates.Push(state);
    //mStates.Back()->Enter();

}

/// Not used at the moment
void GameStateHandler::RemoveLastState()
{
    /*  if ( !mStates.Empty() )
      {
          mStates.Back()->Exit();
          //remove component's node  remove node and component
          mStates.Back()->GetNode()->Remove();
          mStates.Pop();
      }*/
}

int GameStateHandler::GetConsoleState(void)
{
    int flag;

    flag = consolestate;

    return flag;
}


int GameStateHandler::SetConsoleState(int flag)
{

    //consolestate=flag;

    return 1;
}

int GameStateHandler::GetUIState(void)
{
    int flag;
    flag=uistate;

    return flag;
}

int GameStateHandler::SetUIState(int flag)
{

    uistate = flag;

    return 1;
}

int GameStateHandler::GetCameraMode(void)
{
    int flag;

    flag = cameramode;

    return flag;;
}

int GameStateHandler::SetCameraMode(int flag)
{

    cameramode = flag;

    return 1;
}

int GameStateHandler::GetDebugHudMode(void)
{
    int flag;

    flag = debughud;

    return flag;;
}

int GameStateHandler::SetDebugHudMode(int flag)
{

    debughud = flag;

    return 1;
}

//}



Main
[/code]


ExistenceClient.H and code on GItHub
[code]#ifndef EXISTENCECLIENT_H
#define EXISTENCECLIENT_H

//
// Copyright (c) 2008-2014 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

#define DISPLAYMESH_MUILTIPLECHARACTER 1
#define DISPLAYMESH_SINGLECHARACTER 2

#define UIBLANK 0
#define UIMAIN  1

#define CHARACTERMAINSCENE          0
#define CHARACTERUISCENE            1

#define CAMERAORIENTATIONROTATEYAW 1
#define CAMERAORIENTATIONROTATEPITCH 1

#include "../../../Urho3D/Procedural/Rules.h"

#include <time.h>

#include "../ExistenceApps.h"
#include "../Account.h"
#include "../factions.h"
#include "../Player.h"
#include "../PlayerLevels.h"


#include "GameStateEvents.h"
#include "GameStateHandler.h"





string ConvertUIntToString(unsigned int val);

/// This first example, maintaining tradition, prints a "Hello World" message.
/// Furthermore it shows:
///     - Using the Sample / Application classes, which initialize the Urho3D engine and run the main loop
///     - Adding a Text element to the graphical user interface
///     - Subscribing to and handling of update events
class ExistenceClient : public ExistenceApp
{
    /// friend the other classes
    friend class ExistenceClientStateSingleton;
    friend class ExistenceClientStateAccount;
    friend class ExistenceClientStateProgress;
    friend class ExistenceClientStateGameMode;
    friend class ExistenceClientStateLogin;
    friend class ExistenceClientStatePlayer;
    friend class ExistenceClientStateMainScreen;

    OBJECT(ExistenceClient);

    /// Construct.
    ExistenceClient(Context* context);

    /// Setup after engine initialization and before running the main loop.
    virtual void Start();

    /// Return XML patch instructions for screen joystick layout for a specific sample app, if any.https://github.com/urho3d/Urho3D/tree/master/Source/Samples
    virtual String GetScreenJoystickPatchString() const
    {
        return
            "<patch>"
            "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Hat0']]\">"
            "        <attribute name=\"Is Visible\" value=\"false\" />"
            "    </add>"
            "</patch>";
    }

    /// Diaplay login screen
    void SetupScreenViewport(void);
    void SetupScreenUI(void);

    /// Subscribe to application-wide logic update events.
    void SubscribeToEvents();
    /// Handle the logic update event.
    void HandleUpdate(StringHash eventType, VariantMap& eventData);
    /// Events Keyboard
    void HandleKeyDown(StringHash eventType, VariantMap& eventData);

    void HandleInput(const String& input);
    void eraseScene(void);

    void AddLogoViewport(void);

    int CreateCursor(void);

    void MoveCamera(float timeStep);
    void Print(const String& output);

    void HandlePostUpdates(StringHash eventType, VariantMap& eventData);

    /// Render related functions
    int LoadCharacterMesh(int mode, String nodename, unsigned int alienrace, unsigned int gender);
    int loadplayerMesh(Node * playermeshNode, int alienrace, int gender,int mode);

    /// File related functions
    void LoadAccount(void);
    void SaveAccount(accountinformation account);
    void SavePlayer(bool activeplayer);
    int LoadAccountPlayers(void);
    int LoadPlayer(int player);
    int LoadTemporaryPlayer(int player);
    int GenerateSceneLoadDifferential(const char *filename=NULL);
    int LoadEnvironmentSettings(const char *environment);

    /// Console related functions
    void InitializeConsole(void);
    void HandleConsoleCommand(StringHash eventType, VariantMap& eventData);

    int ConsoleActionEnvironment(const char * lineinput);
    int ConsoleActionCamera(const char * lineinput);
    int ConsoleActionDebug(const char * lineinput);
    int ConsoleActionCharacter(const char * lineinput);
    int ConsoleActionRenderer(const char * lineinput);
    int ConsoleActionBuild(const char * lineinput);

    /// UI Related Functions

    void loadSceneUI(void);
    bool loadHUDFile(const char * filename, const int positionx, const int positiony);
    void loadUIXMLClosePressed(StringHash eventType, VariantMap& eventData);
    bool loadUIXML(int windowtype, const int positionx, const int positiony, int selected);
    void QuickMenuPressed(StringHash eventType, VariantMap& eventData);
    void UpdateUI(float timestep);
    void PlayerWindowUpdateUI(int selected);
    void PlayerWindowHandleDisplaySelection(StringHash eventType, VariantMap& eventData);
    int UpdateUISceneLoader(void);
    void UpdatePlayerInfoBar(void);
    void SceneLoaderHanderPress(StringHash eventType, VariantMap& eventData);
    int GenerateSceneUpdateEnvironment(terrain_rule terrainrule);

    /// Temporary online
    bool IsClientConnected(void);
    bool ClientConnect(void);
    bool SetServerSettings(void);

    /// Get subsubsystems
    Renderer * GetRenderSubsystems(void);
    UI * GetUISubsystems(void);
    Graphics * GetGraphicsSubsystems(void);
    ResourceCache * GetResourceCacheSubsystems(void);

    Window * GetSharedWindow(void);

protected:
private:

    /// Urho3D window shared pointers
    SharedPtr<Window> window_;
    SharedPtr<Window> window2_;

    /// Urho3D UIelement root, viewport, and render path
    SharedPtr<UIElement> uiRoot_;
    SharedPtr<Viewport> viewport;

    SharedPtr<RenderPath> effectRenderPath;

    /// Urho3D Shared pointer for input
    SharedPtr<Input> input_;

    /// Existence Weak pointer for a single character
    WeakPtr<Character> character_;

    /// Existence Game State Handler Pointer for Game State
    GameStateHandler * ExistenceGameState;

    /// Existence player structure class and variable declation for character/player related information
    Player  TemporaryPlayer;
    Player  * TemporaryAccountPlayerList;
    unsigned int TemporaryAccountPlayerSelected;
    unsigned int TemporaryAccountPlayerListLimit;

    /// Existence class and variable declaration for alien race alliance information
    vector<string> aliensarray;
    vector<string> tempaliensarray;

    /// This is temoporarily the necessary code
    bool accountexist;

    bool ServerConnection;
};


/// Login State
class ExistenceClientStateSingleton: public ExistenceClient
{
    OBJECT(ExistenceClientStateSingleton);
public:
    ExistenceClientStateSingleton(Urho3D::Context * context);
    virtual ~ExistenceClientStateSingleton();
    virtual void Enter();
    virtual void Exit();
    virtual void OnUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData );
private:
    void Singleton(void);
protected:

};

/// Login State
class ExistenceClientStateLogin : public ExistenceClient
{
    OBJECT(ExistenceClientStateLogin);
public:
    ExistenceClientStateLogin(Urho3D::Context * context);
    virtual ~ExistenceClientStateLogin();
    virtual void Enter();
    virtual void Exit();
    virtual void OnUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData );
private:
    void LoginScreen(void);
    void LoginScreenUI(void);
    void LoginScreenUINewAccountHandleClosePressed(StringHash eventType, VariantMap& eventData);
    void LoginScreenUILoginHandleClosePressed(StringHash eventType, VariantMap& eventData);

protected:

};

/// Account State
class ExistenceClientStateAccount: public ExistenceClient
{
    OBJECT(ExistenceClientStateAccount);
public:
    ExistenceClientStateAccount(Urho3D::Context * context);
    virtual ~ ExistenceClientStateAccount();
    virtual void Enter();
    virtual void Exit();
    virtual void OnUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData );
private:
    void Account(void);
    void CreateAccountScreenUI(void);
    void CreateAccountUIHandleClosePressed(StringHash eventType, VariantMap& eventData);
protected:

};

/// Main Screen State
class ExistenceClientStateMainScreen: public ExistenceClient
{
    OBJECT(ExistenceClientStateMainScreen);
public:
    ExistenceClientStateMainScreen(Urho3D::Context * context);
    virtual ~ExistenceClientStateMainScreen();
    virtual void Enter();
    virtual void Exit();
    virtual void OnUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData );
private:
    void MainScreen(void);
    void MainScreenUI(void);
    void MainScreenUIHandleClosePressed(StringHash eventType, VariantMap& eventData);
    void HandleCharacterStartButtonReleased(StringHash eventType, VariantMap& eventData);
    void HandleCharacterSelectedReleased(StringHash eventType, VariantMap& eventData);
    void HandleCharacterSelectedInfoButtonReleased(StringHash eventType, VariantMap& eventData);
protected:

};

/// Main Screen State
class ExistenceClientStateGameMode: public ExistenceClient
{
    OBJECT(ExistenceClientStateGameMode);
public:
    ExistenceClientStateGameMode(Urho3D::Context * context);
    virtual ~ExistenceClientStateGameMode();
    virtual void Enter();
    virtual void Exit();
    virtual void OnUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData );
private:
    void GameMode(void);
protected:

};

/// Player Create Login State
class ExistenceClientStatePlayer: public ExistenceClient
{
    OBJECT(ExistenceClientStatePlayer);
public:
    ExistenceClientStatePlayer(Urho3D::Context * context);
    virtual ~ExistenceClientStatePlayer();
    virtual void Enter();
    virtual void Exit();
    virtual void OnUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData );
private:
    void Player(void);
    void CreatePlayerScreenUI(void);
    void HandlerCameraOrientation(StringHash eventType, VariantMap& eventData);
    void CameraOrientationRotateMove (float degrees, int movement);
    void HandleMouseReleased(StringHash eventType, VariantMap& eventData);
    void CreatePlayerUIHandleClosePressed(StringHash eventType, VariantMap& eventData);
    void loadSceneCreationCreation(const char * lineinput);
    void CreatePlayerUIHandleControlClicked(StringHash eventType, VariantMap& eventData);
    void HandlePersonalitySelectionItemClick(StringHash eventType, VariantMap& eventData);
protected:

};

/// Main Screen State
class ExistenceClientStateProgress :public ExistenceClient
{
    OBJECT(ExistenceClientStateProgress);
public:
    ExistenceClientStateProgress(Urho3D::Context * context);
    virtual ~ExistenceClientStateProgress();
    virtual void Enter();
    virtual void Exit();
    virtual void OnUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData );
private:
    void Progress(void);
    void ProgressScreenUI(void);
    void ProgressScreenUIHandleClosePressed(StringHash eventType, VariantMap& eventData);
    void CreateCharacter(void);
    void GenerateScene(terrain_rule terrainrule,const char *differentialfilename);
    int GenerateSceneBuildWorld(terrain_rule terrainrule);
    void loadDummyScene(void);
    void loadScene(const int mode, const char * lineinput);
protected:

};


/// Miscellanous functions
vector<string> split(const string& s, const string& delim, const bool keep_empty=true);
time_t ConvertStringToTime(const char * buff, time_t timeseed);
string GenerateName(char group, char subgroup);

string ConvertUIntToString(unsigned int val);
float cutoff(float inputvalue, float pointmid, float range,bool debug);
float StringToFloat(string buffer);
Vector3 NormalizedToWorld(Image *height, Terrain *terrain, Vector2 normalized);
typedef std::pair<float,float> range ;
bool intersects( range a, range b );
range make_range( float a, float b );

#endif
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:05:37 UTC | #8

Hi

I ran into a hiccup and need help. The game state changer works fine but some reading the game mode load part doesn'. The status text does not update but if youlook at the picture with the window it actually runs.

[imgur.com/a/K9F9q](http://imgur.com/a/K9F9q)

I can't figure it out after throwing a massive amount of debug messages and looking at the call stack. So, I uploaded the code to Github including resources needed mentioned in the blog.

As to the status, its pretty much a running standalone, I did not add scene save(any changes) or save user changes etc. Waiting to make a playable game with purpose.

As to everything, if anyone wants to help me develop it while I can focus back on the procedural expect. I welcome any additional developer and hopefully present Urho3D and provide a gaming experience. Aka. A game for now.

Some areas I can see is more in depth, character display, ghost mode save and load, NPC(with varied AI), content like some starbases and ground map, object interaction, inventory attachment systems, vehicles, armor, guns etc and above all exploration objections with a bunch of surprise.

This is my call out to develop it full speed. My email is [cgprojectsfx@gmail.com](mailto:cgprojectsfx@gmail.com)

Vivienne Anthony

-------------------------

