johnnycable | 2017-03-16 16:55:42 UTC | #1

I have a noob question. Is there in Urho something like a scheduler/sequencer in the form:
execute/schedule(function(), number_of_times, time_interval)?
That's to execute the function times number of times every time interval...
Should be something tied to fixed timestep logic, what is the right event to connect it? E_PHYSICSPRESTEP ?
Running such a scheduler with physics steps could be an escamotage, but being a noob I cannot foresee if it could work...

-------------------------

rasteron | 2017-03-17 20:54:40 UTC | #2

You can do it with PhysicsPreStep like here in NSW..

https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/NinjaSnowWar.as#L79-L80

Where it spawns objects at intervals with timestep

https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/NinjaSnowWar.as#L433-L440

-------------------------

johnnycable | 2017-03-17 08:59:53 UTC | #3

Ok, that hooks to the physics simulation then, as expected. 
Thank you very much.

-------------------------

