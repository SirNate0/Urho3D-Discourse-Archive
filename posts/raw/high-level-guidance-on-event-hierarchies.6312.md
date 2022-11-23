vmost | 2020-08-11 01:56:38 UTC | #1

Hi,

Today I am studying the overall structure of RunFrame(). Here is what I found, i.e. more or less everything the engine will or might do.
```
- RunFrame
	- Timer::BeginFrame		//sends out the E_BEGINFRAME event, signaling the beginning of the frame
	- E_BEGINFRAME
		- Workqueue::HandleBeginFrame()
		- Input::HandleBeginFrame()
		- FileSystem::HandleBeginFrame()
		- Network::Update()
		- ResourceCache::HandleBeginFrame()
		- UI::HandleBeginFrame()				//for resetting cursor each frame

		note: the timer sets the event data that is passed to all 'RunFrame' updates
			- frame number: which frame is beginning
			- time step: how long ago did the previous frame start

	- PlayAudio				//turns on audio if engine turned it off in the previous frame, or if we went from minimized->full mode
				
	- Update 				//sends out a series of update events that organize update workflow
		- E_UPDATE
			- Scene::Update()
			- Material::HandleAttributeAnimationUpdate() 	//sometimes, not clear what situations
		- E_POSTUPDATE
		- E_RENDERUPDATE
			- Audio::Update()
			- Octree::Update()				//when in headless mode, manually update Octree
			- Renderer::Update()
			- Network::PostUpdate()
			- UI::RenderUpdate()
		- E_POSTRENDERUPDATE

	- Render 				//render the application to screen
		- Graphics::BeginFrame()
		- Renderer -> Render()
		- UI -> Render()
		- Graphics::EndFrame()

	- ApplyFrameRateLimit 	//timing magic
		- normal: the engine has a 'FrameTimer' that times frames... at engine initialization the timer is started, and then at the end of the first frame it is reset; the recorded value is the 'time step' between frames; at the same point in each frame the timer gets reset, ensuring very minimal clock losses; the actual gap between resetting the timer and the next 'E_BEGINFRAME' event should be on the order of nanoseconds unless the E_ENDFRAME event is abused by the programmer
		- real frame rate exceeds max frame rate: the minimum gap between frames hasn't been reached, so a real-time delay is inserted
		- real frame rate is below min frame rate: the maximum gap between frames has been exceeded; since it isn't possible to speed up the program execution, the frame rate is artificially slowed down; in other words, the time step is lowered to the max gap between frames; for example, even though 5 seconds have passed in the world, only 4 seconds will be recorded as elapsing in the program's world; in effect, the program will enter slow motion

		note: by default the time step recorded is a moving average of real timesteps, presumably as a low-pass filter on frame rates to mitigate jitter; however, I suspect when frame rates increase rapidly then the in-game physics will slow down, and vice versa

	- Timer::EndFrame		//sends out the E_ENDFRAME event, signaling the end of the frame
		- E_ENDFRAME
			- Graphics::DebugRenderer()
			- Input::HandleEndFrame() 		// only for 'EMSCRIPTEN' builds
			- Log::HandleEndFrame()
```
From what I can tell, 'first to subscribe is first to respond on event send; sender-specific responses all go before generic responses (objects only respond once to an event, and sender-specific responses will take precedence over general responses if the object has multiple subscriptions to the same event with different senders [or no sender])' according to the use of `EventReceiverGroup`. This means in the main update cycle, if a scene was initialized before any application objects subscribed to `E_UPDATE`, the scene will respond to `E_UPDATE` first before those other subscribers. Of course, a scene can technically be initialized anywhere.

I suppose my question is about best practices around order sequences of responses. If order matters, is it best to use different events that are sent sequentially? Should I assume all responses to an event could be randomly sequenced? Is there ever a situation where it is reasonable to use subscription order to control response order?

I'd love to hear anyone's thoughts on how to fit the structure of an application into the engine's workflow.

-------------------------

Eugene | 2020-08-11 07:49:22 UTC | #2

[quote="vmost, post:1, topic:6312"]
If order matters, is it best to use different events that are sent sequentially?
[/quote]
Yes. You may need to add some intermediate events if existing are not enough.
I wish we had something like update graph for both scene and global subsystems, but we don't.
[quote="vmost, post:1, topic:6312"]
Should I assume all responses to an event could be randomly sequenced?
[/quote]
Yes. Order may or may not be preserved now, but it is not reliable behaviour.
[quote="vmost, post:1, topic:6312"]
Is there ever a situation where it is reasonable to use subscription order to control response order?
[/quote]
You better not.

-------------------------

vmost | 2020-08-11 12:19:20 UTC | #3

Thanks @Eugene. I was also wondering, it seems some engines implement a fixed-timestep internal loop within the frame loop for more streamlined physics. Is there a reason Urho3D did not implement that internal loop? I suppose it wouldn't be unreasonably hard to implement one locally if necessary.

-------------------------

Eugene | 2020-08-11 13:15:10 UTC | #4

Bullet physics implements fixed step loop internally and Urho reuses it via events.

-------------------------

vmost | 2020-08-15 01:41:27 UTC | #5

Maybe this is a dumb question... it seems like most or all event handlers are implemented like this:
```
void HandleEvent(StringHash eventType, VariantMap &eventData);
```
I'm wondering why is eventData not made `const`? If order-based event handling isn't safe, then there shouldn't be any situation where modifying `eventData` is safe or sensical. So, it would seem to want `const` always. Except maybe to pass information back to the sender... but even so that would be a rare exception for removing `const`, not a standard practice.

EDIT: Apparently `operator[]() const` for `HashMap` returns a pointer, while non-const returns a reference. Either way it is write access...

-------------------------

Eugene | 2020-08-15 11:59:08 UTC | #6

1) It is _impossible_ to implement safe `operator []` for constant dictionary in C++, if it returns value (=not pointer/optional/whatever). And value access via `[]` is convinient in most scenarios.
2) If you know there is only one event recepient, it's fine to return values via event data.
3) Even if you know there may be multiple event recepients, it's fine to return values via event data, as long as you know what you are doing.
4) And (1) or (2) is basically the only way you can possibly get feedback from event if you need it.

It pretty much forces events to accept mutable event data.

-------------------------

