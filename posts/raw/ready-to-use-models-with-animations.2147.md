Lumak | 2017-01-26 12:09:09 UTC | #1

Mixamo characters with animations ready for use for Urho3D - [url]https://github.com/Lumak/Urho3D-Assets/tree/master/Models[/url]
**How to get mixamo char/anims - page2 of this thread.**

notes:

- the model faces the opposite Z direction, so you'll need to spin it by 180
- avoid adjusting the "Head" node due to the above reason (or just fix it)
**[How to spin your char by 180](http://discourse.urho3d.io/t/ready-to-use-models-with-animations/2147/12) - **note: this change, along with the Mutant char, was added to Urho3D/master as of August 16, 2016.**

models:
[img]http://i.imgur.com/6lEN7dl.png[/img]

[b]AssetImporter:[/b]
Modified AssetImporter to suppress "$AssimpFbx$" nodes that's generated for Mixamo characters. Of course, this works for all fbx files.
The option is now enabled by default.   **To disable it**, use:
```
AssetImporter model <input file.fbx> <output file> -np
AssetImporter anim <input file.fbx> <output file>  -np
```
**This was added to Urho3D/master, Aug 22, 2016.**

Edit: added info about the assetImporter merge.

-------------------------

1vanK | 2017-01-02 01:13:28 UTC | #2

> the model faces the opposite Z direction, so you'll need to spin it by 180

If u use Blender exporter, you can choose forward direction for result model

-------------------------

codingmonkey | 2017-01-02 01:13:28 UTC | #3

Thanks for sharing! i guess this useful for prototyping game

-------------------------

rku | 2017-01-02 01:13:28 UTC | #4

This is great, but way more useful would be to know method how you did it. There are tons of animations and we would love to be able to do same thing for other animations ourselves. Naive attempt i tried (just converting fbx to mdl/ani) did not produce a working animations.

-------------------------

Lumak | 2017-01-02 01:13:28 UTC | #5

[quote="1vanK"]
If u use Blender exporter, you can choose forward direction for result model[/quote]
That's good to know, but I primarily use Maya LT to retarget animations. I could probably figure out how to do it in Maya, but adding an adjustNode to spin it 180 is simple to do...

[quote="codingmonkey"]Thanks for sharing! i guess this useful for prototyping game[/quote]
It might become more beneficial than just for prototyping when I provide skeleton.fbx files.

[quote="rku"]This is great, but way more useful would be to know method how you did it. There are tons of animations and we would love to be able to do same thing for other animations ourselves. Naive attempt i tried (just converting fbx to mdl/ani) did not produce a working animations.[/quote]
I discover that most models on the site have pivot rotation which causes "$AssimpFbx$" node insertion. This ends up inflating the skeleton bone count - I had a few models that ended up with 200+ bones! To correct it, you'll have to zero out the rotation pivot, but take the rotation pivot value and add it to the transform rotation field.  Essentially, you're elevating the rotation pivot to its parent transform.


**note**
Added another model to the repository and run anim for x_bot.

-------------------------

Lumak | 2017-01-02 01:13:28 UTC | #6

I have completed the Swat standing rifle pack animations.  I know there are at least three ppl making a shooter game in the community, hope these animations help.

Edit: link [url]https://github.com/Lumak/Urho3D-Assets/tree/master/Models/Swat[/url]

-------------------------

Lumak | 2017-01-02 01:13:29 UTC | #7

Added Mutant model/anim [url]https://github.com/Lumak/Urho3D-Assets/tree/master/Models/Mutant[/url].

-------------------------

jenge | 2017-01-02 01:13:29 UTC | #8

If possible, including source fbx/blend/collada in repo with import settings documented would be great for being able to import/export to future mdl runtime representations or asset importer improvements.

EDIT: Noting probably not possible due to source of files :slight_smile:

EDIT2: Looks like [github.com/Lumak/Urho3D-Assets/ ... els/Mutant](https://github.com/Lumak/Urho3D-Assets/tree/master/Models/Mutant) needs a LICENSE.TXT

Thanks!  Great stuff!

-------------------------

Lumak | 2017-01-02 01:13:29 UTC | #9

mutant/license.txt added along with a few more anim files.

I've added _skeleton.fbx file for each model which can be used to skin your own custom mesh  **(acian uses x_bot) .

-------------------------

rku | 2017-01-02 01:13:29 UTC | #10

[quote="jenge"]If possible, including source fbx/blend/collada in repo [b]with import settings documented[/b] would be great for being able to import/export to future mdl runtime representations or asset importer improvements.

EDIT: Noting probably not possible due to source of files :slight_smile:

EDIT2: Looks like [github.com/Lumak/Urho3D-Assets/ ... els/Mutant](https://github.com/Lumak/Urho3D-Assets/tree/master/Models/Mutant) needs a LICENSE.TXT

Thanks!  Great stuff![/quote]

That indeed would be great so we could replicate the process ourselves. Lumak either seems to not be interested in telling us how to do that or we are having some miscommunication here since i already asked for same thing in my previous post.

Btw Lumak arent all mixamo models using same skeleton?

-------------------------

Lumak | 2017-01-26 12:07:34 UTC | #11

[quote="rku"]
That indeed would be great so we could replicate the process ourselves. Lumak either seems to not be interested in telling us how to do that or we are having some miscommunication here since i already asked for same thing in my previous post.
Btw Lumak arent all mixamo models using same skeleton?[/quote]

On the contrary, I have shared my process on how I did it and are described in my reply to you in this post and in [url]http://discourse.urho3d.io/t/mixamo-animations-characters-free/1999/1[/url]. I will reiterate it here but in a step-by-step manner for clarity.  But before I do, let me clarify/answer a couple of things:
1) As jenge himself realized, [b]mixamo license prohibits distribution of character/animation file in editable format[/b]. And this restriction is the only reason I cannot provide model.fbx or animation.fbx files in the repository.
2) "Do models use same skeleton?" - They are not the same. While the base joint names are the same, i.e. named as "Hip", "Neck", etc., some models have different prefix added to the base, e.g. "mixamorig:Head", "swat:Head", "Mutant:Head", etc.

### Mixamo character/animation port process using Maya
As I mentioned numerous times in my posts, I use Maya LT for the porting process. I will describe this process first then will describe what I discovered just using the animation mapping process in mixamo.com.

0) prerequisite: have Maya or Maya LT installed
1) goto mixamo.com and download your model.fbx (t-pose) and animation set (or single animation) in .fbx format.
2) open your model.fbx in maya, open HumanIK editor, choose Create Character Definition, map all joints of your model to the character definition until it becomes "green" lit -> save your model file (maya format) -> export as fbx format with animation box unchecked.
*note1* clear any non-zero pivot rotation - the values found "jointOrientation" needs to be elevated to the parent transform, i.e. add it to the transfrom field for the same joing.
*note2* even doing note1 sometimes result in wonky animation. If this happens, you'll need to reskin the model or replace the rig(skeleton) with a known working rig and re-skin.

