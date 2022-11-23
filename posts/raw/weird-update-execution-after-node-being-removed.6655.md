CE184 | 2021-01-09 01:47:54 UTC | #1

**I found the component Update() function is still executed one time after the component/node is removed. And the override base class function is not executed at that place.**

I have a base component class for character control:
```
class CharacterControllerBase : public LogicComponent {
 URHO3D_OBJECT(CharacterControllerBase, LogicComponent)
 ...
```
And another derived class 
```
class CharacterControllerPlayer : public CharacterControllerBase {
 URHO3D_OBJECT(CharacterControllerPlayer, CharacterControllerBase)
 ...
```

In the base class, Update() function is:
```
void CharacterControllerBase::Update(float timestep) {
  LogicComponent::Update(timestep);
  // ...
  spdlog::debug("base charcter_control_input_ type: {}",
                magic_enum::enum_name(character_control_input_->GetInputType()));
  if (character_control_input_->GetInputType() == kPlayer) {
    spdlog::debug("base charcter_control_input_: {}", character_control_input_);
    // ...
  }
}
```
And in the derived class, Update() function is:
```
void CharacterControllerPlayer::Update(float timestep) {
  CharacterControllerBase::Update(timestep);  // not called?
  spdlog::debug("charcter_control_input_: {}", character_control_input_);
  // ...
}
```

During the program, I created this derived component ```CharacterControllerPlayer``` to attached to the character node, and then remove the whole node when character dies:
```
  spdlog::debug("{}: Character died.", node_->GetName().CString());
  node->Remove();
```


I am confused by the log dump
```
// Before node is removed, Update() execution seems normal.
[2021-01-06 10:26:42.531] [debug] base charcter_control_input_ type: kPlayer
[2021-01-06 10:26:42.531] [debug] base charcter_control_input_: 0x7fc0dd9a7c60
[2021-01-06 10:26:42.531] [debug] charcter_control_input_: 0x7fc0dd9a7c60
...
[2021-01-06 10:26:42.584] [debug] Player: Character died.
[2021-01-06 10:26:42.586] [debug] charcter_control_input_: 0x0
// Notice character_control_input_ is another component attached to the node and is nullptr after node is removed.
```

After player dies and the node is removed. The ```CharacterControllerPlayer::Update()``` **is still called!** However, the base class function ```CharacterControllerBase::Update(timestep);``` **is in the override function but is not called?!**

-------------------------

SirNate0 | 2021-01-09 03:56:53 UTC | #2

In the `// ...` in the base class do you return early at some point? Maybe on some null pointer check or something?

-------------------------

CE184 | 2021-01-09 03:56:47 UTC | #3

You are right! the check death logic is there and ```node->Remove()``` is called during that time. Stupid me.

-------------------------

