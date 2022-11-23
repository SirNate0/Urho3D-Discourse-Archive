1vanK | 2017-01-02 01:12:58 UTC | #1

I have plane with dualside material. I use this function for raycasting:

[code]bool CanvasLogic::RaycastToCanvas(Vector3& hitPos)
{
    auto mousePos = INPUT->GetMousePosition();
    auto camera = GetScene()->GetChild("Camera")->GetComponent<Camera>();
    float x = (float)mousePos.x_ / GRAPHICS->GetWidth();
    float y = (float)mousePos.y_ / GRAPHICS->GetHeight();
    auto cameraRay = camera->GetScreenRay(x, y);
    PODVector<RayQueryResult> results;
    RayOctreeQuery query(results, cameraRay, RAY_TRIANGLE, 1000.0f, DRAWABLE_GEOMETRY);
    GetScene()->GetComponent<Octree>()->Raycast(query);
    foreach(auto result, results)
    {
        if (result.node_ == node_)
        {
            hitPos = result.position_;
            return true;
        }
    }
    return false;
}[/code]

But it works only for forward side. How to fix it?

-------------------------

1vanK | 2017-01-02 01:12:58 UTC | #2

RAY_OBB works fine for my (canvas has rectangle shape)

-------------------------

cadaver | 2017-01-02 01:12:58 UTC | #3

Ray test functions currently don't support a twosided parameter. Shouldn't be impossible to add.

-------------------------

Modanung | 2017-01-02 01:13:00 UTC | #4

Another way would be to create a model with double vertices having identical vertex positions, but opposite normals. To easily achieve this with any model in Blender:

[ul]
- Enter edit mode (Tab)
- Select all (A (x2))
- Duplicate (Shift+D)
- Cancel grab (Esc or right mouse button)
- Flip the face normals (Ctrl+F then F)
[/ul]
Note that this [i]will[/i] double the vertex count.
To restore the earlier state of the object without undo you can:

[ul]
- Select all (A (x2))
- Remove Doubles (W then R)
- Recalculate Normals (Ctrl(+Shift)+N)
[/ul]

Furthermore it might be useful to know the L key adds all elements linked to the element closest to the cursor to the selection, Shift + L deselects in the same manner.

-------------------------

