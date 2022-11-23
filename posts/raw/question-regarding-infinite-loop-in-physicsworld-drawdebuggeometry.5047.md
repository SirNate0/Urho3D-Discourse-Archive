Leith | 2019-03-23 09:53:04 UTC | #1

Recently, my frame update has become a little more complex, and I have started to notice a problem that happens randomly, but consistently.
At (or near) the first frame, Debug Drawing of physics geometry enters into an infinite loop, and though I can break the loop in my debugger, it tells me every time that this loop is all about physics debug drawing.![debugdrawbug|690x144](upload://iyUJBJFcncBzwQDCPO9zLRv3Xlh.png)

When the issue occurs, its like the cpu is spinning its wheels - I get a graphical output, but time stands still on the first frame, with debugging still working - its very odd, and seems to be narrowed down to debugdraw of (definitely disabled) constraints. I sense a threading issue. Something is not happening at a convenient moment.

-------------------------

Leith | 2019-03-23 09:54:49 UTC | #2

I wish I could say that turning on debug drawing at runtime was the answer, but this issue also sometimes happens when I do that, plus it gets tiresome to hit an extra key when debugging.

-------------------------

Modanung | 2019-03-23 10:44:22 UTC | #3

What does your `HandlePosterRenderUpdate` (or equivalent) function look like?

-------------------------

Leith | 2019-03-23 11:57:18 UTC | #4

[code]
void Character::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
{
   // if (drawDebug_)
   if(solver_!=nullptr)
        solver_->DrawDebugGeometry(false);
}
[/code]

looks pretty safe to me - that part is just for ik debugging

I am sorry, here is the rest.
[code]

        void GamePlayState::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
        {
            // If draw debug mode is enabled, draw physics debug geometry. Use depth test to make the result easier to interpret
            if (drawDebug_)
                gamescene_->GetComponent<PhysicsWorld>()->DrawDebugGeometry(false);
        }
[/code]

-------------------------

Leith | 2019-03-24 03:33:59 UTC | #5


I definitely feel this issue is not directly caused by my disabling of constraints, although I was suprised that Bullet does not check whether a constraint is disabled before attempting to debug-draw it.
The process seems to be spending an inordinate amount of time trying to draw some lines (probably arcs) for constraints that are effectively disabled. The implication of disabling constraints is that they are not updated in Bullet, and so they are very likely to be violated by me teleporting connected bodies prior to debugdraw. This might cause problems when drawing the arcs that represent angular limits.

In one execution, I was able to break into a worker thread that appears to be waiting for a mutex that is never unlocked. I will try to reproduce this result in order to capture the call stack.
It really does smell like a threading issue, since the problem does not occur on every execution, it happens more or less randomly, but always during the debug-drawing of constraints on the first frame.![debug_threading|690x166](upload://oDcaa3dzzkdSBw5xXvfY7e3l3Tj.png)

-------------------------

Leith | 2019-03-25 07:07:06 UTC | #6

When this bug occurs, the following call is never returning to the caller.
[code]
gamescene_->GetComponent<PhysicsWorld>()->DrawDebugGeometry(false);
[/code]

Ultimately, the issue seems to be that I screw around with constrained rigidbodies after the physics tick but before the debug-drawing : despite the fact that my constraints are disabled, Bullet attempts to draw them, and since they are disabled, and the bodies have been moved, constraint state is no longer assured to be valid (I create constraints on the model in its bindpose, but we've animated the model, and its rigidbodies, and not corrected the constraint transforms).

The error appears to be related to drawing limit arcs on violated constraints:
[quote]
|#0 ??|__sincosf_fma (x=-nan(0x7fffff), sinx=0x7fffffffd7bc, cosx=0x7fffffffd7b8) (../sysdeps/x86_64/fpu/multiarch/s_sincosf-fma.c:161)|
|---|---|
|#1 0x555555bef83b|btDiscreteDynamicsWorld::debugDrawConstraint(btTypedConstraint*) () (??:??)|
|#2 0x555555bf8ce4|btDiscreteDynamicsWorld::debugDrawWorld() () (??:??)|
|#3 0x5555557d9597|Urho3D::PhysicsWorld::DrawDebugGeometry(bool) () (??:??)|
|#4 0x55555563d6f3|GameState::GamePlayState::HandlePostRenderUpdate(this=0x55555708ed20, eventType=..., eventData=...) (/home/leith/Desktop/NewFolder/UrhoTest/source/GameStates.cpp:832)|
|#5 0x555555643dd9|Urho3D::EventHandlerImpl<GameState::GamePlayState>::Invoke(this=0x5555584222e0, eventData=...) (../URHO_BUILD/include/Urho3D/Core/../Core/Object.h:315)|
|#6 0x5555559abd12|Urho3D::Object::OnEvent(Urho3D::Object*, Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) () (??:??)|
|#7 0x5555559ad5e8|Urho3D::Object::SendEvent(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&) () (??:??)|
|#8 0x555555977ed2|Urho3D::Engine::Update() () (??:??)|
|#9 0x555555979456|Urho3D::Engine::RunFrame() () (??:??)|
|#10 0x555555990cf5|Urho3D::Application::Run() () (??:??)|
|#11 0x55555561d942|RunApplication() (/home/leith/Desktop/NewFolder/UrhoTest/main.cpp:146)|
|#12 0x55555561d9fd|main(argc=1, argv=0x7fffffffe648) (/home/leith/Desktop/NewFolder/UrhoTest/main.cpp:146)|
[/quote]

If we check the current stackframe in the callstack, we can see that "sincosf_fma" has been called with an invalid argument, now we could probably deal with that in Urho's debugdrawer implementation, but I truly feel that Bullet should be checking whether a constraint is disabled before trying to draw it.

I do not feel that removing and re-adding constraints to the simulation is an acceptable solution, given that we can disable them - the question I keep asking myself is "Why is Bullet trying to operate on disabled objects?" I feel this was merely an oversight in the default debugdrawer, a shortcoming which Urho has inherited - I am certain that Erwin would, if asked about this, state clearly that the default debugdrawer is meant only to act as an example, or at most as a base interface, and that end-users can adapt it to their requirements.

-------------------------

Leith | 2019-03-25 12:13:34 UTC | #7

I've narrowed this issue down to drawing of angular limits on constraints.
If I disable that, then the bug is never triggered.
This is a workaround, and not really a solution as such, but at least we now know that the issue is located in btDiscreteDynamicsWorld::debugDrawWorld(), where constraints are iterated for debug drawing, irrespective of their enabled or disabled state, or whether the constraint is otherwise in a valid state for rendering. Unfortunately, this makes it unlikely that we can deal with the problem in Urho, since we don't derive or redefine that class (and the offending method is non-virtual), and really, this is more of a Bullet issue than any problem in Urho. Therefore, I'll likely bring this issue to Erwin - but before I do, can anyone tell me precisely what version of Bullet we're using in the Master branch?

[code]
            auto* phys = gamescene_->GetComponent<PhysicsWorld>();
            phys->setDebugMode(phys->getDebugMode() &  ~btIDebugDraw::DBG_DrawConstraintLimits);
[/code]

-------------------------