3) for each animation that you want to port, open the animation.fbx file in maya, goto frame -1 (negative 1) and set it to t-pose (frame -1 because animations typically start at frame 0), key all your joints in frame -1, open HumanIK editor, select Create Character Definition,  map all joints -> save the file (maya format).
4) open your saved maya model file, 
   from the file explorer drag in your saved animation file into maya, 
   in the HumanIK editor- character control panel, select "Character:" as your model's character, select "Source:" as the animation's character
   set the key frame range of the animation
   in HumanIK, choose Bake > Bake To Skeleton
   delete the animation rig
   save the file as model_animation or w/e
   export to .fbx file format, w/ the animation box checked

5) using AssetImporter and arguments:
   for model -  AssetImporter [b]model[/b] your_model.fbx output_file.mdl
   for animation - AssetImporter [b]anim[/b] your_model_animation.fbx output_animation_file.anim
   *note* output file will contain something like "Take-00" or w/e, remove that and rename it as ouput_animfile.anim
   *note2* you may have to use an additional option [b]-t[/b] to Generate tangents for models with normal bump map

-------------------------------------------------------------------------------------------

### Porting character/animation right out of mixamo.com
I have not done this process until just a few minutes ago, and it seemed to work.
1) goto mixamo.com -> Browse Animation -> select "Creature Pack" as an example
2) At the right of the window, it shows "19 animation in Creature Pack on X Bot" (for me at least), click on "Change Character" and select the Mutant character.
3) click on the "Add To My Assets" button, once it completes the button changes to "View/Download" -> click it
4) on the left side of the window there's a check box next to the trash can, selecting it will select your animation(s) -> click Queue Download -> pop up confirmation : .fbx, t-pose , and every other option as default
5) once the progress completes, check your animation, click download.
6) unzip your In_Progress.zip (following the creature pack/mutant example got me this file)
7) using AssetImporter and arguments:
   for model -  AssetImporter [b]model[/b] Mutant.fbx output_file.mdl
   for animation - AssetImporter [b]anim[/b] mutant_idle.fbx Mutant_Idle.anim
   *note* the output file will contain a string "_mixamo.com.ani", just remove the "_mixamo.com"
   *note2* you may have to use an additional option [b]-t[/b] ->Generate tangents for models with normal bump map

