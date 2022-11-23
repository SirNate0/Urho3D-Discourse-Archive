rogerdv | 2017-01-02 01:01:52 UTC | #1

Is there some way to animate lights, to simulate fire lighting?

-------------------------

codingmonkey | 2017-01-02 01:01:53 UTC | #2

that do you mean then talk about light anim ? 

if it not about animated textures, you may do something like this:

for example for my boom fx i'm animate brightness of light

[code]
	//light
	light_ = GetNode()->GetComponent<Light>();
	
	lightAnim_ =  SharedPtr<ValueAnimation>(new ValueAnimation(context_));
	
	lightAnim_->SetKeyFrame(0.0f, 0.0f); // 0 sec
	lightAnim_->SetKeyFrame(0.5f, 10.0f); 
	lightAnim_->SetKeyFrame(1.0f, 0.0f); // 1 sec

	light_->SetAttributeAnimation("Brightness Multiplier", lightAnim_);
[/code]

mb also may animate - "range" from low->max->low...

i don't know color of the light also animated or not.

-------------------------

rogerdv | 2017-01-02 01:01:53 UTC | #3

Cant remember if was in Torque3D or Unity3D editor, but there was a parameter that allowed to animate a light, specifically the one I used was Fire. The resulting light behaved like fire, randomly chaging intensity, I think that also the casted shadows shifted position, like the real fire light does.

-------------------------

codingmonkey | 2017-01-02 01:01:53 UTC | #4

mb you need particles + light range/bright animation + customize texures of particles for flame like textures.
[url=http://savepic.su/4543952.htm][img]http://savepic.su/4543952m.png[/img][/url]

-------------------------

rogerdv | 2017-01-02 01:01:53 UTC | #5

Yes, but particles cant be saved yet, unless I missed some commmit that enbales serialization for it.

-------------------------

Azalrion | 2017-01-02 01:01:59 UTC | #6

You could write an ValueAnimation that sets it to varying intensities at varying timeframes. Not that easy to randomize values though, you'd have to either have a suitable long time frame and loop or recreate after its finished.

-------------------------

rogerdv | 2017-01-02 01:02:01 UTC | #7

Damn, Ill have to postpone that until I know more Urho3D and graphics programming.

-------------------------

JTippetts | 2017-01-02 01:02:01 UTC | #8

It's in the documentation. In fact, the entry on [url=http://urho3d.github.io/documentation/1.32/_attribute_animation.html]attribute animation[/url] specifically includes an example for animating the position and color of a light using object animation.

-------------------------

