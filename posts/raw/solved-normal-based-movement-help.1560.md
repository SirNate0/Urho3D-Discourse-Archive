practicing01 | 2017-01-02 01:08:30 UTC | #1

Edit #0: Simplified the code, spider is still crabwalking..
[img]http://i.imgur.com/PjBz6OX.gif?1[/img]
[code]
FoinSpider = ScriptObject()

function FoinSpider:Start()
  self.MOVE_FORCE = 0.5
  self.BRAKE_FORCE = 0.025
  self.rotDummy_ = nil
  self.rayDistance_ = 30.0
  self.gravityForce_ = Vector3(-9.81, -9.81, -9.81)
  self.slerpDest_ = Quaternion()
  self.slerpInterval_ = 0.1
  self.slerpProgress_ = 0.0

  self.STATE_STAND = 0
  self.STATE_IDLE = 1
  self.STATE_FOLLOW = 2
  self.STATE_SPIT = 3
  self.currentState_ = 0

  self.targetNode_ = nil
  self.body_ = nil
  self.animController_ = nil
end

function FoinSpider:DelayedStart()
  self.rotDummy_ = self.node:GetChild("rotDummy")
  self.body_ = self.node:GetComponent("RigidBody")
  self.animController_ = self.node:GetComponent("AnimationController")

  self:SetState(self.STATE_STAND)

  self:SubscribeToEvent(self.node:GetChild("playerTrigger"), "NodeCollisionStart", "FoinSpider:HandleNodeCollisionStart")
  self:SubscribeToEvent(self.node:GetChild("playerTrigger"), "NodeCollisionEnd", "FoinSpider:HandleNodeCollisionStart")
  --self:SubscribeToEvent("PostRenderUpdate", "FoinSpider:HandlePostRenderUpdate")
end

function FoinSpider:Stop()
  --
end

function FoinSpider:FixedUpdate(timeStep)
  self:FollowPath(timeStep)

  if self.rotDummy_ == nil then return end

  local nodePos = self.node:GetWorldPosition()
  local aimPoint = self.rotDummy_:GetWorldPosition()
  local rayDir = (aimPoint - nodePos):Normalized()
  rayDir = rayDir * Vector3(-1.0, -1.0, -1.0)

  local result = LevelScene_:GetComponent("PhysicsWorld"):RaycastSingle(Ray(aimPoint, rayDir), self.rayDistance_, 2)

  if result.body ~= nil then
    local invertedNormal = result.normal * self.gravityForce_
    self.body_:SetGravityOverride(invertedNormal)
    local quat = Quaternion()
    quat:FromLookRotation(self.node:GetDirection(), result.normal)
    
    self.node:SetRotation(quat)

    --[[if quat ~= self.slerpDest_ then
      self.slerpDest_ = quat
      self.slerpProgress_ = 0.0
    end

    local rot = self.body_:GetRotation()

    if self.slerpProgress_ < 1.0 then
      rot = rot:Slerp(self.slerpDest_, self.slerpProgress_)
      self.node:SetRotation(rot)

      self.slerpProgress_ = self.slerpProgress_ + (self.slerpInterval_ * timeStep)
      --self.slerpProgress_ = self.slerpProgress_ + (self.slerpInterval_)
      self.slerpProgress_ = Clamp(self.slerpProgress_, 0.0, 1.0)
    elseif rot ~= self.slerpDest_ then
      self.node:SetRotation(self.slerpDest_)
    end--]]

end

end

function FoinSpider:HandleNodeCollision(eventType, eventData)
  --
end

function FoinSpider:HandleNodeCollisionStart(eventType, eventData)
  local trigger = eventData["Trigger"]:GetBool()
  local otherNode = eventData["OtherNode"]:GetPtr("Node")

  if trigger == true then
    self.targetNode_ = otherNode
    self:SetState(self.STATE_FOLLOW)
  end

end

function FoinSpider:SetState(state)
  self.currentState_ = state

  if state == self.STATE_STAND then
    self:StateStand()
  elseif state == self.STATE_FOLLOW then
    self:StateFollow()
  end

end

