codingmonkey | 2017-01-02 01:01:22 UTC | #1

Hi, folks!)
I create some like a boom fx, and when i turn away from it, and i turn to it again - boom fx have something like a lag or phase shift in animation.
Why is this happening? and how to solve this?

[video]http://youtu.be/vrf38AYw1qM[/video]

this my code for animation if it needed
[code]
void ScriptBoom::Start()
{
	ResourceCache* cache = GetSubsystem<ResourceCache>(); 
	material_ = cache->GetResource<Material>("Materials/MT_Boom.xml");
	
	ringNode_ = GetNode()->GetChild("boomRing",true);
	
	// AlphaMask Factor
	factorAnim_ = SharedPtr<ValueAnimation>(new ValueAnimation(context_));
	
	//srand(0);
	float noise = Random(0.1f, 0.5f);
	float lag = Random(-0.5f, 0.5f);

	factorAnim_->SetKeyFrame(0.0f, 0.5f);
	factorAnim_->SetKeyFrame(0.5f, 1.3f);
	factorAnim_->SetKeyFrame(1.0f, 2.0f);
	
	material_->SetShaderParameterAnimation("Factor", factorAnim_);
	
	// Scale
	scaleAnim_ = SharedPtr<ValueAnimation>(new ValueAnimation(context_));
	

	float startSize = 0.1f;
	float endSize = 8.0f;
	
	scaleAnim_->SetKeyFrame(0.0f, Vector3(startSize, startSize, startSize));
	scaleAnim_->SetKeyFrame(0.5f, Vector3(endSize, endSize, endSize));
	scaleAnim_->SetKeyFrame(1.0f, Vector3(startSize, startSize, startSize));
	
	GetNode()->SetScale(startSize);

	GetNode()->SetAttributeAnimation("Scale", scaleAnim_, WM_LOOP);
	


	//light
	light_ = GetNode()->GetComponent<Light>();
	lightAnim_ =  SharedPtr<ValueAnimation>(new ValueAnimation(context_));
	
	lightAnim_->SetKeyFrame(0.0f, 0.0f);
	lightAnim_->SetKeyFrame(0.5f, 10.0f);
	lightAnim_->SetKeyFrame(1.0f, 0.0f);

	light_->SetAttributeAnimation("Brightness Multiplier", lightAnim_);

	// ring
	ringMaterial_ =  cache->GetResource<Material>("Materials/MT_BoomRing.xml");
	ringAlphaAnim_ =  SharedPtr<ValueAnimation>(new ValueAnimation(context_));

	ringAlphaAnim_->SetKeyFrame(0.0f, Vector4(1.0f,1.0f,1.0f,0.0f));
	ringAlphaAnim_->SetKeyFrame(0.5f, Vector4(1.0f,1.0f,1.0f,2.0f));
	ringAlphaAnim_->SetKeyFrame(0.7f, Vector4(1.0f,1.0f,1.0f,0.5f));
	ringAlphaAnim_->SetKeyFrame(1.0f, Vector4(1.0f,1.0f,1.0f,0.0f));

	ringMaterial_->SetShaderParameterAnimation("MatDiffColor", ringAlphaAnim_);
}
[/code]

-------------------------

cadaver | 2017-01-02 01:01:22 UTC | #2

The problem may be the following: ValueAnimations update always, regardless of visibility. But AnimatedModel and ParticleSystem animations by default do not update (I don't know from your post which one you are using for the effect's main geometry) when not visible, to optimize CPU usage.

You should be able to call SetUpdateInvisible(true) in the geometry component and hopefully this fixes the phase shift issue.

-------------------------

codingmonkey | 2017-01-02 01:01:23 UTC | #3

[quote]I don't know from your post which one you are using for the effect's main geometry[/quote]

Boom Fx has only two StaticModel, first is an - isosphere ( with my custom render tech: DiffAlphaMaskWithFactor for mask animation ) and second model have bit of planes for white alpha rings (with std tech: DiffUnlitAlpha).
[url=http://savepic.ru/6296021.htm][img]http://savepic.ru/6296021m.png[/img][/url]
[url=http://savepic.org/6473439.htm][img]http://savepic.org/6473439m.png[/img][/url]
[url=http://savepic.org/6473436.htm][img]http://savepic.org/6473436m.png[/img][/url]

And root node of this boomfx only change his scale on time by valueAnimation. 
GetNode()->SetScale(startSize);

Two materials have own valueAnimations;

-------------------------

cadaver | 2017-01-02 01:01:23 UTC | #4

Looked at the code more precisely and turned out that material shader parameter animations are only being updated when they have visible batches on the screen, while component attribute animations are being updated whenever the scene is being updated. So I was being wrong.

This is a bit nasty issue to solve properly, because materials do not belong to a scene, while components do. And we'd want the animation update to be dependant on the scene update timestep, and not just the whole engine's frame update.

-------------------------

codingmonkey | 2017-01-02 01:01:23 UTC | #5

Do I understand correctly that this is a problem of materials which are constantly animated and do not depend on visibility. 
While the animation model(node) depends on visibility. Therefore, there is an offset between these animations.

-------------------------

cadaver | 2017-01-02 01:01:23 UTC | #6

The other way around: material shader parameter animations currently depend on visibility. Attribute animations (in nodes and components) don't depend on visibility, but update always.

-------------------------

cadaver | 2017-01-02 01:01:23 UTC | #7

The dependency on visibility should now be fixed in master branch. You can optionally assign a scene to the material to make it follow the scene's update events (respecting the timescale) instead of global updates.

-------------------------

codingmonkey | 2017-01-02 01:01:23 UTC | #8

Thanks, I'll try this.

-------------------------

codingmonkey | 2017-01-02 01:01:23 UTC | #9

Yeah, now it's work better )
[video]http://youtu.be/xIOyBnPS9Pw[/video]
Thanks, [b]cadaver[/b].

-------------------------

