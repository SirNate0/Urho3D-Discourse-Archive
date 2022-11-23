TikariSakari | 2017-01-02 01:04:31 UTC | #1

I was thinking about some optimization for my project. I should be writing game instead of thinking bottle necks. Anyways I have been testing random things, like what causes performance to drop, and I've come to realise that animated models are one.

So I was thinking if I could for example make it so that it would update the animation so that in frame 1 it would update half of the models, and on frame 2 second half. I kind of noticed that what truly happens is, that even if the models aren't updating at all, it still requires the whole bone structure to be rendered, and thus the performance gain was a lot less than I actually thought on models where nothing was updated on a frame.

Then I tried to make it so that on every unit node, I add one static mesh, and one animated mesh. I made a button that when I press it, it enables the static mesh, and disables the animated model. On my Nexus 5, the fps jumps quite a lot, since most of my meshes have roughly 20 bones. The fps is roughly ~15 on ~900 animated models and it jumps up to 50, with the enabling of static mesh, and disenabling animated meshes. The model then uses the staic pose.

So I was wondering if there is something in animated model to actually do this by just giving command like useStatic(true); which would kind of make the mesh static until we call useStatic(false). This is, because it seems kind of a waste to actually load same mesh 2, well actually 3 times on same node. The third mesh is for my outlines, which is probably terrible way to do things, since it still adds extra pass and makes controlling stuff hard, maybe one day I will figure out how to properly write a shader.

I guess the changing of animated mesh to a static mesh would be something like LOD kind of implementation for animated skeletons. Would it be possible to have different skeletons on a single mesh or would the system have to be something like I have made, where you'd have an array of meshes, then it picks one, enables it and disables the other ones. It would pick the correct mesh based on distance or something. This also makes me wonder if blender has something like skeletal lods. Also I wonder if this would be expensive in memory wise.

Edit: I figured making a "picture" would probably give better view.

[code]
Unit-node
  StaticMesh (disabled)
    StaticOutlineMesh(disabled)
  AnimatedMesh(enabled)
    AnimatedOutlineMesh(enabled)
[/code]
After the swap:
[code]
Unit-node
  StaticMesh (enabled)
    StaticOutlineMesh(enabled)
  AnimatedMesh(disabled)
    AnimatedOutlineMesh(disabled)
[/code]
So I was wondering if there is a way to use only one mesh and somehow use different levels of skeletons or something. To combine the outlinemesh to parent mesh, I would have to have better understanding about shaders and the techniques, and do some shader stuff. It also creates extra pass, since my outline shader is using opposite culling.

-------------------------

TikariSakari | 2017-01-02 01:04:32 UTC | #2

I guess this is what I get from writing something just before going to sleep. I know that the 900 animated models, which after waking up I am using 25*25 = 625 animated models, which consists of 4 different characters, and 1 of the 4 characters has 2 models (body and clothes). So the amount of models would then be 625 * 5 / 4 ? 780.

The 780 models is probably 20 times more than I would ever need to use, and on my phone it runs perfectly fine 60 fps even with over 100 animated models (roughly 1000 faces, 20 bones per model). This is actually more than enough in terms of performance, but I am not expecting every phone to be as fast as my nexus 5.

This is on desktop:
Why I was asking about lod for skeletons is because at least on my test, if you have animated model with 20 bones and opengl3 or my phone which uses opengl2es, regardless if I animate it or not, there is almost no performance difference. This probably also means that I become gpu bound. On opengl2, the urho there seems to be lot less gained between having a model static vs animated. I noticed that I became cpu bound, and it was running roughly 100 fps, 72% gpu usage and with static models 168fps, 100% gpu usage. So if I count 168 * 0.72 ? 120 fps, which would be like 20% increase, which might not mean much as a number, considering its also freeing cpu usage. On a side note, things generally did run a lot faster on my setup using opengl2 than 3, but I suppose opengl3 leaves more cpu power to do other things.

On another side note, I am guessing that for current phones (android at least?), I can assume that phones when rendering 3D will almost always be more likely to be GPU bound than CPU bound. Considering a lot of em are quad core 2+ghz CPUs, and the GPU is probably a lot less powerful than CPUs. Although I have no idea what kind of performance 

