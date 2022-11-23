sabotage3d | 2017-01-02 01:07:35 UTC | #1

Hi guys,
I am building a simple FSM and I wonder what would be the best approach to make a transition between the states coupling it with Urho3D's animation system. At the moment I am switching the states like jump, run and idle. But I am not sure what would be the best approach to blend between them.

-------------------------

cadaver | 2017-01-02 01:07:35 UTC | #2

You probably can start with the AnimationController component and call its PlayExclusive function on state transitions. This starts fading in an animation within a certain time interval, and fades out all other animations on the same blending layer with the same interval, achieving a crossfade. That's what NinjaSnowWar is doing.

-------------------------

sabotage3d | 2017-01-02 01:07:36 UTC | #3

Thanks cadaver. I am not entirely sure where to we feed the transition. I have Jump -> transition -> Run , what format do I need the transition to blend between the two. I am already using the PlayExclusive inside the states.

-------------------------

magic.lixin | 2017-01-02 01:07:36 UTC | #4

class Transition
  {
       float duration;
       String name;
       State@ fromState;
       State@ toState;
  };
  
  class State 
  { 
    String animationName;
    bool   looped;
     
     void OnEnter(Transition@ t)
    {
       PlayExclusive(animationName, 0, looped, t.duration);
    }

  };

  If you mean transition animation, that will be a another state.

-------------------------

sabotage3d | 2017-01-02 01:07:36 UTC | #5

I mean blending between the two animations. Is there a specific method for that or it does it autoamtically when we use PlayExclusive? Like blending all the bones with quaternion from one animation to another for smooth transition.

-------------------------

cadaver | 2017-01-02 01:07:36 UTC | #6

The blending is controlled by the individual AnimationStates' weights. AnimationController animates these in a crossfade-like manner when you call PlayExclusive. You could also control them manually if you wanted, but in that case you shouldn't use AnimationController at all, as manual control and AnimationController will conflict.

Also, to play an animation on a skeleton partially (for example a shooting or aiming animation only in the upper body, while the lower body runs or walks), you can also control AnimationState weights per-bone, or use the startbone parameter to pick a specific bone as a startpoint in the hierarchy for applying the animation.

-------------------------

sabotage3d | 2017-01-02 01:07:36 UTC | #7

Thanks a lot cadaver, it makes sense now.

-------------------------

