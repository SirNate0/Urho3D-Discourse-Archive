vivienneanthony | 2017-07-17 12:24:33 UTC | #1

Hello

I'm trying to export a character but it's taking way to long. If I export the Skeleton and Animations my CPU goes to 70% and even after a half hour it's trying to process. If I do the model and the rush it takes second. It's even weirder because I took another model from Makehuman to Blender to Urho3D and the exporter has no problem exporting the animation, character, skeleton, and mesh.

[dropbox.com/s/02hz1fb2as1qs ... blend?dl=0](https://www.dropbox.com/s/02hz1fb2as1qsld/CharacterRiggedAllRaceFactions.blend?dl=0)

Alice2 - Works fine
[dropbox.com/s/zn6ukjwnmendw ... blend?dl=0](https://www.dropbox.com/s/zn6ukjwnmendw1t/alice2.blend?dl=0)

Any ideas what's wrong?

Vivienne

-------------------------

TikariSakari | 2017-01-02 01:03:56 UTC | #2

Well I didn't open them, only clicked the link and your alice is 4 MB file, your other file is 69MB. If we assume most of the data in Alice blend is textures, and the human from make human has as much as 10MB of textures, 60MB for vertex data is quite a lot.

Edit: I did quickly check out of the blend file and most of the characters had over 100k faces, which is quite a high number for a game, maybe they weren't the meshes you were planning on using though.  I also checked alice, the alice has bit under 20k faces and only 3 submeshes, where as some of the models on your other file has over 10 sub meshes.

So my best bet would be the high amount of data per model would cause some hiccups when exporting. Also I noticed that it required some python file to load the huge blend file. The file is called rig_ui.py, I have no idea what it does though and I just simply pressed ignore.

-------------------------

vivienneanthony | 2017-01-02 01:03:56 UTC | #3

[quote="TikariSakari"]Well I didn't open them, only clicked the link and your alice is 4 MB file, your other file is 69MB. If we assume most of the data in Alice blend is textures, and the human from make human has as much as 10MB of textures, 60MB for vertex data is quite a lot.

Edit: I did quickly check out of the blend file and most of the characters had over 100k faces, which is quite a high number for a game, maybe they weren't the meshes you were planning on using though.  I also checked alice, the alice has bit under 20k faces and only 3 submeshes, where as some of the models on your other file has over 10 sub meshes.

So my best bet would be the high amount of data per model would cause some hiccups when exporting. Also I noticed that it required some python file to load the huge blend file. The file is called rig_ui.py, I have no idea what it does though and I just simply pressed ignore.[/quote]

So you thinking maybe that's the cause of it. The bigger one has about 2x4 about 8 characters and clothing. I can reduce the mesh vertix some but it a combined .blend file. Hence the bigger file size

Each mesh face is about 13k(13,378) faces with 13380 Vertices. So even a single mesh without clothing with animation export should be fine. If I disable the modifier it evens   go down to 7k and still the same problem.

-------------------------

vivienneanthony | 2017-01-02 01:03:56 UTC | #4

This is 20 minutes after hitting export of animation ([imgur.com/JZ4LxHP](http://imgur.com/JZ4LxHP))

Which is weird considering I deleted most vertices so there shouldn't be much left to calculate.

-------------------------

TikariSakari | 2017-01-02 01:03:57 UTC | #5

Did you try to export animations without models, or just use one model to get the animation file out? As for the face count, it does indeed seem that the face count is a lot lower than what I first saw it be. The structure of the models was just quite confusing when I quickly glanced it through.

What I mean is, you can use same animation for all the models under one armature, or at least I think you should be able to. As long as they all have the same groups assosiated with the animation file. Like if I have a model and then outfit model, I only need to export the animation from one of the models, since they both are parented to same armature.

-------------------------

vivienneanthony | 2017-01-02 01:03:57 UTC | #6

[quote="TikariSakari"]Did you try to export animations without models, or just use one model to get the animation file out? As for the face count, it does indeed seem that the face count is a lot lower than what I first saw it be. The structure of the models was just quite confusing when I quickly glanced it through.

What I mean is, you can use same animation for all the models under one armature, or at least I think you should be able to. As long as they all have the same groups associated with the animation file. Like if I have a model and then outfit model, I only need to export the animation from one of the models, since they both are parented to same armature.[/quote]


I will try again in a few. The latter is how i have it setup. Four races with male and female but only a skeleton for one male and female.

-------------------------

rogerdv | 2017-01-02 01:03:58 UTC | #7

At least in my experience, animation exporting is slow. I just have an old core 2 duo 6850 and it takes some minutes to export 8 animations of 1-2 seconds each, and by minutes I mean that I have to sit and watch a video or something, it takes about 1 second per 1%.

-------------------------

vivienneanthony | 2017-01-02 01:03:59 UTC | #8

[quote="rogerdv"]At least in my experience, animation exporting is slow. I just have an old core 2 duo 6850 and it takes some minutes to export 8 animations of 1-2 seconds each, and by minutes I mean that I have to sit and watch a video or something, it takes about 1 second per 1%.[/quote]

Yup. I let it run when I went to sleep two days ago. It exported it but it's definitely a while.

-------------------------

vivienneanthony | 2017-01-02 01:03:59 UTC | #9

Hi

I made this basic code.

[code]    /// Add animation state
        Animation * IdleAnimation = new Animation(context_);
        IdleAnimation = cache->GetResource<Animation>("Resources/Models/standardbipedolianmaleIdleGuardAction.ani");

        IdleAnimation -> SetAnimationName ("IdleAnimation");
        playermeshObject1 -> AddAnimationState(IdleAnimation);

        /// Get Controller
        AnimationController * playermeshAnimationController1 = playermeshNode1 -> GetComponent<AnimationController>();

        /// Set Morph Weight
        playermeshAnimationController1-> SetWeight("IdleAnimation",1);
        playermeshAnimationController1-> SetTime("IdleAnimation",1.80991); // I got the time from the editor.[/code]

Several questions, I noticed in the editor the animation weight, animation time, and loop, and state.I'm not seeing the weight in the documents. Is that the morph weight?

I'm refering to

[code]void 	SetLength (float length)
 	Set animation length. 

void 	SetMorphWeight (unsigned index, float weight)
 	Set vertex morph weight by index.[/code]

Additionally, do I have to set all the above or is it preloaded when the animation is loaded.

Vivienne

-------------------------

