Enhex | 2017-01-02 01:06:26 UTC | #1

The documentation on ScriptObject is confusing.
So far I understood that it's like a LogicComponent.
ScriptInstance is the Urho3D component for instancing a single ScriptObject for a node.

Is that correct?
Am I missing anything?

-------------------------

Bluemoon | 2017-01-02 01:06:27 UTC | #2

Yeah you are kind of correct. And No, you are not missing anything much?
If I'm to put it in the AngelScript context  (I have never touched lua  :confused:  ), Script Object are Angel Script Classes that can be added to nodes like components through the help of the ScriptInstance component. And as started in the documentation
[quote]The class must implement the empty interface ScriptObject to make its base class statically known[/quote]
Sure, just like LogicComponent you can subscribe for event and send event, coupled with other additional functions

In one of the projects I work on, the Game Objects (players and enemies) are implemented as Script Objects and even creating of models are handled by them

-------------------------

cadaver | 2017-01-02 01:06:27 UTC | #3

ScriptObject is somewhat of a dummy, because in theory it could be any class, Urho3D doesn't mandate it to implement any functions or other members, but rather ScriptInstance "scans" it after instantiation to see if it implements any of the LogicComponent-like functions.

However for AngelScript practical use (to be able to transport these objects between C++ and script nicely) we need a known (base) class for the objects that can be contained by ScriptInstance.

-------------------------

