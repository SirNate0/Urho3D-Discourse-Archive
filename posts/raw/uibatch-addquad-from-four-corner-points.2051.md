godan | 2017-01-02 01:12:35 UTC | #1

To facilitate drawing custom shapes in the UI, it would be great to have a version of UIBatch::AddQuad that takes four corner points (either IntVector2 or Vector3, doesn't really matter). The following code is a basic implementation (although ignore some of the hardcoded variables...):

[code]

void UICurve::AddCurveSegment(UIBatch& batch, Vector3 a, Vector3 b, Vector3 c, Vector3 d)
{
	//args
	int x = 0;
	int y = 0;
	const IntVector2& size = GetSize();
	int width = size.x_;
	int height = size.y_;
	Matrix3x4 transform = GetTransform();
	int texOffsetX = imageRect_.left_;
	int texOffsetY = imageRect_.top_;
	int texWidth = imageRect_.right_ - imageRect_.left_;
	int texHeight = imageRect_.bottom_ - imageRect_.top_;

	//URHO3D_LOGINFO("a: " + String(a) + ",b: " + String(b) + ",c: " + String(c) + ",d: " + String(d));
	

	//logic
	unsigned topLeftColor, topRightColor, bottomLeftColor, bottomRightColor;

	if (!batch.useGradient_)
	{
		// If alpha is 0, nothing will be rendered, so do not add the quad
		if (!(batch.color_ & 0xff000000))
			return;

		topLeftColor = batch.color_;
		topRightColor = batch.color_;
		bottomLeftColor = batch.color_;
		bottomRightColor = batch.color_;
	}
	else
	{
		topLeftColor = batch.GetInterpolatedColor(x, y);
		topRightColor = batch.GetInterpolatedColor(x + width, y);
		bottomLeftColor = batch.GetInterpolatedColor(x, y + height);
		bottomRightColor = batch.GetInterpolatedColor(x + width, y + height);
	}

/*	Vector3 v1 = (transform * Vector3((float)x, (float)y, 0.0f)) - batch.posAdjust;
	Vector3 v2 = (transform * Vector3((float)x + (float)width, (float)y, 0.0f)) - batch.posAdjust;
	Vector3 v3 = (transform * Vector3((float)x, (float)y + (float)height, 0.0f)) - batch.posAdjust;
	Vector3 v4 = (transform * Vector3((float)x + (float)width, (float)y + (float)height, 0.0f)) - batch.posAdjust*/;

	Vector3 v1 = (transform * a) - batch.posAdjust;
	Vector3 v2 = (transform * b) - batch.posAdjust;
	Vector3 v3 = (transform * c) - batch.posAdjust;
	Vector3 v4 = (transform * d) - batch.posAdjust;

	float leftUV = 0.0f; // ((float)texOffsetX) * batch.invTextureSize_.x_;
	float topUV = 0.0f;// ((float)texOffsetY) * batch.invTextureSize_.y_;
	float rightUV = 1.0f;// ((float)(texOffsetX + (texWidth ? texWidth : width))) *batch.invTextureSize_.x_;
	float bottomUV = 1.0f;// ((float)(texOffsetY + (texHeight ? texHeight : height))) * batch.invTextureSize_.y_;

	unsigned begin = batch.vertexData_->Size();
	batch.vertexData_->Resize(begin + 6 * UI_VERTEX_SIZE);
	float* dest = &(batch.vertexData_->At(begin));
	batch.vertexEnd_ = batch.vertexData_->Size();

	dest[0] = v1.x_;
	dest[1] = v1.y_;
	dest[2] = 0.0f;
	((unsigned&)dest[3]) = topLeftColor;
	dest[4] = leftUV;
	dest[5] = topUV;

	dest[6] = v2.x_;
	dest[7] = v2.y_;
	dest[8] = 0.0f;
	((unsigned&)dest[9]) = topRightColor;
	dest[10] = rightUV;
	dest[11] = topUV;

	dest[12] = v3.x_;
	dest[13] = v3.y_;
	dest[14] = 0.0f;
	((unsigned&)dest[15]) = bottomLeftColor;
	dest[16] = leftUV;
	dest[17] = bottomUV;

	dest[18] = v2.x_;
	dest[19] = v2.y_;
	dest[20] = 0.0f;
	((unsigned&)dest[21]) = topRightColor;
	dest[22] = rightUV;
	dest[23] = topUV;

	dest[24] = v4.x_;
	dest[25] = v4.y_;
	dest[26] = 0.0f;
	((unsigned&)dest[27]) = bottomRightColor;
	dest[28] = rightUV;
	dest[29] = bottomUV;

	dest[30] = v3.x_;
	dest[31] = v3.y_;
	dest[32] = 0.0f;
	((unsigned&)dest[33]) = bottomLeftColor;
	dest[34] = leftUV;
	dest[35] = bottomUV;
}
[/code]

-------------------------

cadaver | 2017-01-02 01:12:38 UTC | #2

Added here:

[github.com/urho3d/Urho3D/commit ... b28c87611c](https://github.com/urho3d/Urho3D/commit/37e3c8269de891929a8c12b0ab5b94b28c87611c)

-------------------------

godan | 2017-01-02 01:12:40 UTC | #3

Amazing! Thanks.

-------------------------

