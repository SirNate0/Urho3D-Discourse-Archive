Mike | 2017-01-02 00:57:46 UTC | #1

What are the steps required to fully remove a scene/level and to init a new one?

I've checked functions like Clear(), SetUpdateEnabled(), ReleaseAllResources() and the Scene destructor ~Scene() but not sure if they are required and don't know how to use the scene destructor.

-------------------------

NemesisFS | 2017-01-02 00:57:46 UTC | #2

I think you just need to delete the old viewport and scene and create new ones.

-------------------------

cadaver | 2017-01-02 00:57:46 UTC | #3

When you Load() or LoadXML() content into a scene object, all previous content is cleared first.

The alternative is to create a new scene object, but it actually shouldn't be necessary, unless you want to retain multiple scenes and return to the previous one quickly. When you have multiple scenes in memory and don't want all of them to update, in that case you can call SetUpdateEnabled(false) to the one that shouldn't be updated.

After a scene change ReleaseAllResources(false) will clear out everything from the cache that is not currently being used, and that's a good practice. ReleaseAllResources(true) forces release of also used resources (but SharedPtr's keeping them alive elsewhere will not be cleared, so it's kind of useless) and is not recommended.

-------------------------

Mike | 2017-01-02 00:57:47 UTC | #4

Many thanks for detailed explanations,

Now the question is how to call the main script file after loading?
I've tried require"myScript" just after scene_:LoadXML("...EmptyScene.xml") but it produces a segmentation fault.

For example, let's say I want to "load" 06_SkeletalAnimation.lua when pressing a button in Example#2 (02_HelloGui.lua). And once pressed, I don't want to keep Example#2 alive (fully remove it).

-------------------------

cadaver | 2017-01-02 00:57:47 UTC | #5

Lua scripts are a bit different than scenes. They are all loaded into the same Lua state but cannot be unloaded.

I would recommend structuring the Lua application so that the main program script is always present and only object scripts are loaded when necessary (these btw. work in the same way, they cannot be unloaded)

Aster (author of Lua script system) will know better what's possible to change/improve in this respect.

-------------------------

Mike | 2017-01-02 00:57:47 UTC | #6

Thanks, hope that will be easily fixed.
Looking forward for Aster tips, I've seen that he recently pushed some new commits regarding Load and Save.

-------------------------

aster2013 | 2017-01-02 00:57:47 UTC | #7

Hi, mike.
I have made a Lua sample for you.  Please get it here [code]https://dl.dropboxusercontent.com/u/56770481/SwitchScene.lua[/code]
Please attention to that in the sample, We create scene with Scene:new() not Scene(), and it is need to destroy scene manual by call scene:delete() at the Stop function.

-------------------------

Mike | 2017-01-02 00:57:50 UTC | #8

Really nice, Aster. Thanks a lot  :wink: 

I've managed to integrate this technique with my file structure/splitting and it seems to work fine. I can build my levels as independant levels and "merge" them with only few modifications. That's great!

-------------------------

adekto | 2017-01-02 01:14:26 UTC | #9

[quote="aster2013"]Hi, mike.
I have made a Lua sample for you.  Please get it here [code]https://dl.dropboxusercontent.com/u/56770481/SwitchScene.lua[/code]
Please attention to that in the sample, We create scene with Scene:new() not Scene(), and it is need to destroy scene manual by call scene:delete() at the Stop function.[/quote]

anyone still has that script?

-------------------------

Mike | 2017-01-02 01:14:26 UTC | #10

Yes, I 'll be able to access it saturday if no one can supply it in the meantime.

-------------------------

adekto | 2017-01-02 01:14:26 UTC | #11

great, thank you in advance
trying to find all the lua code right now, but seems not allot of people use that side of the engine  :confused:

-------------------------

Mike | 2017-01-02 01:14:29 UTC | #12

Here is the SwitchScene.lua script:
[spoiler][code]
-- Switch scene.
require "LuaScripts/Utilities/Sample"

