nicos | 2017-01-02 01:10:07 UTC | #1

Hi !
I still work on my avatar project for puppet show. Urho3D is a great Engine, I become in love with it  :smiley: 
For those who doesnt know what I'm talking about : [url]http://discourse.urho3d.io/t/serial-input/1732/1[/url].
The head rotation works nice now, I made an 'Avatar' LogicComponent with it. I found a lot of help in samples, almost Vehicle Sample. We'll have some differents 'Avatars' to use, and I though I can save some attributes in XML format (maybe a UI, if I have enough time...) so as to work easily with puppeteer and art director on stage.

I'ld like to know how I can clamp bones rotations. I tried some stuff with Urho3D::Clamp function, but I think I don't really understand how it works.  :blush: 
I saw, in Vehicle sample , another way by adding constraints with the physic engine. But I'm not sure I need to code with physics for this project.

What do you think about it ?

Thanks to all, have a nice day (or night, I think there's poeple from all over the world here...)

-------------------------

Modanung | 2017-01-02 01:10:26 UTC | #2

Did you have a look at the [url=https://github.com/urho3d/Urho3D/blob/c4f6f315ff5b6ea992340780521d3e5f2e668b11/Source/Samples/13_Ragdolls/CreateRagdoll.cpp]ragdoll sample[/url]?

-------------------------

gawag | 2017-01-02 01:10:28 UTC | #3

I had a project with a plane and used bones to control the flaps:
[code]
    Urho3D::Node* node_flap_l;
    Urho3D::Node* node_plane;
    float flaps=0;
    ...
    node_plane=scene_->CreateChild("plane");
    AnimatedModel* plane=node_plane->CreateComponent<AnimatedModel>();
    plane->SetModel(cache->GetResource<Model>("plane/plane.mdl"));
    node_flap_l=node_plane->GetChild("flap.L",true);    // the bone is called flap.L
    // if you are using animations you may want to disable them for the
    // manually controlled bones:
    plane->GetSkeleton()->GetBone("flap.L")->animated_=false;
    ...
    // in the update function:
    if(input->GetKeyDown(KEY_F))
        flaps+=timeStep*20;
    if(input->GetKeyDown(KEY_R))
        flaps-=timeStep*20;
    flaps=Clamp(flaps,0.0,60.0);             // keep the flap angle between 0 and 60
    node_flap_l->SetRotation(Quaternion());             // reset the rotation
    node_flap_l->Yaw(flaps);                            // yaw the bone
...
[/code]
I don't know if there's an automatic way to keep a bone in a certain angle range. If you move them manually though like I did there pretty straight forward.

-------------------------

