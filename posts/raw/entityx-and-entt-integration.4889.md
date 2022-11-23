ViteFalcon | 2019-02-03 07:56:44 UTC | #1

Just for the heck of learning about ECS and how it works, I have been trying to integrate [EntityX](https://github.com/alecthomas/entityx) with Urho3D.

I'm presenting [my work](https://github.com/ViteFalcon/ecstest) here as a way to learn, improve, and hopefully help others with the work.

The Github repo that I'm sharing is supposed to duplicate (and extend) the [First Project](https://github.com/urho3d/Urho3D/wiki/First-Project).

With the ECS integration, creating a box looks like so:

```cpp
auto box = CreateRenderableEntity("Box");
box.assign<StaticModel>("Models/Box.mdl", "Materials/Stone.xml");
box.assign<Position>(0, 2, 15);
box.assign<Direction>(); // So that we can apply angular velocity
box.assign<Scale>(3, 3, 3);
box.assign<AngularVelocity>(10, 20, 0); // Rotates the box
```

The full Demo scene setup code can be seen [here](https://github.com/ViteFalcon/ecstest/blob/master/src/state/DemoState.cpp).

I'm not fully happy with the structure of how things are glued, and I'm looking into how to refactor the code so that it's cleaner. Let me know if you have any suggestions around that.

Constructive criticism is always welcome! Let me know what you think.

-------------------------

Leith | 2019-02-01 23:11:03 UTC | #2

Nice to see someone else has an interest in ECS :)
Urho3D already has an 'entity component system', if we accept that a new node is an empty entity.
But neither urho nor entityx are DOD-ECS. Data oriented design ECS stores components of the same type in contiguous arrays in memory, in an effort to avoid CPU cache misses. They use Placement-New in an effort to avoid allocating small blocks of memory at runtime. DOD components have no code, they are Plain Old Data structs, the code for them lives in a Subsystem, and there is a Subsystem for every kind of Component, so quite different to what we see here in Urho, or Unity for that matter.

-------------------------

ViteFalcon | 2019-02-01 23:22:25 UTC | #3

From what I can tell (and I could be wrong), EntityX is built to be cache-coherent because the components are created from a contiguous [memory pool](https://github.com/alecthomas/entityx/blob/master/entityx/Entity.cc#L49), which is used to [do placement new allocation of components when the component gets assigned to the entity](https://github.com/alecthomas/entityx/blob/master/entityx/Entity.h#L633-L657).

-------------------------

Leith | 2019-02-01 23:43:46 UTC | #4

That may be so - it's been a while since I looked closely at entityx sourcecode.
Still, entityx has a concept of components being attached to entities, while a pure dod-ecs does not need entities to exist at all - an entity can be simply an ID, not an object, and so the components that are associated with an entity are tagged with the same ID, no pointers involved. The main difference between classic ecs and dod-ecs is the way we update. In a classic ecs, we evaluate the scene hierarchy, updating components in the order we find them, while a dod-ecs updates the Subsystems in the order they are registered, and each Subsystem updates its Components as a flat array, irrespective of which entity owns them.

-------------------------

ViteFalcon | 2019-02-02 00:29:22 UTC | #5

> Still, entityx has a concept of components being attached to entities, while a pure dod-ecs does not need entities to exist at all - an entity can be simply an ID, not an object, and so the components that are associated with an entity are tagged with the same ID, no pointers inolved.

I belive, EntityX's [`Entity`](https://github.com/alecthomas/entityx/blob/master/entityx/Entity.h#L59-L79) class is just a wrapper around a [`uint64_t` id](https://github.com/alecthomas/entityx/blob/master/entityx/Entity.h#L61-L79) and [has a pointer to the manager](https://github.com/alecthomas/entityx/blob/master/entityx/Entity.h#L59-L79) not the components. I believe, that the `Entity` class is simply a helper non-reference class.

To illustrate an example of an interaction; to find entities that has a specific set of components you would [query the manager](https://github.com/ViteFalcon/ecstest/blob/master/src/systems/MovementSystem.cpp#L34-L40).

Any operation of adding components to an entity happens [through the EntityManager](https://github.com/alecthomas/entityx/blob/master/entityx/Entity.h#L946-L950).

But in effect, that class is just a wrapper of how you would otherwise do directly with `EntityManager` to associate components to an entity identified by a `uint64_t` ID.

-------------------------

Leith | 2019-02-02 14:01:01 UTC | #6

Sounds like there's been some changes in the design and implementation that bring entityx much closer to Data Oriented Design :) Nice! I'm tempted to post my firestorm engine docs, which describe a close to the metal approach to DOD-ECS that I implemented, it runs blazingly fast, and deals with multithreading and rendering in the days when we still had to cope with opengl context issues, which is the current state of this engine, to the best of my knowledge

-------------------------

johnnycable | 2019-02-02 14:05:25 UTC | #7

What about this [entt](https://github.com/skypjack/entt)?
Looks like an improvement over EntityX...

EDIT: whoa, it changed a lot since last time I used it...

-------------------------

ViteFalcon | 2019-02-02 17:36:51 UTC | #8

Let me give EnTT a spin. I will duplicate this project for that, probably different branch.

-------------------------

Alan | 2019-02-02 18:22:09 UTC | #9

This is great! :+1: for EnTT!
I disagree that Urho has an ECS, it has "Components", an ECS implies in components being data without logic, otherwise the "S" doesn't make sense, but that's just semantics.
In any case this sounds awesome I'm going to take a look at the code. EnTT is very high perf and very actively developed... This could really be the start of the modernization Urho needs so badly at this point!

-------------------------

Alan | 2019-02-02 18:41:02 UTC | #10

After taking a look at the code, I just realized that you're not actually replacing the Nodes/Components/Internal Logic for their ECS counterparts but just adding ECS on top of the existing model (wrapping the Urho objects in EntityX components). That's not what I was expecting tbh, and I see little point in doing that.
Do you plan to actually do away with the Urho Nodes/Components in favor of a real ECS for the code logic? That will certainly require a major revamp of Urho's code.

-------------------------

ViteFalcon | 2019-02-02 21:29:48 UTC | #11

Like I said, it was purely for learning how ECS works. I want to first learn different aspects of ECS before I jump into anything more involved like revamping Urho3D to be powered by ECS.

Let me preface by saying that I'm not going to commit to anything that I'm going say, but I am definitely interested to see if I can change Urho3D to be using pure ECS. Once I get a better grasp of how ECS works, I will probably try making small changes to Urho3D to prove the concept.

-------------------------

QBkGames | 2019-02-03 05:29:27 UTC | #12

I had a brief look at the "proper" ECS like EntityX and entt as well, but my feeling is that it's only very useful if you have a game with lots of objects all of the same type and you end up with a few components and a few systems that update a lot of entities.

A screen shot of my test project (1000 ships: 100 X-wings vs 900 Tie fighters, all with basic AI and shooting in real time, no physics though, only basic shape collisions):
![Play%203A|690x408](upload://9DFDm5vOR4USI90bU38y1xoToTZ.jpeg) 

However when you do a game (adventure, survival, etc) where you have a lot of different type of objects, with small numbers of each in the level, then you end up with a lot of components, a big stack of systems, each of which only updates one or a few entities. So I think for this kind of games the current Urho/Unity ECS implementation is easier to work with.
Ideal the engine should have both and you can used whichever you want based on the type of game you are making.

-------------------------

ViteFalcon | 2019-02-03 07:56:18 UTC | #13

So, I got the demo modified and working for [EnTT](https://github.com/skypjack/entt). You can check it out here: [ECS Test / entt branch](https://github.com/ViteFalcon/ecstest/tree/entt).

The usage looks very similar but a bit involved:

```cpp
auto box = CreateRenderableEntity("Box");
mRegistry.assign<Position>(box, x, -3, z);
mRegistry.assign<Scale>(box, 2, 2, 2);
mRegistry.assign<StaticModel>(box, "Models/Box.mdl", "Materials/Stone.xml");
```
Iterating the entities with specific components looks like this:

```cpp
auto rotatingEntities = registry.view<Direction, AngularVelocity>();
for (auto entity : rotatingEntities) {
  auto &velocity = registry.get<AngularVelocity>(entity).value;
  Urho3D::Quaternion deltaRotation = Urho3D::Quaternion(
      velocity.x_ * dt, velocity.y_ * dt, velocity.z_ * dt);
  registry.get<Direction>(entity).Rotate(deltaRotation);
}
```

-------------------------

johnnycable | 2019-02-03 11:42:36 UTC | #14

I agree about having such a system is for games with really lots of objects. Basicly, you may want to put it, for instance, at the base of a server side system which manages a mmorpg or something like that... worlds, lots of rooms, lots of players...
Add to it that its inner working is not easily grasped by novices... you have to have a bit of a data-thinking mind; it easier to think in term of "players, non-players..."

BTW: I still have the fork I did in the beginning of it, when it was a simple plain ECS system, without the full bells and whistles as it is now... [here](https://github.com/kabukunz/entt)

-------------------------

Sinoid | 2019-02-04 05:32:39 UTC | #15

If you have something that fits the academic ECS pattern better than others there's nothing stopping you from including an appropriate *system* component to do that workload ...

... that's how the DetourCrowd and physics stuff works.

Urho runs a bit of middle ground.

-------------------------

Leith | 2019-02-04 05:39:28 UTC | #16

I recently asked for a clean definition of what a subsystem is, but in urho, subsystems dont own stuff, which shocked me, they are just there for eventing, and not specific - this I found to be quite distant to dod-ecs and took me some time to absorb
The best answer I got, was that subsystems are just singleton objects that are registered with the engine, and the only point of doing so is that we can access them, rather than making singletons be static and so shared.

-------------------------

Sinoid | 2019-02-04 05:38:28 UTC | #17

ResourceCache owns stuff, but in general - subsystems don't.

Scene *system-style* components do.

-------------------------

Leith | 2019-02-04 05:42:37 UTC | #18

I asked about resourcecache recently too, and got no answer about managing resource memory footprints, but so far its not a big issue, just a looming issue

-------------------------

Sinoid | 2019-02-04 05:45:22 UTC | #19

PM me the links to those posts if you could, you've got a ton of posts in a narrow timespan so tracking them down could be hard. Might have insight depending on the questions.

-------------------------

Leith | 2019-02-04 05:55:21 UTC | #20

yeah I am new here, but I am an old hand at game dev, and have a lot to learn and a lot to say, I agree I am posting a lot, but it's during my learn curve, so please give me some slack while i find my feet on this ship. My teachers worked on games, and I spent years to learn my craft. I just wasted a year using Unity, and it made me worse at my craft, so I needed to find an engine that did not make me a worse coder. I am here now, and in this environment, I can give my fixes, not sell them.

-------------------------

