vivienneanthony | 2017-01-02 01:08:28 UTC | #1

Hello,

I am trying to be able to use  "GameAssetManager@  AssetManager;" in angelscript for example including calling functions from it. I know how to register components but I'm not sure how to register it fully in the script engine. I'm starting off with this base code.


[code]void EngineEditorApp::Start()
{
    // Start the app
	EngineApp::Start();

    // Register here
	GameAssetManager::RegisterObject(context_);

    // Get Resource path
    ResourceCache * ResCache = g_pApp->GetConstantResCache();

	m_bIsInit = true;

    // Set Script file
	String scriptFileName_ = String("Scripts/Editor.as");
	String extension = GetExtension(scriptFileName_);

    if (extension != ".lua" && extension != ".luc")
    {
        // Instantiate and register the AngelScript subsystem
        context_->RegisterSubsystem(new Script(context_));

        // Get Script engine
        asIScriptEngine * ThisScriptEngine = GetSubsystem<Script>()->GetScriptEngine();

        // Pass Engine
        GameAssetManager::RegisterAPI(ThisScriptEngine);

        // Hold a shared pointer to the script file to make sure it is not unloaded during runtime
        scriptFile_= ResCache ->GetResource<ScriptFile>(scriptFileName_);

        /// \hack If we are running the editor, also instantiate Lua subsystem to enable editing Lua ScriptInstances

        // If script loading is successful, proceed to main loop
        if (scriptFile_ && scriptFile_->Execute("void Start()"))
        {
            // Subscribe to script's reload event to allow live-reload of the application
            SubscribeToEvent(scriptFile_, E_RELOADSTARTED, URHO3D_HANDLER(EngineEditorApp, HandleScriptReloadStarted));
            SubscribeToEvent(scriptFile_, E_RELOADFINISHED, URHO3D_HANDLER(EngineEditorApp, HandleScriptReloadFinished));
            SubscribeToEvent(scriptFile_, E_RELOADFAILED, URHO3D_HANDLER(EngineEditorApp, HandleScriptReloadFailed));

            return;
        }
    }
}
[/code]


and


[code]#include "EngineStd.h"

#include <iostream>

using namespace std;

#include "GameAsset.h"
#include "GameAssetRules.h"
#include "GameAssetManager.h"

#include "Urho3D/AngelScript/APITemplates.h"

// constructor - initialize set default
GameAssetManager::GameAssetManager(Context* context)
    :LogicComponent(context)
    ,m_pGameAssetLibrary(NULL)
    ,m_pGameAssetRuleLibrary(NULL)
    ,m_pGameAssetResources(NULL)

{
    // GameAssetLibrary
    m_pGameAssetLibrary = new Vector<GameAsset*>();
    m_pGameAssetRuleLibrary = new Vector<GameAssetRule*>();

}

// Register Subsystem
void GameAssetManager::RegisterObject(Context* context)
{
    ///context -> RegisterSubsystem(new GameAssetManager(context));

    context->RegisterFactory<GameAssetManager>("EngineStd");


    return;
}

void GameAssetManager::RegisterAPI(asIScriptEngine * engine)
{
    engine->RegisterObjectType("GameAssetManager",0, asOBJ_REF); // asOBJ_REF because you wanted a reference call

    engine->RegisterObjectBehaviour("GameAssetManager",asBEHAVE_ADDREF,"void f()",asFUNCTION(FakeAddRef),asCALL_CDECL_OBJLAST);
    engine->RegisterObjectBehaviour("GameAssetManager",asBEHAVE_RELEASE,"void f()",asFUNCTION(FakeReleaseRef),asCALL_CDECL_OBJLAST);

}


// setup asset path
void GameAssetManager::Init(void)
{
    // get file system
    FileSystem* filesystem = GetSubsystem<FileSystem>();

    m_pGameAssetResources = new GameAssetData(context_);

    // Set Data filename
    m_pGameAssetResources->SetAddDataFile(String("GameData.pak"));

    // initalize base assets
    InitializeBaseGameAssets();

    return;
}

// add game asset - base symbol
GameAsset * GameAssetManager::AddGameAsset(String GA_Name, String GA_Symbol,GameAssetType GA_Type, GameAssetState GA_State)
{
    // if asset library is null
    if(!m_pGameAssetLibrary)
    {
        return NULL;
    }

    // check valid
    if(GA_Name.Empty() || GA_Symbol.Empty())
    {
        return NULL;
    }

    // check if state or type is valid
    if(GA_Type == GAType_None || GA_State==GAState_None)
    {
        return NULL;
    }

    // create new game asset
    GameAsset * newGameAsset;

    newGameAsset = new GameAsset(context_);

    newGameAsset ->SetSymbol(GA_Symbol);
    newGameAsset ->SetTypeState(GA_Type, GA_State);

    // add to library
    m_pGameAssetLibrary->Push(newGameAsset);


    return newGameAsset;
}



