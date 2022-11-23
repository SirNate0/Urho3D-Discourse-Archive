btschumy | 2020-07-06 14:48:45 UTC | #1

I'm hoping someone can give me a few pointers for how to do hit testing in Urho3D.  I have a scene with several BillboardSets and a few other nodes.  I am trying to learn which billboard items are hit with either touch or the mouse.

One posting I read said you needed to raycast and said the Decals sample had an example.  I am not able to figure out how to use that to accomplish hit testing.

Any words of advice?

-------------------------

Lys0gen | 2020-07-06 15:59:00 UTC | #2

Yes raycasting is what should help you. Not sure where your problem lies with it. In short you will need a check like this when you get a mouse click (or whenever you want to check)

            	unsigned int MASK = -1;//0xFFFFFFFF
            	Urho3D::Ray ray = camera->GetScreenRay(input->GetMousePosition().x_/float(window->GetSize().x_), input->GetMousePosition().y_/float(window->GetSize().y_));

            	PODVector<RayQueryResult> result;
            	RayOctreeQuery q(result, ray, RAY_AABB, M_INFINITY, DRAWABLE_GEOMETRY, MASK);
            	octree->RaycastSingle(q);

            	if(result.Size() > 0){
                	Drawable* selectedObject = result[0].drawable_;
				//we hit something!
				}

whereas *window* is your Urho3D::Graphics* window and the Urho3D::Octree* *octree* needs to be initialized, perhaps together with your camera like this

		octree = scene_->CreateComponent<Urho3D::Octree>();

The MASK property can be used to ignore certain objects but for most cases that is not necessary.

-------------------------

btschumy | 2020-07-07 14:51:25 UTC | #3

Thanks for the confirmation that this is the correct approach.  I have it mostly working now.

I need to detect taps on the billboard items.  It seems I need to use RAY_TRIANGLE rather than RAY_AABB for this to work.  If using RAY_AABB, I get a hit if I tap anywhere in the billboardSet's volume and the SubObject is always null.  If I use RAY_TRIANGLE, I only get a hit when tapping on a billboard and SubObject will contain the index of the tapped billboard.

So I do have one additional problem.  The billboards in this case can be somewhat small (they represent deep sky objects in our Galaxy).  They are hard to tap when small.  I was hoping I could use the Aabb option and just increase the size of the bounding box.  That doesn't seem like an option given what I said above.

I will either have to make the billboard larger and fill the periphery with transparent pixels, or I will need to do my own hot testing.  Any thoughts on how to write my own RaycastSingle that detects a hit on a slightly larger area than the triangles?

-------------------------

Modanung | 2020-07-07 15:30:33 UTC | #4

[quote="btschumy, post:3, topic:6247"]
I will either have to make the billboard larger and fill the periphery with transparent pixels
[/quote]

You could clamp the texture UVs by creating a `TextureName.xml` in the same folder containing:
```
<address coord="u" mode="clamp" />
<address coord="v" mode="clamp" />
```
...and modify the U/V offsets in the material's XML.

I think that should work.

-------------------------

