GoogleBot42 | 2017-01-02 01:04:10 UTC | #1

I am planning on making a mesh combiner to make rendering even faster by combining models and having them all become a much bigger model...  To do this I clearly will need to be able to select a single "sub-texture" from a big texture that serves as a texture map with UV coordinates.  But I am not sure how I can do this because the Urho3D api doesn't allow setting start and end UV texture coordinates.

Materials have this function: 	SetUVTransform (const Vector2 &offset, float rotation, float repeat)

but this doesn't seem like enough... Maybe I just missed something...

-------------------------

codingmonkey | 2017-01-02 01:04:10 UTC | #2

>mesh combiner to make rendering even faster by combining models 
I think that the some kind of StaticInstasing with pack all static geometry into one VertexBuffer on engine start is good feature for urho in future add, but today the better way I think to reduce count of batches is - manually
do:
1. blocking base of level.
2. find or define the static group's of objects that have an some shared textures, similar texture parts
3. for each of this groups do join textures into one big texture  
4. manually merge static mesh in 3d editor with same material into one mesh
5. adjust uv offset
this give you one renderer batch and not several

there is in urho also exist the StaticMeshGroup for some kind of instancing many objects at one time but it no reduce batches count

-------------------------

GoogleBot42 | 2017-01-02 01:04:10 UTC | #3

You are totally right about that.  In a tool like blender, it would be much easier.  Although, I am planning on making a minecraft cloned designed from the ground up to be modded.  So I cannot premerge any models or textures as they are added at runtime.   :confused:

I have made some progress on UV texture mapping.  In the UV function I mentioned before the function sets two shader parameters to specify the mapping after doing some matrix math (I don't really know any matrix math atm).

[code]    SetShaderParameter("UOffset", Vector4(transform.m00_, transform.m01_, transform.m02_, transform.m03_));
    SetShaderParameter("VOffset", Vector4(transform.m10_, transform.m11_, transform.m12_, transform.m13_));[/code]

Under default mapping the values are:

[code]        SetShaderParameter("UOffset", Vector4(1.0f, 0.0f, 0.0f, 0.0f));
        SetShaderParameter("VOffset", Vector4(0.0f, 1.0f, 0.0f, 0.0f));[/code]

Summary of my testing for what each value means:
[code]        SetShaderParameter("UOffset", Vector4(/* how many time repeated x dir */, /* skewing */, /* idk */, /* x offset */));
        SetShaderParameter("VOffset", Vector4(/* how many time repeated y dir */, /* skewing */, /* idk */, /* y offset */));[/code]

I think I can figure it out know. :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:04:11 UTC | #4

I guess that binding then material for each cube with other uv-offsets is very expensive tech
better you must think about tech that uses one material binding pre draw all chunks of cubes on the world map
I think you need doing some calculation to fill vertexbuffer based on camera view, and then you fill VB you just set some UV-offset in vertexes for cube (choice texture in texture-atlas based on cube type).

simplified render

-bind texture (static data)
-bind shader (most time static parameters)
(texture + shader = material in urho terms )

-bind vertex buffer with a chunk of cubes 8*8 or 16*16... (this data calculate each frame) 
draw()

-------------------------

GoogleBot42 | 2017-01-02 01:04:11 UTC | #5

I don't think I am understanding you... are you essentially saying that I should have one material per entire chunk mesh?

This is what I was planning on doing but the only way I can see that this can be done is if the mesh of each block in the chunk is combined to make one big chunk mesh and then the material is assigned.  So the next thing I am going to do is create a texture class that represents a map of textures.  Then I will make a mesh+texture combiner.

Is this pretty much what you were saying?  If you have a better/easier idea I definately would love to hear it!  :slight_smile:

EDIT: Marking this solved becase my original question was answered.

-------------------------

codingmonkey | 2017-01-02 01:04:11 UTC | #6

yes, even more so - for the whole world ) 
one texture one material one uber-shader and several dynamic VB with all information(stored in free FFP field) that need in shader to draw all cubes as you needed.
You can even try to use the free std vertex fields for doing selection technique of shading in the own custom shader.
> If you have a better/easier idea I definately would love to hear it! :slight_smile:
no i'm do not had any other easier idea.

-------------------------

GoogleBot42 | 2017-01-02 01:04:11 UTC | #7

Hmmm as much as I really would like to do the entire world (in fact I was planning on doing just that for a while) I realized just how slow updating a chunk would be... Any time a block is added or removed the chunk mesh will need to be updated and the larger it is the slower the update will be...

