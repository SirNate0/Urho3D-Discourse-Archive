GodMan | 2020-02-10 02:33:53 UTC | #1

I am trying to add an upper body animation to my character while he is running. The upper body animation only contains animation data for the torso and up. The characters pelvis and down should keep playing the running animation. I have been able to get it to play fine but my running animation does not seem to play correctly. The characters legs seem like they are barely moving. 

Code: 	
	
    Animation* combat_sword_idle = cache->GetResource<Animation>("Models/combat_sword_move_front.ani");
    		Animation* combat_sword_melee2 = cache->GetResource<Animation>("Models/combat_sword_melee2.ani");

        		state = modelObject2->AddAnimationState(combat_sword_idle);
        		state->SetWeight(1.0f);
        		state->SetLooped(true);

        		state2 = modelObject2->AddAnimationState(combat_sword_melee2);
        		state2->SetWeight(0.5f);
        		state2->SetLooped(true);

-------------------------

Modanung | 2020-02-10 11:26:45 UTC | #2

Try setting the _start bone_ for the upper body animation to being one of the spine bones through the `AnimationController`, so it leaves the legs unaffected.

-------------------------

GodMan | 2020-02-10 04:02:22 UTC | #3

Here is the code if anyone wants to know in the future. @Modanung Thanks man. 

    		Animation* combat_sword_idle = cache->GetResource<Animation>("Models/combat_sword_move_front.ani");
    		Animation* combat_sword_melee2 = cache->GetResource<Animation>("Models/combat_sword_melee2.ani");

    		Bone* root = modelObject2->GetSkeleton().GetBone("spine");

    		state = modelObject2->AddAnimationState(combat_sword_idle);
    		state->SetWeight(1.0f);
    		state->SetLooped(true);

    		state2 = modelObject2->AddAnimationState(combat_sword_melee2);
    		state2->SetWeight(0.5f);
    		state2->SetLooped(true);
    		state2->SetStartBone(root);

-------------------------

