evolgames | 2020-02-23 22:44:29 UTC | #1

Hey guys, how can I smoothly LookAt something? I've got a simple enemy that is going from Idling to Walking and facing the player.
I'm scripting with Lua. Obviously, this works:

```
enemyNode:LookAt(targetPosition)
```

but also obviously, that's too immediate.

Years ago (maybe 7) with Unity I recall doing the same thing with either Lerp or Slerp. How can I do a simple LookAt rotation over time in Urho3d?

In Unity it would apparently be something like this below, but there is no RotateTowards for Vector3s in the lua API.
```
targetRotation = Quaternion.LookRotation(object.position - target.postion);
object.rotation = Vector3.RotateTowards(Object.rotation, targetRotation, Time.deltaTime * turnSpeed)
```

I've tried the following:

```
enemyNode.rotation = Quaternion(degree, Vector3(0, 1, 0))
```

but I can't figure out how to find the right degree and then move to it over time. In Urho3d, what's the best way to do this?

-------------------------

Modanung | 2020-02-24 07:58:32 UTC | #2

In Urho you could do something like:
```
Quaternion to{};
if (to.FromLookRotation(targetPosition, up))
    node_->SetWorldRotation(node_->GetWorldRotation().Slerp(to, t));
```

Alternatively, you could lerp the target position:
```
node_->LookAt(node_->LocalToWorld(Vector3::FORWARD).Lerp(targetPosition, t), up);
```
In some cases using an `AttributeAnimation` might make more sense.

-------------------------

evolgames | 2020-02-24 19:36:37 UTC | #3

@Modanung
I appreciate the reply.

So the second one I converted to lua (assuming t here is timestep?) and it produced exactly the same result as LookAt(targetPosition).

For the first one I wasn't able to figure out how to convert this to lua:
```
Quaternion to{};
if (to.FromLookRotation(targetPosition, up))
```

but I tried just this:
```
node_->SetWorldRotation(node_->GetWorldRotation().Slerp(to, t));
```
by writing it as this (changing *to* to the targetposition):
```
enemyNode:SetWorldRotation(enemyNode:GetWorldRotation():Slerp(targetPosition, timestep))
```

What happens now is my enemy rotates halfway to the player, and then slowly moves itself back. It's not really responding correctly to where the player is, and sometimes it won't turn at all, even if I circle it. I'm not sure what's going on here, or why a WorldRotation is changing the position...

Also, whatever is causing the entity to move in position is also making it eventually move through walls.

Should the targetPosition be a WorldPosition?
I know with 2d when you manually set a position or rotation in a physics world, it can cause missed collisions. Is that what's happening here, and shouldn't I then just apply an angular force?

-------------------------

Modanung | 2020-02-24 20:31:05 UTC | #4