local window = nil
local windowTitle = nil

local scene_ = nil
local sceneIndex_ = -1
local cameraNode = nil
local yaw = 0.0
local pitch = 0.0

function Start()
    -- Execute the common startup for samples
    SampleStart()

    -- Enable OS cursor
    input.mouseVisible = true

    -- Load XML file containing default UI style sheet
    local style = cache:GetResource("XMLFile", "UI/DefaultStyle.xml")

    -- Set the loaded style as default style
    ui.root.defaultStyle = style

    -- Initialize Window
    InitWindow()

    -- Create and add some controls to the Window
    InitControls()

    SubscribeToEvents()

    SwitchScene(0)
end

function Stop()
    if scene_ ~= nil then
        scene_:delete()
    end
end

function InitControls()
    -- Create a Button
    local button = Button:new()
    button:SetName("Button")
    button.minHeight = 24

    -- Add controls to Window
    window:AddChild(button)

    button:SetStyleAuto()
end

function InitWindow()
    -- Create the Window and add it to the UI's root node
    window = Window:new()
    ui.root:AddChild(window)
    
    -- Set Window size and layout settings
    window.minWidth = 384;
    window:SetLayout(LM_VERTICAL, 6, IntRect(6, 6, 6, 6))
    window:SetAlignment(HA_CENTER, VA_CENTER)
    window:SetName("Window")
    
    -- Create Window 'titlebar' container
    local titleBar = UIElement:new()
    titleBar:SetMinSize(0, 24)
    titleBar.verticalAlignment = VA_TOP
    titleBar.layoutMode = LM_HORIZONTAL

    -- Create the Window title Text
    windowTitle = Text:new()
    windowTitle.name = "WindowTitle"
    
    -- Create the Window's close button
    local buttonClose = Button:new()
    buttonClose:SetName("CloseButton")

    -- Add the controls to the title bar
    titleBar:AddChild(windowTitle)
    titleBar:AddChild(buttonClose)

    -- Add the title bar to the Window
    window:AddChild(titleBar)    
    
    -- Apply styles
    window:SetStyleAuto()
    windowTitle:SetStyleAuto()
    buttonClose:SetStyle("CloseButton")
    
    -- Lastly, subscribe to buttonClose release (following a 'press') events
    SubscribeToEvent(buttonClose, "Released", "HandleClosePressed")
end

function SubscribeToEvents()
    -- Subscribe handler invoked whenever a mouse click event is dispatched
    SubscribeToEvent("UIMouseClick", "HandleControlClicked")
    -- Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent("Update", "HandleUpdate")
end

function HandleClosePressed(eventType, eventData)
    engine:Exit()
end

function HandleControlClicked(eventType, eventData)
    local clicked = eventData["Element"]:GetPtr("UIElement")    
    if clicked ~= nil and clicked.name == "Button" then
        SwitchScene(1 - sceneIndex_)
    end
end

function SwitchScene(index)
    if sceneIndex_ == index then
        return
    end

    -- Delete current scene
    if scene_ ~= nil then
        scene_:delete()
    end

    -- Reset camera parameter
    cameraNode = nil
    yaw = 0.0
    pitch = 0.0
    
    sceneIndex_ = index
    
    if sceneIndex_ == 0 then
        CreateStaticScene()
        windowTitle.text = "Click Button to Switch to Animating Scene"
    else        
        CreateAnimatingScene()
        windowTitle.text = "Click Button to Switch to Static Scene"
    end
    
    if scene_ ~= nil then
        SetupViewport()
    end
end

