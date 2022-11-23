dakilla | 2017-01-02 01:11:27 UTC | #1

Hi

I'd like to be able to use an external time to control urho update and animations from my own editor and its timeline (scratch time forward, backaward, play, stop...). but I didn't see any way to do it actually.

For testings, I modified Engine::RunFrame to give it a time value as parameter and by forcing a custom timeStep_ using this external time value. It works but it's not very elegant. 
How it could be added nicely in urho ? or is there any another way to do that ?

thanks.

-------------------------

hdunderscore | 2017-01-02 01:11:28 UTC | #2

That doesn't sound like a bad way. Another way is you could block the update loop and send your own update events with your timestep.

Either way I imagine there might be issues with perfect sync between going forwards and backwards in time due to precision and the kinds of code you could run (eg, randomised code).

-------------------------

cadaver | 2017-01-02 01:11:29 UTC | #3

In general, things like physics and animation controllers only think of simulating time forward, and your usecase is not really supported, and I would argue it should not be supported by the Urho runtime itself due to the complexity increase that it would cause. When you want to go back in an arbitrary simulation, you need to be saving previous states (e.g. node transforms and velocities) and then restore them, which can consume a lot of memory. For simple animation playback only, you can naturally use AnimationState::SetTime().

You should however be able to do what you're doing without Urho modifications, by calling Engine::SetNextTimeStep() in between RunFrame calls.

-------------------------

dakilla | 2017-01-02 01:11:30 UTC | #4

yes you're right.

Finally, a manually scene update using scene::Update(customtimestep) is good enough for what I need. Physics will be played in realtime.

Thanks for answers.

-------------------------

