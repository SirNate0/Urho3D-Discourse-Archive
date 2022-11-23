Mike | 2017-01-02 00:59:22 UTC | #1

I have some trouble retrieving a ScriptObject's Vector3 after reloading a saved scene.
Here is a simplified version of what I'm doing in lua:
[spoiler][code]
require "LuaScripts/Utilities/Sample"

function Start()
	SampleStart()
	scene_ = Scene()
	SubscribeToEvent("Update", "HandleUpdate")
	local node = scene_:CreateChild("MyNode")
	node:CreateScriptObject("MyObject")
end

MyObject = ScriptObject()

function MyObject:Start()
	self.destination = Vector3(10, 0, 10)
end

function MyObject:Load(deserializer)
	self.destination = deserializer:ReadVector3()
	print(self.destination:ToString()) -- Retrieval is OK
end

function MyObject:Save(serializer)
	serializer:WriteVector3(self.destination)
end

function MyObject:Update(timeStep)
	print(self.destination:ToString())
end

function HandleUpdate(eventType, eventData)
	if input:GetKeyPress(KEY_F5) then scene_:SaveXML(fileSystem:GetProgramDir().."Data/Scenes/TempExport.xml") end
	if input:GetKeyPress(KEY_F7) then scene_:LoadXML(fileSystem:GetProgramDir().."Data/Scenes/TempExport.xml") end
end
[/code][/spoiler]
After reloading the scene, deserialization is OK but self.destination is immediately overwritten to an almost Vector3.ZERO

-------------------------

aster2013 | 2017-01-02 00:59:22 UTC | #2

You do not need write load and save functions for it. Self.desternation will be saved as attribute automatic.

You can check your saved xml file.

-------------------------

Mike | 2017-01-02 00:59:22 UTC | #3

Thanks Aster.
Unfortunately issue is still the same with or without load and save.

By the way, how can you determine when a variable needs load and save?
It's cool to have it loaded/saved automatically.

-------------------------

aster2013 | 2017-01-02 00:59:22 UTC | #4

Hi, mike, 

It is a bug in setting user type attribute, I have fixed it. You can check it. Thanks.

You don't need write your load and save function for attribute in Lua script object. But I prefer you write a setting for it. like:
[code]
function MyObject:SetDestination(value)
   self.destination = Vector3(value)
end
[/code]
The setter function name must with "[b]Set + VarianceName[/b]" (first character need in upper).

-------------------------

Mike | 2017-01-02 00:59:23 UTC | #5

Many thanks for helpful fix and tips  :stuck_out_tongue: 

Maybe we should remove unnecessary load/save variables in sample 18 (onGround, okToJump and inAirTimer) as they are misleading.

-------------------------

aster2013 | 2017-01-02 00:59:23 UTC | #6

Don't remove these functions, but you can remove the attribute load code, just keep controls.yaw and pitch.

[code]
function Character:Load(deserializer)
    self.controls.yaw = deserializer:ReadFloat()
    self.controls.pitch = deserializer:ReadFloat()
end

function Character:Save(serializer)
    serializer:WriteFloat(self.controls.yaw)
    serializer:WriteFloat(self.controls.pitch)
end

[/code]

-------------------------