**things to do outside of assetImporter**
1) you'll need to extract the textures using something like Blender. I did this once but I think it was: choose geom > material > output texture (can't remember exactly)
2) the model in Urho3D is huge - scaled by 100 from the looks of it - fix this in Blender or scale the node by 0.01f (this works properly)
3) some animations have root motion - fix it in Blender

I hope this wall of text helps.

Edit: clearing pivot rotation needs to happen in Maya step 2, not 3
Edit: added scaling info in *problems 2)
Edit: added info about additional option [b]-t[/b] using the assetImporter for normal bump map

-------------------------

Lumak | 2017-01-26 12:07:57 UTC | #12

No one asked how to spin your model by 180 in code. I guess everyone already knows how to do this, but here is how-to for some who don't know.

Using 18_CharacterDemo, snippets of relevant sections.

### Spinning your model by 180 in code
CharacterDemo.cpp

[code]
void CharacterDemo::CreateCharacter()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    Node* objectNode = scene_->CreateChild("Jack");
    objectNode->SetPosition(Vector3(0.0f, 1.0f, 0.0f));

    // rotate model by 180 ****************************
    Node* adjustNode = objectNode->CreateChild("AdjNode");
    Quaternion qAdjRot(180, Vector3(0,1,0) ); // rotate it by 180 
    adjustNode->SetRotation( qAdjRot );

    // Create the rendering component + animation controller
    AnimatedModel* object = adjustNode->CreateComponent<AnimatedModel>();

    //********************* change the model and material name
    object->SetModel(cache->GetResource<Model>("Models/Jack.mdl"));
    object->SetMaterial(cache->GetResource<Material>("Materials/Jack.xml"));
    object->SetCastShadows(true);

    adjustNode->CreateComponent<AnimationController>();

      // ******************** rename it to proper head joint name // Set the head bone for manual control
    object->GetSkeleton().GetBone("Bip01_Head")->animated_ = false;

. . .
}
[/code]

