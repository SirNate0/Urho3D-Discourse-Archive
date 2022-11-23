att | 2017-01-02 01:14:09 UTC | #1

I created dynamic geometry like following, but if I add a ui element like button or label, the program will crash at
- (void)swapBuffers
{
    .......
    /* viewRenderbuffer should always be bound here. Code that binds something
     * else is responsible for rebinding viewRenderbuffer, to reduce duplicate
     * state changes. */
    [context presentRenderbuffer:GL_RENDERBUFFER];
}

and the OpenGL debug say,
[code]
"This draw call accessed a vertex outside the range of an array buffer in use."
36 glDrawArrays(GL_TRIANGLE_STRIP, 0, 200)
[/code]

if I missed or misused something?

[code]
struct VertexData
{
    Vector3 pos_;
    Vector2 uv_;
};

const int MAX_POINTS = 100;
float offset = 0;
int index = 0;
Vector<Vector2> xyPoints;
Vector<VertexData> verticesData;

for (int i=0; i<MAX_POINTS; i++)
{
        Vector2 v;
        v.x_ = index++;
        v.y_ = offset + Random(-1.0f, 1.0f);
        xyPoints.Push(v);
}

for (int i=0; i<MAX_POINTS; i++)
{
        Vector2 p = xyPoints.At(i);
        VertexData data;
        data.pos_.x_ = p.x_;
        data.pos_.y_ = -3.0f;
        data.pos_.z_ = 0;
        data.uv_.x_ = p.x_;
        data.uv_.y_ = 1;
        verticesData.Push(data);
        
        data.pos_.x_ = p.x_;
        data.pos_.y_ = p.y_;
        data.pos_.z_ = 0;
        data.uv_.x_ = p.x_;
        data.uv_.y_ = 0;
        verticesData.Push(data);
}

unsigned char* data = reinterpret_cast<unsigned char*>(verticesData.Buffer());

SharedPtr<Model> fromScratchModel(new Model(context_));
SharedPtr<VertexBuffer> vb(new VertexBuffer(context_));
SharedPtr<Geometry> geom(new Geometry(context_));
    
PODVector<VertexElement> elements;
elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
elements.Push(VertexElement(TYPE_VECTOR2, SEM_TEXCOORD));

vb->SetShadowed(false);
vb->SetSize(verticesData.Size(), elements, true);
vb->SetData(data);
    
geom->SetVertexBuffer(0, vb);
geom->SetDrawRange(TRIANGLE_STRIP, 0, 0, 0, verticesData.Size());
    
fromScratchModel->SetNumGeometries(1);
fromScratchModel->SetGeometry(0, 0, geom);
fromScratchModel->SetBoundingBox(BoundingBox(Vector3(0, -5, -1), Vector3(110, 5, 1)));
    
Node *node = scene_->CreateChild();
ResourceCache *cache = GetSubsystem<ResourceCache>();
StaticModel* object = node->CreateComponent<StaticModel>();
object->SetModel(fromScratchModel);
object->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));

UIElement *root = GetSubsystem<UI>()->GetRoot();
Button *button = root->CreateChild<Button>();
button->SetMinSize(IntVector2(100, 50));
button->SetMaxSize(IntVector2(100, 50));
button->SetSize(IntVector2(100, 50));
[/code]

-------------------------

