berrymooor | 2017-10-30 20:17:18 UTC | #1

Hi, can't find any example or tut about how to use event frames in AngelScript.
For example, if i need to execute some function after animation, logicaly it must be something like this:

     ValueAnimation@ animatePos = ValueAnimation();
     animatePos.SetKeyFrame (0.0f, Variant(Vector3(0.0f,0.0f,0.0f)));
     animatePos.SetKeyFrame (0.1f, Variant(Vector3(30.0f,30.0f,30.0f)));
     animatePos.SetKeyFrame (0.2f, Variant(Vector3(28.0f,40.0f,30.0f)));
     animatePos.SetEventFrame (0.3f, "AnimationEnd");
     node.SetAttributeAnimation("Position", animatePos,WM_ONCE);

    void AnimationEnd (StringHash eventType, VariantMap& eventData)
    {
        // some code
        }

but, this not work... please help)

-------------------------

orefkov | 2017-10-30 19:53:11 UTC | #2

Imho time of EventFrame must be less or equal last key frame in animation.
And you must subscribe for that event.

-------------------------

jmiller | 2017-11-05 19:37:38 UTC | #3

Perhaps subscribe to E_ATTRIBUTEANIMATIONREMOVED ?

  https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/SceneEvents.h

E_ATTRIBUTEANIMATIONUPDATE may be useful in other cases.

-------------------------

