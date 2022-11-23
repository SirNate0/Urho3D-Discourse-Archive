NemesisFS | 2017-01-02 00:58:08 UTC | #1

Hi,

I experiment a bit with the engine at the moment. I want to write a component for my game objects (Space Ships) which holds their parameters (i.e. HP, max-acceleration etc) and also allows to set commands that apply force before the physics is simulated.
I want to allow such objects to be controlled by input (keyboard), network, or by an AI, for guided missiles for example. How would you implement that scenario? Im not sure how to make it as robust as possible.

-------------------------

weitjong | 2017-01-02 00:58:08 UTC | #2

Have you looked at the NinjaSnowWar sample? It has rudimentary AI implementation to control the enemy characters. I have created a moon racer demo app largely based on NinjaSnowWar some times ago. The racer pods controller could be switched between player and AI seamlessly. So, I would say it worths a look if you have not studied that sample closely.

-------------------------

friesencr | 2017-01-02 00:58:09 UTC | #3

I copied ninjasnowwasr ai controller.  I found that i needed much more inputs/data into the ai so i changed the logic to have an input phase which writes some data to the node and then an acting phase which acts on the data that was provided by either human/ai input.

-------------------------

NemesisFS | 2017-01-02 00:58:09 UTC | #4

If I understand the way NinjaSnowWar does it correctly it has an AI Controller and every Ninja that is controlled by it has a reference to it. Id prefer a implementation where the object is completly agnostic to the AI and gets commands only via its public methods.
I dont think a central controller will work if the strategies need to safe data also I will propably have interchangable Strategies (for example a guided missile that recognizes that it cannot hit the target will change to a self-destruct strategy).

The two Phase approach friesencr mentioned seems to be the way I`d like to do it, yet I`m still undecided on how to implement it; Could a subsystem be what I`m looking for? It would listen to some pre-physics event, get input/AI decisions and apply them to the gameobjects.

-------------------------

JTippetts | 2017-01-02 00:58:09 UTC | #5

You shouldn't need a subsystem. You can just build your controllers as components, and subscribe them to listen for the PhysicsPreStep (E_PHYSICSPRESTEP) event, which occurs right before the physics update. They can then issue whatever orders they need to their owning object in a self-contained manner, without having an external system handling it all. I recently did a blog post on a third-person rpg camera system I implemented for some of my projects ( [gamedev.net/blog/33/entry-22 ... on-camera/](http://www.gamedev.net/blog/33/entry-2259326-demo-and-explanation-of-third-person-camera/) ) that includes a demo in Lua. The demo implements a very simple RPG-type level with a camera that has a number of options. The demo includes 2 player controllers: 1 that allows point-and-click, Diablo-style movement with pathfinding, and the other (commented out in the object instance section in levelgenerator.lua, but you can uncomment it and comment out the other) that implements WASD-style movement. They are implemented as ScriptObject components that do their work during Update. There is also a random-wander AI controller as well assigned to a handful of AI units. Each controller is a self-contained component that is instanced into a node to provide that node with the desired behavior.

In my opinion, you should try to implement everything within the game as components attached to nodes; subsystems should only be done if something needs to be visible to many different objects globally, rather than being local to the object as a player or AI controller is. My personal preference is to do [i]everything[/i] as components; and if something requires subsystem-type behavior, do it as a scene-level component similar to PhysicsWorld, Octree, NavigationMesh, etc...

-------------------------

NemesisFS | 2017-01-02 00:58:10 UTC | #6

I`ll think I will use that approach, thanks JTippetts.
Though I propably will use a controller with plugable strategies which it will then evaluate for the input.

edit:
what events should I listen to? the AI will need to be executed before the "space-ship-component" applies its forces. Is there an overview in which order the built-in events are thrown by the render-loop?

-------------------------

JTippetts | 2017-01-02 00:58:13 UTC | #7

The main loop event sequence can be found at: [url]http://urho3d.github.io/documentation/a00013.html[/url]

-------------------------

