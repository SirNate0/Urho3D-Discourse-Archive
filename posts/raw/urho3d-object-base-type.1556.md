sabotage3d | 2017-01-02 01:08:29 UTC | #1

Hi guys I switched to 1.5 from 1.4 and I have a question for the new URHO3D_OBJECT. In 1.4 we just defined OBJECT(typeName) and we had seperate macro for the BASEOBJECT wich wasn't mandatory if I am not mistaken. Now we have URHO3D_OBJECT(typeName, baseTypeName), where we always have to specify the base type. For the base type do we have to specify a base class from Urho3d or it can be any other base class for example:
[code]class State: public LogicComponent
{ ... }
class JumpState: public State
{ ... }[/code]
Do we need URHO3D_OBJECT(JumpState, State) or URHO3D_OBJECT(JumpState, LogicComponent)?

-------------------------

ghidra | 2017-01-02 01:08:29 UTC | #2

This would be correct:

for state
[code]
 URHO3D_OBJECT(State, LogicComponent)
[/code]

for jumpsate
[code]
 URHO3D_OBJECT(JumpState, State)
[/code]

-------------------------

sabotage3d | 2017-01-02 01:08:29 UTC | #3

Thanks It makes sense now.

-------------------------

