vivienneanthony | 2017-01-02 01:05:50 UTC | #1

Hi

Since I can't compile a c/c++ Urho3D editor. How do I add my components to the Editor.as?

Do I have modify Urho3DPlayer.cpp with functions to subscribe to all the custom components? As do I have to add some code to Editor.as to register the components?

I think I did something like this a long time ago. I don't remember

Vivienne

-------------------------

setzer22 | 2017-01-02 01:05:51 UTC | #2

I do it exactly like that, modifying Urho3DPlayer.cpp. I do the registration manually, all my components have a static RegisterObject method so I only have to call that.

-------------------------

vivienneanthony | 2017-01-02 01:05:51 UTC | #3

[quote="setzer22"]I do it exactly like that, modifying Urho3DPlayer.cpp. I do the registration manually, all my components have a static RegisterObject method so I only have to call that.[/quote]


I was looking through the .as scripts to figure out where to add it. Since I'm not familiar with .as but familiar to c++.

-------------------------

