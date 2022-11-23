sabotage3d | 2017-01-02 01:08:42 UTC | #1

Hi guys, 
I have a bit of a headache converting unsigned char* to float array from a vertex buffer in Urho3d. I cannot figure out the offsets if I have position, normal and uvs coming from vertex data: [code]unsigned char* vertexData = (unsigned char*)vertexBuffer->Lock(0, vertexCount);[/code]
At the moment I can only get the positions offset like this: [code]const Urho3D::Vector3& p = *reinterpret_cast<const Urho3D::Vector3*>(vertexData + i * vertexSize);[/code]
Is there any neat way to convert the vertex data to array of floats?

-------------------------

Kyle00 | 2017-01-02 01:08:43 UTC | #2

Something like this for other elements?
[spoiler][code]
    m_vGeomData.Clear();
    const unsigned char *pVertexData = (const unsigned char*)pVbuffer->Lock(0, pVbuffer->GetVertexCount());

    // copy geom data
    if ( pVertexData )
    {
        unsigned uElementMask = pVbuffer->GetElementMask();
        unsigned numVertices = pVbuffer->GetVertexCount();
        unsigned vertexSize = pVbuffer->GetVertexSize();

        m_vGeomData.Resize( numVertices );

        for ( unsigned i = 0; i < numVertices; ++i )
        {
            unsigned char *pDataAlign = (unsigned char *)(pVertexData + i * vertexSize);
            GeomData geom;

            if ( uElementMask & MASK_POSITION )
            {
                Vector3 &vPos = *reinterpret_cast<Vector3*>( pDataAlign );
                pDataAlign += sizeof( Vector3 );
                geom.m_vPosition = vPos;
            }
            if ( uElementMask & MASK_NORMAL )
            {
                Vector3 &vNorm = *reinterpret_cast<Vector3*>( pDataAlign );
                pDataAlign += sizeof( Vector3 );
                geom.m_vNormal = vNorm;
            }
            if ( uElementMask & MASK_COLOR )
            {
                pDataAlign += sizeof( unsigned );
            }
            if ( uElementMask & MASK_TEXCOORD1 )
            {
                Vector2 &vUV = *reinterpret_cast<Vector2*>( pDataAlign );
                pDataAlign += sizeof( Vector2 );
                geom.m_vUV = vUV;
            }
            if ( uElementMask & MASK_TEXCOORD2 )
            {
                pDataAlign += sizeof( Vector2 );
            }
            if ( uElementMask & MASK_CUBETEXCOORD1 )
            {
                pDataAlign += sizeof( Vector2 );
            }
            if ( uElementMask & MASK_CUBETEXCOORD2 )
            {
                pDataAlign += sizeof( Vector2 );
            }
            if ( uElementMask & MASK_TANGENT )
            {
                Vector4 &tangent = *reinterpret_cast<Vector4*>( pDataAlign );
                geom.m_vTangent = tangent;
            }

    }
[/code][/spoiler]

For (float*), just reinterpret_cast to <float*>

-------------------------

cadaver | 2017-01-02 01:08:43 UTC | #3

I believe the code is going to be ugly in any case, and you'll just need to try to come up with the least ugly casting. Certainly I don't recommend any copying to a float array, because that would cost performance. Also note that not all elements are floats, for example colors and blend indices. You can look for existing code e.g. in AnimatedModel.cpp where it applies morphs to a vertex buffer.

-------------------------

sabotage3d | 2017-01-02 01:08:43 UTC | #4

Thanks a lot guys. Kyle00 your solution works well I couldn't figure it out on my own. The confusing bit is that the VertexBuffer Lock method gives us the vertex data as unsigned char*  the same as the GetRawData method in the Geometry class, but when we need to set the data back using the SetData method we need a float array. Can we just have a new method GetData that returns a float array it will make code a lot neater or just an overload of GetRawData method of the Geometry class? Please correct me if I am missing something.

-------------------------

cadaver | 2017-01-02 01:08:44 UTC | #5

VertexBuffer::SetData() accepts a void pointer, meaning any type is fine. Are you thinking of setting shader uniforms?

-------------------------

