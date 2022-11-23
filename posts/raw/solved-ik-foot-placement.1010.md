Mike | 2017-01-02 01:04:47 UTC | #1

I'm currently experimenting a basic inverse kinematics (IK) foot placement for grounding feet on uneaven surfaces.

What I'd like to achieve is:
- apply the animation (for real or virtually)
- then compute rotations for hip and knee joints to match the target positions (I get 4 Quaternions)
- then override the animation with the quaternions

I'm missing the last step (applying the 4 quaternions after playing the animation has no effect). Or maybe it could be done differently?

-------------------------

cadaver | 2017-01-02 01:04:48 UTC | #2

Running skinned animations are updated in Octree::Update(), which is done as part of the render preparation, so using postupdate is likely too early in the frame. When it's done with the animation updates, Octree::Update() triggers the Scene to send the E_SCENEDRAWABLEUPDATEFINISHED event. Updating IK's should be done as response to that. This is just before octree reinsertion & culling, so you should be able to move & rotate bone nodes without issues.

-------------------------

Mike | 2017-01-02 01:04:48 UTC | #3

Many thanks Cadaver, it works great now :stuck_out_tongue:
I'll post a sample after some cleanup.

-------------------------

Mike | 2017-06-29 10:29:10 UTC | #4

Sample lua demonstration:

