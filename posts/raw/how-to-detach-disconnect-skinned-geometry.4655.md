lhlvieira | 2018-11-07 21:10:45 UTC | #1

Hello there,
I am trying to create a dismemberment effect for a zombie game. Let's use the ragdoll sample for reference. I have successfully detached 2 bones (simply used 'Enabled = false' on a constraint). Problem: the mesh follows the bones around, stretching itself to them. This is obviously expected to happen. So, how could I prevent this ?

Well, I think the solution lies in modifying a bone's influence on the vertices and then detaching some vertices, but...
1- Is it even possible to edit a model's mesh at runtime ?
2- Is it possible to access the vertices a bone has influence to and modify them, specifically bone weights ?

-------------------------

orefkov | 2018-11-07 21:29:54 UTC | #2

Imho, personally, I would just prepare two different models in advance, at design time, with different weights. And at the moment of dismemberment simply replaced one model with another.
Although, of course, nothing prevents you from creating a copy of the vertex buffer at run time, changing the weights during copying, and then assigning a new vertex buffer to the geometry.

-------------------------

Sinoid | 2018-11-07 21:52:13 UTC | #3

[quote="lhlvieira, post:1, topic:4655"]
1- Is it even possible to edit a model’s mesh at runtime ?
[/quote]

Yes, but you're not going to want to.

> 2- Is it possible to access the vertices a bone has influence to and modify them, specifically bone weights ?

Yes, but you're not going to want to.

> How to detach/disconnect skinned geometry

You can realistically (in Urho3D) only do this if you're separating distinct geometries from an aggregate model, such as multiple AnimatedModel's attached to a master.

---

You cannot trivially piece-meal an arbitrary mesh.

0) Make a whole ton of models and swap them
    - Only even remotely viable if you use 3dsMax, the modifier stack can actually cope with some crazy trees of edits

1) CSG is tempting, don't waste your time
    - you have to deal with vertex-attributes, which are non-trivial and most changes you'll want to do will involve such
    - fake CSG can work (discard triangles and close the open-loop)
        - stupid when the options below exist (open-loop finding is hard)
    - have to isolate *floating* geometries (from severing) into discrete meshes and then fit a physics collider to them in a tight time-span
        - CSG on organics is stupid slow, it's much faster on inorganics which are less tri-soupy

2) The easiest approach will be to scale the the joint at the severing point to 0 (which will collapse all geometry weighted to it or downstream to nothing) then spawning a *severed-limb* with the orientation of the severed joint had and then adding a *gore-flower* at the point the joint collapsed down to.
    - Not very granular though
    - Not sure if it ended up there in the end but that approach was used early on in the new Doom, there's 3 variations of a paper on that - all behind pay-walls though (1 book, 2 acad).

3) Roll a custom exporter and write out a crap-load of different combinations of index-buffers. The old Ghoul2 system worked this way by changing the indices drawn, all vertex data was always present and gore just changed what the triangle layout was.
    - Again, you have to spawn stuff (limb parts, gore-flowers, etc)

4) Valve's Left4Dead2 slides are easy to find, they're shader based though and they'll make a mess of batching (though animated models already do that ... so not a ton of loss).
    - You still have to spawn stuff (limb parts, gore-flowers, etc)

5) No, you can't really use bullet softbodies for this

6) Morph targets and texture swaps are plenty for superficial gore, and complementary to anything else

---

Realistically you're going to have to make use of a whole bunch of different things.

I'm trying out a combination of Ghoul2-esque index swapping, morph-targets, Left4Dead2's ellipsoid method, and prefab scenes for spawn-lists. I was previously using too much CSG and that was a waste of time, now I've moved to just using volume selections to filter triangles and then fill the open-loops for a base geo. Though my gore requirements are closer to MK than a zombie game.

-------------------------

lhlvieira | 2018-11-07 23:23:10 UTC | #4

[quote="orefkov, post:2, topic:4655, full:true"]
Imho, personally, I would just prepare two different models in advance, at design time, with different weights. And at the moment of dismemberment simply replaced one model with another.
Although, of course, nothing prevents you from creating a copy of the vertex buffer at run time, changing the weights during copying, and then assigning a new vertex buffer to the geometry.
[/quote]
I have thought of that method too, but it is really inefficient in my opinion. Imagine having to create all sorts of variations for every zombie model in the game. I think Chivalry Medieval Warfare used this approach, but in their case, it is rather ok due to low amount of models in the game.

EDIT 1: Added quotes
EDIT 2: Added game reference

-------------------------

orefkov | 2018-11-07 22:38:31 UTC | #5

Only one additional model for every zombie model. Just copy of usual model, but for vertexes leave only one weight, every vertex leave linked only to one bone. And loop cut vertex groups one from another. After it you can subst model and move bones in any way.
And still it would be possible to add morph animation of different injuries for each limb.

-------------------------

lhlvieira | 2018-11-07 23:21:01 UTC | #6

