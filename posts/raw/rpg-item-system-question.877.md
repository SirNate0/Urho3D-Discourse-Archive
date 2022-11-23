rogerdv | 2017-01-02 01:03:44 UTC | #1

In previous projects, I implemented a simple system to equip items in my RPG: I just attach the mesh to a bone. I tested it in Urho and it works. But I was talking to my 3D artist and he pointed me one flaw in the idea: usually model torso has 2-3 bones, if the character bends forward, the armor mesh would get inside the character body. We tried to figure out some solution (adding bones to armor, splitting armor in two sections, etc) but none of them seems to be easy and effective. Can somebody give me a suggestion about this?

-------------------------

TikariSakari | 2017-01-02 01:03:44 UTC | #2

I would assume that if you made the model for example in blender, then use same starting point/rotation/scaling for both armatures (0,0,0) so they both have same local coordinate-system, and synced the timeline in both objects animations they should move the same way? Anyways I really do not know much about modeling nor urho, but it does sound more like issue with modeling rather than urho.

On urho I am not sure if the animations are bound to vertexes, meaning if you use same armature on both objects, you might be able to use same animation created from one object to have all animations transferred from one skeleton to other object.

-------------------------

cadaver | 2017-01-02 01:03:44 UTC | #3

You can make skinned attachments by authoring them to use the same skeleton as the main model, exporting them as separate models, then instantiating them as an additional AnimatedModel in the same scene node as the main model (the main model must be the first added AnimatedModel; this becomes the so-called "master" component, which controls the animation, and the other attachment models or "slaves" just sync to the master's bone movements)

However some games like Elder Scrolls Oblivion hide parts of the player body model when eg. wearing an armor suit, to avoid the body clipping issues.

-------------------------

rogerdv | 2017-01-02 01:03:54 UTC | #4

Well, how do I do that if I have several different armors, gloves, boots, etc?
The artist is suggesting to have the body mesh splitted in parts: head, torso, etc. Equipping item would be done simply switching material and perhaps attaching some little detail mesh. The inconvenient I see: instead of one node+one base mesh I have to deal with several children nodes, each one containing one AnimatedModel. I have no idea about how to tell that big... whatever, what skeleton it should use. The good side, I can put different heads on the player character, which allows to implement look customization (I thought that was out of my reach).

-------------------------

codingmonkey | 2017-01-02 01:03:55 UTC | #5

look at this tut. 
how to fast add new clothes to the armature and paint weights for new clothes with  transfer weights. 
[video]https://www.youtube.com/watch?v=WVfTRwXpmuQ[/video]
your artist must create the uber-skeleton with many bones for all stuff things that put in on that skeleton.
and then you just load the clothes model that needed in this time and play animations.

-------------------------

cadaver | 2017-01-02 01:03:55 UTC | #6

The skeleton sharing as it's implemented in Urho will only work when the skinned attachments are all added into the same base node. Add the "main character" AnimatedModel first, which will control the animation, while the AnimatedModels added after that are slaves (like described in my last post.) Non-skinned attachments (that don't do any skeleton sharing) can be added separately to the child (bone) nodes.

-------------------------

rogerdv | 2017-01-02 01:03:55 UTC | #7

How can I access the slave AnimatedModels? Could I use this method to implement character customization (like changing heads)?

-------------------------

cadaver | 2017-01-02 01:03:55 UTC | #8

For example using this function which fills all components of a given type into the destination vector: template <class T> void Node::GetComponents(PODVector<T*>& dest, bool recursive)

Or alternatively storing pointers to the different AnimatedModels as you instantiate them.

Yes, you should be able to swap the slave models freely (either delete and recreate them, or simply do SetModel() on them), as long as they conform to the same skeleton. That is more of an art / export question; Urho finds the bones simply by name, so if you have eg. a bone named "Head" referred to in both the head model and the body model, the skinning should work right.

-------------------------

TikariSakari | 2017-01-02 01:03:56 UTC | #9

When I saw this post, I decided to try out how it would work. I made one model for the body, and other model for clothes on top. Then I added one armature in blender and parented both models to same armature. It seemed to work perfectly in urho just porting both models separately, but they both seem to need own master node. Like the urho doesn't seem to like that one node has 2 animated models attached to it.

For me the biggest problem was actually how the clothes would be shown through the model at some frames, so I had to do some fiddling around with the model to make it work. I also came to the conclusion if there are certain parts of the body that are always under the outfits, those parts should be simply deleted from the body-model to reducde the time spent on figuring out how to animate the model so that the body doesn't glitch through the clothes.

-------------------------

rogerdv | 2017-01-02 01:03:56 UTC | #10

The problem is when you have an RPG with dozens of different armors, and the possibility to remove all items. You cant simply leave holes in the base model (my artist tried that to save polygons, until I noticed it was a bad idea).

-------------------------

Mike | 2017-01-02 01:03:57 UTC | #11

An alternative to deletion is to use multiple materials for the same geometry and to assign an empty material (a material file with only '<material/>') on-the-fly to the part you want to hide, mimicking a mask.

-------------------------

rogerdv | 2017-01-02 01:03:57 UTC | #12

Yesterday looked at Wasteland 2, and seems to use splitted meshes. So, I decided to try this solution, I will switch meshes or materials as required.
Forgot to ask, how do I decide what piece will be the master AnimatedModel? The head, the torso?

-------------------------

cadaver | 2017-01-02 01:03:57 UTC | #13

The master model needs to have all the bones you will use for all skinned attachments, otherwise the choice is up to you. If you're using AssetImporter and all the bones do not have geometry attached (not even a single triangle or such), you'll need to use the -s switch to make sure those bones get included.

-------------------------

rogerdv | 2017-01-02 01:03:57 UTC | #14

Sorry for asking too mucho, currently we have the body model splitted in head, torso with arms, hands, legs and feet. It has (or will) an armature with animations. My question is, can I simply take of torso and assign another thing? Or do I need to reafactor the models just containing the armature and maybe a head?

-------------------------

