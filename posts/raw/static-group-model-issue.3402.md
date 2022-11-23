zedraken | 2017-07-31 17:15:31 UTC | #1

Hello guys,

I am experiencing the use of the _StaticModelGroup_ class. My goal is to create and display several gates from one unique model file called "Models/Gate.mdl".

Here is the code snippet I use : 

    Node *gatesGroupNode = mScene->CreateChild("GatesGroup");
    StaticModelGroup *group = gatesGroupNode->CreateComponent<StaticModelGroup>();
    group->SetModel(mResourcesCache->GetResource<Model>("Models/Gate.mdl"));

    for(int index = 0; index < 20; index++)
    {
        LOGINFO("Creating gate node n°" + String(index));
        Node *gateNode = mScene->CreateChild("Gate");
        gateNode->SetPosition(Vector3(index * 10, 0, index * 10));
        group->AddInstanceNode(gateNode);
    } 

When I execute that code, I see no gates displayed while in my debug window, I see the message:
"Creating gate node n°0"
…

If I set the number of gates to create to 1 in the _for_ loop, meaning that I only create one single gate, it works fine. I see the unique gate displayed in my view port. 
The code seems to be quite correct and it works for one gate. But it does not work for more that one (2, 3, and more).

I am turning around and for the moment, I cannot figure out what is wrong with my code. Or maybe I forgot something ?

I am very interested if you might have some ideas that can help me solve that issue.

For information, my code is inspired from the sample HugeObjectCount provided in Urho3D engine. Such example works fine, but not mine :frowning_face: and I do not really see the differences between both programs.

Thanks a lot in advance for your answers.

Regards.

-------------------------

Dave82 | 2017-07-31 20:53:18 UTC | #2

Instead of using your gate.mdl , try using one the Urho's default models (box.mdl , cone.mdl , cylinder.mdl , etc) and see if it works with those models.If it works , it means something is wrong with your gate model.

-------------------------

zedraken | 2017-08-01 06:41:46 UTC | #3

Hi Dave,

thanks for your suggestion. I gave it a try with some objects : Box, Cone, Cylinder, … but the result is always the same. If I add only one node in the group, it is properly displayed. Otherwise, I do not see anything.
I have added printing of some debug message each time I create a node in my _for_ loop and here is what I get : 

    Creating gate node n°0
    Group number of occluders : 62
    Group number of instances : 1

    Creating gate node n°1
    Group number of occluders : 124
    Group number of instances : 2

    Creating gate node n°2
    Group number of occluders : 186
    Group number of instances : 3

    Creating gate node n°3
    Group number of occluders : 248
    Group number of instances : 4

Every new node seems to be properly created and added into the group. The number of instances within the group is incremented by one each time a new node is added, and this is also the case of the number of occluders.

So, what's wrong ????? This is really making me crazy :stuck_out_tongue_winking_eye:

Any clue that can help me solving that situation is welcome. In the mean time, I keep trying to check what are the differences between the _HugeObjectCount_ demo (which works !) and my program.

Thanks !

-------------------------

zedraken | 2017-08-01 07:28:12 UTC | #4

As Slapin suggested in another post, I disabled the "dynamic instancing" in my _Start()_ function, like this : 

    Renderer *rdr = GetSubsystem<Renderer>();
    rdr->SetDynamicInstancing(false);

And now all the nodes (of the same model) added to the group are correctly displayed !

Do you think that there might be some issues with "dynamic instancing" and some graphic drivers ?

-------------------------

cadaver | 2017-08-01 07:54:00 UTC | #5

It's highly likely that Urho and some graphics drivers interact in a way that cause this bug. May be an actual error in Urho code, but on e.g. Nvidia cards (and older Intel) I haven't been able to reproduce. Realistically, this probably needs someone with the issue occurring to debug it and post a fix to the renderer internals, if possible.

-------------------------

Victor | 2017-08-01 08:06:21 UTC | #6

Would using the Graphics::GetInstancingSupport be the proper solution for setting the DynamicInstancing flag?

https://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_graphics.html#a373ed5634fcb256cd309f844d19c3aa4

-------------------------

zedraken | 2017-08-01 08:28:41 UTC | #7

Thanks for the tip. 
In my code, I first check for HW instancing capabilities, and I disable dynamic instancing depending of the capabilities.
So, I added the following line in my _Start()_ function: 

