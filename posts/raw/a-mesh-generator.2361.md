rbnpontes | 2017-03-14 15:05:49 UTC | #1

Hello Guys, i have posted in this forum about CustomGeometry component, i have some headcache to export Mesh generated,
So i think it best Create my own mesh Generator, i will Share with community.
the i did not put texcoord parameters, if you place I'll thank

**Mesh.h**
```
#pragma once
#include <Urho3D\Urho3DAll.h>
/// Created by Ruben Pontes
/// If you like this code, please place my credits
/// i'm stay happy if you share my work
namespace REngine {
	namespace Tools {
		struct MeshFace {
			Vector3 v0;
			Vector3 v1;
			Vector3 v2;
			Vector3 normal;
			Vector2 texcoord;
		};
		typedef unsigned short ushort;
		typedef unsigned int uint;
		class Mesh : public Object {
			URHO3D_OBJECT(Mesh, Object);
		public:
			Mesh(Context* context);
			void AddFace(Vector3 v0, Vector3 v1, Vector3 v2);
			void AddFace(Vector3 v0, Vector3 v1, Vector3 v2,Vector3 normal);
			void AddFace(MeshFace face);
			void SetFace(uint i, MeshFace face);
			MeshFace GetFace(uint i);
			void Commit();
			void CalculateNormals(bool check);
			void Clear();
			void Save(String path);
			Geometry* GetGeometry();
			Model* GetModel();
			VertexBuffer* GetVertexBuffer();
			IndexBuffer* GetIndexBuffer();
		private:
			bool _calcNormals;
			Vector<MeshFace> _faces;
			SharedPtr<Geometry> _geometry;
			SharedPtr<Model> _model;
			SharedPtr<VertexBuffer> _vertexBuffer;
			SharedPtr<IndexBuffer> _indexBuffer;
			Vector<float> _vertexData;
			Vector<ushort> _indexData;
		};
	}
}
```

**Mesh.cpp**

