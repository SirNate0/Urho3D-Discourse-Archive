oooooome | 2021-09-14 03:47:19 UTC | #1

hi, all!

I am trying to use inverse kinematics to control the flexion of my fingers, but there seems to be a problem.

I am currently controlling the index finger. The method I use is to set the effector on the farthest joint of the index finger, and set the solver on the bottom joint of the index finger, and update the target position of the effector every time to make the index finger bend.

```
    //set the Effector and Solver
    //...
    bindLeftHandTrans = modelNode->GetChild(("LeftHand"), true);
    bindLeftHandTrans->SetWorldPosition(Vector3(0, -10, 0));
    bindLeftHandTrans->SetRotation(Quaternion(0, 90, 90));
    bindLeftHandIndex1 = modelNode->GetChild(("LeftHandIndex1"), true);
    bindLeftHandIndex2 = modelNode->GetChild(("LeftHandIndex2"), true);
    bindLeftHandIndex3 = modelNode->GetChild(("LeftHandIndex3"), true);

    indexEffector_3 = bindLeftHandIndex3->CreateComponent<IKEffector>();
    indexEffector_3->SetChainLength(2);
    solver_index2 = bindLeftHandIndex1->CreateComponent<IKSolver>();

    solver_index2->SetFeature(IKSolver::UPDATE_ORIGINAL_POSE, true);
    solver_index2->SetAlgorithm(IKSolver::TWO_BONE);
    solver_index2->SetFeature(IKSolver::AUTO_SOLVE, false);
    //...



    // HandleSceneDrawableUpdateFinished fuction
    //...
    indexEffector_3->SetTargetPosition(indexPos3);
    solver_index2->Solve();
    //...
```

But the result was different from what I imagined. The model's finger looked like it was broken.
![image|690x431](upload://5rbqSdcEqlM3dJ7wqr78l7ZwKkX.jpeg)

I also tried the constraints in the ragdoll example, but to no avail

I don't know if the bones of the model are bound incorrectly or the way I control it is incorrect. I want to know if anyone has solved such a problem

This is the skeleton of the model
![image|690x477](upload://7ftIHUjbil0drg1rzktnHo2jRAD.jpeg)

-------------------------

George1 | 2021-09-14 10:36:23 UTC | #2

Maybe object need to face +z direction on import or specify incorrect angle/axis for that bone.

-------------------------

Modanung | 2021-09-14 09:34:54 UTC | #3

Try putting the bones inside the finger, connected head to tail and the local X-axis pointing sideways.

-------------------------

SirNate0 | 2021-09-14 10:23:06 UTC | #4

If the model was imported from fbx into Blender I believe one of the import options will connect them head to tail for you. Though you'd have to reimport it, of course.

-------------------------

oooooome | 2021-10-08 08:11:57 UTC | #5

@Modanung @SirNate0  thanks guys, i will try!

-------------------------

