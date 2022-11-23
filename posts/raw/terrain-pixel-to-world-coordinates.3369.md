jamesbaltar | 2017-07-19 14:18:49 UTC | #1

Is there a way to get the world coordinates of a given pixel in a terrain's heightmap image? I've read through the source (Terrain.cpp) and I think I can do something like this if I have an access to the private member patchWorldOrigin_ then interpolate with this and the terrain's node transformation but I'm not sure if this is the best approach.

Just to add, what I want to do is to add an overlay to the terrain that is aligned with the heightmap vertices. These overlayed quads will display a visualization of some sort using different colors that depends on the height of the terrain where the 4 vertices of the quad touches.

Example:
h1, h2, h3,
h4, h5, h6
h7, h8, h9

Above is a simple representation of the heightmap image's pixels. What I want to do is overlay a quad per cell from h1 to h8. Note that these quads must be aligned with the vertices of the heightmap. TIA.

-------------------------

Lumak | 2017-07-19 18:26:18 UTC | #2

My personal code:
[code]
Vector3 Terrain::HeightMapToWorld(const IntVector2& pixelPosition) const
{
    if (!node_)
    {
        return Vector3::ZERO;
    }

    IntVector2 v2pos(pixelPosition.x_, numVertices_.y_ - 1 - pixelPosition.y_);
    float xPos = (float)(v2pos.x_ * spacing_.x_ + patchWorldOrigin_.x_);
    float zPos = (float)(v2pos.y_ * spacing_.z_ + patchWorldOrigin_.y_);
    Vector3 Lpos(xPos, 0, zPos);
    Vector3 WPos = node_->GetWorldTransform() * Lpos;
    WPos.y_ = GetHeight(WPos);

    return WPos;
}

[/code]
edit: modifying the code to be consistent with Terrain code as it was not written for that class but for a helper class

-------------------------

jamesbaltar | 2017-07-20 09:55:47 UTC | #3

Thanks @Lumak for a fast reply. I was hoping I wouldn't need to edit the source file but if this is what you did in yours then I'm comfortable changing the source knowing that this was also how you did it.

-------------------------

Lumak | 2017-07-20 16:46:09 UTC | #4

You don't have make changes on your end now. That function was added to the master and all you need to do is get the latest.

-------------------------

