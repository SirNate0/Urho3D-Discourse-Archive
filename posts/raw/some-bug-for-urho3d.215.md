att | 2017-01-02 00:58:55 UTC | #1

I think following code 
void LogicComponent::HandlePhysicsPostStep(StringHash eventType, VariantMap& eventData)
{
    using namespace PhysicsPostStep;
    
    // Execute user-defined fixed post-update function
    [b]FixedUpdate(eventData[P_TIMESTEP].GetFloat());[/b]
}

should be

void LogicComponent::HandlePhysicsPostStep(StringHash eventType, VariantMap& eventData)
{
    using namespace PhysicsPostStep;
    
    // Execute user-defined fixed post-update function
    [b]FixedPostUpdate(eventData[P_TIMESTEP].GetFloat());[/b]
}

-------------------------

cadaver | 2017-01-02 00:58:55 UTC | #2

Good find, thanks!

-------------------------