[details=Code]
```
require "LuaScripts/Utilities/Sample"
require "LuaScripts/Utilities/Touch"

CTRL_FORWARD = 1
CTRL_BACK = 2
CTRL_LEFT = 4
CTRL_RIGHT = 8
local CTRL_JUMP = 16

local MOVE_FORCE = 0.8
local INAIR_MOVE_FORCE = 0.02
local BRAKE_FORCE = 0.2
local JUMP_FORCE = 7
local YAW_SENSITIVITY = 0.1
local INAIR_THRESHOLD_TIME = 0.1
firstPerson = false -- First person camera flag

local characterNode = nil
local doIK = false


function Start()
    SampleStart() -- Execute the common startup for samples
    CreateScene() -- Create static scene content
    CreateJack()  -- Create the controllable character
    CreateInstructions() -- Create the UI content
    SubscribeToEvents() -- Subscribe to necessary events
end

function CreateScene()
    -- Scene
    scene_ = Scene()
    scene_:CreateComponent("Octree")
    physicsWorld = scene_:CreateComponent("PhysicsWorld")
    debug = scene_:CreateComponent("DebugRenderer")

    -- Create camera and define viewport. Camera does not necessarily have to belong to the scene
    cameraNode = Node()
    local camera = cameraNode:CreateComponent("Camera")
    camera.farClip = 300
    renderer:SetViewport(0, Viewport:new(scene_, camera))

    -- Create a Zone component for ambient lighting & fog control
    local zoneNode = scene_:CreateChild("Zone")
    local zone = zoneNode:CreateComponent("Zone")
    zone.boundingBox = BoundingBox(-1000, 1000)
    zone.ambientColor = Color(0.15, 0.15, 0.15)
    zone.fogColor = Color(0.5, 0.5, 0.7)
    zone.fogStart = 100
    zone.fogEnd = 300

    -- Create a directional light to the world. Enable cascaded shadows on it
    local lightNode = scene_:CreateChild("DirectionalLight")
    lightNode.direction = Vector3(0.6, -1, 0.8)
    local light = lightNode:CreateComponent("Light")
    light.lightType = LIGHT_DIRECTIONAL
    light.castShadows = true
    light.shadowBias = BiasParameters(0.00025, 0.5)
    -- Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
    light.shadowCascade = CascadeParameters(10, 50, 200, 0, 0.8)

    -- Create the floor object
    local floorNode = scene_:CreateChild("Floor")
    floorNode.position = Vector3(0, -0.5, 0)
    floorNode.scale = Vector3(200, 1, 200)
    local object = floorNode:CreateComponent("StaticModel")
    object.model = cache:GetResource("Model", "Models/Box.mdl")
    object.material = cache:GetResource("Material", "Materials/Stone.xml")

    local body = floorNode:CreateComponent("RigidBody")
    -- Use collision layer bit 2 to mark world scenery. This is what we will raycast against to prevent camera from going inside geometry
    body.collisionLayer = 2
    local shape = floorNode:CreateComponent("CollisionShape")
    shape:SetBox(Vector3(1, 1, 1))

    -- Create mushrooms of varying sizes
    local NUM_MUSHROOMS = 60
    for i = 1, NUM_MUSHROOMS do
        local objectNode = scene_:CreateChild("Mushroom")
        objectNode.position = Vector3(Random(180) - 90, 0, Random(180) - 90)
        objectNode.rotation = Quaternion(0, Random(360), 0)
        objectNode:SetScale(2 + Random(5))
        local object = objectNode:CreateComponent("StaticModel")
        object.model = cache:GetResource("Model", "Models/Mushroom.mdl")
        object.material = cache:GetResource("Material", "Materials/Mushroom.xml")
        object.castShadows = true

        local body = objectNode:CreateComponent("RigidBody")
        body.collisionLayer = 2
        local shape = objectNode:CreateComponent("CollisionShape")
        shape:SetTriangleMesh(object.model, 0)
    end

    -- Create movable boxes. Let them fall from the sky at first
    local NUM_BOXES = 100
    for i = 1, NUM_BOXES do
        local scale = Random(2) + 0.5

        local objectNode = scene_:CreateChild("Box")
        objectNode.position = Vector3(Random(180) - 90, Random(10) + 10, Random(180) - 90)
        objectNode.rotation = Quaternion(Random(360), Random(360), Random(360))
        objectNode:SetScale(scale)
        local object = objectNode:CreateComponent("StaticModel")
        object.model = cache:GetResource("Model", "Models/Box.mdl")
        object.material = cache:GetResource("Material", "Materials/Stone.xml")
        object.castShadows = true

        local body = objectNode:CreateComponent("RigidBody")
        body.collisionLayer = 2
        -- Bigger boxes will be heavier and harder to move
        body.mass = scale * 2
        local shape = objectNode:CreateComponent("CollisionShape")
        shape:SetBox(Vector3(1, 1, 1))
    end
end

function CreateJack()
    characterNode = scene_:CreateChild("Jack")

    -- Create the rendering component + animation controller
    local object = characterNode:CreateComponent("AnimatedModel")
    object.model = cache:GetResource("Model", "Models/Jack.mdl")
    object.material = cache:GetResource("Material", "Materials/Jack.xml")
    object.castShadows = true
    characterNode:CreateComponent("AnimationController")

    -- Create rigidbody, and set non-zero mass so that the body becomes dynamic
    local body = characterNode:CreateComponent("RigidBody")
    body.collisionLayer = 1
    body.mass = 1

    -- Set zero angular factor so that physics doesn't turn the character on its own.
    -- Instead we will control the character yaw manually
    body.angularFactor = Vector3(0, 0, 0)

    -- Set the rigidbody to signal collision also when in rest, so that we get ground collisions properly
    body.collisionEventMode = COLLISION_ALWAYS

    -- Set a capsule shape for collision
    local shape = characterNode:CreateComponent("CollisionShape")
    shape:SetCapsule(0.7, 1.8, Vector3(0, 0.9, 0))

    -- Create the character logic object, which takes care of steering the rigidbody
    characterNode:CreateScriptObject("Character")

    -- Create IK chains
    CreateIKChains()
end

function CreateInstructions()
    -- Construct new Text object, set string to display and font to use
    local instructionText = ui.root:CreateChild("Text")
    instructionText.text = "Use directional keys and mouse to move\n".."Space to jump, F to toggle 1st/3rd person\n".."F5 to save scene, F7 to load"
    instructionText:SetFont(cache:GetResource("Font", "Fonts/Anonymous Pro.ttf"), 15)
    instructionText.textAlignment = HA_CENTER
    instructionText.horizontalAlignment = HA_CENTER
    instructionText.verticalAlignment = VA_CENTER
    instructionText:SetPosition(0, ui.root.height / 4)
end

function SubscribeToEvents()
    SubscribeToEvent("Update", "HandleUpdate") -- Subscribe to Update event for setting the character controls before physics simulation
    SubscribeToEvent("PostUpdate", "HandlePostUpdate") -- Subscribe to PostUpdate event for updating the camera position after physics simulation
    UnsubscribeFromEvent("SceneUpdate") -- Unsubscribe the SceneUpdate event from base class as the camera node is being controlled in HandlePostUpdate() in this sample
    SubscribeToEvent("SceneDrawableUpdateFinished", "HandleSceneDrawableUpdateFinished") -- Subscribe to the SceneDrawableUpdateFinished event which is triggered after the animations have been updated so we can apply IK to override them
	SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate") -- Process post-render update event, during which we request debug geometry
end

function HandleUpdate(eventType, eventData)
    if characterNode == nil then return end

    local character = characterNode:GetScriptObject()
    if character == nil then return end

    -- Clear previous controls
    character.controls:Set(CTRL_FORWARD + CTRL_BACK + CTRL_LEFT + CTRL_RIGHT + CTRL_JUMP, false)

    -- Update controls using touch utility
    if touchEnabled then UpdateTouches(character.controls) end

    -- Update controls using keys
    if ui.focusElement == nil then
        if not touchEnabled or not useGyroscope then
            if input:GetKeyDown(KEY_UP) then character.controls:Set(CTRL_FORWARD, true) end
            if input:GetKeyDown(KEY_DOWN) then character.controls:Set(CTRL_BACK, true) end
            if input:GetKeyDown(KEY_LEFT) then character.controls:Set(CTRL_LEFT, true) end
            if input:GetKeyDown(KEY_RIGHT) then character.controls:Set(CTRL_RIGHT, true) end
        end
        if input:GetKeyDown(KEY_SPACE) then character.controls:Set(CTRL_JUMP, true) end

        -- Add character yaw & pitch from the mouse motion or touch input
        if touchEnabled then
            for i=0, input.numTouches - 1 do
                local state = input:GetTouch(i)
                if not state.touchedElement then -- Touch on empty space
                    local camera = cameraNode:GetComponent("Camera")
                    if not camera then return end

                    character.controls.yaw = character.controls.yaw + TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.x
                    character.controls.pitch = character.controls.pitch + TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.y
                end
            end
        else
            character.controls.yaw = character.controls.yaw + input.mouseMoveX * YAW_SENSITIVITY
            character.controls.pitch = character.controls.pitch + input.mouseMoveY * YAW_SENSITIVITY
        end
        -- Limit pitch
        character.controls.pitch = Clamp(character.controls.pitch, -80, 80)

        -- Switch between 1st and 3rd person
        if input:GetKeyPress(KEY_F) then firstPerson = not firstPerson end

        -- Turn on/off gyroscope on mobile platform
        if input:GetKeyPress(KEY_G) then useGyroscope = not useGyroscope end

        -- Check for loading / saving the scene
        if input:GetKeyPress(KEY_F5) then scene_:SaveXML(fileSystem:GetProgramDir().."Data/Scenes/CharacterDemo.xml") end
        if input:GetKeyPress(KEY_F7) then
            scene_:LoadXML(fileSystem:GetProgramDir().."Data/Scenes/CharacterDemo.xml")
            -- After loading we have to reacquire the character scene node, as it has been recreated
            -- Simply find by name as there's only one of them
            characterNode = scene_:GetChild("Jack", true)
            if characterNode == nil then return end
        end
    end

    -- Set rotation already here so that it's updated every rendering frame instead of every physics frame
    characterNode.rotation = Quaternion(character.controls.yaw, Vector3.UP)

	-- Toggle debug geometry with 'Q'
	if input:GetKeyPress(KEY_Q) then drawDebug = not drawDebug end
end

function HandlePostRenderUpdate(eventType, eventData)
	if drawDebug then scene_:GetComponent("PhysicsWorld"):DrawDebugGeometry(true) end -- Draw physics debug geometry. Use depth test to make the result easier to interpret
end

function HandlePostUpdate(eventType, eventData)
    if characterNode == nil then return end

    local character = characterNode:GetScriptObject()
    if character == nil then return end

    -- Get camera lookat dir from character yaw + pitch
    local rot = characterNode.rotation
    local dir = rot * Quaternion(character.controls.pitch, Vector3(1, 0, 0))

    if firstPerson then
        -- First person camera: position to the head bone + offset slightly forward & up
        cameraNode.position = headNode.worldPosition + rot * Vector3(0, 0.15, 0.2)
        cameraNode.rotation = dir
    else
        -- Third person camera: position behind the character
        local aimPoint = characterNode.position + rot * Vector3(0, 1.7, 0) -- You can modify x Vector3 value to translate the fixed character position (indicative range[-2;2])

        -- Collide camera ray with static physics objects (layer bitmask 2) to ensure we see the character properly
        local rayDir = dir * Vector3.BACK -- For indoor scenes you can use dir * Vector3(0, 0, -0.5) to prevent camera from crossing the walls
        local rayDistance = cameraDistance
        local result = scene_:GetComponent("PhysicsWorld"):RaycastSingle(Ray(aimPoint, rayDir), rayDistance, 2)
        if result.body ~= nil then
            rayDistance = Min(rayDistance, result.distance)
        end
        rayDistance = Clamp(rayDistance, CAMERA_MIN_DIST, cameraDistance)

        cameraNode.position = aimPoint + rayDir * rayDistance
        cameraNode.rotation = dir
    end
end

-- Character script object class
Character = ScriptObject()

function Character:Start()
    self.controls = Controls() -- Character controls
    self.onGround = false -- Grounded flag for movement
    self.okToJump = true -- Jump flag
    self.inAirTimer = 0 -- In air timer. Due to possible physics inaccuracy, character can be off ground for max. 1/10 second and still be allowed to move
    self:SubscribeToEvent(self.node, "NodeCollision", "Character:HandleNodeCollision")
end

function Character:Load(deserializer)
    self.controls.yaw = deserializer:ReadFloat()
    self.controls.pitch = deserializer:ReadFloat()
end

function Character:Save(serializer)
    serializer:WriteFloat(self.controls.yaw)
    serializer:WriteFloat(self.controls.pitch)
end

function Character:HandleNodeCollision(eventType, eventData)
    local contacts = eventData:GetBuffer("Contacts")

    while not contacts.eof do
        local contactPosition = contacts:ReadVector3()
        local contactNormal = contacts:ReadVector3()
        local contactDistance = contacts:ReadFloat()
        local contactImpulse = contacts:ReadFloat()

        -- If contact is below node center and mostly vertical, assume it's a ground contact
        if contactPosition.y < self.node.position.y + 1 then
            local level = Abs(contactNormal.y)
            if level > 0.75 then self.onGround = true end
        end
    end
end

function Character:FixedUpdate(timeStep)
    -- Could cache the components for faster access instead of finding them each frame
    local body = self.node:GetComponent("RigidBody")
    local animCtrl = self.node:GetComponent("AnimationController")

    -- Update the in air timer. Reset if grounded
    if not self.onGround then self.inAirTimer = self.inAirTimer + timeStep else self.inAirTimer = 0 end
    -- When character has been in air less than 1/10 second, it's still interpreted as being on ground
    local softGrounded = self.inAirTimer < INAIR_THRESHOLD_TIME

    -- Update movement & animation
    local rot = self.node.rotation
    local moveDir = Vector3.ZERO
    local velocity = body.linearVelocity
    -- Velocity on the XZ plane
    local planeVelocity = Vector3(velocity.x, 0, velocity.z)

    if self.controls:IsDown(CTRL_FORWARD) then moveDir = moveDir + Vector3.FORWARD end
    if self.controls:IsDown(CTRL_BACK) then moveDir = moveDir + Vector3.BACK end
    if self.controls:IsDown(CTRL_LEFT) then moveDir = moveDir + Vector3.LEFT end
    if self.controls:IsDown(CTRL_RIGHT) then moveDir = moveDir + Vector3.RIGHT end

    -- Normalize move vector so that diagonal strafing is not faster
    if moveDir:LengthSquared() > 0 then moveDir:Normalize() end

    -- If in air, allow control, but slower than when on ground
    if softGrounded then
        body:ApplyImpulse(rot * moveDir * MOVE_FORCE)
    else
        body:ApplyImpulse(rot * moveDir * INAIR_MOVE_FORCE)
    end

    if softGrounded then
        -- When on ground, apply a braking force to limit maximum ground velocity
        local brakeForce = planeVelocity * -BRAKE_FORCE
        body:ApplyImpulse(brakeForce)

        -- Jump. Must release jump control inbetween jumps
        if self.controls:IsDown(CTRL_JUMP) then
            if self.okToJump then
                body:ApplyImpulse(Vector3.UP * JUMP_FORCE)
                self.okToJump = false
            end
        else
            self.okToJump = true
        end
    end

    -- Play walk animation if moving on ground, otherwise fade it out
    if softGrounded and not moveDir:Equals(Vector3.ZERO) then animCtrl:PlayExclusive("Models/Jack_Walk.ani", 0, true, 0.2) else animCtrl:Stop("Models/Jack_Walk.ani", 0.2) end
    -- Set walk animation speed proportional to velocity
    animCtrl:SetSpeed("Models/Jack_Walk.ani", planeVelocity:Length() * 0.3)

	-- Set IK state (we will apply foot IK only when grounded)
	doIK = self.onGround

    -- Reset grounded flag for next frame
    self.onGround = false
end


--====================================  IK  ============================================

-- Variables
local unevenThreshold = 0.05 -- Set this threshold according to the delta between feet height in idle position/animation
local leftFoot, rightFoot, legAxis, rootBone, leftLegLength, rightLegLength, originalRootHeight

function HandleSceneDrawableUpdateFinished(eventType, eventData)
	if doIK then SolveLegIK() end -- Foot IK only when grounded
end


function CreateIKChains()
	-- Set effector & axis for foot IK chains
	leftFoot = characterNode:GetChild("Bip01_L_Foot", true)
	rightFoot = characterNode:GetChild("Bip01_R_Foot", true)
	legAxis = Vector3(0, 0, -1)

	-- Set variables that will be used later
	local skel = characterNode:GetComponent("AnimatedModel").skeleton
	rootBone = characterNode:GetChild(skel.rootBone.name, true) -- Get root bone of the skeleton as we will move it to match IK targets
	leftLegLength = skel:GetBone(leftFoot.parent.parent.name).boundingBox.size.y + skel:GetBone(leftFoot.parent.name).boundingBox.size.y -- Left thigh length + left calf length
	rightLegLength = skel:GetBone(rightFoot.parent.parent.name).boundingBox.size.y + skel:GetBone(rightFoot.parent.name).boundingBox.size.y -- Right thigh length + right calf length
	originalRootHeight = rootBone.worldPosition.y - characterNode.position.y -- Used when no animation is playing
end


function SolveLegIK()
	-- ONLY IF NO ANIMATION playing: reset rootBone height
	if not characterNode:GetComponent("AnimationController"):IsPlaying("Models/Jack_Walk.ani") then rootBone.worldPosition = Vector3(rootBone.worldPosition.x, characterNode.position.y + originalRootHeight, rootBone.worldPosition.z) end

	-- Root bone and feet height from animation keyframe and character position
	rootHeight = rootBone.worldPosition.y - characterNode.position.y
	footHeightL = leftFoot.worldPosition.y - characterNode.position.y
	footHeightR = rightFoot.worldPosition.y - characterNode.position.y

	-- Current feet position from animation keyframe
	local leftGround = leftFoot.worldPosition
	local rightGround = rightFoot.worldPosition

	-- Determine which foot should be grounded
	local leftDown, rightDown = false, false -- Reset
	if leftGround.y < rightGround.y - unevenThreshold then leftDown = true
	elseif rightGround.y < leftGround.y - unevenThreshold then rightDown = true end

	-- Left Foot target (NB: ray cast is performed from a position above the foot, but not higher than the character so that we get an accurate result when foot is currently underground)
	local result = physicsWorld:RaycastSingle(Ray(leftGround + Vector3(0, leftLegLength, 0), Vector3.DOWN), 10, 2) -- NB: restrict targets to layer 2 to discard self-collision
	leftGround = result.position
	leftDist = leftFoot.worldPosition.y - (leftGround.y + footHeightL) -- Distance from foot to ground, while preserving animation's foot offset from ground
	local leftNormal = result.normal -- Used to make foot to face along the ground normal

	-- Right Foot target (NB: ray cast is performed from a reachable position above the foot so that we get an accurate result when foot is currently underground)
	local result = physicsWorld:RaycastSingle(Ray(rightGround + Vector3(0, leftLegLength, 0), Vector3.DOWN), 10, 2) -- NB: restrict targets to layer 2 to discard self-collision
	rightGround = result.position
	rightDist = rightFoot.worldPosition.y - (rightGround.y + footHeightR) -- Distance from foot to ground, while preserving animation's foot offset from ground
	local rightNormal = result.normal -- Used to make foot to face along the ground normal

	-- Set root bone target height to reach grounded foot target position
	local heightDiff = 0
	if leftDown or leftGround.y <= rightGround.y then
		heightDiff = leftDist
		if Abs(heightDiff) > 0.001 then rightGround = rightGround + Vector3(0, heightDiff, 0) end
	elseif rightDown or rightGround.y < leftGround.y then
		heightDiff = rightDist
		if Abs(heightDiff) > 0.001 then leftGround = leftGround + Vector3(0, heightDiff, 0) end
	end

	if Abs(heightDiff) < 0.001 then return end -- Skip if heightDiff not significant

	-- Move the root bone (NB: characterNode has already been 'moved' by its physics collider)
	rootBone.worldPosition = rootBone.worldPosition - Vector3(0, heightDiff, 0)

	-- Selectively solve IK
	if not leftDown then SolveIK(leftFoot, leftGround) end
	if not rightDown then SolveIK(rightFoot, rightGround) end

	-- TODO: make foot to face along the ground normal
end


function SolveIK(effectorNode, targetPos)

	-- Get current world position for the 3 joints of the IK chain
	local startJointPos = effectorNode.parent.parent.worldPosition -- Thigh pos (hip joint)
	local midJointPos = effectorNode.parent.worldPosition -- Calf pos (knee joint)
	local effectorPos = effectorNode.worldPosition -- Foot pos (ankle joint)

	-- Direction vectors
	local thighDir = midJointPos - startJointPos -- Thigh direction
	local calfDir = effectorPos - midJointPos -- Calf direction
	local targetDir = targetPos - startJointPos -- Leg direction

	-- Direction vectors lengths
	local length1 = thighDir:Length()
	local length2 = calfDir:Length()
	local limbLength = length1 + length2
	local lengthH = targetDir:Length()
	if lengthH > limbLength then
		targetDir = targetDir * (limbLength / lengthH) * 0.999 -- Do not overshoot if target unreachable
		lengthH = targetDir:Length()
	end
	local lengthHsquared = targetDir:LengthSquared()

	-- Current knee angle (from animation keyframe)
	local kneeAngle = thighDir:Angle(calfDir)

	-- New knee angle
	local cos_theta = (lengthHsquared - thighDir:LengthSquared() - calfDir:LengthSquared()) / (2 * length1 * length2)
	if cos_theta > 1 then cos_theta = 1 elseif cos_theta < -1 then cos_theta = -1 end
	local theta = Acos(cos_theta)

	-- Quaternions for knee and hip joints
	if Abs(theta - kneeAngle) > 0.01 then
		local newKneeAngle = Quaternion((theta - kneeAngle), legAxis)
		local newHipAngle = Quaternion(-(theta - kneeAngle)*0.5, legAxis)

		-- Apply rotations
		effectorNode.parent.rotation = effectorNode.parent.rotation * newKneeAngle
		effectorNode.parent.parent.rotation = effectorNode.parent.parent.rotation * newHipAngle
	end
end
```
[/details]

