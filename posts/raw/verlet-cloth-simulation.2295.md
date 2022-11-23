artgolf1000 | 2017-01-02 01:14:33 UTC | #1

Hi,

In my project, I need a soft stage curtain, so I ported [github.com/nnkgw/verlet_cloth](https://github.com/nnkgw/verlet_cloth) to Urho3D today.

I have optimized the performance for mobile device, on my iPad Mini Retina , CPU occupation statistics:

When disabled verlet cloth simulation:
Debug mode: 16%
Release mode: 16%

When enabled verlet cloth simulation:
Debug mode: 19%
Release mode: 17%

I use a ball to push the curtain to simulate wind, the curtain looks amazing.

Note that width = 11, height = 11, iteration = 2 are good for mobile device, the default values are good for desktop applications.

C++
[code]Node* planeNode = scene_->CreateChild("VerletCloth");
planeNode->SetPosition(Vector3(0.0f, 2.6f, 20.0f));
planeNode->SetScale(Vector3(20.0f, 10.0f, 20.0f));
StaticModel* planeObject = planeNode->CreateComponent<StaticModel>();
planeObject->SetModel(new VerletCloth(context_, 11, 11, 2, false));
planeObject->SetMaterial(cache->GetResource<Material>("Materials/Curtain.xml"));
[/code]

Material
[code]<?xml version="1.0"?>
<material>
    <technique name="Techniques/DiffUnlit.xml" quality="0" loddistance="0" />
    <texture unit="diffuse" name="Textures/Background.jpg" />
</material>
[/code]

VerletCloth.h
[code]#pragma once

#include <Urho3D/Urho3DAll.h>

/*
 Port of https://github.com/nnkgw/verlet_cloth
 to Urho3D
 */

class CParticle{
private:
    bool      m_IsMovable;
    Vector3 m_Position;
    Vector3 m_OldPosition;
    Vector3 m_Acceleration;
    
public:
    CParticle(bool is_movable, Vector3& position, Vector3& acceleration) :
    m_IsMovable(is_movable),
    m_Position(position),
    m_OldPosition(position),
    m_Acceleration(acceleration){}
    CParticle(){};
    ~CParticle(){}
    
    inline void       Update(float t){
        if (m_IsMovable){
            Vector3 tmp = m_Position;
            m_Position += (m_Position - m_OldPosition) + m_Acceleration * t * t;
            m_OldPosition = tmp;
        }
    }
    inline Vector3& GetPosition()  { return m_Position; }
    inline void       AddPosition(const Vector3 pos){
        if (m_IsMovable){
            m_Position += pos;
        }
    }
};

class CConstraint{
private:
    float      m_Distance;
    CParticle* m_Particle1;
    CParticle* m_Particle2;
    
public:
    CConstraint(CParticle* p1, CParticle* p2) :
    m_Distance(0.0f),
    m_Particle1(p1),
    m_Particle2(p2){
        Vector3 p1_to_p2 = m_Particle2->GetPosition() - m_Particle1->GetPosition();
        m_Distance = p1_to_p2.Length();
    }
    
    inline void Satisfy(){
        Vector3 p1_to_p2          = m_Particle2->GetPosition() - m_Particle1->GetPosition();
        float     diff              = p1_to_p2.Length() - m_Distance;
        Vector3 correction_vector = p1_to_p2.Normalized() * diff * 0.5f;
        m_Particle1->AddPosition( correction_vector);
        m_Particle2->AddPosition(-correction_vector);
    }
};

class CBall{
private:
    float     m_Frequency;
    Vector3 m_Position;
    float     m_Radius;
    float m_Offset;
    
public:
    CBall(float radius) :
    m_Frequency(0.0f),
    m_Position(0.0f,0.0f,0.0f),
    m_Radius(radius),
    m_Offset(RandStandardNormal() * M_PI * 2.0f){}
    
    inline void Update(float dt){
        m_Position.z_ = 1.0f + cos(m_Frequency+m_Offset);
        m_Frequency += dt * 0.2f;
        if (m_Frequency > M_PI * 2.0f){ m_Frequency -= M_PI * 2.0f; }
    }
    
    Vector3& GetPosition(){ return m_Position; }
    inline float      GetRadius()  { return m_Radius;   }
};

class CCloth{
private:
    int                      m_Width;
    int                      m_Height;
    PODVector<CParticle>   m_Particles;
    PODVector<CConstraint> m_Constraints;
    
    CParticle* GetParticle(int w, int h) {return &m_Particles[ h * m_Width + w ];}
    void       MakeConstraint(CParticle* p1, CParticle* p2) { m_Constraints.Push(CConstraint(p1, p2));}
    
public:
    CCloth(float width, float height, int num_width, int num_height):
    m_Width(num_width),
    m_Height(num_height) {
        m_Particles.Resize(m_Width * m_Height);
        for(int w = 0; w < m_Width; w++){
            for(int h = 0; h < m_Height; h++){
                Vector3 pos( width  * ((float)w/(float)(m_Width - 1) ) - width  * 0.5f,
                              -height * ((float)h/(float)(m_Height - 1)) + height * 0.5f,
                              0.0f );
                bool is_movable = (h == 0) ? false : true;
                Vector3 gravity( 0.0f, -0.98f, 0.0f );
                m_Particles[ h * m_Width + w ] = CParticle(is_movable, pos, gravity);
            }
        }
        for(int w = 0; w < m_Width; w++){
            for(int h = 0; h < m_Height; h++){           // structual constraint
                if (w < m_Width  - 1){ MakeConstraint(GetParticle(w, h), GetParticle(w+1, h  )); }
                if (h < m_Height - 1){ MakeConstraint(GetParticle(w, h), GetParticle(w,   h+1)); }
                if (w < m_Width  - 1 && h < m_Height - 1){ // shear constraint
                    MakeConstraint(GetParticle(w,   h), GetParticle(w+1, h+1));
                    MakeConstraint(GetParticle(w+1, h), GetParticle(w,   h+1));
                }
            }
        }
        for(int w = 0; w < m_Width; w++){
            for(int h = 0; h < m_Height; h++){           // bend constraint
                if (w < m_Width  - 2){ MakeConstraint(GetParticle(w, h), GetParticle(w+2, h  )); }
                if (h < m_Height - 2){ MakeConstraint(GetParticle(w, h), GetParticle(w,   h+2)); }
                if (w < m_Width  - 2 && h < m_Height - 2){
                    MakeConstraint(GetParticle(w,   h), GetParticle(w+2, h+2));
                    MakeConstraint(GetParticle(w+2, h), GetParticle(w,   h+2));
                }
            }
        }
    }
    ~CCloth(){}
    
    inline Vector3& GetPosition(int w, int h)  { return m_Particles[ h * m_Width + w ].GetPosition(); }
    
    void Update(float dt, CBall* ball, int iteration){
        PODVector<CParticle>::Iterator particle;
        for(particle = m_Particles.Begin(); particle != m_Particles.End(); particle++){
            (*particle).Update(dt);
        }
        for(int i = 0; i < iteration; i++){
            for(particle = m_Particles.Begin(); particle != m_Particles.End(); particle++){
                Vector3 vec    = (*particle).GetPosition() - ball->GetPosition();
                float     length = vec.Length();
                float     radius = ball->GetRadius() * 1.4f; // fake radius
                if (length < radius) {
                    (*particle).AddPosition(vec.Normalized() * (radius - length));
                }
            }
            PODVector<CConstraint>::Iterator constraint;
            for(constraint = m_Constraints.Begin(); constraint != m_Constraints.End(); constraint++){
                (*constraint).Satisfy();
            }
        }
    }
};

/// Custom logic component for rotating a scene node.
class VerletCloth : public Model
{
    URHO3D_OBJECT(VerletCloth, Model);
    
public:
    /// Construct.
    VerletCloth(Context* context, int width = 21, int height = 21, int iteration = 5, bool updateNormal = false) :
    Model(context),
    width_(width),
    height_(height),
    iteration_(iteration),
    updateNormal_(updateNormal),
    cloth_(nullptr),
    ball_(nullptr),
    buffer_(nullptr)
    {
        cloth_ = new CCloth(1.0f, 1.0f, width_, height_);
        ball_ = new CBall(0.05f);
        
        CreateScratchModel();
        
        buffer_ = GetGeometry(0, 0)->GetVertexBuffer(0);

        // Subscribe HandleUpdate() function for processing update events
        SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(VerletCloth, HandleUpdate));
    }
    
    virtual ~VerletCloth()
    {
        if (cloth_) {
            delete cloth_;
            cloth_ = nullptr;
        }
        if (ball_) {
            delete ball_;
            ball_ = nullptr;
        }
        buffer_ = nullptr;
    }
    
    void HandleUpdate(StringHash eventType, VariantMap& eventData)
    {
        using namespace Update;
        
        // Take the frame time step, which is stored as a float
        float timeStep = 0.0333333333f;//eventData[P_TIMESTEP].GetFloat();
        
        cloth_->Update(timeStep, ball_, iteration_);
        ball_->Update(timeStep);
        
        float* vertexData = (float*)buffer_->Lock(0, buffer_->GetVertexCount());
        if (vertexData)
        {
            // Update vertices
            for (int w=0; w<width_; w++) {
                for (int h=0; h<height_; h++) {
                    Vector3& src = cloth_->GetPosition(w, h);
                    Vector3& dest = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w) * 8);
                    dest = src;
                }
            }
            // Update normals
            if (updateNormal_) {
                for (int w=0; w<width_; w++) {
                    for (int h=0; h<height_; h++) {
                        Vector3 n1, n2, n3, n4, n5, n6;
                        // Detect surrounding triangles
                        if (w-1>0 && h-1>0) {
                            Vector3& v1 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w - 1) * 8);
                            Vector3& v2 = *reinterpret_cast<Vector3*>(vertexData + ((h - 1) * width_ + w - 1) * 8);
                            Vector3& v3 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w) * 8);
                            n1 = (v2 - v1).CrossProduct(v3 - v2).Normalized();
                        }
                        if (w-1>0 && h-1>0) {
                            Vector3& v1 = *reinterpret_cast<Vector3*>(vertexData + ((h - 1) * width_ + w - 1) * 8);
                            Vector3& v2 = *reinterpret_cast<Vector3*>(vertexData + ((h - 1) * width_ + w) * 8);
                            Vector3& v3 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w) * 8);
                            n2 = (v2 - v1).CrossProduct(v3 - v2).Normalized();
                        }
                        if (w+1<width_ && h-1>0) {
                            Vector3& v1 = *reinterpret_cast<Vector3*>(vertexData + ((h - 1) * width_ + w) * 8);
                            Vector3& v2 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w + 1) * 8);
                            Vector3& v3 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w) * 8);
                            n3 = (v2 - v1).CrossProduct(v3 - v2).Normalized();
                        }
                        if (w+1<width_ && h+1<height_) {
                            Vector3& v1 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w + 1) * 8);
                            Vector3& v2 = *reinterpret_cast<Vector3*>(vertexData + ((h + 1) * width_ + w + 1) * 8);
                            Vector3& v3 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w) * 8);
                            n4 = (v2 - v1).CrossProduct(v3 - v2).Normalized();
                        }
                        if (w+1<width_ && h+1<height_) {
                            Vector3& v1 = *reinterpret_cast<Vector3*>(vertexData + ((h + 1) * width_ + w + 1) * 8);
                            Vector3& v2 = *reinterpret_cast<Vector3*>(vertexData + ((h + 1) * width_ + w) * 8);
                            Vector3& v3 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w) * 8);
                            n5 = (v2 - v1).CrossProduct(v3 - v2).Normalized();
                        }
                        if (w-1>0 && h+1<height_) {
                            Vector3& v1 = *reinterpret_cast<Vector3*>(vertexData + ((h + 1) * width_ + w) * 8);
                            Vector3& v2 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w - 1) * 8);
                            Vector3& v3 = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w) * 8);
                            n6 = (v2 - v1).CrossProduct(v3 - v2).Normalized();
                        }
                        Vector3& n = *reinterpret_cast<Vector3*>(vertexData + (h * width_ + w) * 8 + 3);
                        // Average surrounding normals
                        n = (n1 + n2 + n3 + n4 + n5 + n6).Normalized();
                    }
                }
            }
            
            buffer_->Unlock();
        }
    }

