yushli | 2017-01-02 01:05:22 UTC | #1

I changed 33_Urho2DSpriterAnimation.lua a little bit to create 300 2DSpriteAnimation instead of 1. during running the attack animation, black blinks will appear at certain internals,maybe around 5 seconds. This happens in the ubuntu desktop version or android version. The changed code is as follows:

[code]-- Urho2D sprite example.
-- This sample demonstrates:
--     - Creating a 2D scene with spriter animation
--     - Displaying the scene using the Renderer subsystem
--     - Handling keyboard to move and zoom 2D camera

require "LuaScripts/Utilities/Sample"

local spriteNodes = {}
local animationIndex = 0
local animationNames = 
{
    "idle",
    "run",
    "attack",
    "hit",
    "dead",
    "dead2",
    "dead3",
}

function Start()
    -- Execute the common startup for samples
    SampleStart()

    -- Create the scene content
    CreateScene()

    -- Create the UI content
    CreateInstructions()

    -- Setup the viewport for displaying the scene
    SetupViewport()

    -- Hook up to the frame update events
    SubscribeToEvents()
end

function CreateScene()
    scene_ = Scene()

    -- Create the Octree component to the scene. This is required before adding any drawable components, or else nothing will
    -- show up. The default octree volume will be from (-1000, -1000, -1000) to (1000, 1000, 1000) in world coordinates it
    -- is also legal to place objects outside the volume but their visibility can then not be checked in a hierarchically
    -- optimizing manner
    scene_:CreateComponent("Octree")

    -- Create a scene node for the camera, which we will move around
    -- The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    cameraNode = scene_:CreateChild("Camera")
    -- Set an initial position for the camera scene node above the plane
    cameraNode.position = Vector3(0.0, 0.0, -10.0)
    local camera = cameraNode:CreateComponent("Camera")
    camera.orthographic = true
    camera.orthoSize = graphics.height * PIXEL_SIZE
    camera.zoom = 0.3 * Min(graphics.width / 1280, graphics.height / 800) -- Set zoom according to user's resolution to ensure full visibility (initial zoom (1.5) is set for full visibility at 1280x800 resolution)

    local animationSet = cache:GetResource("AnimationSet2D", "Urho2D/imp/imp.scml")
    if animationSet == nil then
        return
    end
    for i=1,300 do
        local    spriteNode = scene_:CreateChild("SpriterAnimation");
        spriteNode.position = Vector3(math.random(30)-30,math.random(30)-30,0);
        local animatedSprite = spriteNode:CreateComponent("AnimatedSprite2D")
        animatedSprite:SetAnimation(animationSet, animationNames[animationIndex + 1])
        spriteNodes[i] = spriteNode
    end
end

function CreateInstructions()
    -- Construct new Text object, set string to display and font to use
    local instructionText = ui.root:CreateChild("Text")
    instructionText:SetText("Mouse click to play next animation, \nUse WASD keys and mouse to move, Use PageUp PageDown to zoom.")
    instructionText:SetFont(cache:GetResource("Font", "Fonts/Anonymous Pro.ttf"), 15)
    instructionText.textAlignment = HA_CENTER -- Center rows in relation to each other

    -- Position the text relative to the screen center
    instructionText.horizontalAlignment = HA_CENTER
    instructionText.verticalAlignment = VA_CENTER
    instructionText:SetPosition(0, ui.root.height / 4)
end

function SetupViewport()
    -- Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    -- at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    -- use, but now we just use full screen and default render path configured in the engine command line options
    local viewport = Viewport:new(scene_, cameraNode:GetComponent("Camera"))
    renderer:SetViewport(0, viewport)
end

function MoveCamera(timeStep)
    -- Do not move if the UI has a focused element (the console)
    if ui.focusElement ~= nil then
        return
    end

    -- Movement speed as world units per second
    local MOVE_SPEED = 4.0

    -- Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
    if input:GetKeyDown(KEY_W) then
        cameraNode:Translate(Vector3(0.0, 1.0, 0.0) * MOVE_SPEED * timeStep)
    end
    if input:GetKeyDown(KEY_S) then
        cameraNode:Translate(Vector3(0.0, -1.0, 0.0) * MOVE_SPEED * timeStep)
    end
    if input:GetKeyDown(KEY_A) then
        cameraNode:Translate(Vector3(-1.0, 0.0, 0.0) * MOVE_SPEED * timeStep)
    end
    if input:GetKeyDown(KEY_D) then
        cameraNode:Translate(Vector3(1.0, 0.0, 0.0) * MOVE_SPEED * timeStep)
    end

    if input:GetKeyDown(KEY_PAGEUP) then
        local camera = cameraNode:GetComponent("Camera")
        camera.zoom = camera.zoom * 1.01
    end

    if input:GetKeyDown(KEY_PAGEDOWN) then
        local camera = cameraNode:GetComponent("Camera")
        camera.zoom = camera.zoom * 0.99
    end
end

function SubscribeToEvents()
    -- Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent("Update", "HandleUpdate")
    SubscribeToEvent("MouseButtonDown", "HandleMouseButtonDown")
SubscribeToEvent("TouchBegin", "HandleMouseButtonDown")
    -- Unsubscribe the SceneUpdate event from base class to prevent camera pitch and yaw in 2D sample
    UnsubscribeFromEvent("SceneUpdate")
end

function HandleUpdate(eventType, eventData)
    -- Take the frame time step, which is stored as a float
    local timeStep = eventData:GetFloat("TimeStep")        
    --for i = 1,300 do
        --spriteNodes[i].position = Vector3(spriteNodes[i].position.x + timeStep,spriteNodes[i].position.y,0);
        -- print(spriteNode.position.x);
        -- Move the camera, scale movement with time step
    --end
    MoveCamera(timeStep)
end

function HandleMouseButtonDown(eventType, eventData)
    animationIndex = (animationIndex + 1) % 7
    for i=1,300 do
        local animatedSprite = spriteNodes[i]:GetComponent("AnimatedSprite2D")        
        animatedSprite:SetAnimation(animationNames[animationIndex + 1], LM_FORCE_LOOPED)
    end
end

-- Create XML patch instructions for screen joystick layout specific to this sample app
function GetScreenJoystickPatchString()
    return
        "<patch>" ..
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/attribute[@name='Is Visible']\" />" ..
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Zoom In</replace>" ..
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button0']]\">" ..
        "        <element type=\"Text\">" ..
        "            <attribute name=\"Name\" value=\"KeyBinding\" />" ..
        "            <attribute name=\"Text\" value=\"PAGEUP\" />" ..
        "        </element>" ..
        "    </add>" ..
        "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/attribute[@name='Is Visible']\" />" ..
        "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Zoom Out</replace>" ..
        "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]\">" ..
        "        <element type=\"Text\">" ..
        "            <attribute name=\"Name\" value=\"KeyBinding\" />" ..
        "            <attribute name=\"Text\" value=\"PAGEDOWN\" />" ..
        "        </element>" ..
        "    </add>" ..
        "</patch>"
end
[/code]

-------------------------

cadaver | 2017-01-02 01:05:22 UTC | #2

Reproduced. May be a case of incorrect animation wrapping (animation time position goes occasionally too far, outside of keyframes, and displays emptiness).

-------------------------

cadaver | 2017-01-02 01:05:22 UTC | #3

It turned out that the animation for "attack" had longer length than the last keyframe. This would cause occasional flashes or sprites disappearing in clamp mode. Now animation length is forced to the last keyframe time.

-------------------------

yushli | 2017-01-02 01:05:23 UTC | #4

Thanks for the quick reply and the fix.  :smiley:

-------------------------

