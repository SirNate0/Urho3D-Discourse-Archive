thebluefish | 2017-01-02 00:58:58 UTC | #1

I have spent a few hours on this, and I haven't really came up with a solution.

Say I have a chest with several objects inside, and I want to know if these objects can be interacted by the player. I want it to be easy for the player to interact with several objects in a small radius around the center of the screen, ordering from nearest to the center to furthest. That way I could have a player grab several items without having to directly look at each one. Sorting the objects is no problem since I can just transform all object to screen space and sort them that way.

So far, I've filtered potential candidates with the following:
[code]Urho3D::PODVector<Urho3D::Node*> results;
GetScene()->GetChildrenWithComponent<GameItem>(results, true);
for(Urho3D::PODVector<Urho3D::Node*>::Iterator itr = results.Begin(); itr != results.End(); itr++)
{
	float distance = (_cameraNode->GetPosition() - (*itr)->GetPosition()).Length();
	Urho3D::BoundingBox box = (*itr)->GetComponent<Urho3D::StaticModel>()->GetBoundingBox();
	box.Transform((*itr)->GetTransform());
	if( Urho3D::INSIDE == camera->GetFrustum().IsInsideFast(box) && distance <= 3.0f)
	{
		debugRenderer->AddBoundingBox((*itr)->GetComponent<Urho3D::StaticModel>()->GetBoundingBox(), (*itr)->GetTransform(), Urho3D::Color::GREEN, false);
	}
}[/code]

Any ideas?

-------------------------

friesencr | 2017-01-02 00:58:58 UTC | #2

That's kind of how I have been doing a bunch of my distancy/radius maths.  I havn't tried using a physics based solution.  Something like having a giant cylinder around the character and capturing all collisons per interaction.  A mask could be used.

I don't exactly know what kind of camera you are using.  That may be helpful information.

-------------------------

thebluefish | 2017-01-02 00:58:58 UTC | #3

One of my original ideas was a cone emitting from the cameraNode pointed out at 3 units length. It worked in grabbing all of the items close by, but again it would still detect items that are hidden away. Such that a player wouldn't have to open a chest to be able to grab everything inside so long as the player was within 3 units of the content.

For the moment I've switched to using a physics-based ray query so that a convex hull at least gives better precision. I'm hoping though that I will be able to make it so that a player could grab items much like in oblivion or skyrim for example.

-------------------------

friesencr | 2017-01-02 00:58:59 UTC | #4

This looks promising:

### Drawable
Methods:
- bool IsInView(Camera@) const

-------------------------

thebluefish | 2017-01-02 00:58:59 UTC | #5

[quote="friesencr"]This looks promising:

### Drawable
Methods:
- bool IsInView(Camera@) const[/quote]

Promising indeed! As a note it only works with occluders and occludees. Here's a little snippet to easily visualize the effect:
[code]Urho3D::PODVector<Urho3D::Node*> results;
	_scene->GetChildrenWithComponent<Urho3D::StaticModel>(results, true);
	for(Urho3D::PODVector<Urho3D::Node*>::Iterator itr = results.Begin(); itr != results.End(); itr++)
	{
		float distance = (_cameraNode->GetPosition() - (*itr)->GetPosition()).Length();
		Urho3D::BoundingBox box = (*itr)->GetComponent<Urho3D::StaticModel>()->GetBoundingBox();
		box.Transform((*itr)->GetTransform());
		if( !(*itr)->GetComponent<Urho3D::StaticModel>()->IsInView(camera))
		{
			debugRenderer->AddBoundingBox((*itr)->GetComponent<Urho3D::StaticModel>()->GetBoundingBox(), (*itr)->GetTransform(), Urho3D::Color::GREEN, false);
		}
	}[/code]

This makes it so that only fully hidden objects are debug drawn. Works like a charm as long as I set my occluders correctly!

I wonder if there may be a better way in the future, though. I can't complain with this approach, but [i][b]it is[/b][/i] based off frame occlusion information, which is dependent on this such as frame size and the likes. I doubt it's a real problem though.

-------------------------

cadaver | 2017-01-02 00:58:59 UTC | #6

If your objects have Drawable components, you can use octree queries (box, sphere, frustum etc.) to get the objects within a geometrical volume. See Octree::GetDrawables(). This is the same what the rendering code is using.

For physics rigidbodies there's similar but more limited functionality, you can query the physics world by a box or sphere volume. See PhysicsWorld::GetRigidBodies() overloads.

-------------------------

