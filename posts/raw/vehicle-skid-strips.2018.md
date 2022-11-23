Lumak | 2017-03-30 21:05:32 UTC | #1

1vank had asked about how I did it, hence, this.

video
https://youtu.be/EAiks7RIpGg

SkidModel code, based on urho3d 1.4 (still, but will be migrating to 1.5 shortly :slight_smile: )
[details=code]

[code]
#define DBG_SKID_STRIPS
#define MAX_SKID_STRIPS         120
#define VERTS_PER_STRIP         4
#define INDECES_PER_STRIP       6
#define STRIP_NORMAL_OFFSET     0.005f
#define MIN_STRIP_LEN           0.4f
#define MIN_LASTPOS_CNT         4

struct SkidStrip
{
    SkidStrip() : vertsArrayValid(false), lastPosCnt(0), valid(false){}

    Vector3     pos;
    Vector3     normal;

    Vector3     v[2];

    bool        vertsArrayValid;
    int         lastPosCnt;
    bool        valid;
};

struct GeomData
{
    Vector3     pos;
    Vector3     normal;
    unsigned    color;
    Vector2     uv;
};

//=============================================================================
//=============================================================================
class SkidModel : public StaticModel
{
    OBJECT(SkidModel);

public:
    static void RegisterObject(Context* context);

    SkidModel(Context *context) : StaticModel(context)
    {
        m_StripCount = 0;
        m_fWidth = 1.0f;
    }
    virtual ~SkidModel()
    {
        m_pParentNode = NULL;
    }

    // world pos methods
    virtual void OnWorldBoundingBoxUpdate();
    void SetParentNode(Node *pParentNode);
    void UpdateWorldPos();

    // validation and set methods
    bool CreateVBuffer(const Color &color, float width);
    bool ValidateBufferElements() const;
    void SetWidth(float width)          
    { 
        m_fWidth = width; 
        m_fHalfWidth = width * 0.5f;
    }
    void SetColor(const Color &color)   
    { 
        m_Color = color; 
        m_unsignedColor = color.ToUInt();
    }

    // skid strip
    void AddStrip(const Vector3 &pos, const Vector3 &normal);
    void ClearStrip();
    bool InSkidState() const;

    const PODVector<GeomData>& GetGeomVector() 
    {
        return m_vSkidGeom;
    }

    void DebugRender(DebugRenderer *dbgRender, const Color &color);

protected:
    void CopyToBuffer();

protected:
    WeakPtr<Node> m_pParentNode;

    // strip
    PODVector<GeomData>         m_vSkidGeom;
    PODVector<unsigned short>   m_vSkidIndex;

    int         m_StripCount;
    SkidStrip   m_firstStripPoint;
    Color       m_Color;
    unsigned    m_unsignedColor;
    float       m_fWidth;
    float       m_fHalfWidth;
};

//=============================================================================
//=============================================================================
void SkidModel::RegisterObject(Context* context)
{
    context->RegisterFactory<SkidModel>();
}

void SkidModel::OnWorldBoundingBoxUpdate()
{
    if ( m_pParentNode )
    {
        worldBoundingBox_ = boundingBox_.Transformed(m_pParentNode->GetWorldTransform());
    }
    else
    {
        StaticModel::OnWorldBoundingBoxUpdate();
    }
}

void SkidModel::SetParentNode(Node *pParentNode)
{
    m_pParentNode = pParentNode;
}

void SkidModel::UpdateWorldPos()
{
    OnMarkedDirty(node_);
}

// **not used. instead, just use a model with (MASK_POSITION | MASK_NORMAL | MASK_COLOR | MASK_TEXCOORD1) elements
bool SkidModel::CreateVBuffer(const Color &color, float width)
{
    return false;
}

