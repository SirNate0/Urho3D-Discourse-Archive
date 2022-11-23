grokko | 2021-02-08 18:47:16 UTC | #1

Hi,
  I cannot figure out how the non bone based (frame by frame transformations) work.

I have this as reference, but the AnimationState 'state' variable returns NULL.
    
    Node* modelNode = scene_->CreateChild("myAnim");    
    modelNode->SetPosition(Vector3(260.0f, 110.0f, 260.0f));
        
    AnimatedModel* modelObject = modelNode->CreateComponent<AnimatedModel>();
    modelObject->SetModel(cache->GetResource<Model>("Models/my.mdl"));

    // walkAnimation is non null		    
    Animation* walkAnimation = cache->GetResource<Animation>("Models/my_Global.ani");
    // this below is always NULL
    AnimationState* state = modelObject->AddAnimationState(walkAnimation);

    // The state would fail to create (return null) if the animation was not found
        if (state)
        {
            // Enable full blending weight and looping
            state->SetWeight(1.0f);
            state->SetLooped(true);
            state->SetTime(Random(walkAnimation->GetLength()));
        } else {
            // NULL here
        }

So there must be something wrong with 'modelObject'.
This works with bone animation, so does anyone know the correct steps?
grokko

-------------------------

JSandusky | 2021-02-09 02:46:36 UTC | #2

[quote="grokko, post:1, topic:6689"]
I cannot figure out how the non bone based (frame by frame transformations) work.
[/quote]

Like a baked physics sim where you've got transforms for a bunch of objects or like morph-targets?

Animation has no communication with morph-targets, you have to do that manually.

For object/node animation you use an `AnimationController` component on the node at the level where the animation will be played and manage the animation from there. Generally if there's a problem there it's usually because your scene hierarchy isn't right and the animation is being played too high/low in the tree to find the nodes it's supposed to move.

-------------------------

grokko | 2021-02-09 05:23:55 UTC | #3

> Like a baked physics sim where you’ve got transforms for a bunch of objects

Exactly. Like 30 frames of a cube translating a certain direction.

Thanx

-------------------------

grokko | 2021-02-10 02:13:09 UTC | #4

Hello,
  Come to think of that I think only skeletal animation might be supported, as Node animation exists for that (like the standard Blender first animation).

grokko

-------------------------

JSandusky | 2021-02-10 04:43:57 UTC | #5

No. You can do what you intend, you probably just don't have things setup correctly. Did you the read the animation pages in the documentation?

Start with a simple single bouncing ball to work out your workflow kinks.

-------------------------

throwawayerino | 2021-02-10 13:00:24 UTC | #6