http://i.imgur.com/JKTL2kJ.png

-------------------------

GoogleBot42 | 2017-01-02 01:04:49 UTC | #5

Nice!  :smiley:  I have been wanting this for a while. :stuck_out_tongue:  Do you think you can port this to C++?

-------------------------

Mike | 2017-01-02 01:04:49 UTC | #6

Yes, code is rather simple, we just have to assign the feet nodes and rotation axis, and set a boolean for toggling on/off.

-------------------------

GoogleBot42 | 2017-01-02 01:04:50 UTC | #7

Hmm I get this error when I run it... (I have lua error checking enabled in Urho3D build options)

[code][Thu Apr 23 14:40:29 2015] ERROR: Execute Lua function failed: invalid type in variable assignment.
     value is 'const Vector3'; 'Vector3' expected.[/code]

There isn't any information that says where the error is occurring though.  :frowning:

-------------------------

sabotage3d | 2017-01-02 01:05:29 UTC | #8

Have anyone ported this to C++ ?

-------------------------

globus | 2017-01-02 01:05:30 UTC | #9

You can compare this Lua script with Character demo c++ code
for understanding.

-------------------------

Mike | 2017-01-02 01:05:30 UTC | #10

I think it needs some improvement before considering porting to C++, like using octree ray casts (less expensive and more versatile than physics) and fixing a few details.