bool SkidModel::ValidateBufferElements() const
{
    Geometry *pGeometry = GetModel()->GetGeometry(0,0);
    VertexBuffer *pVbuffer = pGeometry->GetVertexBuffer(0);
    const unsigned uElementMask = pVbuffer->GetElementMask();
    const unsigned uRequiredMask = MASK_POSITION | MASK_NORMAL | MASK_COLOR | MASK_TEXCOORD1;
    unsigned zeroMask = ( uElementMask & ~uRequiredMask );
    return ( uElementMask & uRequiredMask ) == uRequiredMask && zeroMask == 0;
}

void SkidModel::AddStrip(const Vector3 &cpos, const Vector3 &normal)
{
    Vector3 pos = cpos + normal * STRIP_NORMAL_OFFSET; // lift the position away from the ground by NORMAL_OFFSET

    // the 1st entry of the strip
    if ( !m_firstStripPoint.valid )
    {
        m_firstStripPoint.pos    = pos;
        m_firstStripPoint.normal = normal;
        m_firstStripPoint.valid  = true;
        m_firstStripPoint.lastPosCnt = MIN_LASTPOS_CNT;
    }
    else
    {
        // calculate direction and right vectors to the previous position
        Vector3 dir = ( m_firstStripPoint.pos - pos );
        m_firstStripPoint.lastPosCnt = MIN_LASTPOS_CNT;

        // avoid creating tiny strips
        if ( dir.Length() < MIN_STRIP_LEN )
        {
            return;
        }

        dir.Normalize();
        Vector3 right = normal.CrossProduct(dir).Normalized();

        GeomData geomData[ VERTS_PER_STRIP ];

        geomData[0].pos = pos - right * m_fHalfWidth;
        geomData[1].pos = pos + right * m_fHalfWidth;
        geomData[2].pos = m_firstStripPoint.pos - right * m_fHalfWidth;
        geomData[3].pos = m_firstStripPoint.pos + right * m_fHalfWidth;

        // copy the last vert positions if present (don't exist on the very first strip)
        if ( m_firstStripPoint.vertsArrayValid )
        {
            geomData[2].pos = m_firstStripPoint.v[0];
            geomData[3].pos = m_firstStripPoint.v[1];
        }

        geomData[0].normal = normal;
        geomData[1].normal = normal;
        geomData[2].normal = m_firstStripPoint.normal;
        geomData[3].normal = m_firstStripPoint.normal;

        geomData[0].color = m_unsignedColor;
        geomData[1].color = m_unsignedColor;
        geomData[2].color = m_unsignedColor;
        geomData[3].color = m_unsignedColor;

        geomData[0].uv = Vector2(0,0);
        geomData[1].uv = Vector2(1,0);
        geomData[2].uv = Vector2(0,1);
        geomData[3].uv = Vector2(1,1);

        // 4 verts, 2 tris, vertex draw order - clockwise dir
        unsigned short triIdx[6] = { 0, 2, 1, 1, 2, 3 };

        // update the first strip (previous) data
        m_firstStripPoint.pos    = pos;
        m_firstStripPoint.normal = normal;
        m_firstStripPoint.vertsArrayValid = true;
        m_firstStripPoint.v[0] = geomData[0].pos;
        m_firstStripPoint.v[1] = geomData[1].pos;

        // shift vbuff elements to the right by 4
        if ( m_vSkidGeom.Size() < VERTS_PER_STRIP * MAX_SKID_STRIPS )
        {
            m_vSkidGeom.Resize(m_vSkidGeom.Size() + VERTS_PER_STRIP);
        }
        for ( int i = (int)m_vSkidGeom.Size() - 1; i >= 0; --i )
        {
            if ( i - VERTS_PER_STRIP >= 0 )
            {
                // shift
                memcpy( &m_vSkidGeom[i], &m_vSkidGeom[i - VERTS_PER_STRIP], sizeof(GeomData) );

                GeomData &geData = m_vSkidGeom[i];

                // fade alpha by a small bit every shift
                // Color::ToUInt() = (a << 24) | (b << 16) | (g << 8) | r;
                unsigned r = m_vSkidGeom[i].color & 0xff;
                unsigned g = (m_vSkidGeom[i].color >>  8) & 0xff;
                unsigned b = (m_vSkidGeom[i].color >> 16) & 0xff;
                unsigned a = (m_vSkidGeom[i].color >> 24);
                float fr = (float)r/255.0f;
                float fg = (float)g/255.0f;
                float fb = (float)b/255.0f;
                float fa = (float)a/255.0f;
                fa *= 0.9995f;

                m_vSkidGeom[i].color = Color( fr, fg, fb, fa ).ToUInt();
            }
        }

        memcpy( &m_vSkidGeom[0], geomData, sizeof(geomData) );

        // shift indexbuff to the right by 6
        if ( m_vSkidIndex.Size() < INDECES_PER_STRIP * MAX_SKID_STRIPS )
        {
            m_vSkidIndex.Resize(m_vSkidIndex.Size() + INDECES_PER_STRIP);
        }
        for ( int i = (int)m_vSkidIndex.Size() - 1; i >= 0; --i )
        {
            if ( i - INDECES_PER_STRIP >= 0 )
            {
                // need to add +4 offset(for newly added verts) to indeces being shifted
                m_vSkidIndex[i] = m_vSkidIndex[i - INDECES_PER_STRIP] + VERTS_PER_STRIP;
            }
        }

        memcpy( &m_vSkidIndex[0], triIdx, sizeof(triIdx) );

        //=================================
        // copy to vertex/index buffers
        #ifndef DBG_SKID_STRIPS
        CopyToBuffer();
        #endif
    }
}