[code]
void CharacterDemo::HandlePostUpdate(StringHash eventType, VariantMap& eventData)
{
    if (!character_)
        return;

    Node* characterNode = character_->GetNode();

    // Get camera lookat dir from character yaw + pitch
    Quaternion rot = characterNode->GetRotation();
    Quaternion dir = rot * Quaternion(character_->controls_.pitch_, Vector3::RIGHT);

    // ************* rename it to proper head joint name // Turn head to camera pitch, but limit to avoid unnatural animation
    Node* headNode = characterNode->GetChild("Bip01_Head", true);
    float limitPitch = Clamp(character_->controls_.pitch_, -45.0f, 45.0f);
    Quaternion headDir = rot * Quaternion(limitPitch, Vector3(1.0f, 0.0f, 0.0f));
    // This could be expanded to look at an arbitrary target, now just look at a point in front
    Vector3 headWorldTarget = headNode->GetWorldPosition() + headDir * Vector3(0.0f, 0.0f, -1.0f); // -z direction ****************************
    headNode->LookAt(headWorldTarget, Vector3(0.0f, 1.0f, 0.0f));
    // Correct head orientation because LookAt assumes Z = forward, but the bone has been authored differently (Y = forward)
//    headNode->Rotate(Quaternion(0.0f, 90.0f, 90.0f)); //************************* dont need this

. . . 
}
[/code]

Character.cpp
[code]
void Character::FixedUpdate(float timeStep)
{
    /// \todo Could cache the components for faster access instead of finding them each frame
    RigidBody* body = GetComponent<RigidBody>();
    AnimationController* animCtrl = node_->GetComponent<AnimationController>(true); //********** recursive get

. . . 
}
[/code]

Edit: changed comment to "recursive get"

-------------------------

jenge | 2017-01-02 01:13:30 UTC | #13

Wow, great docs on the model import process!  High quality 3D models have always been one of the most challenging assets for projects.  This is really awesome. thanks for the models and trailblazing the process  :smiley:

-------------------------

Lumak | 2017-01-26 12:10:08 UTC | #14

[quote="jenge"]Wow, great docs on the model import process!  High quality 3D models have always been one of the most challenging assets for projects.  This is really awesome. thanks for the models and trailblazing the process  :smiley:[/quote]

You're welcome.

I was really surprised by how easy it was to download then import character/animations using the **Porting character/animation right out of mixamo.com** method.  
It was my first attempt and didn't expect to have an animating character in Urho3D following this process**.  Can't get any easier than that!

Edit: **rephrased

-------------------------

Bluemoon | 2017-01-02 01:13:33 UTC | #15

Great work Lumark!! This is just what I need

Unfortunately when I import the models into the editor and setup the materials I get an unlit material like shown below [img]http://i.imgur.com/ucUFJ7p.jpg[/img]
When I edited the material's technique from "Techniques/DiffNormalSpec.xml" to "Techniques/DiffNormalSpecEmissive.xml" it seemed to correct but I noticed that it flickers on and off based on camera angle.

I honestly have no idea what is going on and I really need to use these models, most importantly their animations  :frowning:

-------------------------

NiteLordz | 2017-01-02 01:13:33 UTC | #16

i found that the models from that were in the repo, were not compatible with the latest version of github, as they were missing vertex declarations.

to test, don't supply a material when using, and it will use the default white material.

i had to export the models myself, which given the above process was simple! (GREAT job btw).

Once i got the steps down, it was easy to follow and import.

I now can test a handful of things i have been wanting, but couldn't because of lack of animation skill.

-------------------------

cadaver | 2017-01-02 01:13:33 UTC | #17

Current Urho runtime code should load both the old & new models, that means without or with vertex declarations.

Where exactly did you run into trouble?

-------------------------

NiteLordz | 2017-01-02 01:13:33 UTC | #18

If you use the "Mutant" model as an example.  

The material provided has a technique of DiffNormal.xml, this will render no model, but the shadow is animated.

If you modified the material to be just Diff.xml, the model will render properly (just not with a normal).

If you enable D3D11_CREATE_DEVICE_DEBUG, you get the following output

