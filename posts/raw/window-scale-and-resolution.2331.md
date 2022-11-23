sabotage3d | 2017-01-02 01:14:48 UTC | #1

Hi I am trying to mimick my mobile device resolution and window scale on dekstop. And I am trying to set window scale different than the resolution. 
For example on desktop I have the window width and height below. On desktop it fills my whole screen is there a way I can scale the window but keep the resolution? I think this is related to the high-DPI settings in SDL 2.0.4. 

[code]    parms_["WindowWidth"] = 1080;
    parms_["WindowHeight"] = 1920;[/code]

-------------------------

rku | 2017-01-02 01:14:48 UTC | #2

Not sure what you mean, but maybe you are looking for UI::SetScale()?

-------------------------

sabotage3d | 2017-01-02 01:14:48 UTC | #3

It is not the UI it is Urho3d window. Let say my resolution is 1080p I want to scale the window 2x smaller but keep the resolution.

-------------------------

Lumak | 2017-01-02 01:14:49 UTC | #4

In one of the industries that I worked, our cabinet (a commercial product) required a monitor on top set vertically and a smaller monitor on bottom.  What we did to emulate it when we had no spare dev cabinet was to just turn our PC monitor sideways :wink:

-------------------------

rku | 2017-01-02 01:14:50 UTC | #5

Is there any reason why you need full mobile resolution on desktop? You can just as easily develop for smaller resolution and make it properly scale.

-------------------------

sabotage3d | 2017-01-02 01:14:50 UTC | #6

I am have some third party libs that are using pixel coordinates.

-------------------------

