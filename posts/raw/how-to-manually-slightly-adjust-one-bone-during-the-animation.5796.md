UrhoIsTheBest | 2019-12-31 01:24:12 UTC | #1

Hi,

I am new to Urho3D engine and loved it very much. I spent several weeks going through the documentation and examples. I decided to start to create a game using it after that. Now I have a question and could not solve it after trying different methods for several day. I will be really appreciated if anyone could help me :slight_smile:

**Question:** 
How to manually slightly adjust one bone during the animation.

**More details:**
**Skeleton:** I have a skeleton with ~20 bones, the root bone is "abdomen", then it's child bone "spine" which is the root bone of all the upper body bones. The "abdomen" has another two children bones named "thigh.L" and "thigh.R", which are root bones for all lower body bones.
> abdomen
>     -- spine 
>     -- thigh.L
>     -- thigh.R

**Animations:** I have N different sword attack animations for upper body; I have 8 (eight direction) different movement animations for lower body.
**Camera:** I have a camera following the character (3rd person angle), the character and camera will rotate with the mouse.  

We know it's pretty straightforward to blend upper/lower body animations to create 8*N animation combinations. (I just set lower body animation with layer = 0, and upper body animations with layer = 1, start_bone = "spine".)

Now it works like this, for example:
If the character is moving towards left. The character node is facing towards left, with the abdomen slightly up and downs during the running animation. Now If I click mouse, the upper body with attack left.
**The problem is:** I would still need the character to attack the forward (as camera direction in this case). The character attack left because "spine" is a child of "abdomen" and "abdomen" direction is controlled by the running left animation.
*My gameplay requires the sword attack/swing direction be exactly the same (only depends on the camera direction) no matter what direction the player is running. Similar to CS, you always aim forward during you press WASD keys.*
**Things I tried:** 
1. Force the "spine" node to face forward using SetWorldDirection. This does not work good because the character would be very rigid for upper body. The original attack animation, running animation both gives the "abdomen" and "spine" node some up and downs which seems more realistic;
2. Get current "spine" direction for each frame of the animation and then rotate it by 90 degrees, set the new direction. This should be the correct solution but I just could not make it work. The whole character just blink a lot, seems like the character is rotating 90 degrees every frame;
3. Use IK. I am not very familiar with IK and struggled a lot here. I set the end node IKEffector to "spine" and attach the IKSolver to "abdomen" like this:
```
// For IK
  spine_node_ = node_->GetChild("spine", true);
  spine_effector_  = spine_node_->CreateComponent<IKEffector>();
  // Control 1 segment to abdomen bone.
  spine_effector_->SetChainLength(1);

  // For the effectors to work, an IKSolver needs to be attached to one of
  // the parent nodes. Typically, you want to place the solver as close as
  // possible to the effectors for optimal performance. Since in this case
  // we're solving the legs only, we can place the solver at the spine.
  abdomen_node_ = node_->GetChild("abdomen", true);
  solver_ = abdomen_node_->CreateComponent<IKSolver>();

  // Two-bone solver is more efficient and more stable than FABRIK (but only
  // works for two bones, obviously).
  solver_->SetAlgorithm(IKSolver::ONE_BONE);

  // Disable auto-solving, which means we need to call Solve() manually
  solver_->SetFeature(IKSolver::AUTO_SOLVE, false);
//  solver_->SetFeature(IKSolver::TARGET_ROTATIONS, true);

  // Only enable this so the debug draw shows us the pose before solving.
  // This should NOT be enabled for any other reason (it does nothing and is
  // a waste of performance).
  solver_->SetFeature(IKSolver::UPDATE_ORIGINAL_POSE, true);
```
This just somehow makes my whole character changed, e.g. upside down. **Should I expect the "abdomen" bone changes the position using this setting? If the root node of IK chain will change, maybe I should set "spine" as root node? Then there is  only one node, there is no chain anymore, how should I make IK change only "spine?**


