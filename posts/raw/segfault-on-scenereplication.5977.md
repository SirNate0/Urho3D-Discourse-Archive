evolgames | 2020-03-12 01:50:56 UTC | #1

I'm trying to implement Scene Replication into my project, using the Sample by the same name. The sample I've gotten to work (there was a syntax error which was just corrected), but I'm getting a Segmentation Fault when replicating the scene.

```
function HandleClientConnected(eventType, eventData)
   local newConnection = eventData["Connection"]:GetPtr("Connection")
    newConnection.scene = scene_
```

I've narrowed it down a bit to this section of code. Starting a server and all that works fine. When the client connects it immediately segfaults and the client's application is closed. The server host application remains running and just says the client disconnected. If I take out this code it works, but obviously nothing happens.

I suppose this has something to do with my scene? At any rate, how can I figure out what exactly is causing this? Because I've got terrain, rocks, tanks, projectiles, sounds, etc. Is there a verbose output somewhere that will tell me why this is segfaulting? Or does anyone know what might be messing up the scene replication?
The sample is very simple, just a ball. So I *guess* I could slowly move my project into that sample to narrow things down, but that'd be tedious.

As always thanks for the help guys.

-------------------------

SirNate0 | 2020-03-08 17:35:47 UTC | #2

Never really used Lua, so I have no idea if this is actually the problem, but could it not know that newConnection is actually a Connection? Does it think it's just a RefCounted object, for example? Alternatively, is newConnection null?

-------------------------

Miegamicis | 2020-03-08 19:42:36 UTC | #3

Did you subscribe to the correct event? Is the scene_ actually set at that point? Here's the event description https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Network/NetworkEvents.h#L51

Mu guess would be that this handler is subscribed to the wrong event which doesn't have "Connection" parameter.

-------------------------

evolgames | 2020-03-10 05:42:04 UTC | #4

EDIT: it wasn't only this.

So I started slowly adding parts of my project to the Sample to figure out what was the culprit. Turns out it was this:

```
SubscribeToEvent(physicsWorld, "PhysicsCollisionStart", "Impact")
```

Doing this *at all* is what crashes the client. That's all it was. Here's my other events:
```
    SubscribeToEvent("PhysicsPreStep", "HandlePhysicsPreStep")
    SubscribeToEvent("PostUpdate", "HandlePostUpdate")
    SubscribeToEvent(connectButton, "Released", "HandleConnect")
    SubscribeToEvent(disconnectButton, "Released", "HandleDisconnect")
    SubscribeToEvent(startServerButton, "Released", "HandleStartServer")
    SubscribeToEvent("ServerConnected", "HandleConnectionStatus")
    SubscribeToEvent("ServerDisconnected", "HandleConnectionStatus")
    SubscribeToEvent("ConnectFailed", "HandleConnectionStatus")
    SubscribeToEvent("ClientConnected", "HandleClientConnected")
    SubscribeToEvent("ClientDisconnected", "HandleClientDisconnected")
    SubscribeToEvent("ClientObjectID", "HandleClientObjectID")
    network:RegisterRemoteEvent("ClientObjectID");
```
Is this because physicsworld is set as LOCAL? 
 ```
physicsWorld=scene_:CreateComponent("PhysicsWorld", LOCAL)
physicsWorld:SetGravity(Vector3(0,-9.8,0))
```
I need to check for those collisions for the bullets and rocks and stuff. How can I use: 
```
SubscribeToEvent(physicsWorld, "PhysicsCollisionStart", "Impact")
```
without the crash?

-------------------------

SirNate0 | 2020-03-10 05:34:21 UTC | #6

Has `physicsWorld` already been defined by the time you're subscribing to it's event? What is the code inside `Impact`?

-------------------------

evolgames | 2020-03-10 05:41:49 UTC | #7

My problem is evolving lol.
Yeah it's been defined prior. And even with nothing it was segfaulting...turns out it *wasnt* just that.

Ive used the raycast vehicle sample to merge with the scene replication sample. The Ninja Snow sample is nice but I can't make much sense of it from AngelScript. The script object creation of the raycast vehicle is messing everything up. In the scene replication, a simple ball is created when a client connects, and is assigned to them. I can't figure out how to take the vehicle script object and create it in place of the ball...

The tank I made from the raycast demo isn't bad though.
https://www.youtube.com/watch?v=b5Xncimgqm0

-------------------------

SirNate0 | 2020-03-10 07:09:39 UTC | #8

Have you tried running it in a debugger and/or building the engine with the SAFE_LUA flag? That might be quicker than trying to guess the cause.

-------------------------

evolgames | 2020-03-10 17:35:44 UTC | #9

So I rebuilt following the instructions for SAFE_LUA flag. No difference.
When I try to instantiate the vehicle (using the raycast vehicle script object) in place of the ball I get this:

```
[Tue Mar 10 13:32:35 2020] ERROR: RaycastVehicle: Incorrect node id = 117 index: 24
```
and then a segmentation fault. It's totally the script object, which I can't figure out how to convert to just a regular child, since all the movements are not going to go through the script (like Vehicle:FixedUpdate) but instead via the client table (cycling through each client to apply controls).

-------------------------

evolgames | 2020-03-11 11:47:42 UTC | #10

