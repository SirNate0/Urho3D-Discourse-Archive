Ray_Koopa | 2017-01-02 01:13:46 UTC | #1

I probably didn't quite grasp the scene management...

Anyway, I thought scenes are used for different stages of the game. Like:
[ul][li]Main Menu[/li]
[li]In-Game (with some nodes for a pause menu overlay)[/li]
[li]Level Editor[/li][/ul]

I only know that a scene is simply instantiated in the Application class when the game starts. But how does the engine actually know which scene is "active"? How can I make another scene active?

Or is there only one and just one scene in Urho3D in which I have to remove all child nodes and insert new ones when switching between the stages mentioned in the list above?

-------------------------

1vanK | 2017-01-02 01:13:46 UTC | #2

[code]        SharedPtr<Viewport> viewport(new Viewport(context_, scene_, camera));
        GetSubsystem<Renderer>()->SetViewport(0, viewport);[/code]

-------------------------

Ray_Koopa | 2017-01-02 01:13:46 UTC | #3

So I just modify the viewport? What happens to nodes in the scene not given to the Viewport anymore? Won't they continue to update and play sounds?

-------------------------

1vanK | 2017-01-02 01:13:46 UTC | #4

[code]/// Enable or disable scene update.
void Scene::SetUpdateEnabled(bool enable);[/code]

-------------------------

Ray_Koopa | 2017-01-02 01:13:47 UTC | #5

Yeah, okay. That disables further updates. But what happens to already playing sounds? They should be stopped.

-------------------------

1vanK | 2017-01-02 01:13:47 UTC | #6

All sound sources from disabled scene paused

-------------------------

Ray_Koopa | 2017-01-02 01:13:47 UTC | #7

Hmm okay, if that's the "official" way to go, I'm gonna try it.

-------------------------

1vanK | 2017-01-02 01:13:47 UTC | #8

Note that the scene should to be changed at the beginning of iteration of a game loop. Otherwise, errors may occur. I mostly use this way:

[code]    Game(Context* context) : Application(context)
    {
        // First handler for first event.
        SubscribeToEvent(E_BEGINFRAME, URHO3D_HANDLER(Game, ApplyGameState));
    }

    void ApplyGameState(StringHash eventType, VariantMap& eventData)
    {
        if (GLOBAL->gameState_ != GLOBAL->neededGameState_)
        {
            // Change game state logic.
            ....
            GLOBAL->gameState_ = GLOBAL->neededGameState_;
        }

        if (GLOBAL->currentLevelIndex_ != GLOBAL->neededLevelIndex_)
        {
            GLOBAL->currentLevelIndex_ = GLOBAL->neededLevelIndex_;
            // Change scene.
            ....
        }
    }

[/code]

It works like [docs.unity3d.com/ScriptReferenc ... Level.html](https://docs.unity3d.com/ScriptReference/Application.LoadLevel.html)

[quote]Actual level change happens in the beginning of the next frame[/quote]

-------------------------

cadaver | 2017-01-02 01:13:49 UTC | #9

To clarify sound management further, you usually have a SoundListener which is in a node in a certain scene. You can switch the currently active SoundListener (there can only be one at a time) from the Audio subsystem.

Menu / UI -type sounds can also be played "scenelessly" if you're not using SoundSource3D, however a sound source still needs to be attached to a node. See the example number 14.

-------------------------

Ray_Koopa | 2017-01-02 01:13:51 UTC | #10

[quote="1vanK"][code]/// Enable or disable scene update.
void Scene::SetUpdateEnabled(bool enable);[/code][/quote]
Shouldn't this prevent all the components in the nodes in the scene on which this is set to false from getting updates called on them?

I made a simple RotatorComponent which dumbly rotates an object. When I call SetUpdateEnabled(false), it still rotates...

-------------------------

cadaver | 2017-01-02 01:13:51 UTC | #11

It depends on what event you are listening to for the update. Scene update events will be stopped by updateEnabled = false, global application update event is not. If in doubt, you probably should ask from the authors of the C# binding.

If you check Urho's 05_AnimatingScene example, the object rotation stops properly by updateEnabled being set to false.

-------------------------

Scellow | 2017-01-02 01:13:51 UTC | #12

Here is how i do:


[code]
    public class BaseScene : Scene
    {
        public virtual void Init() { }

        public virtual void CleanUI()
        {
            TheRoguer.Instance.UI.Root.RemoveAllChildren();
        }
        
        public virtual void Dispose() { }
    }

    public class LoginScene : BaseScene
    {
        // ..
    }



    public class SceneManager
    {
        public BaseScene Scene;

        public static SceneManager Instance = new SceneManager();


        public void SetScene(BaseScene scene)
        {
            Scene?.CleanUI();
            Scene?.Dispose();
            Scene?.Remove();

            Scene = scene;
            Scene.Init();
        }
    }
[/code]



And to change scene: 

            SceneManager.Instance.SetScene(new LoginScene());

There are probably better ways to do that, but it works fine for my needs

-------------------------

Ray_Koopa | 2017-01-02 01:13:51 UTC | #13

Yeah, that's similar to how I do it by now. Though I still have the scene switching logic in my Application class. I also switch the scene in BeginFrame as it was suggested earlier.
Took me some time to understand inheriting from `Scene` is actually not that bad and kinda required for such a logic to work fine.

The only thing that still raises my eyebrows a little is that you call Scene?.Remove(), but the doc says it removes the scene from the parent node, but the scene is the root, so that shouldn't have any effect, or should it?

Here's my code, though it uses the UrhoSharp C# wrapper.
[code]public class Game : Application
{
	private StageBase _currentStage;
	private StageBase _nextStage;

	public Game()
		: base(new ApplicationOptions("Data"))
	{
	}

	internal StageBase CurrentStage
	{
		get
		{
			return _currentStage;
		}
		set
		{
			// Do not immediately change the stage, and queue it to be done at the start of the next frame.
			_nextStage = value;
		}
	}

	protected override void Start()
	{
		Time.FrameStarted += Time_FrameStarted;
		CurrentStage = new MenuStage(this);
	}
	
	private void Time_FrameStarted(FrameStartedEventArgs obj)
	{
		// Switch the stage if any was queued.
		if (_nextStage != null)
		{
			// Give the stage a chance to cleanup (and possibly store its status later on). Then destroy all nodes.
			if (_currentStage != null)
			{
				_currentStage.Stop();
				_currentStage.UpdateEnabled = false;
				_currentStage.Clear(true, true);
				_currentStage.Remove();
				UI.Clear();
			}

			// Activate the new stage and call its method to set itself up.
			_currentStage = _nextStage;
			_currentStage.Start();
			_nextStage = null;
		}
	}
}[/code]

My extended Scenes are called "Stages" for whatever reason I might not like soon :stuck_out_tongue:
[code]internal abstract class StageBase : Scene
{
	internal StageBase(Game game)
	{
		Game = game;
	}

	protected Game Game { get; private set; }

	internal abstract void Start();

	internal abstract void Stop();
}[/code]

-------------------------

