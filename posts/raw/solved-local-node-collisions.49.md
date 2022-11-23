Mike | 2017-01-02 00:57:35 UTC | #1

I'm trying to implement local node collisions.

Playing with example#18, I've put a phantom RigidBody to Head node and subscribed HeadNode to NodeCollision event.
Collisions with Jack itself are accurately reported, but no other collisions are reported.
I've checked my physics settings by drawing physics debug geometry and the phantom is moving/rotating adequately, so I don't understand what's going on.

-------------------------

cadaver | 2017-01-02 00:57:36 UTC | #2

Is the head "inside" the character's collision cylinder? Then I believe other objects will collide always with the cylinder first and never with the head's collision shape.

-------------------------

Mike | 2017-01-02 00:57:36 UTC | #3

Yes, the head is inside the character's collision capsule.

I've tried to "magnify" the HeadNode shape so that it's mostly out of the capsule but to no avail. Idem using a collisionMask to disable "self" collision.
Next I'll try to reduce the capsule/offset HeadNode body to avoid overlap but even if it works, this is not optimal as I want more nodes to collide.

Is there a hack or an alternative solution to do the job?

-------------------------

cadaver | 2017-01-02 00:57:36 UTC | #4

It depends on what you want the head collisions for. For something like bullet ray hit detection in a shooter game, you can use octree (drawable) raycast, as it will automatically collide against the bone hitboxes of an AnimatedModel and you'll get the bone index in the subObject variable of the RayQueryResult.

-------------------------

Mike | 2017-01-02 00:57:36 UTC | #5

Many thanks for suggestion, so we don't necessarily need bodies if I understand correctly.
Ideally what I'd like to achieve is to check if a particular bone collides with another one from a different animated model.

-------------------------

cadaver | 2017-01-02 00:57:37 UTC | #6

Yeah, the physics simulation will take less CPU hit if you don't add rigidbodies for bones for this, and if you don't need the bones to actually physically simulate (ragdoll is another matter, in that case you do need per-bone physics simulation)

I haven't verified if you can actually do it in Lua script, but you should be able to do a box octree query with your AnimatedModel's bounding box, check if other AnimatedModels are present in the result (for a coarse test), then proceed to manually check bone bounding boxes for overlap according to the coarse test.

-------------------------

Mike | 2017-01-02 00:57:37 UTC | #7

This looks very exciting.

For now I've managed to get the target bone using
[code]if result.subObject ~= nil then print(result.drawable:GetNode():GetComponent("AnimatedModel").skeleton:GetBone(result.subObject).name) end[/code]
Correct me if I'm overcomplicating things.

Now I'll try to implement BoxOctreeQuery, this sounds promising.

EDIT: is BoxOctreeQuery exposed to script at all?

-------------------------

cadaver | 2017-01-02 00:57:37 UTC | #8

No it doesn't seem to be. In AngelScript fictional Octree functions (GetDrawables()) have been added for each shape such as BoundingBox, similar Lua functions need to be added.

-------------------------

cadaver | 2017-01-02 00:57:37 UTC | #9

GetDrawables() functions have been added to Octree Lua bindings. Because an array of pointers couldn't be exposed directly, they return an array of OctreeQueryResult, a fictional struct that is only used for Lua bindings, which has drawable & node properties.

Example: bounding box query around a Vector3 hitPos

[code]
local octree = scene_:GetComponent("Octree");
local result = octree:GetDrawables(result, BoundingBox(hitPos + Vector3(-10,-10,-10), hitPos + Vector3(10,10,10)), DRAWABLE_GEOMETRY);
print("Octree bbox hits: " .. result:Size() .. " at position " .. hitPos:ToString());
for i = 0, result:Size() - 1 do
    print("Result " .. i .. " Drawable type: " .. result[i].drawable.typeName .. " node name: " .. result[i].node.name .. " node pos: " .. result[i].node.position:ToString());
end
[/code]

-------------------------

Mike | 2017-01-02 00:57:37 UTC | #10

Awesome! :stuck_out_tongue:

-------------------------

Mike | 2017-01-02 00:57:38 UTC | #11

Congrats Lasse, it works perfectly.

The only caveat is that for movable StaticModels, the BoundingBox doesn't rotate, so that if for example a box is rotated, collisions become inaccurate.

Here is my code so far for checking collision between Batman's right hand (this AnimatedModel has a fight animation) and Jack's head :
[code]
hitTest(characterNode:GetChild("mixamorig:RightHand", true).worldPosition) -- called in HandleUpdate

