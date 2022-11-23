codingmonkey | 2017-01-02 01:01:32 UTC | #1

I'm trying to figure out how to slowdown the whole world(scene).
but I do not need same thing slowless for my object.

I make that world is now more slowdown by Scene.SetTimeScale(), 

[code]
	if (input->GetKeyDown(KEY_P)) 
	{
		if (!isTimeScaled) 
		{
			GetNode()->GetScene()->SetTimeScale(0.1f);
			isTimeScaled = true;
		}
	}
[/code]

but how to make a normal speed for my one selected node(object)?
I thought to increase the SetTimeScale in the same number of times that I reduced the speed of the world.
but the object was not his own SetTimeScale()

-------------------------

boberfly | 2017-01-02 01:01:33 UTC | #2

Hi codingmonkey,

Forgive me about stating the obvious, but wouldn't you just set the timescale to 0.1 and just multiply the speed of everything related to that object to *10.0? Timescale would be global so it would affect that object unless you artificially just boost the object's timescale-related attributes. Unless you are requesting that each object has an override to the timescale?

-------------------------

codingmonkey | 2017-01-02 01:01:33 UTC | #3

>and just multiply the speed of everything related to that object to *10.0?

I think that you can do without it. ?nly settings(multiply) timescale of selected object w/o change speed of objects, besides objects consist from more complecs components and change (multiply speed) all of them: animation mesh, animation materials, amin shaders, rigid body speeds, time based logic...ect - this is hard way, you know.

> Unless you are requesting that each object has an override to the timescale?
if I understood you correctly. I just want it and that each object has changed it's own timescale for affecting to it's own and their children, and components.

-------------------------

