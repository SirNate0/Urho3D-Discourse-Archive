szamq | 2017-01-02 00:58:54 UTC | #1

I loaded AnimatedModel in editor, manually rotated bones and then saved the scene.
When i load this scene in editor, the bones nodes are rotated as saved. However when I load the scene in my angel script application then the bone rotations are reset to the rest positions. I checked the editor loading code but didn't find why the results are different.
I'm loading by:
[code]    File loadFile(fileSystem.programDir + "Data/Scenes/HospitalRoom.xml", FILE_READ);
	scene_.LoadXML(loadFile);[/code]

Ps. I know that I should probably create animation or Animation state for that, but the question is what makes loading of the same scene different.

-------------------------

cadaver | 2017-01-02 00:58:54 UTC | #2

When you are manipulating an AnimatedModel's bones manually, you should disable animation applying from them. Otherwise it's a matter of luck that the bone transforms stay. The function where the skeleton reset happens is AnimatedModel::UpdateAnimation(). 

The inconsistency between editor and your application sounds odd; what may be different is that the editor doesn't update the scene until you press the play button.

Take a look at the Ragdoll sample to see how it disables animation from bones:

[code]
// Disable keyframe animation from all bones so that they will not interfere with the ragdoll
AnimatedModel@ model = node.GetComponent("AnimatedModel");
Skeleton@ skeleton = model.skeleton;
for (uint i = 0; i < skeleton.numBones; ++i)
    skeleton.bones[i].animated = false;
[/code]
Unfortunately the "animated" property of each bone can not be exposed as an easily editable attribute, but you could momentarily attach (in the editor) a script into your AnimatedModel node which does the above step.

-------------------------

cadaver | 2017-01-02 00:58:54 UTC | #3

I've pushed a fix related to this; there were unnecessary calls to trigger an animation update, even with no animation states. However, what I said generally applies especially if you want to combine animation states and manual bone update.

-------------------------

szamq | 2017-01-02 00:58:55 UTC | #4

Thanks, works great.

-------------------------

