simonsch | 2018-03-29 11:58:59 UTC | #1

Hi,

i have a large amount of vertices to render and want to explore the best way of rendering them. (Around 4 million points). The amount of data is growing in each frame so i add a new <CustomGeometry> Component each frame. I looked up the DynamicGeometry Example but this does not work in my case. 

            CustomGeometry* localcloud = cloudnode->CreateComponent<CustomGeometry>();
            localcloud->SetMaterial(cloudmat);
            localcloud->BeginGeometry(0, POINT_LIST);
            for (int i = 0; i < vertexValues.size(); i++) {
                localcloud->DefineVertex(Vector3(vertexValues[i].position[0],
                                            vertexValues[i].position[1],
                                            -vertexValues[i].position[2]));
                localcloud->DefineNormal(Vector3(vertexValues[i].normal[0],
                                            vertexValues[i].normal[1],
                                            -vertexValues[i].normal[2]));
                localcloud->DefineColor(Color(vertexValues[i].color[0],
                                         vertexValues[i].color[1],
                                         vertexValues[i].color[2]));
            }
            localcloud->Commit();

The problem i have is that adding the vertices this way is a large overhead. My vertexValues are already in structure which is easy to bind through a normal vbo in opengl. I want to do this as well in Urho3D, so i tryed the VertexElements stuff. In my scene creation i initialize

    model = new Model(context_);
    vertexBuffer = new VertexBuffer(context_);
    geometry = new Geometry(context_);
    elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
    elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
    elements.Push(VertexElement(TYPE_VECTOR3, SEM_COLOR));

    Node* node = scene_->CreateChild("container");
    auto* object = node->CreateComponent<StaticModel>();
    object->SetModel(model);
    object->SetMaterial(cloudmat);

Then i wanted to fill the vertexbuffer with only the actual data in each frame so i added to my frame update

    vertexBuffer->SetSize(vertexValues.size(), elements, true);
    vertexBuffer->SetData(vertexValues.data());
    geometry->SetVertexBuffer(0, vertexBuffer);
    geometry->SetDrawRange(POINT_LIST, 0, 0, 0, vertexValues.size());
    model->SetNumGeometries(1);
    model->SetGeometry(0,0,geometry);

I read out the vertexBuffer and saw that it's size is allocated correctly, but in the result i don't see anything rendered. I also don't get any error message.

-------------------------

Sinoid | 2018-03-29 17:37:17 UTC | #2

What's your vertex data struct look like? That Vector3 for color looks sketchy.

-------------------------

simonsch | 2018-04-03 14:49:53 UTC | #3

Hey,

the struct looks like this
```
struct VertexData {
	float position[3];
	float normal[3];
	float color[3];
};
```
Had my color encoded as uchar before, but converted it now to float.

I should also say that rendering each pointcloud is working fine with the
```
CustomGeometry* localcloud = cloudnode->CreateComponent<CustomGeometry>();
localcloud->SetMaterial(cloudmat);
localcloud->BeginGeometry(0, POINT_LIST);
for (int i = 0; i < vertexValues.size(); i++) {
    localcloud->DefineVertex(Vector3(vertexValues[i].position[0],
                                     vertexValues[i].position[1],
                                    -vertexValues[i].position[2]));
    localcloud->DefineNormal(Vector3(vertexValues[i].normal[0],
                                     vertexValues[i].normal[1],
                                    -vertexValues[i].normal[2]));
    localcloud->DefineColor(Color(vertexValues[i].color[0],
                                     vertexValues[i].color[1],
                                     vertexValues[i].color[2]));
}
localcloud->Commit();
```
So i can ensure that all data are present and correct, position, color as well as normals. I just want to be able to use a dynamic vertexbuffer for faster data binding.

-------------------------

Sinoid | 2018-04-03 19:13:09 UTC | #4

Input elements need to match your semantics/attributes. If you're going to feed a float3 for color instead of a float4 it needs to be a float3 in the shader as well.

