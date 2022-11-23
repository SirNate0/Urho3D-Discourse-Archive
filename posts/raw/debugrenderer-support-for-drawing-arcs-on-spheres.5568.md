Leith | 2019-09-12 08:14:44 UTC | #1

Here's a screen shot that shows an arc being drawn between two points on the surface of a sphere.
Note the orange arc, drawn between the two purple vectors...
I plan to use it as part of an orientation widget, to help visualize a proposed quaternion-slerp.

![Screenshot%20from%202019-09-12%2017-35-40|690x388](upload://9K6yopw3OIDcda5ip2duZQQygew.jpeg) 

Here's the code:
[code]
void DebugRenderer::AddArc(const Sphere& sphere, const Vector3& from, const Vector3& to, const Color& color, int steps, bool depthTest)
{
    Vector3 prevPoint, nextPoint;

    float omega = Acos(from.DotProduct(to));
    float d = Sin(omega);

    for(float t=0; t<=1.0f; t+=1.0f / (float)steps){
        prevPoint = nextPoint;
        float s0 = Sin((1.0f - t) * omega);
        float s1 = Sin(t * omega);
        nextPoint = (from * s0 + to * s1) / d;
        if(t>0)
            AddLine(prevPoint*sphere.radius_+sphere.center_, nextPoint*sphere.radius_+sphere.center_, color, depthTest);
    }
}
[/code]

The two input vectors are assumed to be direction normals (from origin of sphere to each surface point).

I hope others find this useful :)

-------------------------

