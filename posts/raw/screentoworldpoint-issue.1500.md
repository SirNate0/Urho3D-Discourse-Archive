codder | 2017-01-02 01:08:09 UTC | #1

Hello again,

I have a perspective camera and I want to use the mouse to move some 3D elements in the scene.
The problem I have is ScreenToWorldPoint() which return a Vector3 considering also Z coord.
What I want is to move the object only on X and Y axis according to mouse movement and keeping Z as is.

How to deal with that?

-------------------------

Jens | 2021-12-07 20:47:16 UTC | #2

If your object is at z==0, then you need to use the negative distance of the camera. So, if the camera z pos == -10, then depth==10 in the ScreenToWorldPoint().  If the object is placed at z==-5, then the depth is 5.

-------------------------

Modanung | 2021-12-08 11:56:17 UTC | #4

```C++
Vector3 ScreenToPlanePos(Camera* camera, const Vector2& screenPos, const Plane& plane)
{
    const Vector3 camPos{ camera->GetNode()->GetWorldPosition() };
    const float signedDistance{ plane.Distance(camPos) };
    const float distance{ Abs(signedDistance) };
    const Vector3 normal{ signedDistance > 0.f ? -plane.normal_ : plane.normal_ };
    const Vector3 direction{ camera->GetScreenRay(screenPos).direction_ };
    const float angle{ direction.Angle(normal) };
    const float cos{ Cos(angle) };

    return camPos + direction * distance / (cos == 0.f ? M_EPSILON : cos);
}
```

`(result - camPosition).DotProduct(camDirection) > 0.f` 

or

`Plane{ camDirection, camPosition }.Distance(result) > 0.f`

...should return `true` for positions in front of the camera and `false` for values you'd want to ignore.

-------------------------

Modanung | 2021-12-08 12:08:00 UTC | #5

Also, I forgot about `Ray::HitDistance`, which makes all this a lot more elegant and concise:

[**`Vector3 Camera::ScreenToPlanePos`**](https://gitlab.com/luckeyproductions/dry/-/blob/832b1d35d3cd7a7e81bd2329df615fb609599464/Source/Dry/Graphics/Camera.cpp#L441-450)
```
(const Vector2& screenPos, const Plane& plane) const
{
    const Ray ray{ GetScreenRay(screenPos) };
    const float distance{ ray.HitDistance(plane) };

    if (distance == M_INFINITY)
        return Vector3::ONE * M_INFINITY;

    return ray.origin_ + ray.direction_ * distance;
}
```

Making of course `result.x_ != M_INFINITY` your new filter.

-------------------------

