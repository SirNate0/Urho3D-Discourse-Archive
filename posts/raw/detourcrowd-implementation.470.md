scorvi | 2017-01-02 01:00:41 UTC | #1

hey,

i am adding detour crowd component to the engine. I have a running sample but i did not create a DetourCrowd lib. 
i want to add this to the engine core libs but DetourCrowd needs detour and i dont know how to add it to the cmake file ... 

my cmake file is in Urho3DDetour\Source\ThirdParty\DetourCrowd and looks like this:
[code]# Define target name
set (TARGET_NAME DetourCrowd)

# Define source files
file (GLOB CPP_FILES source/*.cpp)
file (GLOB H_FILES include/*.h)
set (SOURCE_FILES ${CPP_FILES} ${H_FILES})

# Define dependency libs
set (INCLUDE_DIRS_ONLY include)

# Setup target
setup_library ()
[/code]

i am compiling with visual studio and i get now the error :
[code]Fehler	1	error C1083: Datei (Include) kann nicht ge?ffnet werden: "DetourNavMeshQuery.h": No such file or directory\Urho3DDetour\Source\ThirdParty\DetourCrowd\include\DetourCrowd.h	22	1	DetourCrowd
Fehler	2	error C1083: Datei (Include) kann nicht ge?ffnet werden: "DetourNavMeshQuery.h": No such file or directory	\Urho3DDetour\Source\ThirdParty\DetourCrowd\include\DetourLocalBoundary.h	22	1	DetourCrowd
Fehler	3	error C1083: Datei (Include) kann nicht ge?ffnet werden: "DetourCommon.h": No such file or directory	\Urho3DDetour\Source\ThirdParty\DetourCrowd\source\DetourObstacleAvoidance.cpp	20	1	DetourCrowd
Fehler	4	error C1083: Datei (Include) kann nicht ge?ffnet werden: "DetourNavMeshQuery.h": No such file or directory	\Urho3DDetour\Source\ThirdParty\DetourCrowd\include\DetourPathCorridor.h	22	1	DetourCrowd
Fehler	5	error C1083: Datei (Include) kann nicht ge?ffnet werden: "DetourNavMesh.h": No such file or directory	\Urho3DDetour\Source\ThirdParty\DetourCrowd\include\DetourPathQueue.h	22	1	DetourCrowd
Fehler	6	error C1083: Datei (Include) kann nicht ge?ffnet werden: "DetourCommon.h": No such file or directory \Urho3DDetour\Source\ThirdParty\DetourCrowd\source\DetourProximityGrid.cpp	22	1	DetourCrowd
[/code]

-------------------------

cadaver | 2017-01-02 01:00:41 UTC | #2

You should be able to add Detour's include dir to the "set (INCLUDE_DIRS_ONLY)" statement, using a relative path like ../Detour/include.

-------------------------

scorvi | 2017-01-02 01:00:42 UTC | #3

yes thx that did it ^^ 

i have now extended the navigation sample with detourcrowd and it works :slight_smile: 
created comonents are:
DetourCrowdManager 
DetourCrowdAgent

i implemented DetourCrowd like the Physics components.
you have to create  DetourCrowdManager  to the root scene node (like PhysicsWorld) and you can add DetourCrowdAgent to your nodes (like RigidBody). 
But you can also only use DetourCrowdManager::AddAgent function to get the agents id. With the id you can call  DetourCrowdManager::GetAgentPosition(id) ... so that you dont have to use the  DetourCrowdAgent component. 

i am also updating the NavigationMesh with NavmeshPartitionTypes and a add the debug functions memononen used in his demo, for better debuging ^^
after that i will add a AnnotationBuilder component to create cover points and Jump Links ([digestingduck.blogspot.fi/2011/0 ... s-and.html](http://digestingduck.blogspot.fi/2011/07/paris-gameai-conference-2011-slides-and.html))


can that be added to the engine (after code cleanup) ?

-------------------------

scorvi | 2017-01-02 01:00:42 UTC | #4

so added the new navmesh debug view ... 

but i have now another problem,
if i add this line in NavigationMesh::RegisterObject(Context* context) :
[code]ENUM_ACCESSOR_ATTRIBUTE(NavigationMesh, "Partition Type", GetPartitionType, SetPartitionType, NavmeshPartitionType, navmeshPartitionTypeNames, NAVMESH_PARTITION_WATERSHED, AM_DEFAULT);[/code]

the urho3d lib compiles but the navigation sample does not. it gets some kind of link error, does not now NavmeshPartitionType ... but without that line it compiles ! 

[url=http://imgur.com/kCBpcOQ][img]http://i.imgur.com/kCBpcOQl.jpg[/img][/url]
[url=http://imgur.com/nDTUFh3][img]http://i.imgur.com/nDTUFh3l.jpg[/img][/url]

-------------------------

cadaver | 2017-01-02 01:00:43 UTC | #5

Yes, when you make a pull request it will be added (pending any cleanup or fixes) and it completes one of the issues we have marked on the tracker.

If the NavmeshPartitionType is an enum defined in the bowels of Detour I recommend to change the type in the NavigationMesh public API to int or unsigned if possible and cast to the Detour type only internally.

-------------------------

weitjong | 2017-01-02 01:00:43 UTC | #6

I don't know how to express this properly but the screenshots look so "delicious" :slight_smile:

-------------------------

scorvi | 2017-01-02 01:00:44 UTC | #7

[quote]If the NavmeshPartitionType is an enum defined in the bowels of Detour I recommend to change the type in the NavigationMesh public API to int or unsigned if possible and cast to the Detour type only internally.[/quote]

the enum is defined in NavigationMesh.h/cpp so i added 
[code] 
 const char* navmeshPartitionTypeNames[] =
 {
 "watershed",
 "monotone",
 "layers",
 0
 };
template<> NavmeshPartitionType Variant::Get<NavmeshPartitionType>() const
 {
 return (NavmeshPartitionType)GetInt();
 }[/code]

and it works now ^^


[quote]I don't know how to express this properly but the screenshots look so "delicious" :slight_smile:[/quote]
yeah, the new debug view from memononen is nice, but i think it needs a staticModel or customGeometry implentation for speed and so that it can be culled. 
I added the annotation builder but it does not find all jump down links ... 
And the first iteration is online [github.com/scorvi/Urho3D/tree/DetourCrowd](https://github.com/scorvi/Urho3D/tree/DetourCrowd)

[url=http://imgur.com/3KGhszO][img]http://i.imgur.com/3KGhszOl.jpg[/img][/url]

[url=http://imgur.com/qeVQGHu][img]http://i.imgur.com/qeVQGHul.jpg[/img][/url]

-------------------------

Mike | 2017-01-02 01:00:44 UTC | #8

Great job so far scorvi, thanks for sharing  :stuck_out_tongue:

I've had to fix 3 CMakeLists (due to inconsistant use of lower/upper case for source folders' name) and DetourCrowdManager.cpp to make it work, maybe fork is not up-to-date.

-------------------------

scorvi | 2017-01-02 01:00:45 UTC | #9

[quote="Mike"]Great job so far scorvi, thanks for sharing  :stuck_out_tongue:

I've had to fix 3 CMakeLists (due to inconsistant use of lower/upper case for source folders' name) and DetourCrowdManager.cpp to make it work, maybe fork is not up-to-date.[/quote]

hmm i just updated the source folder. can you check if the the issues are no resolved or can you say what you edited ? 

so i just added the navigation agent and a crowd debug view 

[url=http://imgur.com/Y9K8tsn][img]http://i.imgur.com/Y9K8tsnl.jpg[/img][/url]
[url=http://imgur.com/9IL02fh][img]http://i.imgur.com/9IL02fhl.jpg[/img][/url]

-------------------------

Mike | 2017-01-02 01:00:45 UTC | #10

I'll send you a pull-request so you will be able to see the modifications, maybe some compilers are not case-sensitive.

-------------------------

JTippetts | 2017-01-02 01:00:49 UTC | #11

I am pretty eager to see this go to master. Looking good.

-------------------------

scorvi | 2017-01-02 01:00:49 UTC | #12

hey 
i think it is ready to go in the master branch but it is not complete ...  i put some todos in there but they are not important one.  so if someone can look at the code and say it is ok i will make a pull request.
hmm  the annotation builder is not ready so it will not upload it. i also made a sample project. 

hmm there was a problem with lower/upper case for include/source folders' names so i changed them to lower cases but github does not update them :-/ how can i update/change folder names ?

-------------------------

JTippetts | 2017-01-02 01:00:49 UTC | #13

I think it might still need a little bit of work before it can be pulled into master. At the very least, it would need the Script and LuaScript bindings. Also, I suspect cadaver would probably want to see vecmath.h and vecmath.cpp replaced. I recommend you check the contribution checklist at [urho3d.github.io/documentation/H ... klist.html](http://urho3d.github.io/documentation/HEAD/_contribution_checklist.html) before you do the pull request, just to make sure you've gotten everything in order.

-------------------------

scorvi | 2017-01-02 01:00:50 UTC | #14

ahh ok thx for the link. i did not see that documentation ...

-------------------------

JTippetts | 2017-01-02 01:00:50 UTC | #15

I've forked your repo and am currently doing some stuff, including writing bindings. I can send you a pull request when I'm done, if you like.

-------------------------

Mike | 2017-01-02 01:01:12 UTC | #16

Hey Scorvi and Joshua,
Are you still working on DetourCrowd?

-------------------------

JTippetts | 2017-01-02 01:01:13 UTC | #17

I am kinda/sorta still working on it, as I can in between 12 hr shifts at work. For the immediate future, I plan to read the Detour Crowd docs through again to see where I can best make some changes. I've got the Lua and Angelscript bindings started for DetourCrowdManager and NavigationAgent, and have made only a few slight changes to what scorvi originally wrote to facilitate the bindings. You can check out what I've got so far at my fork: [github.com/JTippetts/Urho3D/tree/DetourCrowd](https://github.com/JTippetts/Urho3D/tree/DetourCrowd)

The AngelScript sample is the most complete, and in fact I haven't started a Lua sample or kept the C++ sample up-to-date with what I've been doing. I'm still a long way from where I want to get with things, but I'll keep plugging away.

-------------------------

Mike | 2017-01-02 01:01:13 UTC | #18

Thanks for reply Joshua.
From gamedev I've seen that your new job has tough rythms.
Let me know if I can be of any help, for example for the lua sample and updating the C++ sample.

-------------------------

Azalrion | 2017-01-02 01:01:14 UTC | #19

It might be worthwhile on adding the masagroup ([github.com/masagroup/recastdetour](https://github.com/masagroup/recastdetour)) improvements to DetourCrowd to provide specific navigation behaviors instead of just pure path following. Happy to do so and create a pull request if no one has any objections.

-------------------------

JTippetts | 2017-01-02 01:01:14 UTC | #20

I notice that the base Recast/Detour git repo has recent activity, but the Masa group one last had a commit a year ago. I, personally, have no objection to the switch if it adds functionality, as long as we don't get stuck in an abandoned fork that isn't going anywhere.

-------------------------

Azalrion | 2017-01-02 01:01:14 UTC | #21

Seems most of the changes in the main repo are to do with bug fixes and filter changes, should be fairly simple to rebase the masa group work onto the main repo to keep both sets of changes, the major difference is that collision avoidance is not done by default in masa group but needs to be chained with other behaviors and so that requires a fairly large change to DetourCrowd, would also mean we would have to keep the Urho version manually updated.

-------------------------

JTippetts | 2017-01-02 01:01:15 UTC | #22

Okay, that's fine with me. Although since this is scorvi's baby, maybe he'd like to weigh in. I'm guessing, too, that we'll probably need to do some redesigning of the component classes to take advantage of it. Perhaps we should take this to a thread in Developer Talk or something.

-------------------------

Azalrion | 2017-01-02 01:01:21 UTC | #23

Spent some time looking at this some more while off work (slow going with only one hand for typing), not worth moving to masa crowd at the moment it would be a complete re-write. Instead just working on finishing and tidying the current impl up with things such as per agent flags, height, radius, more pathing events and getting it to play nice with physics. I'll add a branch to the main urho repo soon for everyone to play with.

[video]https://www.youtube.com/watch?v=BpB_Ar31O8I[/video]

-------------------------

OvermindDL1 | 2017-01-02 01:01:22 UTC | #24

Looks fascinating, looking forward.

-------------------------

hdunderscore | 2017-01-02 01:01:22 UTC | #25

Very cool !

-------------------------

weitjong | 2017-01-02 01:02:44 UTC | #26

Any update on this work? It has been months since the last post.

-------------------------

codingmonkey | 2017-01-02 01:04:35 UTC | #27

Awesome, great work!
Is it going into master also ?

-------------------------

GoogleBot42 | 2017-01-02 01:04:35 UTC | #28

Great work!  Looks amazing!   :smiley:

-------------------------

weitjong | 2017-01-02 01:04:38 UTC | #29

I have been looking forward for this. Thanks for sharing it.

-------------------------

weitjong | 2017-01-02 01:04:38 UTC | #30

That makes two of us, I am no CMake guru too. I only know enough of the tool to use it to scratch my own itch. I just have a quick look on your Urho3D fork and I agree with you that this approach will make the future update harder than necessary. What kind of problem you encounter when trying to add those sub-libs separately as recommended by memononen. There should be no problem to modify the CMakeLists.txt for one sub-lib to depend on the include dir from the other sub-lib.

-------------------------

TikariSakari | 2017-01-02 01:04:38 UTC | #31

I've been trying to have some sort of obstacle like thing with the urho and navmeshes, but looks like this would make it a lot easier for moving objects than having to constantly rebuild the navmesh. So big thanks for this.

I tested out the example, and I noticed that the characters do not move that close to the point where I actually click. I feel like in general it was bottom left corner where a crowd settled to considering where my mouse was, not center.

On the screenshot the cursor in middle of the screen came from taking the screenshot, so the "real" cursor is the other one.
[url]http://i.imgur.com/zToLG0e.jpg[/url]
I guess this line is the culpirit
[code]
agent->SetMoveTarget(pathPos + Vector3(Random(7.0f), 0.0f, Random(7.0f)));
[/code]
Also it feels bit odd that even if I only have one jack moving, it still goes off from the point of where I click, but that is more of an example thing rather than a bug with the detour crowd.

Another thing that I noticed is that there seems to be some sort of easing with the moving. By easing I mean that the jacks "drive" past the target point, then go back few steps. As far as I looked at the example, I didn't see this behavior being set, so this is by default I assume?.  I hope that there is a way to set this to a linear interpolation.

Edit: Also I was curious with the example what would happen if I tried to move the characters into top right corner of the scene. Since it sets the movement points to location + bit of randomness. It turns out that if it doesn't random a point that actually exists on the plane, those units do not move at all.

-------------------------

thebluefish | 2017-01-02 01:04:46 UTC | #32

Any estimate for when this gets merged with the urho3d master branch?

It looks like I've ran across a couple of issues with this. They seem to revolve around the CrowdAgent component. Right now I'm saving out a node with everything configured, and then instantiating it later.

The first issue is that when I load the node xml, and then save it back out, the CrowdAgent no longer moves. ResourceCache is set to auto-refresh the files. I am calling the following, which is still being called every frame:

[code]
Urho3D::CrowdAgent* agent = GetNode()->GetComponent<Urho3D::CrowdAgent>();
			agent->SetMoveTarget(_playerNode->GetPosition());
[/code]

The second issue is what happens when I don't do that. If I simply load the game and play it without saving the xml, then the CrowdAgent properly moves around. However all agents start at position (0,0,0). This happens even though I'm creating the node at a specific position before-hand.

If I load the node, then save it out (reproducing the first issue), I can see the agents positioned properly.

Edit:

It appears that the second issue comes from the fact that the node's position is set after all of its components are added when calling InstantiateXML. Debugging shows that the node is created, the component added, the agent added to the crowd manager, then the node's position is set. I have currently worked around this by using the following code:

[code]
Urho3D::XMLFile* file = cache->GetResource<Urho3D::XMLFile>("Objects/Enemy.xml");

			Urho3D::DynamicNavigationMesh* navMesh = GetComponent<Urho3D::DynamicNavigationMesh>();
			Urho3D::Vector3 position = navMesh->GetRandomPoint();
			Urho3D::Node* node = GetScene()->InstantiateXML(file->GetRoot(), position, GetNode()->GetRotation());

			Urho3D::CrowdAgent* agent = node->GetComponent<Urho3D::CrowdAgent>();
			if (agent)
			{
				agent->SetEnabled(false);
				node->SetPosition(position);
				agent->SetEnabled(true);
			}
[/code]

Edit:

It looks like the first issue is related to the fact that DetourCrowdManager is automatically created when loading the node in the editor. Apparently having this component already in the scene appears to break things.

-------------------------

thebluefish | 2017-01-02 01:04:47 UTC | #33

For the first issue - The DetourCrowdManager and DynamicNavigationMesh are both created in the editor. The CrowdAgent is created during runtime by a scene-level component. I actually serialize out the editor scene and then serialize it back in when testing the game, and it still breaks if DetourCrowdManager is present initially.

-------------------------

thebluefish | 2017-01-02 01:04:48 UTC | #34

I have been playing with this for a few days now. I have found a few issues:

- There is a slow down after a number of agents has been created. I find that around 190-200 (~100 in Debug) agents with a move target begins to show some slowdown at around 30 FPS on this PC. At around 250-300 (~120-150) agents, that drops to <1 FPS on the same machine. If there aren't any move targets, then there's no slow down. I have reproduced this with nodes with only the CrowdAgent component in order to rule out other components (ParticleEmitter, etc...) being the problem.

It would also be nice to have some additional functions in DetourCrowdManager. In particle, getset the max number of agents, and getting a list of agents would be nice. I've implemented these in my branch in a dirty way for now though.

-------------------------

friesencr | 2017-01-02 01:04:49 UTC | #35

If I recall from the docs, 1ms / 30 agents from just detour crowd.

-------------------------

JTippetts | 2017-01-02 01:05:01 UTC | #36

Just saw that this has been pulled into master. Thanks a lot for continuing work on this thing.

-------------------------

weitjong | 2017-01-02 01:05:02 UTC | #37

I have said it in my earlier post but thanks again for your awesome work. BTW, the HTML5 version of the new sample is uploaded this morning. [urho3d.github.io/samples/39_CrowdNavigation.html](http://urho3d.github.io/samples/39_CrowdNavigation.html)

-------------------------

weitjong | 2017-01-02 01:05:03 UTC | #38

I made a line comment in the GitHub on these lines of code: [github.com/urho3d/Urho3D/blob/m ... #L504-L507](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Navigation/DetourCrowdManager.cpp#L504-L507). In my opinion, I think navigation should not depend on physics. Any objection to change the event type from E_PHYSICSPRESTEP (fixed-rate timestep) to, say, E_SCENESUBSYSTEMUPDATE (variable-rate timestep)? It not only decouples Detour crowd navigation from Physics subsystem but also makes crowd manager to update at the same (variable) rate as the DynamicNavigationMesh component. If there is no objection then I will include this change in my next commit which mainly consists of minor code cleanup due to code convention.

-------------------------

weitjong | 2017-01-02 01:05:03 UTC | #39

OK. I will include that change in my next commit. About the agent being "locked", yes, I am observing that too. The locked agent can be produced in the manner you just mentioned and also when spawning too many Jacks on a same tight spot (i.e. when it is spawned on top of another or on top a cube).

-------------------------

cadaver | 2017-01-02 01:05:03 UTC | #40

Ah yes, moving away from FixedUpdate is good for at least two additional reasons:
1) No spiral-of-death if navigation would suddenly take a lot of time
2) Physics interpolates transforms, while applying the navigation positions doesn't, so it will look smoother

-------------------------

weitjong | 2017-01-02 01:05:04 UTC | #41

One more other minor thing. There is inconsistency (at least to me) in naming the member variable/method for "area type/id" in different classes. I think we should either stick to "area id" following the internal implementation of DetourCrowd or stick to "area type" through out Urho3D API.

-------------------------

Mike | 2017-01-02 01:05:04 UTC | #42

I find 'id' more intuitive than 'type', for which I was mistakenly expecting an enum.

-------------------------

weitjong | 2017-01-02 01:05:04 UTC | #43

[quote="Sinoid"]Was the cube case you saw in the angelscript example? For some dumb reason I set the spawned Jacks' Y position to 0 instead of using the exact point from the nav mesh. That causes the agents to be hidden inside the boxes, the other examples don't appear to suffer this (at least from a quick look).[/quote]
I believe I encountered this on native version. I think it has something to do with the cube size (or more precisely its height). On a taller cube the agent behaves normally, although Jack does not know how to climb down :slight_smile:, it is not locked in place. On a shorter cube, however, the agent is locked. I think it has something to do with the nav mesh itself. It appears that any agents spawned in between the floor and a certain height-threshold is locked.

[quote="Sinoid"]Because the agent's state could become invalid (and therefore frozen) in different ways (a very large obstacle was placed right on top of it, it was knocked far off the navmesh, etc) it's probably best to leave the handling of that to the user.

The next viable option for simple cases would be to allow for a "correction margin" in which the agent would snap to the nearest point on the navmesh if within the range of the margin - though you could accomplish the same thing according to specific needs by handling the event.[/quote]
I am totally agree with you that it would be best to leave the handling of such case to the user (app-specific). For a Lemmings-type game, one would probably just kills the agent. It would be great if we have a unique event type for this situation or we have an indicator flag for this somewhere. We can then demonstrate how to handle such event in the simplest case as you mentioned above in the sample just as an example.

-------------------------

Mike | 2017-01-02 01:05:12 UTC | #44

Does anybody successfully tested off-mesh connections?

-------------------------

Mike | 2017-01-02 01:05:12 UTC | #45

Thanks Sinoid, I've tried from code to jump from one box to another and failed. I'll try to replicate your experiment.
In my experiment I've created OffMeshConnection before building, after looking at NavigationMesh.cpp code.

Just to be sure, what are your 'start' node (holding the component) and your end node? Does radius matter?

-------------------------

Mike | 2017-01-02 01:05:12 UTC | #46

Ah! It didn't hook (white debug geometry). I'll test this immediately! Many thanks for these insights Sinoid  :stuck_out_tongue:

-------------------------

Mike | 2017-01-02 01:05:12 UTC | #47

Finally I used FindNearestPoint() to set my nodes' position and it works perfectly  :stuck_out_tongue: 
Thanks again for your detailed great insights.

@Cadaver, maybe we could add this to the samples (15 and/or 39), it only costs a few lines of code to create 2 nodes  :unamused:

-------------------------

cadaver | 2017-01-02 01:05:12 UTC | #48

Yes, feel free to add.

-------------------------

Mike | 2017-01-02 01:05:12 UTC | #49

Great, thanks.

-------------------------

Mike | 2017-01-02 01:05:12 UTC | #50

I've added off-mesh connections to sample 39. Overall it works great, but sometimes it fails:
- although hooking correctly, a few boxes are still non climbable
- after climbing on the tallest box, agent can't go down

I also noticed that when removing a moving agent, its target path remains (in debug draw) when creating a new agent. Maybe some agent data needs to be cleared when removing an agent.

[spoiler][code]
-- CrowdNavigation example.
-- This sample demonstrates:
--     - Generating a dynamic navigation mesh into the scene
--     - Performing path queries to the navigation mesh
--     - Adding and removing obstacles at runtime from the dynamic mesh
--     - Adding and removing crowd agents at runtime
--     - Raycasting drawable components
--     - Crowd movement management
--     - Accessing crowd agents with the crowd manager
--     - Using off-mesh connections to make boxes climbable

require "LuaScripts/Utilities/Sample"

local crowdManager = nil
local agents = {}

function Start()
    -- Execute the common startup for samples
    SampleStart()

    -- Create the scene content
    CreateScene()

    -- Create the UI content
    CreateUI()

    -- Setup the viewport for displaying the scene
    SetupViewport()

    -- Hook up to the frame update and render post-update events
    SubscribeToEvents()
end

function CreateScene()
    scene_ = Scene()
    -- Create octree, use default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
    -- Also create a DebugRenderer component so that we can draw debug geometry
    scene_:CreateComponent("Octree")
    scene_:CreateComponent("DebugRenderer")

    -- Create scene node & StaticModel component for showing a static plane
    local planeNode = scene_:CreateChild("Plane")
    planeNode.scale = Vector3(100.0, 1.0, 100.0)
    local planeObject = planeNode:CreateComponent("StaticModel")
    planeObject.model = cache:GetResource("Model", "Models/Plane.mdl")
    planeObject.material = cache:GetResource("Material", "Materials/StoneTiled.xml")

    -- Create a Zone component for ambient lighting & fog control
    local zoneNode = scene_:CreateChild("Zone")
    local zone = zoneNode:CreateComponent("Zone")
    zone.boundingBox = BoundingBox(-1000.0, 1000.0)
    zone.ambientColor = Color(0.15, 0.15, 0.15)
    zone.fogColor = Color(0.5, 0.5, 0.7)
    zone.fogStart = 100.0
    zone.fogEnd = 300.0

    -- Create a directional light to the world. Enable cascaded shadows on it
    local lightNode = scene_:CreateChild("DirectionalLight")
    lightNode.direction = Vector3(0.6, -1.0, 0.8)
    local light = lightNode:CreateComponent("Light")
    light.lightType = LIGHT_DIRECTIONAL
    light.castShadows = true
    light.shadowBias = BiasParameters(0.00025, 0.5)
    -- Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
    light.shadowCascade = CascadeParameters(10.0, 50.0, 200.0, 0.0, 0.8)

    -- Create randomly sized boxes. If boxes are big enough, make them occluders. Occluders will be software rasterized before
    -- rendering to a low-resolution depth-only buffer to test the objects in the view frustum for visibility
    local boxes = {}
    for i = 1, 20 do
        local boxNode = scene_:CreateChild("Box")
        local size = 1.0 + Random(10.0)
        boxNode.position = Vector3(Random(80.0) - 40.0, size * 0.5, Random(80.0) - 40.0)
        boxNode:SetScale(size)
        local boxObject = boxNode:CreateComponent("StaticModel")
        boxObject.model = cache:GetResource("Model", "Models/Box.mdl")
        boxObject.material = cache:GetResource("Material", "Materials/Stone.xml")
        boxObject.castShadows = true
        if size >= 3.0 then
            boxObject.occluder = true
            table.insert(boxes, boxNode)
        end
    end

    -- Create a DynamicNavigationMesh component to the scene root
    local navMesh = scene_:CreateComponent("DynamicNavigationMesh")
    -- Enable drawing debug geometry for obstacles and off-mesh connections
    navMesh.drawObstacles = true
--    navMesh.drawOffMeshConnections = true
    -- Set the agent height large enough to exclude the layers under boxes
    navMesh.agentHeight = 10
    -- Set nav mesh tilesize to something reasonable
    navMesh.tileSize = 64
    -- Set nav mesh cell height to minimum (allows agents to be grounded)
    navMesh.cellHeight = 0.05
    -- Create a Navigable component to the scene root. This tags all of the geometry in the scene as being part of the
    -- navigation mesh. By default this is recursive, but the recursion could be turned off from Navigable
    scene_:CreateComponent("Navigable")
    -- Add padding to the navigation mesh in Y-direction so that we can add objects on top of the tallest boxes
    -- in the scene and still update the mesh correctly
    navMesh.padding = Vector3(0.0, 10.0, 0.0)
    -- Now build the navigation geometry. This will take some time. Note that the navigation mesh will prefer to use
    -- physics geometry from the scene nodes, as it often is simpler, but if it can not find any (like in this example)
    -- it will use renderable geometry instead
    navMesh:Build()

    -- Create an OffMeshConnection for each box to make it climbable (tiny boxes are skipped)
    for i, box in ipairs(boxes) do
        local boxPos = box.position
        local connectionStart = scene_:CreateChild("Connection1")
        connectionStart.position = navMesh:FindNearestPoint(boxPos + Vector3(box.scale.x / 2, -box.scale.y / 2, 0), Vector3.ONE) -- Base of box
        local connectionEnd = connectionStart:CreateChild("Connection2")
        connectionEnd.worldPosition = navMesh:FindNearestPoint(boxPos + Vector3(box.scale.x / 2, box.scale.y / 2, 0), Vector3.ONE) -- Top of box

        local connection = connectionStart:CreateComponent("OffMeshConnection")
        connection.endPoint = connectionEnd
    end

    -- Create a DetourCrowdManager component to the scene root
    crowdManager = scene_:CreateComponent("DetourCrowdManager")

    -- Create Jack node as crowd agent
    SpawnJack(Vector3(-5, 0, 20))

    -- Create some mushrooms as obstacles. Note that obstacles are added onto an already buit navigation mesh
    for i = 1, 100 do
        CreateMushroom(Vector3(Random(90.0) - 45.0, 0.0, Random(90.0) - 45.0))
    end

    -- Create the camera. Limit far clip distance to match the fog. Note: now we actually create the camera node outside
    -- the scene, because we want it to be unaffected by scene load / save
    cameraNode = Node()
    local camera = cameraNode:CreateComponent("Camera")
    camera.farClip = 300.0

    -- Set an initial position for the camera scene node above the plane
    cameraNode.position = Vector3(0.0, 5.0, 0.0)
end

function CreateUI()
    -- Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
    -- control the camera, and when visible, it will point the raycast target
    local style = cache:GetResource("XMLFile", "UI/DefaultStyle.xml")
    local cursor = Cursor:new()
    cursor:SetStyleAuto(style)
    ui.cursor = cursor
    -- Set starting position of the cursor at the rendering window center
    cursor:SetPosition(graphics.width / 2, graphics.height / 2)

    -- Construct new Text object, set string to display and font to use
    local instructionText = ui.root:CreateChild("Text")
    instructionText.text = "Use WASD keys to move, RMB to rotate view\n"..
        "LMB to set destination, SHIFT+LMB to spawn a Jack\n"..
        "MMB to add obstacles or remove obstacles/agents\n"..
        "F5 to save scene, F7 to load\n"..
        "Space to toggle debug geometry"
    instructionText:SetFont(cache:GetResource("Font", "Fonts/Anonymous Pro.ttf"), 15)
    -- The text has multiple rows. Center them in relation to each other
    instructionText.textAlignment = HA_CENTER

    -- Position the text relative to the screen center
    instructionText.horizontalAlignment = HA_CENTER
    instructionText.verticalAlignment = VA_CENTER
    instructionText:SetPosition(0, ui.root.height / 4)
end

function SetupViewport()
    -- Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
    local viewport = Viewport:new(scene_, cameraNode:GetComponent("Camera"))
    renderer:SetViewport(0, viewport)
end

function SubscribeToEvents()
    -- Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent("Update", "HandleUpdate")

    -- Subscribe HandlePostRenderUpdate() function for processing the post-render update event, during which we request
    -- debug geometry
    SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate")

    -- Subscribe HandleCrowdAgentFailure() function for resolving invalidation issues with agents, during which we
    -- use a larger extents for finding a point on the navmesh to fix the agent's position
    SubscribeToEvent("CrowdAgentFailure", "HandleCrowdAgentFailure")
end

function SpawnJack(pos)
    local jackNode = scene_:CreateChild("Jack")
    jackNode.position = pos
    local modelObject = jackNode:CreateComponent("AnimatedModel")
    modelObject.model = cache:GetResource("Model", "Models/Jack.mdl")
    modelObject.material = cache:GetResource("Material", "Materials/Jack.xml")
    modelObject.castShadows = true

    -- Create a CrowdAgent component and set its height (use default radius)
    local agent = jackNode:CreateComponent("CrowdAgent")
    agent.height = 2.0
    agents = crowdManager:GetActiveAgents() -- Update agents container
end

function CreateMushroom(pos)
    local mushroomNode = scene_:CreateChild("Mushroom")
    mushroomNode.position = pos
    mushroomNode.rotation = Quaternion(0.0, Random(360.0), 0.0)
    mushroomNode:SetScale(2.0 + Random(0.5))
    local mushroomObject = mushroomNode:CreateComponent("StaticModel")
    mushroomObject.model = cache:GetResource("Model", "Models/Mushroom.mdl")
    mushroomObject.material = cache:GetResource("Material", "Materials/Mushroom.xml")
    mushroomObject.castShadows = true

    -- Create the navigation Obstacle component and set its height & radius proportional to scale
    local obstacle = mushroomNode:CreateComponent("Obstacle")
    obstacle.radius = mushroomNode.scale.x
    obstacle.height = mushroomNode.scale.y
    return mushroomNode
end

function SetPathPoint()
    local hitPos, hitDrawable = Raycast(250.0)
    local navMesh = scene_:GetComponent("DynamicNavigationMesh")

    if hitDrawable then
        local pathPos = navMesh:FindNearestPoint(hitPos, Vector3.ONE)

        if input:GetQualifierDown(QUAL_SHIFT) then
            -- Spawn a Jack
            SpawnJack(pathPos)
        else
            -- Set target position and ignit agents' move
            for i = 1, table.maxn(agents) do
                local agent = agents[i]

                if i == 1 then
                    -- The first agent will always move to the exact position
                    agent:SetMoveTarget(pathPos)
                else
                    -- Other agents will move to a random point nearby
                    local targetPos = navMesh:FindNearestPoint(pathPos + Vector3(Random(-4.5, 4.5), 0, Random(-4.5, 4.5)), Vector3.ONE)
                    agent:SetMoveTarget(targetPos)
                end
            end
        end
    end
end

function AddOrRemoveObject()
    -- Raycast and check if we hit a mushroom node. If yes, remove it, if no, create a new one
    local hitPos, hitDrawable = Raycast(250.0)
    if hitDrawable then

        local hitNode = hitDrawable.node
        if hitNode.name == "Mushroom" then
            hitNode:Remove()
        elseif hitNode.name == "Jack" then
            hitNode:Remove()
            agents = crowdManager:GetActiveAgents() -- Update agents container
        else
            CreateMushroom(hitPos)
        end
    end
end

function Raycast(maxDistance)
    local hitPos = nil
    local hitDrawable = nil

    local pos = ui.cursorPosition
    -- Check the cursor is visible and there is no UI element in front of the cursor
    if (not ui.cursor.visible) or (ui:GetElementAt(pos, true) ~= nil) then
        return nil, nil
    end

    local camera = cameraNode:GetComponent("Camera")
    local cameraRay = camera:GetScreenRay(pos.x / graphics.width, pos.y / graphics.height)
    -- Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
    local octree = scene_:GetComponent("Octree")
    local result = octree:RaycastSingle(cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY)
    if result.drawable ~= nil then
        return result.position, result.drawable
    end

    return nil, nil
end

function MoveCamera(timeStep)
    -- Right mouse button controls mouse cursor visibility: hide when pressed
    ui.cursor.visible = not input:GetMouseButtonDown(MOUSEB_RIGHT)

    -- Do not move if the UI has a focused element (the console)
    if ui.focusElement ~= nil then
        return
    end

    -- Movement speed as world units per second
    local MOVE_SPEED = 20.0
    -- Mouse sensitivity as degrees per pixel
    local MOUSE_SENSITIVITY = 0.1

    -- Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
    -- Only move the camera when the cursor is hidden
    if not ui.cursor.visible then
        local mouseMove = input.mouseMove
        yaw = yaw + MOUSE_SENSITIVITY * mouseMove.x
        pitch = pitch + MOUSE_SENSITIVITY * mouseMove.y
        pitch = Clamp(pitch, -90.0, 90.0)

        -- Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
        cameraNode.rotation = Quaternion(pitch, yaw, 0.0)
    end

    -- Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
    if input:GetKeyDown(KEY_W) then
        cameraNode:Translate(Vector3(0.0, 0.0, 1.0) * MOVE_SPEED * timeStep)
    end
    if input:GetKeyDown(KEY_S) then
        cameraNode:Translate(Vector3(0.0, 0.0, -1.0) * MOVE_SPEED * timeStep)
    end
    if input:GetKeyDown(KEY_A) then
        cameraNode:Translate(Vector3(-1.0, 0.0, 0.0) * MOVE_SPEED * timeStep)
    end
    if input:GetKeyDown(KEY_D) then
        cameraNode:Translate(Vector3(1.0, 0.0, 0.0) * MOVE_SPEED * timeStep)
    end
    -- Set destination or spawn a jack with left mouse button
    if input:GetMouseButtonPress(MOUSEB_LEFT) then
        SetPathPoint()
    end
    -- Add new obstacle or remove existing obstacle/agent with middle mouse button
    if input:GetMouseButtonPress(MOUSEB_MIDDLE) then
        AddOrRemoveObject()
    end

    -- Toggle debug geometry with space
    if input:GetKeyPress(KEY_SPACE) then
        drawDebug = not drawDebug
    end

    -- Check for loading/saving the scene from/to the file Data/Scenes/CrowdNavigation.xml relative to the executable directory
    if input:GetKeyPress(KEY_F5) then
        scene_:SaveXML(fileSystem:GetProgramDir().."Data/Scenes/CrowdNavigation.xml")
    end
    if input:GetKeyPress(KEY_F7) then
        scene_:LoadXML(fileSystem:GetProgramDir().."Data/Scenes/CrowdNavigation.xml")

        -- After reload, reacquire crowd manager & agents
        crowdManager = scene_:GetComponent("DetourCrowdManager")
        agents = crowdManager:GetActiveAgents()

        -- Re-enable debug draw for obstacles
        local navMesh = scene_:GetComponent("DynamicNavigationMesh")
        navMesh.drawObstacles = true
    end
end

function HandleUpdate(eventType, eventData)
    -- Take the frame time step, which is stored as a float
    local timeStep = eventData:GetFloat("TimeStep")

    -- Move the camera, scale movement with time step
    MoveCamera(timeStep)

    -- Make the CrowdAgents face the direction of their velocity
    for i = 1, table.maxn(agents) do
        local agent = agents[i]
        agent.node.worldDirection = agent.actualVelocity
    end
end

function HandlePostRenderUpdate(eventType, eventData)
    -- If draw debug mode is enabled, draw navigation debug geometry
    if drawDebug then
        -- Visualize navigation mesh and obstacles
        local navMesh = scene_:GetComponent("DynamicNavigationMesh")
        navMesh:DrawDebugGeometry(true)

        -- Visualize agents' path and position to reach
        crowdManager:DrawDebugGeometry(true)
    end
end

function HandleCrowdAgentFailure(eventType, eventData)

    local node = eventData:GetPtr("Node", "Node")
    local agent = eventData:GetPtr("CrowdAgent", "CrowdAgent")
    local agentState = eventData:GetInt("CrowdAgentState")

    -- If the agent's state is invalid, likely from spawning on the side of a box, find a point in a larger area
    if agentState == CROWD_AGENT_INVALID then
        local navMesh = scene_:GetComponent("DynamicNavigationMesh")
        -- Get a point on the navmesh using more generous extents
        local newPos = navMesh:FindNearestPoint(node:GetWorldPosition(), Vector3(5, 5, 5))
        -- Set the new node position, CrowdAgent component will automatically reset the state of the agent
        node:SetWorldPosition(newPos)
    end

end

-- Create XML patch instructions for screen joystick layout specific to this sample app
function GetScreenJoystickPatchString()
    return
        "<patch>" ..
        "    <add sel=\"/element\">" ..
        "        <element type=\"Button\">" ..
        "            <attribute name=\"Name\" value=\"Button3\" />" ..
        "            <attribute name=\"Position\" value=\"-120 -120\" />" ..
        "            <attribute name=\"Size\" value=\"96 96\" />" ..
        "            <attribute name=\"Horiz Alignment\" value=\"Right\" />" ..
        "            <attribute name=\"Vert Alignment\" value=\"Bottom\" />" ..
        "            <attribute name=\"Texture\" value=\"Texture2D;Textures/TouchInput.png\" />" ..
        "            <attribute name=\"Image Rect\" value=\"96 0 192 96\" />" ..
        "            <attribute name=\"Hover Image Offset\" value=\"0 0\" />" ..
        "            <attribute name=\"Pressed Image Offset\" value=\"0 0\" />" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"Label\" />" ..
        "                <attribute name=\"Horiz Alignment\" value=\"Center\" />" ..
        "                <attribute name=\"Vert Alignment\" value=\"Center\" />" ..
        "                <attribute name=\"Color\" value=\"0 0 0 1\" />" ..
        "                <attribute name=\"Text\" value=\"Spawn Jack\" />" ..
        "            </element>" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"KeyBinding\" />" ..
        "                <attribute name=\"Text\" value=\"LSHIFT\" />" ..
        "            </element>" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"MouseButtonBinding\" />" ..
        "                <attribute name=\"Text\" value=\"LEFT\" />" ..
        "            </element>" ..
        "        </element>" ..
        "        <element type=\"Button\">" ..
        "            <attribute name=\"Name\" value=\"Button4\" />" ..
        "            <attribute name=\"Position\" value=\"-120 -12\" />" ..
        "            <attribute name=\"Size\" value=\"96 96\" />" ..
        "            <attribute name=\"Horiz Alignment\" value=\"Right\" />" ..
        "            <attribute name=\"Vert Alignment\" value=\"Bottom\" />" ..
        "            <attribute name=\"Texture\" value=\"Texture2D;Textures/TouchInput.png\" />" ..
        "            <attribute name=\"Image Rect\" value=\"96 0 192 96\" />" ..
        "            <attribute name=\"Hover Image Offset\" value=\"0 0\" />" ..
        "            <attribute name=\"Pressed Image Offset\" value=\"0 0\" />" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"Label\" />" ..
        "                <attribute name=\"Horiz Alignment\" value=\"Center\" />" ..
        "                <attribute name=\"Vert Alignment\" value=\"Center\" />" ..
        "                <attribute name=\"Color\" value=\"0 0 0 1\" />" ..
        "                <attribute name=\"Text\" value=\"Obstacles\" />" ..
        "            </element>" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"MouseButtonBinding\" />" ..
        "                <attribute name=\"Text\" value=\"MIDDLE\" />" ..
        "            </element>" ..
        "        </element>" ..
        "    </add>" ..
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/attribute[@name='Is Visible']\" />" ..
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Set</replace>" ..
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]\">" ..
        "        <element type=\"Text\">" ..
        "            <attribute name=\"Name\" value=\"MouseButtonBinding\" />" ..
        "            <attribute name=\"Text\" value=\"LEFT\" />" ..
        "        </element>" ..
        "    </add>" ..
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/attribute[@name='Is Visible']\" />" ..
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Debug</replace>" ..
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]\">" ..
        "        <element type=\"Text\">" ..
        "            <attribute name=\"Name\" value=\"KeyBinding\" />" ..
        "            <attribute name=\"Text\" value=\"SPACE\" />" ..
        "        </element>" ..
        "    </add>" ..
        "</patch>"
end
[/code][/spoiler]

-------------------------

Mike | 2017-01-02 01:05:13 UTC | #51

Currently off-mesh connections can be added post-build with dynamic navMesh, but they must be added before building a static navMesh.
I have a preference for the post-build addition, as it allows using FindNearestPoint(). Maybe same behavior can be applied to static navMesh.

-------------------------

Mike | 2017-01-02 01:05:13 UTC | #52

Thanks Sinoid.

[quote]It works in your Lua code there because the OffMeshConnections are added before Obstacles are added to the scene, which causes tiles to be rebuilt...if adding offmeshconnections at runtime (without changing obstacles) is reliable then there's a bug[/quote]
I've tried to add only a few Obstacles: OffMeshConnections get created only for tiles including an Obstacle, so it is effectively incidental here that OffMeshConnections get created post build (as there are lots of Obstacles, each tile has at least one and get rebuilt, incidentally hooking OffMeshConnections). Fortunately no potential bug here.

For the few boxes non climbable issue, it may be difficult to reproduce as using random positions, I assume the scene might be different from one computer to another. For example when running the AngelScript sample, I only see the texture of a box at start, as a box is created just in front of the camera.

-------------------------

Mike | 2017-01-02 01:05:13 UTC | #53

Currently for moving obstacles in the scene I am removing the component and add it back. Is there a better way to achieve this?

-------------------------

Mike | 2017-01-02 01:05:13 UTC | #54

Maybe we could simply create moving obstacles as agents with very low pushiness.
This way we don't even need physics to push the obstacles.
I'll try this today.

-------------------------

Mike | 2017-01-02 01:05:14 UTC | #55

Works great  :stuck_out_tongue: 
To make an agent strong enough to push another agent, its pushiness must be set to 'high' (as long as other agents don't also have high pushiness).
Here I've added 20 barrels that can be pushed only by the main agent.
And I also tested cloning agents.
EDIT: also added teleportation
EDIT2: also added AnimationController
[spoiler][code]
-- CrowdNavigation example.
-- This sample demonstrates:
--     - Generating a dynamic navigation mesh into the scene
--     - Performing path queries to the navigation mesh
--     - Adding and removing obstacles at runtime from the dynamic mesh
--     - Adding and removing crowd agents at runtime
--     - Raycasting drawable components
--     - Crowd movement management
--     - Accessing crowd agents with the crowd manager
--     - Using off-mesh connections to make boxes climbable
--     - Using agents to simulate pushing obstacles without using physics

require "LuaScripts/Utilities/Sample"

local crowdManager = nil
local agents = {}
local navMesh = nil

function Start()
    -- Execute the common startup for samples
    SampleStart()

    -- Create the scene content
    CreateScene()

    -- Create the UI content
    CreateUI()

    -- Setup the viewport for displaying the scene
    SetupViewport()

    -- Hook up to the frame update and render post-update events
    SubscribeToEvents()
end

function CreateScene()
    scene_ = Scene()
    -- Create octree, use default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
    -- Also create a DebugRenderer component so that we can draw debug geometry
    scene_:CreateComponent("Octree")
    scene_:CreateComponent("DebugRenderer")

    -- Create scene node & StaticModel component for showing a static plane
    local planeNode = scene_:CreateChild("Plane")
    planeNode.scale = Vector3(100.0, 1.0, 100.0)
    local planeObject = planeNode:CreateComponent("StaticModel")
    planeObject.model = cache:GetResource("Model", "Models/Plane.mdl")
    planeObject.material = cache:GetResource("Material", "Materials/StoneTiled.xml")

    -- Create a Zone component for ambient lighting & fog control
    local zoneNode = scene_:CreateChild("Zone")
    local zone = zoneNode:CreateComponent("Zone")
    zone.boundingBox = BoundingBox(-1000.0, 1000.0)
    zone.ambientColor = Color(0.15, 0.15, 0.15)
    zone.fogColor = Color(0.5, 0.5, 0.7)
    zone.fogStart = 100.0
    zone.fogEnd = 300.0

    -- Create a directional light to the world. Enable cascaded shadows on it
    local lightNode = scene_:CreateChild("DirectionalLight")
    lightNode.direction = Vector3(0.6, -1.0, 0.8)
    local light = lightNode:CreateComponent("Light")
    light.lightType = LIGHT_DIRECTIONAL
    light.castShadows = true
    light.shadowBias = BiasParameters(0.00025, 0.5)
    -- Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
    light.shadowCascade = CascadeParameters(10.0, 50.0, 200.0, 0.0, 0.8)

    -- Create randomly sized boxes. If boxes are big enough, make them occluders. Occluders will be software rasterized before
    -- rendering to a low-resolution depth-only buffer to test the objects in the view frustum for visibility
    local boxes = {}
    for i = 1, 20 do
        local boxNode = scene_:CreateChild("Box")
        local size = 1.0 + Random(10.0)
        boxNode.position = Vector3(Random(80.0) - 40.0, size * 0.5, Random(80.0) - 40.0)
        boxNode:SetScale(size)
        local boxObject = boxNode:CreateComponent("StaticModel")
        boxObject.model = cache:GetResource("Model", "Models/Box.mdl")
        boxObject.material = cache:GetResource("Material", "Materials/Stone.xml")
        boxObject.castShadows = true
        if size >= 3.0 then
            boxObject.occluder = true
            table.insert(boxes, boxNode)
        end
    end

    -- Create a DynamicNavigationMesh component to the scene root
    navMesh = scene_:CreateComponent("DynamicNavigationMesh")
    -- Enable drawing debug geometry for obstacles and off-mesh connections
    navMesh.drawObstacles = true
    navMesh.drawOffMeshConnections = true
    -- Set the agent height large enough to exclude the layers under boxes
    navMesh.agentHeight = 10
    -- Set nav mesh tilesize to something reasonable
    navMesh.tileSize = 64
    -- Set nav mesh cell height to minimum (allows agents to be grounded)
    navMesh.cellHeight = 0.05
    -- Create a Navigable component to the scene root. This tags all of the geometry in the scene as being part of the
    -- navigation mesh. By default this is recursive, but the recursion could be turned off from Navigable
    scene_:CreateComponent("Navigable")
    -- Add padding to the navigation mesh in Y-direction so that we can add objects on top of the tallest boxes
    -- in the scene and still update the mesh correctly
    navMesh.padding = Vector3(0.0, 10.0, 0.0)
    -- Now build the navigation geometry. This will take some time. Note that the navigation mesh will prefer to use
    -- physics geometry from the scene nodes, as it often is simpler, but if it can not find any (like in this example)
    -- it will use renderable geometry instead
    navMesh:Build()

    -- Create an off-mesh connection for each box to make it climbable (tiny boxes are skipped).
    -- Note that OffMeshConnections must be added before building the navMesh, but as we are adding Obstacles next, tiles will be automatically rebuilt.
    -- Creating connections post-build here allows us to use FindNearestPoint() to procedurally set accurate positions for the connection
    CreateBoxOffMeshConnections(boxes)

    -- Create a DetourCrowdManager component to the scene root
    crowdManager = scene_:CreateComponent("DetourCrowdManager")

    -- Create some mushrooms as obstacles. Note that obstacles are added onto an already buit navigation mesh
    for i = 1, 100 do
        CreateMushroom(Vector3(Random(90.0) - 45.0, 0.0, Random(90.0) - 45.0))
    end

    -- Create some moving crates. We create them as crowd agents as for moving entities it is less expensive than using obstacles
    CreateMovingBarrels()

    -- Create Jack node as crowd agent
    SpawnJack(Vector3(-5, 0, 20))

    -- Create the camera. Limit far clip distance to match the fog. Note: now we actually create the camera node outside
    -- the scene, because we want it to be unaffected by scene load / save
    cameraNode = Node()
    local camera = cameraNode:CreateComponent("Camera")
    camera.farClip = 300.0

    -- Set an initial position for the camera scene node above the plane
    cameraNode.position = Vector3(0.0, 5.0, 0.0)
    local nodes = scene_:GetChildrenWithComponent("CrowdAgent")
end

function CreateUI()
    -- Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
    -- control the camera, and when visible, it will point the raycast target
    local style = cache:GetResource("XMLFile", "UI/DefaultStyle.xml")
    local cursor = Cursor:new()
    cursor:SetStyleAuto(style)
    ui.cursor = cursor
    -- Set starting position of the cursor at the rendering window center
    cursor:SetPosition(graphics.width / 2, graphics.height / 2)

    -- Construct new Text object, set string to display and font to use
    local instructionText = ui.root:CreateChild("Text")
    instructionText.text = "Use WASD keys to move, RMB to rotate view\n"..
        "LMB to set destination, SHIFT+LMB to spawn a Jack, CTRL+LMB to teleport\n"..
        "MMB to add obstacles or remove obstacles/agents\n"..
        "F5 to save scene, F7 to load\n"..
        "Space to toggle debug geometry"
    instructionText:SetFont(cache:GetResource("Font", "Fonts/Anonymous Pro.ttf"), 12)
    -- The text has multiple rows. Center them in relation to each other
    instructionText.textAlignment = HA_CENTER

    -- Position the text relative to the screen center
    instructionText.horizontalAlignment = HA_CENTER
    instructionText.verticalAlignment = VA_CENTER
    instructionText:SetPosition(0, ui.root.height / 4)
end

function SetupViewport()
    -- Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
    local viewport = Viewport:new(scene_, cameraNode:GetComponent("Camera"))
    renderer:SetViewport(0, viewport)
end

function SubscribeToEvents()
    -- Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent("Update", "HandleUpdate")

    -- Subscribe HandlePostRenderUpdate() function for processing the post-render update event, during which we request
    -- debug geometry
    SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate")

    -- Subscribe HandleCrowdAgentFailure() function for resolving invalidation issues with agents, during which we
    -- use a larger extents for finding a point on the navmesh to fix the agent's position
    SubscribeToEvent("CrowdAgentFailure", "HandleCrowdAgentFailure")
end

function SpawnJack(pos)
    local jackNode = scene_:CreateChild("Jack")
    jackNode.position = pos
    local modelObject = jackNode:CreateComponent("AnimatedModel")
    modelObject.model = cache:GetResource("Model", "Models/Jack.mdl")
    modelObject.material = cache:GetResource("Material", "Materials/Jack.xml")
    modelObject.castShadows = true
    jackNode:CreateComponent("AnimationController")

    -- Create a CrowdAgent component and set its height (use default radius)
    local agent = jackNode:CreateComponent("CrowdAgent")
    agent.height = 2.0
    agent.maxSpeed = 4
    agent.maxAccel = 100
    agents = crowdManager:GetActiveAgents() -- Update agents container
end

function CreateMushroom(pos)
    local mushroomNode = scene_:CreateChild("Mushroom")
    mushroomNode.position = navMesh:FindNearestPoint(pos)
    mushroomNode.rotation = Quaternion(0.0, Random(360.0), 0.0)
    mushroomNode:SetScale(2.0 + Random(0.5))
    local mushroomObject = mushroomNode:CreateComponent("StaticModel")
    mushroomObject.model = cache:GetResource("Model", "Models/Mushroom.mdl")
    mushroomObject.material = cache:GetResource("Material", "Materials/Mushroom.xml")
    mushroomObject.castShadows = true

    -- Create the navigation Obstacle component and set its height & radius proportional to scale
    local obstacle = mushroomNode:CreateComponent("Obstacle")
    obstacle.radius = mushroomNode.scale.x
    obstacle.height = mushroomNode.scale.y
    return mushroomNode
end

function CreateBoxOffMeshConnections(boxes)
    for i, box in ipairs(boxes) do
        local boxPos = box.position
        local boxHalfSize = box.scale.x / 2

        -- Create 2 empty nodes for the start & end points of the connection. Note that order matters only when using one-way/unidirectional connection.
        local connectionStart = scene_:CreateChild("ConnectionStart")
        connectionStart.position = navMesh:FindNearestPoint(boxPos + Vector3(boxHalfSize, -boxHalfSize, 0)) -- Base of box
        local connectionEnd = connectionStart:CreateChild("ConnectionEnd")
        connectionEnd.worldPosition = navMesh:FindNearestPoint(boxPos + Vector3(boxHalfSize, boxHalfSize, 0)) -- Top of box

        -- Create the OffMeshConnection component to one node and link the other node
        local connection = connectionStart:CreateComponent("OffMeshConnection")
        connection.endPoint = connectionEnd
    end
end

function CreateMovingBarrels()
    local barrel = scene_:CreateChild("Barrel")
    local model = barrel:CreateComponent("StaticModel")
    model.model = cache:GetResource("Model", "Models/Cylinder.mdl")
    model.material = cache:GetResource("Material", "Materials/StoneTiled.xml")
    model.material:SetTexture(0, cache:GetResource("Texture2D", "Textures/TerrainDetail2.dds"))
    model.castShadows = true
    barrel:CreateComponent("CrowdAgent")
    for i = 1, 20 do
        local clone = barrel:Clone()
        local size = 0.5 + Random(1)
        clone.scale = Vector3(size/1.5, size*2, size/1.5)
        clone.position = navMesh:FindNearestPoint(Vector3(Random(80.0) - 40.0, size * 0.5 , Random(80.0) - 40.0))
        local agent = clone:GetComponent("CrowdAgent")
        agent.radius = clone.scale.x * 0.5
        agent.height = size
    end
    barrel:Remove()
end

function SetPathPoint()
    local hitPos, hitDrawable = Raycast(250.0)
    local navMesh = scene_:GetComponent("DynamicNavigationMesh")

    if hitDrawable then
        local pathPos = navMesh:FindNearestPoint(hitPos, Vector3.ONE)

        if input:GetQualifierDown(QUAL_SHIFT) then
            -- Spawn a Jack
            SpawnJack(pathPos)

        elseif input:GetQualifierDown(QUAL_CTRL) then
            -- Teleport
            local agent = agents[table.maxn(agents)] -- Get last agent
            if agent.node.name == "Barrel" then return end
            local node = agent.node
            node:LookAt(pathPos) -- Face target
            agent:SetMoveVelocity(Vector3.ZERO) -- Stop agent
            node.position = pathPos
            return

        else
            -- Set target position and init agents' move
            for i, agent in ipairs(agents) do
                if agent.node.name == "Jack" then
                    if i == table.maxn(agents) then
                        -- The last agent will always move to the exact position and is strong enough to push barrels and his siblings
                        agent.navigationPushiness = PUSHINESS_HIGH
                        agent:SetMoveTarget(pathPos)
                    else
                        -- Other agents will move to a random point nearby
                        local targetPos = navMesh:FindNearestPoint(pathPos + Vector3(Random(-4.5, 4.5), 0, Random(-4.5, 4.5)), Vector3.ONE)
                        agent:SetMoveTarget(targetPos)
                    end
                end
            end
        end
    end
end

function AddOrRemoveObject()
    -- Raycast and check if we hit a mushroom node. If yes, remove it, if no, create a new one
    local hitPos, hitDrawable = Raycast(250.0)
    if hitDrawable then

        local hitNode = hitDrawable.node
        if hitNode.name == "Mushroom" then
            hitNode:Remove()
        elseif hitNode.name == "Jack" then
            hitNode:Remove()
            agents = crowdManager:GetActiveAgents() -- Update agents container
        else
            CreateMushroom(hitPos)
        end
    end
end

function Raycast(maxDistance)
    local pos = ui.cursorPosition
    -- Check the cursor is visible and there is no UI element in front of the cursor
    if (not ui.cursor.visible) or (ui:GetElementAt(pos, true) ~= nil) then
        return nil, nil
    end

    local camera = cameraNode:GetComponent("Camera")
    local cameraRay = camera:GetScreenRay(pos.x / graphics.width, pos.y / graphics.height)
    -- Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
    local octree = scene_:GetComponent("Octree")
    local result = octree:RaycastSingle(cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY)
    if result.drawable ~= nil then
        return result.position, result.drawable
    end

    return nil, nil
end

function MoveCamera(timeStep)
    -- Right mouse button controls mouse cursor visibility: hide when pressed
    ui.cursor.visible = not input:GetMouseButtonDown(MOUSEB_RIGHT)

    -- Do not move if the UI has a focused element (the console)
    if ui.focusElement ~= nil then
        return
    end

    -- Movement speed as world units per second
    local MOVE_SPEED = 20.0
    -- Mouse sensitivity as degrees per pixel
    local MOUSE_SENSITIVITY = 0.1

    -- Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
    -- Only move the camera when the cursor is hidden
    if not ui.cursor.visible then
        local mouseMove = input.mouseMove
        yaw = yaw + MOUSE_SENSITIVITY * mouseMove.x
        pitch = pitch + MOUSE_SENSITIVITY * mouseMove.y
        pitch = Clamp(pitch, -90.0, 90.0)

        -- Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
        cameraNode.rotation = Quaternion(pitch, yaw, 0.0)
    end

    -- Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
    if input:GetKeyDown(KEY_W) then
        cameraNode:Translate(Vector3(0.0, 0.0, 1.0) * MOVE_SPEED * timeStep)
    end
    if input:GetKeyDown(KEY_S) then
        cameraNode:Translate(Vector3(0.0, 0.0, -1.0) * MOVE_SPEED * timeStep)
    end
    if input:GetKeyDown(KEY_A) then
        cameraNode:Translate(Vector3(-1.0, 0.0, 0.0) * MOVE_SPEED * timeStep)
    end
    if input:GetKeyDown(KEY_D) then
        cameraNode:Translate(Vector3(1.0, 0.0, 0.0) * MOVE_SPEED * timeStep)
    end
    -- Set destination or spawn a jack with left mouse button
    if input:GetMouseButtonPress(MOUSEB_LEFT) then
        SetPathPoint()
    end
    -- Add new obstacle or remove existing obstacle/agent with middle mouse button
    if input:GetMouseButtonPress(MOUSEB_MIDDLE) then
        AddOrRemoveObject()
    end

    -- Toggle debug geometry with space
    if input:GetKeyPress(KEY_SPACE) then
        drawDebug = not drawDebug
    end

    -- Check for loading/saving the scene from/to the file Data/Scenes/CrowdNavigation.xml relative to the executable directory
    if input:GetKeyPress(KEY_F5) then
        scene_:SaveXML(fileSystem:GetProgramDir().."Data/Scenes/CrowdNavigation.xml")
    end
    if input:GetKeyPress(KEY_F7) then
        scene_:LoadXML(fileSystem:GetProgramDir().."Data/Scenes/CrowdNavigation.xml")
        -- After reload, reacquire crowd manager & agents
        crowdManager = scene_:GetComponent("DetourCrowdManager")
        agents = crowdManager:GetActiveAgents()
    end
end

function HandleUpdate(eventType, eventData)
    -- Take the frame time step, which is stored as a float
    local timeStep = eventData:GetFloat("TimeStep")

    -- Move the camera, scale movement with time step
    MoveCamera(timeStep)

    -- Make the CrowdAgents face the direction of their velocity and play animation
    for i, agent in ipairs(agents) do
        local node = agent.node
        if node.name == "Jack" then
            local animCtrl = node:GetComponent("AnimationController")
            local velocity = agent.actualVelocity
            if velocity:Length() < 0.6 then
                animCtrl:Stop("Models/Jack_Walk.ani", 0.2)
            else
                node.worldDirection = velocity
                animCtrl:PlayExclusive("Models/Jack_Walk.ani", 0, true, 0.2)
                animCtrl:SetSpeed("Models/Jack_Walk.ani", velocity:Length() * 0.3)
            end
        end
    end
end

function HandlePostRenderUpdate(eventType, eventData)
    if drawDebug then
        -- Visualize navigation mesh, obstacles and off-mesh connections
        navMesh:DrawDebugGeometry(true)
        -- Visualize agents' path and position to reach
        crowdManager:DrawDebugGeometry(true)
    end
end

function HandleCrowdAgentFailure(eventType, eventData)
    local node = eventData:GetPtr("Node", "Node")
    local agent = eventData:GetPtr("CrowdAgent", "CrowdAgent")
    local agentState = eventData:GetInt("CrowdAgentState")

    -- If the agent's state is invalid, likely from spawning on the side of a box, find a point in a larger area
    if agentState == CROWD_AGENT_INVALID then
        -- Get a point on the navmesh using more generous extents
        local newPos = navMesh:FindNearestPoint(node.worldPosition, Vector3(5, 5, 5))
        -- Set the new node position, CrowdAgent component will automatically reset the state of the agent
        node:SetWorldPosition(newPos)
    end
end

-- Create XML patch instructions for screen joystick layout specific to this sample app
function GetScreenJoystickPatchString()
    return
        "<patch>" ..
        "    <add sel=\"/element\">" ..
        "        <element type=\"Button\">" ..
        "            <attribute name=\"Name\" value=\"Button3\" />" ..
        "            <attribute name=\"Position\" value=\"-120 -120\" />" ..
        "            <attribute name=\"Size\" value=\"96 96\" />" ..
        "            <attribute name=\"Horiz Alignment\" value=\"Right\" />" ..
        "            <attribute name=\"Vert Alignment\" value=\"Bottom\" />" ..
        "            <attribute name=\"Texture\" value=\"Texture2D;Textures/TouchInput.png\" />" ..
        "            <attribute name=\"Image Rect\" value=\"96 0 192 96\" />" ..
        "            <attribute name=\"Hover Image Offset\" value=\"0 0\" />" ..
        "            <attribute name=\"Pressed Image Offset\" value=\"0 0\" />" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"Label\" />" ..
        "                <attribute name=\"Horiz Alignment\" value=\"Center\" />" ..
        "                <attribute name=\"Vert Alignment\" value=\"Center\" />" ..
        "                <attribute name=\"Color\" value=\"0 0 0 1\" />" ..
        "                <attribute name=\"Text\" value=\"Spawn Jack\" />" ..
        "            </element>" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"KeyBinding\" />" ..
        "                <attribute name=\"Text\" value=\"LSHIFT\" />" ..
        "            </element>" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"MouseButtonBinding\" />" ..
        "                <attribute name=\"Text\" value=\"LEFT\" />" ..
        "            </element>" ..
        "        </element>" ..
        "        <element type=\"Button\">" ..
        "            <attribute name=\"Name\" value=\"Button4\" />" ..
        "            <attribute name=\"Position\" value=\"-120 -12\" />" ..
        "            <attribute name=\"Size\" value=\"96 96\" />" ..
        "            <attribute name=\"Horiz Alignment\" value=\"Right\" />" ..
        "            <attribute name=\"Vert Alignment\" value=\"Bottom\" />" ..
        "            <attribute name=\"Texture\" value=\"Texture2D;Textures/TouchInput.png\" />" ..
        "            <attribute name=\"Image Rect\" value=\"96 0 192 96\" />" ..
        "            <attribute name=\"Hover Image Offset\" value=\"0 0\" />" ..
        "            <attribute name=\"Pressed Image Offset\" value=\"0 0\" />" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"Label\" />" ..
        "                <attribute name=\"Horiz Alignment\" value=\"Center\" />" ..
        "                <attribute name=\"Vert Alignment\" value=\"Center\" />" ..
        "                <attribute name=\"Color\" value=\"0 0 0 1\" />" ..
        "                <attribute name=\"Text\" value=\"Obstacles\" />" ..
        "            </element>" ..
        "            <element type=\"Text\">" ..
        "                <attribute name=\"Name\" value=\"MouseButtonBinding\" />" ..
        "                <attribute name=\"Text\" value=\"MIDDLE\" />" ..
        "            </element>" ..
        "        </element>" ..
        "    </add>" ..
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/attribute[@name='Is Visible']\" />" ..
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Set</replace>" ..
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]\">" ..
        "        <element type=\"Text\">" ..
        "            <attribute name=\"Name\" value=\"MouseButtonBinding\" />" ..
        "            <attribute name=\"Text\" value=\"LEFT\" />" ..
        "        </element>" ..
        "    </add>" ..
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/attribute[@name='Is Visible']\" />" ..
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Debug</replace>" ..
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]\">" ..
        "        <element type=\"Text\">" ..
        "            <attribute name=\"Name\" value=\"KeyBinding\" />" ..
        "            <attribute name=\"Text\" value=\"SPACE\" />" ..
        "        </element>" ..
        "    </add>" ..
        "</patch>"
end

[/code][/spoiler]

-------------------------

Mike | 2017-01-02 01:05:14 UTC | #56

Thanks Sinoid, I've just read your discussion with Mikko. I wasn't aware of the neighbor tile limitation.

Do you think using Agents for moving obstacles, like I did, is a sound approach?

-------------------------

Mike | 2017-01-02 01:05:14 UTC | #57

Perfect! I will clean the sample and push it to master.

-------------------------

Mike | 2017-01-02 01:05:14 UTC | #58

Found the culprit for my issue with some connections unclimbable: as mask and areaID are not set to their default at creation, random values are assigned, making some connections non walkable. Enforcing to defaults, it never fails.

Is it OK to set mask and areaID to their default (1 and 0) at creation of the connection (I can fix this in OffMeshConnection.cpp), or is there a reason to not do so?

-------------------------

Mike | 2017-01-02 01:05:14 UTC | #59

No problem, I'll fix this  :wink: 

Do you think it is possible to automate the tile(s) rebuild when removing a connection?

Not related, I noticed that after creating the DetourCrowdManager component, calling navMesh->Build() segfaults, which prevents from rebuilding the full scene.

-------------------------

Mike | 2017-01-02 01:05:15 UTC | #60

OK, thanks.

-------------------------

Mike | 2017-01-02 01:05:15 UTC | #61

Currently, DetourCrowdManager assumes there's only one navMesh, rooted to scene node (OnNodeSet()). Is this a limitation of DetourCrowd, or can we allow the use of multiple navMeshes that don't belong directly to the scene root? I've tried to use SetNavigationMesh() just after creating the DetourCrowdManager but I still can't add agents to it.

Also, the CreateCrowd() method is public and there exists some bindings for it. Not sure if this is good.

-------------------------

Mike | 2017-01-02 01:05:15 UTC | #62

What I've experimented is:
- create 2 independant navMeshes, not rooted to scene node
- the goal is not to make them communicate, they are 2 separate worlds behaving on their own
- creating a crowd manager fails, which is expected as it can't pick a navMesh, so I used SetNavigationMesh() to 'feed' it with an already built navMesh
- doing so, no agent get added to the crowd manager

[spoiler][code]
require "LuaScripts/Utilities/Sample"

local crowdManager = nil
local agents = {}
local NUM_BARRELS = 0

function Start()
	SampleStart()
	CreateScene()
	CreateUI()
	SubscribeToEvents()
end

function CreateScene()
	scene_ = Scene()
	-- Create octree, use default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
	-- Also create a DebugRenderer component so that we can draw debug geometry
	scene_:CreateComponent("Octree")
	scene_:CreateComponent("DebugRenderer")

	-- ZONE
	local zoneNode = scene_:CreateChild("Zone")
	local zone = zoneNode:CreateComponent("Zone")
	zone.boundingBox = BoundingBox(-1000, 1000)
	zone.ambientColor = Color(0.15, 0.15, 0.15)
	zone.fogColor = Color(0.5, 0.5, 0.7)
	zone.fogStart = 100
	zone.fogEnd = 300

	-- LIGHT
	local lightNode = scene_:CreateChild("DirectionalLight")
	lightNode.direction = Vector3(0.6, -1, 0.8)
	local light = lightNode:CreateComponent("Light")
	light.lightType = LIGHT_DIRECTIONAL
	light.castShadows = true
	light.shadowBias = BiasParameters(0.00025, 0.5)
	-- Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
	light.shadowCascade = CascadeParameters(10, 50, 200, 0, 0.8)

	-- CAMERA
	cameraNode = Node()
	local camera = cameraNode:CreateComponent("Camera")
	camera.farClip = 300
	cameraNode.position = Vector3(0, 5, 0)
	renderer:SetViewport(0, Viewport:new(scene_, camera))

--====================  REGION #1  ==========================
	local region1 = scene_:CreateChild("Region1")
	region1:CreateComponent("Navigable")

	-- FLOOR
	local planeNode = region1:CreateChild("Plane")
	planeNode.scale = Vector3(50, 1, 100)
	planeNode.position = Vector3(26, 0, 0)
	local planeObject = planeNode:CreateComponent("StaticModel")
	planeObject.model = cache:GetResource("Model", "Models/Plane.mdl")
	planeObject.material = cache:GetResource("Material", "Materials/StoneTiled.xml")
	planeNode:CreateComponent("Navigable")

	-- BOX
	local boxes = {}
	for i = 1, 20 do
		local boxNode = region1:CreateChild("Box")
		local size = 1 + Random(8)
		boxNode.position = Vector3(26 + Random(40) - 20, size * 0.5, Random(80) - 40)
		boxNode:SetScale(size)
		local boxObject = boxNode:CreateComponent("StaticModel")
		boxObject.model = cache:GetResource("Model", "Models/Box.mdl")
		boxObject.material = cache:GetResource("Material", "Materials/Stone.xml")
		boxObject.castShadows = true
		if size >= 3 then
			boxObject.occluder = true
			table.insert(boxes, boxNode)
		end
		boxNode:CreateComponent("Navigable")
	end

	-- DynamicNavigationMesh
	local navMesh = region1:CreateComponent("DynamicNavigationMesh")
	navMesh.drawObstacles = true
	navMesh.drawOffMeshConnections = true
	navMesh.agentHeight = 10
	navMesh.cellHeight = 0.05
	navMesh.padding = Vector3(0, 10, 0)
	navMesh:Build()

	-- DetourCrowdManager
	crowdManager = scene_:CreateComponent("DetourCrowdManager")
	crowdManager.navMesh = navMesh

	-- CrowdAgent
	SpawnJack(navMesh, Vector3(5, 0, 20))

--====================  REGION #2  ==========================
	local region2 = scene_:CreateChild("Region2")
	region2:CreateComponent("Navigable")

	-- FLOOR
	local planeNode = region2:CreateChild("Plane")
	planeNode.scale = Vector3(50, 1, 100)
	planeNode.position = Vector3(-26, 0, 0)
	local planeObject = planeNode:CreateComponent("StaticModel")
	planeObject.model = cache:GetResource("Model", "Models/Plane.mdl")
	planeObject.material = cache:GetResource("Material", "Materials/StoneTiled.xml")

	-- BOX
	local boxes = {}
	for i = 1, 20 do
		local boxNode = region2:CreateChild("Box")
		local size = 1 + Random(8)
		boxNode.position = Vector3(-26 + Random(40) - 20, size * 0.5, Random(80) - 40)
		boxNode:SetScale(size)
		local boxObject = boxNode:CreateComponent("StaticModel")
		boxObject.model = cache:GetResource("Model", "Models/Box.mdl")
		boxObject.material = cache:GetResource("Material", "Materials/Stone.xml")
		boxObject.castShadows = true
		if size >= 3 then
			boxObject.occluder = true
			table.insert(boxes, boxNode)
		end
	end

	-- DynamicNavigationMesh
	local navMesh = region2:CreateComponent("DynamicNavigationMesh")
	navMesh.drawObstacles = true
	navMesh.drawOffMeshConnections = true
	navMesh.agentHeight = 10
	navMesh.cellHeight = 0.05
	navMesh.padding = Vector3(0, 10, 0)
	navMesh:Build()

	-- DetourCrowdManager
--	local crowdManager2 = scene_:CreateComponent("DetourCrowdManager")
--	crowdManager2.navigationMesh = navMesh

	-- CrowdAgent
--	SpawnJack(navMesh, Vector3(-5, 0, 20))
end

function CreateUI()
	-- Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
	-- control the camera, and when visible, it will point the raycast target
	local style = cache:GetResource("XMLFile", "UI/DefaultStyle.xml")
	local cursor = Cursor:new()
	cursor:SetStyleAuto(style)
	ui.cursor = cursor
	-- Set starting position of the cursor at the rendering window center
	cursor:SetPosition(graphics.width / 2, graphics.height / 2)
end

function SubscribeToEvents()
	SubscribeToEvent("Update", "HandleUpdate")
end

function SpawnJack(navMesh, pos)
	local jackNode = scene_:CreateChild("Jack")
	jackNode.position = navMesh:FindNearestPoint(pos)
	local modelObject = jackNode:CreateComponent("AnimatedModel")
	modelObject.model = cache:GetResource("Model", "Models/Jack.mdl")
	modelObject.material = cache:GetResource("Material", "Materials/Jack.xml")
	modelObject.castShadows = true
	jackNode:CreateComponent("AnimationController")

	-- Create a CrowdAgent component and set its height and realistic max speed/acceleration. Use default radius
	local agent = jackNode:CreateComponent("CrowdAgent")
	agent.height = 2
	agent.maxSpeed = 4
	agent.maxAccel = 100
	agents = crowdManager:GetActiveAgents() -- Update agents container
	print(#agents)
end

function SetPathPoint()
    local hitPos, hitDrawable = Raycast(250.0)

    if hitDrawable then
		local region = hitDrawable.node.parent
		local navMesh = region:GetComponent("DynamicNavigationMesh")
        local pathPos = navMesh:FindNearestPoint(hitPos, Vector3.ONE)

        if input:GetQualifierDown(QUAL_SHIFT) then
            -- Spawn a Jack
            SpawnJack(navMesh, pathPos)

        elseif input:GetQualifierDown(QUAL_CTRL) and table.maxn(agents) > NUM_BARRELS then
            -- Teleport
            local agent = agents[NUM_BARRELS + 1] -- Get first Jack agent
            local node = agent.node
            node:LookAt(pathPos) -- Face target
            agent:SetMoveVelocity(Vector3.ZERO) -- Stop agent
            node.position = pathPos

        else
            -- Set target position and init agents' move
            for i = NUM_BARRELS + 1, table.maxn(agents) do
                local agent = agents[i]
                if i == NUM_BARRELS + 1 then
                    -- The first Jack agent will always move to the exact position and is strong enough to push barrels and his siblings (no avoidance)
                    agent.navigationPushiness = PUSHINESS_HIGH
                    agent:SetMoveTarget(pathPos)
                else
                    -- Other Jack agents will move to a random point nearby
                    local targetPos = navMesh:FindNearestPoint(pathPos + Vector3(Random(-4.5, 4.5), 0, Random(-4.5, 4.5)), Vector3.ONE)
                    agent:SetMoveTarget(targetPos)
                end
            end
        end
    end
end

function AddOrRemoveObject()
	-- Raycast and check if we hit a mushroom node. If yes, remove it, if no, create a new one
	local hitPos, hitDrawable = Raycast(250)
	if hitDrawable then

		local hitNode = hitDrawable.node
		if hitNode.name == "Mushroom" then
			hitNode:Remove()
		elseif hitNode.name == "Jack" then
			hitNode:Remove()
			agents = crowdManager:GetActiveAgents() -- Update agents container
		else
			CreateMushroom(hitPos)
		end
	end
end

function Raycast(maxDistance)
	local pos = ui.cursorPosition
	-- Check the cursor is visible and there is no UI element in front of the cursor
	if (not ui.cursor.visible) or (ui:GetElementAt(pos, true) ~= nil) then return nil, nil end

	local camera = cameraNode:GetComponent("Camera")
	local cameraRay = camera:GetScreenRay(pos.x / graphics.width, pos.y / graphics.height)
	-- Pick only geometry objects, not eg. zones or lights, only get the first (closest) hit
	local octree = scene_:GetComponent("Octree")
	local result = octree:RaycastSingle(cameraRay, RAY_TRIANGLE, maxDistance, DRAWABLE_GEOMETRY)
	if result.drawable ~= nil then
		return result.position, result.drawable
	end

	return nil, nil
end

function MoveCamera(timeStep)
	-- Right mouse button controls mouse cursor visibility: hide when pressed
	ui.cursor.visible = not input:GetMouseButtonDown(MOUSEB_RIGHT)

	-- Do not move if the UI has a focused element (the console)
	if ui.focusElement ~= nil then
		return
	end

	-- Movement speed as world units per second
	local MOVE_SPEED = 20
	-- Mouse sensitivity as degrees per pixel
	local MOUSE_SENSITIVITY = 0.1

	-- Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
	-- Only move the camera when the cursor is hidden
	if not ui.cursor.visible then
		local mouseMove = input.mouseMove
		yaw = yaw + MOUSE_SENSITIVITY * mouseMove.x
		pitch = pitch + MOUSE_SENSITIVITY * mouseMove.y
		pitch = Clamp(pitch, -90, 90)

		-- Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
		cameraNode.rotation = Quaternion(pitch, yaw, 0)
	end

	-- Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
	if input:GetKeyDown(KEY_W) then cameraNode:Translate(Vector3(0, 0, 1) * MOVE_SPEED * timeStep) end
	if input:GetKeyDown(KEY_S) then cameraNode:Translate(Vector3(0, 0, -1) * MOVE_SPEED * timeStep) end
	if input:GetKeyDown(KEY_A) then cameraNode:Translate(Vector3(-1, 0, 0) * MOVE_SPEED * timeStep) end
	if input:GetKeyDown(KEY_D) then cameraNode:Translate(Vector3(1, 0, 0) * MOVE_SPEED * timeStep) end

	-- Set destination or spawn a jack with left mouse button
	if input:GetMouseButtonPress(MOUSEB_LEFT) then
		SetPathPoint()
	end
	-- Add new obstacle or remove existing obstacle/agent with middle mouse button
	if input:GetMouseButtonPress(MOUSEB_MIDDLE) then
		AddOrRemoveObject()
	end

	-- Check for loading/saving the scene from/to the file Data/Scenes/CrowdNavigation.xml relative to the executable directory
	if input:GetKeyPress(KEY_F5) then
		scene_:SaveXML(fileSystem:GetProgramDir().."Data/Scenes/CrowdNavigation.xml")
	end
	if input:GetKeyPress(KEY_F7) then
		scene_:LoadXML(fileSystem:GetProgramDir().."Data/Scenes/CrowdNavigation.xml")
		-- After reload, reacquire crowd manager & agents
		crowdManager = scene_:GetComponent("DetourCrowdManager")
		agents = crowdManager:GetActiveAgents()
	end

	-- Toggle debug geometry with space
	if input:GetKeyPress(KEY_SPACE) then
		drawDebug = not drawDebug
	end
end

function HandleUpdate(eventType, eventData)
	-- Move the camera, scale movement with time step
	MoveCamera(eventData:GetFloat("TimeStep"))

	-- Make the CrowdAgents face the direction of their velocity and update animation
	for i, agent in ipairs(agents) do
		local node = agent.node
		if node.name == "Jack" then
			local animCtrl = node:GetComponent("AnimationController")
			local velocity = agent.actualVelocity
			if velocity:Length() < 0.6 then
				animCtrl:Stop("Models/Jack_Walk.ani", 0.2)
			else
				node.worldDirection = velocity
				animCtrl:PlayExclusive("Models/Jack_Walk.ani", 0, true, 0.2)
				animCtrl:SetSpeed("Models/Jack_Walk.ani", velocity:Length() * 0.3)
			end
		end
	end
end
[/code][/spoiler]

-------------------------

Mike | 2017-01-02 01:05:16 UTC | #63

Thanks, I must admit that this experiment is more to test the limits than for real-life practice, so it may not be worth investigating further.

-------------------------

weitjong | 2017-01-02 01:05:17 UTC | #64

I am too experimenting with this sample lately. I have increased the number of "moving barrels" from 20 to 200 and spawned a few dozens of Jacks to walk around. In this scenario, one could observe easily a number of Jacks simply do not able to reach their targets due to the barrels on their paths. It is unexpected because they know how to walk around obstacles, yet they are easily stopped by the barrels as they are "too polite" to wait for barrels to clear the way which of course the barrels don't. Currently only the pilot Jack is strong enough to throw its weight to push the barrels around. Long story short, setting the navigation pushiness to "high" to all the Jacks solves the problem so they can clear the paths by themselves. However, this creates yet another problem. The "high" setting makes Jacks do not play nice with each other. I have spent quite some time to tweak the settings but I could not get the result I desire. Basically, all jacks can push barrels but play nice by avoiding each other (instead of pushing each other). May be I have missed out some other settings. Anyone know how to achieve this?

-------------------------

weitjong | 2017-01-02 01:05:18 UTC | #65

[quote="Sinoid"][quote]May be I have missed out some other settings.[/quote]

Nope, there isn't a whole lot there - big black box.

To explain pushiness: as pushiness increases the agent's "pending collision range" and separation space it likes between itself and others decreases. A less pushy agent stays further away and avoids sooner. A pushier agent practically runs everyone over, forcing less pushy agents away because their separation space has been violated.[/quote]
Thanks for the reply. Yes, I have understood that much. I could almost conclude myself that it is not possible to achieve what I desire with the current crowd agent setup alone. As it is, the "pushiness" or "niceness" of the crowd agent is an absolute setting instead of relative one. That is, it does not know how to handle the other agents differently based on their own "weight", which is a pity. To me, it appears that the only way to achieve my desired effect is to use the Physics proper.

-------------------------

franck22000 | 2017-01-02 01:05:18 UTC | #66

In my old engine i was using recast and i was using navmesh obstacles for dealing wit obstacles. Why it is not possible on the current implementation ? :slight_smile: 

[video]https://www.youtube.com/watch?v=EXQuJvMiY-o[/video]

-------------------------

weitjong | 2017-01-02 01:05:18 UTC | #67

I believe you have missed the point of what the barrel in the sample is trying to emulate. If we use the actual "obstacle" to implement the barrel and partially rebuild the nav mesh when it has moved then there should be also no problem with our current implementation. The sample intentionally uses the "crowd agent" to implement the barrel to simulate a "moving obstacle" to avoid the cost of rebuilding the nav mesh. And this is where the problem begins.

-------------------------

franck22000 | 2017-01-02 01:05:18 UTC | #68

Alright weitjong now i see :slight_smile:

-------------------------

Mike | 2017-01-02 01:05:19 UTC | #69

@ weitjong, did you try with low pushiness (or medium) + low navigation quality for agents?

-------------------------

weitjong | 2017-01-02 01:05:19 UTC | #70

[quote="Mike"]@ weitjong, did you try with low pushiness (or medium) + low navigation quality for agents?[/quote]
I think I have tried all the combinations of pushiness setting that make sense but none work. I have not tried to modify the navigation quality though. However, as per explanation from Sinod and also from my experiment observation, it is simply not possible to do with crowd agent alone due to agent pushiness setting cannot be set relatively, say, Jack to another Jack is "medium" and Jack to another barrel is "high", or something like that.

I have almost complete experimenting with the sample. I have also made changes and bug fixes in the DetourCrowd implementation classes along the way. There is one more thing I observed that looks strange to me. When an agent reaches its target, a target "arrived" state change event is fired. This is expected. However, somehow it will be followed by yet another agent reposition and target "valid" state change events before everything comes to a full stop. To me, these reposition and target "valid" state change event should not have occurred and that the target "arrived" should be the last event. @Sinoid, do you know why it happens and can it be prevented? In my revised sample, I plan to use the target "arrived" event to stop the walking animation. Currently it does not work well because the following "bogus" reposition event starts the animation again immediately after.

-------------------------

weitjong | 2017-01-02 01:05:19 UTC | #71

Thanks for the quick reply. I will take a closer look at that GetTargetState() function again tomorrow. I was (still am) kind of lost with the "corner" thingy earlier. It is quite late here already. Stopping the animation correctly is the last thing I want to do before committing my patch. You can go ahead to push yours.

-------------------------

weitjong | 2017-01-02 01:05:20 UTC | #72

I have just pushed my patch to master branch. @Sinoid, feel free to revert back any of the changes.

I am this close to remove the barrel agents for emulating the moving obstacles as they don't work as expected with any combination of the pushiness I have tried. I also feel that it does not fit the purpose of the sample to demonstrate a proper usage of the CrowdAgent class. Anyway, that is only my opinion so in the end I just leave them untouched in the sample.

While refactoring the DetourCrowd implementation, I notice that a few setter methods call MarkNetworkUpdate(), however, there are no corresponding network attribute to be propagated remotely. I don't have the time to clean up those yet. I think they should either have the network attribute added or just remove the call if the network attribute does not make sense for the specific setter method.

-------------------------

weitjong | 2017-01-02 01:05:23 UTC | #73

Just a head up. I am still in refactoring mode or mood, so expect more changes to come. Although I agree with you that we have to be careful not to flood the network when agents are being updated, we should also at the same time keep all the crowd managers in the network to update the crowd agents in a deterministic way. So, IMHO, in order to achieve this then all the agent's attributes and parameters must be in sync across the network.

I have a few questions (not related to the above). It looks to me there may be a copy-paste error here. [github.com/urho3d/Urho3D/blob/m ... #L343-L373](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Navigation/DetourCrowdManager.cpp#L343-L373). I have to admit I have no experience with DetourCrowd before so I don't know what is the sensible settings for low, medium, and high navigation quality. I suppose the "obstacleAvoidanceType" setting should be different in each case. At the moment it always stays at 3 (because it is also initialized to 3 when the agent is added initially). Line 355 appears to be redundant. And with that line removed then the "updateFlags" is effectively the same between low and medium[?]

-------------------------

weitjong | 2017-01-02 01:05:24 UTC | #74

Thanks for your insight. It would be good to hear from the original author also. Aside from the apparently copy-paste error, there may be a good reason why the flags are being set as they are now. Why the DT_CROWD_SEPARATION flag is not set in the "high" setting, but effectively DT_CROWD_SEPARATION flag is the only remaining after the bitwise flip for the "low" and "medium". If I could do it my way then I would probably set the flags for "low", "medium", and "high" based on the amount of CPU processing they require (see DetourCrowd::Update() implementation). Something like this.

[code]
        if (scope & SCOPE_NAVIGATION_QUALITY_PARAMS)
        {
            switch (navQuality_)
            {
            case NAVIGATIONQUALITY_LOW:
                params.updateFlags = 0
                    | DT_CROWD_OPTIMIZE_VIS
                    | DT_CROWD_ANTICIPATE_TURNS;
                break;

            case NAVIGATIONQUALITY_MEDIUM:
                params.updateFlags = 0
                    | DT_CROWD_OPTIMIZE_TOPO
                    | DT_CROWD_OPTIMIZE_VIS
                    | DT_CROWD_ANTICIPATE_TURNS
                    | DT_CROWD_SEPARATION;
                break;

            case NAVIGATIONQUALITY_HIGH:
                params.obstacleAvoidanceType = 3;
                params.updateFlags = 0
                    // Path finding
                    | DT_CROWD_OPTIMIZE_TOPO
                    | DT_CROWD_OPTIMIZE_VIS
                    // Steering
                    | DT_CROWD_ANTICIPATE_TURNS
                    | DT_CROWD_SEPARATION
                    // Velocity planning
                    | DT_CROWD_OBSTACLE_AVOIDANCE;
                break;
            }
        }
[/code]
But then again, as I said I have no past experience to justify any of this. The "obstacleAvoidanceType" setting is really only required for the last case as only there the "DT_CROWD_OBSTACLE_AVOIDANCE" flag is set. I think it should be made as a standalone attribute/property so it can be set/get separately instead of always hardcoding it to type 3.

-------------------------

weitjong | 2017-01-02 01:05:26 UTC | #75

I have created another branch for the refactoring work. Reason being, the changes break a few of the APIs. The params.updateFlags switch cases is now modified to what I have proposed in my earlier post. Please shout early when any of you don't like where the new branch is heading.

Today I find yet another discrepancy between what is expected by NavigationMesh component class and (Detour)CrowdManager component class. From what I understand, the former expects to receive and return position in world coordinate, while the latter expects them in local coordinate. More precisely, the latter assumes the local and world coordinates are to be the same because it always assume the dtCrowd is initialized with navmesh parented to root scene node. I find it a little bit disturbing. Should we not making that assumption and always perform the world <-> local coordinate conversion in the CrowdManager/CrowdAgent components? It will make it easier should we later decide to support navmesh to be parented in any node. Actually this point has been brought up by Mike earlier. Are there any practicality in supporting multiple (disconnected) navmeshes in a single scene hierarchy?

-------------------------

cadaver | 2017-01-02 01:05:26 UTC | #76

I originally wrote the basic NavigationMesh to take into account that it might not be in the scene root, and might not have zero origin, so doing the same for CrowdManager would be logical. There may be an issue how the crowdmanager will find the navmesh if not in scene root, and likewise how the agents will find the crowdmanager if not in scene root, though.

-------------------------

thebluefish | 2017-01-02 01:05:27 UTC | #77

Well say I wanted 8 different, completely unrelated crowds. Right now it doesn't seem like that would be possible because we're limited to one CrowdManager.

Simplest idea is to have the agents check its parent, its parent's parent, etc... up the tree until it finds a parent with a CrowdManager component, then use that. Alternatively have an Attribute with a Node ID or Component ID.

-------------------------

weitjong | 2017-01-02 01:05:27 UTC | #78

[quote="Sinoid"]Ah, local/world space. NavAreas are wrong, both in debug visualization and marking in the navigation mesh. DebugDraw has to be relative to the space of the navmesh as the bounds has to be an AABB relative to the dtNavMesh.[/quote]
I cannot decide which is more important to do first. Supporting navmesh in any node or fixing those coordinate space conversion first? If a navmesh can be made to attach to a transformed node then it will be easy to spot the coordinate space mistake. On the other hand, I am still not sure whether there is any valid use cases for (multiple) navmesh attached to any node, but probably it is easier to justify to have a single navmesh attached to a non-scene node. The problem of searching the correct navmesh (should we have more than one in the scene hierarchy) is a solvable one though. I think it is understandable that multiple navmesh support requires multiple dtCrowd objects (probably still being managed by one CrowdManager class).

[quote="Sinoid"]Who belongs to which NavigationMesh? As in navigables, obstacles, and navareas. Just those beneath it in the scene tree from the mesh?[/quote]
Yes, that is the most sensible way to do it. So, if an application had chosen to attach the navmesh in the scene node then the navmesh would be built using all the components beneath the scene node similar to what we have now. No surprises.

[quote="thebluefish"]Well say I wanted 8 different, completely unrelated crowds. Right now it doesn't seem like that would be possible because we're limited to one CrowdManager.[/quote]
Aside from memory footprint problem pointed by Sinoid, I don't agree this is a valid reason or use case for having multiple navmesh. I could be wrong but from the context, I think you meant to say "8 crowds moving to 8 different target positions (from a same navmesh)". If so then that is doable now with current implementation. The dtCrowd just simulates the crowd movement. It does not really care much where each agent is going or whether they are going in flock.

-------------------------

weitjong | 2017-01-02 01:05:50 UTC | #79

@Sinoid. Thanks for the offer. My refactoring was abruptly disrupted by my attempt to switch IDE from Eclipse to CLion. In the process I had to side track to perform yet another refactoring to make our code base plays nice with CLion. I will attempt to rebase the refactor-crowd branch when I have time later to bring it up to speed. I am sorry that I could not give you any notes as I am not sure myself where I have left off last time.  :wink:  But I do have local commit that I haven't pushed and some unfinished work in git stash.

-------------------------

weitjong | 2017-01-02 01:05:56 UTC | #80

The refactor-crowd branch is now rebased and reformat to match what we have in the master branch. Be my guest to send PR against it (or you can probably write to Lasse to become Urho3D team member and grant you direct push privilege). I think I remember now where I left it. I think I want to make the navMesh to be auto-discovered in the scene hierarchy, i.e. freeing it from the assumption that it is direct child of root scene node. As such, the component(s) need to perform world <--> local coordinate space transformation as necessary. I also intend to clean up the classes as necessary and to make them better integrate with the Scene Editor. I think I am only done doing that for CrowdAgent and CrowdManager class. The changes are not necessarily backward compatible. I will continue to work on this branch when I have time.

-------------------------

weitjong | 2017-01-02 01:06:28 UTC | #81

@cadaver, any objection to merge this branch in as it is? Although the refactoring work to make the navMesh auto-discovered in the scene hierarchy with world <--> local coordinate space transformation has not been completed yet, some of the work to improve the attribute editing for the CrowdAgent & CrowdManager in Editor should be valuable enough to be merged for earlier testing. As mentioned before, some of the changes are not backward compatible. But at the very least, as it is now the branch is at a nice logical break point where early merge does not break the build and the crowd navigation demo still runs. This way, I don't need to keep rebasing it.

-------------------------

cadaver | 2017-01-02 01:06:28 UTC | #82

No objections.

-------------------------

Mike | 2017-01-02 01:06:46 UTC | #83

Seems that NavigationMesh::GetRandomPoint() no longer works in script (always returns a Vector3::ZERO).
This is certainly due to the Detour parameters of the function (dtQueryFilter and dtPolyRef).

-------------------------

weitjong | 2017-01-02 01:06:46 UTC | #84

I am not able to reproduce your problem using Lua script. Both the NavigationMesh::GetRandomPoint() and CrowdManager::GetRandomPoint() are tested. Are you mixing up the usage between these two? The latter requires a "queryFilterType" argument.

-------------------------

Mike | 2017-01-02 01:06:46 UTC | #85

Thanks, I'm using NavigationMesh::GetRandomPoint() with AngelScript.

-------------------------

weitjong | 2017-01-02 01:06:47 UTC | #86

I am using 39_CrowdNavigation.as to test. Replacing the GetRandomPointInCircle() with GetRandomPoint(). Also called the navmesh version instead of crowdmanager version. They work as expected. I am using the latest master branch revision. I am testing using Linux platform as always. Both the Lua and AngelScript bindings rely on the fact that dtQueryFilter* and dtPolyRef* parameters will be defaulted to 0. I think I have done enough regression test before making that change while the code were still in the refactoring branch. I would be surprised if the same code runs differently on other target platforms though.

-------------------------

Mike | 2017-01-02 01:06:47 UTC | #87

EDIT: has been fixed by this [url=https://github.com/urho3d/Urho3D/commit/ae0544291afb5a01e26ecc6429c161515aeb8375]commit[/url].

-------------------------

