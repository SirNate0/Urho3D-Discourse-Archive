slapin | 2017-07-05 09:58:11 UTC | #1

Hi, all!

Passed through simple things like basic animation controllers and basic game mechanics,
I'm still struggling with some more advanced game concepts. I have implemented
behavior tree, and many things I need, but I have trouble with visual representation of some things.
But not with animation/graphics per se, as that is just matter of skill, but with understanding of structure.

I need the following game mechanics which is somewhat close to concept of "cut scene" but really not,
as these should be integrated into game visually. These are transitional states from/to various
aspects of game. I was taking some break to have things settled, but really I still have no basic idea how to do this nicely so it integrates with game.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ef2eab2a0f374a1a19aa2ba7fcf0120de1e9f342.png" width="500" height="500">

The problem is that I quickly get **overwhelmed by amount of options and states required to**
**support the concept**. I need to disable character controller, get to "NPC mode" with simple BT,
select which door to walk to (how?), walk to the door, play realistic animation of openning the door (!)
enter the openning (disable physics, do all preparations), then (if car) sit properly to appropriate free seat(need check) then close door.
This whole thing is extremely stateful this way which is very incompatible with current AI concepts (BTs and Utility AI). Also it is very hard to sync door openning with character animation due to lack of tools. I really want to write tools appropriate for this task, but I still could not find definition of **appropriate**. Any ideas?
I'd like to see into some **architecture** of such complex **behaviors + animation logic**.

Currently I have characters simply **teleported** into cars and buildings. That is very not cool...

Also I wonder if integration of animation triggers with BTs might somehow make the problem easier to comprehend. My head is almost exploding with this. I tried to PoC this in UE4 and it was about 3 minutes to have working scene. I need to find proper workflow with Urho. Please!

-------------------------

johnnycable | 2017-07-05 22:40:44 UTC | #2

you can define routes with recast and detour... your behaviours are probably too high level if the character doesn't know what to do... you can put interest points along the routes to let the character choose what to do...
blending atomic animations (i.e. look at the key - take the key on table - open the door) must be programmed, but you could use a state machines on those common behaviours...
probably UE4 has some sort of sophisticated blending state machine, but I bet **just on pre-made scenarios**... those things must be programmed by your department AI specialists... :upside_down_face:
As a weapon of last resort, if you are desperate you could use an entity component system, for assigning and switching funcionalities and/or behaviours... but that probably is only going to get in the way more...

-------------------------

slapin | 2017-07-05 23:10:02 UTC | #3

Thanks for your answer.

What do you mean by  **entity component system**? Any examples or tutorials on that?

I wonder how to form complex behavior so that they do not become modal, i.e. openning the door is good,
but if there's shooting nearby, finding cover might be better option...

I think more of something like priorities - like "I need to get out of here" = find vehicle, (get into vehicle|hijack vehicle (if not friendly)), drive out of camera sight, (if not important to player - disintegrate, otherwise
get to available NPCs table keeping macro data).
The problem is splitting this into behaviors atomic enough but still manageable and not getting int too low-level details...
The state machinery can be done with BT, but I try to be as stateless as possible (keep state number to minimum) as that leads to the system which is hard to comprehend.
I really can't make system to find proper level for behaviors. Making atomic motions and animations into behaviors makes system overcomplicated and really hard to design and debug, as when you make animations you can't visualize the final result, so you have to do tweaking-testing loop which might take ages to complete. For example, if I need to animate 2 characters shaking hands I need to see both of them to do proper animation, If I animate just one I don't see the result so I have to guess too many things.
I did some tools for quick animation matching testing/offsetting, but that is still extremely slow process.

Also coding a cutscene is also very tedious process, as I do full cutscene in Blender, then I export
scene via collada with animation, but this animation consists of both character skeletal animations and
value animations for motion, with everything needed to be set up manually. I wonder how people manage,
i.e. how they set up asset workflow for such things...

-------------------------

johnnycable | 2017-07-06 12:41:15 UTC | #4

An ECS is used to manage behaviuors / states and so on dynamically while assigning them to characters and characters to level. While this is not a rule of thumb, it allows you to "prefab" your components once and reassign a behaviour or a group of them to many characters.
Good for mass management, not so good if you have few guys...
Here's a classical example by Ray Wenderlich for Ios
https://www.raywenderlich.com/155780/gameplaykit-tutorial-entity-component-system-agents-goals-behaviors-2
I personally use EntityX. It is well laid, but they say it's slow. Others exists, you can google for them...

https://github.com/alecthomas/entityx

-------------------------

slapin | 2017-07-07 02:47:06 UTC | #5

Thanks for details.

But by looking at it I see that Urho already have perfect entity-component system.
My BT logic is also a component. But I don't understand how this is mixed to my original goal...

-------------------------

