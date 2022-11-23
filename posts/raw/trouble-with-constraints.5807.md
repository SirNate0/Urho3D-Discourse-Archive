evolgames | 2020-01-08 11:25:27 UTC | #1

Hello, I'm a new Urho3d user. I'm developing with lua bindings, and so far so good.

However, I'm having trouble with constraints. What I'm trying to make is a "creature," made up of various rigid bodies. It's randomly generated, and I'm using impulses to make it move. The problem I have is that it is floppy no matter what I do. Hinge joints with strictly low limits don't seem to limit at all. Also, point constraints seem to have the same affect.

I tried messing with the axis, lower and upper limits, and switching between Hinge and Point constraints. I'm assuming Point constraint means "weld joint"? Or, is there a weld joint/constraint somewhere else that I'm missing?

I'd love to be able to weld bodies together, and also to be able to limit hinges properly, so that I can make natural "knee" and "elbow" movements. Right now, it just tumbles to the floor and everything is freely spinning, rotating, and moving.

Here is a relevant sample code from a "part" of the creature. A for loop creates 5,10 of these and joins them randomly. So they all more or less will have similar controls.

```
guy[i].partNode = scene_:CreateChild()
guy[i].partNode.scale = Vector3(sx,sy,sz)
guy[i].partNode.position=Vector3(posx,posy,posz)
guy[i].posx=posx
guy[i].posy=posy
guy[i].posz=posz
guy[i].sx=sx
guy[i].sy=sy
guy[i].sz=sz
guy[i].dirx=dirx
guy[i].diry=diry
guy[i].dirz=dirz

guy[i].partObject = guy[i].partNode:CreateComponent("StaticModel")
guy[i].partBody = guy[i].partNode:CreateComponent("RigidBody")
guy[i].partShape = guy[i].partNode:CreateComponent("CollisionShape")
guy[i].partConstraint = guy[i].partNode:CreateComponent("Constraint")
guy[i].partObject.model = cache:GetResource("Model", "Models/Box.mdl")
guy[i].color=RandomInt(1,4)
guy[i].partObject.material = mat[guy[i].color]

guy[i].partObject.castShadows = true
guy[i].partShape:SetBox(Vector3(sx,sy,sz))
guy[i].partBody.friction = 1
guy[i].partBody.mass = (sx*sy*sz)/set.massFac
guy[i].partBody.linearDamping = 0.2
guy[i].partBody.angularDamping = 0.2
guy[i].partBody.collisionLayer = 1
guy[i].partBody:SetCcdMotionThreshold(1)
guy[i].partBody:SetCcdRadius(1)
guy[i].partBody.collisionEventMode = COLLISION_ALWAYS

guy[i].whichjoint=RandomInt(0,1)
if guy[i].whichjoint==1 then
guy[i].partConstraint.constraintType = CONSTRAINT_HINGE
else
guy[i].partConstraint.constraintType = CONSTRAINT_POINT
end

guy[i].partConstraint.otherBody = guy[connect].partNode:GetComponent("RigidBody")
guy[i].partConstraint.worldPosition = Vector3(jposx,jposy,jposz)

guy[i].axis1=Random(1.0)
guy[i].axis2=Random(1.0)
guy[i].axis3=Random(1.0)
while math.abs(guy[i].axis1+guy[i].axis2+guy[i].axis3)>1 do
guy[i].axis1=Random(1.0)
guy[i].axis2=Random(1.0)
guy[i].axis3=Random(1.0)
end
guy[i].lowlim1=Random(180.0)*-1
guy[i].lowlim2=Random(180.0)*-1
guy[i].uplim1=Random(180.0)
guy[i].uplim2=Random(180.0)
guy[i].partConstraint.axis = Vector3(guy[i].axis1, guy[i].axis2, guy[i].axis3)
guy[i].partConstraint.lowLimit = Vector2(guy[i].lowlim1, guy[i].lowlim2)
guy[i].partConstraint.highLimit = Vector2(guy[i].uplim1,guy[i].uplim2)
guy[i].partConstraint.disableCollision = false
```
**Please excuse gutter-formatting*

Yes, the parameters of the constraint are randomly applied here, but it doesn't matter if I set all the axis to 1 or 0, or the lower/upper limits to 0 or 180. It's all the same floppy mess in the end. That said, they *are* connected, and I have no problem creating the constraint, they just are weak and not restricted in movement. They stretch and pull apart easily.

Any help with this would be greatly appreciated, as I'm scratching my head on this one. I'm sure I must be missing something.

Thanks!

-------------------------

Sinoid | 2020-01-08 01:48:14 UTC | #2

Point constraint isn't a weld, welds in Bullet have to be done with the 6-dof constraint that Urho doesn't use anywhere (you'd have to add it).

Compound shapes are automatically constructed with all `CollisionShapes` on a node. You can fake a permanent weld joint that way. Although it looks tricky you could probably modify `CollisionShape` to search up the tree to find an **enabled** `RigidBody` so that welding+unwelding would be a matter of parenting and toggling a RigidBody's enabled state - it looks tricky though.

-------------------------

Modanung | 2020-01-08 01:43:07 UTC | #3

https://discourse.urho3d.io/t/6dof-bullet-samples/5675

@evolgames Welcome to the forums! :confetti_ball: :slight_smile:

-------------------------

evolgames | 2020-01-08 01:48:50 UTC | #4

Thank you, I will check it out!

-------------------------

evolgames | 2020-01-08 01:50:52 UTC | #5

Okay, I was afraid of that. I'm marking this as the solution, then. I'll see if I can hack something together.
I'm assuming I can't just create a 3d model with code, and feed the coordinates to Urho for the two shapes I want to weld, effectively achieving the same thing?

-------------------------

