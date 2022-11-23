att | 2017-01-02 00:58:55 UTC | #1

Hi,
I encountered a problem about physics events.
I created two scenes, main menu scene and game scene which has physics simulation.
When I switched from game scene to main menu scene, the program always crash. I think it is because the node which has rigid body component has been released but the physics world still send collision events to it.

-------------------------

cadaver | 2017-01-02 00:58:55 UTC | #2

What do you mean with switching scenes? Do you destroy the game scene?

Generally the PhysicsWorld code should be quite resilient to components or nodes being removed (examples like NinjaSnowWar do physical object destruction all the time) so maybe you should post some code that will minimally reproduce the crash you're experiencing.

-------------------------

att | 2017-01-02 00:58:55 UTC | #3

No, I just create two scene class, mainMenuScene and gameScene, which all subclass from Object, in gameScene, I tested whether some physics collision occurred, if so, I will change gameScene to mainMenuScene, and the game has just a scene value scene_, which managed by a subsystem sceneManager, like this:
[code]SceneMgr::SceneMgr(Context *context)
: Object(context)
, curScene_(NULL)
{
    scene_ = new Scene(context);
    scene_->CreateComponent<Octree>();
    scene_->CreateComponent<PhysicsWorld>();
}

void SceneMgr::ChangeSceneTo(SCENETYPE type)
{
    if (curScene_ != NULL)
    {
        if (curScene_->GetType() == type)
        {
            return;
        }
        
        curScene_->Stop();
    }
    
    switch (type)
    {
        case SCENE_MAINMENUSCENE:
        {
            curScene_ = new MainMenuScene(context_, scene_);
        } break;
            
        case SCENE_GAMESCENE:
        {
            curScene_ = new GameScene(context_, scene_);
        } break;
            
        default:
            break;
    }

    curScene_->Start();
}
[/code]
in gameScene, I tested the collision start events like this

[code]void GameScene::HandleCollisionEvent(Urho3D::StringHash eventType, VariantMap &eventData)
{
    crashed_ = true;
}

void GameScene::Update(float timeStep)
{
    if (crashed_)
    {
        SceneMgr *mgr = GetSubsystem<SceneMgr>();
        mgr->ChangeSceneTo(SCENE_MAINMENU);

        return;
    }
......[/code]

and when the collision events happen, the game crashed

-------------------------

att | 2017-01-02 00:58:55 UTC | #4

I think I found the crash reason, I subclass the gameScene and mainMenuScene from a baseScene class which have a sharedptr value scene_, when I created these class instance, I will transfer it a scene value from subsystem sceneMgr. I changed the sharedptr to weakptr, the crash disappeared.
I do not know why

[quote="cadaver"]What do you mean with switching scenes? Do you destroy the game scene?

Generally the PhysicsWorld code should be quite resilient to components or nodes being removed (examples like NinjaSnowWar do physical object destruction all the time) so maybe you should post some code that will minimally reproduce the crash you're experiencing.[/quote]

-------------------------

cadaver | 2017-01-02 00:58:56 UTC | #5

Is your curScene_ a raw or a shared pointer? If it's raw then you're leaking objects (leaving the previous one existing and responding to events) when switching.

-------------------------

att | 2017-01-02 00:58:56 UTC | #6

curScene_ is a shared ptr, and it can be normally released.

-------------------------

