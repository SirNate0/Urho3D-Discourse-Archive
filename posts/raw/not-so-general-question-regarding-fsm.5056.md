Leith | 2019-03-31 07:09:27 UTC | #1


So, I've started working on a template-based solution for FSM's.
I use a dedicated FSM for my gamestate manager, but I would like to find a cleaner pattern, and implement it more widely...

Other than gamestate management, I have (at least) two more possible use-cases: one is the Character Class, and the other is a derived AnimationController, which implements a similar logic to Unity / Mechanim.

I'd love to hear what you guys are doing, what your implementation looks like.
I wasted some time trying to implement script-based condition checking, but in the end I would rather rush to a working data-driven solution in c++ than mess around with scripts.

Here's a high-level peek at my implementation, happy to share.

[code]
        void Character::DelayedStart(){

            /// Instantiate all possible States: note, all States are notified which StateMachine owns them
            State<Character>* idle = new IdleState(stateMachine);
            State<Character>* walk = new WalkingState(stateMachine);

            /// Populate States with valid State Transitions: note, all States know a list of possible states
            /// that they can, under the right Conditions, transition to.
            idle->AddTransition(walk);
            walk->AddTransition(idle);

            /// Set the initial State
            stateMachine->SetCurrentState(idle);

        }
[/code]

-------------------------

