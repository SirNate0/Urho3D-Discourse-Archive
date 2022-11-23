SirNate0 | 2020-04-24 04:20:10 UTC | #1

I've done a bit of work extending the class someone else shared previously to allow a smoother appearance and allow the curve to detect if the mouse is over it. The work is by no means finished, as I intend to have a poly-spline class as well as a class to allow the editing of curves (like Blender's F-Curves, as well as hopefully allowing those to be exported and imported between Blender and Urho). For now, though, the UICurve class is about done.

Sometime in the future I'll go create a repository with all of these (or maybe a PR once everything is finished), but for now I thought some might find this useful even in a not-polished state.

---
The originals:
https://discourse.urho3d.io/t/node-graph-with-urho-ui/2048

---
The new ones:
### UICurve.h
```
#pragma once

#include <Urho3D/UI/Sprite.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/UI/UIBatch.h>
using namespace Urho3D;

class URHO3D_API UICurve : public Sprite
{
    URHO3D_OBJECT(UICurve, Sprite)
public:
    UICurve(Context* context);
    ~UICurve() {};
    ///segments for cuve rendering
    int segments_ = 25;
    ///thickness
    float thickness_ = 25.0f;
    ///flag for redrawing curve
    bool isDirty = true;
    ///define controls pts
    Vector<Vector3> controlPoints;
    /// Return UI rendering batches.
    virtual void GetBatches(PODVector<UIBatch>& batches, PODVector<float>& vertexData, const IntRect& currentScissor);
    void AddCurveSegment(UIBatch& batch, int segmentIndex, Vector3 a, Vector3 b, Vector3 c, Vector3 d);
    ///fills the path verts vectors from the control points
    void BezierCurve(int segments);
    ///Helper function that offsets the path verts and fills the quads vector
    void OffsetCurve();
    ///update path and quads
    void UpdatePath();
    ///Set and end point
    void SetEndPoint(Vector3 newPos, bool moveTangent=true);
    ///Set start point
    void SetStartPoint(Vector3 newPos, bool moveTangent = true);
    ///custom update logic
    virtual void Update(float timeStep);

    virtual void OnHover(const IntVector2& position, const IntVector2& screenPosition, int buttons, int qualifiers, Cursor* cursor);

    bool IsMouseOver(const IntVector2& point) const
    {
        return GetClosestPointTimeDistance(point).w_ <= thickness_*0.5f;
    }
    // Returns the closest point as (pt.x_, pt.y_, t_on_spline, distance_from_spline)
    Vector4 GetClosestPointTimeDistance(const IntVector2& queryPoint) const;

private:
    ///pts defining segmented curve
    Vector<Vector3> pathVerts;
    ///quads that render the curve, by offsetting or filling it
    Vector<Vector3> pathQuads;
    ///Maximum angle before we just split between two quads instead of merging with the last points
    static constexpr float MAX_SEGMENT_ANGLE = 120.0f;
};
```
### UICurve.cpp
```
#include <Urho3D/Urho3D.h>

#include "UICurve.h"

#include <Urho3D/IO/Log.h>
#include <Urho3D/UI/UI.h>

#include <Urho3D/Math/Ray.h>

#ifdef DEBUG_CURVE
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/Graphics.h>
#endif

UICurve::UICurve(Context* context) : Sprite(context)
{
    context->RegisterFactory<UICurve>("UI");
    SetName("UI-Curve");
};

void UICurve::GetBatches(PODVector<UIBatch>& batches, PODVector<float>& vertexData, const IntRect& currentScissor)
{
    if (pathQuads.Size() < 4)
        return;

    bool allOpaque = true;
    if (GetDerivedOpacity() < 1.0f || colors_[C_TOPLEFT].a_ < 1.0f || colors_[C_TOPRIGHT].a_ < 1.0f ||
        colors_[C_BOTTOMLEFT].a_ < 1.0f || colors_[C_BOTTOMRIGHT].a_ < 1.0f)
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

        AddCurveSegment(batch, i, a, b, c, d);
    }

    UIBatch::AddOrMerge(batch, batches);

    // Reset hovering for next frame
    hovering_ = false;
}

void UICurve::Update(float timeStep)
{
    auto pt = GetSubsystem<UI>()->GetCursorPosition();
    if (IsMouseOver(pt))
        colors_[0] = Color::YELLOW;
    else
        colors_[0] = Color::MAGENTA;
    UpdatePath();
}

void UICurve::OnHover(const IntVector2& position, const IntVector2& screenPosition, int buttons, int qualifiers, Cursor* cursor)
{
    colors_[0] = Color::GREEN;
    UpdatePath();

}

Pair<float, float> /*__attribute__((optimize("O0")))*/ DistanceAndDistanceAlongPtToLineSeg(const Vector3& point, const Vector3& lineA, const Vector3& lineB)
{
    // Per https://mathworld.wolfram.com/Point-LineDistance3-Dimensional.html
    Vector3 diff = lineB - lineA;
    Vector3 diff2Point = (lineA - point);
    float denom = 1.0f/diff.LengthSquared();

    float d = Sqrt((diff2Point.CrossProduct(diff)).LengthSquared() * denom);
    float t = -diff2Point.DotProduct(diff) * denom;
    float l = diff.Length();
    if (t > 1.0)
        return {(point-lineB).Length(),1.0};
    else if (t < 0.0)
        return {diff2Point.Length(),0.0};
    else
        return {d,t};
}

Vector4 UICurve::GetClosestPointTimeDistance(const IntVector2& queryPoint) const
{

    if (pathVerts.Empty())
        return {};
    else if (pathVerts.Size() == 1)
    {
        Vector2 v = {pathVerts[0].x_,pathVerts[0].y_};
        return {v.x_,v.y_,0.0,(v - Vector2(queryPoint)).Length()};
    }

#ifdef DEBUG_CURVE
    auto dr = GetSubsystem<DebugRenderer>();
    auto cam = GetSubsystem<Camera>();
    if (!dr || !cam)
    {
        URHO3D_LOGERROR("NO Debug Renderer or no Camera.");
        return {};
    }
#endif

    Vector3 pt{(float)queryPoint.x_,(float)queryPoint.y_,0};

    float minLength = M_INFINITY;
    int min = -1;
    const float t_step = 1.0f / (float)segments_;
    float t = t_step * min;
    float t_local = 0;
    for (int i = 0; i < pathVerts.Size()-1; ++i)
    {
        const Vector3& v = pathVerts[i];
        const Vector3& vNext = pathVerts[i+1];
        Pair<float, float> distTime = DistanceAndDistanceAlongPtToLineSeg(pt,v,vNext);
//        float length = Vector2{v.x_ - queryPoint.x_,v.y_ - queryPoint.y_}.Length();
        if (distTime.first_ < minLength)
        {
            minLength = distTime.first_;
            min = i;
            t_local = distTime.second_;
            t = t_step * min + t_local / (float) segments_;

#ifdef DEBUG_CURVE
            auto scale = Vector3(Vector2(GetSubsystem<Graphics>()->GetRenderTargetDimensions()),1);
            dr->AddLine(cam->ScreenToWorldPoint(v/scale+Vector3::FORWARD*0.5),cam->ScreenToWorldPoint(pt/scale+Vector3::FORWARD*0.5),Color::RED,false);
            dr->AddLine(cam->ScreenToWorldPoint(v.Lerp(vNext,t_local)/scale+Vector3::FORWARD*0.5),cam->ScreenToWorldPoint(pt/scale+Vector3::FORWARD*0.5),Color::MAGENTA,false);
            if (Abs(distTime.second_-0.5) < 0.45)
            {
                URHO3D_LOGERROR(String(distTime.second_));
                URHO3D_LOGERROR(String(t_local));
                dr->AddLine(cam->ScreenToWorldPoint(v.Lerp(vNext,t_local)/scale+Vector3::FORWARD*0.5),cam->ScreenToWorldPoint(pt/scale+Vector3::FORWARD*0.5),Color::BLUE,false);
            }
            if (v.z_ != 0.0f)
                URHO3D_LOGERROR("z: " + String(v.z_));
#endif
        }
    }

    Vector3 interp = Lerp(pathVerts[min],pathVerts[min+1], t_local);

    return {interp.x_,interp.y_,t,minLength};

}

void UICurve::UpdatePath()
{
    BezierCurve(segments_);
    OffsetCurve();
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

void UICurve::OffsetCurve()
{
    //check that path verts has a least two points
    if (pathVerts.Size() < 2)
    {
        URHO3D_LOGERROR("Not enough path verts for curve offset");
        return;
    }

    float halfThickness = thickness_ * 0.5;

    //clear
    pathQuads.Clear();

    //create the perp lines
    //ordering is

    /*************************************************************

    0          1
    |          |                }=halfThickness
    |----------|---------- etc
    |          |                }=halfThickness
    2          3

    *************************************************************/

    for (int i = 0; i < pathVerts.Size()-1; i++)
    {
        if (i == 0)
        {
            Vector3 dirVec = pathVerts[i + 1] - pathVerts[i];
            Vector3 perpVec(dirVec.y_, -dirVec.x_, 0);
            perpVec.Normalize();

            Vector3 p1 = pathVerts[i] + halfThickness * perpVec;
            Vector3 p2 = pathVerts[i] - halfThickness * perpVec;
            Vector3 p3 = pathVerts[i + 1] + halfThickness * perpVec;
            Vector3 p4 = pathVerts[i + 1] - halfThickness * perpVec;

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


            Vector3 p1 = pathVerts[i] + halfThickness * perpVec;
            Vector3 p2 = pathVerts[i] - halfThickness * perpVec;
            Vector3 p3 = pathVerts[i + 1] + halfThickness * perpVec;
            Vector3 p4 = pathVerts[i + 1] - halfThickness * perpVec;

            //push
            pathQuads.Push(p1);
            pathQuads.Push(p3);
            pathQuads.Push(p2);
            pathQuads.Push(p4);


        }

        else
        {
            Vector3 dirVec = pathVerts[i + 1] - pathVerts[i];
            Vector3 prevDirVec = pathVerts[i] - pathVerts[i - 1];
            Vector3 perpVec(dirVec.y_, -dirVec.x_, 0);
            Vector3 prevPerpVec(prevDirVec.y_, -prevDirVec.x_, 0);
            perpVec.Normalize();
            prevPerpVec.Normalize();
            if (prevPerpVec.Angle(perpVec) >= MAX_SEGMENT_ANGLE)
                prevPerpVec = perpVec;

            Vector3 p1 = pathVerts[i] + halfThickness * prevPerpVec;
            Vector3 p2 = pathVerts[i] - halfThickness * prevPerpVec;
            Vector3 p3 = pathVerts[i + 1] + halfThickness * perpVec;
            Vector3 p4 = pathVerts[i + 1] - halfThickness * perpVec;

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

void UICurve::AddCurveSegment(UIBatch& batch, int segmentIndex, Vector3 a, Vector3 b, Vector3 c, Vector3 d)
{
    const IntVector2& size = GetSize();

    float widthFloat = size.x_ / segments_;
    //args
    int x = segmentIndex * widthFloat;
    int y = 0;
    int width = (segmentIndex + 1) * widthFloat - x;//size.x_;
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
```

-------------------------

