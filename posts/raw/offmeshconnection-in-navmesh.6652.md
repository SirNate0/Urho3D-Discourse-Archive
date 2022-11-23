CE184 | 2021-01-05 01:49:26 UTC | #1

The off-mesh connection usage in the crowd navigation example is quite primitive. The agent goes to one end of the connection and instantly appears on the other end.
I subscribed the ```E_CROWD_AGENT_STATE_CHANGED``` and found it never sends any event related to off-mesh link. Then I found ```CA_STATE_OFFMESH``` is just a place-holder in ```CrowdAgentState``` and never used anywhere in the code. So I suppose it's not supported yet in Urho3D?
**Anyone has done something similar in real project how to get information about agent reaching start/end side of the connection and trigger related animation, etc?**

My ultimate goal is that the character can:
- climb up/down a vertical ladder;
- jump up/down within given height diff;
- jump horizontally between a gap.

It should be very similar to this [video](https://www.reddit.com/r/Unity3D/comments/5mg3lk/first_test_of_offmesh_links_with_custom_animations/).

There it looks easier since we can disable the Auto Traverse Offmesh Links in Unity, and it should be firing enough events to detailed agent state information too.

**How should I do it in the framework of Urho3D? Does the Raycast&Detour lib itself support these and just need to implement them into Urho3d?**

-------------
**Another question** is about the shape of OffMeshConnection triggering area. From current implementation, it looks like the end of each connection is only a circle given a radius. What I would like to have, is to have a narrow rectangle as the triggering area. For example, the whole edge of the wall, can be the start of the connection, and the ground under the wall can be the end of the connection. So the agent can "jump" off the wall **at ANY place** near the wall edge, instead of manually set different points everywhere.
**Is this even possible with the Raycast&Detour lib too?**

-------------------------

JSandusky | 2021-01-05 03:33:56 UTC | #2

The path corridor in the `dtCrowdAgent` contains polyrefs you can use to get the `dtPoly` and then check if the first poly in the corridor is an offmesh-connection with `getType()` (they're just degenerate polys as far as Detour is concerned). You'll have to keep the 0th polys' type buffer for old vs new checks to identify the change.

Identifying specific kinds of offmesh connections is tricky but doable. I wanted to expand the userID to 64bits and just store a pointer, arguably the navmesh could index all offmesh connections with unique ids ... which goes to hell when you have tiles and runtime updates. So it never happened. Probably updating the dtOffmesh's userID to a uint64_t would go fine.

You can't assume that DetourCrowd is ready to go out of the box and have to be prepared to break out the elbow grease. Crowds also raise so many events that they penalize scripting making C++ use mandatory if you're going to use very large ones, as well as possibly refactoring somewhat to jobify it (fairly easy but adds errors to agent actions). I had to compromise somewhere during that part (@scorvi and @JTippetts are the other large scale contributors on navigation, lots of handoffs were involved) and opted towards flexibility in the general case and not optimal for more than ~100 agents (150 agents in Angelscript on an Ivy-Bridge mobile chip [SurfacePro1] was my test target).

-------------------------

CE184 | 2021-01-06 01:22:33 UTC | #3

Thanks for the input!

I know it's not an easy task to support all my requirements, just wondering if it's doable in the framework of Racast&Detour library. If so, I can dig deeper later since it's a long term plan in my head. I checked a little bit about Unity and Unreal but could not find what lib they are using, do they have their own implementation other than Recast&Detour?

As you also mentioned the num of agents ~100 for general use. I was wondering what kind of improvement I can do if I want to support several hundreds agents? I was aiming for ~1000 agents on mainstream PC hardware but I am not sure if it's realistic in current framework. I do see lots of games can do that though, for example, Mount&Blade now can support 1024 + 1024 battle size on main stream PC. That also includes a lot of AI and animation computation there. My game would be much simpler so I assume it's doable though.
One thing in my mind for such a large system is that, I could use flocking behavior to reduce the computation. For example, within those ~1000 agents, only ~100 do crowd nav computation, and the rest would simply follow/copy their path. I am not sure if the flocking mechanism is included in Reycast&Detour lib too.

Anyway, given all my requirements. I only have very limited knowledge on navigation algorithm now. Do you have any links or papers related to how the algorithm is implemented in Raycast&Detour? So I start to learn something.

-------------------------

JTippetts1 | 2021-01-06 05:02:10 UTC | #4

The current implementation of navigation and crowds definitely could use some work. In my own stuff, my tendency is to bypass the engine wrappings and interact with detour and crowd directly. If you want to learn more about the workings, you could check out the old (defunct) blog of R/D's creator at http://digestingduck.blogspot.com/?m=1 for some info. Its pretty old stuff, but it should help a little.

-------------------------

QBkGames | 2021-01-06 23:54:21 UTC | #5

1000s of units are not realistic with general purpose engines like Urho (and most other). The best you can hope for is 100-200.

Games that have units in the 1000s most likely use custom inhouse engines optimized for large number of units, designed around the Data-Oriented, Entity-Component-System, which use struct-of-array rather than array-of-struct design patterns that make them very CPU cache friendly (and thus very fast).

There is an article on Godot design philosophy (you can search for) which clearly states that Godot (which represents a general purpose engine, just like Urho) is designed to make a good compromise between performance and ease of use. For most game types where cutting edge performance is not that critical, ease of use is preferred (also ease of maintenance, etc).

So, if you want 1000 of agents you have to roll your own engine, and good luck with that :P (although not impossible, it does take a long time, believe me I've tried (and still haven't finished): https://www.youtube.com/watch?v=lcy-12kMQJE&t=45s  ).

-------------------------

CE184 | 2021-01-07 03:45:05 UTC | #6

Very interesting video! Thanks for sharing!

Several followup questions:
- What is the most computational expensive part for your game when you have 1000 spaceships?
- From the video, I guess there is no physics collision stuff? so it would be easier?
- There is no animation system per spaceship neither? so another performance saver?
- What kind of AI are you using? find nearest and attack? since there is no any nav mesh involved, I would assume it's easier too. Probably some k-d tree update for a N*lg N would be enough.
- For those laser beam, are you using just a infinite long raycast hit detection and only show those beam as effect? or you are using the beam actually moving with raycast detection every frame? For former, you save lots of computation but you don't have that latency effect (you hit instantly when you press fire).
- When you write your own engine, what is your start point? purely from scratch? like opengl/directx with everything? or at least based on some framework?

I don't think it's realistic for me to write my own engine at this time. The rendering stuff alone cross platform will drive me crazy.

BTW: I think Urho3D is extremely good at performance compared to other engines. For example, Sample_12 physics stress test can generate 1000 cubes in the scene, and the framerate ~60 after all cubes become static. So I think Urho has the ability to deal with ~1000 entities within the framework if the entity is simple enough.

-------------------------

JSandusky | 2021-01-07 03:59:33 UTC | #7

There's a number of things that eat away at crowds (in Urho). 

- The volume of events they send is pretty massive, so just by ditching script for C++ when it comes to crowds will be a win.
    - It'd probably be good to add "*binned*" events that roll up everything for all agents like physics does for contacts
    - ExecuteFunction beneath update crowd is probably in the thousands in the profiler
- They update as part of scene subsystem updates and not fixed update so they're ticking constantly and sending those events constantly (making it worse)
- Agents are processed one-by-one in the callback instead of doing it in bulk after crowd update where they could split it up for the thread-tasks
    - adding binned events requires addressing this
- DetourCrowd is single-threaded, parts of it you can split up to jobify but it's not that much
    - Urho using a callback during that update probably doesn't help the update loop's perf either ... another reason to bin things up afterwards

---

The easiest way to check offmesh connections is to check the agent state for DT_CROWDAGENT_STATE_OFFMESH, then you can test the path-corridor to find out which offmesh connection it's actually on (it'll be index 0 or 1 in the corridor depending on time in the internal animation). The hard part is just how to map detour's view of an offmesh-connection back to Urho3Ds in a way that doesn't become a mess with tile regeneration and the like ... probably by checking out IDs from the NavigationMesh and having it keey a `HashMap<unsigned, WeakPtr<OffmeshConnection> >` or such.

-------------------------

throwawayerino | 2021-01-07 11:51:49 UTC | #9

By “binned” do you mean each agent sends only one event with everything that happened to it, or the crowd controller collects the state of each agent and sends a single event with everything in the `eventData` ?

-------------------------

JSandusky | 2021-01-07 17:15:38 UTC | #10

The latter, sending them all means you can do it in a tight loop instead of jumping-around or split it up into thread-jobs (which is only really applicable to C++). Script invocations aren't free.

I binned up the basic update at one point in my own fork and it helped, still wasn't a magic bullet.

-------------------------

Eugene | 2021-01-07 20:18:16 UTC | #11

Speaking of D/R, do you know any nice way to keep agents grounded?
I know that in theory Recast can generate “detail” mesh for positioning, but in practice this mesh is coarse enough to have significant gaps between feet and ground.

Maybe I should just keep all walkable geometry in some acceleration structure and do final raycast on each agent reposition to snap them to ground. Is this the only way?

-------------------------

JSandusky | 2021-01-08 02:01:50 UTC | #12

Nope, I've done it with physics masks in spherecast.

If static you could map dtPolyRefs to a list of triangles to check (if totally static that can just be a offset and count into one big list of triangle-#s) just linking tris inside a bounds around the dtPoly. Or map dtPolyRefs to to a cell in an acceleration structure. There's obvious limits there with navmesh updates and how large you could go.

Being n-gons makes the dtPolys a headache.

---

Though this has all been about Detour it's still worth noting that rendering the agents isn't free. You start pushing several hundred and UpdateDrawables/skinning gets expensive too. If you really want to push that number you're going to have to get creative.

-------------------------

JTippetts1 | 2021-01-08 06:15:04 UTC | #13

The best success I've had in this, without a lot of work, is to build your level geometry pieces such that horizontal walking surfaces lie as near the top of a nav volume voxel as possible. For example, if your volume voxels at navmesh generation are set at 0.5 units high, then any ground plane with a y value between 0 and 0.5 will result in a y value of 0.5 in the navmesh. If your ground plane is 0, that means units will float 0.5 units above the ground. It is a bit of a pain, but with care you can edit your ground planes to fall on the 0.5-interval (or whatever) voxel boundaries, and eliminate the worst of the floating.

-------------------------

QBkGames | 2021-01-09 06:42:51 UTC | #14

The 1000 ship battle is a minimalistic tech demo that does not count as either an engine nor a game, as such, as you've guessed from the video, it has no physics (just simple ray-sphere intersection between laser beams and other objects), no skeletal animation, not even shadows. Laser beams a short line segments that move every frame and are checked for collision with other objects.

If you do want to try the crazy idea of writing your own game/engine optimized for large number of objects, you want to adopt the philosophy of simplify and optimize as low level as possible so you do want to try and write as much as possible yourself, starting with low level API such as OpenGL (which up to about 5 years ago used to mean cross-platform). However, you can use low level libraries such as SDL for windowing/input, some texture loading lib (jpglib, pnglib, etc), and maybe a sound mixer lib and a physics lib. With physics you might want to write your own simplified and optimized library, especially if all you need is collision detection and maybe some simple acceleration.

Other things you want to consider (which are lacking in most general-purpose engines) is some low level memory manager/allocator that combines paging and caching to minimize calls to new/delete.
A simpler scene manager instead of the oct-tree which for most scenarios is overkill and slows down more than helps (I used a static uniform 2D grid for my demo, which I think is a better solution for most games). 

And last and most important, moving away form Object Oriented design to Data oriented design based on the struct-of-arrays pattern, which, for large number of dynamic objects can give up up to 10x performance boost over traditional OO design.

There are lots of things that can be done, but everything takes time, and time is our most precious resource which gets less and less as days go by into eternity.

-------------------------

