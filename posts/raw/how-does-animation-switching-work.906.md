vivienneanthony | 2017-01-02 01:04:00 UTC | #1

Hello,

I am able to do animation but the problem I have is switching. If I use PlayExclusive. It tends to lose the animation and if I use Play the animation doesn't repeat I thought maybe it is the weight but it's not the case. I seems maybe I have the animations on the same layer and Urho3D might be getting confused.

I'm not sure.

Vivienne




[code]
 AnimatedModel* objectNodemodel=objectNode->CreateComponent<AnimatedModel>();

    /// Add Animation Controller
    objectNode->CreateComponent<AnimationController>();

    /// Setup mesh and mesh details nodes and stactic models
    if(gender<51)
    {
           ///       Code for character 


        /// Add animation state
        Animation * IdleAnimation = new Animation(context_);
        IdleAnimation = cache->GetResource<Animation>("Resources/Models/standardbipedolianfemaleIdleAction.ani");

        objectNodemodel -> AddAnimationState(IdleAnimation);
        IdleAnimation -> SetAnimationName ("IdleAnimation");

        /// Add Walking Animation
        Animation * AddAnimation = new Animation(context_);
        AddAnimation = cache->GetResource<Animation>("Resources/Models/standardbipedolianFemaleWalkAction.ani");

        objectNodemodel -> AddAnimationState(AddAnimation);
        AddAnimation -> SetAnimationName ("WalkAnimation");

        /// Get Controller
        AnimationController * playermeshAnimationController1 = objectNode -> GetComponent<AnimationController>();

        /// Set Morph Weight
        playermeshAnimationController1-> SetWeight("IdleAnimation",1);
        playermeshAnimationController1-> SetTime("IdleAnimation",1.89753);

        playermeshAnimationController1-> SetWeight("WalkAnimation",1);
        playermeshAnimationController1-> SetTime("WalkAnimation",2.45833);

        playermeshAnimationController1->Play("IdleAnimation",0,1,0);[/code]


Code in FixedUpdate

[code]    // Movement in four directions
    if (controls_.IsDown(CTRL_FORWARD|CTRL_BACK|CTRL_LEFT|CTRL_RIGHT))
    {

      /// code for controls

        /// If in air, allow control, but slower than when on ground
        body->ApplyImpulse(rot * moveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE));

        animCtrl -> StopAll();

        animCtrl -> PlayExclusive("WalkAnimation", 0, true, 0);
    }
    else
    {

        if(softGrounded)
        {
            if(!animCtrl->IsPlaying("IdleAnimation"))
            {
                animCtrl -> PlayExclusive("IdleAnimation", 0, true, 0);
            }
        }
    }[/code]

-------------------------

codingmonkey | 2017-01-02 01:04:01 UTC | #2

i'm do not use the AnimationController yet
but i guess that the play function need full path to ani file [urho3d.github.io/documentation/1 ... oller.html](http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_animation_controller.html)

PlayExclusive
[quote]Play an animation, set full target weight and fade out all other animations on the same layer. Name must be the full resource name. Return true on success. [/quote]

for anim states (i usually use they with own FSM construction):
set to IdleAnimation state lower priority layer (0). SetWeight(1.0f) - always. prevState = CharacterState and now CharacterState = IDLE
set to walkAnimation state high priority layer(1)  0+1. SetWeight(1.0f) - only then you press WASD buttons(or you also may add fadeWeight for few sec).  prevState =  CharacterState and now CharacterState  = WALK

in update (timeStep) 
{
//STAGE1. clear prev states
if (preState == WALK) 
{
  walkAnimation. SetWeight(0);
  walkAnimation.SetTime(0.0f);
}
else if (preState == IDLE) 
{
  // do not needed to reset anything this state are default for play
}
else if (...)
{

}
...

//STAGE2. anim current selected state
if ( CharacterState == IDLE) 
{
   IdleAnimation. SetWeight(1.0f);
   IdleAnimation.AddTime(timeStep);
}
else if (CharacterState == WALK) 
{
  walkAnimation. SetWeight(1.0f);
  walkAnimation.AddTime(timeStep);
}
...
more complex example how i switch animStates 
[github.com/MonkeyFirst/FH/blob/ ... BigBot.cpp](https://github.com/MonkeyFirst/FH/blob/master/Featheredhat/BigBot.cpp)

-------------------------

Mike | 2017-01-02 01:04:01 UTC | #3

Maybe you should use a fadeTime different than zero and not use weights.

-------------------------

vivienneanthony | 2017-01-02 01:04:05 UTC | #4

[quote="codingmonkey"]i'm do not use the AnimationController yet
but i guess that the play function need full path to ani file [urho3d.github.io/documentation/1 ... oller.html](http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_animation_controller.html)
[/quote]

I went to the state changing method directly. I tried AnimationController but once that I read that it deletes animations. It couldn't be used because I preload the animations with the character.

Unless there was a flag or function to tell AnimationController not to delete I'll do the animation switching directly. Maybe copy AnimationController and modify so it was it doesn't delete preloaded animations to make life easier. 

I updated Git with the rough animations added.

-------------------------

