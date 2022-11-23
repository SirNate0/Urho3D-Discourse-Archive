evolgames | 2020-03-03 02:11:41 UTC | #1

Okay, here's a fun one.
I'm making this tank game. I have a simple model. The barrel of the tank is a separate model that is childed to the tank "character," and rotates yaw and pitch with the mouse.

On a mouse click I have it instantiate a ball and ApplyForce to shoot it across the map. I'm having trouble instantiating the ball at the end of the barrel.

Here are the relevant sections:
```
--makes the tank. I've taken out the wheels and other parts. Below is the hull and the turret top with the barrel
function CreateCharacter()
    characterNode = scene_:CreateChild("Player")
    characterNode.position = Vector3(0.0,0.0, 0.0)
    main= characterNode:CreateChild("Player")
    main.position = Vector3(0.0, 0.0, 0.0)
    local object = main:CreateComponent("StaticModel")
    object.model = cache:GetResource("Model", "Models/hull.mdl")

    local body = characterNode:CreateComponent("RigidBody")
    body.collisionLayer = 1
    body.mass = 100.0
    body.angularFactor = Vector3(0.0, 1.0, 0.0)
    body.collisionEventMode = COLLISION_ALWAYS
    body:SetAngularDamping(.9)
    body:SetLinearDamping(.9)
    local shape = characterNode:CreateComponent("CollisionShape")
    shape:SetBox(Vector3(3.6,1.8,7.5))

    barrel= characterNode:CreateChild("Player")
    barrel.position = Vector3(0.0, 0, 0.0)
    local barrel = tube:CreateComponent("StaticModel")
    barrel.model = cache:GetResource("Model", "Models/top.mdl")

...

end

--this just creates a bullet
function Shoot()
    local pos=characterNode:GetPosition()
    local objectNode = scene_:CreateChild("Box")
objectNode.position=Vector3(characterNode.position.x,characterNode.position.y+1.8,characterNode.position.z) + objectNode.rotation* Quaternion(character.controls.yaw, Vector3(0.0, 1.0, 0.0))* Quaternion(character.controls.pitch, Vector3(0.0, 0.0, 1.0)) * Quaternion(0,90,-character.controls.pitch)
        local yaw = Quaternion(character.controls.yaw+90, Vector3(0.0, 1.0, 0.0))
        local pitch=Quaternion(character.controls.pitch, Vector3(0.0, 0.0, 1.0))
        local dir = yaw * pitch
	    objectNode.rotation=dir
        objectNode:SetScale(Vector3(.5,.5,.5))
        local object = objectNode:CreateComponent("StaticModel")
        object.model = ball

        local body = objectNode:CreateComponent("RigidBody")
        body.mass = 2
        body.collisionEventMode = COLLISION_ALWAYS
        local shape = objectNode:CreateComponent("CollisionShape")
        shape:SetBox(Vector3(1.0, 1.0, 1.0))
        body:ApplyImpulse(objectNode.rotation*Vector3(0,0,1)*500)
end
```

![Screenshot|690x369](upload://epkBJm0qqDzgd4dIGhwStITcYLn.jpeg)

-------------------------

George1 | 2020-03-03 02:04:26 UTC | #2

Forward direction is z for all object.
Set your object global rotation to the tank rotation before impulse.  There is the same thread by GodMan a few days back.

-------------------------

evolgames | 2020-03-03 02:09:49 UTC | #3

Ok cool, so pitch and yaw are good now.
Any idea on how to get the position of the end of the rotated barrel for instantiating the bullet?

-------------------------

GodMan | 2020-03-03 03:22:05 UTC | #4

To get the barrels position assuming it model origins are 0,0,0. You could get the nodes worldPosition then offset it like this worldPosition + Vector3(0,0,2.0f); you will have to play with offset some to get it right. Then use that position to spawn you missle

-------------------------

evolgames | 2020-03-03 03:38:27 UTC | #5

I just went over your other thread. I didn't mean to re-ask the same thing, but yours didn't show up as a "similar thread," while writing this one.
Anyways, that's what I was trying, but I guess it's because the model needs to rotate in the center, making the barrel do a wide arc. And the bullet needs to come from the barrel...
For the time being I just made a dummy uncollidable body attached to the end of the barrel and I take its position haha. It's a little dumb but it works.

-------------------------

GodMan | 2020-03-03 03:50:46 UTC | #6

I was also going to suggest that in a 3d editor you could add a dummy or bone at the end of the barrel. Then give urho3d that bone or dummy as a node. Then get it's position like any other node. I have done that for many things.

-------------------------

evolgames | 2020-03-03 03:53:08 UTC | #7

Seems simple enough! I should really use the editor more lol. I'll mark that as the solution, although I did it via code.
It's funny that I was racking my head over Quaternions when something stupidly simple works immediately.

-------------------------

GodMan | 2020-03-03 04:02:46 UTC | #8

I add mine to model in 3ds max that I know will need it. Like a character that needs to spawn something.

-------------------------

