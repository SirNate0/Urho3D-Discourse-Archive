vivienneanthony | 2017-01-02 01:05:17 UTC | #1

Hi

Have any made a load game mode loader? Something that does something like 

My idea of a preloader

Viv

[code]
SET game preloader mode
fade out current scene
fade in game preloader scene
Upgrade progress bar text
load character
Update progress bar text
IF fail 
  display error prompt
  fade out game preloader scene
  Fade in current scene
  Exit
Load scene
DO 
 Update progress bar state i
 Update progress bar effect
WHIle scene loading or timeout falsr
IF timeout
  display error prompt
  fade out game preloader scene
  Fade in current scene
  Exit 
ElSE
 Update progress bar state i
 Update progress bar effect
 SET game to game mode 
 fade out game preloader screen
 fade in new scene
END IF
return success

[/code]

-------------------------

globus | 2017-01-02 01:05:18 UTC | #2

It can help:

Managing Game State
[url]http://discourse.urho3d.io/t/managing-game-state/66/1[/url]

OverLib
[url]http://discourse.urho3d.io/t/overlib/762/1[/url]

[SOLVED] how to create a loading screen
[url]http://discourse.urho3d.io/t/solved-how-to-create-a-loading-screen/58/1[/url]

Simple Splash screen
[url]http://discourse.urho3d.io/t/simple-splash-screen/127/1[/url]

Perhaps it makes sense do example for it.
With "Continue" button (for not loading big scene).
But the State Manager is logic stuff and depending from the specific project design.

-------------------------

vivienneanthony | 2017-01-02 01:05:19 UTC | #3

Hello

I'll look at the code. I have to decipher it compared my current code. Usually happens if I am not sure what's going on. I spend more time deciphering.

I have something that saves a game state basically a class which I assign flags. It's nothing special but I think I made it to be in the same concept.

Hmmm.

Viv

[quote="globus"]It can help:

Managing Game State
[url]http://discourse.urho3d.io/t/managing-game-state/66/1[/url]

OverLib
[url]http://discourse.urho3d.io/t/overlib/762/1[/url]

[SOLVED] how to create a loading screen
[url]http://discourse.urho3d.io/t/solved-how-to-create-a-loading-screen/58/1[/url]

Simple Splash screen
[url]http://discourse.urho3d.io/t/simple-splash-screen/127/1[/url]

Perhaps it makes sense do example for it.
With "Continue" button (for not loading big scene).
But the State Manager is logic stuff and depending from the specific project design.[/quote]

-------------------------