-------------------------

Mike | 2017-01-02 01:06:08 UTC | #11

I've done a few updates/fixes, set as a component and ported to AngelScript (as I almost don't use lua anymore).
It's still far from perfect as it requires some manual settings (like 'lerp', 'doIK'...) and an AnimationController (and I haven't tested how it behaves without physics).

Also I haven't found a convenient way to check if the AnimationController is playing something or not.

[spoiler]class FootIK : ScriptObject
{
	String leftFootName = "";
	String rightFootName = "";
	Vector3 legAxis;
	float unevenThreshold = 0.05; // Set this threshold according to the delta between feet height in idle position/animation
	bool doIK = true; // Allow to disable Foot IK, which is only relevant when the character is grounded

	Node@ leftFoot;
	Node@ rightFoot;
	Node@ rootBone;
	float leftLegLength = 0;
	float rightLegLength = 0;
	float originalRootHeight = 0;
	Quaternion leftFootInitialRot;
	Quaternion rightFootInitialRot;


void CreateIKChains()
{
	// Set IK chains effectors
	leftFoot = node.GetChild(leftFootName, true);
	rightFoot = node.GetChild(rightFootName, true);
	if (leftFoot is null || rightFoot is null)
	{
		log.Info("Cannot get feet nodes " + leftFootName + " and/or " + rightFootName);
		return;
	}

	if (leftFoot.parent is null || leftFoot.parent.parent is null || rightFoot.parent is null || rightFoot.parent.parent is null)
		return;

	// Set variables
	AnimatedModel@ model = node.GetComponent("AnimatedModel");
	Skeleton@ skel = model.skeleton;
	if (skel is null) return;
	rootBone = node.GetChild(skel.rootBone.name, true); // Get root bone of the skeleton as we will move its node up/down to match IK targets

	leftLegLength = skel.GetBone(leftFoot.parent.parent.name).boundingBox.size.y + skel.GetBone(leftFoot.parent.name).boundingBox.size.y; // Left thigh length + left calf length
	rightLegLength = skel.GetBone(rightFoot.parent.parent.name).boundingBox.size.y + skel.GetBone(rightFoot.parent.name).boundingBox.size.y; // Right thigh length + right calf length
	originalRootHeight = rootBone.worldPosition.y - node.position.y; // Used when no animation is playing

	// Keep track of initial rotation in case no animation is playing
	leftFootInitialRot = skel.GetBone(leftFootName).initialRotation;
	rightFootInitialRot = skel.GetBone(rightFootName).initialRotation;

	// Subscribe to the SceneDrawableUpdateFinished event which is triggered after the animations have been updated, so we can apply IK to override them
	SubscribeToEvent("SceneDrawableUpdateFinished", "HandleSceneDrawableUpdateFinished");
}


void HandleSceneDrawableUpdateFinished(StringHash eventType, VariantMap& eventData)
{
	if (doIK) SolveLegIK(eventData["TimeStep"].GetFloat());
}


void SolveIKUrho(Node@ effectorNode, Vector3 targetPos)
{
	// Get current world position for the 3 joints of the IK chain
	Vector3 startJointPos = effectorNode.parent.parent.worldPosition; // Thigh pos (hip joint)
	Vector3 midJointPos = effectorNode.parent.worldPosition; // Calf pos (knee joint)
	Vector3 effectorPos = effectorNode.worldPosition; // Foot pos (ankle joint)

	// Direction vectors
	Vector3 thighDir = midJointPos - startJointPos; // Thigh direction
	Vector3 calfDir = effectorPos - midJointPos; // Calf direction
	Vector3 targetDir = targetPos - startJointPos; // Leg direction

	// Vectors lengths
	float length1 = thighDir.length;
	float length2 = calfDir.length;
	float limbLength = length1 + length2;
	float lengthH = targetDir.length;
	if (lengthH > limbLength)
	{
		targetDir = targetDir * (limbLength / lengthH) * 0.999; // Do not overshoot if target unreachable
		lengthH = targetDir.length;
	}
	float lengthHsquared = targetDir.lengthSquared;

	// Current knee angle (from animation keyframe)
	float kneeAngle = thighDir.Angle(calfDir);

	// New knee angle
	float cos_theta = (lengthHsquared - thighDir.lengthSquared - calfDir.lengthSquared) / (2 * length1 * length2);
	if (cos_theta > 1) cos_theta = 1; else if (cos_theta < -1) cos_theta = -1;
	float theta = Acos(cos_theta);

	// Quaternions for knee and hip joints
	if (Abs(theta - kneeAngle) > 0.01)
	{
		Quaternion deltaKnee = Quaternion((theta - kneeAngle), legAxis);
		Quaternion deltaHip = Quaternion(-(theta - kneeAngle) * 0.5, legAxis);

		// Apply rotations
		effectorNode.parent.rotation = effectorNode.parent.rotation * deltaKnee;
		effectorNode.parent.parent.rotation = effectorNode.parent.parent.rotation * deltaHip;
	}
}


void SolveLegIK(float timeStep)
{
	// ONLY IF NO ANIMATION playing: reset rootBone height
	AnimationController@ animCtrl = node.GetComponent("AnimationController");
	if (node.name == "Jack" && !animCtrl.IsPlaying("Models/Jack_Walk.ani"))
		rootBone.worldPosition = Vector3(rootBone.worldPosition.x, node.position.y + originalRootHeight, rootBone.worldPosition.z);

	// Root bone and feet height from animation keyframe and character node position
	float footHeightL = leftFoot.worldPosition.y - node.position.y;
	float footHeightR = rightFoot.worldPosition.y - node.position.y;

	// Current feet position from animation keyframe
	Vector3 leftGround = leftFoot.worldPosition;
	Vector3 rightGround = rightFoot.worldPosition;

	Octree@ octree = scene.octree;
	float leftHeightDiff = 0; // Distance from left foot to ground, while preserving animation's foot offset from ground
	float rightHeightDiff = 0; // Distance from right foot to ground, while preserving animation's foot offset from ground
	Vector3 leftNormal = Vector3(0, 0, 0);
	Vector3 rightNormal = Vector3(0, 0, 0);

	// Left Foot (NB: ray cast is performed from a position above the foot, but not higher than the character so that we get an accurate result when foot is currently underground)
	RayQueryResult result = octree.RaycastSingle(Ray(leftGround + Vector3(0, leftLegLength, 0), Vector3(0, -1, 0)), RAY_TRIANGLE, 10, DRAWABLE_GEOMETRY, 63); // NB: skip last 2 view mask layers that contain self, foot effects, cutouts...
	if (result.drawable !is null)
	{
		leftGround = result.position;
		leftHeightDiff = leftFoot.worldPosition.y - (leftGround.y + footHeightL); // Distance from foot to ground, while preserving animation's foot offset from ground
		leftNormal = result.normal; // Used to make foot to face along the ground normal
	}

	// Right Foot (NB: ray cast is performed from a position above the foot, but not higher than the character so that we get an accurate result when foot is currently underground)
	RayQueryResult result2 = octree.RaycastSingle(Ray(rightGround + Vector3(0, rightLegLength, 0), Vector3(0, -1, 0)), RAY_TRIANGLE, 10, DRAWABLE_GEOMETRY, 63); // NB: skip last 2 view mask layers that contain self, foot effects, cutouts...
	if (result2.drawable !is null)
	{
		rightGround = result2.position;
		rightHeightDiff = rightFoot.worldPosition.y - (rightGround.y + footHeightR); // Distance from foot to ground, while preserving animation's foot offset from ground
		rightNormal = result2.normal; // Used to make foot to face along the ground normal
	}

	// Feet are facing ground normal
	if (node.name == "Jack" && !animCtrl.IsPlaying("Models/Jack_Walk.ani")) // When no animation is playing, manually reset rotation (when an animation is playing, rotation is reset by the keyframe)
	{
		leftFoot.rotation = leftFootInitialRot;
		rightFoot.rotation = rightFootInitialRot;
	}
	leftFoot.worldRotation = Quaternion(Vector3(0, 1, 0), leftNormal) * leftFoot.worldRotation;
	rightFoot.worldRotation = Quaternion(Vector3(0, 1, 0), rightNormal) * rightFoot.worldRotation;

	// Skip grounding if flat ground
	if(Abs(rightHeightDiff - leftHeightDiff) < 0.001) return;

	// From animation keyframe, determine which foot should be grounded
	bool leftDown = false;
	bool rightDown = false;
	if (leftGround.y < rightGround.y - unevenThreshold) leftDown = true;
	else if (rightGround.y < leftGround.y - unevenThreshold) rightDown = true;

	// If feet are at even level in animation, ground at lowest ray cast level
	if (!leftDown && !rightDown)
	{
		if (leftGround.y < rightGround.y) leftDown = true; else rightDown = true;
	}

	// Set root bone offset to reach grounded foot target position. Also update non grounded foot from this offset
	float heightDiff = 0;
	if (leftDown)
	{
		heightDiff = leftHeightDiff;
		rightGround = rightGround + Vector3(0, heightDiff, 0);
	}
	else if (rightDown)
	{
		heightDiff = rightHeightDiff;
		leftGround = leftGround + Vector3(0, heightDiff, 0);
	}

	// Move the root bone (NB: node has already been 'moved' by its physics collider)
	rootBone.worldPosition = rootBone.worldPosition - Vector3(0, heightDiff, 0);

	// Selectively solve IK
	if (!leftDown) SolveIKUrho(leftFoot, leftGround);
	if (!rightDown) SolveIKUrho(rightFoot, rightGround);
}

}[/spoiler]
[spoiler]#include "Scripts/Utilities/Sample.as"
#include "Scripts/Utilities/Touch.as"
#include "Scripts/Perso/Foot_IK.as"

