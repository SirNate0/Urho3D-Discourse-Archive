Lys0gen | 2020-03-22 16:40:25 UTC | #1

Hello everyone,
I am currently having issues with raycasting on a CustomGeometry (TRIANGLE_STRIP). For some reason the hits do detect, but only on the first defined tri. The geometry displays fine and on previous tryouts the raycast worked perfectly on a Terrain, but I don't see what I can change here to make it work as expected.

The geometry is defined like this:

        CustomGeometry* slopeGeometry = visual->CreateComponent<CustomGeometry>();
        slopeGeometry->BeginGeometry(0, TRIANGLE_STRIP);
        slopeGeometry->DefineVertex(verts[0]);
        slopeGeometry->DefineTexCoord(tex[0]);
        slopeGeometry->DefineNormal(norms[0]);

        slopeGeometry->DefineVertex(verts[1]);
        slopeGeometry->DefineTexCoord(tex[1]);
        slopeGeometry->DefineNormal(norms[1]);

        slopeGeometry->DefineVertex(verts[2]);
        slopeGeometry->DefineTexCoord(tex[2]);
        slopeGeometry->DefineNormal(norms[2]);
        [^ tri defined by the above registers with the raycast, any more do not]
        slopeGeometry->DefineVertex(verts[3]);
        slopeGeometry->DefineTexCoord(tex[3]);
        slopeGeometry->DefineNormal(norms[3]);
        [... potentially more vertices defined here...]
        slopeGeometry->Commit();

And this is the raycast:

    unsigned int MASK = -1;//0xFFFFFFFF
    Urho3D::Ray ray = camera->GetScreenRay(input->GetMousePosition().x_/float(getWindow()->GetSize().x_), input->GetMousePosition().y_/float(getWindow()->GetSize().y_));

    PODVector<RayQueryResult> result;
    RayOctreeQuery q(result, ray, RAY_TRIANGLE, M_INFINITY, DRAWABLE_GEOMETRY, MASK);
    octree->RaycastSingle(q);

    if(result.Size() > 0){
    [... hit evaluation...]

Adding additional CustomGeometry components to the node makes them register the raycast as well - but again only on the first tri. I guess I could add a new component for every single tri but that seems like a waste.
Thanks for any help!

-------------------------

Lys0gen | 2020-03-22 18:16:40 UTC | #2

Okay sorry, fiddled a bit more with it. The solution is to change the RAY_TRIANGLE parameter of the RayOctreeQuery to either RAY_AABB or RAY_OBB.
Why, I don't quite know though.

-------------------------

Dave82 | 2020-03-22 18:04:11 UTC | #3

Try using raycast instead of ray castSingle

-------------------------