I took a look [here](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Physics/RaycastVehicle.cpp#L228) and it looks like it's here:
```
if (!wheelNode)
{
    URHO3D_LOGERROR("RaycastVehicle: Incorrect node id = " + String(node_id) + " index: " + String(index));
    continue;
}
```
So I'm wondering if this is because the network is duplicating the scene...maybe that's throwing off the node_id increment somehow.

-------------------------

Miegamicis | 2020-03-11 04:51:48 UTC | #11

Now that I think of it I guess the Raycast vehicle is maybe not really ready for replication. Could you try creating that component as a local one?

-------------------------

evolgames | 2020-03-11 05:10:08 UTC | #12

I was afraid that was the case. Well, if I do it as:
```
local raycastVehicle = node:CreateComponent("RaycastVehicle", LOCAL)
```
when creating the vehicle, replacing CreateControllableObject() with CreateVehicle(), the client stops crashing.

However, the client also doesn't have a vehicle now.

-------------------------

Miegamicis | 2020-03-11 05:15:59 UTC | #13

I was doing Raycast vehicle network replication a while ago and my solution was to make the static model nodes for body and wheels replicated, but the component itself as local.

-------------------------

evolgames | 2020-03-11 06:09:26 UTC | #14

Hm okay. The way the sample seems to do it is the host controls all of the clients after taking in their inputs. So would having the raycast vehicle local leave all control up to each client?

EDIT: yeah this really isn't working. If I take the CreateControllableObject ball and create a raycast vehicle, it'll crash just because of that component, local or not. I'd love to see how you set it up. Otherwise I think I might be doomed to recreate a vehicle manually.

-------------------------

Miegamicis | 2020-03-11 07:23:25 UTC | #15

I would say that raycast vehicle's should be only created on the server, clients should only see the replicated scene. Could you show the function that sets up the raycastVehicle? I just checked my other project where I dealt with raycast vehicles and networking and I see that I did just as I said in my previous post, created all the vehicle nodes as replicated, but the raycast components itself - local. One thing to note though is that my implementation was done before the raycast components was introduced in the engine's core, so the implementation my differ.

-------------------------

evolgames | 2020-03-11 23:27:31 UTC | #16

I appreciate all the help. When you say make them as replicated, you just mean make them global, and for the others, appending LOCAL to the end, right?

To make things simpler, I'm sticking as close to the Sample as possible to figure out the vehicle.

```
function HandleClientConnected(eventType, eventData)
PlaySound(fxConnect,1)
    -- When a client connects, assign to scene to begin scene replication
   local newConnection = eventData["Connection"]:GetPtr("Connection")
    newConnection.scene = scene_

    -- Then create a controllable object for that client
    local newObject = CreateControllableObject()
    local newClient = {}
    newClient.connection = newConnection
    newClient.object = newObject
    table.insert(clients, newClient)

    -- Finally send the object's node ID using a remote event
  local remoteEventData = VariantMap()
  remoteEventData["ID"] = newObject.ID
  newConnection:SendRemoteEvent("ClientObjectID", true, remoteEventData)
end


function CreateControllableObject()
    -- Create the scene node & visual representation. This will be a replicated object
    local ballNode = scene_:CreateChild("Ball")
    ballNode.position = Vector3(Random(40.0) - 20.0, 5.0, Random(40.0) - 20.0)
    ballNode:SetScale(0.5)
    local ballObject = ballNode:CreateComponent("StaticModel")
    ballObject.model = cache:GetResource("Model", "Models/Sphere.mdl")
    ballObject.material = cache:GetResource("Material", "Materials/StoneSmall.xml")
	local raycastVehicle=ballNode:CreateComponent("RaycastVehicle", LOCAL)
    -- Create the physics components
    local body = ballNode:CreateComponent("RigidBody")
    body.mass = 1.0
    body.friction = 1.0
    -- In addition to friction, use motion damping so that the ball can not accelerate limitlessly
    body.linearDamping = 0.5
    body.angularDamping = 0.5
    local shape = ballNode:CreateComponent("CollisionShape")
    shape:SetSphere(1.0)

    return ballNode
end
```

So when a client connects, the server creates a controllable object for them. Clients send in controls and the server loops through these objects and applies those controls accordingly. As soon as I add the raycast vehicle component, whether local or not, I get client crashing.

Unless I need to do the raycast vehicle component creation elsewhere? I assume that the server is creating these controllable objects, and so they are all being replicated?


EDIT: As a test, I did the following under the connect function, which should only be used by each client...
```
function HandleConnect(eventType, eventData)
PlaySound(fxConnect,1)
    local address = textEdit.text
    if address == "" then
        address = "localhost" -- Use localhost to connect if nothing else specified
    end

    -- Connect to server, specify scene to use as a client for replication
    clientObjectID = 0 -- Reset own object ID from possible previous connection
    network:Connect(address, SERVER_PORT, scene_)

UpdateButtons()

test = scene_:CreateChild("test")
local raycastVehicle = test:CreateComponent("RaycastVehicle", LOCAL)
    
end
```

Same thing.

-------------------------

Miegamicis | 2020-03-13 00:26:54 UTC | #17

Was able to quickly reproduce this by doing the same thing in C++. The issue that you are seeing is caused by the unitialized `RaycastVehicle` component. You must properly initialize raycast vehicle like this: 

```
local raycastVehicle = node:CreateComponent("RaycastVehicle")
raycastVehicle:Init()
```

Check the https://github.com/urho3d/Urho3D/blob/master/bin/Data/LuaScripts/46_RaycastVehicleDemo.lua#L294-L295 for more details

-------------------------

evolgames | 2020-03-13 00:29:48 UTC | #18

That was it!
I didn't realize it required initialization like that. I was getting that line confused with the following function:
```
function Vehicle:Init()
    -- This function is called only from the main program when initially creating the vehicle, not on scene load
    local node = self.node
    local hullObject = node:CreateComponent("StaticModel")
    self.hullBody = node:CreateComponent("RigidBody")
    local hullShape = node:CreateComponent("CollisionShape")
...
end
```

and so in my consolidation I assumed I didn't need to call it and forgot about it. I was just assuming creating the raycast vehicle component was all that was required. I get it now.

Thanks so much for the help!

-------------------------

