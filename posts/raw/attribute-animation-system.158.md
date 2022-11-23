aster2013 | 2017-01-02 00:58:30 UTC | #1

Hi, all

I have created a new branch (animation) for attribute animation system. In the system, all attribute in an Animatable object(Node, Scene, Component, UIElement) can be animated.
For example, we can apply an animation to light's color attribute like this:
[code]
    Node* lightNode = scene_->CreateChild("DirectionalLight");
    lightNode->SetDirection(Vector3(0.6f, -1.0f, 0.8f)); // The direction vector does not need to be normalized
    Light* light = lightNode->CreateComponent<Light>();
    light->SetLightType(LIGHT_DIRECTIONAL);

    /// Create light color animation
    SharedPtr<AttributeAnimation> colorAnimation(new AttributeAnimation(context_));
    colorAnimation->SetValueType(VAR_COLOR);
    colorAnimation->AddKeyFrame(0.0f, Color::WHITE);
    colorAnimation->AddKeyFrame(1.0f, Color::RED);
    colorAnimation->AddKeyFrame(2.0f, Color::GREEN);
    colorAnimation->AddKeyFrame(3.0f, Color::WHITE);
    light->SetAttributeAnimation("Color", colorAnimation);[/code]

This is a simple usage for attribute system. 
Also we can create an animation file, it include all animation for a scene, it can be loaded and apply a scene. 

Current the animation system is beginning, If you have good idea on it, please tell us. thank you.

-------------------------

szamq | 2017-01-02 00:58:30 UTC | #2

I like the idea. One thing that would be nice to have is to choose time(or event) which determines the change. I'm talking here specifically about variable timestep when rendering and fixed timestep driven by physics. The second one is important to make the animation deterministic. I can imagine animating position of the node with collision shape and rigidbody(something like elevator) and it would have the same positions over the time when using fixed time. Using variable timestep could cause some unexpected results, let's say there is 1 sec lag or whatever and then the animating body would be teleported away a large distance (causing the player fall from the elevator).

Edit: checked the branch and i see that E_SCENEPOSTUPDATE is used, which is variable timestep. What I would suggest is to create boolean flag like "Fixed Timestep" to subscribe to E_PHYSICSPRESTEP or E_PHYSICSPOSTSTEP

-------------------------

friesencr | 2017-01-02 00:58:30 UTC | #3

Thanks for working on this Aster.  I am definitely in need of something like this.  I was sort of resigning myself to completely scripted cut scenes but this could really make a big difference.  It looks like you have thought through the portability and storage.

Suggestions:

Easings [learningthreejs.com/data/tweenjs ... ation.html](http://learningthreejs.com/data/tweenjs_for_smooth_animation/tweenjs_for_smooth_animation.html)
Start / End events for when the animation has started / finished
A manual update method could be made where they pass in a number to incremement the animation.  This could be used in fixed update / scene update  or  whatever.  This would allow easy pausing.
A cancel method to immediately terminate and set to the initial value.
A finish method to immediately terminate and set to the final value.

I haven't been able to figure out how it handles the current value of the attribute.  If the animation starts will it jump to the first keyframe or will it use the current attribute value.  However it handles that there will likely be an fair split of times you will want it to handle it different ways.  Its something to think about.

-------------------------

Mike | 2017-01-02 00:58:30 UTC | #4

Another great contribution, thanks Aster  :wink: 
This opens new interesting possibilities for animating cameras, elevators, doors, controlling morphs, building trailers...

-------------------------

boberfly | 2017-01-02 00:58:34 UTC | #5

Awesome!

I'm thinking not only animation but adding things like expression syntax, different kinds of lerps or direct connections from other compatible attributes as well. Can an animation attribute have weighting? Things like (in Maya terms) driver driven keys could be used where a complex animation scheme could be driven by a handful of other keys eg. if you had a skeleton for a character and some bones have keyframes, have secondary bones which are driven by those primary bones at certain angles (so if bone1 rotates by 75 degrees in Y, move bone2 by 10 units in X). I worked on a AAA title doing art and character stuff ages ago, and we exported driver/driven keys into XML which defined this kind of data and the game engine would do the linking, very handy.

[youtube.com/watch?v=myZcUvU8YWc#t=800](https://www.youtube.com/watch?v=myZcUvU8YWc#t=800) )

Cheers!

-------------------------

aster2013 | 2017-01-02 00:58:48 UTC | #6

the first version of Attribute animation system has finished, please check out it.
thanks.

-------------------------

