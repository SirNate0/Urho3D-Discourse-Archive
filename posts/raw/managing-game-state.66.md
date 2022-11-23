carlomaker | 2017-01-02 00:57:44 UTC | #1

This is a simple game state  manager inspired from a good article about [url=http://gamedevgeek.com/tutorials/managing-game-states-in-c]managing game states[/url]  , i tried to adapt it in Urho3d 
using events rather than loops update on virtual methods that kill performance.

GameStateHandler  is a states manager ;
IGameState  state  base class ,
GameIntroSample   splash screen 
GameMainMenuSample  ,a class for general purposes

[spoiler][gist]https://gist.github.com/CarloMaker/8689585[/gist][/spoiler]

-------------------------

vivienneanthony | 2017-01-02 01:05:22 UTC | #2

[quote="carlomaker"]This is a simple game state  manager inspired from a good article about [url=http://gamedevgeek.com/tutorials/managing-game-states-in-c]managing game states[/url]  , i tried to adapt it in Urho3d 
using events rather than loops update on virtual methods that kill performance.

GameStateHandler  is a states manager ;
IGameState  state  base class ,
GameIntroSample   splash screen 
GameMainMenuSample  ,a class for general purposes

[spoiler][gist]https://gist.github.com/CarloMaker/8689585[/gist][/spoiler][/quote]

Hey. I need to update my state manager so I can do stuff load splash and preloading screens.

I'm looking at your code and trying to figure it out.

From what I can see each main area of a game would go in a subclass in the igamestate. In my code, that's probably Login, CreateAccount, CreatePlayer, MainScreen, PreloadGameMode(I want to add), GameMode.

The Class Wiki I'm assume would be my App class to ExistenceClient.

Main Git and specific Source 
[github.com/vivienneanthony/Urho ... -Existence](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence)
[github.com/vivienneanthony/Urho ... stenceApps](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/tree/development/Source/ExistenceApps)

I will be doing a lot of cleanup. It is missing error and dialog prompts, worst case checks like missing files, and some other things.

Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:05:22 UTC | #3

I'm  not sure what the use of the 	[code]Urho3D::SharedPtr<Urho3D::Node> mainNode;[/code] would be.

-------------------------

thebluefish | 2017-01-02 01:05:23 UTC | #4

That just creates a root node "Main" under the scene. If you don't want to use this, you can safely remove its use. It will not affect the functionality of the state manager.

-------------------------

vivienneanthony | 2017-01-02 01:05:23 UTC | #5

[quote="thebluefish"]That just creates a root node "Main" under the scene. If you don't want to use this, you can safely remove its use. It will not affect the functionality of the state manager.[/quote]

I got the code in and placed it on Github. I just can't figure out how to change the state.

[github.com/vivienneanthony/Urho ... stenceApps](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence/tree/development/Source/ExistenceApps)

-------------------------

vivienneanthony | 2017-01-02 01:05:23 UTC | #6

[quote="carlomaker"]This is a simple game state  manager inspired from a good article about [url=http://gamedevgeek.com/tutorials/managing-game-states-in-c]managing game states[/url]  , i tried to adapt it in Urho3d 
using events rather than loops update on virtual methods that kill performance.

GameStateHandler  is a states manager ;
IGameState  state  base class ,
GameIntroSample   splash screen 
GameMainMenuSample  ,a class for general purposes

[spoiler][gist]https://gist.github.com/CarloMaker/8689585[/gist][/spoiler][/quote]


How is the event change triggered??

-------------------------