function boundingBoxescollision(bbox1, bbox2) -- Check if 2 BoundingBoxes overlap (3D AABB collision test)
	if bbox2.min.x >= bbox1.max.x	-- too much @left
	or bbox2.max.x <= bbox1.min.x	-- too much @right
	or bbox2.min.y >= bbox1.max.y	-- too high
	or bbox2.max.y <= bbox1.min.y	-- too low 
	or bbox2.min.z >= bbox1.max.z	-- too forward
	or bbox2.max.z <= bbox1.min.z	-- too backward

	then return false
	else return true end
end

function customBoundingBox(position, size, visible)
	local bboxSize = Vector3(size, size, size) -- Size of the BoundingBox
	local bbox = BoundingBox(position -bboxSize, position + bboxSize) -- Set BoundingBox position & size

	if visible == true then scene_:GetComponent("DebugRenderer"):AddBoundingBox(bbox, Color(0.5, 0.5, 0.5)) end -- Draw BoundingBox

	return bbox
end

function hitTest(hitPos)
	local bbox = customBoundingBox(hitPos, 0.1, true) -- Get BoundingBox from hitPos & size and draw it
	local result = octree:GetDrawables(bbox, DRAWABLE_GEOMETRY)

	for i = 0, result:Size() -1 do
		if result[i].node.name ~= "Batman" and result[i].node.name ~= "Sky" then -- Exclude Skybox & Self (Batman)
			if result[i].node:GetComponent("StaticModel") ~= nil then scene_:GetComponent("DebugRenderer"):AddBoundingBox(result[i].node:GetComponent("StaticModel").worldBoundingBox, Color(1, 1, 1)) end -- Draw node BoundingBox
			if result[i].node:GetComponent("AnimatedModel") ~= nil then -- For AnimatedModel, check if specified bones are colliding with the BoundingBox
				print(boundingBoxescollision(customBoundingBox(result[i].node:GetChild("Bip01_Head", true).worldPosition, 0.1, true), bbox)) -- Check collision between the 2 BoundingBoxes & draw them
			end
		end
	end

end
[/code]

NB:
- I've added drawing of BoundingBoxes to help debug
- I check boxes overlap by using a custom 3D AABB collision test function, maybe it is already available somewhere.

I'll post an example using Ninja & Jack characters ASAP.

-------------------------

Mike | 2017-01-02 00:57:39 UTC | #12

I've extended example#18 (with external file BoneCollisions.lua, content below) so that Jack is attacked by a ninja when pressing key B

Modifications to file 18_CharacterDemo.lua:

require "LuaScripts/BoneCollisions"

in HandleUpdate function:
    if input:GetKeyPress(KEY_B) then CreateEnemy() end -- Create ennemy (ninja)
	hitTest(characterNode:GetChild("Bip01_Head", true).worldPosition) -- Check Jack's head collisions

What's strange is that using "self.node:LookAt(dir, Vector3(0,1,0))" to rotate the ninja toward Jack produces a Bullet AABB overflow.

[code]
-- BoneCollisions.lua

-- Demonstrates:
--    - accurate bone collisions
--    - enemy head always facing the main character
--    - playing context animation

local BRAKE_FORCE = 0.3 -- Set slightly upper than Jack so that Jack is faster

function boundingBoxescollision(bbox1, bbox2) -- Check if 2 BoundingBoxes overlap (3D AABB collision test)
	if bbox2.min.x >= bbox1.max.x		-- too much @left
	or bbox2.max.x <= bbox1.min.x	-- too much @right
	or bbox2.min.y >= bbox1.max.y	-- too high
	or bbox2.max.y <= bbox1.min.y	-- too low 
	or bbox2.min.z >= bbox1.max.z	-- too forward
	or bbox2.max.z <= bbox1.min.z	-- too backward

	then return false
	else return true end
end

function customBoundingBox(position, size, visible)
 	local bboxSize = Vector3(size, size, size) -- Size of the BoundingBox
	local bbox = BoundingBox(position -bboxSize, position + bboxSize) -- Set BoundingBox position & size

	if visible == true then scene_:GetComponent("DebugRenderer"):AddBoundingBox(bbox, Color(0.5, 0.5, 0.5)) end -- Draw BoundingBox

	return bbox
end

function hitTest(hitPos)
	local bbox = customBoundingBox(hitPos, 0.1, true) -- Get BoundingBox from hitPos & size and draw it
	local result = scene_:GetComponent("Octree"):GetDrawables(bbox, DRAWABLE_GEOMETRY)

