codingmonkey | 2017-01-02 01:07:33 UTC | #1

Hi folks )
I try to figure out with some kind of cutscenes tech
for this reason I create animation in blender for camera movement: targetBone , cameraBone, ect... this all works fine.
also I wrote additional script for export camera specific parameters (shift xy, fov, zoom, clip) from blender into ObjectAnimation.xml file.
the length of both animations(skinned and object) is the same, around 9 sec.

And for now I need to find way to sync both. Actually I want to synchronize object animation into AnimationModel
I mean if Animation model has time is (7.3s) then object animation set the same time.
How this may be done? 

Is it possible to add some kind of method - ObjectAnimation->SetParentAnimation( AnimatedModel ) ?

-------------------------

cadaver | 2017-01-02 01:07:33 UTC | #2

Had to look up the API and the ObjectAnimation simply updates itself forward when set, which isn't sufficient for scenarios like this. The manual time positioning as in the issue [github.com/urho3d/Urho3D/issues/926](https://github.com/urho3d/Urho3D/issues/926) shouldn't be hard to do.

-------------------------

codingmonkey | 2017-01-02 01:07:33 UTC | #3

>The manual time positioning as in the issue [github.com/urho3d/Urho3D/issues/926](https://github.com/urho3d/Urho3D/issues/926) shouldn't be hard to do.
I think the switching ObjectAnimation and ValueAnimation into manual mode time control it's better then this - ObjectAnimation->SetParentAnimation( AnimatedModel )
because this code do the same sync, but in low-level manner
[code]  void HandleUpdate(StringHash eventType, VariantMap& eventData)
  {
    using namespace Update;
    float timeStep = eventData[P_TIMESTEP].GetFloat();
    if (am) 
    {
      animationState->AddTime(timeStep);
      objectAnimation->SetTime(animationState->GetTime());
    }
  } [/code] 

and one another question: Is it possible to use ValueAnimation / ObjectAnimation for long time objects animation (10-30 sec) ? if we will be saying in performance terms, it have the same performance as skinned animation ?

> updates itself forward when set
I guessing it may do not do this "update forward" if flag manualUpdate_ = true are present. 
[code]
bool ValueAnimationInfo::Update(float timeStep)
{
  if (!animation_ || !target_)
        return true;

  if (!manualUpdate_)
    currentTime_ += timeStep * speed_;
[/code]

And in this case OA/VA continue to use currentTime_. 
The value currentTime_ we may change manually with - SetTime(float time) as we wish.

-------------------------

cadaver | 2017-01-02 01:07:34 UTC | #4

Performance per track is roughly similar to skeletal animation, it advances in a list of keyframes and interpolates between the adjacent keyframes. However object animations like camera movement typically has a lot less separate tracks than skeletal animations (which have track per bone, and can have easily e.g. 20+ bones). Have to check the object animation code, if it's nicely written and caches the last keyframe it has advanced to, animation length shouldn't be a factor in performance.

Yes, when manual time control is desired it shouldn't update automatically. I'll meditate on whether I'll add SetAutoUpdate(false) or SetManualUpdate(true) but the end result is roughly same.

-------------------------

codingmonkey | 2017-01-02 01:07:35 UTC | #5

>However object animations like camera movement typically has a lot less separate tracks than skeletal animations
Actually i use skeletal animation for camera movements ) and ObjectAnimation only for camera parameters animation.
That's why I needed this sync between skinned animation and OA. 
I think it more easily for me use bones for camera movement and orientation with cooperate in OA for animate camera parameters.
I just try figure out with cutscenes making, and may be in future I do this in other  way.



I also want to mention few things, that i think probably also needed to introduce to engine in future:
[spoiler]1. Introduce supporting for animate RenderPath parameters, with helps OA or VA for animate such things as: tags enabling/disabling, values parameters animation...
2. TimeLine component, for adjusting time of few various animated objects(group) at once.

TimeLine* tm1 = new TimeLine(context_)

AnimationState->SetTimeLine(tm1)
ObjectAnimation->SetTimeLine(tm1)
ValueAnimation->SetTimeLine(tm1)
...
n - animated components

tm1->SetTime(time);
tm1->AddTime(time);
tm1->Pause(true/false);
tm1->PlayingDirection(forward/backward)[/spoiler]

-------------------------

Mike | 2017-01-02 01:07:35 UTC | #6

I've noticed that object and value animation don't account for each segment length (distance between 2 keyframes) to adjust a constant speed, so a long segment is super fast to travel and a short segment is slow.

-------------------------

codingmonkey | 2017-01-02 01:07:35 UTC | #7

i'm testing my previous stuff for cutscene after this new changes (PR) into master and do not find "fast traveling" effect, I guess it works fine now. 
but i'm do just visual compare between in-engine animation and blender viewport animation and it looks at first sight as the same.

or you mean something else ?

-------------------------

Mike | 2017-01-02 01:07:35 UTC | #8

Sorry, I simply forgot to 'time' my keyframes not evenly, I'm using Inkscape to build my anims.

-------------------------

codingmonkey | 2017-08-29 16:05:10 UTC | #9

today I finish to create primitive cutscene. 
Basically it based on Hellblade video intro, with few my own changes for simplify, because i'm not very good animator :slight_smile:
https://www.youtube.com/watch?v=q93mKx8F5xA
But actually in this animation I do not use OA or VA yet. 
I think it will be second pass with adding - camera specific animation parameters.

-------------------------

