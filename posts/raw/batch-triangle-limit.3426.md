sabotage3d | 2017-08-06 18:23:01 UTC | #1

When I draw custom geometry with more than 50k triangle in single batch anything drawn after that is not displaying. Is there a limit of the number of triangles per batch? My class inherits from Drawable and the geometry type is set to GEOM_STATIC.

-------------------------

1vanK | 2017-08-07 08:14:49 UTC | #2

try enable `largeIndices` for IndexBuffer

-------------------------

sabotage3d | 2017-08-06 23:19:58 UTC | #3

I just tried it but when enabled it didn't display anything at all. Have anyone tried it before?

-------------------------

1vanK | 2017-08-06 23:27:41 UTC | #4

Without code I can not guess

-------------------------

sabotage3d | 2017-08-06 23:46:49 UTC | #5

This is the relevant part.
	
    batches_[batchIndex_].geometryType_ = GEOM_TRAIL_FACE_CAMERA;

    mask =  MASK_POSITION | MASK_COLOR | MASK_TEXCOORD1 | MASK_TANGENT | MASK_OBJECTINDEX;

    indexBuffer_->SetSize(numPoints_ - 1), true, false);
    vertexBuffer_->SetSize(numPoints_, mask, true);

    unsigned short* dest = (unsigned short*)indexBuffer_->Lock(0, numPoints_ - 1), true);
    if (!dest)
        return;

-------------------------

Lumak | 2017-08-07 08:14:49 UTC | #6

greater than 64k indices

[code]
unsigned* dest = (unsigned*)indexBuffer_->Lock(0, numPoints_ - 1), true);
[/code]

-------------------------

sabotage3d | 2017-08-06 23:49:25 UTC | #7

Thank you. The combination of `largeIndices` with `unsigned` instead of `unsigned short` worked.

-------------------------

