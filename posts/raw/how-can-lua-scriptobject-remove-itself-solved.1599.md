practicing01 | 2017-01-02 01:08:49 UTC | #1

Edit: Thanks Mike.

Hello, I'm using lua ScriptObjects like LogicComponents.  I need a ScriptObject to remove itself from the node.  self:Remove() isn't working.  Thanks for any help.

ScriptObject that is trying to remove itself:
[code]
Snare = ScriptObject()

function Snare:Start()
  self.active_ = false
  self.magnitude_ = 1.0
  self.duration_ = -1.0
  self.elapsedTime_ = 0.0
end

function Snare:Snare(magnitude, duration)
  local speedSO = self.node:GetScriptObject("Speed")
  if speedSO == nil then return end
  
  self.active_ = true
  self.magnitude_ = magnitude
  self.duration_ = duration
  self.elapsedTime_ = 0.0
  
  speedSO.speed_ = speedSO.speed_ - self.magnitude_
end

function Snare:Update(timeStep)
  if self.active_ == false then return end
  
  if self.duration_ == -1.0 then return end
  
  self.elapsedTime_ = self.elapsedTime_ + timeStep
  
  if self.elapsedTime_ >= self.duration_ then
    local speedSO = self.node:GetScriptObject("Speed")
    
    if speedSO ~= nil then
      speedSO.speed_ = speedSO.speed_ + self.magnitude_
    end
    
    self:Remove()
  end
  
end

[/code]

-------------------------

1vanK | 2017-01-02 01:08:49 UTC | #2

may be (becose LuaScriptInstance is Component)
node->RemoveComponent()

-------------------------

practicing01 | 2017-01-02 01:08:55 UTC | #3

self.node:RemoveComponent(self) didn't work, the Update() loop still runs.

-------------------------

Mike | 2017-01-02 01:08:55 UTC | #4

This is demonstrated in sample 13_Ragdolls:
[code]self.instance:Remove()[/code]

-------------------------

