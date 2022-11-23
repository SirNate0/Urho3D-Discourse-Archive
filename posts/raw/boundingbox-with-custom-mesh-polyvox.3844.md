Tahri | 2017-12-13 03:17:29 UTC | #1

Hello Urho Community, 

I'm using Polyvox to create an object with just vertexes. I can create the model and render it. 

However I can't seem to get the bounding box to match up with the model. 

Is there a way to set the bounding box from the geometry? I'm not sure how to approach this without manually setting the bounding box. 

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/7/794fec3f8ceebbe91b926d7ca1ccdaf1b67e6cd8.png'>

Thanks in advance! 


>Model* createVoxels()
{

			const size_t num_indices = surfaceMesh.getNoOfIndices();
			const size_t num_vertices = surfaceMesh.getNoOfVertices();
	
			std::vector<float>vertexData;
			std::vector<unsigned short> indexData;

			vertexData.resize(num_vertices);
			indexData.resize(num_indices);

			vertexData.resize(num_vertices * 3); // vertex + normal
			for (size_t i = 0; i < num_vertices; i++)
			{
				vertexData[i * 3 + 0] = surfaceMesh.getVertex(i).position.getX();
				vertexData[i * 3 + 1] = surfaceMesh.getVertex(i).position.getY();
				vertexData[i * 3 + 2] = surfaceMesh.getVertex(i).position.getZ();
				//vertexData[i * 6 + 3] = surfaceMesh.getVertex(i).normal.getX();
				//vertexData[i * 6 + 4] = surfaceMesh.getVertex(i).normal.getY();
				//vertexData[i * 6 + 5] = surfaceMesh.getVertex(i).normal.getZ();
			}

			for (unsigned int j = 0; j < num_indices ; j++) 
			{
				indexData[j] = surfaceMesh.getIndex(j);
				
			}

			vb_ = (new VertexBuffer(context_));
			ib_ = (new IndexBuffer(context_));
		

			vb_-> SetShadowed(true);
			vb_->SetSize(num_vertices, MASK_POSITION);
			vb_->SetData(&vertexData[0]);
		

			ib_->SetShadowed(true);
			ib_->SetSize(num_indices, false);
			ib_->SetData(&indexData[0]);


	float size = 30.0;
	geom_ = (new Geometry(context_));
	geom_->SetVertexBuffer(0, vb_);
	geom_->SetIndexBuffer(ib_);
	geom_->SetDrawRange(TRIANGLE_LIST, 0, ib_->GetIndexCount());
	
	testModel = (new Model(context_));
	testModel->SetNumGeometries(1);
	testModel->SetNumGeometryLodLevels(0, 1);
	testModel->SetGeometry(0, 0, geom_);

	BoundingBox * bb = new BoundingBox();
	// Define the model buffers and bounding box
	PODVector<unsigned> emptyMorphRange;
	//testModel->SetVertexBuffers(vertexData[0], emptyMorphRange, emptyMorphRange);
	//	testModel->SetIndexBuffers(dlibVector);
	testModel->SetBoundingBox(BoundingBox(Vector3(-1, -1, -1)*size, Vector3(1,1,1)*size));


	return testModel;
}

-------------------------

SirNate0 | 2017-12-13 04:18:13 UTC | #2

This might do it:
```
//Merge an array of vertices. 
BoundingBox::Merge (const Vector3 *vertices, unsigned count)
```
 Or the same arguments with BoundingBox::Define or its constructor.

-------------------------

