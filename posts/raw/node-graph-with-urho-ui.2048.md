godan | 2017-01-02 01:12:33 UTC | #1

There's been a lot of talk about replacing the native Urho UI. However, after spending some serious time with it, I have to say, it has grown on me! I think a critical change was the recent decision to make UIBatch vertex data public. This meant I could create a little BezierCurve class that inherits from Sprite:

[img]https://dl.dropboxusercontent.com/u/69779082/Nodes.PNG[/img]

Nothing really special yet, but it does show that possibilities! Here is my UICurve class (Disclaimer: code might be ugly - I wrote this pretty quickly). One quick request: It would be great if UIBatch::AddQuad had a version that accepts four corner vertices (that way you can draw pretty much any arbitrary shape).

[code]
#pragma once
#include "AppIncludes.h"
#include <Urho3D/UI/Sprite.h>
#include "Urho3D/UI/UIBatch.h"
using namespace Urho3D;

class URHO3D_API UICurve : public Sprite
{
	URHO3D_OBJECT(UICurve, Sprite)
public:
	UICurve(Context* context);
	~UICurve() {};
	///segments for cuve rendering
	int segments_ = 50;
	///thickness
	float thickness_ = 3.0f;
	///flag for redrawing curve
	bool isDirty = true;
	///define controls pts
	Vector<Vector3> controlPoints;
	/// Return UI rendering batches.
	virtual void GetBatches(PODVector<UIBatch>& batches, PODVector<float>& vertexData, const IntRect& currentScissor);
	void AddCurveSegment(UIBatch& batch, Vector3 a, Vector3 b, Vector3 c, Vector3 d);
	///fills the path verts vectors from the control points
	void BezierCurve(int segments);
	///Helper function that offsets the path verts and fills the quads vector
	void OffsetCurve(float thickness);
	///pts defining segmented curve
	Vector<Vector3> pathVerts;
	///quads that render the curve, by offsetting or filling it
	Vector<Vector3> pathQuads;
	///update path and quads
	void UpdatePath();
	///Set and end point
	void SetEndPoint(Vector3 newPos, bool moveTangent=true);
	///Set start point
	void SetStartPoint(Vector3 newPos, bool moveTangent = true);
	///custom update logic
	virtual void Update(float timeStep);
};
[/code]

[code]
#include "UICurve.h"

UICurve::UICurve(Context* context) : Sprite(context)
{
	context->RegisterFactory<UICurve>("UI");
};

void UICurve::GetBatches(PODVector<UIBatch>& batches, PODVector<float>& vertexData, const IntRect& currentScissor)
{
	if (pathQuads.Size() < 4)
		return;
	
	bool allOpaque = true;
	if (GetDerivedOpacity() < 1.0f || color_[C_TOPLEFT].a_ < 1.0f || color_[C_TOPRIGHT].a_ < 1.0f ||
		color_[C_BOTTOMLEFT].a_ < 1.0f || color_[C_BOTTOMRIGHT].a_ < 1.0f)
		allOpaque = false;

	const IntVector2& size = GetSize();
	UIBatch
		batch(this, blendMode_ == BLEND_REPLACE && !allOpaque ? BLEND_ALPHA : blendMode_, currentScissor, texture_, &vertexData);

	//iterate over pathQuads and push to batch
	for (int i = 0; i < pathQuads.Size()/4; i ++)
	{
		//adjust ordering for render
		Vector3 a = pathQuads[4 * i];
		Vector3 b = pathQuads[4 * i + 1];
		Vector3 c = pathQuads[4 * i + 2];
		Vector3 d = pathQuads[4 * i + 3];

		AddCurveSegment(batch, a, b, c, d);
	}

	UIBatch::AddOrMerge(batch, batches);

	// Reset hovering for next frame
	hovering_ = false;
}

void UICurve::Update(float timeStep)
{

}

void UICurve::UpdatePath()
{
	BezierCurve(segments_);
	OffsetCurve(thickness_);
}

void UICurve::SetStartPoint(Vector3 newPos, bool moveTangent)
{
	if (controlPoints.Size() < 4)
	{
		URHO3D_LOGERROR("Control points have not been initialize.");
		return;
	}

	//get move vec
	Vector3 vec = newPos - controlPoints[0];
	controlPoints[0] = newPos;

	if (moveTangent)
	{
		controlPoints[1] += vec;
	}

	UpdatePath();
}

void UICurve::SetEndPoint(Vector3 newPos, bool moveTangent)
{
	if (controlPoints.Size() < 4)
	{
		URHO3D_LOGERROR("Control points have not been initialize.");
		return;
	}

	//get move vec
	Vector3 vec = newPos - controlPoints[3];
	controlPoints[3] = newPos;

	if (moveTangent)
	{
		controlPoints[2] += vec;
	}

	UpdatePath();
}

