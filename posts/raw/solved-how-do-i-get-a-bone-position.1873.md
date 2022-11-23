noals | 2017-01-02 01:10:58 UTC | #1

hi,

i load a StaticModel* in the scene and would like to get its bone positions in the scene.

i searched on the net but most examples use scripts so it wasn't good for me. 
then i saw on another post that i didn't need to get the skeleton to have access to bones, i could just use nodes so i tryed and it compiled fine but when i started the application, it just crashed so i guess it was because it wasn't finding the bone node i wanted to access as my model's child.

actually, when i rig my model, it is the model that is a child of the skeleton so should i rig it the other way so the bones become a child of the model ? (i don't animated those models, it is just to get some positions when the model is loaded)
or is there another method to access bones from the loaded model ?

thx.

-------------------------

gawag | 2017-01-02 01:11:02 UTC | #2

Normally you should be able to get bones as they are child nodes of the node of the model:
[code]
Node* n=node_model->GetChild("torso",true);
[/code]
The bone in this case is called "torso". I think with the "true" the function goes recursively through the bones with their childs until it finds the asked node/bone via its name.
Also Nodes have a GetWorldPosition: [urho3d.github.io/documentation/1 ... 7f37a684ba](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_node.html#a92372a305fa427e9ce58df7f37a684ba)
This may only work with AnimatedModels.

Also the node has to have the AnimatedModel:
[code]
AnimatedModel* boxObject=node_model->CreateComponent<AnimatedModel>();
boxObject->SetModel(cache->GetResource<Urho3D::Model>("Data/Models/robot.mdl"));
[/code]

-------------------------

noals | 2017-01-02 01:11:02 UTC | #3

thx, i knew i can't GetSkeleton with StaticModel but with the node method, i wasn't sure about the bones.

i encounter a weird problem, the model doesn't show up in the application when i use AnimatedModel.
[code]
        moduleNode=my_scene->CreateChild("module");
        moduleNode->SetPosition(Vector3(0,0,0));
        //StaticModel* moduleObject=moduleNode->CreateComponent<StaticModel>();
        AnimatedModel* moduleObject=moduleNode->CreateComponent<AnimatedModel>();
        moduleObject->SetModel(cache->GetResource<Model>(modulePath));
        moduleObject->SetMaterial(cache->GetResource<Material>(moduleTexturePath));
[/code]

with the commented StaticModel :
[url=http://www.hostingpics.net/viewer.php?id=460007staticmodel.png][img]http://img15.hostingpics.net/pics/460007staticmodel.png[/img][/url]

with the AnimatedModel :
[url=http://www.hostingpics.net/viewer.php?id=831747animatedmodel.png][img]http://img15.hostingpics.net/pics/831747animatedmodel.png[/img][/url]

-------------------------

gawag | 2017-01-02 01:11:03 UTC | #4

Huh that's weird.
Has the model a proper skeleton? Is it maybe rotated or offsetted so that the model is not visible?
Does it load in the editor?

-------------------------

noals | 2017-01-02 01:11:03 UTC | #5

my models are rigged like that :
[url=http://www.hostingpics.net/viewer.php?id=371091rig.png][img]http://img15.hostingpics.net/pics/371091rig.png[/img][/url]
bones look like they're on top but it is because of the x-ray view, they are well centered.
i wasn't sure a bone would return a position from its beginning or from its end so i rigged it like that.
Armature
-----Bone1
        |-----exit1
-----Bone2
        |-----exit2
-----Bone3
       |-----exit3
-----Bone4
       |-----exit4

i export them from blender with the Skeleton but maybe i need to export them with Animations too for it to work as an AnimatedModel even through there are no animations ?
[b]edit: i guess that's it because when i check the animation box in the exporter there is a "only keyed bones" options so i will try that next time and tell you how it goes, thank you.[/b]

[quote]Does it load in the editor?[/quote]
i don't use the editor but i tested it previously when i wasn't able to load my model before so i'm pretty sure it does since it load without problem in my program as a StaticModel.

-------------------------

gawag | 2017-01-02 01:11:04 UTC | #6

Oh I did something really similar as you seem to be doing. I did parts of a cave with bones at their openings and connected them randomly together in Urho.
Looks like this in Blender: [i.imgur.com/kVRdiCB.jpg](http://i.imgur.com/kVRdiCB.jpg)
The project doesn't build currently and this seems to be the only existing image: vignette2.wikia.nocookie.net/urho3d/images/1/19/Sus1.jpg
You could check it out at [github.com/damu/Spooky-Urho-Sample](https://github.com/damu/Spooky-Urho-Sample) but I think it's not building with Urho >=1.5 currently.
The bones in Blender seem to have their root/tail at the opening, yours their head. I think the tail (this is in your case in the middle of the model) is in Urho reported as the position.
I'm loading the models as AnimatedModel's. The interesting code for the room stuff seems to be in world_part.h, world_part.cpp and misc.h. The world is actually generated here [github.com/damu/Spooky-Urho-Sam ... g.cpp#L127](https://github.com/damu/Spooky-Urho-Sample/blob/master/gs_playing.cpp#L127)
The Blender file with the "rooms" is blends/mineshaft.blend

No idea why it isn't loading as an animated model. Can you upload the Blender file?

-------------------------

noals | 2017-01-02 01:11:07 UTC | #7

it seem you didn't see my edit :
[quote]edit: i guess that's it because when i check the animation box in the exporter there is a "only keyed bones" options so i will try that next time and tell you how it goes, thank you.[/quote]
i will see tomorow if i can't have anything working with the animation exporting from blender.


about the other project, thx, i will check it later, it could have some interesting examples.

for know i just progress step by step.
i'm able to randomly load a module from a xml list.
i need to know the bones position because when i load a module, i get its number of exits; and so for each exits i will need to get the bones position and put it in some kind of list or struct.
then when i load another random module, i update again my exits list and delete from the list exits that are taken.
the models was just for trying stuff with programmation, it will be easy to add anything but i will maybe need to make a module class or something. i will see later for the automation algo.

-------------------------

rasteron | 2017-01-02 01:11:07 UTC | #8

I think the NSW demo has an actual example where you get bone position.

-------------------------

noals | 2017-01-02 01:11:08 UTC | #9

here are my blend files :
[s000.tinyupload.com/index.php?fi ... 7565826291](http://s000.tinyupload.com/index.php?file_id=96351725697565826291)
(and the textures  :blush:  [s000.tinyupload.com/index.php?fi ... 2691415834](http://s000.tinyupload.com/index.php?file_id=43763937082691415834))
it was the same result with the animation export so i don't know what i did wrong.


[quote]I think the NSW demo has an actual example where you get bone position.[/quote]
nsw is only made with script ? i didn't checked about scripting yet, i don't want to mix stuffs if i don't need it. it's hard enough for me as it is.

-------------------------

rasteron | 2017-01-02 01:11:09 UTC | #10

[quote="noals"]
[quote="rasteron"]I think the NSW demo has an actual example where you get bone position.[/quote]
nsw is only made with script ? i didn't checked about scripting yet, i don't want to mix stuffs if i don't need it. it's hard enough for me as it is.[/quote]

You can check out scorvi's C++ port of NSW if you are having trouble checking the actual AS code:

[github.com/scorvi/Urho3DSamples ... njaSnowWar](https://github.com/scorvi/Urho3DSamples/tree/master/07_NinjaSnowWar)

I think it's the part where it queries the feet position to generate dust particle if that is related to your bone position question.

-------------------------

noals | 2017-01-02 01:11:09 UTC | #11

this answered my question but since another problem arised, i can't even test it.
[quote="gawag"]Normally you should be able to get bones as they are child nodes of the node of the model:
[code]
Node* n=node_model->GetChild("torso",true);
[/code]
The bone in this case is called "torso". I think with the "true" the function goes recursively through the bones with their childs until it finds the asked node/bone via its name.
Also Nodes have a GetWorldPosition: [urho3d.github.io/documentation/1 ... 7f37a684ba](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_node.html#a92372a305fa427e9ce58df7f37a684ba)
This may only work with AnimatedModels.

Also the node has to have the AnimatedModel:
[code]
AnimatedModel* boxObject=node_model->CreateComponent<AnimatedModel>();
boxObject->SetModel(cache->GetResource<Urho3D::Model>("Data/Models/robot.mdl"));
[/code][/quote]

-------------------------

noals | 2017-01-02 01:11:10 UTC | #12

here is my full project so far if you want to take a look and if you can fix my disappearing AnimatedModel issue, that would be great; in hope the gawag method to get bones positions works later on.
[s000.tinyupload.com/index.php?fi ... 9858335300](http://s000.tinyupload.com/index.php?file_id=05514931609858335300)

-------------------------

Modanung | 2017-01-02 01:11:10 UTC | #13

Niether of the blend files have the Weights option checked, try exporting your models with (Bone) Weights if you didn't. It might solve your problem, or at least part of it.

-------------------------

noals | 2017-01-02 01:11:10 UTC | #14

thx, that was it.
everything seem to work fine now.

[url=http://www.hostingpics.net/viewer.php?id=524936exit1Pos.png][img]http://img15.hostingpics.net/pics/524936exit1Pos.png[/img][/url]

[code]
        moduleNode=my_scene->CreateChild("module");
        moduleNode->SetPosition(Vector3(0,0,0));
        AnimatedModel* moduleObject=moduleNode->CreateComponent<AnimatedModel>();
        moduleObject->SetModel(cache->GetResource<Model>(modulePath));
        moduleObject->SetMaterial(cache->GetResource<Material>(moduleTexturePath));
        exit1=moduleNode->GetChild("exit1", true);
        exit1Pos=exit1->GetWorldPosition();
        exit1PosX=exit1Pos.x_;
        exit1PosY=exit1Pos.y_;
        exit1PosZ=exit1Pos.z_;
[/code]

thanks again.

-------------------------