const int CTRL_FORWARD = 1;
const int CTRL_BACK = 2;
const int CTRL_LEFT = 4;
const int CTRL_RIGHT = 8;
const int CTRL_JUMP = 16;

const float MOVE_FORCE = 0.8f;
const float INAIR_MOVE_FORCE = 0.02f;
const float BRAKE_FORCE = 0.2f;
const float JUMP_FORCE = 7.0f;
const float YAW_SENSITIVITY = 0.1f;
const float INAIR_THRESHOLD_TIME = 0.1f;
bool firstPerson = false; // First person camera flag

Node@ characterNode;
String characterName = "Jack"; // Character to create, from "Jack", "Ninja" or a prefab character


void Start()
{
	SampleStart(); // Execute the common startup for samples
	CreateScene(); // Create static scene content

	// Create the controllable character
	if (characterName == "Jack") CreateJack();
	else if (characterName == "Ninja") CreateNinja();
	else CreateCharacter(characterName);

	CreateInstructions(); // Create the UI content
	SubscribeToEvents(); // Subscribe to necessary events
}

void CreateScene()
{
	scene_ = Scene();

	// Create scene subsystem components
	scene_.CreateComponent("Octree");
	scene_.CreateComponent("PhysicsWorld");
	scene_.CreateComponent("DebugRenderer");

	// Create camera and define viewport. Camera does not necessarily have to belong to the scene
	cameraNode = Node();
	Camera@ camera = cameraNode.CreateComponent("Camera");
	camera.farClip = 300.0f;
	renderer.viewports[0] = Viewport(scene_, camera);

	// Create a Zone component for ambient lighting & fog control
	Node@ zoneNode = scene_.CreateChild("Zone");
	Zone@ zone = zoneNode.CreateComponent("Zone");
	zone.boundingBox = BoundingBox(-1000.0f, 1000.0f);
	zone.ambientColor = Color(0.15f, 0.15f, 0.15f);
	zone.fogColor = Color(0.5f, 0.5f, 0.7f);
	zone.fogStart = 100.0f;
	zone.fogEnd = 300.0f;

	// Create a directional light to the world. Enable cascaded shadows on it
	Node@ lightNode = scene_.CreateChild("DirectionalLight");
	lightNode.direction = Vector3(0.6f, -1.0f, 0.8f);
	Light@ light = lightNode.CreateComponent("Light");
	light.lightType = LIGHT_DIRECTIONAL;
	light.castShadows = true;
	light.shadowBias = BiasParameters(0.00025f, 0.5f);
	// Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
	light.shadowCascade = CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f);

	// Create the floor object
	Node@ floorNode = scene_.CreateChild("Floor");
	floorNode.position = Vector3(0.0f, -0.5f, 0.0f);
	floorNode.scale = Vector3(200.0f, 1.0f, 200.0f);
	StaticModel@ object = floorNode.CreateComponent("StaticModel");
	object.model = cache.GetResource("Model", "Models/Box.mdl");
	object.material = cache.GetResource("Material", "Materials/Stone.xml");

	RigidBody@ body = floorNode.CreateComponent("RigidBody");
	// Use collision layer bit 2 to mark world scenery. This is what we will raycast against to prevent camera from going inside geometry
	body.collisionLayer = 2;
	CollisionShape@ shape = floorNode.CreateComponent("CollisionShape");
	shape.SetBox(Vector3(1.0f, 1.0f, 1.0f));

	// Create mushrooms of varying sizes
	const uint NUM_MUSHROOMS = 60;
	for (uint i = 0; i < NUM_MUSHROOMS; ++i)
	{
		Node@ objectNode = scene_.CreateChild("Mushroom");
		objectNode.position = Vector3(Random(180.0f) - 90.0f, 0.0f, Random(180.0f) - 90.0f);
		objectNode.rotation = Quaternion(0.0f, Random(360.0f), 0.0f);
		objectNode.SetScale(2.0f + Random(5.0f));
		StaticModel@ object = objectNode.CreateComponent("StaticModel");
		object.model = cache.GetResource("Model", "Models/Mushroom.mdl");
		object.material = cache.GetResource("Material", "Materials/Mushroom.xml");
		object.castShadows = true;

		RigidBody@ body = objectNode.CreateComponent("RigidBody");
		body.collisionLayer = 2;
		CollisionShape@ shape = objectNode.CreateComponent("CollisionShape");
		shape.SetTriangleMesh(object.model, 0);
	}

	// Create movable boxes. Let them fall from the sky at first
	const uint NUM_BOXES = 100;
	for (uint i = 0; i < NUM_BOXES; ++i)
	{
		float scale = Random(2.0f) + 0.5f;

		Node@ objectNode = scene_.CreateChild("Box");
		objectNode.position = Vector3(Random(180.0f) - 90.0f, Random(10.0f) + 10.0f, Random(180.0f) - 90.0f);
		objectNode.rotation = Quaternion(Random(360.0f), Random(360.0f), Random(360.0f));
		objectNode.SetScale(scale);
		StaticModel@ object = objectNode.CreateComponent("StaticModel");
		object.model = cache.GetResource("Model", "Models/Box.mdl");
		object.material = cache.GetResource("Material", "Materials/Stone.xml");
		object.castShadows = true;

		RigidBody@ body = objectNode.CreateComponent("RigidBody");
		body.collisionLayer = 2;
		// Bigger boxes will be heavier and harder to move
		body.mass = scale * 2.0f;
		CollisionShape@ shape = objectNode.CreateComponent("CollisionShape");
		shape.SetBox(Vector3(1.0f, 1.0f, 1.0f));
	}

	// STEEP
	Node@ slope = scene_.CreateChild("Slope");
	slope.scale = Vector3(10, 1, 5);
	slope.position = Vector3(0, 1.5, 5);
	slope.rotation = Quaternion(0, -90, 25);
	StaticModel@ model = slope.CreateComponent("StaticModel");
	model.model = cache.GetResource("Model", "Models/Box.mdl");
	model.material = cache.GetResource("Material", "Materials/Stone.xml");

	RigidBody@ steepBody = slope.CreateComponent("RigidBody");
	steepBody.collisionLayer = 2;
	CollisionShape@ steepShape = slope.CreateComponent("CollisionShape");
	steepShape.SetBox(Vector3(1, 1, 1));
}

