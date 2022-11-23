nicos | 2017-01-02 01:10:00 UTC | #1

Hello !

I still work on this project : [url]http://discourse.urho3d.io/t/serial-input/1732/1[/url]. I'm OK with the serial input, inheriting the Thread class. It works very well, thanks for your assist  :slight_smile: 

So as to rotate the character's head with the Blender's Game Engine, we used a trick with an empty. The Bone "Tete" can't rotate without being constrained.
The bone has a "copy rotation"  constraint on an Empty, else it can't rotate.
Maybe this picture can help :
[img]http://s28.postimg.org/gs48ks6u5/2016_02_12_133951_1280x720_scrot.png[/img]

I tested rotate this bone with Urho, but as in Blender's Engine, it doesn't move. I tried to rotate some other bones which is ok.

Before try to code a solution that could'nt work, I try to have a tip here.
Is there a way to do the same trick with Urho (I don't work with scripts, only C++) ?

Thank you, have a nice day :wink:

-------------------------

codingmonkey | 2017-01-02 01:10:00 UTC | #2

Hi nicos, mb you need just use manual control for selected bone ?
there is simple example:

[code]onInit() 
{

	animModel_ = node_->GetComponent<AnimatedModel>();
	boneCenter_ = animModel_->GetSkeleton().GetBone("ThereIsNameOfBoneForManualRotate");
	boneCenter_->animated_ = false; // turn-off animation for this bone for manual control 

}

onTransform() 
{
	boneCenter_->node_->LookAt(EmptyNode.position, Vector3:UP, TS_WORLD);	
}[/code]

-------------------------

nicos | 2017-01-02 01:10:00 UTC | #3

Thanks codingmonkey !

It woooooorks ! ! !

We've got a sentence in France, that can resume myself : 
"Pourquoi faire simple quand on peut faire compliqu?"  
"Why make it simple when you can make it complicated"

Miss the neck, vertices et weigh problems on export from blender. I hope I'll fix it by myself, without disturbing anyone.

Thank you :slight_smile:

-------------------------