[code]D3D11 WARNING: ID3D11Device::CreateInputLayout: The provided input signature expects to read an element with SemanticName/Index: 'BLENDINDICES'/0 and component(s) of the type 'int32'.  However, the matching entry in the Input Layout declaration, element[6], specifies mismatched format: 'R8G8B8A8_UINT'.  This is not an error, since behavior is well defined: The element format determines what data conversion algorithm gets applied before it shows up in a shader register. Independently, the shader input signature defines how the shader will interpret the data that has been placed in its input registers, with no change in the bits stored.  It is valid for the application to reinterpret data as a different type once it is in the vertex shader, so this warning is issued just in case reinterpretation was not intended by the author. [ STATE_CREATION WARNING #391: CREATEINPUTLAYOUT_TYPE_MISMATCH]
D3D11 WARNING: ID3D11DeviceContext::DrawIndexed: The Pixel Shader expects a Render Target View bound to slot 0, but none is bound. This is OK, as writes of an unbound Render Target View are discarded. It is also possible the developer knows the data will not be used anyway. This is only a problem if the developer actually intended to bind a Render Target View here. [ EXECUTION WARNING #3146081: DEVICE_DRAW_RENDERTARGETVIEW_NOT_SET][/code]

If you run the fbx model provided by mixamo thru the AssetImporter, then the model will just drop right in properly.

Hope this helps

-------------------------

cadaver | 2017-01-02 01:13:34 UTC | #19

That's probably from missing tangents in the model, which are required for normal mapping techniques. D3D11 is strict in that sense and fails to create the input layout when shader wants data that isn't there in the buffer (resulting in failure to render), while D3D9 and OpenGL would just fetch invalid data, probably zeroes.

-------------------------

Lumak | 2017-01-02 01:13:34 UTC | #20

@ Bluemoon
Is it possible that it's the same issue Cadaver mentioned with missing tangents? Try using an additional option [b]-t[/b] in the assetImporter.

@NiteLordz, the models in my repo didn't work for you? Hmm, I'm using OpenGL renderer and it works for me, although, I also forgot to generate tangents.

-------------------------

NiteLordz | 2017-01-02 01:13:34 UTC | #21

Yea, I am on d3d 11, and they didn't work.

When I reexport them, using it instructions, I added the -t and they worked.

-------------------------

Lumak | 2017-01-02 01:13:34 UTC | #22

Ok, good to know.  I'll have to regenerate the .mdl files on the repo with tangents enabled - probably not today but in few days.

-------------------------

Bluemoon | 2017-01-02 01:13:34 UTC | #23

@Lumark, I actually used the model in your repo. The issue might probably be with the tangent as noted by cadaver

-------------------------

Lumak | 2017-01-02 01:13:35 UTC | #24

@Bluemoon, ok I updated the swat and mutant.mdl files in the repo.  They should work properly now.

-------------------------

Lumak | 2017-01-02 01:13:43 UTC | #25

I've been working on the AssetImporter to squash "$AssimpFbx$" nodes that's generated for several Mixamo characters.  This method saves me time from manually editing all joints with pivot transforms in Maya.

See the first page, [url]http://discourse.urho3d.io/t/ready-to-use-models-with-animations/2147/1[/url]

-------------------------

TheSHEEEP | 2017-01-02 01:13:43 UTC | #26

Is there a reason not to do that automatically?
And instead create an option to disable the feature.

-------------------------

Lumak | 2017-01-02 01:13:44 UTC | #27

@SHEEP
Good question. I've considered having this option set as default but have two reasons why it's not yet.  First is I don't know how prevalent this problem is.  I have bought some models with fbx files and couple models had few $AssimpFbx$ ($fbx for short from now on) bones generated but not in the extent which generated near 200 like some mixamo models. 

Is it common? I don't know the answer.  

Second is while it's it's common to have multiple $fbx nodes per bone in models, I have yet to see multiple $fbx nodes per bone articulated in animation. I haven't sampled enough mixamo animation files to know if there exists such case.  If they do exist then complexity of extrapolating animation would became significantly more difficult; something that would require testing.

If anyone finds an fbx model that cannot be animated using this option, whether it's mixamo model or your own, I'd like to get my hands on it for testing.

-------------------------

Lumak | 2017-01-02 01:13:49 UTC | #28

Added a few more mutant anims in the repo.

-------------------------

Lumak | 2017-01-02 01:13:51 UTC | #29

Added two more Mutant [color=#0000FF]layer animations[/color]: Throw and HitHead.  And with that, I'll say the Mutant sample animation is now complete.

-------------------------

weitjong | 2017-01-02 01:13:52 UTC | #30

Thanks for sharing them!

-------------------------

jenge | 2017-01-26 12:10:42 UTC | #31

Thanks!  

Great work documenting the process!

I had fun yesterday porting the character example to C#, you can checkout the [i]work in progress[/i] scripts here: 

[github.com/AtomicGameEngine/Ato ... Components](https://github.com/AtomicGameEngine/AtomicExamples/tree/master/AtomicNET/AtomicMutant/Resources/Components)

:slight_smile:

https://www.youtube.com/watch?v=GO0yr9wCdlY

- Josh

-------------------------

Eugene | 2017-01-02 01:15:22 UTC | #32

Can you please specify velocity of walk/run anims?

I tried to adjust velocity of Swat:WalkFwd, it's about 1.5~2.0m/s, but it's pretty hard for me.

-------------------------

Lumak | 2017-01-02 01:15:22 UTC | #33

I don't have the velocity info on the walk/run anims.  You can try dumping the foot joint position keys during the animations and derive it.

-------------------------

Eugene | 2017-01-02 01:15:23 UTC | #34

[quote="Lumak"]I don't have the velocity info on the walk/run anims.  You can try dumping the foot joint position keys during the animations and derive it.[/quote]
Huh... The problem is that foot joint velocity is not always constant during ground contact...

-------------------------

Lumak | 2017-01-02 01:15:23 UTC | #35

Based on the animation duration and the distance traveled:
[ul]
[li]walk - 1.842 m/s[/li]
[li]run - 4.78 m/s[/li]
[li]sprint - 7.164 m/s[/li][/ul]

-------------------------

dakilla | 2017-01-25 17:42:17 UTC | #36

Hi

I detailed the process I used to convert mixamo animated models for Urho3D using Blender.
[here](https://github.com/fredakilla/UrhoTournament/wiki/Import-mixamo-3D-model-to-Urho3D)

-------------------------

Lumak | 2017-01-25 18:07:01 UTC | #37

Nice write up. I think that'll be helpful for ppl using Blender.
I rarely use Blender but there's Urho3D exporter for Blender.  Couldn't you just use that instead and skip the middle step of exporting to an FBX file?

-------------------------

dakilla | 2017-01-26 06:07:29 UTC | #38

It depends of the characters complexity, problem is if there is multiple geometries with multiple materials and if you want  a simplified model and unique material. when merging objects it is necessary to recreate uvmaps and bake textures, I dont think the exporter do that (maybe it is possible to automate the process). Why I did it manually, and it learn how to do it yourself :slight_smile: . But yes, it's possible to use the blender exporter, it works fine, to directly export .mdl, materials, and textures instead of exporting to fbx and using manually AssetImporter.

-------------------------

Lumak | 2017-01-26 19:09:50 UTC | #39

I see. What you've described is useful for Blender users.

-------------------------

sirop | 2018-06-26 15:30:41 UTC | #40

Hello, @dakilla , 
I used your method and could download and  export Malcolm from Blender to Urho with all the materials and textures set right.

However the exported animation does not work.

What shall I do? Apply some tweaks as @Lumak proposes?
Have some more sophisticated code than in 06_SkeletalAnimation sample ?

Thanks in advance.

BTW, when doing
 > Animation* walkAnimation = cache->GetResource<Animation>("Malcolm/walking_inplace.ani");
> 	AnimationState* state = modelObject->AddAnimationState(walkAnimation);
> 	// The state would fail to create (return null) if the animation was not found
> 	if (state)
> 	{		
>         URHO3D_LOGINFO("Animation state added.");
>         // Enable full blending weight and looping
> 		state->SetWeight(1.0f);
> 		state->SetLooped(true);
> 		state->SetTime(Random(walkAnimation->GetLength()));        
> 	}

I get no "Animation state added." message in the log file.

-------------------------

Lumak | 2018-06-26 17:58:57 UTC | #41

Mixamo made some changes since this post: FBX download option was added and you should always choose **FBX for Unity(.fbx).**

Simply download the model and animations and import them directly from the editor and they'll work.  Although, you'll still have to scale the main node to (0.01, 0.01, 0.01).

I tested Malcolm model with walking in-place animation:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/c/ce7f905339803789a4843dfcde1aa6b51af376ab.png[/img]

-------------------------

sirop | 2018-06-27 06:30:50 UTC | #42

[quote="Lumak, post:41, topic:2147"]
Simply download the model and animations
[/quote]

Thanks for your answer. I already achieved similar results with Blender and simple ( non Unity) fbx.
But when using these results in sample 6 "SkeletonAnimation" no animation shows up.

What do you mean with "download the model and animations and import them" ?
Are there different files for the model and for animation on Mixamo?

-------------------------

Lumak | 2018-06-27 13:40:01 UTC | #43

Key word is "import them *directly from the editor*", no Blender used. When using the editor, the import process calls AssetImporter.  Mixamo now offers two fbx formats to download, 1) an fbx format and 2) FBX for Unity(.fbx).  The first is probably a FBX 2016 format and the latter is most likely FBX 2013.  Assimp still only supports FBX 2013, so the logical choice is to choose FBX for Unity.

Just looked at both FBX formats in binary:
* FBX file =  FBX SDK/FBX Plugins version 2014.2.1
* FBX for Unity = FBX SDK/FBX Plugins version 2014.2.1 build=20131219

So, I still don't address why it doesn't work with Blender (someone else might have that answer as I don't use Blender), but my point is you can use the Urho3D editor to import the fbx files directly and they'll work, provided you download the FBX for Unity files.

-------------------------

johnnycable | 2018-06-27 17:48:35 UTC | #44

[quote="Lumak, post:43, topic:2147"]
So, I still don’t address why it doesn’t work with Blender
[/quote]

Autodesk license for their importer is incompatible with Blender license. Has been substituted with a reverse engineer solution, but without too much love... :wink:

EDIT: I've used dae from Mixamo with Blender, with some success. But I'm not sure it they truly work...

-------------------------

sirop | 2018-06-28 17:05:34 UTC | #45

Ok, thanks so far. Instead of using the Urho editor I used the Asset importer from command line.

Now I landed at something similar to  [Spinning your model by 180 in code](https://discourse.urho3d.io/t/ready-to-use-models-with-animations/2147/12) .

Blender exporter has an option for exporting bones orientation. I would try this out
as I do not know how universal your approach in [Spinning your model by 180 in code](https://discourse.urho3d.io/t/ready-to-use-models-with-animations/2147/12) is.

-------------------------

Lumak | 2018-06-29 12:55:49 UTC | #46

Is there a question in your statement?  Anyway, there's always alternatives. You can modify AssetImporter to flip the model and animation or fix Urho3D exporter for Blender.

-------------------------

glebedev | 2022-05-13 10:04:13 UTC | #47

Hey! I would like to add couple new animations for Mutant but bone names seems to be different if I export the model from Mixamo. In your original files the bone names have prefix Mutant and in my case it is mixamorig. Is there some export options I'm missing?

-------------------------

Lumak | 2022-06-07 02:38:00 UTC | #48

I had to do some backtracing to see how the bone names were named, and it looks like, as you already noticed, the mixamorig prefix was replaced with Mutant. The change in the prefix was I think it had to do with Maya adding additional prefix to already existing mixamorig prefix, which got really messy, and stripping that resulted in the model name prefix.
If you need to make changes to the model/animation set to add new animation(s) then you should.

-------------------------

