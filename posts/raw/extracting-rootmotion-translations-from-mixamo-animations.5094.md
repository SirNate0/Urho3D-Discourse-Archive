Leith | 2019-04-11 07:41:10 UTC | #1

Usually, when artists apply root motions to animations, they do so by animating the root bone.
In my case, I have a root bone called "RootNode", with a child called "Hips" - the typical setup.
When applying a typical Mixamo jump animation, the root node is not translated - the hips are! Given that AnimationController can't help us with root motion, is there a consistent workflow (preferably for Blender) to let me bake hip translations into the root bone?

-------------------------

jmiller | 2019-04-11 14:59:09 UTC | #2

I found Blender's Motion Capture Tools (aka MoCap addon) indispensable for retargeting animations.

https://archive.blender.org/wiki/index.php/Extensions:2.6/Py/Scripts/Animation/Motion_Capture_Tools/

[edit]
I found *eliminating* unwanted root motion was usually straightforward. Have not actually tried copying it; perhaps a bit more involved.

Some related blog posts and tools
https://duckduckgo.com/?q=+mixamo+root+motion

-------------------------

Leith | 2019-04-12 03:10:45 UTC | #3

Recently, I was using a Dynamic character controller, and I wanted to suppress all root motion. I found the controller very tactile, but the "feel" of the animations was lost to the physics engine. 
Currently I am experimenting with a Kinematic character controller, which I hope to drive using the original root motions, but I quickly noticed that artists don't always animate on the root node - they sometimes animate on the hips.
I'll probably end up dealing with this issue in code, via xml metadata I already provide for character animation sets. But if there's a decent workflow to fix this issue, and I don't need to touch python, I'm definitely interested :)

-------------------------

