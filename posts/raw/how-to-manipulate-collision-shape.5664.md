suppagam | 2019-10-14 20:16:16 UTC | #1

Is there a way, in the Urho built-in editor, to customize the collision shape for objects? Like scaling, increasing in X, or Y, etc?

![image|501x500](upload://sMxXnqIs9YjzlOaX2rpLaVAviCf.jpeg) 

Or should I be doing the collision shapes as some sort of special layer in Blender?

-------------------------

Modanung | 2019-10-16 00:06:25 UTC | #2

The following functions of the `CollisionShape` allow you to set its position, rotation and/or scale:
```
/// Set as a box.
void SetBox(const Vector3& size, const Vector3& position = Vector3::ZERO, const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a sphere.
void SetSphere(float diameter, const Vector3& position = Vector3::ZERO, const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a static plane.
void SetStaticPlane(const Vector3& position = Vector3::ZERO, const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a cylinder.
void SetCylinder(float diameter, float height, const Vector3& position = Vector3::ZERO, const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a capsule.
void SetCapsule(float diameter, float height, const Vector3& position = Vector3::ZERO, const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a cone.
void SetCone(float diameter, float height, const Vector3& position = Vector3::ZERO, const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a triangle mesh from Model. If you update a model's geometry and want to reapply the shape, call physicsWorld->RemoveCachedGeometry(model) first.
void SetTriangleMesh(Model* model, unsigned lodLevel = 0, const Vector3& scale = Vector3::ONE, const Vector3& position = Vector3::ZERO,
    const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a triangle mesh from CustomGeometry.
void SetCustomTriangleMesh(CustomGeometry* custom, const Vector3& scale = Vector3::ONE, const Vector3& position = Vector3::ZERO,
    const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a convex hull from Model.
void SetConvexHull(Model* model, unsigned lodLevel = 0, const Vector3& scale = Vector3::ONE, const Vector3& position = Vector3::ZERO,
    const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a convex hull from CustomGeometry.
void SetCustomConvexHull(CustomGeometry* custom, const Vector3& scale = Vector3::ONE, const Vector3& position = Vector3::ZERO,
    const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a triangle mesh from Model. If you update a model's geometry and want to reapply the shape, call physicsWorld->RemoveCachedGeometry(model) first.
void SetGImpactMesh(Model* model, unsigned lodLevel = 0, const Vector3& scale = Vector3::ONE, const Vector3& position = Vector3::ZERO,
    const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a triangle mesh from CustomGeometry.
void SetCustomGImpactMesh(CustomGeometry* custom, const Vector3& scale = Vector3::ONE, const Vector3& position = Vector3::ZERO,
    const Quaternion& rotation = Quaternion::IDENTITY);
/// Set as a terrain. Only works if the same scene node contains a Terrain component.
void SetTerrain(unsigned lodLevel = 0);
/// Set shape type.
void SetShapeType(ShapeType type);
/// Set shape size.
void SetSize(const Vector3& size);
/// Set offset position.
void SetPosition(const Vector3& position);
/// Set offset rotation.
void SetRotation(const Quaternion& rotation);
/// Set offset transform.
void SetTransform(const Vector3& position, const Quaternion& rotation);
```

I don't know about exporting these from Blender, but the Urho Editor can be used to create prefabs - or extend them - with collision shapes.

-------------------------

Modanung | 2019-10-15 11:16:35 UTC | #4

I noticed the convex hull doesn't seem to take size into account. Whereas triangle meshes use the size as scale.

----

[quote="QBkGames, post:3, topic:5664"]
To the question of whether you can do it in the editor, if you didn’t find a way to do it, you most likely cannot.
[/quote]

![ColliderEdit|333x195](upload://r14VwNQzA2KYSSPwalM2Tb6b0Ef.png)

-------------------------