-- Copy from 04_StaticScene.lua
function CreateStaticScene()
    scene_ = Scene:new()

    -- Create the Octree component to the scene. This is required before adding any drawable components, or else nothing will
    -- show up. The default octree volume will be from (-1000, -1000, -1000) to (1000, 1000, 1000) in world coordinates it
    -- is also legal to place objects outside the volume but their visibility can then not be checked in a hierarchically
    -- optimizing manner
    scene_:CreateComponent("Octree")

    -- Create a child scene node (at world origin) and a StaticModel component into it. Set the StaticModel to show a simple
    -- plane mesh with a "stone" material. Note that naming the scene nodes is optional. Scale the scene node larger
    -- (100 x 100 world units)
    local planeNode = scene_:CreateChild("Plane")
    planeNode.scale = Vector3(100.0, 1.0, 100.0)
    local planeObject = planeNode:CreateComponent("StaticModel")
    planeObject.model = cache:GetResource("Model", "Models/Plane.mdl")
    planeObject.material = cache:GetResource("Material", "Materials/StoneTiled.xml")

    -- Create a directional light to the world so that we can see something. The light scene node's orientation controls the
    -- light direction we will use the SetDirection() function which calculates the orientation from a forward direction vector.
    -- The light will use default settings (white light, no shadows)
    local lightNode = scene_:CreateChild("DirectionalLight")
    lightNode.direction = Vector3(0.6, -1.0, 0.8) -- The direction vector does not need to be normalized
    local light = lightNode:CreateComponent("Light")
    light.lightType = LIGHT_DIRECTIONAL
    light.castShadows = true

    -- Create more StaticModel objects to the scene, randomly positioned, rotated and scaled. For rotation, we construct a
    -- quaternion from Euler angles where the Y angle (rotation about the Y axis) is randomized. The mushroom model contains
    -- LOD levels, so the StaticModel component will automatically select the LOD level according to the view distance (you'll
    -- see the model get simpler as it moves further away). Finally, rendering a large number of the same object with the
    -- same material allows instancing to be used, if the GPU supports it. This reduces the amount of CPU work in rendering the
    -- scene.
    local NUM_OBJECTS = 200
    for i = 1, NUM_OBJECTS do
        local mushroomNode = scene_:CreateChild("Mushroom")
        mushroomNode.position = Vector3(Random(90.0) - 45.0, 0.0, Random(90.0) - 45.0)
        mushroomNode.rotation = Quaternion(0.0, Random(360.0), 0.0)
        mushroomNode:SetScale(0.5 + Random(2.0))
        local mushroomObject = mushroomNode:CreateComponent("StaticModel")
        mushroomObject.model = cache:GetResource("Model", "Models/Mushroom.mdl")
        mushroomObject.material = cache:GetResource("Material", "Materials/Mushroom.xml")
        mushroomObject.castShadows = true
    end

    -- Create a scene node for the camera, which we will move around
    -- The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    cameraNode = scene_:CreateChild("Camera")
    cameraNode:CreateComponent("Camera")

    -- Set an initial position for the camera scene node above the plane
    cameraNode.position = Vector3(0.0, 5.0, 0.0)

	-------------------
	-- ANIMATED SPRITE
	-------------------
	spriteNode = scene_:CreateChild("SpriterAnimation")
	spriteNode.position = Vector3(-1.4, 2, -10)
			local animatedSprite = spriteNode:CreateComponent("AnimatedSprite2D")
			animatedSprite.animationSet = cache:GetResource("AnimationSet2D", "Urho2D/imp/imp.scml") -- Get scml file
			animatedSprite.animation = "idle" -- Play "idle" anim
end

