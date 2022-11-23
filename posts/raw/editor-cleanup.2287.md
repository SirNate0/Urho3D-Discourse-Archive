TheComet | 2017-01-02 01:14:31 UTC | #1

I'm trying to get the editor to run in-game, so when the user presses ESC once it starts the editor on the currently active scene, and when he presses ESC again it takes him back to the game.

I'm running into a LOT of difficulty with this, because the editor doesn't perform any cleanup when Stop() is called, other than calling SaveConfig(). All of the UI elements, cameras, viewports and event handlers remain active after the editor has been stopped.

Is there something I'm missing? Perhaps some script function that I need to call manually to do the cleanup? Perhaps some magic Urho3D::ScriptFile member function that cleans up everything a script has done?

EDIT: Would it perhaps be possible to create a new Context in which I can run the editor, and let the context do the cleanup for me? Is that a viable solution to this issue?

-------------------------

cadaver | 2017-01-02 01:14:31 UTC | #2

The editor hasn't been programmed with the idea that it could be shared with a running game. 

For practical purposes I recommend spawning a second process either for the editor or for the game, whatever feels better.

Alternatively you could start cleaning up the editor exit and submit a PR, but for a general case there will be always the problem that the editor will destroy the game's UI.

-------------------------

TheComet | 2017-01-02 01:14:32 UTC | #3

Yeah I think you are right. Another downside of opening the editor on the active scene is that components added/removed during gameplay show up in the hierarchical view, along with other custom components that are registered by the game. You don't really want those to be saved in the scene.

Consider this solved!

-------------------------

cadaver | 2017-01-02 01:14:32 UTC | #4

For that there's already a sort of solution, the editor can optionally make a scene backup when it starts to "play" scene updates and rolls back to the backup when you press "stop". That would just have to be extended for external control.

Also, there have been ideas to "desingletonize" the UI, for example using in 3D in-world UI's. In that case it should also be possible for the editor to have its own UI hierarchy, which doesn't disturb the game's UI hierarchy. However I don't recommend holding your breath for this, as it's not clear who (if anyone) is going to implement it. After that there would only be the case of other subsystems with their global settings getting affected (Audio, Renderer..)

-------------------------