If you're using DX11 then set the device to debug mode so it'll print behavioural errors like those (ie. *what you're doing will not do what you think it will*).

-------------------------

simonsch | 2018-04-04 07:16:59 UTC | #5

So as far as i see it the Constructor of Color has a default value for its alpha value:

```
/// Construct from RGB values and set alpha fully opaque.
Color(float r, float g, float b) :
        r_(r),
        g_(g),
        b_(b),
        a_(1.0f)
    {
    }
````

I am using opengl, so my possibilities are limited, is there any example on how to use 
Model
Geometry
VertexBuffer
VertexElements
for rendering dynamic content?

-------------------------

Sinoid | 2018-04-04 07:32:56 UTC | #6

You just said your VertexData contains `float color[3];`, that's not the Color type.

In the shaders color is defined as `attribute vec4 iColor;`, DirectX will scream at you for doing that, OpenGL being its usual evil self will probably just use an alpha value of 0.0 since you didn't give it an alpha.

Fix your vertex data structure.

-------------------------

simonsch | 2018-04-04 07:49:43 UTC | #7

Did as you said i changed my struct to color values to
````
float color[4]; 
````
And my VertexElement 
```
elements.Push(VertexElement(TYPE_VECTOR4, SEM_COLOR));
```
But the result is the same, vertexbuffer gets filled with data but nothing is rendered.

-------------------------

Sinoid | 2018-04-04 08:50:46 UTC | #8

Unless you toss your code onto pastebin/hastebin/github-gist/github you're going to have to step through it in the debugger and see if your geometry is ever being drawn or break out RenderDoc and see the draw record to check the state.

-------------------------

simonsch | 2018-04-04 09:57:17 UTC | #9

I know it is hard to make any qualitive response on my provided information. But maybe i got it working in a most basic way now. I tried using the Dynamic Geometry Sample Code again and found out that this
```
                SharedPtr<Model> fromScratchModel(new Model(context_));
                SharedPtr<VertexBuffer> vb(new VertexBuffer(context_));
                SharedPtr<Geometry> geom(new Geometry(context_));

                // We could use the "legacy" element bitmask to define elements for more compact code, but let's demonstrate
                // defining the vertex elements explicitly to allow any element types and order
                PODVector<VertexElement> elements;
                elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
                elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
                elements.Push(VertexElement(TYPE_VECTOR4, SEM_COLOR));
                vb->SetSize(vertexValues.size(), elements);
                vb->SetData(vertexValues.data());

                geom->SetVertexBuffer(0, vb);
                geom->SetDrawRange(POINT_LIST, 0, 0,  0, vertexValues.size());

                fromScratchModel->SetNumGeometries(1);
                fromScratchModel->SetGeometry(0, 0, geom);

                Node* node = scene_->CreateChild("FromScratchObject");
                node->SetPosition(Vector3(0.0f, 0.0f, 0.0f));
                auto* object = node->CreateComponent<StaticModel>();
                object->SetMaterial(cloudmat);
                object->SetModel(fromScratchModel);
```
renders points on screen with correct position, now the problem i have is that my material seems to be not applied, or loaded. The vertices are just little dots.

-------------------------

Sinoid | 2018-04-04 10:19:19 UTC | #10

> The vertices are just little dots.

That's all they can be though. You're on GL so point-size might be emulatable by the driver but I don't believe there's anything anywhere in Urho for setting it since it's something that hasn't existed for quite a while.

Are you trying to do point-sprites? If so then you should be using BillboardSet (either as is or deriving from it).

-------------------------

simonsch | 2018-04-04 11:09:17 UTC | #11

I already have a custom shader which sets PointSize, etc... i just want to apply the corresponding material :thinking: that worked before on my CustomGeometry as well.

-------------------------

johnnycable | 2018-04-04 11:46:39 UTC | #12

There's [Spark](https://discourse.urho3d.io/t/spark-particle-engine-renderer/3670/24) too if you wanna go the particles route...

-------------------------

simonsch | 2018-04-04 11:54:39 UTC | #13

No i can't use particles. I have the above code creating me a Geometry based on my data bindings through the vertex buffer. Now i want my 'already' working pointcloudshader to be applied to this Geometry. 

For a CustomGeometry i could call 'SetMaterial', for a normal Geometry there is no function. So the only possible way to set it is for 'Static Model' which still does not apply the material with its shaders to the normal Geometry.

-------------------------

Sinoid | 2018-04-05 00:34:45 UTC | #14

Set the model before the material, you probably have nothing in to set a material on.

-------------------------

simonsch | 2018-04-05 07:26:56 UTC | #15

:see_no_evil: Captain Obvious in the most positive sense, didn't see this logical order yesterday. A lot of thx, it is now working as expected! :grin:

-------------------------