[/code]

In the header I defined RegisterObject and RegisterAPI as static void

When I run the editor it says GameAssetManager is not a valid name identifier in the global namespace and the rest of the .as script doesn't compile.  I modifed the code to the above.

I'm just get this when compiling.

[code]||=== Build: EngineEditor in Urho3D (compiler: GNU GCC Compiler) ===|
rho3D-Hangars-Myfork-BuildEditor/include/Urho3D/ThirdParty/AngelScript/angelscript.h|421|error: cannot convert ?GameAssetManager::FakeAddRef? from type ?void (GameAssetManager::)(void*)? to type ?void (GameAssetManager::*)(void*)?|
rho3D-Hangars-MyForkEditor/Source/EngineStd/GameAssetManager/GameAssetManager.cpp|42|note: in expansion of macro ?asFUNCTION?|
Urho3D-Hangars-Myfork-BuildEditor/include/Urho3D/ThirdParty/AngelScript/angelscript.h|421|error: cannot convert ?GameAssetManager::FakeReleaseRef? from type ?void (GameAssetManager::)(void*)? to type ?void (GameAssetManager::*)(void*)?|
Urho3D-Hangars-MyForkEditor/Source/EngineStd/GameAssetManager/GameAssetManager.cpp|43|note: in expansion of macro ?asFUNCTION?|
Urho3D-Hangars-Myfork-BuildEditor/include/Urho3D/ThirdParty/AngelScript/angelscript.h||In instantiation of ?asSFuncPtr asFunctionPtr(T) [with T = void (GameAssetManager::*)(void*)]?:|
rho3D-Hangars-MyForkEditor/Source/EngineStd/GameAssetManager/GameAssetManager.cpp|42|required from here|
Urho3D-Hangars-Myfork-BuildEditor/include/Urho3D/ThirdParty/AngelScript/angelscript.h|1184|error: invalid cast from type ?void (GameAssetManager::*)(void*)? to type ?size_t {aka long unsigned int}?|
||=== Build failed: 3 error(s), 2 warning(s) (0 minute(s), 20 second(s)) ===|
[/code]

Any help is appreciated.



Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:08:28 UTC | #2

This is the header file.

[code]#ifndef GameAssetManager_GameAssetManager_Included
#define GameAssetManager_GameAssetManager_Included


#include "GameAssetData.h"

using namespace std;
using namespace Urho3D;

class URHO3D_API GameAssetManager : public LogicComponent
{
    URHO3D_OBJECT(GameAssetManager, LogicComponent);
public:
    // Constructor and Destructor
    GameAssetManager(Context* context);
    ~GameAssetManager();

    // Register API
    static void RegisterObject(Context* context);

    // Fpr scripting
    static void RegisterAPI(asIScriptEngine * engine);

    void FakeAddRef(void * ptr);
    void FakeReleaseRef(void* ptr);

    // initialize
    void Init(void);

    // add game asset - base symbol
    GameAsset* AddGameAsset(String GA_Name, String GA_Symbol, GameAssetType GA_Type, GameAssetState GA_State);

    // search asset by name
    GameAsset* FindGameAssetByKeyword(String Keyword, bool useName);
    GameAsset* FindGameAssetByName(String Keyword){ return FindGameAssetByKeyword(Keyword, true); };
    GameAsset* FindGameAssetBySymbol(String Keyword){ return FindGameAssetByKeyword(Keyword, false); };

    // load initialial assets
    void InitializeBaseGameAssets(void);

    // load game assets
    bool LoadGameAssets(void)
    {
        if(m_pGameAssetLibrary == NULL || m_pGameAssetResources == NULL)
        {
            return NULL;
        }

        // load into memory
        return m_pGameAssetResources->LoadGameAssets(m_pGameAssetLibrary);
    };


    // find a specific asset
    GameAsset* GetGameAssetByIdx(unsigned int idx);

    // get total assets
    unsigned int GetTotalGameAssets(void);

    // delete asset
    bool DeleteGameAsset(GameAsset* RemoveGameAsset);

private:
    // Game Asset Library - Actual data
    Vector<GameAsset*>*		m_pGameAssetLibrary;
    Vector<GameAssetRule*>* m_pGameAssetRuleLibrary;

    GameAssetData*			m_pGameAssetResources;

};

#endif
[/code]

-------------------------

Enhex | 2017-01-02 01:08:28 UTC | #3

I made my game into a library so I can link it to Urho3DPlayer.
Just look how Urho exposes AngelScript API and do the same.

-------------------------

vivienneanthony | 2017-01-02 01:08:29 UTC | #4

[quote="Enhex"]I made my game into a library so I can link it to Urho3DPlayer.
Just look how Urho exposes AngelScript API and do the same.[/quote]

