Mike | 2017-01-02 00:58:34 UTC | #1

The 3 basic indicative frameworks for partial rebuilds of the NavigationMesh when dealing with dynamic/moving objects are:

1) realtime continuous rebuild at each Update timeStep (caveat is heavy performance cost, not suitable for mobiles and often unnecessary on desktop)
2) infrequent rebuilds that can be triggered by fixed elapsed time (for example every other 2 seconds) / velocity of the moving object / distance travelled since last update / proximity of an object or anything else that makes sense in your game logic
3) one unic rebuild when the object comes to rest or when any other custom event occurs

When you call NavigationMesh::Build with a bounding box parameter, you're providing the total area you want updated. The NavigationMesh will then proceed to take a snapshot of the scene inside that box, and update all tiles that fall within it.


If you're using 2) or 3) then your object might move outside of its original tile. You will then need to merge the before-and-after bounding boxes of the object if you want the NavigationMesh to update correctly. Two solutions are provided to achieve this:

A) Merge the 2 BoundingBoxes (origin and destination) and then rebuid this merged BoundingBox. Merge is achieved using origin->Merge(destination) in C++, origin.Merge(destination) in AngelScript, BoundingBox(origin):Merge(destination) in lua (we need to make a copy of the original BoundingBox in lua because Drawable:GetWorldBoundingBox() returns a reference, not the BoundingBox itself).

B) Rebuild the 2 BoundingBoxes (navMesh:Build(origin) navMesh:Build(destination)). Use this solution if its faster than the previous one.

You can experiment with this by modifying AddOrRemoveObject() function in example 15_Navigation this way:

In AngelsScript:
[code]
    if (hitNode.name == "Mushroom")
    {
        updateBox = hitDrawable.worldBoundingBox;
        hitNode.position = hitNode.position + Vector3(10.0f, 0.0f, 0.0f); //Move mushroom to the right
        //updateBox.Merge(hitDrawable.worldBoundingBox); //Uncomment this line to check its impact
    }
[/code]

In lua:
[code]
    if hitNode.name == "Mushroom" then
        updateBox = BoundingBox(hitDrawable.worldBoundingBox)
        hitNode.position = hitNode.position + Vector3(10, 0, 0) -- Move mushroom to the right
        --updateBox:Merge(hitDrawable.worldBoundingBox) -- Uncomment this line to check its impact
    else
[/code]

Clicking middle mouse button on a mushroom will move it to the right. Try to move it inside its tile and outside of its tile, and comment/uncomment the Merge() function to see the difference.

-------------------------