[quote="Sinoid, post:3, topic:4655"]
Make a whole ton of models and swap them
[/quote]
Similiar to orefkov ideal I think, but yeah, I thought of this approach too but meh, really bad in opinion, I cant imagine myself creating every variation by hand. If I am not mistaken, Chivalry Medieval Warfare used something similar to this.

[quote="Sinoid, post:3, topic:4655"]
CSG is tempting, don’t waste your time
[/quote]
You mean performing boolean operations and all that ? Not gonna lie, such system would be perfect for gore games, but if I am not mistaken, the mesh has to be water-tight and non-self-intersecting, and that is a nono already. Can't even imagine how complicated must to even implement it.
I actually have this pending idea/project in my mind of implementing an object slicer (which I believe would be easier than CSG), inspired on the one in Shadow Warrior 2. Slicing the object itself is probably easy, the biggest problem is doing that to an actual skinned and ragdolled object.

[quote="Sinoid, post:3, topic:4655"]
The easiest approach will be to scale the the joint at the severing point to 0 (which will collapse all geometry weighted to it or downstream to nothing) then spawning a *severed-limb* with the orientation of the severed joint had and then adding a *gore-flower* at the point the joint collapsed down to.
[/quote]
I also thought of that, but I see this approach as a hack more than anything else. I have seen this technique being used in some games, cant remember which though. Actually, one day I almost made a Skyrim mod that would utilize this idea of shrinking to 0, I've never finished the mod though.

[quote="Sinoid, post:3, topic:4655"]
Roll a custom exporter and write out a crap-load of different combinations of index-buffers. The old Ghoul2 system worked this way by changing the indices drawn, all vertex data was always present and gore just changed what the triangle layout was.
[/quote]
I think I don't fully understand the idea. You mean I could have multiple geometries in one place, but choose which one to render ? Is it similiar to Fallout 3's approach ? Where artist had to define the vertices that could get removed, and also manually place the _gore-caps_ ?.

[quote="Sinoid, post:3, topic:4655"]
Valve’s Left4Dead2 slides are easy to find, they’re shader based though and they’ll make a mess of batching (though animated models already do that … so not a ton of loss).
[/quote]
This is the best gore method I know of, it is really modular, and if done right it works with every model in the game. I have seen this approach being used in MK9 and X, Dying Light and Shadow Warrior too. I noted it has a small disadvantage though, since pixels get 'dicarded', no actual geometry gets disconnect from the mesh, meaning you probably will have to spawn a generic limb.

[quote="Sinoid, post:3, topic:4655"]
No, you can’t really use bullet softbodies for this
[/quote]
I figured. I don't plan to make a boobs game :joy:.

[quote="Sinoid, post:3, topic:4655"]
Realistically you’re going to have to make use of a whole bunch of different things.

I’m trying out a combination of Ghoul2-esque index swapping, morph-targets, Left4Dead2’s ellipsoid method, and prefab scenes for spawn-lists. I was previously using too much CSG and that was a waste of time, now I’ve moved to just using volume selections to filter triangles and then fill the open-loops for a base geo. Though my gore requirements are closer to MK than a zombie game.
[/quote]
Nice, good luck in your journey. Truth is, I am a noob at programming, I started out recently so I have all this ideas in my head but I cant really do the maths and codes to get them working. Plus, I am actually using UrhoSharp because its noob-friendlier.

-------------------------

lhlvieira | 2018-11-07 23:43:52 UTC | #7

[quote="orefkov, post:5, topic:4655, full:true"]
Only one additional model for every zombie model. Just copy of usual model, but for vertexes leave only one weight, every vertex leave linked only to one bone. And loop cut vertex groups one from another. After it you can subst model and move bones in any way.
And still it would be possible to add morph animation of different injuries for each limb.
[/quote]

Ok help me understand your idea. Correct me if I am wrong, you are saying to:
1- At design time, create a second model that has only 1 bone weight per vertex OR at runtime copy vertex-buffer and modify its vertices-weight to only 1 bone.
2- Loop cut vertex groups <-- this I dont quite understand. Do you mean I should separate/cut/slice the vertices per bone ? So I could have, like, one vertex-buffer/geometry per character limb ?

-------------------------

orefkov | 2018-11-08 07:15:30 UTC | #8

I record small video how I make it in Blender on the example of the left hand.
https://youtu.be/UmaSabmIHls

First I make copy of mesh.
Then select left arm part of mesh and separate it to different mesh.
In new mesh all vertexes add to group "lowerarm_l" and remove from others groups.
In old mesh (without left arm) - select vertices from lowerarm_l group and remove it from that group.
After I join two meshes back to one and export old mesh and new copy.
In editor create two AnimatedModel componen on one node.
For first component set usual model, for second - new model.
And then move the lowerarm_l node, alternately setting models enabled.

In principle, this process can be automated, and you can write a script for the Blender or right in Urho3D. However, you need to know for which vertices and by how mach you need to change weights.

