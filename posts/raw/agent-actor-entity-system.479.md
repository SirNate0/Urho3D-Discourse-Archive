scorvi | 2017-01-02 01:00:45 UTC | #1

hey 

i am currently working on an EntitySystem (or Agent/ActorSystem ...) and detourcrowd navigation is one of its components. 

my plan is to create something like [url=http://rivaltheory.com/rain/features/]Rival{Theory} Rain AI[/url], [url=http://nodecanvas.com/]nodecanvas[/url], [url=http://www.seas.upenn.edu/~mubbasir/projects-adapt.html]ADAPT[/url] or horde3ds  [url=http://www.hcm-lab.de/projects/GameEngine/doku.php]GameEngine[/url] has also an [url=https://hcm-lab.de/public/Horde3D/trunk/Tools/GameEngine/src/]GameAgentComponent[/url]

i created some components already in other projects and now i have to combine them ^^ in a good way so that it is easy to use ... 

my design concept is somthing like this:
EntityManager: 
will be created at the root scene node and manages the entities (updates the different entityComonents individual )

EntityComponent:
on initialization it creates the basic components: Motor, Brain, Animator, Navigator, Physics(collision handling) and Perception(area awareness).
you can add scripts which can alter the entity. virtual function are : Pre() Sense() Think() Act() React() Post()  they just call the entity components  and then the scripts or custom components for this entity.

currently i am working on the Motor and Navigator component. I have simple steering implemented and now the detourCrowd Navigator will be added. 
after that i will start with the Brain component, because i have already an FSM for it. 

So my questions are:
(1) Is there a need to implement it for the urho3d engine core, like detourcrowd ? I will try to create it as generic as posible but for that some help would be nice ^^ 
(2) To edit the Brain components, i want to add somthing like a node canvas (for FSM and behaviour Trees design ). But dont know how to start !? Has someone created something like that ? It should be generic as well, so you can use it not only for the ai design but also to create shaders, procedural content ... 

(3) i would really like 2 more subforums. One for Tutorials and one for currently WIP core engine features, so we all can see who is working on what and how he/she is doing it and to see the thought process of choosing the class design for a component ...

-------------------------

cadaver | 2017-01-02 01:00:45 UTC | #2

There should not be a need to touch Urho core for that. There are already manager-like components, like PhysicsWorld, and you can define more even outside the core, so I would think your EntityManager would be similar.

Note that in Urho terminology we don't have entities at all, just nodes and components. Usually the root node of a particular object (like a soldier or spaceship) would be considered to represent the whole "entity." I recommend making sure that you don't add management overhead that is not strictly necessary.

-------------------------

thebluefish | 2017-01-02 01:00:45 UTC | #3

Urho3D's Scene is already structured like a classic Entity-Component system, just replace "Entity" with "Node" and you've practically got the same thing.

Now from what I have seen, there are two main approaches to Entity-Component systems: Data-Drive and Logic-Driven.

- Data-Driven: Entities hold components, components hold data. External logic controllers work on individual components or sets of components (ie, a logic system that would work only on entities that have HealthComponent, PositionComponent, and PlayerComponent). A classic example of this would be the Artemis Entity-Component system (Which I have used for several Android apps).

- Logic-Drive: Components hold their own logic. They can communicate with other components that may or may not be there. Components hold their own data, but generally make it available to other components for use. I've used several such systems back when I worked with Ogre3D, but I don't remember any significant players in this area. Urho3D is generally geared towards this type of system.

Now the main thing to note is that components can have logic, but you aren't forced to do so. You can have a Component on the Scene root managing your logic, or you can have a Subsystem to manage your logic. What works best depends on what you're trying to accomplish.

For example, I've found it best for my card game to include Scene-level components to manage the scene-wide logic. However if I wanted to have a PlayerComponent to handle controlling a Player object, I would probably put all of the controller logic within the component and attach it directly to the player's Node.

For what you're trying to accomplish, do so by creating different components. Looking at how physics is handled is probably the best way to model your system off of. After-all, there are multiple components necessary to defining a Physics object, so you can see how those components deal with not having the other required components on a node. PhysicsWorld shows you how to manage all of these objects from the scene's root level. I would imagine your implementation would follow rather closely to how existing systems are handled.

-------------------------

