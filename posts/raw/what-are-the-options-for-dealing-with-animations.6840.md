Batch | 2021-05-11 14:58:17 UTC | #1

Do they have to be .ANI files? If so, where can I see the format spec? The AssetImporter seems to have an animation ("anim") option, but it doesn't seem to have any description. What kind of input data is the AssetImporter expecting in order to generates .ANI files?

-------------------------

SirNate0 | 2021-05-11 15:55:18 UTC | #2

Regarding the .ani file format, see

https://urho3d.github.io/documentation/1.7.1/_file_formats.html

I think some things can be animated with an xml file, but I'm not sure whether that would include skeletal animations.

-------------------------

Batch | 2021-05-11 16:12:20 UTC | #3

Sweet, thanks. Part of me wants to poke around the old Blender addon and try to update it for the modern version, but part of me is hoping that I can just configure the AssetImporter and Blender such that no additional coding work is required.

-------------------------

JTippetts1 | 2021-05-11 22:48:29 UTC | #4

The Blender addon has a [2.8 branch](https://github.com/1vanK/Urho3D-Blender/tree/2_80) which works also for the latest 2.92 release.

-------------------------

Batch | 2021-05-12 16:35:08 UTC | #5

I thought I had tried every version of that I could find on 2.92, but I figured I'd give it a shot anyway and it seems to work. I guess it was somehow user error on my part.  
  
Do you know how to satisfy the requirements of this addon with regards to exporting animations? I can't select the Animations checkbox unless Skeleton is checked, and when I exported just a Cube with a rotation animation it gave an error saying it needed an armature/bone. I added an armature/bone, and I set the Cube's parent to be the armature, then I moved the animation to the armature. When I click Export it says Armature has no animation to export. This is as far as I've gotten, as from what I can tell there's an animation on the armature.

edit: Nevermind, I poked through the python script and it implied the channels were wrong, so I changed the settings from Actions used in tracks to All actions, and I have both mdl and ani files.

edit2: Now that I've setup a test environment and loaded the mdl/ani files I'm having a strange issue with AnimatedModel. If I use StaticModel, then the test Cube draws properly, but if I switch to AnimatedModel then suddenly part of it draws where it's located, and part of it stretches back to 0,0,0 in world coordinates. I tried loading up the sample mdl/ani files from the Skeleton example and they worked as expected, so something about the exported Cube.mdl is wonky.

edit3: By trial and error, I found enabling the checkbox "Use skinning for parent bones" causes the cube to render properly, but I've yet to get the model to actually animate.

-------------------------

HappyWeasel | 2021-05-12 20:35:47 UTC | #6

I initially had the same problem, check out this simple animated fbx (without skeleton):
https://gofile.io/d/tSLp7Z (I hope file uploads are okay) .. 

I imported it with AssetImporter like this:

    AssetImporter.exe model C:\Scenes\Arrows-anim.fbx Data\Models\Arrows.mdl -nc -nm
    Reading file C:\Scenes\Arrows-anim.fbx
    Writing model RootNode
    Writing geometry 0 with 470 vertices 1632 indices
    Writing animation AnimStack::Take 001 length 2.08333

Then in the code:

    Node* animRootNode_ = ...

    StaticModel* mdl = animRootNode_->CreateComponent<StaticModel>();
    mdl->SetModel( GetSubsystem<ResourceCache>()->GetResource<Model>( "Models/Arrows.mdl" ) );
    AnimationController* ctrl = animRootNode_->CreateComponent<AnimationController>();
    ctrl->PlayExclusive( "Models/Arrows AnimStackTake 001.ani", 0, true, 0.2f );

I think I renamed the .ani file. No idea how AssetImporter determines the name...  Probably dependant upon the app exporting the fbx..
I was not able to play it from within the editor, I had to use code..

Meanwhile skeletal animations play fine from within the editor, Just check out the ninja examples..

-------------------------