void CreateJack()
{
	characterNode = scene_.CreateChild("Jack");

	// Create the rendering component + animation controller
	AnimatedModel@ object = characterNode.CreateComponent("AnimatedModel");
	object.model = cache.GetResource("Model", "Models/Jack.mdl");
	object.material = cache.GetResource("Material", "Materials/Jack.xml");
	object.castShadows = true;
	characterNode.CreateComponent("AnimationController");
	object.viewMask = 64; // Enable layer 7 only, to skip when raycasting the octree

	// Create rigidbody, and set non-zero mass so that the body becomes dynamic
	RigidBody@ body = characterNode.CreateComponent("RigidBody");
	body.collisionLayer = 1;
	body.mass = 1;

	// Set zero angular factor so that physics doesn't turn the character on its own.
	// Instead we will control the character yaw manually
	body.angularFactor = Vector3(0, 0, 0);

	// Set the rigidbody to signal collision also when in rest, so that we get ground collisions properly
	body.collisionEventMode = COLLISION_ALWAYS;

	// Set a capsule shape for collision
	CollisionShape@ shape = characterNode.CreateComponent("CollisionShape");
	shape.SetCapsule(0.6, 1.8, Vector3(0, 0.9, 0));

	// Create the character logic object, which takes care of steering the rigidbody
	characterNode.CreateScriptObject(scriptFile, "Character");

	// Create a foot IK script object
	FootIK@ footIK = cast<FootIK>(characterNode.CreateScriptObject(scriptFile, "FootIK"));
	footIK.leftFootName = "Bip01_L_Foot";
	footIK.rightFootName = "Bip01_R_Foot";
	footIK.legAxis = Vector3(0, 0, -1);
	footIK.CreateIKChains();
}


void CreateCharacter(String name)
{
	characterNode = scene_.InstantiateXML(cache.GetFile("Assets/" + name + "/Objects/" + name + ".xml"), Vector3(0, 0, 0), Quaternion(0, 0, 0));
	characterNode.CreateComponent("AnimationController");
	characterNode.CreateScriptObject(scriptFile, "Character");
	AnimatedModel@ model = characterNode.GetComponent("AnimatedModel");
	model.viewMask = 64; // Enable layer 7 only, to skip when raycasting the octree

	// Create a foot IK script object
	FootIK@ footIK = cast<FootIK>(characterNode.CreateScriptObject(scriptFile, "FootIK"));
	footIK.leftFootName = "Foot.L";
	footIK.rightFootName = "Foot.R";
	footIK.legAxis = Vector3(-1, 0, 0);
	footIK.CreateIKChains();
}


void CreateNinja()
{
	characterNode = scene_.CreateChild("Ninja");

	// Create the rendering component + animation controller
	AnimatedModel@ object = characterNode.CreateComponent("AnimatedModel");
	object.model = cache.GetResource("Model", "Models/NinjaSnowWar/Ninja.mdl");
	object.material = cache.GetResource("Material", "Materials/NinjaSnowWar/Ninja.xml");
	object.castShadows = true;
	characterNode.CreateComponent("AnimationController");
	object.viewMask = 64; // Enable layer 7 only, to skip when raycasting the octree

	// Create rigidbody, and set non-zero mass so that the body becomes dynamic
	RigidBody@ body = characterNode.CreateComponent("RigidBody");
	body.collisionLayer = 1;
	body.mass = 1;

	// Set zero angular factor so that physics doesn't turn the character on its own.
	// Instead we will control the character yaw manually
	body.angularFactor = Vector3(0, 0, 0);

	// Set the rigidbody to signal collision also when in rest, so that we get ground collisions properly
	body.collisionEventMode = COLLISION_ALWAYS;

	// Set a capsule shape for collision
	CollisionShape@ shape = characterNode.CreateComponent("CollisionShape");
	shape.SetCapsule(0.5, 1.8, Vector3(0, 0.9, 0));

	// Create the character logic object, which takes care of steering the rigidbody
	characterNode.CreateScriptObject(scriptFile, "Character");

	// Create a foot IK script object
	FootIK@ footIK = cast<FootIK>(characterNode.CreateScriptObject(scriptFile, "FootIK"));
	footIK.leftFootName = "Joint20";
	footIK.rightFootName = "Joint25";
	footIK.legAxis = Vector3(1, 0, 0);
	footIK.CreateIKChains();
}

