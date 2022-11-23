codingmonkey | 2017-01-02 01:07:51 UTC | #1

Hi folks!
I try to figure to how to get depth texture (and send it to texture unit for shader lookup) of rendered frame for post-process (such as DOF) but in Forward.xml render path.
Any ideas?
Previously, I tried to use ForwardHWDepth.xml for other things but I guessing that this renderpath have some kind of visual bugs or something like this.

-------------------------

cadaver | 2017-01-02 01:07:51 UTC | #2

If you want most compatibility, use the ForwardDepth.xml renderpath, which doesn't use a true hardware depth buffer. Instead it will render the scene twice to also render depth to a linear buffer (similar to the default deferred & prepass paths). Rendering twice will naturally cost performance.

-------------------------

codingmonkey | 2017-01-02 01:07:51 UTC | #3

>If you want most compatibility
I want max performance.

I take a look closer into two renderpath and find that 
ForwardHWDepth use 
    <rendertarget name="depth" sizedivisor="1 1" format="readabledepth" />

and ForwardDepth
<rendertarget name="depth" sizedivisor="1 1" format="lineardepth" />

is it mean that "readabledepth" 
- it's "true" depth? 
- is it possible read in PS shader ? (any example how to put this depth into TU ? (I guessing it use d24 format and not rgb(a))) 
- is it render scene in single pass or similar to lineardepth twice?

-------------------------

cadaver | 2017-01-02 01:07:52 UTC | #4

If you want max performance, then the HWDepth family of renderpaths is the only way to go. They use a D24 format hardware depth buffer (the one that is actually used for Z tests). The path instructs to use it as the depth-stencil buffer in all subsequent passes, which means the scene won't be rendered twice. If you're on OpenGL, it disables attempting to use a D24S8 format for compatibility reasons, so it's just bare D24 and stencil won't be available, which disables some optimizations.

