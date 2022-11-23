codder | 2017-01-02 01:12:10 UTC | #1

Hello,

I'm using VertexBuffer to generate some vertices.
I'm using a 3rd party library that seems to create "layers" of vertices with the same position.

[code]
graphics->SetBlendMode(BLEND_ALPHA);

float* dest = (float*)vertexBuffer_->Lock(0, draw->TotalVertices, true);

for (int i = 0; i < draw->LayerCount; i++)
{
        DrawList* dl = draw->Layer[i];

        for (int j = 0; j < dl->VertexBuffer.Size(); j++)
        {
                VertBuffer vb = dl->VertexBuffer[j];
                
                *dest++ = vb.pos.x;
                *dest++ = vb.pos.y;
                *dest++ = 0.f; // that library doesn't provide any Z coord so I think the issues is here...
                ... // color
                ... // uv     
        }
}

vertexBuffer_->Unlock();
...

[/code]

When the 3rd party library have 1 layer, everything works correctly but when it have more than 1 I see some artifacts with alpha channel.
Is possible to blend those "layers"?

-------------------------

Lumak | 2017-01-02 01:12:10 UTC | #2

Here is a code snippet on how Bullet's softbody data is copied to Urho vbuff:
[code]
            unsigned char* pVertexData = (unsigned char*)vb_->Lock(0, vb_->GetVertexCount());
        
            // copy bullet's softbody data to vertex buffer
            if (pVertexData)
            {
                unsigned numVertices = vb_->GetVertexCount();
                unsigned vertexSize = vb_->GetVertexSize();
                unsigned uElementMask = vb_->GetElementMask();
        
                for (int i = 0; i < body_->m_nodes.size(); ++i)
                {
                    btSoftBody::Node& n = body_->m_nodes[i];
                    unsigned char *pDataAlign = (pVertexData + i * vertexSize);

                    // position
                    if ( uElementMask & MASK_POSITION )
                    {
                        Vector3 &src = *reinterpret_cast<Vector3*>( pDataAlign );
                        src = ToVector3( n.m_x );
                        pDataAlign += sizeof( Vector3 );
                    }

                    // normal
                    if ( uElementMask & MASK_NORMAL )
                    {
                        Vector3 &normal = *reinterpret_cast<Vector3*>( pDataAlign );
                        normal = ToVector3( n.m_n );
                        pDataAlign += sizeof( Vector3 );
                    }
                }
                vb_->Unlock();
[/code]

Problem with yours is that it's missing:
[b]
                    unsigned char *pDataAlign = (pVertexData + i * vertexSize);
[/b]
to align to a correct buffer offset in the j-loop.

-------------------------

codder | 2017-01-02 01:12:10 UTC | #3

[code]
            vertexBuffer_->SetSize(draw->TotalVertices, Urho3D::MASK_POSITION | Urho3D::MASK_COLOR | Urho3D::MASK_TEXCOORD1, true);
            ...

            unsigned char* dataAlign = (dest + i * vertexSize);

            if (elementMask & Urho3D::MASK_POSITION)
            {
                Urho3D::Vector3& src = *reinterpret_cast<Urho3D::Vector3*>(dataAlign);
                src = Urho3D::Vector3(vert.pos.x, vert.pos.y, 0.f);
                dataAlign += sizeof(Urho3D::Vector3);
            }

            if (elementMask & Urho3D::MASK_COLOR)
            {
                unsigned int& src = *reinterpret_cast<unsigned int*>(dataAlign);
                src = vert.col;
                dataAlign += sizeof(unsigned int);
            }

            if (elementMask & Urho3D::MASK_TEXCOORD1)
            {
                Urho3D::Vector2& src = *reinterpret_cast<Urho3D::Vector2*>(dataAlign);
                src = Urho3D::Vector2(vert.uv.x, vert.uv.y);
                dataAlign += sizeof(Urho3D::Vector2);
            }
[/code]

Its hard to explain but in short its better than before but still have issues.

-------------------------

Lumak | 2017-01-02 01:12:10 UTC | #4

I don't see your entire source code, but I'm guessing there's still the layer i-loop and the dl->VertexBuffer j-loop. If that's the case then your urho vbuff index would be incremented as:

graphics->SetBlendMode(BLEND_ALPHA);

float* dest = (float*)vertexBuffer_->Lock(0, draw->TotalVertices, true);
[b]unsigned idxVBuff = 0;[/b]

for (int i = 0; i < draw->LayerCount; i++)
{
        DrawList* dl = draw->Layer[i];

        for (int j = 0; j < dl->VertexBuffer.Size(); j++)
        {
                VertBuffer vb = dl->VertexBuffer[j];
               unsigned char* dataAlign = (dest + [b]idxVBuff++[/b] * vertexSize);
. . .

Secondly, if you adjust the vbuff then you may have to also tweak your indexbuff. 
[b]set your vertex triangle draw order[/b]

And lastly, having adjusted your vbuff and ibuff, you'll need to reset the geometry draw range by calling:
[b]    pGeometry->SetDrawRange( pGeometry->GetPrimitiveType(), 0, pIbuffer->GetIndexCount(), 0, pVbuffer->GetVertexCount() );[/b]

-------------------------

codder | 2017-01-02 01:12:11 UTC | #5

I don't get what you mean by 

"Secondly, if you adjust the vbuff then you may have to also tweak your indexbuff. 
set your vertex triangle draw order".

How do I access the draw order?

I also don't have access to geometry as I only use IndexBuffer and VertexBuffer. 
Could be this the issue? Should I use a Geometry instead of simple IndexBuffer and VertexBuffer?

-------------------------

Lumak | 2017-01-02 01:12:11 UTC | #6

Maybe your [b]DrawList* dl[/b] has the triangle list?

You don't need geometry.  It's just my preference to modify Model->Geometry->VertexBuffer and ->IndexBuffe to avoid writing anything else unrelated.

-------------------------

codder | 2017-01-02 01:12:11 UTC | #7

That was an abstract type I wrote to keep things simple. Here is the full code.

[code]

void GUI::Draw(ImDrawData* draw_data)
{
    Urho3D::Graphics* graphics = GetSubsystem<Urho3D::Graphics>();

    ImDrawList** const cmd_lists = draw_data->CmdLists;
    int cmd_lists_count = draw_data->CmdListsCount;

    if (cmd_lists_count == 0)
        return;

    vertexBuffer_->SetSize(draw_data->TotalVtxCount + 500, Urho3D::MASK_POSITION | Urho3D::MASK_COLOR | Urho3D::MASK_TEXCOORD1, true);
    indexBuffer_->SetSize(draw_data->TotalIdxCount + 1000, true);
    
    // Lock vertices and indices
    unsigned char* vtx_dst = (unsigned char*)vertexBuffer_->Lock(0, draw_data->TotalVtxCount, true);
    unsigned* idx_dst = (unsigned*)indexBuffer_->Lock(0, draw_data->TotalIdxCount, true);

    unsigned idxVBuff = 0;

    for (int n = 0; n < draw_data->CmdListsCount; n++)
    {
        const ImDrawList* cmd_list = draw_data->CmdLists[n];

        unsigned int numVertices = vertexBuffer_->GetVertexCount();
        unsigned int vertexSize = vertexBuffer_->GetVertexSize();
        unsigned int elementMask = vertexBuffer_->GetElementMask();

        for (int i = 0; i < cmd_list->VtxBuffer.size(); i++)
        {
            ImDrawVert vert = cmd_list->VtxBuffer[i];

            unsigned char* dataAlign = (vtx_dst + idxVBuff++ * vertexSize);//(vtx_dst + i * vertexSize);

            *reinterpret_cast<Urho3D::Vector3*>(dataAlign) = Urho3D::Vector3(vert.pos.x, vert.pos.y, 0.f);
            dataAlign += sizeof(Urho3D::Vector3);

            *reinterpret_cast<unsigned int*>(dataAlign) = vert.col;
            dataAlign += sizeof(unsigned int);

            *reinterpret_cast<Urho3D::Vector2*>(dataAlign) = Urho3D::Vector2(vert.uv.x, vert.uv.y);
            dataAlign += sizeof(Urho3D::Vector2);
 
        }

        for (int i = 0; i < cmd_list->IdxBuffer.size(); i++)
        {
            ImDrawIdx idx = cmd_list->IdxBuffer[i];
            idx_dst[i] = idx;
        }
    }

    vertexBuffer_->Unlock();
    indexBuffer_->Unlock();

    graphics->SetVertexBuffer(vertexBuffer_);
    graphics->SetIndexBuffer(indexBuffer_);
}
[/code]

-------------------------

Lumak | 2017-01-02 01:12:11 UTC | #8

Where you populate the vbuff and ibuff looks okay to me. I'm not sure about the below:

. . .
                graphics->Draw(Urho3D::TRIANGLE_LIST, idx_offset, pcmd->ElemCount, vtx_offset, 0, cmd_list->VtxBuffer.size()); // not sure if you need  vtx_offset since the triangle list starts from 0??
            }

            idx_offset += pcmd->ElemCount; // not sure if this should be idx_offset += elemcount * 3; if each element is a triangle
        }

        vtx_offset += cmd_list->VtxBuffer.size(); // is this needed since there's only a single vbuff and the triangle list starts from 0??
. . .

-------------------------

Lumak | 2017-01-02 01:12:11 UTC | #9

What about your indexbuffer index in:
        for (int i = 0; i < cmd_list->IdxBuffer.size(); i++)
        {
            ImDrawIdx idx = cmd_list->IdxBuffer[i];
            idx_dst[i] = idx;
        }

Shouldn't that be set like what you did with idxVBuff?:
int idxIBuff = 0;
idx_dst[idxIBuff++] = idx;

-------------------------

codder | 2017-01-02 01:12:11 UTC | #10

Oh yea seems to work. Thank you very much!

-------------------------

Lumak | 2017-01-02 01:12:11 UTC | #11

Ok, cool.

I thought of one more thing.  If your [b] cmd_list->IdxBuffer[/b] has a triangle order specific to [b]cmd_list->VtxBuffer[/b] then you might need to account for where the current index offset is:

int curIndexOffset = idxIBuff;

for (int i = 0; i < cmd_list->IdxBuffer.size(); i++)
{
   ImDrawIdx idx = cmd_list->IdxBuffer[i];
   idx_dst[ idxIBuff++ ] = idx + curIndexOffset;
}

-------------------------

codder | 2017-01-02 01:12:11 UTC | #12

IdxBuffer is just an array of ImDrawIdx. ImDrawIdx is unsigned int.
The previous code seems to work correctly. I think the issue was the index of the Urho3D::IndexBuffer, I forgot to keep in mind the extra counter  :slight_smile:

-------------------------

Lumak | 2017-01-02 01:12:11 UTC | #13

Ok, if it's working.

Now, a pic of what's working would be cool :slight_smile:

-------------------------

codder | 2017-01-02 01:12:11 UTC | #14

Here :stuck_out_tongue:
[img]http://s19.postimg.org/meb5a6cgj/screen.jpg[/img]

-------------------------

Lumak | 2017-01-02 01:12:11 UTC | #15

That looks awesome! Gratz!

lol about "TNX LUMAK" haha, and you're welcome! :slight_smile:

-------------------------