void SkidModel::CopyToBuffer()
{
    Geometry *pGeometry = GetModel()->GetGeometry(0,0);
    VertexBuffer *pVbuffer = pGeometry->GetVertexBuffer(0);
    IndexBuffer *pIbuffer = pGeometry->GetIndexBuffer();
    const unsigned uElementMask = pVbuffer->GetElementMask();

    // don't need shadow - will get disabled only once
    if ( pVbuffer->IsShadowed() )
    {
        pVbuffer->SetShadowed(false);
    }
    if ( pVbuffer->GetVertexCount() != m_vSkidGeom.Size() )
    {
        pVbuffer->SetSize(m_vSkidGeom.Size(), uElementMask);
    }
    if ( pIbuffer->GetIndexCount() != m_vSkidIndex.Size() )
    {
        pIbuffer->SetSize(m_vSkidIndex.Size(), false);
    }

    void *pVertexData = (void*)pVbuffer->Lock(0, pVbuffer->GetVertexCount());
    void *pIndexData = (void*)pIbuffer->Lock(0, pIbuffer->GetIndexCount());

    if ( pVertexData && pIndexData )
    {
        memcpy( pVertexData, &m_vSkidGeom[0], sizeof(GeomData) * m_vSkidGeom.Size() );
        memcpy( pIndexData, &m_vSkidIndex[0], sizeof(unsigned short) * m_vSkidIndex.Size() );

        pVbuffer->Unlock();
        pIbuffer->Unlock();

        // update draw range
        pGeometry->SetDrawRange( TRIANGLE_LIST, 0, m_vSkidIndex.Size(), 0, m_vSkidGeom.Size() );
    }
}

void SkidModel::ClearStrip()
{
    if ( --m_firstStripPoint.lastPosCnt <= 0 )
    {
        m_firstStripPoint.valid = false;
        m_firstStripPoint.vertsArrayValid  = false;
    }
}

bool SkidModel::InSkidState() const
{
    return m_firstStripPoint.valid;
}