void CreateInstructions()
{
	// Construct new Text object, set string to display and font to use
	Text@ instructionText = ui.root.CreateChild("Text", "Instructions");
	instructionText.text = "Use WASD keys and mouse to move\n" "Space to jump, F to toggle 1st/3rd person\n" "F5 to save scene, F7 to load";
	instructionText.SetFont(cache.GetResource("Font", "Fonts/Anonymous Pro.ttf"), 15);
	// The text has multiple rows. Center them in relation to each other
	instructionText.textAlignment = HA_CENTER;

	// Position the text relative to the screen center
	instructionText.horizontalAlignment = HA_CENTER;
	instructionText.verticalAlignment = VA_CENTER;
	instructionText.SetPosition(0, ui.root.height / 4);
}

void SubscribeToEvents()
{
	SubscribeToEvent("Update", "HandleUpdate"); // Subscribe to Update event for setting the character controls before physics simulation
	SubscribeToEvent("PostUpdate", "HandlePostUpdate"); // Subscribe to PostUpdate event for updating the camera position after physics simulation
	UnsubscribeFromEvent("SceneUpdate"); // Unsubscribe the SceneUpdate event from base class as the camera node is being controlled in HandlePostUpdate() in this sample
	SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate"); // Process post-render update event, during which we request debug geometry
}

void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
	if (characterNode is null)
		return;

	Character@ character = cast<Character>(characterNode.scriptObject);
	if (character is null)
		return;

	// Clear previous controls
	character.controls.Set(CTRL_FORWARD | CTRL_BACK | CTRL_LEFT | CTRL_RIGHT | CTRL_JUMP, false);

	// Update controls using touch utility
	if (touchEnabled)
		UpdateTouches(character.controls);

	// Update controls using keys (desktop)
	if (ui.focusElement is null)
	{
		if (touchEnabled || !useGyroscope)
		{
			character.controls.Set(CTRL_FORWARD, input.keyDown[KEY_UP]);
			character.controls.Set(CTRL_BACK, input.keyDown[KEY_DOWN]);
			character.controls.Set(CTRL_LEFT, input.keyDown[KEY_LEFT]);
			character.controls.Set(CTRL_RIGHT, input.keyDown[KEY_RIGHT]);
		}
		character.controls.Set(CTRL_JUMP, input.keyDown[KEY_SPACE]);

		// Add character yaw & pitch from the mouse motion or touch input
		if (touchEnabled)
		{
			for (uint i = 0; i < input.numTouches; ++i)
			{
				TouchState@ state = input.touches[i];
				if (state.touchedElement is null) // Touch on empty space
				{
					Camera@ camera = cameraNode.GetComponent("Camera");
					if (camera is null)
						return;

					character.controls.yaw += TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.x;
					character.controls.pitch += TOUCH_SENSITIVITY * camera.fov / graphics.height * state.delta.y;
				}
			}
		}
		else
		{
			character.controls.yaw += input.mouseMoveX * YAW_SENSITIVITY;
			character.controls.pitch += input.mouseMoveY * YAW_SENSITIVITY;
		}
		// Limit pitch
		character.controls.pitch = Clamp(character.controls.pitch, -80.0f, 80.0f);

		// Switch between 1st and 3rd person
		if (input.keyPress['F'])
			firstPerson = !firstPerson;

		// Turn on/off gyroscope on mobile platform
		if (input.keyPress['G'])
			useGyroscope = !useGyroscope;

		// Check for loading / saving the scene
		if (input.keyPress[KEY_F5])
		{
			File saveFile(fileSystem.programDir + "Data/Scenes/CharacterDemo.xml", FILE_WRITE);
			scene_.SaveXML(saveFile);
		}
		if (input.keyPress[KEY_F7])
		{
			File loadFile(fileSystem.programDir + "Data/Scenes/CharacterDemo.xml", FILE_READ);
			scene_.LoadXML(loadFile);
			// After loading we have to reacquire the character scene node, as it has been recreated
			// Simply find by name as there's only one of them
			characterNode = scene_.GetChild("Jack", true);
			if (characterNode is null)
				return;
		}
	}

	// Set rotation already here so that it's updated every rendering frame instead of every physics frame
	characterNode.rotation = Quaternion(character.controls.yaw, Vector3(0.0f, 1.0f, 0.0f));

	// Toggle debug geometry with 'Z'
	if (input.keyPress[KEY_Z]) drawDebug = !drawDebug;
}

void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
	if (drawDebug) scene_.physicsWorld.DrawDebugGeometry(true); // Draw physics debug geometry. Use depth test to make the result easier to interpret
}

void HandlePostUpdate(StringHash eventType, VariantMap& eventData)
{
	if (characterNode is null)
		return;

	Character@ character = cast<Character>(characterNode.scriptObject);
	if (character is null)
		return;

	// Get camera lookat dir from character yaw + pitch
	Quaternion rot = characterNode.rotation;
	Quaternion dir = rot * Quaternion(character.controls.pitch, Vector3(1.0f, 0.0f, 0.0f));

	// Third person camera: position behind the character
	Vector3 aimPoint = characterNode.position + rot * Vector3(0.0f, 1.7f, 0.0f); // You can modify x Vector3 value to translate the fixed character position (indicative range[-2;2])

	// Collide camera ray with static physics objects (layer bitmask 2) to ensure we see the character properly
	Vector3 rayDir = dir * Vector3(0.0f, 0.0f, -1.0f); // For indoor scenes you can use dir * Vector3(0.0, 0.0, -0.5) to prevent camera from crossing the walls
	float rayDistance = cameraDistance;
	PhysicsRaycastResult result = scene_.physicsWorld.RaycastSingle(Ray(aimPoint, rayDir), rayDistance, 2);
	if (result.body !is null)
		rayDistance = Min(rayDistance, result.distance);
	rayDistance = Clamp(rayDistance, CAMERA_MIN_DIST, cameraDistance);

	cameraNode.position = aimPoint + rayDir * rayDistance;
	cameraNode.rotation = dir;
}

// Character script object class
//
// Those public member variables that can be expressed with a Variant and do not begin with an underscore are automatically
// loaded / saved as attributes of the ScriptInstance component. We also have variables which can not be automatically saved
// (yaw and pitch inside the Controls object) so we write manual binary format load / save methods for them. These functions
// will be called by ScriptInstance when the script object is being loaded or saved.
class Character : ScriptObject
{
	// Character controls.
	Controls controls;
	// Grounded flag for movement.
	bool onGround = false;
	// Jump flag.
	bool okToJump = true;
	// In air timer. Due to possible physics inaccuracy, character can be off ground for max. 1/10 second and still be allowed to move.
	float inAirTimer = 0.0f;

	void Start()
	{
		SubscribeToEvent(node, "NodeCollision", "HandleNodeCollision");
	}