function FoinSpider:StateStand()
  local STAND_ANI = "Models/foinSpider/stand.ani"

  self.body_:SetLinearVelocity(Vector3.ZERO)
  self.body_:SetFriction(10.0)

  if self.animController_ ~= nil then
    self.animController_:PlayExclusive(STAND_ANI, 0, true, 0.0)
end
end

function FoinSpider:StateFollow()
  local WALK_ANI = "Models/foinSpider/walk.ani"

  self.body_:SetFriction(0.0)

  if self.animController_ ~= nil then
    self.animController_:PlayExclusive(WALK_ANI, 0, true, 0.0)
end
end

function FoinSpider:FollowPath(timeStep)
  if self.currentState_ == self.STATE_STAND then
    return
  end
  
  --local nodePos = self.node:GetWorldPosition()
  local nodePos = self.rotDummy_:GetWorldPosition()
  local targetPos = self.targetNode_:GetWorldPosition()

  if (targetPos - nodePos):Length() > 25.0 then
    --self.node:LookAt(targetPos, Vector3.UP, TS_WORLD)
    self.node:LookAt(targetPos)
  else
    self:SetState(self.STATE_STAND)
    return
  end
  
  local velocity = self.body_.linearVelocity
  --local speed = velocity:Length()

  --local speedRatio = speed / self.MOVE_FORCE

  self.body_:ApplyImpulse((targetPos - nodePos):Normalized() * self.MOVE_FORCE)

  local brakeForce = velocity * -self.BRAKE_FORCE
  self.body_:ApplyImpulse(brakeForce)
  
  local WALK_ANI = "Models/foinSpider/walk.ani"
  self.animController_:SetSpeed(WALK_ANI, (self.body_:GetLinearVelocity():Length() * 0.05))
end

function FoinSpider:HandlePostRenderUpdate(eventType, eventData)
  local debug = LevelScene_:GetComponent("DebugRenderer")
  --LevelScene_:GetComponent("PhysicsWorld"):DrawDebugGeometry(true)
  --LevelScene_:GetComponent("Octree"):DrawDebugGeometry(true)
  renderer:DrawDebugGeometry(true)

  local nodePos = self.node:GetWorldPosition()
  local aimPoint = self.rotDummy_:GetWorldPosition()
  local rayDir = (aimPoint - nodePos):Normalized()
  rayDir = rayDir * Vector3(-1.0, -1.0, -1.0)

  --debug:AddLine(aimPoint, aimPoint + (rayDir * self.rayDistance_), Color(1.0, 1.0, 1.0), false)
  debug:AddCross(aimPoint, 2.0 , Color(1.0, 1.0, 1.0), false)
  debug:AddCross(aimPoint + (rayDir * self.rayDistance_), 2.0, Color(1.0, 1.0, 1.0), false)
  
  debug:AddLine(nodePos, nodePos + (self.node:GetDirection() * self.rayDistance_), Color(1.0, 1.0, 1.0), false)
  debug:AddLine(aimPoint, aimPoint + (self.node:GetDirection() * self.rayDistance_), Color(1.0, 1.0, 1.0), false)
end

[/code]

Edit: I've ditched pathfinding because i couldn't get it to work.  I think I've gotten the ground normal + target direction rotations combining but the target direction is sideways.  Any ideas as to why that is?

new code:
[code]
FoinSpider = ScriptObject()

function FoinSpider:Start()
  self.MOVE_FORCE = 0.5
  self.BRAKE_FORCE = 0.025
  self.rotDummy_ = nil
  self.rayDistance_ = 50.0
  --self.gravityForce_ = Vector3(-9.81, -9.81, -9.81)
  self.gravityForce_ = Vector3(-9.81, -9.81, -9.81)
  self.slerpDest_ = Quaternion()
  self.slerpInterval_ = 0.1
  self.slerpProgress_ = 0.0

  self.STATE_STAND = 0
  self.STATE_IDLE = 1
  self.STATE_FOLLOW = 2
  self.STATE_SPIT = 3
  self.currentState_ = 0

  self.targetNode_ = nil
end

