practicing01 | 2017-01-02 01:08:08 UTC | #1

Hello, not sure if lua even has that but if it does it's not being called.  If it doesn't then I'm getting self == nil on an event handler.  Thanks for any help.

Unfinished script for reference:
[spoiler][code]
local MSG_LCMSG = 8008148

Cyberetta = ScriptObject()

function Cyberetta:Start()
  self.skillData =
  {
    clientExecuting_ = false,
    elapsedTime_ = 0.0,
    cooldown_ = 1.0,
    lc_ = "",
    clientID_ = -1,
    nodeID_ = -1
  }
  
  self.targetData =
  {
    node_ = nil,
    lc_ = "",
    clientID_ = -1,
    nodeID_ = -1
  }

  --[[self.targetData.node_ = self.node

  self:SubscribeToEvent("SetNodeInfo", "Cyberetta:HandleSetNodeInfo")

  local vm = VariantMap()
  vm["Node"] = Variant(self.targetData.node_)
  SendEvent("GetNodeInfo", vm)

  self.skillData.lc_ = self.targetData.lc_
  self.skillData.clientID_ = self.targetData.clientID_
  self.skillData.nodeID_ = self.targetData.nodeID_

  self:SubscribeToEvent("SkillbarButt", "Cyberetta:HandleSkillbarButt")
  self:SubscribeToEvent("LcMsg", "Cyberetta:HandleLCMSG")
  self:SubscribeToEvent("GetLc", "Cyberetta:HandleGetLc")--]]
end

function Cyberetta:DelayedStart()
  print("delayed start")
  self.targetData.node_ = self.node

  self:SubscribeToEvent("SetNodeInfo", "Cyberetta:HandleSetNodeInfo")

  local vm = VariantMap()
  vm["Node"] = Variant(self.targetData.node_)
  SendEvent("GetNodeInfo", vm)

  self.skillData.lc_ = self.targetData.lc_
  self.skillData.clientID_ = self.targetData.clientID_
  self.skillData.nodeID_ = self.targetData.nodeID_

  self:SubscribeToEvent("SkillbarButt", "Cyberetta:HandleSkillbarButt")
  self:SubscribeToEvent("LcMsg", "Cyberetta:HandleLCMSG")
  self:SubscribeToEvent("GetLc", "Cyberetta:HandleGetLc")
end

function Cyberetta:Stop()
  if self.skillData.clientExecuting_ then
    local vm = VariantMap()
    SendEvent("TouchUnSubscribe", vm)
  end
end

function Cyberetta:HandleSetNodeInfo(eventType, eventData)
  local sceneNode = eventData["Node"]:GetPtr("Node")
  
  if sceneNode == self.targetData.node_ then
  self.targetData.lc_ = eventData["Lc"]:GetString()
  self.targetData.clientID_ = eventData["ClientID"]:GetInt()
  self.targetData.nodeID_ = eventData["NodeID"]:GetInt()
  
  print(self.targetData.lc_)
  print(self.targetData.clientID_)
  print(self.targetData.nodeID_)
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
    
    local vm = VariantMap()
    SendEvent("TouchSubscribe", vm)
    
    self:SubscribeToEvent("TouchEnd", "Cyberetta:HandleTouchEnd")
end

function Cyberetta:HandleTouchEnd(eventType, eventData)
  if ui.focusElement ~= nil then
    return
  end
  
  self:UnsubscribeFromEvent("TouchEnd")
  
  local vm = VariantMap()
  
  SendEvent("TouchUnSubscribe", vm)
  
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
    
    local vm = VariantMap()
    vm["Node"] = Variant(self.targetData.node_)
    SendEvent("GetNodeInfo", vm)
    
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
  
  local vm = VariantMap()
  vm["Node"] = Variant(self.node)
  vm["Animation"] = Variant("attack")
  vm["Loop"] = Variant(false)
  vm["Layer"] = Variant(1)
	SendEvent("AnimateSceneNode", vm);
  
  self.skillData.elapsedTime_ = timeRamp
  
  if sendToServer == true then    
    local msg = VectorBuffer()
    msg:WriteInt(self.skillData.clientID_)
    msg:WriteString("Cyberetta")
    msg:WriteInt(self.skillData.nodeID_)
    msg:WriteString(self.targetData.lc_)
    msg:WriteInt(self.targetData.clientID_)
    msg:WriteInt(self.targetData.nodeID_)
    msg:WriteFloat(timeRamp)
    
    if network:IsServerRunning() then
      network:BroadcastMessage(MSG_LCMSG, true, true, msg);
    else
      network:GetServerConnection():SendMessage(MSG_LCMSG, true, true, msg);
    end
    
  end

  self:SubscribeToEvent("Update", "Cyberetta:HandleUpdate")
end

function Cyberetta:ClearTarget()
  self.targetData.node_ = nil
  self.targetData.lc_ = ""
  self.targetData.clientID_ = -1
  self.targetData.nodeID_ = -1
end

function Cyberetta:HandleUpdate(eventType, eventData)
  local timeStep = eventData["TimeStep"]:GetFloat()
  
  self.skillData.elapsedTime_ = self.skillData.elapsedTime_ + timeStep
  
  if self.skillData.elapsedTime_ >= self.skillData.cooldown_ then
    self.skillData.clientExecuting_ = false
    self:UnsubscribeFromEvent("Update")
  end
  
end

function Cyberetta:HandleLCMSG(eventType, eventData)
  print("handleLC")
  local msg = eventData["Data"]:GetBuffer()
  
  local clientID = msg:ReadInt()
  local lc = msg:ReadString()
  
  if lc == "Cyberetta" then
    if self.skillData.clientID_ == clientID then
      local nodeID = msg:ReadInt()
      if self.skillData.nodeID_ == nodeID then        
        local targetLC = msg:ReadString()
        local targetClientID = msg:ReadInt()
        local targetNodeID = msg:ReadInt()
        local timeRamp = msg:ReadFloat()
        
        --get lag time
        --exec
        --isServer exclusive broadcast
      end
      
    end
    
  end
  
end

function Cyberetta:HandleGetLc(eventType, eventData)
  print("getLC")
end

[/code][/spoiler]

-------------------------

cadaver | 2017-01-02 01:08:08 UTC | #2

Lua didn't have this. Will be pushed to master shortly.

-------------------------