void SkidModel::DebugRender(DebugRenderer *dbgRender, const Color &color)
{
    for ( unsigned i = 0; i < m_vSkidGeom.Size(); i += VERTS_PER_STRIP )
    {
        dbgRender->AddLine( m_vSkidGeom[i+0].pos, m_vSkidGeom[i+1].pos, color );
        dbgRender->AddLine( m_vSkidGeom[i+0].pos, m_vSkidGeom[i+2].pos, color );
        dbgRender->AddLine( m_vSkidGeom[i+1].pos, m_vSkidGeom[i+2].pos, color );
        dbgRender->AddLine( m_vSkidGeom[i+1].pos, m_vSkidGeom[i+3].pos, color );
        dbgRender->AddLine( m_vSkidGeom[i+2].pos, m_vSkidGeom[i+3].pos, color );
    }
}

[/code]

[/details]

**NOTES:**
1) As you are aware, the vertex buffer typically contains local space positions and the positions are multiplied by parent node_'s transform, however, it's the opposite for the skidModel.  The vertex buffer contains world space positions and the parent node_'s transform is fixed at position(0,0,0) and identiy() matrix.  To render in the scene, the class overrides [b]virtual void OnWorldBoundingBoxUpdate()[/b] and passes m_pParentNode's (vehicle's) bounding box info.
2) I used existing model with (MASK_POSITION | MASK_NORMAL | MASK_COLOR | MASK_TEXCOORD1) elements because I'm too lazy to create a vbuff from scratch.

Rewrite 1 & 2 however you like.

-------------------------

Modanung | 2017-03-30 21:06:14 UTC | #2

That's exactly what [url=https://github.com/LucKeyProductions/OGTatt]OG Tatt[/url] needs; thanks for sharing! :slight_smile: 
_After I get the cars to drive._

-------------------------

Lumak | 2017-01-02 01:12:31 UTC | #3

You're welcome. I gotta admit that I looked at your tailgenerator class in Hexon to figure this out.

-------------------------

Modanung | 2017-01-02 01:12:32 UTC | #4

[quote="Lumak"]You're welcome. I gotta admit that I looked at your tailgenerator class in Hexon to figure this out.[/quote]
That's [url=https://github.com/MonkeyFirst/urho3d-component-tail-generator]CodeMonkey's work[/url], who probably got some of the inspiration from somewhere else. :slight_smile:
Unfortunately the TailGenerator component is suffering from drawing errors with the latest Urho3D. I'm expecting similar issues with the SkidStrip until the 1.5 migration.

-------------------------

Lumak | 2017-01-02 01:12:32 UTC | #5

[quote]Unfortunately the TailGenerator component is suffering from drawing errors with the latest Urho3D[/quote]

That doesn't sound good. I guess I'll also have to deal with this issue once 1.6 comes out.

-------------------------

Lumak | 2017-01-02 01:12:44 UTC | #6

This does not work in 1.5 in d3d9 or gl.  Looking into it...

-------------------------

Lumak | 2017-01-02 01:12:46 UTC | #7

Correction - it works fine in 1.5, just didn't have all my assets copied to my new build folder.

-------------------------

Modanung | 2017-01-02 01:12:46 UTC | #8

You might like to know 1vanK [url=https://github.com/MonkeyFirst/urho3d-component-tail-generator/commit/c55ac068ab9e987e11eb092a4a1f3bcd84554a84]fixed[/url] the TailGenerator some days ago.

-------------------------

Lumak | 2017-01-02 01:12:47 UTC | #9

I'm glad that's fixed for you. I'll probably download hexon again and check it out.

-------------------------

Lumak | 2017-01-02 01:12:54 UTC | #10

Re-coded the color fading.  Change that portion to this:
[code]
#define SMALL_BIT               0.99f

                // fade alpha by a small bit every shift
                // Color::ToUInt() = (a << 24) | (b << 16) | (g << 8) | r;
                unsigned a = (m_vSkidGeom[i].color >> 24);
               a = ((unsigned)Clamp((int)( (float)a * SMALL_BIT ), 0, 255)) << 24;
                m_vSkidGeom[i].color = (m_vSkidGeom[i].color & 0x00ffffff) | a;
[/code]

-------------------------

