Leith | 2019-07-05 05:06:15 UTC | #1


In the following example (a guard stack for a recursive and potentially re-entrant method), I'm looking to use Node User Variables to store a VariantVector. Node::vars_ is a protected member, so we have to use accessors (GetVar/SetVar) 
Since Node::GetVar and its counterpart Node::GetVars both only provide const (read-only) access, this means that any non-trivial types such as vectors and maps need to be completely copied every time we want to perform read-write access to a node user variable.

[code]
    BTNodeState BehaviorTree::Process(float timeStep, Urho3D::ScriptInstance* callerAgent)
    {
        if (isActive_)
        {
            this->callingAgent = callerAgent;
            timeStep_=timeStep;

            /// We assume that the scriptinstance's parent node has a "subtree stack" variable...
            Variant v=callingAgent->GetNode()->GetVar("SubtreeStack_");
            if(v.GetType()==VAR_NONE)
            {
                /// Agent does not yet have a Subtree Stack variable: add one now
                VariantVector vv {this};
                callingAgent->GetNode()->SetVar("SubtreeStack_", vv);
            }else{

                /// Obtain a pointer to the stack object within variant v
                VariantVector* pv=v.GetVariantVectorPtr();

                /// Check if this behaviortree exists in the execution guard stack
                if(pv && pv->Contains(this))
                {
                    URHO3D_LOGERROR("Behavior Subtree Recursion was prevented!");
                    return NS_ERROR;
                }
                /// Push this behaviortree onto the guard stack
                pv->Push(this);

                /// Write modified variant back to node variable
                callingAgent->GetNode()->SetVar("SubtreeStack_",v);
            }

            /// Push sentinal nullptr onto list of active nodes
            activeNodes_.Push(nullptr);

            /// Execute behaviortree
            while(Step(timeStep))
                continue;

            /// Pop this behaviortree from the guard stack
            v=callingAgent->GetNode()->GetVar("SubtreeStack_"); /// Probably not necessary: local variant v should still be valid?
            v.GetVariantVectorPtr()->Pop();
            callingAgent->GetNode()->SetVar("SubtreeStack_",v);

        }
        return currentState_;
    }
[/code]

Take note of the last few lines, where we need to "pop" a value from the stack, then write the variant back to the node variable container...
Am I overlooking something?

-------------------------

Leith | 2019-07-05 06:19:46 UTC | #2

I suggest Node::GetVarPtr, and/or Node::GetVarWriteable

-------------------------

SirNate0 | 2019-07-05 17:48:20 UTC | #3

I don't really object to the idea of adding a new method to improve the functionality, but why not overload the method based on const-ness (or the GetVars() method, perhaps) instead of adding one with a new name? If we use a new babe, I propose GetModifiableVar following the pattern of the VectorBuffer GetModifiableData.
Also, if you just want a solution to not having to copy it, you can probably just const_cast away the problem (if I had to guess, I'm pretty sure it would work).

-------------------------

Leith | 2019-07-06 03:56:19 UTC | #4

It had never occurred to me that I could cast away the const-ness for direct access to subvariants, I will sure test that out, thanks!

-------------------------

