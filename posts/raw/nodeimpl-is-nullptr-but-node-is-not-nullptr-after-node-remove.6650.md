CE184 | 2021-01-04 09:36:27 UTC | #1

A weird nullptr problem.

I have a character node that has two important components, one is AI to find enemy targets, one is character control to handle various things like death.

In the former AI component Update() function:
```
// just for this debug, it crashed at target_->GetComponent<CharacterStatus>() below previously.
  if (target_) {
    spdlog::trace("{}: Checking target", node_->GetName().CString());
    spdlog::trace("{}: Check target: {}", node_->GetName().CString(), target_->GetName().CString());
  }
// remove dead character target.
  if (target_ && target_->GetComponent<CharacterStatus>()
      && target_->GetComponent<CharacterStatus>()->IsDead()) {
    target_ = nullptr;
  }
```
In the latter character control component Update() function, I will check if character is death and will trigger:
```
void Character::OnCharacterDeath() {
  spdlog::debug("{}: Character died.", node_->GetName().CString());
  node_->Remove();
}
```

However, when one character died, the program crashes.
The crash line is in that AI component Update() function
```
spdlog::trace("{}: Check target: {}", node_->GetName().CString(), target_->GetName().CString());
```
Particularly, the ```target_->GetName()``` operator ```->``` crashes because
```
const String& GetName() const { return impl_->name_; }
```
Notice I checked nullptr for ```target_```, so it looks like the impl_ is nullptr here.


**I am super confused. What did I do wrong?**
I don't have any strong pointer reference anywhere for the node except the root scene owns it.


For reference, here is the detailed log dump:
```
[2021-01-03 12:58:39.121] [trace] RandomAI_kBodyTeamTwo_4: Checking target
[2021-01-03 12:58:39.121] [trace] RandomAI_kBodyTeamTwo_4: Check target: RandomAI_kBodyTeamOne_3
...
[2021-01-03 12:58:39.145] [trace] RandomAI_kBodyTeamOne_3: Checking target
[2021-01-03 12:58:39.145] [trace] RandomAI_kBodyTeamOne_3: Check target: RandomAI_kBodyTeamTwo_5
[2021-01-03 12:58:39.145] [debug] RandomAI_kBodyTeamOne_3: Character died.
Assertion failed: (ptr_), function operator->, file /Users/honghaoli/git_folder/Urho3D/Source/Urho3D/AngelScript/../Core/../Container/Ptr.h, line 605.
...
[2021-01-03 12:58:39.153] [trace] RandomAI_kBodyTeamTwo_4: Checking target
Signal: SIGABRT (signal SIGABRT)
```
You can see the RandomAI_kBodyTeamTwo_4 first has a target RandomAI_kBodyTeamOne_3. Then, RandomAI_kBodyTeamOne_3 died, then when RandomAI_kBodyTeamTwo_4 AI component Update() again, it crashed.

-------------------------

Modanung | 2021-01-04 12:48:49 UTC | #2

What does `IsDead()` do in the `AI::Update()`, if the node is removed on death?

-------------------------

Eugene | 2021-01-04 18:52:59 UTC | #3

[quote="CE184, post:1, topic:6650"]
Particularly, the `target_->GetName()` operator `->` crashes because
[/quote]
Maybe dangling pointer to removed node?

-------------------------

SirNate0 | 2021-01-04 13:22:15 UTC | #4

Following up on that, is `target_` a smart pointer (Weak/SharedPtr) or a normal non-smart pointer?

-------------------------

CE184 | 2021-01-04 18:37:10 UTC | #5

```
  inline bool IsDead() const { return health_ <= 0.0f; };
```
It's just an inline function for ```CharacterStatus``` component, which does not have much logic, only store some data like ```health_```.
If the node is removed, the GetComponent<CharacterStatus> for that node should be null, right, then that if condition will not proceed.

-------------------------

CE184 | 2021-01-04 18:45:51 UTC | #6

```target_``` is just a raw pointer.
```
  Node* target_ = nullptr;
```
And the only place to set that pointer is in the same Update() function later

-------------------------

CE184 | 2021-01-04 18:49:21 UTC | #7

Yes, you both are right! My stupid mistake! :disappointed_relieved:

I should use ```WeakPtr<Node> target_``` instead of  ```Node* target_```.

-------------------------

