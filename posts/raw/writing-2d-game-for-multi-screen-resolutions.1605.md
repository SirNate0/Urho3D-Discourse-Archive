greenhouse | 2017-01-02 01:08:52 UTC | #1

My workflow In Cocos2d-x is I prepare 3 folders of graphical assets for high-resolution devices, standard and low-resolution devices.
During game initialization I check device's screen resolution and decide which assets to use hd, sd or ld and add search path for assets to that folder.
I also set the Design-Resolution (resolution during design)to be the resolution of the chosen assets folder and Resolution-Policy which specifies which sides of the screen to truncate if device's screen resolution doesn't match to Design-Resolution of assets folder.

How to prepare game and assets to support multi-screen resolutions in Urho3D game?

-------------------------

greenhouse | 2017-01-02 01:08:58 UTC | #2

Anybody writing a 2D game with Urho3D for mobile platforms? :slight_smile:

-------------------------

