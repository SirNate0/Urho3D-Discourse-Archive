smellymumbler | 2018-09-05 22:57:15 UTC | #1

http://blog.magnum.graphics/backstage/the-unnecessarily-short-ways-to-do-a-quaternion-slerp/

Really cool article.

-------------------------

Leith | 2019-03-22 03:43:11 UTC | #2

Nice article!

I had a related issue with Urho's inability to determine the shortest rotation between two direction vectors (which I needed to implement a basic steering behaviour).
Here's my workaround:
[code]
/// Calculate signed angle between two vectors
float SignedAngle(Vector3 from, Vector3 to, Vector3 axis)
        {
            float unsignedAngle = from.Angle(to);
            float sign = axis.DotProduct(from.CrossProduct(to));
            if(sign<0)
                unsignedAngle = -unsignedAngle;
            return unsignedAngle;
}
[/code]

-------------------------

