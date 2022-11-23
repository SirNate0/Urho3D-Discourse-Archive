sabotage3d | 2017-01-02 01:10:20 UTC | #1

Hi, 
I am adding a new class part of the Urho3D namespace where I want to call the engine's update directly. Is it possible to access it without subscribing to the event? Is it recommended doing something like this?

-------------------------

cadaver | 2017-01-02 01:10:20 UTC | #2

If you want to call Engine::Update() manually, then you shouldn't be calling Engine::RunFrame() anywhere, since that already calls update and there would be double-update per frame. But yes, that is possible, since anything that Engine::RunFrame() does is available publicly.

You can take a look at the ProcessOneFrame() function from the tundra-urho3d project [github.com/realXtend/tundra-urh ... mework.cpp](https://github.com/realXtend/tundra-urho3d/blob/master/src/TundraCore/Framework/Framework.cpp) (around line 316) where we measure the frame timestep manually, update our own subsystems outside Urho, then also update the Urho engine.

I wouldn't recommend this in any case where the usual call to Engine::RunFrame() does the job. Events sent as part of the frame update should normally be used to hook in the application functionality.

-------------------------

sabotage3d | 2017-01-02 01:10:23 UTC | #3

Thanks cadaver. The idea is to call update on an action system with a queue of blocking and non-blocking actions. Some will be called sequentially others asynchronously. Would this work using the E_UPDATE event?

-------------------------

cadaver | 2017-01-02 01:10:28 UTC | #4

I would probably just make the action system subscribe to the E_UPDATE event to update itself every frame, and check which actions are valid to advance. The actions themselves should use some different event to avoid confusion with the builtin events, or perhaps have a virtual method which the action system calls.

-------------------------

