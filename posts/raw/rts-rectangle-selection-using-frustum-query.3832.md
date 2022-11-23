ab4daa | 2017-12-10 04:55:59 UTC | #1

Hi, 
I am trying doing typical RTS unit selection by dragging a rectangle on screen.
![screen|690x438](upload://5dAWnOd2S6OQY48xRA8CkuDbl3E.png)

I saw the Frustum.c and thought I can manipulate vertices of camera frustum to be the frustum of the rectangle part.
![frustum|374x414](upload://83KO6QOXOk6VpW8hgETVkcOxno3.png)
The code is projecting the 4 points of the rectangle to near plane and far plane of camera frustum, then using projected points to form a new frustum for query.

It doesn't work.
Could I know what's wrong with it?
Thanks
<pre>
<code class="cpp">
IntVector2 rectPos;
IntVector2 rectEnd;
rectPos.x_ = Min(drag_start.x_, pos.x_);
rectPos.y_ = Max(drag_start.y_, pos.y_);
rectEnd.x_ = Max(drag_start.x_, pos.x_);
rectEnd.y_ = Min(drag_start.y_, pos.y_);
if (rectEnd.x_ > rectPos.x_ && rectPos.y_ > rectEnd.y_)
{
	Graphics* graphics = GetSubsystem&lt;Graphics>();
	Camera* camera = cameraNode_->GetComponent&lt;Camera>();
	Frustum fr = camera->GetFrustum();
	Ray lefttopRectRay = camera->GetScreenRay((float)rectPos.x_ / graphics->GetWidth(), (float)rectPos.y_ / graphics->GetHeight());
	float dNear = lefttopRectRay.HitDistance(fr.planes_[PLANE_NEAR]);
	float dFar = lefttopRectRay.HitDistance(fr.planes_[PLANE_FAR]);
	fr.vertices_[3] = lefttopRectRay.origin_ + dNear * lefttopRectRay.direction_;
	fr.vertices_[7] = lefttopRectRay.origin_ + dFar * lefttopRectRay.direction_;

	Ray leftbottomRectRay = camera->GetScreenRay((float)rectPos.x_ / graphics->GetWidth(), (float)rectEnd.y_ / graphics->GetHeight());
	dNear = leftbottomRectRay.HitDistance(fr.planes_[PLANE_NEAR]);
	dFar = leftbottomRectRay.HitDistance(fr.planes_[PLANE_FAR]);
	fr.vertices_[2] = leftbottomRectRay.origin_ + dNear * leftbottomRectRay.direction_;
	fr.vertices_[6] = leftbottomRectRay.origin_ + dFar * leftbottomRectRay.direction_;

	Ray righttopRectRay = camera->GetScreenRay((float)rectEnd.x_ / graphics->GetWidth(), (float)rectPos.y_ / graphics->GetHeight());
	dNear = righttopRectRay.HitDistance(fr.planes_[PLANE_NEAR]);
	dFar = righttopRectRay.HitDistance(fr.planes_[PLANE_FAR]);
	fr.vertices_[0] = righttopRectRay.origin_ + dNear * righttopRectRay.direction_;
	fr.vertices_[4] = righttopRectRay.origin_ + dFar * righttopRectRay.direction_;

	Ray rightbottomRectRay = camera->GetScreenRay((float)rectEnd.x_ / graphics->GetWidth(), (float)rectEnd.y_ / graphics->GetHeight());
	dNear = rightbottomRectRay.HitDistance(fr.planes_[PLANE_NEAR]);
	dFar = rightbottomRectRay.HitDistance(fr.planes_[PLANE_FAR]);
	fr.vertices_[1] = rightbottomRectRay.origin_ + dNear * rightbottomRectRay.direction_;
	fr.vertices_[5] = rightbottomRectRay.origin_ + dFar * rightbottomRectRay.direction_;

	fr.UpdatePlanes();

	PODVector&lt;Drawable *> results;
	FrustumOctreeQuery query(results, fr);
	scene_->GetComponent&lt;Octree>()->GetDrawables(query);
	URHO3D_LOGINFO(Urho3D::String("select ") + Urho3D::String(results.Size()) + Urho3D::String(" things"));
	for (unsigned int ii = 0; ii < results.Size(); ii++)
	{
		URHO3D_LOGINFO(Urho3D::String("select ") + Urho3D::String(results[ii]->GetNode()->GetName()));
	}
}
</code>
</pre>

-------------------------

ab4daa | 2017-12-10 07:45:02 UTC | #2

The rect should be 
<pre><code class="cpp">IntVector2 rectPos;
IntVector2 rectEnd;
rectPos.x_ = Min(drag_start.x_, pos.x_);
rectPos.y_ = Min(drag_start.y_, pos.y_);
rectEnd.x_ = Max(drag_start.x_, pos.x_);
rectEnd.y_ = Max(drag_start.y_, pos.y_);
if (rectEnd.x_ > rectPos.x_ && rectEnd.y_ > rectPos.y_)
</code></pre>

It still doesn't work always.
Sometimes hitdistance on near plane will return infinite, how does it happen?
The near plane should be always in front of camera, isn't it?

-------------------------

George1 | 2017-12-10 07:54:44 UTC | #3

Just curious
How long have you tried it?

    Rect r = Rect((float)minX/w, (float)minY/ h, (float)maxX/ w, (float)maxY/ h);
    for (int i = 0; i < lstEnt.Size(); ++i)
    			{
    Vector2 pos = cameraNode_->GetComponent<Camera>()->WorldToScreenPoint(lstEnt[i]->GetNode()->GetWorldPosition());
    				
    				if (r.IsInside(pos))
    				{
    					AddSelectedNode(lstEnt[i]->GetNode());
    				}
    }

-------------------------

ab4daa | 2017-12-10 08:06:53 UTC | #4

Hi George1
Because there will be a lot of objects(at least 10,000~20,000), I want to take advantage of octree.

By adding a nearclip using GetSplitFrustum, it seems OK now.
<pre><code class="cpp">Frustum fr = camera->GetSplitFrustum(1.0f, 1000.0f);</code></pre>

-------------------------

George1 | 2017-12-10 08:08:06 UTC | #5

Great
Thanks for the detail.

Best regards

-------------------------

