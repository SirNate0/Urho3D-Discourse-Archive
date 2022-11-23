Leith | 2019-08-13 08:38:00 UTC | #1

In order to implement intelligent steering behaviours, we need a way to know which way to turn.
I used this code as the basis for steering,

[code]
    /// Calculate signed angle between two vectors - needed for AI steering behaviours!
    float SignedAngle(Vector3 from, Vector3 to, Vector3 upVector)
    {
        float unsignedAngle = from.Angle(to);
        float sign = upVector.DotProduct(from.CrossProduct(to));
        if(sign<0)
            unsignedAngle = -unsignedAngle;
        return unsignedAngle;
    }
[/code]

Yell if it dont werk, I'll fix the post, it will be so.

-------------------------

throwawayerino | 2019-08-12 21:21:47 UTC | #2

Why not use `abs` instead of conditional? It guarantees that it won't return `-0` in some edge cases

-------------------------

George1 | 2019-08-13 00:56:36 UTC | #3

Maybe name the thread title to be something related to steering :slight_smile: 
I would create a gif and link it here to show the point.

-------------------------

TheComet | 2019-08-13 08:32:03 UTC | #4

I don't think an up vector belongs in a ```Vector3::SignedAngle``` method, given that ```Vector3::Angle``` doesn't have one either. It would however be nice to have a signed angle method:

```cpp
float Vector3::SignedAngle(const Vector3& rhs)
{
    return Angle(rhs) * Urho3D::Sign(DotProduct(CrossProduct(rhs)));
}
```

-------------------------

Leith | 2019-08-13 09:38:14 UTC | #5

TheComet - Its not really an up vector, its a vector we expect to be "relatively" orthonormal to the other two, which acts as a reference for discerning the sign. It's an arbitrary axis for comparing against. I couldn't think of a way to entirely eliminate it, given we want to effectively perform a planar partitioning (the dot product versus some normal)
We are making a + or - decision about the state of a 3D spatial system.... a binary decision. The sign of a dot product is a binary result of a 3D comparison of two vectors.

-------------------------

Leith | 2019-08-13 08:42:03 UTC | #6

George1 - Done :slight_smile:

-------------------------

Leith | 2019-08-13 08:45:59 UTC | #7

throwawayerino - the entire point is to determine the unknown sign of a known but unsigned angle - abs eliminates sign, we want to discover it ;) The result of the dot product is a value between -1 and +1 , and we just want to know the sign, and then apply it to the unsigned angle, so we are returning a signed angle.

-------------------------

Leith | 2019-08-13 09:05:35 UTC | #8

Example implementation:
[code]
                // Compute the angle between current and new directions
                float angle = SignedAngle(currentDir, newDir, Vector3::UP);

                // Apply angular velocity
                angle *= 5 * timeStep;

                // Rotate character toward target direction
                characterNode_->Rotate( Quaternion(angle, Vector3::UP));
[/code]

-------------------------

TheComet | 2019-08-13 09:49:10 UTC | #9

https://stackoverflow.com/questions/10133957/signed-angle-between-two-vectors-without-a-reference-plane

-------------------------

Leith | 2019-08-13 09:52:36 UTC | #10

TheComet - I'll check it out, thanks for taking your time to look

-------------------------

Leith | 2019-08-14 08:04:56 UTC | #11

@TheComet - Comments indicate what I already suspected - there appears to be no reliable way to discern sign without a reference vector, and especially if our other two vectors are moving.

-------------------------