```
#include "Mesh.h"
namespace REngine {
	namespace Tools {
		Mesh::Mesh(Context * context) : Object(context)
		{

		}
		void Mesh::AddFace(Vector3 v0, Vector3 v1, Vector3 v2)
		{
			MeshFace face;
			face.v0 = v0;
			face.v1 = v1;
			face.v2 = v2;
			AddFace(face);
		}
		void Mesh::AddFace(Vector3 v0, Vector3 v1, Vector3 v2, Vector3 normal)
		{
			MeshFace face;
			face.v0 = v0;
			face.v1 = v1;
			face.v2 = v2;
			face.normal = normal;
			AddFace(face);
		}
		void Mesh::AddFace(MeshFace face)
		{
			_faces.Push(face);
		}
		void Mesh::SetFace(uint i, MeshFace face)
		{
			assert(i >= _faces.Size());
			_faces[i] = face;
		}
		MeshFace Mesh::GetFace(uint i)
		{
			return _faces[i];
		}
		void Mesh::Commit()
		{
			BoundingBox box;
			uint lastFace = 0;
			for (uint i = 0; i < _faces.Size(); i++) {
				MeshFace face = _faces[i];
				//Calculate BoundingBox
				box.Merge(face.v0);
				box.Merge(face.v1);
				box.Merge(face.v2);
				//Assign Vertices
				_vertexData.Push(face.v0.x_);
				_vertexData.Push(face.v0.y_);
				_vertexData.Push(face.v0.z_);
				
				_vertexData.Push(face.normal.x_);
				_vertexData.Push(face.normal.y_);
				_vertexData.Push(face.normal.z_);

				_vertexData.Push(face.v1.x_);
				_vertexData.Push(face.v1.y_);
				_vertexData.Push(face.v1.z_);

				_vertexData.Push(face.normal.x_);
				_vertexData.Push(face.normal.y_);
				_vertexData.Push(face.normal.z_);

				_vertexData.Push(face.v2.x_);
				_vertexData.Push(face.v2.y_);
				_vertexData.Push(face.v2.z_);

				_vertexData.Push(face.normal.x_);
				_vertexData.Push(face.normal.y_);
				_vertexData.Push(face.normal.z_);

				_indexData.Push(lastFace);
				_indexData.Push(lastFace + 1);
				_indexData.Push(lastFace + 2);
				lastFace += 3;
			}
			// Calculate face normals now
			/*
			for (unsigned i = 0; i < _faces.Size() * 2; i += 3)
			{
				Vector3& v1 = *(reinterpret_cast<Vector3*>(&_vertexData[6 * i]));
				Vector3& v2 = *(reinterpret_cast<Vector3*>(&_vertexData[6 * (i + 1)]));
				Vector3& v3 = *(reinterpret_cast<Vector3*>(&_vertexData[6 * (i + 2)]));
				Vector3& n1 = *(reinterpret_cast<Vector3*>(&_vertexData[6 * i + 3]));
				Vector3& n2 = *(reinterpret_cast<Vector3*>(&_vertexData[6 * (i + 1) + 3]));
				Vector3& n3 = *(reinterpret_cast<Vector3*>(&_vertexData[6 * (i + 2) + 3]));

				Vector3 edge1 = v1 - v2;
				Vector3 edge2 = v1 - v3;
				n1 = n2 = n3 = edge1.CrossProduct(edge2).Normalized();
			}
			*/
			if(_model == NULL)
			_model = new Model(context_);
			if (_vertexBuffer == NULL)
			_vertexBuffer = new VertexBuffer(context_);
			if (_indexBuffer == NULL)
			_indexBuffer = new IndexBuffer(context_);
			if (_geometry == NULL)
			_geometry = new Geometry(context_);

			_vertexBuffer->SetShadowed(true);
			
			PODVector<VertexElement> elements;
			elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
			elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));

			_vertexBuffer->SetSize(_faces.Size() * 3, elements);
			_vertexBuffer->SetData(_vertexData.Buffer());

			_indexBuffer->SetShadowed(true);
			_indexBuffer->SetSize(_faces.Size() * 3, false);
			_indexBuffer->SetData(_indexData.Buffer());

			_geometry->SetNumVertexBuffers(1);
			_geometry->SetVertexBuffer(0, _vertexBuffer);
			_geometry->SetIndexBuffer(_indexBuffer);
			_geometry->SetDrawRange(TRIANGLE_LIST, 0, _faces.Size()*3);

			_model->SetNumGeometries(1);
			_model->SetGeometry(0, 0, _geometry);
			_model->SetBoundingBox(box);
			Vector<SharedPtr<VertexBuffer> > vertexBuffers;
			Vector<SharedPtr<IndexBuffer> > indexBuffers;
			vertexBuffers.Push(_vertexBuffer);
			indexBuffers.Push(_indexBuffer);
			PODVector<unsigned> morphRangeStarts;
			PODVector<unsigned> morphRangeCounts;
			morphRangeStarts.Push(0);
			morphRangeCounts.Push(0);
			_model->SetVertexBuffers(vertexBuffers, morphRangeStarts, morphRangeCounts);
			_model->SetIndexBuffers(indexBuffers);
		}
		void Mesh::CalculateNormals(bool check)
		{
			_calcNormals = check;
		}
		void Mesh::Clear()
		{
			_faces.Clear();
			_vertexData.Clear();
			_indexData.Clear();
		}
		void Mesh::Save(String path)
		{
			if (_model == NULL)
			{
				URHO3D_LOGERROR("REngine::Mesh Mesh is not Build");
				return;
			}
			File file(context_, path, FILE_WRITE);
			if (file.IsOpen()) {
				_model->Save(file);
			}
			file.Close();
		}
		Geometry * Mesh::GetGeometry()
		{
			return _geometry;
		}
		Model * Mesh::GetModel()
		{
			return _model;
		}
		VertexBuffer * Mesh::GetVertexBuffer()
		{
			return _vertexBuffer;
		}
		IndexBuffer * Mesh::GetIndexBuffer()
		{
			return _indexBuffer;
		}
	}
}
[/code]
[b]How to use[/b]
[code]
Mesh mesh = new Mesh(context_);
mesh->AddFace(Vertice0,Vertice1,Vertice2);
mesh->Commit() // Use this for build geometry
mesh->Save("c://MeshName") // If you save mesh
StaticMesh* staticMesh = new StaticMesh(context_);
staticMesh->SetModel(mesh->GetModel()); // For Display
```

**Some Screenshots using the Code**
This is my tool for generate Roads

https://scontent-gru2-1.xx.fbcdn.net/t31.0-8/14615697_1161032567300574_6593746272698322565_o.jpg

-------------------------

magic.lixin | 2017-01-02 01:14:59 UTC | #2

cool !

-------------------------

namic | 2017-01-02 01:15:10 UTC | #3

How's the performance of it? Thanks for the contribution. This should be available in the engine itself.

-------------------------

rbnpontes | 2017-01-02 01:15:11 UTC | #4

I coudn't test the performance, but i think is nearly value of CustomGeometry because i used CustomGeometry with reference

-------------------------

Victor | 2017-03-19 01:05:23 UTC | #5

I stumbled upon this thread not to long ago and decided to update the code so I could utilize it in my project. This update includes calculating normals, tangents, and uvs (not perfect). Hopefully someone else can continue to improve on the code. Thanks for your contribution @rbnpontes! 

CustomMesh.h
https://gist.github.com/victorholt/2dac4b295623afd66641e629c8b16dad

CustomMesh.cpp
https://gist.github.com/victorholt/bf2f50584095a47da6f3ca3654e93168

**Result**
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/eeb1179ad939a670f761218608ebb6d98ef1a439.png'>

-------------------------

Victor | 2017-03-19 01:10:23 UTC | #6

Just a note, I did this update really quickly... so there are definitely some inefficiencies in it which should be resolved. I'm sure some of those are easy to spot as you traverse through the code. Although, for the most part it does work pretty well.

-------------------------

