sabotage3d | 2017-01-02 01:08:54 UTC | #1

Hi guys I need some help with this as I spent quite a while and I cannot solve it on my own. I have added a new method inside the Geometry class and I am trying to create new VertexBuffer but when I call SetSize it crashes. Inside the method I have:
[code]SharedPtr<VertexBuffer> cVertBuffer(new VertexBuffer(context_));
cVertBuffer->SetShadowed(true);
cVertBuffer->SetSize(GetVertexCount() * instances.Size(), vertexBuffers_[0]->GetElementMask(), false);[/code]
Everything passed to SetSize seems to be valid in the debugger. The last method of the crash is at glGenBuffers(1, &object_) inside the OGLVertexBuffer, VertexBuffer::Create() method. If I create the VertexBuffer headless it doesn't crash. The same applies for the IndexBuffer.
[code]#3	0x00000001000b4ccb in Urho3D::Geometry::CreateCombinedGeometry() const at Geometry.cpp:465
#2	0x0000000100112e6b in Urho3D::VertexBuffer::SetSize(unsigned int, unsigned int, bool) at OGLVertexBuffer.cpp:197
#1	0x0000000100112828 in Urho3D::VertexBuffer::Create() at OGLVertexBuffer.cpp:406[/code]

-------------------------

codingmonkey | 2017-01-02 01:08:54 UTC | #2

Well i'm test this code:
[code]        SharedPtr<VertexBuffer> vb = SharedPtr<VertexBuffer>(new VertexBuffer(context_));
        vb->SetShadowed(true);
        vb->SetSize(10000000, MASK_POSITION | MASK_NORMAL | MASK_COLOR | MASK_TEXCOORD1, false);[/code]
and it's working fine

Did you modify Geometry class inside?
why you think if it's has been already created you need to create VB again ? Maybe if you decide to create new VB, probably you will need release old VB ?

I suppose what Drawables have some methods for update geometry in it self internally.
Every frame (if it pushed to renderer) it check some flags in UpdateGeometry()
for example:
[code]
void Drawable::UpdateGeometry(const FrameInfo& frame)
{
    if (bufferSizeDirty_ || indexBuffer_->IsDataLost())
        UpdateBufferSize();

    if (bufferDirty_ || vertexBuffer_->IsDataLost() || forceUpdateVertexBuffer_)
        UpdateVertexBuffer(frame);
}
[/code]

you may manage this flags (in your derived class)  - bufferSizeDirty_, bufferDirty_ if you need reassemble VB by some reason.
and Drawable::UpdateBufferSize() you just setup IB size (and may feed it with indexes) and also setup VB.SetSize()

and in method Drawable::UpdateVertexBuffer(const FrameInfo& frame) you just assemble your VB feed it with new geometry. 
There is no place where new VB been created. It already exits by default.

I don't known, but you may try just SetSize and feed VB with new geom and do not allocate new.

-------------------------

sabotage3d | 2017-01-02 01:08:54 UTC | #3

Thanks codingmonkey. Yes I am modifying the geometry class but I cannot use a reference to the same geometry as I am doing a new combined buffer of multiple instances. I looked into other classes in Urho3D and this seems to work. I think you are right I might need to update the geometry somewhere else as well but I am not sure where. Maybe I should just make a new class and inherit from Geometry instead of adding new methods.

-------------------------

TikariSakari | 2017-01-02 01:08:54 UTC | #4

Ive been using customgeometry, and at least there it is easy to just add or remove the stuff in the end. It is bit harder to remove vertices from the middle though, so I've been swapping the ones from the end to the middle. Although I think in general I am doing lots of things wrong, such as defining many customgeometries for creating armature/skeleton with customgeometry for my voxel modeling thingie.

I think CustomGeometry by default has support for multiple geometries, I just haven't figured out how I could give different transformations to the geometries. I also noticed that for some reason, even if I use same material for all the geometries, at least when the material is created on the fly by modifying texture, the geometries for some reason do not become single batch. Again this is probably just me being dumb, which is nothing unusual.

-------------------------

cadaver | 2017-01-02 01:08:54 UTC | #5

CustomGeometry is not intelligent. If you create 2 subgeometries, they also create 2 draw calls even with same materials.

Drawcall combining only happens in Urho automatically via hardware instancing. The requirements are same Geometry, same Material, same lighting conditions. In case of CustomGeometry, the Geometries are always unique, therefore no instancing.

-------------------------

sabotage3d | 2017-01-02 01:08:55 UTC | #6

Can we create custom geometry with new vertex and index buffer inside the Geometry class or it is not recommended?

-------------------------

cadaver | 2017-01-02 01:08:55 UTC | #7

You must have some way to supply the Geometry to the rendering pipeline, in other words probably your own Drawable subclass, unless you put the Geometry inside a Model resource, in which case it can be rendered by a normal StaticModel component. The latter way is demonstrated by the DynamicGeometry sample.

-------------------------

sabotage3d | 2017-01-02 01:08:56 UTC | #8

I am already calling this method inside the StaticModelGroup. If I try to create new vertex or index buffer and the set the size inside StaticModelGroup::UpdateBatches it crashes. Is there anything specific I need to do in order to sync it with the gpu buffer? Outside of Urho3D classes this usually works.
[code]SharedPtr<IndexBuffer> ib(new IndexBuffer(context_));
ib->SetShadowed(true);
ib->SetSize(10, false);[/code]

-------------------------

codingmonkey | 2017-01-02 01:08:56 UTC | #9

