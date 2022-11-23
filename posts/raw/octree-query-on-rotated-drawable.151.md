Mike | 2017-01-02 00:58:24 UTC | #1

When performing a BoundingBox octree query in lua using GetDrawables, drawable's rotation is not taken into account, which can give inaccurate results depending on the shape of the drawable.

Is there a turnaround for this issue?

Example:

[spoiler][code]
require "LuaScripts/Utilities/Sample"

function Start()
	SampleStart()
	CreateScene()
	SubscribeToEvent("PostRenderUpdate", "HandlePostRenderUpdate")
end

function CreateScene()
	scene_ = Scene()
	scene_:CreateComponent("Octree")
	scene_:CreateComponent("DebugRenderer")

	-- Box1
	box1 = scene_:CreateChild("Box1")
	box1.position = Vector3(0, 0, 3)
	box1.rotation = Quaternion(0, 45, 0)
	local boxObject = box1:CreateComponent("StaticModel")
	boxObject.model = cache:GetResource("Model", "Models/Box.mdl")
	boxObject.material = cache:GetResource("Material", "Materials/StoneEnvMapSmall.xml")

	-- Box2
	box2 = scene_:CreateChild("Box2")
	box2.position = Vector3(0.9, 0, 1.9)
	local boxObject = box2:CreateComponent("StaticModel")
	boxObject.model = cache:GetResource("Model", "Models/Box.mdl")
	boxObject.material = cache:GetResource("Material", "Materials/StoneEnvMapSmall.xml")

	-- Camera
	cameraNode = Node()
	cameraNode.position = Vector3(0, 4, 0)
	cameraNode:LookAt(scene_:GetChild("Box1", true))
	camera = cameraNode:CreateComponent("Camera")
	camera.farClip = 300
	renderer:SetViewport(0, Viewport:new(scene_, camera))

        -- BoundingBox Octree query
	local bbox = box2:GetComponent("StaticModel").worldBoundingBox
	local result = scene_:GetComponent("Octree"):GetDrawables(bbox, DRAWABLE_GEOMETRY)
	for i =1,  table.maxn(result) do print(result[i].node.name) end
end

function HandlePostRenderUpdate(eventType, eventData)
	scene_:GetComponent("DebugRenderer"):AddBoundingBox(box1:GetComponent("StaticModel").worldBoundingBox, Color(1, 1, 1))
end
[/code][/spoiler]

-------------------------

cadaver | 2017-01-02 00:58:24 UTC | #2

All octree queries except ray tests are against the drawables' world axis aligned bounding boxes, which will only grow (leading to possible false positives) when they rotate.

You can do your own filtering of the results afterward, however note the BoundingBox class doesn't support oriented bounding box tests. But you could manually construct a tight bounding sphere for the object you're interested in (there's no automatic function for that, it depends on the object whether that will even lead to good results) and test if the sphere is inside the query area.

-------------------------

Mike | 2017-01-02 00:58:24 UTC | #3

Thanks for detailed explanations, now it makes sense why ray tests are so accurate compared to octree ones.
Will continue to use custom spheres, and physics if needs be.

-------------------------

