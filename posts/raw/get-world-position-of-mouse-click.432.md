setzer22 | 2017-01-02 01:00:21 UTC | #1

I made this and I feel like posting it as a code snippet. If you notice anything weird on it I'd also like to know!

Given the mouse input in normalized screen coordinates it calculates the first collision point (you can mask it to ignore geometries) with the geometry.

[code]
void screenToWorld(Vector2 normalizedScreenPos, Camera* camera, Octree* octree) {
    uint MASK = -1;
    PODVector<RayQueryResult> result;
    Ray ray = camera->GetScreenRay(normalizedScreenPos.x_,normalizedScreenPos.y_);
    RayOctreeQuery q (result, ray, RAY_TRIANGLE, M_INFINITY, DRAWABLE_GEOMETRY, MASK);
    octree->RaycastSingle(q);
    //now use result[0].position_  for the collision point.
}[/code]

Note that the mask is -1 for this example. This means that the value stored in it (in hexadecimal) is 0xFFFFFFFF, i.e. all bits to 1. Masks work using the bitwise AND operator (&) against the view mask of the geometry. If (MASK & model_viewmask == 0), the geometry for that model gets ignored. So if you want to ignore some layers you'll have to do some extra work modifying the view masks for the models in your scene. 

This works for me, and many games might benefit from it as well, but for anything more advanced you should take a look at the documentation / source code for the classes 

[ul][li][b]RayQueryResult[/b]: If you want to get other data from the collision, like the normal.
[/li]
[li][b]Octree[/b], [b]OctreeQuery[/b] and [b]Ray[/b]: To get a more comprehensive view on how everything works, and check out any other ways you might want to query an Octree rather than by a RayCast.[/li][/ul]

-------------------------

