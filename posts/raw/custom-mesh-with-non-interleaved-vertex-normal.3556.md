ganibc | 2017-09-11 06:00:26 UTC | #1

Hi, 

I have mesh data that doesn't have vertex and normal interleaved (vert norm vert norm ......).
The vertices are in 1 array and the normals are in separate array (vert vert ..... vert - norm norm ..... norm).
The samples that I found are always assumed the data is interleaved. Like the code below.

> 	SharedPtr<Urho3D::VertexBuffer> vb(new Urho3D::VertexBuffer(context_));
> 	vb->SetShadowed(true);
> 	PODVector<VertexElement> elements;
> 	elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
> 	elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
> 	vb->SetSize(meshData.vertices.size(), elements);
> 	vb->SetData(meshData.vertices.data());		

How do I set the normals data without making it interleave?
Thanks.

-------------------------

Eugene | 2017-09-12 12:39:11 UTC | #2

Use two separate vertex buffers.

-------------------------

ganibc | 2017-09-12 02:37:01 UTC | #3

Hi, Thanks for the reply.
Will try the code.

Edit:
It works. Thanks again.

-------------------------

