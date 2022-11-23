codingmonkey | 2017-01-02 01:03:03 UTC | #1

Hi folks!
Today, I was trying to figure out how to write my own component class based on drawable class. 
My trying it's fully based on BillboardSet component.
i'm write some minimal code and trying to debug it. for this i'm set some breakpoints for few methods of my component.
it's creates successfull as node's component

[pastebin]X2r4RRzb[/pastebin]

but it's do not execute any of drawable methods after creation (and setup some set's methods)  
the drawable methods such as - Update, UpdateBatches, UpdateGeometry, they do not called at all, why ? 

code
h
[spoiler][pastebin]btW59e7h[/pastebin][/spoiler]
cpp
[spoiler][pastebin]nVsiH8cC[/pastebin][/spoiler]

-------------------------

cadaver | 2017-01-02 01:03:03 UTC | #2

It may be that it never generates geometry -> bounding box is empty or undefined -> it doesn't pass culling.

Drawable::Update() is not called automatically each frame, rather you must mark the drawable explicitly to need an update. It will then be performed at the same time as the octree updates itself. See MarkForUpdate() and the AnimatedModel / ParticleEmitter classes.

Also note that you don't necessarily need Drawable::Update() at all, if all you want is a periodic tick update that is independent of the octree / view processing you can also just subscribe to the frame tick events.

-------------------------

codingmonkey | 2017-01-02 01:03:03 UTC | #3

I added this

[code]void TailGenerator::OnNodeSet(Node* node)
{
	Drawable::OnNodeSet(node);
}[/code]

and it seems that it's what's needed to methods began to be called
now i can  debug code.

-------------------------

cadaver | 2017-01-02 01:03:03 UTC | #4

Ah ok, did not notice that you had overridden that one with an empty function at first. Drawable::OnNodeSet() is responsible for adding the drawable to the octree, and indeed without that the drawable won't participate in rendering at all.

-------------------------

codingmonkey | 2017-01-02 01:03:04 UTC | #5

I also temporarily given size to BB
as 
[code]
void TailGenerator::OnWorldBoundingBoxUpdate() 
{
	worldBoundingBox_.Define(-M_LARGE_VALUE, M_LARGE_VALUE);
}
[/code]

i don't know but in case dual tail with high rotation it's looks  wierd. 
I use delta-move based method for spawn base points of tail path. 
maybe it's wrong method ?

[video]http://www.youtube.com/watch?v=kJe9GhqRL6A[/video]

-------------------------

codingmonkey | 2017-01-02 01:03:04 UTC | #6

in addition with previous
I aslo have an question about the Drawable::GetUpdateGeometryType()

[code]
UpdateGeometryType TailGenerator::GetUpdateGeometryType()
{
	if (bufferDirty_ || bufferSizeDirty_ || vertexBuffer_->IsDataLost() || indexBuffer_->IsDataLost() || forceUpdateVertexBuffer_)
		return UPDATE_MAIN_THREAD;
	else
		return UPDATE_NONE;
}
[/code]

it is called every frame in engine, then batches are going to prepare for render or no ?
i just want to split my logic of building mesh in work thread and put ready compiled mesh data in the main thread with helps of few lines of the code.

-------------------------

cadaver | 2017-01-02 01:03:05 UTC | #7

That is going to be called after UpdateBatches() but before UpdateGeometry(), for a drawable that is in the view frustum.

Note that UpdateBatches() itself may be called from a worker thread.

-------------------------

codingmonkey | 2017-01-02 01:03:06 UTC | #8

i'm trying to prepare mesh data in worker thread and then it's ready it copying in main thread to vertex buffer, but after few seconds i got an freez. i guess that something i doing wrong. now i rewrite code all without workers, all stages going in main thread (i guess).

today i'm find a strange effect
then i setup the batch in constructor as:

[code]batches_[0].geometryType_ = GEOM_STATIC;   [/code] 

