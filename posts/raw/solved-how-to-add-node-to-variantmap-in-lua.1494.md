practicing01 | 2017-01-02 01:08:08 UTC | #1

Edit: This worked:
[code]
local v = Variant(self.targetData.node_)
local ed = VariantMap()
ed["Node"] = v
SendEvent("GetNodeInfo", ed)
[/code]

Unfinished script for snippet reference:
[spoiler][code]
Cyberetta = ScriptObject()

function Cyberetta:Start()
  self.skillData =
  {
    clientExecuting_ = false,
    elapsedTime_ = 0.0,
    cooldown_ = 0.0
  }
  
  self.targetData =
  {
    node_ = nil,
    lc_ = "",
    clientID_ = -1,
    nodeID_ = -1
  }

  self:SubscribeToEvent("SkillbarButt", "Cyberetta:HandleSkillbarButt")
end

function Cyberetta:Stop()
  if self.skillData.clientExecuting_ then
    local ed = VariantMap()
    SendEvent("TouchUnSubscribe", ed)
  end
end

function Cyberetta:HandleSetNodeInfo(eventType, eventData)
  local sceneNode = eventData["Node"]:GetPtr("Node")
  
  if sceneNode == self.targetData.node_ then
  self.targetData.lc_ = eventData["Lc"]:GetString()
  self.targetData.clientID_ = eventData["ClientID"]:GetInt()
  self.targetData.nodeID_ = eventData["NodeID"]:GetInt()
  end
  
  self:UnsubscribeFromEvent("SetNodeInfo")
end

function Cyberetta:HandleSkillbarButt(eventType, eventData)
    local skill = eventData["Skill"]:GetString()
    if skill ~= "Cyberetta" then
      return
    end
    
    local blindLC = self.node:GetComponent("Blind")
    local isBlind = false
    
    if blindLC ~= nil then
      isBlind = blindLC.isBlind_
    end
     
    if self.skillData.clientExecuting_ == true and isBlind == true then
      return
    end
    
    self.skillData.clientExecuting_ = true
    self.skillData.elapsedTime_ = 0.0
    
    local ed = VariantMap()
    SendEvent("TouchSubscribe", ed)
    
    self:SubscribeToEvent("TouchEnd", "Cyberetta:HandleTouchEnd")
end

function Cyberetta:HandleTouchEnd(eventType, eventData)
  if ui.focusElement ~= nil then
    return
  end
  
  self:UnsubscribeFromEvent("TouchEnd")
  
  local ed = VariantMap()
  
  SendEvent("TouchUnSubscribe", ed)
  
  local cameraNode = self.node:GetChild("cameraNode")
  local camera = cameraNode:GetComponent("Camera")
  
  local pos = { x = 0.0, y = 0.0}
  pos.x = eventData["X"]:GetInt()
  pos.y = eventData["Y"]:GetInt()
  
  local cameraRay = camera:GetScreenRay(pos.x / graphics.width, pos.y / graphics.height)

  local physicsWorld = self.node:GetScene():GetComponent("PhysicsWorld")
  
  local raeResult = physicsWorld:RaycastSingle(cameraRay, 10000.0, 2)
  
  if raeResult.body ~= nil then
    self:ClearTarget()
    
    self.targetData.node_ = raeResult.body:GetNode()
    
    self:SubscribeToEvent("SetNodeInfo", "Cyberetta:HandleSetNodeInfo")
    
    local v = Variant(self.targetData.node_)
    local ed = VariantMap()
    ed["Node"] = v
    SendEvent("GetNodeInfo", ed)
    
    if self.targetData.clientID_ ~= -1 then
      self:Exec(0.0, true)
    end
    
  else
    self.skillData.clientExecuting_ = false
  end
  
end

function Cyberetta:Exec(timeRamp, sendToServer)
  if engine:IsHeadless() ~= true then
    --particles and sound
  end
  print("execing")
end

function Cyberetta:ClearTarget()
  self.targetData.node_ = nil
  self.targetData.lc_ = ""
  self.targetData.clientID_ = -1
  self.targetData.nodeID_ = -1
end

[/code][/spoiler]

Hello, I'm getting "attempt to call method 'SetPtr' (a nil value)" with the following lua code:

[code]
local ed = VariantMap()
ed:SetPtr("Node", self.node)
SendEvent("GetNodeInfo", ed)
[/code]

Thanks for any help.

Full, incomplete script:
[spoiler][code]
Cyberetta = ScriptObject()

function Cyberetta:Start()
  self.skillData =
  {
    clientExecuting_ = false,
    elapsedTime_ = 0.0,
    cooldown_ = 0.0
  }
  
  self:SubscribeToEvent("SetNodeInfo", "Cyberetta:HandleSetNodeInfo")
  local ed = VariantMap()
  ed:SetPtr("Node", self.node)
  SendEvent("GetNodeInfo", ed)

  self:SubscribeToEvent("SkillbarButt", "Cyberetta:HandleSkillbarButt")
end

function Cyberetta:Stop()
  if self.skillData.clientExecuting_ then
    local ed = VariantMap()
    SendEvent("TouchUnSubscribe", ed)
  end
end

function Cyberetta:HandleSetNodeInfo(eventType, eventData)
  local sceneNode = eventData["Node"]:GetPtr("Node")
  
  if sceneNode == self.node then
    --
  end
  
  self:UnsubscribeFromEvent("SetNodeInfo")
  print("got SetNodeInfo")
end

function Cyberetta:HandleSkillbarButt(eventType, eventData)
    local skill = eventData["Skill"]:GetString()
    if skill ~= "Cyberetta" then
      return
    end
    
    local blindLC = self.node:GetComponent("Blind")
    local isBlind = false
    
    if blindLC ~= nil then
      isBlind = blindLC.isBlind_
    end
     
    if self.skillData.clientExecuting_ == true and isBlind == true then
      return
    end
    
    self.skillData.clientExecuting_ = true
    self.skillData.elapsedTime_ = 0.0
    
    local ed = VariantMap()
    SendEvent("TouchSubscribe", ed)
    
    self:SubscribeToEvent("TouchEnd", "Cyberetta:HandleTouchEnd")
end

function Cyberetta:HandleTouchEnd(eventType, eventData)
  if ui.focusElement ~= nil then
    return
  end
  
  self:UnsubscribeFromEvent("TouchEnd")
  
  local ed = VariantMap()
  SendEvent("TouchUnSubscribe", ed)
  
  local cameraNode = self.node:GetChild("cameraNode")
  local camera = cameraNode:GetComponent("Camera")
  
  local pos = { x = 0.0, y = 0.0}
  pos.x = eventData["X"]:GetInt()
  pos.y = eventData["Y"]:GetInt()
  
  local cameraRay = camera:GetScreenRay(pos.x / graphics.width, pos.y / graphics.height)

  local physicsWorld = self.node:GetScene():GetComponent("PhysicsWorld")
  
  local raeResult = physicsWorld:RaycastSingle(cameraRay, 10000.0, 2)
  
  if raeResult.body ~= nil then
    local targetNode = raeResult.body:GetNode()
    --self:Exec()
  else
    self.skillData.clientExecuting_ = false
  end
  
end

function Cyberetta:Exec(clientID, nodeID, timeRamp, sendToServer)
  if engine:IsHeadless() ~= true then
    --particles and sound
  end
  
end

[/code][/spoiler]

-------------------------