With example on desktop same scene, same models one where I have same model as static mesh and other as a animated mesh. Without instancing there was still almost 200% fps gain when changing the animated models to static ones. What I noticed is that with high amount of models animated models, I started to become cpu bound. I have honestly never seen so high usage of cpu in any game as I've seen on Urho (something to notice though I am not exactly running a game, just graphics rendering currently), although I haven't used linux more than a month, so maybe it is a linux vs windows thing as well (on 6 core system 50% cpu usage). I gained 50% fps when I stopped animating the models, but what I did notice is that when I was animtaing the models, my gpu usage was 66%, and when I stopped animating them, it went to 100%. This would pretty much explain the 50% gain, to become gpu bound. So I guess with opengl3 the gpu usage is same or pretty close to same regardless if the animation is running or not, but cpu usage is a lot lower.

This made me think, although I havent tested, how would a character with different skeletons work. Like if I had one version where whole arm = 1 bone, leg = 1 bone, so arms + legs = 4 bones and then spine and head, so there would be like 6 control bones + root bone. Surely you cannot control the character so well with less bones, but I would assume it would free up some gpu.

The project that I hopefully will eventually get on to would be tactical rpg or something. There seems to be one similar one [url]http://discourse.urho3d.io/t/my-project-wip/818/1[/url]. Basically doing something similar as Setzers. From his video you can see that the other character stands still, which I figured in my case could be static mesh, then when selecting the unit, it would swap into animated one to save some frames with phone.

Also I do think that I might be going too much of trying to optimize things that aren't exactly neccessary. Then again I am very noobish and have almost 0 knowledge about 3d, so its been kind of testing stuff for the past few months. This means that I might be looking at completely wrong kind of things to begin with. When I first thought about 3D on mobile phones, I thought I could just dump just about anything on the screen and phones would today be fast enough to handle it, but I guess I have proved myself that it is very wrong to assume such.

Edit forgot to put the code for the creating of animated node. It is using pretty much sample 06 with just compounding several different models on one node.
[code]
Urho3D::Node* MainGame::addAnimatedModel( Urho3D::Node* node, Urho3D::String nodeName, Urho3D::String folder,
        Urho3D::String modelName, Urho3D::String matName, Urho3D::String animName, bool createOutline ) {

    Urho3D::ResourceCache* cache = GetSubsystem<ResourceCache>();

    if( folder.Length() > 0 )
        folder += "/";

    modelName = folder + modelName;
    matName = folder + matName;
    animName = folder + animName;

    Urho3D::Node* modelNode = node->CreateChild( "GameUnit_Node_" + nodeName);

    Urho3D::Node* modelDynamicNode = modelNode->CreateChild( "GameUnit_Dynamic_" + nodeName);
    Urho3D::Node* modelStaticNode = modelNode->CreateChild( "GameUnit_Static_" + nodeName);

    createAnimatedModel( modelDynamicNode, modelName, matName, animName );
    createStaticdModel( modelStaticNode, modelName, matName );


    // Create outline
    if( createOutline )
    {
        Urho3D::Node* modelStaticOutlineNode = modelStaticNode->CreateChild("GameUnit_Outline");
        createAnimatedModel( modelDynamicNode->CreateChild("GameUnit_Outline"), modelName, "Materials/OutlineMat.xml", animName );
        createStaticdModel( modelStaticOutlineNode, modelName, "Materials/OutlineMat.xml" );
        modelStaticOutlineNode->SetEnabled(false);
    }

    modelStaticNode->SetEnabled(false);

    return modelNode;
}

void MainGame::createStaticdModel( Urho3D::Node* node,
        Urho3D::String modelName, Urho3D::String matName )
{
    Urho3D::ResourceCache* cache = GetSubsystem<ResourceCache>();
    Urho3D::StaticModel* modelObject = node->CreateComponent<Urho3D::StaticModel>();
    modelObject->SetModel(cache->GetResource<Urho3D::Model>(modelName));
    modelObject->SetMaterial(cache->GetResource<Urho3D::Material>(matName));
}

void MainGame::createAnimatedModel( Urho3D::Node* node,
        Urho3D::String modelName, Urho3D::String matName, Urho3D::String animName )
{
    Urho3D::ResourceCache* cache = GetSubsystem<ResourceCache>();

    Urho3D::AnimatedModel* modelObject = node->CreateComponent<Urho3D::AnimatedModel>();

    modelObject->SetModel( cache->GetResource<Urho3D::Model>( modelName ) );
    modelObject->SetMaterial( cache->GetResource<Urho3D::Material>( matName) );

    Animation* animation = cache->GetResource<Urho3D::Animation>( animName );
/*
    if (animation) {
        Urho3D::AnimationState* state = modelObject->AddAnimationState(animation);
        // The state would fail to create (return null) if the animation was not found
        if (state)
        {
            // Enable full blending weight and looping
            state->SetWeight(1.0f);
            state->SetLooped(true);
        }

        // Create our custom Mover component that will move & animate the model during each frame's update
        node->CreateComponent<Mover>();
    }
*/
}

