vivienneanthony | 2017-01-02 01:11:51 UTC | #1

Hi

Do anyone have any suggestions on smoothing out movement? I think maybe just setting set max FPS.  In the video the login scene and lobby scene is running locally local physics, the hangar is running is client/server mode which the server is handling the physics.

[youtube.com/watch?v=njCHPhf19mY](https://www.youtube.com/watch?v=njCHPhf19mY)

Vivienne

-------------------------

rasteron | 2017-01-02 01:11:51 UTC | #2

Afaik, you can just apply delta or delta time to your player, scene and entity movements. It's already been used on most of the example demos.

-------------------------

Modanung | 2017-01-02 01:11:51 UTC | #3

It looks like the player's position is updated to where it was on the server the moment you stopped walking.

-------------------------