`GetSubsystem<Renderer>()->SetDynamicInstancing(GetSubsystem<Graphics>()->GetInstancingSupport());`

And it seems to do the trick.

As I expected, my hardware (_nVidia GeForce GTX660_) does not support dynamic instancing.

-------------------------

cadaver | 2017-08-01 08:47:46 UTC | #8

No, the engine should refuse to erroneously enable instancing if not supported. However, GetInstancingSupport() check is for ancient hardware and mostly not relevant anymore, except for mobiles & web, as on desktops it should always be true and we have already dropped Shader Model 2 support (on which it could be false.) So on a desktop machine, that particular error is something else; not GetInstancingSupport() being false.

EDIT: will have to review this a bit. The renderer allows instancing to be enabled even without support, but it should later understand this situation and not attempt to actually render instanced. This is probably not a good idea, as it makes the code more fragile / errorprone.

-------------------------

Victor | 2017-08-01 08:39:27 UTC | #9

Gotcha, good to know! :)

@zedraken Looks like your nvidia card should support 4.5: https://www.techpowerup.com/gpudb/895/geforce-gtx-660 (opengl) DirectX: 12.0, Shader Model 5.0**

-------------------------

Victor | 2017-08-01 08:41:24 UTC | #10

I guess, what's weird about this issue is that the StaticGroupModel example in the HugeObjectCount works fine for you... So you definitely have support now that I think about it. Very odd :(

-------------------------

cadaver | 2017-08-01 08:43:40 UTC | #11

It could also be something like that the instancing is in a bad shape initially (for some reason), but calling Renderer::SetDynamicInstancing() again recreates the instancing vertex buffer and fixes it.

-------------------------

zedraken | 2017-08-01 08:49:32 UTC | #12

If I force a call to: 

`GetSubsystem<Renderer>()->SetDynamicInstancing(true);`

in my _Start()_ function, hoping it will set to a stable known internal state, it does not work anymore, on final.

I guess the issue I have has something to deal with my hardware. Since I have other computers at home (with different hardware) I will check for the issue on them.

-------------------------

zedraken | 2017-08-01 08:50:39 UTC | #13

Or maybe it is a good opportunity to update my graphic card to a more recent one ? :grin:

-------------------------

zedraken | 2017-08-01 08:53:31 UTC | #14

Thanks for the link. My graphic card is definitely an old one... But it works (almost) fine !

-------------------------

cadaver | 2017-08-01 08:58:41 UTC | #15

It could be a bad driver. Instancing was supported since SM3.0.

-------------------------

cadaver | 2017-08-01 14:40:09 UTC | #16

Ok. Reviewed the code. At least just manually setting instancingsupport to false in Graphics caused the rendering to happen correctly without instancing.

-------------------------

cadaver | 2017-08-02 06:48:56 UTC | #17

One more thought regarding this, if you were to call GetSubsystem<Graphics>()->GetInstancingSupport() before the window is opened and the graphics context exists, it would return always false. However, this should not be the case when the Engine & Application classes are used normally, since the Start() would be executed when the engine is initialized and the window is already open.

-------------------------

zedraken | 2017-08-05 06:58:48 UTC | #18

Hi cadaver,

thanks for those explanations. I check for dynamic instancing support in the _Start()_ function so I assume that it is the right place to do that as you said.
I also tried my application on another computer running a _Linux Mint_ distro, with a GeForce GTS450 graphic board (an old one ;)), and with the nvidia driver 375.66.
The _GetInstancingSupport()_ returns true but I still have to force Dynamic Instancing to false in order for my objects to be properly displayed, otherwise it does not work (nothing is displayed).
For information, I compiled my app against the latest development release of Urho3D (the _git clone_ was done yesterday).

-------------------------

cadaver | 2017-08-05 17:16:50 UTC | #19

Could you publish the model somewhere, or send to loorni@gmail.com? I could test if it's a combination of vertex attributes that is not encountered with the Urho default models, and which breaks Urho's handling of instancing attributes on OpenGL, regardless of the driver.

-------------------------

zedraken | 2017-08-06 04:43:15 UTC | #20

Do you mean the Blender file or directly the .mdl file ? Which one is the most useful for debugging ?
Or maybe I can prepare an archive with both…

-------------------------