function FoinSpider:DelayedStart()
  self.rotDummy_ = self.node:GetChild("rotDummy")

  self:SetState(self.STATE_STAND)

  --self:SubscribeToEvent("Update", "FoinSpider:HandleUpdate")
  --self:SubscribeToEvent(self.node, "NodeCollision", "FoinSpider:HandleNodeCollision")
  self:SubscribeToEvent(self.node:GetChild("playerTrigger"), "NodeCollisionStart", "FoinSpider:HandleNodeCollisionStart")
  self:SubscribeToEvent(self.node:GetChild("playerTrigger"), "NodeCollisionEnd", "FoinSpider:HandleNodeCollisionStart")
  self:SubscribeToEvent("PostRenderUpdate", "FoinSpider:HandlePostRenderUpdate")
end

function FoinSpider:Stop()
  --
end

function FoinSpider:HandleUpdate(eventType, eventData)
  local timeStep = eventData["TimeStep"]:GetFloat()
end

function FoinSpider:FixedUpdate(timeStep)
  self:FollowPath(timeStep)

  if self.rotDummy_ == nil then return end

  local body  = self.node:GetComponent("RigidBody")

  local nodePos = self.node:GetWorldPosition()
  local aimPoint = self.rotDummy_:GetWorldPosition()
  local rayDir = (aimPoint - nodePos):Normalized()
  rayDir = rayDir * Vector3(-1.0, -1.0, -1.0)

  local result = LevelScene_:GetComponent("PhysicsWorld"):RaycastSingle(Ray(aimPoint, rayDir), self.rayDistance_, 2)

  if result.body ~= nil then
    local invertedNormal = result.normal * self.gravityForce_
    body:SetGravityOverride(invertedNormal)
    local quat = Quaternion()
    quat:FromLookRotation(self.node:GetDirection(), result.normal)
    
    body:SetRotation(quat)
--[[
    if quat ~= self.slerpDest_ then
      self.slerpDest_ = quat
      self.slerpProgress_ = 0.0
    end

    local rot = body:GetRotation()

    if self.slerpProgress_ < 1.0 then
      rot = rot:Slerp(self.slerpDest_, self.slerpProgress_)
      body:SetRotation(rot)

      --self.slerpProgress_ = self.slerpProgress_ + (self.slerpInterval_ * timeStep)
      self.slerpProgress_ = self.slerpProgress_ + (self.slerpInterval_)
      self.slerpProgress_ = Clamp(self.slerpProgress_, 0.0, 1.0)
    elseif rot ~= self.slerpDest_ then
      body:SetRotation(self.slerpDest_)
    end--]]

end

end

function FoinSpider:HandleNodeCollision(eventType, eventData)
  --
end

function FoinSpider:HandleNodeCollisionStart(eventType, eventData)
  local trigger = eventData["Trigger"]:GetBool()
  local otherNode = eventData["OtherNode"]:GetPtr("Node")

  if trigger == true then
    self.targetNode_ = otherNode
    self:SetState(self.STATE_FOLLOW)
  end

end

function FoinSpider:SetState(state)
  self.currentState_ = state

  if state == self.STATE_STAND then
    self:StateStand()
  elseif state == self.STATE_FOLLOW then
    self:StateFollow()
  end

end

function FoinSpider:StateStand()
  local STAND_ANI = "Models/foinSpider/stand.ani"
  local animCtrl = self.node:GetComponent("AnimationController")

  local body = self.node:GetComponent("RigidBody")
  body:SetLinearVelocity(Vector3.ZERO)
  body:SetFriction(10.0)

  if animCtrl ~= nil then
    animCtrl:PlayExclusive(STAND_ANI, 0, true, 0.0)
end
end

function FoinSpider:StateFollow()
  local WALK_ANI = "Models/foinSpider/walk.ani"
  local animCtrl = self.node:GetComponent("AnimationController")
  local body = self.node:GetComponent("RigidBody")

  body:SetFriction(0.0)

  if animCtrl ~= nil then
    animCtrl:PlayExclusive(WALK_ANI, 0, true, 0.0)
end
end

