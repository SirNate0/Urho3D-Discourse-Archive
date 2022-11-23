amit.nath30 | 2017-01-30 20:21:10 UTC | #1

What is the best way to create a matrix3x4?

I am doing 

Urho3D::Matrix3x4 xTranform  = Urho3D::Matrix3x4::IDENTITY;
Urho3D::Matrix3x4 yTranform  = Urho3D::Matrix3x4::IDENTITY;
Urho3D::Matrix3x4 zTranform  = Urho3D::Matrix3x4::IDENTITY;
Urho3D::Matrix3x4 objToWorld = Urho3D::Matrix3x4::IDENTITY;

xTranform.Decompose(Urho3D::Vector3::ZERO, rotation * Urho3D::Quaternion(-90, Urho3D::Vector3::UP), Urho3D::Vector3::ONE);
 yTranform.Decompose(Urho3D::Vector3::ZERO, rotation * Urho3D::Quaternion(-90, Urho3D::Vector3::RIGHT), Urho3D::Vector3::ONE);
zTranform.Decompose(Urho3D::Vector3::ZERO, rotation, Urho3D::Vector3::ONE);
objToWorld.Decompose(position, Urho3D::Quaternion::IDENTITY, scale);

but getting error

F:\URHO-3D\Urho3d-IDE\TransformHandle\runtimehandles.cpp:780: error: binding 'const Urho3D::Vector3' to reference of type 'Urho3D::Vector3&' discards qualifiers

-------------------------

1vanK | 2017-01-30 20:28:40 UTC | #2

Decompose is "inverse" operation of creating :)

Use constructor instead 
```
    /// Construct from translation, rotation and uniform scale.
    Matrix3x4(const Vector3& translation, const Quaternion& rotation, float scale)
```

-------------------------

