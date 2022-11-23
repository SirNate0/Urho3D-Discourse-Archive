thebluefish | 2017-01-02 01:04:13 UTC | #1

I want to manage multiple scenes in my game, and I also want to fire off game events that will be specific to my scene. If I do this globally, events from one scene will interfere with another.

Currently I am sending events to the Scene, and subscribing to the Scene directly for the events I know will be done scene-wide. Is there any better way to do this?

-------------------------

codingmonkey | 2017-01-02 01:04:14 UTC | #2

put into your event a pointer to the scene and check this pointer when you got event for "it is from this scene or not"

-------------------------

TikariSakari | 2017-01-02 01:04:14 UTC | #3

My idea, in a middle of implementing, and might be bad, but I am trying to build a game state manager. Basically I have a stack of game states, such as Main menu -> World menu -> Game -> Options. Each state is just put on top of each other, like in general way of doing game states. Then I pass the so called global events only to the top most state, like handling esc-press only the top most component would have access to it.

The UI I was thinking of handing in a way where I have only one UI, but each state has its own UIElement, and disenable on state changes.

Scenes I was thinking of doing the same way, where each state has its own node-component that is set onto root scene, and they only control the state of their own node. When state is changed then the node might be disenabled. I guess it depends on the game, but for what I was planning there is no need to update the state of the game when being in menus.

Most likely there are a lot of flaws in this, but to my understanding this is a common way of handling multiple states.

-------------------------

thebluefish | 2017-01-02 01:04:14 UTC | #4

That's a common way, but not my preferred way. My state manager works off of the idea that states should be created/destroyed as needed. A MenuState is only present when I need to display the Main Menu, and similarly a GameState is only present when playing the game (and handles its own pause menu). I use a custom UIState class to handle UI "prefabs" that manage their own logic, and can be simply loaded/switched as necessary within a State.

The component idea is weird, and I'm not sure what benefit it allows. You can pause a scene while handling logic in your state, and ideally there would be a different scene for each state. After all, that's what scenes are designed for :p

-------------------------

thebluefish | 2017-01-02 01:04:14 UTC | #5

[quote="codingmonkey"]put into your event a pointer to the scene and check this pointer when you got event for "it is from this scene or not"[/quote]

That's what my old way of doing things was. I find it cleaner and easier to fix mistakes by sending to the Scene directly instead of including it as part of the map.

-------------------------

cadaver | 2017-01-02 01:04:14 UTC | #6

If it's fine that the subscribers need to know that those events will originate from the Scene, I would use the Scene to send the events (you can do this from outside the scene as well, as SendEvent is public), and make the subscribers use the "explicit sender" form of SubscribeToEvent.

-------------------------

