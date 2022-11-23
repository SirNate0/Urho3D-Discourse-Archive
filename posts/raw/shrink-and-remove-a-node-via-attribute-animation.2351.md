vudugun | 2017-01-02 01:14:54 UTC | #1

Hello,
  is this the proper way to shrink a node and remove it using attribute animation?

[code]void MyComponent::ShrinkAndRemove()
{
    ValueAnimation* anim{ new ValueAnimation{ context_ } };
    anim->SetKeyFrame(0.0f, Vector3{ 1.0f, 1.0f, 1.0f });
    anim->SetKeyFrame(0.5f, Vector3{ 0.2f, 0.2f, 0.2f });
    anim->SetEventFrame(0.51f, E_SHRUNK);

    GetNode()->SetAttributeAnimation("Scale", anim, WM_ONCE);

    SubscribeToEvent(GetNode(), E_SHRUNK, URHO3D_HANDLER(MyComponent, HandleShrunk));
}

void MyComponent::HandleShrunk(StringHash eventType, VariantMap& eventData)
{
    GetNode()->Remove();
}[/code]
I am asking because I need two patches to get it working.

[size=150]Problem 1[/size]

The event does not fire when time > 0.5. I traced the problem down to ValueAnimation::SetEventFrame(), where the begin/end times are [b]not[/b] updated, unlike what happens in SetKeyFrame:

[code]bool ValueAnimation::SetKeyFrame(float time, const Variant& value)
{
    ...
    beginTime_ = Min(time, beginTime_);
    endTime_ = Max(time, endTime_);
    splineTangentsDirty_ = true;

    return true;
}

void ValueAnimation::SetEventFrame(float time, const StringHash& eventType, const VariantMap& eventData)
{
    VAnimEventFrame eventFrame;
    eventFrame.time_ = time;
    eventFrame.eventType_ = eventType;
    eventFrame.eventData_ = eventData;

    if (eventFrames_.Empty() || time >= eventFrames_.Back().time_)
        eventFrames_.Push(eventFrame);
    else
    {
        for (unsigned i = 0; i < eventFrames_.Size(); ++i)
        {
            if (time < eventFrames_[i].time_)
            {
                eventFrames_.Insert(i, eventFrame);
                break;
            }
        }
    }

    // ****** NOTHING HERE?? ******
}[/code]
Copying the three lines from SetKetFrame() solved the problem.

[size=150]Problem 2[/size]

I am getting a crash inside Animatable::UpdateAttributeAnimations() just after my event handler is called (in the same loop):

[code]void Animatable::UpdateAttributeAnimations(float timeStep)
{
    if (!animationEnabled_)
        return;

    SharedPtr<Animatable> self(this); // ****** PATCH

    Vector<String> finishedNames;
    for (HashMap<String, SharedPtr<AttributeAnimationInfo> >::ConstIterator i = attributeAnimationInfos_.Begin();
         i != attributeAnimationInfos_.End(); ++i)
    {
        if (i->second_->Update(timeStep))
            finishedNames.Push(i->second_->GetAttributeInfo().name_); // ****** CRASH HERE
    }

    for (unsigned i = 0; i < finishedNames.Size(); ++i)
        SetAttributeAnimation(finishedNames[i], 0);
}[/code]

The debugger shows the Animatable "this" pointer is invalid at that point because Node::Remove() deletes the node as well (no references left). So, I added the ugly line above to keep it alive.

-------------------------

cadaver | 2017-01-02 01:14:57 UTC | #2

Thanks, look like definite bugs! The common pattern we use in UI code is to always check for sender existence after returning from the event, no doubt it's necessary here as well.

-------------------------

cadaver | 2017-01-02 01:14:57 UTC | #3

Fixes are in the master branch.

-------------------------

vudugun | 2017-01-02 01:14:57 UTC | #4

Thanks for the reply and the quick fixes!

In the meantime, I managed to crash in Material::HandleAttributeAnimationUpdate() as well, for the same reason as above (remove node at the end of material animation)

-------------------------

cadaver | 2017-01-02 01:14:57 UTC | #5

Should be fixed as well. In addition in my testing I found that material animation event could be erroneously transmitted on the first frame, which got fixed too.

-------------------------

