George | 2017-01-02 01:06:33 UTC | #1

Hello, 
I want to have my component update by event time and time step.

That is, I will manually specify the update time instead of using the real time.

Is there any way to achieve that.

Thanks,
George

-------------------------

cadaver | 2017-01-02 01:06:33 UTC | #2

You could use a custom event, to which the component subscribes. In this case don't use the LogicComponent::Update() virtual function at all, instead do the update inside your event handler function. You can send the custom event from some central "manager" object at some point during the frame processing. See the events documentation page for details. [urho3d.github.io/documentation/1.4/_events.html](http://urho3d.github.io/documentation/1.4/_events.html)

In case you want to update the whole scene (and as a result, all the LogicComponents inside it) using the same non-realtime timestep, you don't even need a custom event. Set scene automatic realtime updates disabled with Scene::SetUpdateEnabled(false), then call Scene::Update() with your own timestep every frame.

-------------------------

George | 2017-01-02 01:06:33 UTC | #3

I like the event based method. Because my target software is discrete event simulation.

1) The first way you describe as there is an event logic. Can I send update event to all my components of all the nodes? 
Is there an event list associate with this event handler? such that if I register lots of event will it sequentially execute based on the time I specified?
Do we have a small example on how to do this one. 

2) The second methods you describe looks great as well, Can I specify additional parameter in the scene::update() event? From the document I can only specify the delta time step.

Thanks mate,
George

-------------------------

