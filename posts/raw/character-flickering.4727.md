Zaroio | 2018-12-10 21:53:54 UTC | #1

Hi, My Character's flickering while moving, moved the code that moves the camera to FixedPostUpdate, it solved at first, but when I switched OS, it stated to flick again.
I can't show it here, cuz I cant manage to capture the flickering, prob due to the frequency my software captures it.


edit, it flickers only when the camera rotate.

    node_->SetWorldPosition((target_->GetWorldPosition() + Vector3::UP * height_) + rotation_ * ( -Vector3::FORWARD * dist_.value_ + offset_.value_));
    node_->LookAt(target_->GetWorldPosition() + Vector3::UP * height_ + rotation_ *  Vector3::FORWARD * 1000.0f);

-------------------------

Modanung | 2018-12-11 14:50:34 UTC | #2

Changes to the scene that directly modify `Node` transforms should occur during ordinary `Update` events, not fixed ones. `FixedUpdate` should be used for things like applying forces.
This is because direct node transformations are not interpolated, physics simulations are.

-------------------------

Zaroio | 2018-12-11 14:50:16 UTC | #3

Thanks removed the Fixed and it solved it.

-------------------------

