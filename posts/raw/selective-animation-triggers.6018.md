GodMan | 2020-03-27 10:55:50 UTC | #1

So let me explain this to be clear. Lets say I have an effect that is created when the npc does a melee attack. However I don't wont this to be triggered by every animation that may have a trigger like footstep sounds. 

So if I have a method that creates this effect in the animation trigger method. How do I keep it from always being triggered by any animation trigger event. 

If this makes sense.

-------------------------

Dave82 | 2020-03-27 08:41:46 UTC | #2

Animation trigger event has a "Name" element that probably contains the name of the animation. Also you can Use "Data" element that you can set what ever you want

-------------------------

GodMan | 2020-03-27 18:14:43 UTC | #3

Okay. Thanks.

So your saying I can check to see what the animation is in perhaps a conditional.

-------------------------

jmiller | 2020-03-28 19:58:08 UTC | #4

The [skeletal animation](https://urho3d.github.io/documentation/HEAD/_skeletal_animation.html) section could perhaps use a small illustration.

Blender exporter sets the trigger data to a String value of the bone name, but I suppose one can use whatever Variant they want; e.g., optimize by using integers or converting the Strings to indices at runtime.

*(edit)* Event:
```
URHO3D_EVENT(E_ANIMATIONTRIGGER, AnimationTrigger)
{
    URHO3D_PARAM(P_NODE, Node);                    // Node pointer
    URHO3D_PARAM(P_ANIMATION, Animation);          // Animation pointer
    URHO3D_PARAM(P_NAME, Name);                    // String
    URHO3D_PARAM(P_TIME, Time);                    // Float
    URHO3D_PARAM(P_DATA, Data);                    // User-defined data type
}
```

Models/run.xml
```
<animation>
  <trigger normalizedtime="0.2" type="String" value="leg left ankle" />
  <trigger normalizedtime="0.7" type="String" value="leg right ankle" />
</animation>
```

```
OnAnimationTrigger(StringHash eventType, VariantMap& eventData) {
  const String& animStateName(eventData[AnimationTrigger::P_NAME].GetString());
  const String& boneName(eventData[AnimationTrigger::P_DATA].GetString());
...
```

-------------------------

GodMan | 2020-03-28 04:48:14 UTC | #5

@jmiller Thanks that's pretty detailed.

-------------------------

GodMan | 2020-03-28 20:01:52 UTC | #6

Okay so for anyone in the future this is what I did:

Code: 

    void AIMelee::HandleAnimationTriggerZombie(StringHash eventType, VariantMap& eventData)
    {
    	using namespace AnimationTrigger;
    	AnimatedModel* model = node_->GetComponent<AnimatedModel>();
    	if (model)
    	{
    		AnimationState* state = model->GetAnimationState(eventData[P_NAME].GetString());

    		if (eventData[P_NAME].GetString() == "SOME_NAME_HERE")
    		{
    			// Do shit here
    		}
    		if (state == NULL)
    		{
    			return;

    		}

    		bone = node_->GetChild(eventData[P_DATA].GetString(), true);



    		if (bone != NULL)
    		{
                    // do something here
    		}

    	}

    }

What I did was opened the animation file. At the top AssetImporter puts the default string Take 001, you can change this to a custom name, and then use a conditional like above to check if that animation is the one that has the animation trigger.

-------------------------