I believe solution 2 should be the correct way to solve it, but I just don't know how to fix all the details.


-------------------------------------------------
BTW:
I've been looking for a 3D game engine for a long time and finally found Urho3D. It satisfied all my requirement:
1. **Light weighted.** I've used Unity and Unreal for a while, but could not stand those big engines. I don't need 99% of those stuff but there is no choice. For my 2014 macbook pro, it cannot even run an empty Unreal project fluently, very disappointing.
2. **Programmer friendly**. I don't like those drag & mouse click operations in editors. It's very inefficient. I like to see everything including settings in code.

The only drawback for me is the **lack of documentation,** which I hope will be improved in the near future.

-------------------------

Modanung | 2019-12-30 12:27:58 UTC | #2

Hello... @UrhoIsTheBest and welcome to the forums! :confetti_ball: :slightly_smiling_face:
Did you take a look at sample 45? (located in Urho3D/Source/Samples/)
Furthermore [here](https://urho3d.github.io/documentation/HEAD/_i_k.html)'s the docs on IK.

For updating a single animated bone, basically all you need to know is that its transform has to be modified during the `SceneDrawableUpdateFinished` event. To get it right though, you may need to do some `Slerp`ing and understand vector math concepts like the cross product and dot product.

-------------------------

Dave82 | 2019-12-30 13:54:31 UTC | #3

[quote="UrhoIsTheBest, post:1, topic:5796"]
How to manually slightly adjust one bone during the animation.
[/quote]
Hi ! I don't know if it will help your situation but the best and most generic way to adjust a bone transform is to subscribe to the E_SCENEDRAWABLEUPDATEFINISHED event and handle it there.
This event is called after all your nodes transforms and updated /calcualated and are ready for rendering.
So you can adjust a bone transform in this function and it will not be overridden by the animation.

-------------------------

UrhoIsTheBest | 2019-12-30 22:18:43 UTC | #4

[quote="Modanung, post:2, topic:5796"]
Furthermore [here ](https://urho3d.github.io/documentation/HEAD/_i_k.html)’s the docs on IK.
[/quote]
Yes, I did check the doc, but I could not figure out which bones are affected and how to choose the correct parameter during the IK process just from the doc.
[quote="Modanung, post:2, topic:5796"]
Did you take a look at sample 45? (located in Urho3D/Source/Samples/)
[/quote]
Yes, I did check example 45. That was much simpler though.

For that example, the bone hierarchy is (from parent to children):
> Bip01_Spine *(IKSolver attached here)*
> --> Bip01_R_Thigh 
> --> Bip01_R_Calf
> --> Bip01_R_Foot *(IKEffector attached here)*

Then it set:
```c++
solver_->SetAlgorithm(IKSolver::TWO_BONE);
rightEffector_->SetChainLength(2);
```
My understanding is (correct me if I am wrong):
This means the bones 2 levels up the effector node would modify the transform, e.g. 3 bones `Bip01_R_Thigh`, `Bip01_R_Calf`, and `Bip01_R_Foot` would be modified. This seems correct according to the demo.

For my case, however, I only need to change "spine" bone, which is the direct child of root bone "abdomen".
> abdomen *(IKSolver attached here)*
> --> spine *(IKEffector attached here)*
Then I can only set:
```c++
solver_->SetAlgorithm(IKSolver::ZERO_BONE);
effector_->SetChainLength(0);
```
Which does **NOT** make any sense, right?

I also tried to use
```c++
solver_->SetAlgorithm(IKSolver::ONE_BONE);
effector_->SetChainLength(1);
```
Then the `abdomen` bone is also modified during the test, the animation seems broken and flicker.

-------------------------

UrhoIsTheBest | 2019-12-30 22:28:45 UTC | #5

That's what I tried according to Example 45.
You can also check my reply to [Modanung](/u/Modanung) above, any advice?

Also I have another related question about the `E_SCENEDRAWABLEUPDATEFINISHED`.

If I need to do physics collision check, e.g. blade vs. enemy body. We know those calculation usually happens in the `FIXEDUPDATE`.
If somehow I update the bone position during `E_SCENEDRAWABLEUPDATEFINISHED`, Would it mess up the physics collision?

For example, in the original animation, the body faces left, the blade swing towards left. So the blade will collide objects in the left side. However, when we force the upper body face forward direction in `E_SCENEDRAWABLEUPDATEFINISHED`. There is no physics collision detection for blade swing towards forward anymore.
The game would look like the character swing a sword in forward direction and it hits the objects in the left side?

-------------------------

UrhoIsTheBest | 2020-01-06 08:22:10 UTC | #6

After days of playing around, now I have a better understanding of the engine and I believe it's powerful enough to do most of things I wanted. I am going to close this thread with some notes which might be helpful for others.

1. I misunderstood the power of IK. It actually only does one thing: calculate the positions of all bones from root-bone to end-bone given the desired location of end-bone. It does not care much about pure rotations. 
For example, if you want `thorax` bone to face one direction and `abdomen` to face another direction. IK would not help you to find a *Visually Natural* rotation between those bones. You have to manually set that by yourself, e.g. `abdomen` bone can face left, then set `spine` bone to rotate 45 degree around axis-Y, also set `thorax` bone to rotate 45 degree around axis-Y. Thus, `thorax` faces forward (45+45=90). You could also set with 30, 60 degree respectively.

2. **You can reconstruct the skeleton structure by inserting extra nodes.**
For example, I tried to add two extra nodes, `lower_body_root_node` and `upper_body_root_node`. Then move `spine` node as child of `upper_body_root_node` (`abdomen` child to `lower_body_root_node` respectively). The original animation system still works perfectly. But I have another degree of freedom to separately control upper & lower body, e.g. rotate some degree between them.

3. **You can do almost everything you want about raw animation resource data due to the accessibility of KeyFrame data.**
An example code path could be
```c++
AnimationState->GetAnimation()->GetTrack(String("abdomen"))->keyFrames_
```
You can directly manipulate bone `position` and `rotation` in [AnimationKeyFrame](https://urho3d.github.io/documentation/1.5/struct_urho3_d_1_1_animation_key_frame.html).
For example, if I want to only apply the rotation change during a bone animation while fixing the bone position (ignoring the position change). You could do something like:
```c++
Vector3 tmp = Vector3::ZERO;
for (AnimationKeyFrame& key_frame : animation_state->GetAnimation()->GetTrack(String("abdomen"))->keyFrames_) {
  // Set all position as the 1st frame, e.g. no position movement for additive animation.
  if (tmp == Vector3::ZERO) {
    tmp = key_frame.position_;
  } else {
    key_frame.position_ = tmp;
  }
}
```
You could do many other interesting stuff with directly manipulating the animation data.

4. **Many other small things** which I wish I could've learned in tutorials somewhere by more experienced developers.

-------------------------

CE184 | 2020-11-23 05:19:08 UTC | #7

I had the same question and thanks, the E_SCENEDRAWABLEUPDATEFINISHED works for me.
But is this event before or after physics update? because I need the physics collision happen to the modified bone  transform too. I check [this page](https://urho3d.github.io/documentation/1.6/_main_loop.html) for the main loop order but could not find the E_SCENEDRAWABLEUPDATEFINISHED.

-------------------------

jmiller | 2020-11-23 12:10:02 UTC | #8

Hello,

I find a few references to that event with regex search:
Defined in  https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/SceneEvents.h

and docs IK section (you linked to 1.6 by the way, a very old version):
  https://urho3d.github.io/documentation/HEAD/_i_k.html#iksolverautosolve

It appears Octree is updated by Renderer in Update.. 
  https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Renderer.cpp#L1503

Could try a breakpoint or such to find relative order.
HTH

-------------------------