void UICurve::BezierCurve(int segments)
{
	int num_segments = segments;
	segments_ = segments;
	float t_step = 1.0f / (float)num_segments;

	//check that we have the right number of control points
	if (controlPoints.Size() < 4)
	{
		URHO3D_LOGERROR("Not enough control points for Bezier curve");
		return;
	}

	//clear the path verts
	pathVerts.Clear();

	//push the first point
	pathVerts.Push(controlPoints[0]);

	for (int i_step = 1; i_step <= num_segments; i_step++)
	{
		float t = t_step * i_step;
		float u = 1.0f - t;
		float w1 = u*u*u;
		float w2 = 3 * u*u*t;
		float w3 = 3 * u*t*t;
		float w4 = t*t*t;

		Vector3 nextVert(w1*controlPoints[0].x_ + w2*controlPoints[1].x_ + w3*controlPoints[2].x_ + w4*controlPoints[3].x_,
			w1*controlPoints[0].y_ + w2*controlPoints[1].y_ + w3*controlPoints[2].y_ + w4*controlPoints[3].y_);

		//push the next pt
		pathVerts.Push(nextVert);
	}

	//mark the curve for redraw
	isDirty = true;
}

void UICurve::OffsetCurve(float thickness)
{
	//check that path verts has a least two points
	if (pathVerts.Size() < 2)
	{
		URHO3D_LOGERROR("Not enough path verts for curve offset");
		return;
	}

	thickness_ = thickness;

	//clear
	pathQuads.Clear();

	//create the perp lines
	//ordering is 

	/*************************************************************
	
	0          1
	|          |
	|----------|---------- etc
	|          |
	2          3
	
	*************************************************************/

	for (int i = 0; i < pathVerts.Size()-1; i++)
	{
		if (i == 0)
		{
			Vector3 dirVec = pathVerts[i + 1] - pathVerts[i];
			Vector3 perpVec(dirVec.y_, -dirVec.x_, 0);
			perpVec.Normalize();

			Vector3 p1 = pathVerts[i] + thickness * perpVec;
			Vector3 p2 = pathVerts[i] - thickness * perpVec;
			Vector3 p3 = pathVerts[i + 1] + thickness * perpVec;
			Vector3 p4 = pathVerts[i + 1] - thickness * perpVec;

			//push
			pathQuads.Push(p1); 
			pathQuads.Push(p3);
			pathQuads.Push(p2);
			pathQuads.Push(p4);

		}
		
		else if (i == pathVerts.Size() - 2)
		{
			Vector3 dirVec = pathVerts[i] - pathVerts[i - 1];
			Vector3 perpVec(dirVec.y_, -dirVec.x_, 0);
			perpVec.Normalize();


			Vector3 p1 = pathVerts[i] + thickness * perpVec;
			Vector3 p2 = pathVerts[i] - thickness * perpVec;
			Vector3 p3 = pathVerts[i + 1] + thickness * perpVec;
			Vector3 p4 = pathVerts[i + 1] - thickness * perpVec;

			//push
			pathQuads.Push(p1);
			pathQuads.Push(p3);
			pathQuads.Push(p2);
			pathQuads.Push(p4);
			

		}

		else
		{
			Vector3 dirVec = pathVerts[i + 1] - pathVerts[i];
			Vector3 perpVec(dirVec.y_, -dirVec.x_, 0);
			perpVec.Normalize();


			Vector3 p1 = pathVerts[i] + thickness * perpVec;
			Vector3 p2 = pathVerts[i] - thickness * perpVec;
			Vector3 p3 = pathVerts[i + 1] + thickness * perpVec;
			Vector3 p4 = pathVerts[i + 1] - thickness * perpVec;

			//push
			pathQuads.Push(p1);
			pathQuads.Push(p3);
			pathQuads.Push(p2);
			pathQuads.Push(p4);
		}
	}
}

//void UICurve::BezierCurve(UIBatch& batch, Vector3 a, Vector3 b, Vector3 c, Vector3 d)
//{
//	int num_segments = 50;
//	float t_step = 1.0f / (float)num_segments;
//
//	Vector3 v1, v2, v3, v4;
//	v1 = a;
//	for (int i_step = 1; i_step <= num_segments; i_step++)
//	{
//		float t = t_step * i_step;
//		float u = 1.0f - t;
//		float w1 = u*u*u;
//		float w2 = 3 * u*u*t;
//		float w3 = 3 * u*t*t;
//		float w4 = t*t*t;
//
//		v2 = Vector3(w1*a.x_ + w2*b.x_ + w3*c.x_ + w4*d.x_, w1*a.y_ + w2*b.y_ + w3*c.y_ + w4*d.y_);
//		
//		//URHO3D_LOGINFO("bezier pt: " + String(b));
//
//		v3 = v2 + Vector3(0, 20, 0);
//		v4 = v1 + Vector3(0, 20, 0);
//
//		AddCurveSegment(batch, v1, v2, v4, v3);
//		v1 = v2;
//
//
//	}
//}

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

dragonCASTjosh | 2017-01-02 01:12:34 UTC | #2

awesome work :slight_smile: do you have example code for the whole node graph and not just the curved connectors because i was looking into making a values shader editor

-------------------------

godan | 2017-01-02 01:12:35 UTC | #3

Hey thanks! I actually do have a fully functional node graph working, but I'm not sure if I'm going to open source it (still undecided...). I will definitely post the WIP version soon, though.

Meanwhile, here are some tabbed node graphs in a docked window...Having a bit of trouble getting the UI transparency layers to work. ScrollView in particular is a bit troublesome.

[img]https://dl.dropboxusercontent.com/u/69779082/nodestabbed.PNG[/img]

-------------------------

