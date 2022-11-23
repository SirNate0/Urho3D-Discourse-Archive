urnenfeld | 2020-12-20 21:49:36 UTC | #1

Hello,

Is it possible to send an event ([SendEvent](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_object.html#ac0088ab93a71b930fd8cbc06b0afddc7)), but the triggering actually happening after a specific delay?

My use case is attemping to trigger an action from a Handler, after a specific amount of time.

Is there any other more elegant method than subscribing E_UPDATE and keeping a [timer](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_timer.html) and only then perform the SendEvent() call? 

... This option, forces extra status handling & logic between the triggering handler, and the update handler.

Thanks!

-------------------------

vmost | 2020-12-20 21:48:56 UTC | #2

If you want a delay, you'll need a timer of some kind... there is nothing built-in for this. If you don't want the timer to block execution, then maybe push your event/handler into a queue and check with every E_UPDATE call if enough time has passed (E_UPDATE has P_TIMESTEP parameter, which returns duration of previous frame as a float in milliseconds).

Unless you want to get into the weeds of controlling FPS, exceeding that level of granularity is pointless.

-------------------------

Eugene | 2020-12-20 21:09:07 UTC | #3

Builtin events don't and can't really support it. `SendEvent` is synchronous, will all benefits and disadvantages of this approach. You have to make your own event system if you want them to be processed in MT or delayed.

-------------------------

S.L.C | 2020-12-20 21:48:56 UTC | #4

There's nothing builtin at the moment iirc. But it shouldn't be too hard to implement a component/sub-system which handle these things for you.

You basically inherit from `Object` type to create your subsystem, which you then create an instance of. Which you then pass to `Context::RegisterSubsystem(...)` to have it as a subsystem in your application. Look at `Source\Urho3D\Core\Timer.h/cpp` for a simple sub-system used by the engine.

You then listen to `E_BEGINFRAME` or `E_ENDFRAME` (*or both*) to process pending events.

Storing events for calling later should be easy. All you need to store is the hash of the event you want to emit, a pointer to the sender (*because the event must appear to come from the sender not your sub-system*), a `VariantMap` with the event parameters and the conditions required to send that event. All of which should be trivial to store in a `Vector`.

Be aware of the sender lifetime tho! I hope I don't have to warn you about the consequences of accessing freed memory. How you tackle this issue is up to you.

On each frame event your custom sub-system receives, you process the array of pending event conditions. And if the condition is met, you invoke the `SendEvent(...)` method on the sender with the hash and stored `VariantMap`.

This would the simplest approach to this if all you need is a timer.

If however the number of pending events is huge and processing starts to affect your frame-time. You may have to look a different approaches. Like processing conditions in a separate thread. But that's outside the scope of this post.

-------------------------

urnenfeld | 2020-12-22 01:03:58 UTC | #5

[quote="Eugene, post:3, topic:6619"]
Builtin events don’t and can’t really support it. `SendEvent` is synchronous, will all benefits and disadvantages of this approach.
[/quote]

From an external point of view, someone would think that the natural way would be inside the Object class... however if I look deeply inside... nah...

In a more generic & phylosofical scope, Does the feature exposed, have any sense?

Anyway, here there is an implementation(closer to @vmost proposal).  Is required to instantiate this class in your Object, and ensure you call the *ProceesTimedEvents()* method in the E_UPDATE handler.

https://gist.github.com/urnenfeld/8dd867fa2f2780446d90c8736581377e

-------------------------

vmost | 2020-12-22 02:32:47 UTC | #6

The concept looks correct to me. You may want to use smart pointers instead of raw pointers.

- `Object* sender` -> `Urho3D::WeakPtr<Object> sender`
note: Urho3D `Object`s are intrusively reference counted, so creating a weak pointer off a normal object should work as expected (afaik).
- `timedEvent->sender->SendEvent(...)` ->
```
if (timedEvent->sender)
    timedEvent->sender->SendEvent(...);
```
- `Vector<tTimedEvent*>` -> `Urho3D::Vector<Urho3D::UniquePtr<tTimedEvent>>`
- `new tTimedEvent {...}` -> `Urho3D::MakeUnique<tTimedEvent>(...)`

-------------------------

Eugene | 2020-12-22 11:26:24 UTC | #7

[quote="urnenfeld, post:5, topic:6619"]
From an external point of view, someone would think that the natural way would be inside the Object class… however if I look deeply inside… nah…
[/quote]
It’s hard to do it inside Object. E.g. what should happen if sender is destroyed? Some events may want to fire anyway, some events should be cancelled. So, event function is required to check if sender is still alive. Moreover, raw pointers in event parameters may expire as well. Also, someone has to take care of allocations. Current events kind of optimize VariantMap allocation which is not compatible with async events.

It’s all solvable, at the cost of API clarity and a lot of code written. It’s simpler to just make external system that fits your needs.

-------------------------

George1 | 2020-12-22 11:40:15 UTC | #8

If this is not discrete event time,  then why not creating a component?  Then you can have unlimited schedule events attach to what other object/entity that you like.

-------------------------

urnenfeld | 2020-12-23 01:48:10 UTC | #9

[quote="vmost, post:6, topic:6619"]
* `Vector<tTimedEvent*>` -> `Urho3D::Vector<Urho3D::UniquePtr<tTimedEvent>>`
* `new tTimedEvent {...}` -> `Urho3D::MakeUnique<tTimedEvent>(...)`
[/quote]

Thanks! that solves some TODOs but:

Isn't this creating actually problems in lines 16, 25 & 35? The pointer gets copied in those lines...

[quote="George1, post:8, topic:6619"]
If this is not discrete event time
[/quote]

I don't understand what you mean by *discrete event time*

[quote="George1, post:8, topic:6619"]
then why not creating a component?
[/quote]

Could be, it would feel more *Urho3D like*...
But would the implementation then only available for **Nodes** or other sibling **Components**? and not to other non-Node kind of **Objects**?

[quote="George1, post:8, topic:6619"]
Then you can have unlimited schedule events attach to what other object/entity that you like.
[/quote]

I used multiple events for testing the implementation. Then... :/ I don't understand the limitation.

-------------------------

vmost | 2020-12-23 03:03:20 UTC | #10

lines 16 and 25: use `timedEvents_.EmplaceBack(MakeUnique<tTimedEvent>(...));` 
line 35: can use `auto` or `UniquePtr<tTimedEvent>`

-------------------------

urnenfeld | 2020-12-23 13:43:05 UTC | #11

Sorry this has become a c++ best practices, but I value your opinion here.
[quote="vmost, post:10, topic:6619"]
lines 16 and 25: use `timedEvents_.EmplaceBack(MakeUnique<tTimedEvent>(...));`
[/quote]
I was stubborn and wanted to keep creating the entry via an initialazer list, and was forced to create a *[MakeUniqueFromList](https://gist.github.com/urnenfeld/8dd867fa2f2780446d90c8736581377e#file-eventscheduler-hpp-L3)*. I have updated the gist, the 3 options shown (EmplaceBack, Push, moving) would be working.

[quote="vmost, post:10, topic:6619"]
line 35: can use `auto` or `UniquePtr<tTimedEvent>`
[/quote]

I am not sure I got you here, creating an UniquePtr([now #51](https://gist.github.com/urnenfeld/8dd867fa2f2780446d90c8736581377e#file-eventscheduler-hpp-L51)) would copy the pointer from the iterator... Check the gist, solved it with a reference(feels cheaty) ... or not creating the intermediate pointer(:chicken:)...

-------------------------

WangKai | 2020-12-25 02:23:13 UTC | #13

My simple solution -
https://gist.github.com/SuperWangKai/d480c48f6056d0ba69a019ae37b665d6

Using lambda as the callback -
```c++
auto timer = node->CreateComponent<CallbackTimer>();
timer->SetCallback([=]() {
    // Do delayed things here.
    node->Remove(); // e.g. to remove the node.
    }, 1.0f, false);
```

The minor issue I see here is that the base class `LogicComponent` is a little large in size, if we use `Urho3D::Object` as the parent class, we have to manage the timer object manually without attaching to the Node.

-------------------------

urnenfeld | 2020-12-25 11:29:32 UTC | #14

Yep, an option, although my intention was to get benefit of the *Events* and its *VariantMaps*.

-------------------------

Modanung | 2020-12-27 11:20:01 UTC | #15

The AS API _does_ have a `DelayedExecute`, btw.

-------------------------

