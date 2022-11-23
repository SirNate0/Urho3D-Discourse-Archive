lexx | 2017-01-02 00:59:49 UTC | #1

Im trying to use multiple animations (I have Idle and Walk animations).
I create node, load model and material and then

[code]
	void LoadAnimation(String name)
	{
		ResourceCache* cache = GetSubsystem<ResourceCache>();
		Animation* animation = cache->GetResource<Animation>("Models/" + name + ".ani");
		assert(animation);
		AnimationState* state = model->AddAnimationState(animation);

		// The state would fail to create (return null) if the animation was not found
		if (state)
		{
			// Enable full blending weight and looping
			state->SetWeight(1.0f);
			state->SetLooped(true);
		}
	}
	void Update(int animNum, float timeStep)
	{
		if (model->GetNumAnimationStates())
		{
			AnimationState* state = model->GetAnimationStates()[animNum];
			state->AddTime(timeStep);
		}
	}

	.
	.
init():	
	mymodel.Load(blah);
	mymodel.LoadAnimation("idle.ani");
	mymodel.LoadAnimation("walk.ani");
	
update():
	mymodel.Update(0, dtime); // first anim doesnt work
	mymodel.Update(1, dtime); // last anim works
[/code]
If I dont load walk.ani, then idle animation works. Why?




PS. I just got animations working with
[code]
	void PlayAnimation(String name)
	{
		AnimationController *animCtrl = (AnimationController*) node->GetComponent("AnimationController");
		assert(animCtrl);
		animCtrl->PlayExclusive("Models/" + name + ".ani", 0, true, 0.5f);
	}
[/code]
but still like to know whats wrong with the first code?

-------------------------

kenji | 2018-02-12 20:06:07 UTC | #2

Beginner Web Code.
・§Androidアプリ入門編⑥☆Multiple 3D-Animation by UrhoSharp.Forms.
 http://yrpcity.dip.jp/strongbox/csherp/and025.html

・§Androidアプリ入門編①☆Lottie Animation Forms.
 http://yrpcity.dip.jp/strongbox/csherp/and012.html

・§Androidアプリ入門編②☆Drawing 3D-Shape by UrhoSharp.Forms.
  http://yrpcity.dip.jp/strongbox/csherp/and015.html

・§Androidアプリ入門編③☆xamarinのサンプル・3D-Cubeの棒グラフチャートを描く
  http://yrpcity.dip.jp/strongbox/csherp/and016.html

・§Androidアプリ入門編④☆3D-おでん串 by UrhoSharp.Forms.
  http://yrpcity.dip.jp/strongbox/csherp/and021.html

・§Androidアプリ入門編⑤☆Drawing 3D-Animation by UrhoSharp.Forms.
 http://yrpcity.dip.jp/strongbox/csherp/and023.html

-------------------------

weitjong | 2018-02-12 20:12:04 UTC | #3

I approved to let this one pass for now. For some reason it stuck in “need approval” list. Let me know if it’s a bad decision.

-------------------------

lexx | 2018-02-24 11:23:24 UTC | #5

Years ago I didnt know how animation blending works, but it is like you cant have more animation than 1.0, so blend them yourself 0.0 -> 1.0  both of them. Middle of the both is setting both to 0.5.

Like this (in C#):
https://pastebin.com/37ySueqG
https://pastebin.com/QSiRdxLy

-------------------------

