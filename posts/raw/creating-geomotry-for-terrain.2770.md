vivienneanthony | 2017-02-10 04:57:26 UTC | #1

I'm looking to replace the current terrain system with the following https://britonia.wordpress.com/2010/05/20/planet-geometry/#comment-97 and https://britonia.wordpress.com/2009/01/23/cube-to-sphere-terrain-projection/ . Hopefully some on the fly heightmap and texture  generation using GPU / shader.  I'm trying to understand the geometry creation on Urho3D side.


I am trying to understand the difference between the indexes in terrain.cpp and terrainpatch.cpp usage and get something to appear in screen.

A excerpt of some code is here

[code]
/// <summary
/// Builds the parent node information for this quadtree face.  The actual terrain mesh is generated in this function.
/// Note that for child nodes, there is a separate function, BuildChildNode().
/// </summary>
/// game is the current instance of the XNA game class.
/// centre is the centre of the planet face (on one of the cube edges).
/// dx is the direction of the X-Axis in local 'terrain space'.
/// dy is the direction of the Y-Axis in local 'terrain space'.
void TerrainPatch::BuildParentNode(Vector3 centre, Vector3 dx, Vector3 dy)
{
    // Define the grid size.  i.e. the number of vertices in a grid (16x16)
    unsigned int GridSize = 16;
    unsigned int GridSizePlus = 17; // GridSize + 1

    // Set buffer size
    vertexBuffer_->SetSize(GridSize*GridSize, MASK_POSITION,true);

    // Create a new buffer for data
    //unsigned int * newDataSize =  (unsigned int *)new float[GridSize * GridSize * sizeof(Vector3)];

    // Didn't work
    float* newDataSize = (float*)vertexBuffer_->Lock(0, vertexBuffer_->GetVertexCount());


    // Set buffer to this
    vertexBuffer_->SetData(newDataSize);

    // Didn't work
    //float* newDataSize = (float*)vertexBuffer_->Lock(0, vertexBuffer_->GetVertexCount());

    BoundingBox box;

    // loop through and create a grid of vertices.
    for (int u = 0; u <= GridSize; u++)
    {
        for (int v = 0; v <= GridSize; v++)
        {
            // Create the vertex grid around the centre of thecube face (which is passed into the function as Vector3 centre).
            Vector3 tempPosition = centre + (dx / GridSize) * (v - GridSize / 2) + (dy / GridSize) * (u - GridSize / 2);

            // This is where we would define the height of the vertex.
            float lfHeight = 0.0f;

            // Project the vertex onto the sphere, taking into consideration the height of the
            // vertex and the radius of the planet.  By specifying 0 as the height, we will
            // get a 'perfectly' round planet/sphere.
            unsigned int position = GridSizePlus * u + v;

            Vector3 pos = SurfaceVectorToCoordinates(tempPosition, 1.0f, lfHeight);

            // set position
            newDataSize[position] = pos.x_;
            newDataSize[position+1] = pos.y_;
            newDataSize[position+2] = pos.z_;

            box.Merge(pos);

        }
    }



    geometry_->SetIndexBuffer(indexBuffer_);
    //geometry_->SetRawVertexData(vertexBuffer_, MASK_POSITION);
    maxLodGeometry_->SetIndexBuffer(indexBuffer_);
    //maxLodGeometry_->SetRawVertexData(vertexBuffer_, MASK_POSITION);
    occlusionGeometry_->SetIndexBuffer(indexBuffer_);
   //occlusionGeometry_->SetRawVertexData(vertexBuffer_, MASK_POSITION);


    // Create the shared index data
    CreateIndexData();

    vertexBuffer_->Unlock();

    //CreateIndexData();

}
[/code]

Viv

-------------------------