Although now I thought - in the detachable hand it was possible not to change all the weights, it was enough to exclude the vertices from the group of the upperarm_l, and in the remaining body to exclude the vertices from the group of lowerarm_l.

The main problem is that the vertices in the place where the lowarm and the upperarm are connected must be doubled, as they initially belong to both groups, but in order for the model to break when the dismemberment occurs, there must be two vertices - one remains in one part , the other - in the other. That's what I meant by the "loop cut"

Thus, it is possible to prepare a single model, divided into several parts, and use this model to implement the dismemberment effect.
You can also add several different morph animations to this new model.

Imho - best way create script for Blender, where you just select loop edge, where you need divide model, and script will do the rest.

-------------------------

orefkov | 2018-11-08 08:04:38 UTC | #9

Also I record process of adding shape keys in Blender for that model.
Then, in the game, in each specific case of separating a part of the body, you can set a random set of values for these keys in order to give individuality to each case and avoid sameness.
https://youtu.be/U1Bkc0XWfkU

Well, for all that beauty, you need to create polygons at the point of separation in this model to close the hole. Well, apply on them a blood-meat texture, well, or whatever happens in a zombie. And add the particle effect of course.

-------------------------

fnadalt | 2018-11-08 11:23:10 UTC | #10

Panda3D uses this approach:
https://www.panda3d.org/manual/index.php/Multi-Part_Actors

-------------------------

orefkov | 2018-11-08 11:52:48 UTC | #11

This is not a little for that. In Urho3D, you can also manage several models tied to individual bones of a skeleton with a single master skeleton.
If you use this mechanism, you still need to prepare several models in advance, each separately for the part of the body to be separated.

-------------------------

Sinoid | 2018-11-08 21:03:38 UTC | #12

@orefkov, you do know that Blender has arbitrary vertex-groups right? You can setup vertex groups and write a script to go through all of them based on naming convention, fill holes, chart the hole-fill faces, and dump the fill info like the edges and centroid (for flowers/caps/particle emitters) to read.

Unfortunately Blender's shoddy FBX export doesn't write groups into FBX selection-sets like it should.

-------------------------

lhlvieira | 2018-11-08 21:34:36 UTC | #13

Nice video, I understand you now. I still think it is is similar to Chivalry, when a model gets dismembered devs replace it with a 2nd model that have disconnected limbs. It is a rather good approach, but I really wanted to do that at runtime instead of setting everything up in blender like that.

I am gonna study Urho capabilities deeper and initially try 2 approaches:

1- At model creation, separate mesh into geometries for each dismember-able limb. Similar to Fallout 3 engine, where artists had to highlight/select which vertices could get dismembered. And then, with code, try some tricks to get the geometry to detach from the model.

2- Instead of dealing with geometries, I could also just use a bone-weight information of vertex and do what you did in Blender with code instead. I think this approach would be better, but I haven't wrapped my head around it yet.

-------------------------

orefkov | 2018-11-09 06:22:21 UTC | #14

[quote="lhlvieira, post:13, topic:4655"]
but I really wanted to do that at runtime instead of setting everything up in blender like that
[/quote]

Clear. It's just that my main use is mobile games, and for performance I profess the principle - everything that can be calculated in advance - should be calculated in advance.
Then I can offer another such idea.
You can create own version of the shader for drawing, in which the parameter will be worked out - which part of the model to draw and which not.
similar like this
https://www.youtube.com/watch?v=SmR_Xa-_Cgs
There is topic about it - https://discourse.urho3d.io/t/models-dissolving-like-doom-3/1625

At the moment of dismemberment, add the second model - a duplicate of the first. Both assign this shader, for one model we ask to draw one part, for another - another.
Bonus - you will be able to portray the tearing of a zombie anywhere, not only along the joints :)

-------------------------

lhlvieira | 2018-12-04 01:46:48 UTC | #15

Just to show off what I came up with.  See it as a poor proof of concept:

Things to note:
- It is a hack, it has bugs, it is slow and therefore should not be used in production, at least not the way I implemented it. 
- The good thing about it is that it is pretty scalable technique and doesn't need any mesh setup, and it can probably work with any skeleton you throw at it.
- It will kill draw calls because each detached limb is a separate AnimatedModel.
- The code is a mess, sorry, so don't try to understand it just run it.
- Decals disabled.
- Left mouse throws ball, Right mouse dismembers.
- Dismember only occurs when ragdoll is on.