`Slerp` stands for _spherical lerp_. The function expects a `Quaternion` (a datatype free of [gimbal lock](https://en.wikipedia.org/wiki/Gimbal_lock)) as its first argument. When it is passed a `Vector3`, I guess a `Quaternion` is constructed from a float array, which is not what you want in this case.

-------------------------

evolgames | 2020-02-24 20:42:58 UTC | #5

Oh alright I see.
So I just need to take the target position as a Quaternion?
I don't know how to get the *to* as a Quaternion, because from the API most of the choices, GetWorldPosition, are given as Vector3s...

-------------------------

SirNate0 | 2020-02-24 21:00:43 UTC | #6

If your Unity code gives you the desired behavior, what you probably want to do is to check the angle between the vector and the target position (node's (world) direction and the rotated direction). If that angle is greater than your angular velocity threshold * the timestep you limit it (I think a Quaternion::Identity.Slerp(targetRotation, maxAngle / measuredAngle) would be the right choice) and if it is <= you just use the targetRotation you got from LookRotation.

Another thing that might work is some tricks with the Cross Product and Quaternion's FromAngleAxis(), but I think the above is most similar to what you have already and probably the easiest to follow.

-------------------------

Modanung | 2020-02-24 21:30:52 UTC | #7

[quote="evolgames, post:3, topic:5943"]
```
Quaternion to{};
if (to.FromLookRotation(targetPosition, up))
```
[/quote]
I have little to no experience in Lua, but I think it should translate to something like this:
```Lua
local to = Quaternion()
if to:FromLookRotation(targetPosition, up) then
    ...
end
```

-------------------------

evolgames | 2020-02-24 21:37:31 UTC | #8

No worries, I only have any skill in Lua, and only do games and stuff for a hobby. I'm getting used to at least reading C++ and AS, even if I don't fully understand them yet.

Hm, interestingly that's exactly what I had tried and it gave me a segmentation fault, I was just assuming I misunderstood it.

-------------------------

SirNate0 | 2020-02-24 23:14:03 UTC | #9

Maybe ensure that targetPosition and up are actually defined? I ran it myself and I got a seg. fault without the definitions at the top, but adding them it worked fine.
```
    -- Failed without these    v
    targetPosition = Vector3(10,1,1)
    up = Vector3(1,0,0)
    -- Failed without these ^
    
    local to = Quaternion()
    if to:FromLookRotation(targetPosition, up) then
        Print(to)
    end
```

-------------------------

evolgames | 2020-02-25 01:09:50 UTC | #10

So the segmentation fault was because I forgot to define the up vector.
You wrote Vector3(1,0,0), which rotates the X axis, so I changed it to Vector3(0,1,0).

My enemy now gradually rotates...to face away from the player.
Also, after he has rotated, he will not rotate at all afterwards, no matter how I circle him. Which is weird because if the targetPosition is constantly changing, shouldn't the rotations do the same?

-------------------------

WangKai | 2020-02-25 02:47:07 UTC | #11

`AttributeAnimation` should be combined with [`Easing`](https://easings.net/) animation, will be super powerful.

-------------------------

evolgames | 2020-02-25 03:57:46 UTC | #12

I don't have enough experience with Urho3d to know how to implement that. But I strictly just need a rotation here, nothing else. The animations are working perfectly and I have no problem with them.

-------------------------

SirNate0 | 2020-02-25 04:31:29 UTC | #13

What does your rotation code look like now? And do you update the variable for the rotation every frame?

-------------------------

evolgames | 2020-02-25 04:51:15 UTC | #14

This is under an update function for enemies, which is getting called each frame. I realize there is probably a simpler way of doing the distance calculation. This section is just a place for me to make sure certain things work.

```
local to = Quaternion()
local up = Vector3(0,1,0)
local player = characterNode:GetWorldPosition()
local orc = orcNode:GetWorldPosition()
local rotSpeed=5

if dist3d(orc.x,orc.y,orc.z,player.x,player.y,player.z)<orcs.sight then

animCtrl:PlayExclusive("Models/Orc/Animations/walk.ani", 1, true, 1)

if to:FromLookRotation(player, up) then
orcNode:SetWorldRotation(orcNode:GetWorldRotation():Slerp(to, rotSpeed*timestep))
end

end
```

-------------------------

Modanung | 2020-02-25 07:47:43 UTC | #15

[quote="evolgames, post:14, topic:5943"]
I realize there is probably a simpler way of doing the distance calculation.
[/quote]
Indeed you should be able to `orc:DistanceToPoint(player) < orcs.sight`.

[quote="evolgames, post:10, topic:5943"]
My enemy now gradually rotates…to face away from the player.
[/quote]

Maybe your *asset* is misoriented?

-------------------------

elix22 | 2020-02-25 19:02:34 UTC | #16

[quote="evolgames, post:14, topic:5943"]
if to:FromLookRotation(player, up) then
[/quote]
Above  line looks wrong to me , try this:

>  to:FromLookRotation(player-orc, up)

-------------------------

SirNate0 | 2020-02-25 15:32:30 UTC | #17

I believe this code might work? (Though I don't use Lua, and haven't tested it, so no gaurantees)
```
local to = Quaternion()
local up = Vector3(0,1,0)
local player = characterNode:GetWorldPosition()
local orc = orcNode:GetWorldPosition()
local rotSpeed=5

if dist3d(orc.x,orc.y,orc.z,player.x,player.y,player.z)<orcs.sight then

animCtrl:PlayExclusive("Models/Orc/Animations/walk.ani", 1, true, 1)

-- degrees per second
maxRotationSpeed = 100

if to:FromLookRotation(player-orc, up) then
    -- Get the change in rotation
    deltaRotation = to * orcNode:GetWorldRotation()
    -- If this is more than allowed, limit it to the maximum velocity change
    -- If you only care about the angle around the y axis (if it can tilt the Orc 
    --     as well) you can probably just use deltaRotation:YawAngle()
    if deltaRotation:Angle() > maxRotationSpeed * timestep then
        deltaRotation = Quaternion():Slerp(deltaRotation, maxRotationSpeed * timestep)
    end
    -- Update the rotation accordingly
    orcNode:SetWorldRotation(deltaRotation * orcNode:GetWorldRotation())
end

end
```

-------------------------

evolgames | 2020-02-25 18:59:16 UTC | #19

@elix22
That was it! The rotation is perfect, and I'm able to adjust the speed easily as well.

For posterity, here is what I have now:

```
local orc=orcNode:GetWorldPosition()
local player=characterNode:GetWorldPosition()
local to = Quaternion()
local up = Vector3(0,1,0)
local rotSpeed = 3

if orc:DistanceToPoint(player)<orcs.sight then
animCtrl:PlayExclusive("Models/Orc/Animations/walk.ani", 1, true, 1)

if to:FromLookRotation(player - orc, up) then
orcNode:SetWorldRotation(orcNode:GetWorldRotation():Slerp(to, rotSpeed*timestep))
end

end
```

I'll likely use the same thing to rotate the enemy's head a bit faster, so as to make him *look* at the player while he turns. The awesome thing is I'll be able to use this for practically every npc rotation.

@SirNate0, thank you either way! I tried that and it *did* rotate, but it was a bit glitchy for some reason. @Modanung and everyone else I really appreciate the help with this. Which post should I mark as the solution since it was a combination of a couple?

-------------------------

Modanung | 2020-02-25 19:08:02 UTC | #20

@elix22 was lowest on solutions. :wink:

-------------------------