-- Copy from 05_AnimatingScene.lua
function CreateAnimatingScene()
    scene_ = Scene:new()

    -- Create the Octree component to the scene so that drawable objects can be rendered. Use default volume
    -- (-1000, -1000, -1000) to (1000, 1000, 1000)
    scene_:CreateComponent("Octree")

    -- Create a Zone component into a child scene node. The Zone controls ambient lighting and fog settings. Like the Octree,
    -- it also defines its volume with a bounding box, but can be rotated (so it does not need to be aligned to the world X, Y
    -- and Z axes.) Drawable objects "pick up" the zone they belong to and use it when rendering several zones can exist
    local zoneNode = scene_:CreateChild("Zone")
    local zone = zoneNode:CreateComponent("Zone")
    -- Set same volume as the Octree, set a close bluish fog and some ambient light
    zone.boundingBox = BoundingBox(-1000.0, 1000.0)
    zone.ambientColor = Color(0.05, 0.1, 0.15)
    zone.fogColor = Color(0.1, 0.2, 0.3)
    zone.fogStart = 10.0
    zone.fogEnd = 100.0

    -- Create randomly positioned and oriented box StaticModels in the scene
    local NUM_OBJECTS = 2000
    for i = 1, NUM_OBJECTS do
        local boxNode = scene_:CreateChild("Box")
        boxNode.position = Vector3(Random(200.0) - 100.0, Random(200.0) - 100.0, Random(200.0) - 100.0)
        -- Orient using random pitch, yaw and roll Euler angles
        boxNode.rotation = Quaternion(Random(360.0), Random(360.0), Random(360.0))
        local boxObject = boxNode:CreateComponent("StaticModel")
        boxObject.model = cache:GetResource("Model", "Models/Box.mdl")
        boxObject.material = cache:GetResource("Material", "Materials/Stone.xml")
		boxObject.castShadows = true

        -- Add the Rotator script object which will rotate the scene node each frame, when the scene sends its update event.
        -- This requires the C++ component LuaScriptInstance in the scene node, which acts as a container. We need to tell the 
        -- class name to instantiate the object
        local object = boxNode:CreateScriptObject("Rotator")
        object.rotationSpeed = {10.0, 20.0, 30.0}
    end

    -- Create the camera. Let the starting position be at the world origin. As the fog limits maximum visible distance, we can
    -- bring the far clip plane closer for more effective culling of distant objects
    cameraNode = scene_:CreateChild("Camera")
    local camera = cameraNode:CreateComponent("Camera")
    camera.farClip = 100.0

    -- Create a point light to the camera scene node
    light = cameraNode:CreateComponent("Light")
    light.lightType = LIGHT_POINT
    light.range = 30.0
    light.castShadows = true
end

-- Copy from 04_StaticScene.lua
function SetupViewport()
    -- Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    -- at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    -- use, but now we just use full screen and default render path configured in the engine command line options
    local viewport = Viewport:new(scene_, cameraNode:GetComponent("Camera"))
    renderer:SetViewport(0, viewport)
end

-- Copy from 04_StaticScene.lua
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
    yaw = yaw +MOUSE_SENSITIVITY * mouseMove.x
    pitch = pitch + MOUSE_SENSITIVITY * mouseMove.y
    pitch = Clamp(pitch, -90.0, 90.0)

    -- Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
    cameraNode.rotation = Quaternion(pitch, yaw, 0.0)

    -- Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
    -- Use the TranslateRelative() function to move relative to the node's orientation. Alternatively we could
    -- multiply the desired direction with the node's orientation quaternion, and use just Translate()
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
end

-- Copy from 04_StaticScene.lua
function HandleUpdate(eventType, eventData)
    -- Take the frame time step, which is stored as a float
    local timeStep = eventData["TimeStep"]:GetFloat()

    -- Move the camera, scale movement with time step
    if cameraNode then MoveCamera(timeStep) end
end

-- Copy from 05_AnimatingScene.lua
-- Rotator script object class. Script objects to be added to a scene node must implement the empty ScriptObject interface
Rotator = ScriptObject()

function Rotator:Start()
    self.rotationSpeed = {0.0, 0.0, 0.0}
end

function Rotator:Update(timeStep)
    local x = self.rotationSpeed[1] * timeStep
    local y = self.rotationSpeed[2] * timeStep
    local z = self.rotationSpeed[3] * timeStep
    self.node:Rotate(Quaternion(x, y, z))
end
[/code][/spoiler]

-------------------------

