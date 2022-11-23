amit.nath30 | 2017-02-10 18:24:54 UTC | #1

Hello,

How can I combine 2 geometry together, I am a unity developer and looking for an alternative of Unity Mesh.CombineMeshes

-------------------------

Eugene | 2017-02-10 19:26:18 UTC | #2

E.g. manually merge content of the several `Model`s.
Since you don't have strict requrements/explanation of what is 'combine', there are a lot of was to do it.

-------------------------

jmiller | 2017-02-10 19:39:46 UTC | #3

Possible similar thread with useful information:
http://discourse.urho3d.io/t/mesh-batching-combining/807/4

-------------------------

amit.nath30 | 2017-02-13 18:27:45 UTC | #4

Yes I have gone through the above forum but did not get my answer.

suppose I have made a VertexBuffer using

    float vertices[] = {
            //position                                          normal                      uv
            -quadWidth * .5f,  cubeHeight * .5f,    0,          0.0f, 0.0f, 0.0f,           1.0f,   0.0f,
             quadWidth * .5f,  cubeHeight * .5f,    0,          0.0f, 0.0f, 0.0f,           0.0f,   0.0f,
             quadWidth * .5f, -cubeHeight * .5f,    0,          0.0f, 0.0f, 0.0f,           0.0f,   1.0f,
            -quadWidth * .5f, -cubeHeight * .5f,    0,          0.0f, 0.0f, 0.0f,           1.0f,   1.0f
        };

    Urho3D::VertexBuffer* vb = new Urho3D::VertexBuffer (context_);

    vb->SetSize(4, Urho3D::MASK_POSITION | Urho3D::MASK_NORMAL | Urho3D::MASK_TEXCOORD1);
    vb->SetData(vertices);

and suppose I have 2 of this vertex buffer what will be the easiest way to combine these 2 VertexBuffer?

-------------------------

