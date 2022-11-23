rogerdv | 2017-01-02 01:02:36 UTC | #1

While developing my game states system I found a problem. I have this parent class:

[code]class GameState
{
	GameState() {}
	void Init() {Print("Gamestate init");}
	void Leave() {}
	void HandleUpdate(StringHash eventType, VariantMap& eventData) {}
	void HandleKeyDown(StringHash eventType, VariantMap& eventData) {}
	void HandleKeyUp(StringHash eventType, VariantMap& eventData) {}
	void HandleControlClicked(StringHash eventType, VariantMap& eventData) {}
}
[/code]

The game states inherit from this class. I tried to avoid having an state manager, but I found that it was difficult to go back to previous states, so I added the manager class:

[code]
#include "Scripts/Engine/GameState.as"

class StateManager
{
  StateManager()
  {
    states.Clear();
  }

  void SubscribeToEvents()
  {
    //SubscribeToEvent(scene, "SceneUpdate", "HandleUpdate");
		SubscribeToEvent("KeyDown", "HandleKeyDown");
		SubscribeToEvent("KeyUp", "HandleKeyUp");
		SubscribeToEvent("UIMouseClick", "HandleControlClicked");
  }

  void Push(GameState st)
  { 
    states.Push(st);
    states[states.length-1].Init();
  }

  /**
  Removes state on top
  */
  void Pop()
  {
    //exit current state
    states[states.length].Leave();
    states.Pop();
  }


  void HandleUpdate(StringHash eventType, VariantMap& eventData)
  {
    states[states.length-1].HandleUpdate(eventType, eventData);
  }

	void HandleKeyDown(StringHash eventType, VariantMap& eventData)
	{
    states[states.length-1].HandleKeyDown(eventType, eventData);
	}

	void HandleKeyUp(StringHash eventType, VariantMap& eventData)
	{
    states[states.length-1].HandleKeyDown(eventType, eventData);
	}

	void HandleControlClicked(StringHash eventType, VariantMap& eventData)
	{
    states[states.length-1].HandleKeyDown(eventType, eventData);
  }

	Array<GameState> states;
	int current;
}[/code]

But there is aproblem here. The StateManager.Push() function always calls the ancestor class (GameState) method, instead of calling the derived class metheds, even when I declare them override. So, this code:

[code]
MainMenuState menu;
menu = MainMenuState()
stManager.Push(menu);
[/code]

Instead of executing MainMenuState.Init(), executes GameState.Init(). Perhaps I should include all the game states classes in the StateManager script?

-------------------------