>Outside of Urho3D classes this usually works.
Hey, I looked into your brunch with smg instansing and trying to create similar feature
and at first look it seem working fine.

look at this: [github.com/MonkeyFirst/Urho3D/c ... a2b04ce022](https://github.com/MonkeyFirst/Urho3D/commit/d7d6f3b975324a684942541d15a871a2b04ce022)

you may copy from this brunch SMG *.h/*.cpp files and try to figure out with this.

how it works:
add node
add to node smg component
set model
set material

add some nodes to smg's node as children
move child nodes
select SMG component
select menu EDIT -> Add children to SM-group
set Use static instancing to true

[url=http://savepic.su/6835727.htm][img]http://savepic.su/6835727m.png[/img][/url]

you may change child nodes positions and static blob will be reassembled per change

-------------------------

sabotage3d | 2017-01-02 01:08:57 UTC | #10

Thanks a lot codingmonkey, but I am getting the same crash maybe when I merged the master branch it was broken I don't have other explanation. As I just took your changes and merged them in the branch I already had.
It crashes now at:
[code]dVB->SetSize(vertexCount * blobInstancesMatrices_.Size(), elementMask, true);[/code]
I will try from scratch with a clean branch.
[b]UPDATE:[/b] I built your branch from scratch bu the same thing happens.

-------------------------

codingmonkey | 2017-01-02 01:08:58 UTC | #11

strange, but I only update my fork yesterday and add this feature (based on your code, with few changes)
I use vs2013 to compile debug and release and it's working fine in my case.
did you try run Urho3DPlayer in debug mode, and debug problem place step by step?

-------------------------

sabotage3d | 2017-01-02 01:08:58 UTC | #12

I tried both in C++ and in the Editor. They both crash at the same place. For the C++ test I just added the lines below inside the HugeObjectCount demo and I tried reducing the number of objects to 10. I also tested the DynamicGeometry example and it works fine. I am under OSX 10.10 and I am using Xcode to compile. Is it possible that my videocard is the problem, its gtx 260?
[code]...
lastGroup->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
lastGroup->SetStatic(true);
...[/code]
It looks like the _object is zero compared to working example outside the engine's classes.
[img]http://i.imgur.com/fEUAGfB.png[/img]

-------------------------

codingmonkey | 2017-01-02 01:09:00 UTC | #13

I doubt it's problems stem from the graphics card, although it is possible version of the driver can somehow influence on this. 
Most likely your compiler have some -pedantic settings?
In addition, the code can contain any unforeseen errors, I wrote a testvy variat it needs polishing. 
I tested, only the editor with one SMG and one thing what very important - model should be without LODs otherwise this instansing does not work as expected.

-------------------------

sabotage3d | 2017-01-02 01:09:00 UTC | #14

I am just testing with the default box model. I just tested on my Linux machine at work I tested both gcc and clang and the same crash happens. If you are building on Windows are you using the DirectX API? Because in my tests I can only test with the OpenGL API. I think is something to do where the graphics is initialized after we create the vertex and index buffers. Maybe I need to set the buffers manually in the graphics subsystem?
[code]0x00007ffff79ad949 in glGenBuffers () from /usr/lib64/nvidia/libGL.so.1[/code]

-------------------------

cadaver | 2017-01-02 01:09:00 UTC | #15

At least you shouldn't create anything GPU-related before you have done Graphics::SetMode() (normally done in engine initialization.) Otherwise the GL context is null and you will quite certainly crash.

-------------------------

sabotage3d | 2017-01-02 01:09:00 UTC | #16

SetMode is already called, but because the code is initialized inside StaticModelGroup I think it might be called before the graphics is initialized. Is there a good way to make sure they are synced?

-------------------------

codingmonkey | 2017-01-02 01:09:00 UTC | #17

>If you are building on Windows are you using the DirectX API?
actually no) most of last time I use only GL renderer 

try to do test:
Compile again my brunch and use [b]only Urho3D Editor to test this instancing[/b], i'm just curious it still will be crashing or no?

-------------------------

sabotage3d | 2017-01-02 01:09:00 UTC | #18

I just tried in the Editor at work on my linux machine and it is not crashing. It is really strange as I tried at home and it was crashing in the Editor. Finally I found the problem is in HugeObjectCount we have already nodes with the same name and when we switch to useGroups_ they are not properly initialized. It is quite unstable but alteast it is working.

-------------------------

codingmonkey | 2017-01-02 01:09:00 UTC | #19

>It is quite unstable but alteast it is working.
Well, my congrats )

Earlier I do some primitive test with this instancing and old(dynamic) and do not found extra boost from this tech )
more over, I found only more using memory GPU bandwidth with this static instancing (test on over 2 million vertexes)

-------------------------

sabotage3d | 2017-01-02 01:09:01 UTC | #20

Thanks a lot for your help. This technique is mainly for mobile I am getting huge boost atleast double the FPS on an old tablet. Unity has these features out of the box as well.
[b]UPDATE:[/b] I think I am going crazy but it is still crashing at home on my OSX box.

-------------------------

sabotage3d | 2017-01-02 01:09:02 UTC | #21

Is it possible that this is some kind of threading issue as it happens only on OSX? Might be something to do with the clang compiler. The Graphics subsytem is already present when the GPUObject and the VertexBuffer are created everything seems fine. Can anyone else verify this on OSX?
[img]http://i.imgur.com/JbWthcD.png[/img]
[b]UPDATE:[/b] It seems we can't create new vertex buffers inside UpdateBatches().

-------------------------