!!! VIRTUAL GORE AHEAD !!!
[spoiler]![deadJack1|690x471](upload://jimm2SMA0lrAp6mhemCgsqcijwv.png) ![deadJack2|690x482](upload://aWlEF4VBl2IlFbgLV6YQfbKxnp3.png)[/spoiler]

LUA Code:

    require "LuaScripts/Utilities/Sample"

    function Start()
        cache.autoReloadResources = true
        -- Execute the common startup for samples
        SampleStart()

        -- Create the scene content
        CreateScene()

        -- Create the UI content
        CreateInstructions()

        -- Setup the viewport for displaying the scene
        SetupViewport()

        -- Set the mouse mode to use in the sample
        SampleInitMouseMode(MM_RELATIVE)

        -- Hook up to the frame update and render post-update events
        SubscribeToEvents()
    end

    function CreateScene()
        scene_ = Scene()

        -- Create octree, use default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
        -- Create a physics simulation world with default parameters, which will update at 60fps. Like the Octree must
        -- exist before creating drawable components, the PhysicsWorld must exist before creating physics components.
        -- Finally, create a DebugRenderer component so that we can draw physics debug geometry
        scene_:CreateComponent("Octree")
        scene_:CreateComponent("PhysicsWorld")
        scene_:CreateComponent("DebugRenderer")

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

        -- Create a floor object, 500 x 500 world units. Adjust position so that the ground is at zero Y
        local floorNode = scene_:CreateChild("Floor")
        floorNode.position = Vector3(0.0, -0.5, 0.0)
        floorNode.scale = Vector3(500.0, 1.0, 500.0)
        local floorObject = floorNode:CreateComponent("StaticModel")
        floorObject.model = cache:GetResource("Model", "Models/Box.mdl")
        floorObject.material = cache:GetResource("Material", "Materials/StoneTiled.xml")

        -- Make the floor physical by adding RigidBody and CollisionShape components
        local body = floorNode:CreateComponent("RigidBody")
        -- We will be spawning spherical objects in this sample. The ground also needs non-zero rolling friction so that
        -- the spheres will eventually come to rest
        local shape = floorNode:CreateComponent("CollisionShape")
        -- Set a box shape of size 1 x 1 x 1 for collision. The shape will be scaled with the scene node scale, so the
        -- rendering and physics representation sizes should match (the box model is also 1 x 1 x 1.)
        shape:SetBox(Vector3(1.0, 1.0, 1.0))

        -- Create animated models
        for z = -1, 1 do
            for x = -4, 4 do
                local modelNode = scene_:CreateChild("Jack")
                modelNode.position = Vector3(x * 5.0, 0.0, z * 5.0)
                modelNode.rotation = Quaternion(0.0, 180.0, 0.0)
                local modelObject = modelNode:CreateComponent("AnimatedModel")
                local model = cache:GetResource("Model", "Models/Jack.mdl")
                modelObject.model = model
                modelObject.material = cache:GetResource("Material", "Materials/Jack.xml")
                modelObject.castShadows = true
                -- Set the model to also update when invisible to avoid staying invisible when the model should come into
                -- view, but does not as the bounding box is not updated
                modelObject.updateInvisible = true

                -- Create a rigid body and a collision shape. These will act as a trigger for transforming the
                -- model into a ragdoll when hit by a moving object
                local body = modelNode:CreateComponent("RigidBody")
                -- The trigger mode makes the rigid body only detect collisions, but impart no forces on the
                -- colliding objects
                body.trigger = true
                local shape = modelNode:CreateComponent("CollisionShape")
                -- Create the capsule shape with an offset so that it is correctly aligned with the model, which
                -- has its origin at the feet
                shape:SetCapsule(0.7, 2.0, Vector3(0.0, 1.0, 0.0))

                -- Create a custom script object that reacts to collisions and creates the ragdoll
                modelNode:CreateScriptObject("CreateRagdoll")
            end
        end

        -- Create the camera. Limit far clip distance to match the fog. Note: now we actually create the camera node outside
        -- the scene, because we want it to be unaffected by scene load / save
        cameraNode = Node()
        local camera = cameraNode:CreateComponent("Camera")
        camera.farClip = 300.0

        -- Set an initial position for the camera scene node above the floor
        cameraNode.position = Vector3(0.0, 5.0, -20.0)
    end

    function CreateInstructions()
        -- Construct new Text object, set string to display and font to use
        local instructionText = ui.root:CreateChild("Text")
        instructionText:SetText(
            "Use WASD keys and mouse to move\n"..
            "LMB to spawn physics objects\n"..
            "F5 to save scene, F7 to load\n"..
            "Space to toggle physics debug geometry")
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
    end

    function DrawDecalAt(ray)
        local result = scene_:GetComponent("Octree"):RaycastSingle(ray, RAY_TRIANGLE, 10000, DRAWABLE_GEOMETRY)
        if not result then
            return
        end
        
        local node = result.drawable.node
        local ds = node:GetComponent("DecalSet")
        if not ds then
            ds = node:CreateComponent("DecalSet")
            ds:SetMaterial(cache:GetResource("Material","Materials/wound1.xml"))
            ds:SetMaxIndices(1024 * 100)
            ds:SetMaxVertices(1024 * 100)
        end
        ds:AddDecal(result.drawable, result.position, cameraNode.rotation, 0.5, 1, 0.5, Vector2(0,0), Vector2(1,1), 0, 0.1)
    end

    function PushRay(dismember)
        local ray = cameraNode:GetComponent("Camera"):GetScreenRay(0.5,0.5)
        local resultPhys = scene_:GetComponent("PhysicsWorld"):RaycastSingle(ray, 10000)
        
        if resultPhys then
            local node = resultPhys.body.node
            if not resultPhys.body.active then
                resultPhys.body:Activate()
            end
            
            local force = 3
            resultPhys.body:ApplyImpulse(ray.direction * force, node:WorldToLocal(resultPhys.position))
            
            if dismember and not node:HasTag("dismembered") then
                DismemberLimb(node)
            end
            --DrawDecalAt(ray)
        end
        
    end

    function DismemberLimb(node)
        local constraint = node:GetComponent("Constraint")
        if constraint then
            constraint.enabled = false
            SeparateLimb1(node)
        end
    end

    function SeparateLimb1(node)
        node:AddTag("dismembered") -- add tag so we dont do process this bone again
        
        local nodeClone = node:Clone()
        local limbNode = scene_:CreateChild("limb") -- contains the limb
        local bodiesNode = limbNode:CreateChild("bodies") -- contains rigid bodies
        nodeClone.parent = bodiesNode
        
        -- ORIGINAL MODEL TWEAK
        local children = node:GetChildrenWithComponent("RigidBody",true)
        for i=1, #children, 1 do
            children[i]:RemoveAllComponents()
        end
        node:RemoveAllComponents()
        node:SetScale(0)
        -- END ORIGINAL MODEL TWEAK
        
        local skelNode = nodeClone:CreateChild("skeleton") -- node that holds the skel bones
        local am = skelNode:CreateComponent("AnimatedModel") -- create the skell bones
        local model = cache:GetResource("Model", "Models/Jack.mdl")
        am.model = model
        
        local skelBone = skelNode:GetChild(node.name, true) -- get same node as our cloned node
        
        local reparentNode = skelNode:CreateChild("reparent") -- this is the node that stores the bones that get scaled to 0
        
        -- reparent
        children = skelNode:GetChildren(false)
        for i=1, #children, 1 do
            children[i].parent = reparentNode
        end
        
        FixSkeleton(bodiesNode, skelNode) -- Fix and assigns each new bone to it repective rigidbodied bone that was cloned (nodeClone)
        reparentNode:SetScale(0) -- set the rest of the body to scale 0
        skelBone.parent = skelNode -- take detached limbBone out of the reparentNode
        
        -- so basically in the end we probably have this 
        -- limbNode (Main node where the detached limbs resides)
            -- bodiesNode (has the rigidbodies tha we cloned)
                -- nodeClone (the clonned node)
                    -- skelNode<AnimatedModel> (has the new skeleton + animated model)
                        -- skelBone (aka the actual detached limb)
                        -- reparentNode (every bone that is not the detached limb should be here)
    end

    function FixSkeleton(bodiesNode, skelNode) -- goes through each rigidbody, gets the respective node of our new AnimatedModel that matches rigidbodies name, and set it as a child of the rigidibody, so it can follow it around. This whole process could be avoided if I could 'retarget' or 'replace' bone nodes, but since I cant, we need to grab the automatically created bone node and set it to be child of its respective 'rigidbody'
        local bodies = bodiesNode:GetChildren()
        for i = 1, #bodies, 1 do
            FixSkeleton(bodies[i], skelNode)
            local bone = skelNode:GetChild(bodies[i].name, true)
            if bone then
                bone.parent = bodies[i]
                bone:SetTransform(Vector3.ZERO, Quaternion.IDENTITY)
                bone:SetScale(1)
            end
        end
    end

    function MoveCamera(timeStep)
        -- Do not move if the UI has a focused element (the console)
        if ui.focusElement ~= nil then
            return
        end

        -- Movement speed as world units per second
        local MOVE_SPEED = 20.0
        -- Mouse sensitivity as degrees per pixel
        local MOUSE_SENSITIVITY = 0.1

        -- Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
        local mouseMove = input.mouseMove
        yaw = yaw + MOUSE_SENSITIVITY * mouseMove.x
        pitch = pitch  +MOUSE_SENSITIVITY * mouseMove.y
        pitch = Clamp(pitch, -90.0, 90.0)

        -- Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
        cameraNode.rotation = Quaternion(pitch, yaw, 0.0)

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

        -- "Shoot" a physics object with left mousebutton
        if input:GetMouseButtonPress(MOUSEB_LEFT) then
            SpawnObject()
        end
        
        if input:GetMouseButtonPress(MOUSEB_RIGHT) then
            nClock = os.clock()
            PushRay(true)
            print("Elapsed time is: " .. os.clock()-nClock)
        end

        -- Check for loading/saving the scene. Save the scene to the file Data/Scenes/Physics.xml relative to the executable
        -- directory
        if input:GetKeyPress(KEY_F5) then
            scene_:SaveXML(fileSystem:GetProgramDir().."Data/Scenes/Ragdolls.xml")
        end
        if input:GetKeyPress(KEY_F7) then
            scene_:LoadXML(fileSystem:GetProgramDir().."Data/Scenes/Ragdolls.xml")
        end

        -- Toggle debug geometry with space
        if input:GetKeyPress(KEY_SPACE) then
            drawDebug = not drawDebug
        end
    end

    function SpawnObject()
        local boxNode = scene_:CreateChild("Sphere")
        boxNode.position = cameraNode.position
        boxNode.rotation = cameraNode.rotation
        boxNode:SetScale(0.25)
        local boxObject = boxNode:CreateComponent("StaticModel")
        boxObject.model = cache:GetResource("Model", "Models/Sphere.mdl")
        boxObject.material = cache:GetResource("Material", "Materials/StoneSmall.xml")
        boxObject.castShadows = true

        local body = boxNode:CreateComponent("RigidBody")
        body.mass = 1.0
        body.rollingFriction = 0.15
        local shape = boxNode:CreateComponent("CollisionShape")
        shape:SetSphere(1.0)

        local OBJECT_VELOCITY = 10.0

        -- Set initial velocity for the RigidBody based on camera forward vector. Add also a slight up component
        -- to overcome gravity better
        body.linearVelocity = cameraNode.rotation * Vector3(0.0, 0.25, 1.0) * OBJECT_VELOCITY
    end

    function HandleUpdate(eventType, eventData)
        -- Take the frame time step, which is stored as a float
        local timeStep = eventData["TimeStep"]:GetFloat()

        -- Move the camera, scale movement with time step
        MoveCamera(timeStep)
    end

    function HandlePostRenderUpdate(eventType, eventData)
        -- If draw debug mode is enabled, draw physics debug geometry. Use depth test to make the result easier to interpret
        if drawDebug then
            renderer:DrawDebugGeometry(true)
            scene_:GetComponent("PhysicsWorld"):DrawDebugGeometry(true)
        end
    end

    -- CreateRagdoll script object class
    CreateRagdoll = ScriptObject()

    function CreateRagdoll:Start()
        -- Subscribe physics collisions that concern this scene node
        self:SubscribeToEvent(self.node, "NodeCollision", "CreateRagdoll:HandleNodeCollision")
    end

    function CreateRagdoll:HandleNodeCollision(eventType, eventData)
        -- Get the other colliding body, make sure it is moving (has nonzero mass)
        local otherBody = eventData["OtherBody"]:GetPtr("RigidBody")

        if otherBody.mass > 0.0 then
            -- We do not need the physics components in the AnimatedModel's root scene node anymore
            self.node:RemoveComponent("RigidBody")
            self.node:RemoveComponent("CollisionShape")

            -- Create RigidBody & CollisionShape components to bones
            self:CreateRagdollBone("Bip01_Pelvis", SHAPE_BOX, Vector3(0.3, 0.2, 0.25), Vector3(0.0, 0.0, 0.0),
                Quaternion(0.0, 0.0, 0.0))
            self:CreateRagdollBone("Bip01_Spine1", SHAPE_BOX, Vector3(0.35, 0.2, 0.3), Vector3(0.15, 0.0, 0.0),
                Quaternion(0.0, 0.0, 0.0))
            self:CreateRagdollBone("Bip01_L_Thigh", SHAPE_CAPSULE, Vector3(0.175, 0.45, 0.175), Vector3(0.25, 0.0, 0.0),
                Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_R_Thigh", SHAPE_CAPSULE, Vector3(0.175, 0.45, 0.175), Vector3(0.25, 0.0, 0.0),
                Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_L_Calf", SHAPE_CAPSULE, Vector3(0.15, 0.55, 0.15), Vector3(0.25, 0.0, 0.0),
                Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_R_Calf", SHAPE_CAPSULE, Vector3(0.15, 0.55, 0.15), Vector3(0.25, 0.0, 0.0),
                Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_Head", SHAPE_CAPSULE, Vector3(0.2, 0.2, 0.2), Vector3(0.1, 0.0, 0.0),
                Quaternion(0.0, 0.0, 0.0))
            self:CreateRagdollBone("Bip01_L_UpperArm", SHAPE_CAPSULE, Vector3(0.15, 0.35, 0.15), Vector3(0.1, 0.0, 0.0),
                Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_R_UpperArm", SHAPE_CAPSULE, Vector3(0.15, 0.35, 0.15), Vector3(0.1, 0.0, 0.0),
                Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_L_Forearm", SHAPE_CAPSULE, Vector3(0.125, 0.4, 0.125), Vector3(0.2, 0.0, 0.0),
                Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_R_Forearm", SHAPE_CAPSULE, Vector3(0.125, 0.4, 0.125), Vector3(0.2, 0.0, 0.0),
                Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_L_Hand", SHAPE_BOX, Vector3(0.1, 0.2, 0.1), Vector3(0.1, 0.0, 0.0),
    			Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_R_Hand", SHAPE_BOX, Vector3(0.1, 0.2, 0.1), Vector3(0.1, 0.0, 0.0),
    			Quaternion(0.0, 0.0, 90.0))
            self:CreateRagdollBone("Bip01_L_Foot", SHAPE_BOX, Vector3(0.125, 0.3, 0.07), Vector3(0.1, 0.075, 0.0),
    			Quaternion(0.0, 0.0, 0.0))
            self:CreateRagdollBone("Bip01_R_Foot", SHAPE_BOX, Vector3(0.125, 0.3, 0.07), Vector3(0.1, 0.075, 0.0),
    			Quaternion(0.0, 0.0, 0.0))

            -- Create Constraints between bones
            self:CreateRagdollConstraint("Bip01_L_Thigh", "Bip01_Pelvis", CONSTRAINT_CONETWIST, Vector3(0.0, 0.0, -1.0),
                Vector3(0.0, 0.0, 1.0), Vector2(45.0, 45.0), Vector2(0.0, 0.0), true)
            self:CreateRagdollConstraint("Bip01_R_Thigh", "Bip01_Pelvis", CONSTRAINT_CONETWIST, Vector3(0.0, 0.0, -1.0),
                Vector3(0.0, 0.0, 1.0), Vector2(45.0, 45.0), Vector2(0.0, 0.0), true)
            self:CreateRagdollConstraint("Bip01_L_Calf", "Bip01_L_Thigh", CONSTRAINT_HINGE, Vector3(0.0, 0.0, -1.0),
                Vector3(0.0, 0.0, -1.0), Vector2(90.0, 0.0), Vector2(0.0, 0.0), true)
            self:CreateRagdollConstraint("Bip01_R_Calf", "Bip01_R_Thigh", CONSTRAINT_HINGE, Vector3(0.0, 0.0, -1.0),
                Vector3(0.0, 0.0, -1.0), Vector2(90.0, 0.0), Vector2(0.0, 0.0), true)
            self:CreateRagdollConstraint("Bip01_Spine1", "Bip01_Pelvis", CONSTRAINT_HINGE, Vector3(0.0, 0.0, 1.0),
                Vector3(0.0, 0.0, 1.0), Vector2(45.0, 0.0), Vector2(-10.0, 0.0), true)
            self:CreateRagdollConstraint("Bip01_Head", "Bip01_Spine1", CONSTRAINT_CONETWIST, Vector3(-1.0, 0.0, 0.0),
                Vector3(-1.0, 0.0, 0.0), Vector2(0.0, 30.0), Vector2(0.0, 0.0), true)
            self:CreateRagdollConstraint("Bip01_L_UpperArm", "Bip01_Spine1", CONSTRAINT_CONETWIST, Vector3(0.0, -1.0, 0.0),
                Vector3(0.0, 1.0, 0.0), Vector2(45.0, 45.0), Vector2(0.0, 0.0), false)
            self:CreateRagdollConstraint("Bip01_R_UpperArm", "Bip01_Spine1", CONSTRAINT_CONETWIST, Vector3(0.0, -1.0, 0.0),
                Vector3(0.0, 1.0, 0.0), Vector2(45.0, 45.0), Vector2(0.0, 0.0), false)
            self:CreateRagdollConstraint("Bip01_L_Forearm", "Bip01_L_UpperArm", CONSTRAINT_HINGE, Vector3(0.0, 0.0, -1.0),
                Vector3(0.0, 0.0, -1.0), Vector2(90.0, 0.0), Vector2(0.0, 0.0), true)
            self:CreateRagdollConstraint("Bip01_R_Forearm", "Bip01_R_UpperArm", CONSTRAINT_HINGE, Vector3(0.0, 0.0, -1.0),
                Vector3(0.0, 0.0, -1.0), Vector2(90.0, 0.0), Vector2(0.0, 0.0), true)
            self:CreateRagdollConstraint("Bip01_L_Hand", "Bip01_L_Forearm", CONSTRAINT_CONETWIST, Vector3(0.0, 0.0, -1.0), 
                Vector3(0.0, 0.0, -1.0), Vector2(45, 0), Vector2(0, 0), true);
            self:CreateRagdollConstraint("Bip01_R_Hand", "Bip01_R_Forearm", CONSTRAINT_CONETWIST, Vector3(0.0, 0.0, -1.0), 
                Vector3(0.0, 0.0, -1.0), Vector2(45, 0), Vector2(0, 0), true);
            self:CreateRagdollConstraint("Bip01_L_Foot", "Bip01_L_Calf", CONSTRAINT_CONETWIST, Vector3(0.0, 0.0, -1.0), 
                Vector3(0.0, 0.0, -1.0), Vector2(45, 0), Vector2(0, 0), true);
            self:CreateRagdollConstraint("Bip01_R_Foot", "Bip01_R_Calf", CONSTRAINT_CONETWIST, Vector3(0.0, 0.0, -1.0), 
                Vector3(0.0, 0.0, -1.0), Vector2(45, 0), Vector2(0, 0), true);

            -- Disable keyframe animation from all bones so that they will not interfere with the ragdoll
            local model = self.node:GetComponent("AnimatedModel")
            local skeleton = model.skeleton
            for i = 0, skeleton.numBones - 1 do
                skeleton:GetBone(i).animated = false
            end

            -- Finally remove self (the ScriptInstance which holds this script object) from the scene node. Note that this must
            -- be the last operation performed in the function
            self.instance:Remove()
        end
    end

    function CreateRagdoll:CreateRagdollBone(boneName, type, size, position, rotation)
        -- Find the correct child scene node recursively
        local boneNode = self.node:GetChild(boneName, true)
        if boneNode == nil then
            print("Could not find bone " .. boneName .. " for creating ragdoll physics components\n")
            return
        end

        local body = boneNode:CreateComponent("RigidBody")
        -- Set mass to make movable
        body.mass = 1.0
        body.restitution = 1
        body.friction = 1
        -- Set damping parameters to smooth out the motion
        body.rollingFriction = 0.01
        body.linearDamping = 0.05
        body.angularDamping = 0.2
        -- Set rest thresholds to ensure the ragdoll rigid bodies come to rest to not consume CPU endlessly
        body.linearRestThreshold = 2
        body.angularRestThreshold = 3

        local shape = boneNode:CreateComponent("CollisionShape")
        -- We use either a box or a capsule shape for all of the bones
        if type == SHAPE_BOX then
            shape:SetBox(size, position, rotation)
        else
            shape:SetCapsule(size.x, size.y, position, rotation)
        end
    end

    function CreateRagdoll:CreateRagdollConstraint(boneName, parentName, type, axis, parentAxis, highLimit, lowLimit, disableCollision)
        local boneNode = self.node:GetChild(boneName, true)
        local parentNode = self.node:GetChild(parentName, true)
        if boneNode == nil then
            print("Could not find bone " .. boneName .. " for creating ragdoll constraint\n")
            return
        end
        if parentNode == nil then
            print("Could not find bone " .. parentName .. " for creating ragdoll constraint\n")
            return
        end

        local constraint = boneNode:CreateComponent("Constraint")
        constraint.constraintType = type
        -- Most of the constraints in the ragdoll will work better when the connected bodies don't collide against each other
        constraint.disableCollision = disableCollision
        -- The connected body must be specified before setting the world position
        constraint.otherBody = parentNode:GetComponent("RigidBody")
        -- Position the constraint at the child bone we are connecting
        constraint.worldPosition = boneNode.worldPosition
        -- Configure axes and limits
        constraint.axis = axis
        constraint.otherAxis = parentAxis
        constraint.highLimit = highLimit
        constraint.lowLimit = lowLimit
    end

    -- Create XML patch instructions for screen joystick layout specific to this sample app
    function GetScreenJoystickPatchString()
        return
            "<patch>" ..
            "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/attribute[@name='Is Visible']\" />" ..
            "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Spawn</replace>" ..
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


How it works, let's say I shot an Arm:
PS: you will see me using the word bone and node interchangeably, because they kinda are.
1- Get the node that was hit, an arm for example.
2- Clone the node. This will also clone children, great.
3- Remove unnecessary components from original node (rigid bodies, contraints, etc.)
4- Scale original node to 0, now there is no arm.
5- Reparent cloned node for a cleaner hierarchy.
What we have so far is:
- Original AnimatedModel without the arm, because it got scaled to 0 and has no components.
- A cloned node that has no other component but the rigidbodies and constraints, therefore, no way to render it.

And this is where the dirty hack begins. The most correct way to attach geometry to the arm would be something like this:
6- Create a new AnimatedModel, obvious step.
Now we need the arm of this AnimatedModel to follow our cloned arm right ? in other words, we need to bind our cloned arm node to the AnimatedModel. So we would do something like
7- Use a function like "ReplaceBone(originalBoneNode, newBoneNode)" that could recursively replace each original bone node of the AnimatedModel with our cloned arm bone nodes.

But the above 2 steps did not happen exactly like that, because there is no such function that replaces a bone with another (at least not in LUA). When you create an AnimatedModel, it automatically creates the bone nodes for you, and there is no way to replace them with custom ones. So there is no way to 'bind' our cloned arm node to the AnimatedModel we just created...
So I had to hack this out, and the way I did it was by, pay attention: Reparenting each new bone to their respective cloned arm bone. So each new bone gets to be a child of their respective cloned arm bone.

8- Scale the rest of the body in relation to the cloned arm (the inverse of step 4), so that there is no body, but jut the arm.

-------------------------