Are you talking about blender shape keys? Urho calls them vertex morphs and IIRC the asset importer doesn't have them covered. You'll have to use the blender plugin.
The function you need is [`AnimatedModel::SetMorphWeight()`](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_animated_model.html#a84c8004a3eeb8f68d9f9b35423ab71d9)

-------------------------

grokko | 2021-02-10 16:01:53 UTC | #7

Hello,
I'm not talking about blender shape keys.I think the proper saying is "Vertex Animation".
I'm talking about having a box, whether StaticModel or AnimatedModel, and simply transforming it by Scale, Rotation, Translation, _in_ Object Mode of blender, exporting the animation - and having it show up in URHO..
I did that, using the URHO exporter in blender. I got a .ani file and a .mdl file. The .ani still cannot make a URHO AnimationState object out of it like

AnimationState* state = modelObjectd->AddAnimationState(vertexAnimation);

My little picture is this

/_/ --------------------------------------------------------------> /_/
frame 1 frame N

All of the animation control seems to be in the AnimationState - and I can't see it there....

Thanks,
Grokko

-------------------------

grokko | 2021-02-10 16:12:05 UTC | #8

I should add that if I make an AnimationState out of the walking demo .ani, at least the state is non NULL, even with my AnimatedModel.

grokko

-------------------------

grokko | 2021-02-10 16:21:54 UTC | #9

The documentation says alot along the lines of

> By default an Animation is played back by using all the available bone tracks. However an animation can be only partially applied by setting a start bone, see SetStartBone(). Once set, the bone tracks will be applied hierarchically starting from the start bone.

I remember in some of my Irrlicht work, I put a bone in the model, and it worked there....

Any ideas?
grokko

-------------------------

throwawayerino | 2021-02-10 17:27:52 UTC | #10

Try attribute animation? Bind a value animation to each of the node's attributes and add in keyframes.
https://urho3d.github.io/documentation/HEAD/_attribute_animation.html

-------------------------

JSandusky | 2021-02-10 19:31:14 UTC | #11

[Urho3D - Documentation - Skeletal animation](https://urho3d.github.io/documentation/1.7.1/_skeletal_animation.html)

## Node animations

Animations can also be applied outside of an [AnimatedModel](https://urho3d.github.io/documentation/1.7.1/class_urho3_d_1_1_animated_model.html)'s bone hierarchy, to control the transforms of named nodes in the scene. The AssetImporter utility will automatically save node animations in both model or scene modes to the output file directory.

Like with skeletal animations, there are two ways to play back node animations:

* Instantiate an [AnimationState](https://urho3d.github.io/documentation/1.7.1/class_urho3_d_1_1_animation_state.html) yourself, using the constructor which takes a root scene node (animated nodes are searched for as children of this node) and an animation pointer. You need to manually advance its time position, and then call [Apply()](https://urho3d.github.io/documentation/1.7.1/class_urho3_d_1_1_animation_state.html#ae662a588f71a9adfb4aea3162bb2a742) to apply to the scene nodes.
* Create an [AnimationController](https://urho3d.github.io/documentation/1.7.1/class_urho3_d_1_1_animation_controller.html) component to the root scene node of the animation. This node should not contain an [AnimatedModel](https://urho3d.github.io/documentation/1.7.1/class_urho3_d_1_1_animated_model.html) component. Use the [AnimationController](https://urho3d.github.io/documentation/1.7.1/class_urho3_d_1_1_animation_controller.html) to play back the animation just like you would play back a skeletal animation.

Node animations do not support blending, as there is no initial pose to blend from. Instead they are always played back with full weight. Note that the scene node names in the animation and in the scene must match exactly, otherwise the animation will not play.

---

You're going to have to fire up the debugger and inspect your animations during load to see what's in them (or use a binary file disassembler if you have one you like).

-------------------------

Dave82 | 2021-02-10 21:40:24 UTC | #12

Just do as JSandusky suggested and it works. I did this previously and it works just fine. You don't need to work with AnimationState and advanced stuff. Just create a root node and add your nodes you want to animate (of course your nodes must have the same name and hierarchy as you exported in your *.ani file) and finally add an AnimationController component to the root node and then just simply Play or PlayExclusive as you do with skinned meshes and bones.
The only reason you have trouble is the animation and scene exporting you're using. I use my own exporter for 3ds max and i can confirm that transform based animations are supported by Urho3d

-------------------------

grokko | 2021-02-10 21:42:44 UTC | #13

Thank You! I figured AnimationController would be there for 'tween' animations.

grokko

-------------------------

grokko | 2021-02-11 01:44:05 UTC | #14

[quote="JSandusky, post:11, topic:6689"]
(of course your nodes must have the same name and hierarchy as you exported in your *.ani file
[/quote]
     
My hierarchy in blender is 'Cube'.
        
    `String name = walkAnimation->GetAnimationName() 
reveals the name as "Cube|Action"

All of which (Cube and Cube|Action) show up in the console as "Resource not found" at Start().

Also, a byte reader on the .ani file from AssetImporter of a .fbx reveals
    `'UANICube_CubeAction_VU_@____Cube__;_________"

of which I tried a few, all of "Resource not found" upon `Playing`
Thanx
grokko

-------------------------

grokko | 2021-02-11 07:19:03 UTC | #15

Hello,
   Here is the code so far, very simple.


        Node* modelNoded = scene_->CreateChild("tween");
        modelNoded->SetPosition(Vector3(-25.0f, 10.0f, 25.0f));
       
        StaticModel* modelObjectd = modelNoded->CreateComponent<StaticModel>();
        modelObjectd->SetModel(cache->GetResource<Model>("Models/Cube.mdl"));
	
        AnimationController * animControl = modelNoded->CreateComponent<AnimationController>();
 
        Animation* walkAnimation = cache->GetResource<Animation>("Models/CubeAction.ani");
	    String name = walkAnimation->GetAnimationName(); // this is "CubeAction"
	    char * name2 = (char *)name.CString(); 
	    float t1 = walkAnimation->GetLength();  // this is 60 frames/2 secs
	    animControl->Play(name,0,true); // always "Resource not Found."


Thats it. I used the Urho blender exporter. "Resource not Found". The GetAnimationName() string seems to be the same as the .ini file.

Thanks,
grokko

-------------------------

SirNate0 | 2021-02-11 07:10:43 UTC | #16

I think the problem is that you didn't add the animation to the animation controller. That, or perhaps you need to use "Models/CubeAction.ani".

-------------------------

grokko | 2021-02-11 07:30:41 UTC | #17

> I think the problem is that you didn’t add the animation to the animation controller. That, or perhaps you need to use “Models/CubeAction.ani”.

The .ani name in there is "CubeAction" whereas "Models/" is the directory name. The AnimationController finds the keys/track in it from the Animation which loads the .ani

Anyone?
grokko

-------------------------

Dave82 | 2021-02-11 12:10:09 UTC | #18

Animation controller's Play function expects a filename. So the correct way of doing it is : 
[code]
AnimationController * animControl = modelNoded->CreateComponent<AnimationController>(); 
animControl->Play("Models/CubeAction.ani",0,true);
[/code]

-------------------------

grokko | 2021-02-11 15:25:51 UTC | #19

Dave82!,
  You got it Man! Thanx Alot! :grinning: :grinning: :grinning:

-------------------------