--	print("Octree bbox hits: " .. result:Size() .. " at position " .. hitPos:ToString())
	for i = 0, result:Size() -1 do
		if result[i].node.name ~= "Jack" then -- Exclude Self (Jack)
			if result[i].node:GetComponent("StaticModel") ~= nil then scene_:GetComponent("DebugRenderer"):AddBoundingBox(result[i].node:GetComponent("StaticModel").worldBoundingBox, Color(1, 1, 1)) end -- Draw node BoundingBox
			if result[i].node:GetComponent("AnimatedModel") ~= nil then -- For AnimatedModel, check if specified bones are colliding with the BoundingBox
				print(boundingBoxescollision(customBoundingBox(result[i].node:GetChild("Joint13", true).worldPosition, 0.1, true), bbox)) -- Check collision between the 2 BoundingBoxes & draw them
				if boundingBoxescollision(customBoundingBox(result[i].node:GetChild("Joint13", true).worldPosition, 0.1, true), bbox) then
					--headShot()
				end
			end
--			print("Result " .. i .. " Drawable type: " .. result[i].drawable.typeName .. " node name: " .. result[i].node.name .. " node pos: " .. result[i].node.position:ToString())
		end
	end
end

function headShot()
	-- do something with Jack (context animation, move backward, rotate head backward...)
end

function CreateEnemy()
	local EnemyNode = scene_:CreateChild("Enemy")
	EnemyNode.position = Vector3(0, 0, 10)
	local object = EnemyNode:CreateComponent("AnimatedModel")
	object.model = cache:GetResource("Model", "Models/Ninja.mdl")
	object.material = cache:GetResource("Material", "Materials/Ninja.xml")
	object.castShadows = true
	local body = EnemyNode:CreateComponent("RigidBody")
	body.mass = 1 -- Set non-zero mass so that the body becomes dynamic
	body.angularFactor = Vector3(0, 0, 0) -- Keep Enemy always upright
	local shape = EnemyNode:CreateComponent("CollisionShape")
	shape:SetCapsule(0.7, 1.8, Vector3(0, 0.9, 0)) -- diameter/height/position
	shape.offset = Vector3(0,1,0)

	EnemyNode:CreateScriptObject("Enemy") -- Create the Enemy logic object, which takes care of steering the rigidbody
	EnemyNode:CreateComponent("AnimationController") -- Create the animation controller
end

-- Enemy script object class
Enemy = ScriptObject()

function Enemy:Start()
	self.isFighting = false
	self:SubscribeToEvent(self.node, "NodeCollision", "Enemy:HandleNodeCollision") -- Subscribe to NodeCollision physics event
end

function Enemy:Load(deserializer)
	self.isFighting = deserializer:ReadBool()
end

function Enemy:Save(serializer)
	serializer:WriteBool(self.isFighting)
end

function Enemy:HandleNodeCollision(eventType, eventData)
	local otherBody = eventData:GetPtr("RigidBody", "OtherBody") -- Get the other colliding body
	local otherNode = eventData:GetPtr("Node", "OtherNode") -- Get the other colliding node

	if otherNode.name == "Jack" then self.isFighting = true else self.isFighting = false end -- Check if fighting to trigger appropriate animation
end


function Enemy:FixedPostUpdate(timeStep)		-- NB: FixedPostUpdate in reaction to Jack's FixedUpdate
	local body = self.node:GetComponent("RigidBody")

	if not self.isFighting then -- When fighting, don't move Enemy

		local dir = characterNode.position - self.node.position
		--self.node:LookAt(dir, Vector3(0,1,0)) -- Uncommenting this line produces an AABB overflow

		-- Rotate Enemy head toward Jack
		local skeleton = self.node:GetComponent("AnimatedModel").skeleton
		skeleton:GetBone("Joint8").animated = false -- Disable head animation
		local headNode = self.node:GetChild("Joint8", true)
		headNode:LookAt(characterNode.position + Vector3(0, 1.7, 0), Vector3(0, 1 ,0)) -- Look at head level
		--Todo: restrict lateral rotation

		-- Update movement
		local velocity = body.linearVelocity

		local planeVelocity = Vector3(velocity.x, 0, velocity.z) -- Velocity on the XZ plane
		local brakeForce = planeVelocity * -BRAKE_FORCE

		body:ApplyImpulse(dir:Normalized())
		body:ApplyImpulse(brakeForce)
	end

	-- Update Animations
	local animCtrl = self.node:GetComponent("AnimationController")

	if self.isFighting then animCtrl:PlayExclusive("Models/Ninja_Attack3.ani", 0, true, 0.2)
	else animCtrl:PlayExclusive("Models/Ninja_Walk.ani", 0, true, 0.3) end

	animCtrl:SetSpeed("Models/Ninja_Walk.ani", 1)
end
[/code]

-------------------------

