kostik1337 | 2017-01-20 09:02:38 UTC | #1

I use Urho2d, and I've got ParticleEmitter2D. I need it to stop emitting particles at some moment, but not immediately disable it, removing all particles, I need existing particles to continue living, and after all die, remove node. Only working way I found is to set node's position somewhere outside the screen, is there any less dirty-hackish way to achieve this?

-------------------------

Modanung | 2017-02-15 15:58:14 UTC | #2

You could give the emitters their own node, and set the parent to being the scene before disabling the rest of the object.

**EDIT:** *After some experimentation it seems it would be better to set emitting to false (which would need to be implemented for* `ParticleEmitter2D`*) and re-enable the emitter's node*

-------------------------

kostik1337 | 2017-01-20 18:07:03 UTC | #3

Sorry, I didn't quite get the idea. You mean, something like this?

node->RemoveChild(particleEmitter->GetNode());
node->GetScene()->AddChild(particleEmitter->GetNode());

(**node** is the top node, it has one child, which contains the **particleEmitter** component)

-------------------------

Modanung | 2017-01-27 16:42:48 UTC | #4

I was thinking more along the lines of:
```
particleEmitter_->SetEmitting(false);
particleEmitter_->GetNode()->SetParent(node_->GetScene())`.
```
And `particleEmitter_->GetNode()->SetParent(node_)` upon reuse. Along with resetting the position and the like.

-------------------------

rku | 2017-01-27 16:15:17 UTC | #5

`ParticleEmitter` has `void SetEmitting(bool enable);`, `ParticleEmitter2D` does not. Looks like it is a missing functionality.

-------------------------

Modanung | 2017-01-27 16:40:54 UTC | #6

I have no experience with the `ParticleEmitter2D` class, but would agree.

-------------------------