But [i]maybe[/i] I can have a smart update that will only update the portion of the mesh that has been changed.  That would probably be much quicker.  IDK I will see if I can make it work.  :wink: 

But you are totally right.  If I can render the entire world in one draw...  :astonished:   That would be so fast! Wow!

-------------------------

GoogleBot42 | 2017-01-02 01:04:11 UTC | #8

Hmmm back on topic for the feature request section...

The first UV modification line doesn't do the same thing as the second two... but shouldn't they be equivalent?  Is this a bug?

[code]        Vector2 start(0.5f,0.5f);
        Vector2 end(1.0f,1.0f);

        Vector2 offset = start;
        Vector2 repeat = end - start;

        // this doesn't do the same thing as the next two statements together...
        mat->SetUVTransform(offset, 0, repeat);

        mat->SetShaderParameter("UOffset", Vector4(repeat.x_, 0.0f, 0.0f, offset.x_));
        mat->SetShaderParameter("VOffset", Vector4(0.0f, repeat.y_, 0.0f, offset.y_));[/code]

If this isn't a bug can we add a function to specify the start and end UV coordinates as a pecentage from 0.0f to 1.0f?

Something like:
[code]SetUVTransform(Vector2 &startCoord, Vector2 &startCoord);[/code]

-------------------------

GoogleBot42 | 2017-01-02 01:04:20 UTC | #9

[quote="Sinoid"]I'm having a really tough time following what you're saying versus what you appear to mean?

    I realized just how slow updating a chunk would be... Any time a block is added or removed the chunk mesh will need to be updated and the larger it is the slower the update will be...



How big are your chunks? Updating a 32x32x16 chunk (size I used when doing one of these) of voxels should be instant and as long as you "suspend" updates so that you aren't building updates for every single block change when doing a flood-fill / ray / radius / etc change to the blocks.[/quote]

If the entire world were one "big" chunk like we were talking about and the update algorithm generated a new from scratch each world mesh generation then the larger the world the longer it would to generate the mesh...  Yes I do know that typically voxels engines divide the world into chunks.  I will be doing a version of this.

[quote="Sinoid"]How are you constructing your voxels? It sounds like you're using cube models? You should be constructing an entire mesh, no inside faces, etc.[/quote]

Heck no!   :astonished:  That would be bad idea for sure!  For the basic block there will be 31 possible meshes that will represent one block  (2^6 - 1 one for each possible combination of sides of the block missing but minus one to remove the case where there are no sides.)  Sides will be removed that are not displayed and each cube mesh will be combined with neighbouring cube meshes in the entire chunk (or maybe the entire world if I can figure out a nice way to do it)  That way there is only one draw call per chunk or the entire world.

[quote="Sinoid"]No, just update the whole chunk - the most clever thing that's worth considering is using greedy meshing which will be slower to update the whole mesh[/quote]

In this context I wasn't talking about chunks I was talking about the entire world.  Generating a new mesh for the entire world on each new block placed/removed would be a really bad idea and it would be screamingly slow especially when there are millions of total blocks.

[quote="Sinoid"]You wouldn't use SetUVTransform in the case of merging meshes as that's a material attribute and I'm assuming that by merging meshes you mean combining all vertex/index data into one and merging the textures into an atlas. [/quote]

Hmmm you are totally right.   :confused:   I wonder how I didn't see this at first... Setting the shader variable sets it for the entire material so it won't work.  So how would I modify the texture coords of a sub mesh so that the same material is used?  Any help would be really appreciated!  :slight_smile:

-------------------------

GoogleBot42 | 2017-01-02 01:04:21 UTC | #10

[quote="Sinoid"]Do you have a Github repository (or someplace else) that contains your voxel code?[/quote]

No I don't... Not sure why that would be very important though... I just need some way to set the texture coords of different verities of a mesh.  I can probably take it from there.  :wink:   When I was using Irrlicht (BTW don't use Irrlicht to make a game.  It is a bad idea and a waste of time.  :angry: ) it was pretty simple to do this.  What about Urho3D?  :slight_smile: 

I have already written a program that can pack rectangles in a bigger rectangle (for making one big texture): [url]https://github.com/GoogleBot42/StripPacking[/url]  It may not be the cleanest but it works great. (I just finished it so that will happen later) :smiley:

-------------------------

GoogleBot42 | 2017-01-02 01:04:22 UTC | #11

I found this: [url]http://discourse.urho3d.io/t/solved-how-to-create-mesh/35/1[/url]  I got it working!  The only thing is that light doesn't seem to work... I am sure it is something simple.  Any thoughts?

