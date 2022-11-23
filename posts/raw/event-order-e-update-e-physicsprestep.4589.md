extobias | 2018-10-11 17:36:09 UTC | #1

Hi there,
Each event E_UPDATE is triggered before the update of the scene, right ?, which causes the update of the physical component by firing E_PHYSICSPRE / POSTSTEP.

However it seems that physical events are triggered before. In the example of the vehicle, I put fprintf to see the order and I got the following

raycastvehicledemo.beginframe
vehicle.fixedupdate
raycastvehicledemo.physicsprestep
raycastvehicledemo.update
raycastvehicledemo.endframe

I also put in the example initialization
PhysicsWorld * pw = scene _-> CreateComponent <PhysicsWorld> ();
pw-> SetFps (30.0f);
pw-> SetInterpolation (false);
engine _-> SetMaxFps (30.0f)

I'm probably missing something, some clue?

-------------------------

Sinoid | 2018-10-11 18:43:34 UTC | #2

Physics is updated via the `E_SCENESUBSYSTEMUPDATE` message that is sent by the scene from it's `E_UPDATE` handler. When physics needs to tick it'll send `E_PHYSICSPRESTEP` which does double-duty as the `fixed update` message.

So depending on your event subscription sequence what you're seeing there makes sense. That's handled through Bullet's internal-tick callback. It sounds like cludge but it does mean that whenever you have a fixed-update fire that you'll also have an actual physics-sim frame and not an interpolation - which is pretty important to any logic you have, it's a win and a subtle nicety.

The sequence of events can be seen in `Scene::Update`.

-------------------------

extobias | 2018-10-11 19:39:07 UTC | #3

So this comment in the sample
// Subscribe to Update event for setting the vehicle controls before physics simulation
means "before next physics simulation", which could be in the next frame?

-------------------------

Sinoid | 2018-10-11 19:52:23 UTC | #4

Can you tell me which sample so I don't go off explaining the wrong thing?

> means “before next physics simulation”, which could be in the next frame?

Assuming that's a script/logic-component/etc then sort of but no, that will be right before physics and fixed-update for the frame currently in flight, not the next-frame - really depends on how you mean *next*.

Although in Scripts and LogicComponent it's referred to as `update` it's actually the `E_SCENEUPDATE` event they use for that, which is also sent by the Scene from `Scene::Update`.

`Update` should always be sent before `fixed-update` which should always be sent before physics does anything.

-------------------------

extobias | 2018-10-11 20:01:53 UTC | #5

[quote="Sinoid, post:4, topic:4589"]
`Update` should always be sent before `fixed-update` which should always be sent before physics does anything.
[/quote]

That's what I thought when I asked. The example is 46_RaycastVehicle
This is how I subscribe to events

raycastvehicledemo.beginframe        E_BEGINFRAME
vehicle.fixedupdate                            LogicComponent FixedUpdate (E_PHYSICSPRESTEP)
raycastvehicledemo.physicsprestep  E_PHYSICSPRESTEP
raycastvehicledemo.update               E_UPDATE
raycastvehicledemo.endframe           E_ENDFRAME

I thought the flow should have been

raycastvehicledemo.beginframe         E_BEGINFRAME
raycastvehicledemo.update                E_UPDATE
vehicle.fixedupdate                             LogicComponent FixedUpdate (E_PHYSICSPRESTEP)
raycastvehicledemo.physicsprestep   E_PHYSICSPRESTEP
raycastvehicledemo.endframe            E_ENDFRAME

-------------------------

Sinoid | 2018-10-11 21:39:40 UTC | #6

Yeah, that's my bad.

`E_UPDATE` is a grab-bag event and will almost always come after physics-update (it depends on subscription/scene-creation sequence), that sample probably shouldn't be subscribing to it. 

`E_SCENEUPDATE` is the one that is guaranteed to occur before physics. `E_UPDATE` could happen in any order.

Edit: there's probably a ton of code that is subscribing to that but really shouldn't be, even in the core-engine. IIRC the scene-events didn't exist at one point in the past.

-------------------------

extobias | 2018-10-11 21:41:32 UTC | #7

Thanks for helping me

-------------------------

