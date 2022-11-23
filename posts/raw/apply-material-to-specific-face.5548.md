nodageboh | 2019-09-04 00:25:42 UTC | #1

I am experimenting with Urho3D a little bit, and I am trying to find out how do I apply a material to a specific face. I'm using the built-in cube as an example. How can I apply one material to top and bottom faces, and another for sides?

-------------------------

Modanung | 2019-09-04 09:04:51 UTC | #2

You could create a cube map texture and set it as your material's diffuse, taking the skybox as example:
```
<cubemap>
    <face name="BrightDay1_PosX.dds" />
    <face name="BrightDay1_NegX.dds" />
    <face name="BrightDay1_PosY.dds" />
    <face name="BrightDay1_NegY.dds" />
    <face name="BrightDay1_PosZ.dds" />
    <face name="BrightDay1_NegZ.dds" />
    <quality low="0" />
</cubemap>
```

-------------------------

k7x | 2019-09-04 09:07:18 UTC | #3

@nodageboh,
I think you should get acquainted with
1) VectorBuffer + IndexBuffer
2) VertexElements & Geometry
3) Model
4) StaticModel

That is, to add materials to the model, you need to break this model into separate geometries where the VectorBuffer and Index buffer will contain vertices to which you will assign the material you need.

        Geometry@ geometry = Geometry();
		VertexBuffer vb;
		IndexBuffer ib;
		
		vb.shadowed = true;
		ib.shadowed = true;
		
		vb.SetSize(numVertex, elements);
		ib.SetSize(numTris * 3, false);
			
		vb.SetData(vertexData);
		ib.SetData(indexData);	
			
		geometry.SetVertexBuffer(0, vb);
		geometry.SetIndexBuffer(ib);
		geometry.SetDrawRange(TRIANGLE_LIST, 0, ib.indexCount);

Elements example:

    VertexElement[] elements;
    elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
    elements.Push(VertexElement(TYPE_UBYTE4_NORM, SEM_NORMAL));
    elements.Push(VertexElement(TYPE_VECTOR2, SEM_TEXCOORD));

When this is done you will have a few Geometry @

Next we create the @ model and paste our geometries into it

    model.SetGeometry(0, 0, geometry);

To the end, set the model for the Static Model @ 

    (StaticModel) object.model = model;

And assign your material 

    object.materials[1] = material;

-------------------------