	void Load(Deserializer& deserializer)
	{
		controls.yaw = deserializer.ReadFloat();
		controls.pitch = deserializer.ReadFloat();
	}

	void Save(Serializer& serializer)
	{
		serializer.WriteFloat(controls.yaw);
		serializer.WriteFloat(controls.pitch);
	}

	void HandleNodeCollision(StringHash eventType, VariantMap& eventData)
	{
		VectorBuffer contacts = eventData["Contacts"].GetBuffer();

		while (!contacts.eof)
		{
			Vector3 contactPosition = contacts.ReadVector3();
			Vector3 contactNormal = contacts.ReadVector3();
			float contactDistance = contacts.ReadFloat();
			float contactImpulse = contacts.ReadFloat();

			// If contact is below node center and mostly vertical, assume it's a ground contact
			if (contactPosition.y < (node.position.y + 1.0f))
			{
				float level = Abs(contactNormal.y);
				if (level > 0.75)
					onGround = true;
			}
		}
	}

	void FixedUpdate(float timeStep)
	{
		/// \todo Could cache the components for faster access instead of finding them each frame
		RigidBody@ body = node.GetComponent("RigidBody");
		AnimationController@ animCtrl = node.GetComponent("AnimationController");
		FootIK@ footIK = cast<FootIK>(characterNode.GetScriptObject("FootIK"));

		// Update the in air timer. Reset if grounded
		if (!onGround)
			inAirTimer += timeStep;
		else
			inAirTimer = 0.0f;
		// When character has been in air less than 1/10 second, it's still interpreted as being on ground
		bool softGrounded = inAirTimer < INAIR_THRESHOLD_TIME;

		// Update movement & animation
		Quaternion rot = node.rotation;
		Vector3 moveDir(0.0f, 0.0f, 0.0f);
		Vector3 velocity = body.linearVelocity;
		// Velocity on the XZ plane
		Vector3 planeVelocity(velocity.x, 0.0f, velocity.z);

		if (controls.IsDown(CTRL_FORWARD))
			moveDir += Vector3(0.0f, 0.0f, 1.0f);
		if (controls.IsDown(CTRL_BACK))
			moveDir += Vector3(0.0f, 0.0f, -1.0f);
		if (controls.IsDown(CTRL_LEFT))
			moveDir += Vector3(-1.0f, 0.0f, 0.0f);
		if (controls.IsDown(CTRL_RIGHT))
			moveDir += Vector3(1.0f, 0.0f, 0.0f);

		// Normalize move vector so that diagonal strafing is not faster
		if (moveDir.lengthSquared > 0.0f)
			moveDir.Normalize();

		// If in air, allow control, but slower than when on ground
		body.ApplyImpulse(rot * moveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE));

		if (softGrounded)
		{
			// When on ground, apply a braking force to limit maximum ground velocity
			Vector3 brakeForce = -planeVelocity * BRAKE_FORCE;
			body.ApplyImpulse(brakeForce);

			// Jump. Must release jump control inbetween jumps
			if (controls.IsDown(CTRL_JUMP))
			{
				if (okToJump)
				{
					body.ApplyImpulse(Vector3(0.0f, 1.0f, 0.0f) * JUMP_FORCE);
					okToJump = false;
				}
			}
			else
				okToJump = true;
		}

		// Play walk animation if moving on ground, otherwise fade it out
		if (softGrounded && !moveDir.Equals(Vector3(0, 0, 0)))
		{
			if (characterName == "Jack") animCtrl.PlayExclusive("Models/Jack_Walk.ani", 0, true, 0.2);
			else if (characterName == "Ninja") animCtrl.PlayExclusive("Models/NinjaSnowWar/Ninja_Walk.ani", 0, true, 0.2);
			else animCtrl.PlayExclusive("Assets/" + characterName + "/Models/Run.ani", 0, true, 0.2);
		}
		else
		{
			if (characterName == "Jack") animCtrl.Stop("Models/Jack_Walk.ani", 0.2);
			else if (characterName == "Ninja") animCtrl.PlayExclusive("Models/NinjaSnowWar/Ninja_Idle2.ani", 0, true, 0.2);
			else animCtrl.PlayExclusive("Assets/" + characterName + "/Models/Idle.ani", 0, true, 0.2);
		}

		// Set walk animation speed proportional to velocity
		animCtrl.SetSpeed("Models/Jack_Walk.ani", planeVelocity.length * 0.3f);
		animCtrl.SetSpeed("Models/NinjaSnowWar/Ninja_Walk.ani", planeVelocity.length * 0.3f);
		animCtrl.SetSpeed("Assets/" + characterName + "/Models/Run.ani", planeVelocity.length * 0.3);

		// Set IK state (we will apply foot IK only when grounded!)
		footIK.doIK = onGround;

		// Reset grounded flag for next frame
		onGround = false;
	}
}


// Create XML patch instructions for screen joystick layout specific to this sample app
String patchInstructions =
		"<patch>" +
		"	<add sel=\"/element\">" +
		"		<element type=\"Button\">" +
		"			<attribute name=\"Name\" value=\"Button3\" />" +
		"			<attribute name=\"Position\" value=\"-120 -120\" />" +
		"			<attribute name=\"Size\" value=\"96 96\" />" +
		"			<attribute name=\"Horiz Alignment\" value=\"Right\" />" +
		"			<attribute name=\"Vert Alignment\" value=\"Bottom\" />" +
		"			<attribute name=\"Texture\" value=\"Texture2D;Textures/TouchInput.png\" />" +
		"			<attribute name=\"Image Rect\" value=\"96 0 192 96\" />" +
		"			<attribute name=\"Hover Image Offset\" value=\"0 0\" />" +
		"			<attribute name=\"Pressed Image Offset\" value=\"0 0\" />" +
		"			<element type=\"Text\">" +
		"				<attribute name=\"Name\" value=\"Label\" />" +
		"				<attribute name=\"Horiz Alignment\" value=\"Center\" />" +
		"				<attribute name=\"Vert Alignment\" value=\"Center\" />" +
		"				<attribute name=\"Color\" value=\"0 0 0 1\" />" +
		"				<attribute name=\"Text\" value=\"Gyroscope\" />" +
		"			</element>" +
		"			<element type=\"Text\">" +
		"				<attribute name=\"Name\" value=\"KeyBinding\" />" +
		"				<attribute name=\"Text\" value=\"G\" />" +
		"			</element>" +
		"		</element>" +
		"	</add>" +
		"	<remove sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/attribute[@name='Is Visible']\" />" +
		"	<replace sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">1st/3rd</replace>" +
		"	<add sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]\">" +
		"		<element type=\"Text\">" +
		"			<attribute name=\"Name\" value=\"KeyBinding\" />" +
		"			<attribute name=\"Text\" value=\"F\" />" +
		"		</element>" +
		"	</add>" +
		"	<remove sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/attribute[@name='Is Visible']\" />" +
		"	<replace sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Jump</replace>" +
		"	<add sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]\">" +
		"		<element type=\"Text\">" +
		"			<attribute name=\"Name\" value=\"KeyBinding\" />" +
		"			<attribute name=\"Text\" value=\"SPACE\" />" +
		"		</element>" +
		"	</add>" +
		"</patch>";[/spoiler]

EDIT:
- lerp no longer needed
- tested OK without physics and with a crowd agent
- removed AnimationController dependency
- ported to C++ (needs some tests before publishing)

-------------------------

christianclavet | 2017-01-02 01:06:09 UTC | #12

This is simply incredible! IK combined with animation! Wow!
Are the LUA events commands are the same on C++? Code look easy to port!

-------------------------