private:
    void CreateScratchModel()
    {
        const unsigned numVertices = width_ * height_;
        const unsigned numIndices = (width_-1) * (height_-1) * 6;
        
        float* vertexData = new float[numVertices * 8];
        memset(vertexData, 0, numVertices * 8 * sizeof(float));
        // Fill vertex buffer
        for (int w=0; w<width_; w++) {
            for (int h=0; h<height_; h++) {
                // Vertex
                vertexData[(h * width_ + w) * 8    ] = (float)w / (float)(width_ - 1) - 0.5f;
                vertexData[(h * width_ + w) * 8 + 1] = -(float)h / (float)(height_ - 1) + 0.5f;
                vertexData[(h * width_ + w) * 8 + 2] = 0.0f;
                // Normal
                vertexData[(h * width_ + w) * 8 + 3] = 0.0f;
                vertexData[(h * width_ + w) * 8 + 4] = 0.0f;
                vertexData[(h * width_ + w) * 8 + 5] = -1.0f;
                // UV
                vertexData[(h * width_ + w) * 8 + 6] = (float)w / (float)(width_ - 1);
                vertexData[(h * width_ + w) * 8 + 7] = (float)h / (float)(height_ - 1);
            }
        }

        unsigned short* indexData = new unsigned short[numIndices];
        memset(indexData, 0, numIndices * sizeof(unsigned short));
        // Fill index buffer
        for (int w=0; w<width_-1; w++) {
            for (int h=0; h<height_-1; h++) {
                // Triangle one, clockwise order.
                indexData[(h * (width_ - 1) + w) * 6    ] = h * width_ + w;
                indexData[(h * (width_ - 1) + w) * 6 + 1] = h * width_ + w + 1;
                indexData[(h * (width_ - 1) + w) * 6 + 2] = (h + 1) * width_ + w + 1;
                // Triangle two, clockwise order.
                indexData[(h * (width_ - 1) + w) * 6 + 3] = h * width_ + w;
                indexData[(h * (width_ - 1) + w) * 6 + 4] = (h + 1) * width_ + w + 1;
                indexData[(h * (width_ - 1) + w) * 6 + 5] = (h + 1) * width_ + w;
            }
        }
        
        SharedPtr<VertexBuffer> vb(new VertexBuffer(context_));
        SharedPtr<IndexBuffer> ib(new IndexBuffer(context_));
        SharedPtr<Geometry> geom(new Geometry(context_));
        
        // Shadowed buffer needed for raycasts to work, and so that data can be automatically restored on device loss
        vb->SetShadowed(true);
        // We could use the "legacy" element bitmask to define elements for more compact code, but let's demonstrate
        // defining the vertex elements explicitly to allow any element types and order
        PODVector<VertexElement> elements;
        elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
        elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
        elements.Push(VertexElement(TYPE_VECTOR2, SEM_TEXCOORD));
        vb->SetSize(numVertices, elements);
        vb->SetData(vertexData);
        
        ib->SetShadowed(true);
        ib->SetSize(numIndices, false);
        ib->SetData(indexData);
        
        geom->SetVertexBuffer(0, vb);
        geom->SetIndexBuffer(ib);
        geom->SetDrawRange(TRIANGLE_LIST, 0, numIndices);
        
        SetNumGeometries(1);
        SetGeometry(0, 0, geom);
        SetBoundingBox(BoundingBox(Vector3(-0.5f, -0.5f, 0.0f), Vector3(0.5f, 0.5f, 0.0f)));
        
        delete [] vertexData;
        delete [] indexData;
    }

    int width_;
    int height_;
    int iteration_;
    bool updateNormal_;
    CCloth* cloth_;
    CBall* ball_;
    VertexBuffer* buffer_;
};
[/code]

-------------------------

ghidra | 2017-01-02 01:14:34 UTC | #2

Nice one!
Could I pester you for a short video showing the verlet effect running in engine?

-------------------------

artgolf1000 | 2017-01-02 01:14:35 UTC | #3

I have just uploaded a short video: [url]https://youtu.be/zIpupeSpXl4[/url]

-------------------------

rasteron | 2017-01-02 01:14:43 UTC | #4

I'm always fascinated in anything Verlet Physics, so great job! ..and just in time for the coming holiday season!   :bulb:

-------------------------

