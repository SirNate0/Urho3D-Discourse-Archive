Enhex | 2017-01-02 01:08:17 UTC | #1

Right now ComponentRemoved is only sent from the scene.

Being able to subscribe to node specific component removed event is useful.
For example when creating temporary nodes for 3D sounds that play once. (NinjaSnowWar uses arbitrary time limit to remove the node)

-------------------------

cadaver | 2017-01-02 01:08:17 UTC | #2

The scene introspection events were originally provided for use by the editor or other tools. Making also nodes send them would add overhead, though fairly minor.

I would advise against basing logic on component additions / removals themselves, since most of the time you are doing them yourself, and know the higher-level cause (for example "object received damage" or such) The sound playback is an exception, as the sound component removes itself. 

EDIT: on further thought, the whole mechanism is a bit nasty, since it's the only place in Urho where a component removes itself automatically. IMO it should be deprecated. Instead the playback end should send an event, and the node's logic could react accordingly (for example remove the node.) Similarly, particle emitters could send a finish event, in which case lifetime counting for something as simple as the both of them would become unnecessary.

-------------------------

Enhex | 2017-01-02 01:08:17 UTC | #3

Components sending finish events sounds much better.

-------------------------

cadaver | 2017-01-02 01:08:17 UTC | #4

The sound finished event is already in the master (and examples tweaked for it), the rest is to follow.

-------------------------