I'm looking aat the code. Just stuck on registering a object and behaviour.... I'm trying the FakeRef method but just getting cannot convert type so behavious aren't setup.

-------------------------

Enhex | 2017-01-02 01:08:29 UTC | #5

Try looking at "void RegisterPhysicsAPI(asIScriptEngine* engine)" or other functions that expose things to the AS API.

-------------------------

vivienneanthony | 2017-01-02 01:08:32 UTC | #6

Hi

I got this far.

I am just having problems figuring how to get the Node updated to the selected node. I tried LastSelectedNode.Get() pointer then  assigned CreatedGameAsset to it.  That creates a call stack / seg fault error. Hmmm.  

[i.imgur.com/dcbMEjE.png](http://i.imgur.com/dcbMEjE.png)

Vivienne


[code]
void HandleGameAssetChooserDoubleClickedItem(StringHash eventType, VariantMap& eventData)
{
    // load resources here
    GameAssetManager@ pAssetManager = GetGameAssetManager();
    GameAssetFactory@ pAssetFactory = GetGameAssetFactory();

    // Get Game Asset Symbol
    Text@ symbolTextItem = eventData["Element"].GetPtr();
    String symbolNameString = symbolTextItem .vars["Symbol"].GetString();

    // Get Gane Asset
    const GameAsset@ SelectedGameAsset = pAssetManager.FindGameAssetBySymbol(symbolNameString,false);

    // Generate a node
    Node@ CreatedGameAsset= pAssetFactory.CreateNode(SelectedGameAsset, INVALID_GAME_NODE_ID);

    return;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:08:32 UTC | #7

I just tried the following but not sure what's wrong. It crashes and when I try any of the listview. I can't tell if it's calling the handler.


[code]
   // Create a UI
    void CreateGameAssetChooserUI()
    {
        // second one is not needed just added
        if (gameAssetChooserWindow !is null)
        {
            if(gameAssetChooserWindow.visible==false)
            {
                gameAssetChooserWindow.visible=true;
                gameAssetChooserWindow.BringToFront();
            }
            return;
        }

       gameAssetChooserWindow = LoadEditorUI("UI/EditorGameAssetChooser.xml");

       // get file list
       gameAssetsList = gameAssetChooserWindow.GetChild("GameAssetList",true);

       // Subscribe to Events
       SubscribeToEvent(gameAssetChooserWindow.GetChild("CloseButton",true),"Released","HandleGameAssetChooserCloseButton");

       // add ui
       ui.root.AddChild(gameAssetChooserWindow);

       // Bring window to front and position to screen width-300,100
       gameAssetChooserWindow.SetPosition(ui.root.width-300, 100);
       gameAssetChooserWindow.BringToFront();

       GameAssetChooserBuildList();

       //Subscribe
       SubscribeToEvent(gameAssetsList, "ItemDoubleClicked", "HandleGameAssetChooserDoubleClickedItem");
    }

    // Build List
    void GameAssetChooserBuildList()
    {
        // load resources here
        GameAssetManager@ pAssetManager = GetGameAssetManager();
        GameAssetFactory@ pAssetFactory = GetGameAssetFactory();

       // get file list
       //gameAssetsList = gameAssetChooserWindow.GetChild("GameAssetList",true);


        uint NumberOfGameAssets = pAssetManager.GetTotalGameAssets();

        for(uint i=0;i<NumberOfGameAssets;i++)
        {
             GameAsset@ ThisAsset = pAssetManager.GetGameAssetByIdx(i);

                // Create elements
                UIElement@ container2 = UIElement();
                container2.SetLayout(LM_HORIZONTAL, 4);
                container2.SetFixedHeight(ATTR_HEIGHT);
                gameAssetsList.AddItem(container2);

                Text@ text = container2.CreateChild("Text");
                text.text =  ThisAsset.GetAssetSymbol();
                text.name =  String("Symbol");
                // Set Style
                text.SetStyleAuto();

                // Set Style
                text.style="EditorChooserText";
        }


        return;
    }


 void HandleGameAssetChooserDoubleClickedItem(StringHash eventType, VariantMap& eventData)
    {
        // load resources here
        GameAssetManager@ pAssetManager = GetGameAssetManager();
        GameAssetFactory@ pAssetFactory = GetGameAssetFactory();

        // Get Game Asset Symbol
        Text@ symbolTextItem = eventData["Element"].GetPtr();
        String symbolNameString = symbolTextItem.text.Trimmed();

        // Get Gane Asset
        const GameAsset@ selectedGameAsset = pAssetManager.FindGameAssetBySymbol(symbolNameString,false);

        // Create a gameNode
        Node@ gameNode =  pAssetFactory.CreateNode(selectedGameAsset, INVALID_GAME_NODE_ID);   // basically 0

        if(gameNode!is null)
        {
            // Add Child to Scene
            editorScene.AddChild(gameNode);
        }

        return;
    }
[/code]

-------------------------

