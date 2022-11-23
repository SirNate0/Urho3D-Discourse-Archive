sabotage3d | 2017-03-16 22:11:12 UTC | #1

I have multiple ParticleEmitter2D and their blend mode is BLEND_ALPHA. When I draw them on top of each other one is always on top. Is there any way to control this? Also is there a way to have them all at the same blending mode without obeying any blending order per particle emitter?

-------------------------

sabotage3d | 2017-03-18 00:16:19 UTC | #2

For example if we the code below particleEmitter2 would be always on top of particleEmitter1. Is ther a way to combine these batches or to choose the order?

    ParticleEffect2D* particleEffect1 = cache->GetResource<ParticleFX>("Urho2D/sun.pex");
    particleEffect1->SetStartColor(Color::RED);

    ParticleEffect2D* particleEffect2 = cache->GetResource<ParticleFX>("Urho2D/greenspiral.pex");
    particleEffect2->SetStartColor(Color::YELLOW);

    SharedPtr<Node> particleNode1 = scene_->CreateChild("ParticleEmitter1");
    ParticleEmitter2D* particleEmitter1 = particleNode_->CreateComponent<ParticleEmitter2D>();
    particleEmitter1->SetEffect(particleEffect1);

    SharedPtr<Node> particleNode2 = scene_->CreateChild("ParticleEmitter2");
    ParticleEmitter2D* particleEmitter2 = particleNode_->CreateComponent<ParticleEmitter2D>();
    particleEmitter2->SetEffect(particleEffect2);

-------------------------

Modanung | 2017-03-18 01:21:26 UTC | #3

Would it hurt to use a 3D particle emitter?

-------------------------

sabotage3d | 2017-03-18 18:00:59 UTC | #4

But I am using it for 2D game and I got used to this pex format. Any ideas on how to sort the batches or combine them in one batch from two emitters?

-------------------------

Modanung | 2017-05-27 05:11:20 UTC | #5

Other than adding depth? Nope; no idea.

-------------------------

sabotage3d | 2017-04-01 23:48:25 UTC | #6

I still cannot figure out how BLEND_ADDALPHA and BLEND_ALPHA blend modes are working. This is the line where the blending mode is set:
`sourceBatches_[0].material_ = renderer_->GetMaterial(sprite_->GetTexture(), blendMode_);`
Is there any place where I can set that BLEND_ADDALPHA should work between different batches?

-------------------------

sabotage3d | 2017-05-26 23:23:05 UTC | #7

Is there a way to set the transparency sorting manually? Per polygon or per component?

-------------------------