function FoinSpider:FollowPath(timeStep)
  if self.currentState_ == self.STATE_STAND then
    return
  end
  
  local body  = self.node:GetComponent("RigidBody")

  local nodePos = self.node:GetWorldPosition()
  local targetPos = self.targetNode_:GetWorldPosition()

  if (targetPos - nodePos):Length() > 25.0 then
    self.node:LookAt(targetPos, Vector3.UP, TS_WORLD)
  else
    self:SetState(self.STATE_STAND)
    return
  end
  
  local velocity = body.linearVelocity
  --local speed = velocity:Length()

  --local speedRatio = speed / self.MOVE_FORCE

  body:ApplyImpulse((targetPos - nodePos):Normalized() * self.MOVE_FORCE)

  local brakeForce = velocity * -self.BRAKE_FORCE
  body:ApplyImpulse(brakeForce)
  
  local WALK_ANI = "Models/foinSpider/walk.ani"
  local animCtrl = self.node:GetComponent("AnimationController")
  animCtrl:SetSpeed(WALK_ANI, (body:GetLinearVelocity():Length() * 0.05))
end

function FoinSpider:HandlePostRenderUpdate(eventType, eventData)
  local debug = LevelScene_:GetComponent("DebugRenderer")
  LevelScene_:GetComponent("PhysicsWorld"):DrawDebugGeometry(true)
  --LevelScene_:GetComponent("Octree"):DrawDebugGeometry(true)
  renderer:DrawDebugGeometry(true)

  local nodePos = self.node:GetWorldPosition()
  local aimPoint = self.rotDummy_:GetWorldPosition()
  local rayDir = (aimPoint - nodePos):Normalized()
  rayDir = rayDir * Vector3(-1.0, -1.0, -1.0)

  debug:AddLine(aimPoint, aimPoint + (rayDir * self.rayDistance_), Color(1.0, 1.0, 1.0), false)
  debug:AddCross(aimPoint, 2.0 , Color(1.0, 1.0, 1.0), false)
  debug:AddCross(aimPoint + (rayDir * self.rayDistance_), 2.0, Color(1.0, 1.0, 1.0), false)
end

[/code]