When reading the D24 depth buffer in pixel shader, you need to use ReconstructDepth() function. Look at the DeferredLight & PrepassLight shaders for an example. Also, when you read the depth buffer, depth write needs to be off in materials (in postprocess quad rendering it's always off).

-------------------------

codingmonkey | 2017-01-02 01:07:52 UTC | #5

Thanks, Lasse.
I use this whitepaper from AMD: Scheuermann_DepthOfField.pdf
in part of whitepaper when need save depth in alpha channel
[url=http://savepic.su/6300547.htm][img]http://savepic.su/6300547m.png[/img][/url]

and I guessing that I need convert(do mapping) cNearClipPS and cFarClipPS(they store world-space values?) into depth range, how I may do this ?
In what range the fn ReconstructDepth() converts depth range [0..1] or [-1..1] or ...?

-------------------------

cadaver | 2017-01-02 01:07:52 UTC | #6

The value returned by ReconstructDepth is such that nearclip distance equals 0 and farclip distance equals 1, and the values inbetween are linearly mapped. So it only undoes the hyperbolic part of the depth mapping.

-------------------------

friesencr | 2019-05-27 17:25:07 UTC | #7

[quote="codingmonkey"]
Thanks, Lasse.
I use this whitepaper from AMD: Scheuermann_DepthOfField.pdf
in part of whitepaper when need save depth in alpha channel
[url=http://savepic.su/6300547.htm][img]http://savepic.su/6300547m.png[/img][/url]

and I guessing that I need convert(do mapping) cNearClipPS and cFarClipPS(they store world-space values?) into depth range, how I may do this ?
In what range the fn ReconstructDepth() converts depth range [0..1] or [-1..1] or ...?
[/quote]

I heard someone doing deferred in webgl by using the alpha channel.

-------------------------

codingmonkey | 2019-05-27 17:26:25 UTC | #8

>I heard someone doing deferred in webgl by using the alpha channel.
I guessing this almost oldest tech (from 2004 year) and maybe someone using parts of this doc from amd.

now  I have some crappy results
[url=http://savepic.su/6306740.htm][img]http://savepic.su/6306740m.png[/img][/url]
[url=http://savepic.su/6337463.htm][img]http://savepic.su/6337463m.png[/img][/url]

in whitepaper written "use destination alpha for depth and blur information" they mean use low-res destination or full-res destination ?
anyway for testing purpose. I use special RT only for save full-res depth into alpha )
and I do not figure out with cameras clip planes (near/far/focal) and hardcode they in shader for while 


[details="Render Path"]
[code]
<renderpath>
    <rendertarget name="blurredFrameH" tag="DOF" sizedivisor="8 8" format="rgba" filter="true" />
    <rendertarget name="blurredFrameV" tag="DOF" sizedivisor="8 8" format="rgba" filter="true" />
    
    <rendertarget name="storedAlpha" tag="DOF" sizedivisor="1 1" format="rgba" filter="true" />
      
    <rendertarget name="depth" sizedivisor="1 1" format="readabledepth" />
    <command type="clear" depth="1.0" output="depth" />
    <command type="scenepass" pass="shadow" output="depth" />
    <command type="clear" color="fog" depthstencil="depth" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" depthstencil="depth" />
    <command type="forwardlights" pass="light" depthstencil="depth" />
    <command type="scenepass" pass="postopaque" depthstencil="depth" />
    <command type="scenepass" pass="refract" depthstencil="depth">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" depthstencil="depth"  />
    <command type="scenepass" pass="postalpha" sort="backtofront" depthstencil="depth" />
    
    <command type="quad" tag="DOF" vs="CopyFramebufferDof" ps="CopyFramebufferDof" blend="replace" output="storedAlpha">
        <texture unit="0" name="viewport" />
        <texture unit="depth" name="depth" />
    </command> 
        
    <!-- Blur passed  -->    
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR5" output="blurredFrameH">
        <parameter name="BlurDir" value="1.0 0.0" />
        <parameter name="BlurRadius" value="4.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="viewport" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR5" output="blurredFrameV">
        <parameter name="BlurDir" value="0.0 1.0" />
        <parameter name="BlurRadius" value="4.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="blurredFrameH" />
    </command> 
      
    <!-- DOF process -->
    <command type="quad" tag="DOF" vs="DepthOfField" ps="DepthOfField" blend="replace" output="viewport">
        <texture unit="0" name="blurredFrameV" />
        <texture unit="1" name="viewport" />
        <texture unit="2" name="storedAlpha" />
    </command>

        
    
</renderpath>
[/code]
[/details]


update:
- add center focus

https://www.youtube.com/watch?v=x0nuRlWoqq4

-------------------------

codingmonkey | 2019-05-27 17:27:06 UTC | #9

I have a strange bug, even i use the same RenderPath in Editor and my project for testing.
if you look into this pictures they are have a different blurriness and dof
the first image from editor view
[url=http://savepic.su/6316904.htm][img]http://savepic.su/6316904m.png[/img][/url]
and second image from compiled project (from camera)
[url=http://savepic.su/6330216.htm][img]http://savepic.su/6330216m.png[/img][/url]

why this happening? as I say before, this is the same renderpath (on gl renderer) it's look likes not all command from renderPath are executed (in case using of test app)


[details="current render path"]
[code]
<renderpath>
    <rendertarget name="blurredFrameH" tag="DOF" sizedivisor="4 4" format="rgba" filter="true" />
    <rendertarget name="blurredFrameV" tag="DOF" sizedivisor="4 4" format="rgba" filter="true" />
    <rendertarget name="stored" tag="DOF" sizedivisor="1 1" format="rgba" filter="true" />
    <rendertarget name="depth" sizedivisor="1 1" format="readabledepth" />
    <command type="clear" depth="1.0" output="depth" />
    <command type="scenepass" pass="shadow" output="depth" />
    <command type="clear" color="fog" depthstencil="depth" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" depthstencil="depth" />
    <command type="forwardlights" pass="light" depthstencil="depth" />
    <command type="scenepass" pass="postopaque" depthstencil="depth" />
    <command type="scenepass" pass="refract" depthstencil="depth">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" depthstencil="depth" />
    <command type="scenepass" pass="postalpha" sort="backtofront" depthstencil="depth" />
    <command type="quad" tag="DOF" vs="CopyFramebufferDof" ps="CopyFramebufferDof" blend="replace" output="stored">
        <texture unit="0" name="viewport" />
        <texture unit="1" name="depth" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurredFrameH">
        <parameter name="BlurDir" value="1.0 0.0" />
        <parameter name="BlurRadius" value="4.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="0" name="stored" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurredFrameV">
        <parameter name="BlurDir" value="0.0 1.0" />
        <parameter name="BlurRadius" value="4.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="0" name="blurredFrameH" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurredFrameH">
        <parameter name="BlurDir" value="1.0 0.0" />
        <parameter name="BlurRadius" value="2.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="0" name="blurredFrameV" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurredFrameV">
        <parameter name="BlurDir" value="0.0 1.0" />
        <parameter name="BlurRadius" value="2.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="0" name="blurredFrameH" />
    </command>
    <command type="quad" tag="DOF" vs="DepthOfField" ps="DepthOfField" blend="replace" output="viewport">
        <texture unit="0" name="blurredFrameV" />
        <texture unit="1" name="stored" />
    </command>
</renderpath>
[/code]
[/details]

repo with current version
[github.com/MonkeyFirst/urho3d-post-process-dof](https://github.com/MonkeyFirst/urho3d-post-process-dof)

-------------------------

codingmonkey | 2019-05-27 17:27:30 UTC | #10

Today I do some checking of what the RaycastSingle really do, then it hit something on scene, and I found strange bug - the invisible barrier.
I don't know that is this, but actually I suspect what I will hit the big rock on far distance and not this "invisible wall"
Is this normal working? Or maybe I doing something wrong?

As always, I make video with this bug.
And I want to mention that Raycast also hit this wall but second hit(on path of ray) and others hits works well
https://www.youtube.com/watch?v=fT80yd_xKg0

[code]
			Ray ray = camera->GetScreenRay(0.5f, 0.5f);

			PODVector<RayQueryResult> results;
			RayOctreeQuery query(results, ray, RAY_TRIANGLE, 1000.0f, DRAWABLE_GEOMETRY, -1);

			Octree* octree = gameScene->scene->GetComponent<Octree>();
			//octree->RaycastSingle(query);
			octree->Raycast(query);

			if (results.Size())
			{
				for (unsigned int i = 0; i < results.Size(); i++)
				{
					RayQueryResult& result = results[i];

					Vector3 hitNormal = result.normal_;
					Vector3 hitPoint = result.position_;

					Node* node= gameScene->scene->InstantiateXML(cache->GetResource<XMLFile>("Objects/hitPrefab.xml")->GetRoot(), hitPoint, Quaternion::IDENTITY, LOCAL);
					node->SetScale(Vector3::ONE * 0.2f);

					Pair<Vector3, Vector3> line;
					line.first_ = hitPoint;
					line.second_ = hitPoint + hitNormal * 2.0f;
					lines.Push(line);
				}				
			}
[/code]

-------------------------

codingmonkey | 2017-01-02 01:08:00 UTC | #11

needs more rays shots to see this "barriers"
[url=http://savepic.su/6401835.htm][img]http://savepic.su/6401835m.png[/img][/url]

I guessing it's some kind of boundbox from other StaticModel - "Trees". 
But actually why Raycast hit'ing this BB if for my need only triangle-level Ray casting?


Aslo I found what Raycast maybe used in separated thread (with workers) but RaycastSingle not (:
This two issue passible to fix ?

-------------------------

codingmonkey | 2017-01-02 01:08:00 UTC | #12

Thanks Jonathan, for pointing about IDs.
I tried to look into it, and find what I always hitting the "Trees" - Animation Model. 
My Trees have 4-bones for wind animation, and in this case I guessing what this is the bone's bound boxes.
[url=http://savepic.su/6388538.htm][img]http://savepic.su/6388538m.png[/img][/url]
[url=http://savepic.su/6374202.htm][img]http://savepic.su/6374202m.png[/img][/url]

Actually I do not needed hitting bones ) Only actual transformed triangles.
Is it possible ignore those animation bones on Raycast query ? 
I guessing maybe also need to add additional flags for RayOctreeQuery(results, ray, RAY_TRIANGLE | IGNORE_BONES, 1000.0f, DRAWABLE_GEOMETRY, -1)

-------------------------

thebluefish | 2017-01-02 01:08:00 UTC | #13

I'm concerned that it would return a result on a bounding box alone since you're using RAY_TRIANGLE. It should only be doing that on RAY_AABB or RAY_OBB.

I would consider classifying that as a bug.

-------------------------

thebluefish | 2017-01-02 01:08:00 UTC | #14

Alternatively set every bone to BONECOLLISION_NONE. That way the bones themselves won't collide with anything.

-------------------------

codingmonkey | 2017-01-02 01:08:01 UTC | #15

>Here's a quick change
Great, there is what I got on debug draw after adding this fixes. On picture only tree's bones.
[url=http://savepic.su/6409084.htm][img]http://savepic.su/6409084m.png[/img][/url]
[url=http://savepic.su/6370160.htm][img]http://savepic.su/6370160m.png[/img][/url]

> Where'd you export the model from?
I use Blender-Urho exporter. Do you think what it may have a bone's BB bug?

>Alternatively set every bone to BONECOLLISION_NONE. That way the bones themselves won't collide with anything.
Thanks, i'm trying this, but it still no working properly. The rays still hit bb of bones (or what is this maybe).
there is my code, where I turn-off bones collision for all animatedModels

[code]
	void SetupAnimatedModel() 
	{

		Skeleton sk;
		Node* nSenua = gameScene->scene->GetChild("cs_senua", true);

		csSenua = nSenua->GetComponent<AnimatedModel>();
		csSenuaState = csSenua->GetAnimationState(StringHash("cutscene"));

		sk = csSenua->GetSkeleton();
		for (int i = 0; i < sk.GetNumBones(); i++)
		{

			Bone* bone = sk.GetBone(i);
			bone->collisionMask_ = BONECOLLISION_NONE;
		}
	

		Node* nWoods = gameScene->scene->GetChild("cs_woods", true);
		csWoods = nWoods->GetComponent<AnimatedModel>();
		csWoodsState = csWoods->GetAnimationState(StringHash("TreesWindAnimation"));

		sk = csWoods->GetSkeleton();
		for (int i = 0; i < sk.GetNumBones(); i++)
		{

			Bone* bone = sk.GetBone(i);
			bone->collisionMask_ = BONECOLLISION_NONE;
		}

		Node* nCamera = gameScene->scene->GetChild("cs_camera", true);
		csCamera = nCamera->GetComponent<AnimatedModel>();

		sk = csCamera->GetSkeleton();
		for (int i = 0; i < sk.GetNumBones(); i++)
		{

			Bone* bone = sk.GetBone(i);
			bone->collisionMask_ = BONECOLLISION_NONE;
		}

		csCameraState = csCamera->GetAnimationState(StringHash("CameraAnimation"));
[/code]

-------------------------

codingmonkey | 2017-01-02 01:08:01 UTC | #16

I add some other fixes into debug renderer skeleton
change this
//AddBoundingBox(bones[i].boundingBox_, parentNode->GetWorldTransform(), Color::RED, true); //COMMENT OUT TO HIDE RED BOXES
to this
AddBoundingBox(bones[i].boundingBox_, bones[i].node_->GetWorldTransform(), Color::RED, true); //COMMENT OUT TO HIDE RED BOXES

and now it's more realistically represent of bone's BB placement
[url=http://savepic.su/6366071.htm][img]http://savepic.su/6366071m.png[/img][/url]

and hits are placed exact in same place as bb bones.

-------------------------

codingmonkey | 2017-01-02 01:08:01 UTC | #17

I add ignoring ability to ray query
[code]			RayOctreeQuery query(results, ray, RAY_TRIANGLE, 1000.0f, DRAWABLE_GEOMETRY, 1, RAY_IGNORE_BONES);
			Octree* octree = gameScene->scene->GetComponent<Octree>();
			octree->RaycastSingle(query);[/code]

with few fixes:
enum RayQueryIgnories
{
	RAY_IGNORE_NONE = 0,
	RAY_IGNORE_BONES
};

add to class RayOctreeQuery
	RayQueryIgnories ignore_;
field

and finally fix Animation class model in ProcessRayQuery()
[code]
    // Check ray hit distance to AABB before proceeding with bone-level tests
    if (query.ray_.HitDistance(GetWorldBoundingBox()) >= query.maxDistance_)
        return;

//CHANGE ->
	// Check before processing a bones, if set flag what allow to ignore bone's raycasting 
	if (ignore & RAY_IGNORE_BONES)
		return;
[/code]

Now Hitting the rock works fine, but all animated model not hitting at all (:
I think what need to do some major changes into AnimationModel to bring raycasting by actual transformed mesh no bones.
Is it store/save last frame (by physics tick) of Animated Model somewhere? 
Is it may in some case used for [u]triangle raycasting [/u] in main thread and workers?
I think I create an Issue for this soon.


update:
Actually I do not found any storing mechanism for transformed by bones AnimationModel. It may use only the Static Model if there no bones in it, thats all.
I found only nodes(bones) transformation by AnimationTracks, and I guessing that this nodes in second pass just put into shader uniforms as bones and thats all. No any actual geometry it's only math in vertex shader. And in this case I think there is have only one way to do actual raycasting use "[u]Transform Feedback[/u]" mechanism of Opengl or DX to do some kind of animation pre-pass not often(by physics tick) for all animated model in scene and grab their back to StaticModel for raycasting.  
and I think it's more complicated thing for me.

and other way to solve this (actually I thinks it's worst way to do this) - use more bones for each tree, even for branches. In this case we got many tiny bone's BB.  
But aslo in this case needed to add opportunity to exclude some of bones from RayCasting. In my case root bone of trees model, because it not represent any of scene model.

-------------------------

codingmonkey | 2019-05-27 17:28:04 UTC | #18

>Software skinning shouldn't be too terribly difficult. Everything is pretty much there and you have the last skin matrices.
I do not know much about this. 
But actually I mean GPU "Transform feedback skinning" for this. Is it possible on GL or DX in same time do animation transformation for model in VertexShader for frame Output and write transformed results into other output VertexBuffer(on Phys tick and less) to grab it then on CPU side into StaticModel ? I'm looked into this [open.gl/feedback](https://open.gl/feedback) and in this example they are do omnit output to frame then doing Transform feedback calculations.

Anyway I think after all this that animating the"trees on bones" are bad idea.
But in same time it's very handy to do animation for trees on the bones in Blender editor.
lastly I think there is exist another solution for this. - Use AttributeAnimation for Nodes(with rotation noise) with StaticModel(Trees) (leafs maybe animated with other material based shader)
But I will be great if we have possibility to get ValueAnimation from selected bone of Skeleton.

In mean this very handy way to getting VA from already existed animation file 
ValueAnimation va = Skeleton.GetValueAnimationFromBone("boneForTree4", GET_TRANSFORM_ROTATION, NORMALIZED or FULL_TIMED);
nodeForStaticModelWithTree->SetAttributeAnimation("Rotation", va, WrapMode::LOOP);

>If you only care about the trunks of the trees and not the branches you could just somehow adjust the bounds sizes in the model file.
I tried this

[code]	
	sk = csWoods->GetSkeleton();
		for (int i = 0; i < sk.GetNumBones(); i++)
		{
			Bone* bone = sk.GetBone(i);
			bone->collisionMask_ = BONECOLLISION_NONE;
			bone->boundingBox_.max_ *= Vector3(0.2f, 1f, 0.2f);
			bone->boundingBox_.min_ *= Vector3(0.2f, 1f, 0.2f);
		}
[/code]
but this not works, the boundaries are same as before

-------------------------

boberfly | 2017-01-02 01:08:02 UTC | #19

Just on a similar subject, today I learned that Unity3D does no GPU skinning with matrix palette out of the box, only CPU. It does however do transform feedback/stream out-style GPU skinning on GL(ES)3+/DX11 platforms if you enable it. Interesting.... Might be to alleviate them from a maintenance burden for shaders and bone limitations.

On the subject at hand, a possible solution could be if the bounding box gets hit, only do CPU skinning on the mesh that that bone's bbox belongs to, and then continue the raycast into that?

A library I've had my eye on for CPU skinning is this (for when GPU skinning doesn't cut it):
[code.google.com/p/ozz-animation/](https://code.google.com/p/ozz-animation/)

Which probably would be better to adapt to Urho3D's geometry format & threading model (if you want threads) or just run it single-threaded.

Cadaver does the D24_S8 limitation for GL exist for 3.0+ or ES 3.0+ or only GL 2.1 and ES 2.0? As in, does GL support it but Urho3D doesn't due to keeping compatibility?

-------------------------

boberfly | 2017-01-02 01:08:03 UTC | #20

[quote]Everything except the final transform (+ morph target blend) and the additional buffer management that would be involved in rendering is already done. Yet another library doesn't make any sense (to me). Can't forget about DecalSet either if doing CPU skinning to actually render.[/quote]

Yeah it's probably easier to just read the code and just implement a function or two in the Urho3D codebase already, from what I remember it was heavy on the macros to set explicit transforms based on how much skin influence there was (to keep performance up) and some SIMD.

-------------------------

cadaver | 2017-01-02 01:08:03 UTC | #21

Will have to test the D24_S8 format again on both Nvidia + AMD GPU's and OpenGL 3. The HW depth support feature was done before GL3 support.

-------------------------