i got a more constast colors on tail's
[url=http://savepic.su/4883438.htm][img]http://savepic.su/4883438m.png[/img][/url]

and then i setup batch as :
[code]batches_[0].geometryType_ = GEOM_BILLBOARD;
[/code] 
i got an more lower contrast on tail's
[url=http://savepic.su/4887534.htm][img]http://savepic.su/4887534m.png[/img][/url]

Why this is happens ?
And what type of geometry tails should be?

[video]http://www.youtube.com/watch?v=5kwpE66G-8M[/video]

also i'm find what using Splines for tail path( + color fade) interpolation it's extremely slow, moreover this dramatically slow on fps
in this case i'm rewrite vertex color (fade/color gradient) interpolation from spline's to vector lerp

-------------------------

cadaver | 2017-01-02 01:03:06 UTC | #9

STATIC geometry is the normal mode for meshes, ie. vertices in vertex buffer are transformed by viewproj and model matrices. BILLBOARD means a different kind of transformation where a point is transformed and then offsetted by a size parameter to get a quad. Look into Transform.hlsl (.glsl) to understand how the shader is transforming the vertices.

-------------------------

codingmonkey | 2017-01-02 01:03:06 UTC | #10

>STATIC geometry is the normal mode for meshes
Ok.
And about shadows. 
If i'm create even the one tail component for any node in all scene, the shadows from bots began looks weird - like an old style shadows with blobs. 
And if scene no have any tails the shadows draws - ok
I think what i'm must do something for shadows for tail. 
Turn off shadow from tail at all or make some basic shadows functionality.

-------------------------

cadaver | 2017-01-02 01:03:07 UTC | #11

If you're still setting a huge bounding box for your object, it will cause the shadow rendering to believe there's a huge object that needs to cast/receive shadows, and the shadow resolution will suffer. You should use a bounding box that encloses your geometry tightly.

-------------------------

codingmonkey | 2017-01-02 01:03:07 UTC | #12

Thank's [b]cadaver[/b]. it's helps, now the shadows is draw.
i'm calculate BoundBox on actual visible points of path.

[pastebin]jzFVPaAL[/pastebin]

bbmin and bbmax calculated in void TailGenerator::UpdateVertexBuffer(const FrameInfo& frame) 

[spoiler][pastebin]v8ALc1gU[/pastebin][/spoiler]

-------------------------

codingmonkey | 2017-01-02 01:03:11 UTC | #13

I uploaded a component to repository and it is now available to everyone.
[github.com/MonkeyFirst/urho3d-c ... -generator](https://github.com/MonkeyFirst/urho3d-component-tail-generator)

Small instruction.
[img]http://savepic.su/4866680.png[/img]

code:
[code]	virtual void Setup()
	{
		TailGenerator::RegisterObject(context_);

	}[/code]

[code]
		tailNode->CreateComponent<TailGenerator>();
		tailNode->GetComponent<TailGenerator>()->SetTailLength(0.5f); // set segment length
		tailNode->GetComponent<TailGenerator>()->SetNumTails(50); //  set num of segments
		tailNode->GetComponent<TailGenerator>()->SetWidthScale(4.0f); // side scale
		tailNode->GetComponent<TailGenerator>()->SetColorForHead(Color(1.0f, 1.0f, 1.0f));
		tailNode->GetComponent<TailGenerator>()->SetColorForTip(Color(0.0f, 0.0f, 1.0f));
[/code]

-------------------------

friesencr | 2017-01-02 01:03:11 UTC | #14

Thanks for sharing.  I regularly watch your progress videos and am always inspired.   You should add a licence to your codebase.

-------------------------

cadaver | 2017-01-02 01:03:11 UTC | #15

Very nice, good that you got it working!

-------------------------

sabotage3d | 2017-01-02 01:03:11 UTC | #16

Thanks for sharing. Your work is amazing as always.

-------------------------

weitjong | 2017-01-02 01:03:12 UTC | #17

Many thanks. Keep up the good work coming.

-------------------------

codingmonkey | 2017-01-02 01:03:12 UTC | #18

Thank's guys, but I think that the component is still far from ideal. And requires some modifications.
Among the main - remove two Batchs and draw two strips with a single batch with degenerate triangle in middle of IB. 
I tried draw tail with one batch but I for some reason did not work.
The second problem is when you need dynamic tail from static object.
This component can only generate tail from the dynamic objects (that change own position in time)

-------------------------

codingmonkey | 2017-01-02 01:04:27 UTC | #19

@Sinoid Thanks, it stored in own repository on git (as few files for copying into your working dir) you may just copy it into yours dev folder.  

>Perhaps a different component similar to this?
i'm also think about this, that it's could be a other component.

-------------------------

codingmonkey | 2017-01-02 01:04:27 UTC | #20

>merge tools choked for me
for me too )

>Dealt with generating a single tri-strip
you mean that now you have one-batch for these 2 strips ?

>Makes for interesting twists.
I guess that you need do some tests this with chaotic node movements (Brownian motion) to avoid strange twists and do some polish to alg for looking-well tailepath in most cases.

>Everything works inside the editor with attributes for all settings and sane defaults.
Wow, cool) Is it generate tail on play button or even then editor in standby mode ?

-------------------------

codingmonkey | 2017-01-02 01:04:27 UTC | #21

>so the horizontal plane can collapses when moving along a direction that isn't forward
Oh, maybe that why i trying to use and spawn points with motion direction of node ) 
In this case i just got less twisted triangles i guess.

Anyway, look at this example (thanks for @carnalis for this link)
[codeflow.org/entries/2012/aug/05 ... id-trails/](http://codeflow.org/entries/2012/aug/05/webgl-rendering-of-solid-trails/)

i guess this method more better. There is almost no tail-path-twists.
also it have only one strip that every time oriented to camera. 
See if you interesting some examples there. 
I think this is really good thing to realize as urho3d engine component.

-------------------------