void MainGame::enableDisableAnimationsOnNode( Urho3D::Node* node )
{
    Urho3D::Node* child;
    const Vector<SharedPtr<Node>>& children = node->GetChildren();
    for( unsigned int j = 0; j < children.Size(); ++j )
    {
        child = children[j];

        if( child->GetName().Substring(0,14) == "GameUnit_Node_")
        {
            enableDisableAnimationsOnNode( child );
        }
        else
        {
            bool enabled = !child->IsEnabled();
            child->SetEnabled( enabled );
            if( auto* c2 = child->GetChild("GameUnit_Outline") )
                c2->SetEnabled( enabled && bShowOutline_ );
        }
    }

}


[/code]
If I uncomment the adding animation thing as in truly add animation to the animated model, the performance gain is there, but it isn't really that good with opengl3, but if I use static models instead of animated ones, I get almost 200% fps boost, while on both cases gpu utilization is close to 100%.

-------------------------

codingmonkey | 2017-01-02 01:04:32 UTC | #3

>but if I use static models instead of animated ones, I get almost 200% fps boost

1. try to update your animation on FixedUpdate() and not on Update() (on each frame)
2. try to increase delta time twice for far objects. Something like this I guess - { if (elapsedTime > (timeStep*2)) AnimationState.AddTime(timeStep*2) }  
In this case you get same poses on far and near objects but far objects moves more discrete and no so often update.   

3. for high distanced units from camera you may create something like Imposter System on Billboards components with animated sprites (they must be prebaked into texture, all action of model )

-------------------------

TikariSakari | 2017-01-02 01:04:33 UTC | #4

[quote="Sinoid"][quote]but I am not expecting every phone to be as fast as my nexus 5.[/quote]

Got a test APK sitting about with around the number of models you need? I'll slap it on an old Samsung Stratosphere (first version, gles2 with a lying bastard of a depth buffer) and report what happens - such is it's sole purpose. Should be older than anything you'll need to worry about (aside from super cheap 'tract phones).[/quote]

Sorry took me a bit of a time. I created new model for the test, which looks as bad as all the other ones I've made. Also I figured out creating the project a bit more test like I suppose, something to try to find limits easier, so one can add more models by press of a button, swap the models from 23 bone version to 7 bone or static ones.

[url]https://www.dropbox.com/s/89hxjkrvlqalxtf/Tiskaria3D_Test.apk?dl=0[/url]

Despite I did make a new model, most likely I will end up using it on my own project, even tho it is not that good. So I shall not give my permission to rip it off from the apk and use it on ones own project. Just being cautious since I am giving link for the dl, and since the forums are public meaning anyone reading the forums can dl it, despite if they use urho or not.

It starts with 16 models, and I figured as long as it runs well with 48 models all should be well. You can add one row of characters per press of a button. They do not need to be outlined tho, since that counts pretty much same as having 96 models. There are several choices of models, like 23 bone version, then 7 bone and finally static model, which is loaded from the 23 bone version.

The outline thing basically creates extra model on top of each model, that is scaled and using counter clockwise rendering. In other words it basically means that each model counts as 2 models + it creates extra pass on each model.

The pause is suppose to stop any animation happening as in still models, but it might not be correctly coded. Basically in my case there is no diffenece if characters are moving or not, and from my tests with desktop it only saves cpu time, but since my phone is gpu bound, there is no difference.

Then there are static models that can be tested against moving ones.

I tried to remove most extra stuff from the packet. I didn't remove the extra stuff it compiles against tho, like it does have net, navigation etc.

I removed all the permissions from the android manifest and renamed the package so it should not conflict with other packages hopefully.

Edit: Forgot to mention: you can move around with dragging one finger, and rotate by using 2 fingers. The zoom is the bar at the bottom instead of using 2 fingers to zoom like normally.

Edit2: Just to point out, all the models use exactly same base mesh, meaning same amount of faces and triangles. With opengl2 the pause vs static models have quite minor difference, but with opengl3 and opengles2 at least on my computer / phone, there is quite a big difference on performance depending if its animatedmodel or staticmodel. Also it could mean that I am not truly stopping the animation from happening, but this difference exists even if I set skeletons boneanimation to false, and never add any animations to the object.

-------------------------