Pic of spider moving towards player.  Notice how its side is facing the player (that's the problem).
[img]http://img.ctrlv.in/img/15/12/11/566a892232d00.png[/img]

Hello, I'm making a spider and through some online snippets have managed to get it moving along surface normals.  I'm really bad at math though and need help rotating three things.  The first is the spider along the normal.  There's some code for that and it seems to be working but I'd like to make sure it's correct (found in FixedUpdate).  Second is the spider towards the current waypoint (combining the current surface normal rotation with the destination waypoint).  Third is the direction of the impulse applied to the spider so that it moves towards the next waypoint (previous two rotations should be applied in FollowPath).  Any help would be greatly appreciated!

[code]
FoinSpider = ScriptObject()

function FoinSpider:Start()
  self.MOVE_FORCE = 2.0
  self.BRAKE_FORCE = 0.025
  self.rotDummy_ = nil
  self.rayDistance_ = 25.0
  self.gravityForce_ = Vector3(-9.81, -9.81, -9.81)
  self.slerpDest_ = Quaternion()
  self.slerpInterval_ = 0.1
  self.slerpProgress_ = 0.0
  
  self.STATE_STAND = 0
  self.STATE_IDLE = 1
  self.STATE_FOLLOW = 2
  self.STATE_SPIT = 3
  self.currentState_ = 0
  
  self.targetNode_ = nil
  self.pathEndPos_ = nil
  self.currentPath_ = nil
  self.nearestExtents_ = 30.0
end

function FoinSpider:DelayedStart()
  local body  = self.node:GetComponent("RigidBody")
  body.collisionEventMode = COLLISION_ALWAYS
  
  body:SetFriction(0.0)
  
  self.rotDummy_ = self.node:GetChild("rotDummy")
  
  self:SetState(self.STATE_STAND)
  
  --self:SubscribeToEvent("Update", "FoinSpider:HandleUpdate")
  --self:SubscribeToEvent(self.node, "NodeCollision", "FoinSpider:HandleNodeCollision")
  self:SubscribeToEvent(self.node:GetChild("playerTrigger"), "NodeCollisionStart", "FoinSpider:HandleNodeCollisionStart")
  self:SubscribeToEvent(self.node:GetChild("playerTrigger"), "NodeCollisionEnd", "FoinSpider:HandleNodeCollisionStart")
  self:SubscribeToEvent("PostRenderUpdate", "FoinSpider:HandlePostRenderUpdate")
end

function FoinSpider:Stop()
  --
end

function FoinSpider:HandleUpdate(eventType, eventData)
  local timeStep = eventData["TimeStep"]:GetFloat()
end

function FoinSpider:FixedUpdate(timeStep)
  if self.rotDummy_ == nil then return end
  
  local body  = self.node:GetComponent("RigidBody")
  
  local nodePos = self.node:GetWorldPosition()
  local aimPoint = self.rotDummy_:GetWorldPosition()
  local rayDir = (aimPoint - nodePos):Normalized()
  rayDir = rayDir * Vector3(-1.0, -1.0, -1.0)
  
  local result = self.node:GetScene():GetComponent("PhysicsWorld"):RaycastSingle(Ray(aimPoint, rayDir), self.rayDistance_, 2)
  
  if result.body ~= nil then
    local invertedNormal = result.normal * self.gravityForce_
    body:SetGravityOverride(invertedNormal)
    local quat = Quaternion()
    quat:FromLookRotation(self.node:GetDirection(), result.normal)
    
    if quat ~= self.slerpDest_ then
      self.slerpDest_ = quat
      self.slerpProgress_ = 0.0
    end

    local rot = body:GetRotation()

    if self.slerpProgress_ ~= 1.0 then
      rot = rot:Slerp(self.slerpDest_, self.slerpProgress_)
      body:SetRotation(rot)

      self.slerpProgress_ = self.slerpProgress_ + (self.slerpInterval_ * timeStep)
    elseif rot ~= self.slerpDest_ then
      body:SetRotation(self.slerpDest_)
    end

  end

  self:FollowPath(timeStep)
end

function FoinSpider:HandleNodeCollision(eventType, eventData)
    --[[local contacts = eventData["Contacts"]:GetBuffer()

    while not contacts.eof do
        local contactPosition = contacts:ReadVector3()
        local contactNormal = contacts:ReadVector3()
        local contactDistance = contacts:ReadFloat()
        local contactImpulse = contacts:ReadFloat()

        -- If contact is below node center and mostly vertical, assume it's a ground contact
        if contactPosition.y < self.node.position.y + 1.0 then
            local level = Abs(contactNormal.y)
            if level > 0.75 then
                --
            end
        end
    end--]]
end

function FoinSpider:HandleNodeCollisionStart(eventType, eventData)
  local trigger = eventData["Trigger"]:GetBool()
  local otherNode = eventData["OtherNode"]:GetPtr("Node")
  
  if trigger == true then
    self.targetNode_ = otherNode
    self:SetState(self.STATE_FOLLOW)
  end
  
end

function FoinSpider:HandlePostRenderUpdate(eventType, eventData)
  local debug = self.node:GetScene():GetComponent("DebugRenderer")
  --self.node:GetScene():GetComponent("PhysicsWorld"):DrawDebugGeometry(true)
  --self.node:GetScene():GetComponent("Octree"):DrawDebugGeometry(true)
  --renderer:DrawDebugGeometry(true)
  
  local nodePos = self.node:GetWorldPosition()
  local aimPoint = self.rotDummy_:GetWorldPosition()
  local rayDir = (aimPoint - nodePos):Normalized()
  rayDir = rayDir * Vector3(-1.0, -1.0, -1.0)
  
  debug:AddLine(aimPoint, aimPoint + (rayDir * self.rayDistance_), Color(1.0, 1.0, 1.0), false)
  debug:AddCross(aimPoint, 2.0 , Color(1.0, 1.0, 1.0), false)
  debug:AddCross(aimPoint + (rayDir * self.rayDistance_), 2.0, Color(1.0, 1.0, 1.0), false)
  
  if self.currentPath_ == nil then
    return
  end
  
  local navMesh = self.node:GetScene():GetComponent("NavigationMesh")
  navMesh:DrawDebugGeometry(true)
  
  -- Visualize the start and end points and the last calculated path
  local size = table.maxn(self.currentPath_)
  if size > 0 then
    debug:AddBoundingBox(BoundingBox(self.pathEndPos_ - Vector3(0.1, 0.1, 0.1), self.pathEndPos_ + Vector3(0.1, 0.1, 0.1)), Color(1.0, 1.0, 1.0))

    -- Draw the path with a small upward bias so that it does not clip into the surfaces
    local bias = Vector3(0.0, 0.05, 0.0)
    debug:AddLine(nodePos + bias, self.currentPath_[1] + bias, Color(1.0, 1.0, 1.0))

    if size > 1 then
      for i = 1, size - 1 do
        debug:AddLine(self.currentPath_[i] + bias, self.currentPath_[i + 1] + bias, Color(1.0, 1.0, 1.0))
      end
    end
  end
end

function FoinSpider:SetState(state)
  self.currentState_ = state
  
  if state == self.STATE_STAND then
    self:StateStand()
  elseif state == self.STATE_FOLLOW then
    self:StateFollow()
  end
  
end

function FoinSpider:StateStand()
  local STAND_ANI = "Models/foinSpider/stand.ani"
  local animCtrl = self.node:GetComponent("AnimationController")
  
  if animCtrl ~= nil then
    if animCtrl:IsPlaying(STAND_ANI) then
    else
      animCtrl:Play(STAND_ANI, 0, true, 0.1)
    end
  end
end

function FoinSpider:StateFollow()
  local WALK_ANI = "Models/foinSpider/walk.ani"
  local animCtrl = self.node:GetComponent("AnimationController")
  local body = self.node:GetComponent("RigidBody")
  
  if animCtrl ~= nil then
    if animCtrl:IsPlaying(WALK_ANI) then
      animCtrl:SetSpeed(WALK_ANI, (body:GetLinearVelocity():Length()) / (self.MOVE_FORCE * 10.0))
    else
      animCtrl:Play(WALK_ANI, 0, true, 0.1)
      animCtrl:SetSpeed(WALK_ANI, (body:GetLinearVelocity():Length()) / (self.MOVE_FORCE * 10.0))
    end
  end
  
  local navMesh = self.node:GetScene():GetComponent("NavigationMesh")
  local pathPos = navMesh:FindNearestPoint(self.targetNode_:GetWorldPosition(), Vector3.ONE * self.nearestExtents_)
  
  self.pathEndPos_ = pathPos
  self.currentPath_ = navMesh:FindPath(self.node:GetPosition(), self.pathEndPos_)
  print("telling to follow")
end

function FoinSpider:FollowPath(timeStep)
  if self.currentPath_ == nil then
    return
  end

  if table.maxn(self.currentPath_) > 0 then
    local nextWaypoint = self.currentPath_[1] -- NB: currentPath[1] is the next waypoint in order
    
    local nodePos = self.node:GetWorldPosition()
    
    local body  = self.node:GetComponent("RigidBody")

    --todo should moveDir be normal dir + target dir?
    local moveDir = (nextWaypoint - nodePos):Normalized()
    local velocity = body.linearVelocity
    --local rot = self.node.rotation
    body:ApplyImpulse(--[[rot *--]] moveDir * self.MOVE_FORCE)
        
    local brakeForce = velocity * -self.BRAKE_FORCE
    body:ApplyImpulse(brakeForce)
    
    --todo combine slerp dest with target dir
    
    if (nextWaypoint - nodePos):Length() < 0.1 then
      table.remove(self.currentPath_, 1)
      return
    end
    
  end
end

[/code]

pic for motivation:
[img]http://img.ctrlv.in/img/15/12/09/566868c94ed89.png[/img]

-------------------------

practicing01 | 2017-01-02 01:08:35 UTC | #2

I got the spider to face correctly by separating the physics components from the model components.  The model components went into a dummy node that was then rotated by -90.  I think I exported using the proper front view in blender so I don't know why I had to resort to this hack.  Perhaps bullet transformations are incompatible with urhos.

[img]http://img.ctrlv.in/img/15/12/12/566c22fb20cc5.png[/img]

-------------------------

Modanung | 2017-01-02 01:08:37 UTC | #3

[quote="practicing01"]I think I exported using the proper front view in blender so I don't know why I had to resort to this hack.[/quote]
I think the axes mentioned after each [i]Front view[/i] option in the Urho3D exporter are confusing. Be sure to double check that export setting while ignoring what's in between parentheses.
Also set Origin to Global and apply the spider's rotation by hitting Ctrl+A, R while having it selected. That way it's more WYSIWYG.

-------------------------