Here is the modified code from the post linked above for those who want to see. :slight_smile:

[code]    float dirLightVertexData[] =
    {
    -1, 1, 0,   0, 0,
    1, 1, 0,    0.5f, 0,
    1, -1, 0,   0.5f, 0.5f,
    -1, -1, 0,  0, 0.5f,
    };

    unsigned short dirLightIndexData[] =
    {
    0, 1, 2,
    2, 3, 0,
    };

    SharedPtr<VertexBuffer> dlvb(new VertexBuffer(context_));
    dlvb->SetShadowed(true);
    dlvb->SetSize(4, MASK_POSITION | MASK_TEXCOORD1);
    dlvb->SetData(dirLightVertexData);

    SharedPtr<IndexBuffer> dlib(new IndexBuffer(context_));
    dlib->SetShadowed(true);
    dlib->SetSize(6, false);
    dlib->SetData(dirLightIndexData);

    Geometry *dirLightGeometry_ = new Geometry(context_);
    dirLightGeometry_->SetVertexBuffer(0, dlvb);
    dirLightGeometry_->SetIndexBuffer(dlib);
    dirLightGeometry_->SetDrawRange(TRIANGLE_LIST, 0, dlib->GetIndexCount());

    SharedPtr<Model> testModel(new Model(context_));
    Vector<SharedPtr<VertexBuffer> > dlvbVector;
    Vector<SharedPtr<IndexBuffer> > dlibVector;
    dlvbVector.Push(dlvb);
    dlibVector.Push(dlib);
    testModel->SetNumGeometries(1);
    testModel->SetNumGeometryLodLevels(0, 1);
    testModel->SetGeometry(0, 0, dirLightGeometry_);

    // Define the model buffers and bounding box
    PODVector<unsigned> emptyMorphRange;
    testModel->SetVertexBuffers(dlvbVector, emptyMorphRange, emptyMorphRange);
    testModel->SetIndexBuffers(dlibVector);
    //testModel->SetBoundingBox(BoundingBox(Vector3(-1.0f, -1.0f, 0.0f), Vector3(1.0f, 1.0f, 0.0f)));

    Node* testnodea = scene_->CreateChild("testasdasd");
    StaticModel* testObjecta = testnodea->CreateComponent<StaticModel>();
    testObjecta->SetModel(testModel);

    Material* mat = new Material(context_);
    mat->SetNumTechniques(1);
    mat->SetTechnique(0, cache->GetResource<Technique>("Techniques/Diff.xml") );
    Texture* tex = cache->GetResource<Texture2D>("Textures/BlueOre.png");
    tex->SetFilterMode(FILTER_NEAREST);
    mat->SetTexture(TU_DIFFUSE, tex);

    testObjecta->SetMaterial(0,mat);[/code]

-------------------------

GoogleBot42 | 2017-01-02 01:04:26 UTC | #12

[quote="Sinoid"]Probably just need to add vertex normals for the lighting to use, same deal as you did for tex coords. With hard-voxels like minecraft you'd all four verts of each face will share the same normal.[/quote]

Yeah I figured it out a while ago... I was just too lazy to post here about it. :wink: (plus i wanted to avoid a triple post :stuck_out_tongue:) 

CustomGeometery components are much easier it turns out...

[code]        customGeo->DefineGeometry(0, TRIANGLE_LIST, 6, true, false, true, false);

        CustomGeometryVertex* ver;

        ver = customGeo->GetVertex(0,0);
        ver->position_ = Vector2::ZERO;
        ver->normal_ = Vector3::BACK;
        ver->texCoord_ = Vector2::UP;

        ver = customGeo->GetVertex(0,1);
        ver->position_ = Vector2::UP;
        ver->normal_ = Vector3::BACK;
        ver->texCoord_ = Vector2::ZERO;

        memcpy(customGeo->GetVertex(0,4),ver,sizeof(CustomGeometryVertex));

        ver = customGeo->GetVertex(0,2);
        ver->position_ = Vector2::RIGHT;
        ver->normal_ = Vector3::BACK;
        ver->texCoord_ = Vector2::ONE;

        memcpy(customGeo->GetVertex(0,3),ver,sizeof(CustomGeometryVertex));

        ver = customGeo->GetVertex(0,5);
        ver->position_ = Vector2::ONE;
        ver->normal_ = Vector3::BACK;
        ver->texCoord_ = Vector2::RIGHT;

        customGeo->Commit();[/code]

-------------------------

