rku | 2017-01-02 01:11:29 UTC | #1

My situation is this: i want to move object certain amount of distance and remove it from the world. Natural fit seems attribute animations. This is what i got:
[code]
<?xml version="1.0"?>
<objectanimation>
    <attributeanimation name="Position" interpolationmethod="Linear" wrapmode="Once" speed="1">
        <keyframe time="0" type="Vector3" value="0 0 0" />
        <keyframe time="1" type="Vector3" value="0 15 0" />
        <eventframe time="1" eventtype="1" />
    </attributeanimation>
</objectanimation>
[/code]
To see if animation is finished i decided to use "eventframe" (undocumented feature it seems).


Q1: Why eventtype is uint? ( [github.com/urho3d/Urho3D/blob/m ... n.cpp#L123](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/ValueAnimation.cpp#L123) ). It ends up converted to StringHash. Would it not be better to allow string types so they have more meaningful names? I could make PR changing it to string, but it is not backwards-compatible so need developer blessing on this one. Ofc it can be made backwards-compatible with ugly hack of converting numeric strings to integers before generating StringHash but its ugly.


Q2: Can we modify scene graph from "eventframe" event? I want to remove node from scene graph when animation is done.
[code]
animation->SubscribeToEvent(StringHash(1), URHO3D_HANDLER(MyObj, OnPickupAnimationEnd));
...
void MyObj::OnPickupAnimationEnd(StringHash eventType, VariantMap& eventData)
{
    node_->Remove();
}
[/code]
Thing is it causes crash somewhere within attribute animation code at a later time so i guess modifying scene graph is not permitted at that time. Still need clarification.


Q3: Is there a way to "queue" some events to certain step? So we can send events at any time and be sure they are executed during E_SCENEUPDATE step for example. I have not seen such functionality while checking out source code. Maybe this is worthy feature request? Or maybe there is another solution to this problem?

-------------------------

lizardperson | 2017-01-02 01:11:31 UTC | #2

I have a very similar question which fits the same topic, so I'll post it here, instead of creating another thread.

Q4: How can I add attribute animation at the handling of frame event?
I add position animation to the camera node and register event on the last frame. 
Then I put the same code which adds animation to the camera inside the event handler. It outputs the debug string ("TWEEN END"), but for some reason doesn't add the next animation to the camera node.
I tried to remove running animation first(the commented line), but it doesn't change anything and camera just stops after the first animation's end.  

[code]void HandleTweenEnd(StringHash eventType,VariantMap& eventData)
{
	 Log::Write(LOG_INFO,String("TWEEN END"));
	 //cameraNode_->RemoveAttributeAnimation("Position");
	 SharedPtr<ValueAnimation> positionAnimation(new ValueAnimation(context_));
	 positionAnimation->SetKeyFrame(0.0f, cameraNode_->GetPosition());
	 positionAnimation->SetKeyFrame(0.5f, cameraNode_->GetPosition() + cameraNode_->GetDirection() * 3);
	 positionAnimation->SetEventFrame(0.5f, "TweenEnd");
	 cameraNode_->SetAttributeAnimation("Position", positionAnimation, WM_ONCE);
}[/code]

-------------------------

Sir_Nate | 2017-01-02 01:11:31 UTC | #3

Regarding Q4, I would guess it does not do anything with the new animation because of how Animatable handles finished animations in updating them:
[code]void Animatable::UpdateAttributeAnimations(float timeStep)
{
    if (!animationEnabled_)
        return;

    Vector<String> finishedNames;
    for (HashMap<String, SharedPtr<AttributeAnimationInfo> >::ConstIterator i = attributeAnimationInfos_.Begin();
         i != attributeAnimationInfos_.End(); ++i)
    {
        if (i->second_->Update(timeStep))
            finishedNames.Push(i->second_->GetAttributeInfo().name_);
    }

    for (unsigned i = 0; i < finishedNames.Size(); ++i)
        SetAttributeAnimation(finishedNames[i], 0);
}[/code]
My guess would be that removing and adding the Position animation still marks the position animation as finished, and so it just ends up being removed (even though it is a new animation).

Regarding Q3, As far as I know there is not, though I don't think it's too hard to add. If the event sender is not important, you can just add an object that stores the events in a map<EventType, multimap<EventType, VariantMap>> and have it subscribe to the first event type, and when it receives that event send all of the events in the second container (a multimap is probably not the best solution -- perhaps a vector of pairs or something instead). If caller is important, you then need to store the caller as well, and ensure that the caller either still exists (i.e. store in SharedPtr<>) or handle the case that the caller is deleted. You then just have a QueueEvent(EventType sendon, EventType willSend, VariantMap data) that adds it to that container and subscribes to the sendon events, with a generic handler that will empty the map of those events, sending all of them with their willSend types, and unsubscribing from that eventtype.

As to Q2, the crashing is probably because you are removing the node that is in the middle of updating it's attribute animations, and removing it probably releases the last reference, causing it to be deleted while it is still executing a function (that later does stuff with this, which has been deleted). My suggestion would be to mark the object with a remove flag, and on the update event remove it. Alternatively, consider adding specific object that simply deletes all of it's children during the update event, and reparent the object to that node instead of removing it directly. As far as I know modifying the scene graph is allowed at this time. You simply aren't allowed to delete the object that is updating it's animations and causing that event to be called.

Regarding Q1, I assume it's for efficiency reasons involved in the size of StringHash vs String, and, more importantly, in the equality comparisons, though I'm not a developer and I'm not at all certain.

-------------------------

rku | 2017-01-02 01:11:33 UTC | #4

Thanks for clarifications Nate. Though i think you are mistaken regarding Q1. Thing is uint is converted to StringHash. If eventframe type was text string it would also be converted to string hash. There are no performance considerations here as it only makes difference when loading xml, and that happens really rare (relatively to other events).

-------------------------

lizardperson | 2017-01-02 01:11:33 UTC | #5

[quote="Sir Nate"]Regarding Q4[/quote]
Thanks! You're right, Nate, it sends event and then marks attribute animation as finished, even if it was reset inside event handler. 
I think, comparing pointer to ValueAnimation before and after the sending of event and making necessary adjustments could fix this behavior. 
I myself fixed it by marking the object first, resending event from the update and handling it from there. I'm writing the tweening interface class based on attribute animation functionality, so additional clutter is hidden inside the implementation.
For users who work with attribute animations directly, patch of this problem would be helpful, I believe, as chaining of animations can be very useful.

-------------------------

