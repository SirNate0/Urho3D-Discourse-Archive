dragonCASTjosh | 2017-01-02 01:14:16 UTC | #1

I am currently adding the visualization for the Area lights but i am unable to find anything that would fit the tube and unsure how to approach creating a tube shaped debug feature. Am i missing something and if not can someone help out with creating one.

-------------------------

1vanK | 2017-01-02 01:14:16 UTC | #2

CollisionShape can draw debug capsule with any transforms, may be take code from thence

-------------------------

dragonCASTjosh | 2017-01-02 01:14:16 UTC | #3

[quote="1vanK"]CollisionShape can draw debug capsule with any transforms, may be take code from thence[/quote]
it looks to draw its debug shape from bullet physics and im not sure if that is best practice to use bullet in the renderer

-------------------------

cadaver | 2017-01-02 01:14:17 UTC | #4

Yes, calling Bullet's debug draw functions would require an actual collisionshape, which I don't recommend. I recommend making your own scaled sphere debug draw and adding it to DebugRenderer.

-------------------------

dragonCASTjosh | 2017-01-02 01:14:17 UTC | #5

[quote="cadaver"]Yes, calling Bullet's debug draw functions would require an actual collisionshape, which I don't recommend. I recommend making your own scaled sphere debug draw and adding it to DebugRenderer.[/quote]
id likely need help on the math for getting a capsule in the debug renderer

-------------------------

1vanK | 2017-01-02 01:14:17 UTC | #6

[code]    void DrawCylinder(const Vector3& position, float radius, float height, const Quaternion& rotation, const Color& color, bool depthTest)
    {
        DebugRenderer* debug = scene_->GetOrCreateComponent<DebugRenderer>();

        Sphere sphere(Vector3::ZERO, radius);
        Vector3 heightVec = rotation * Vector3(0, height, 0);
        Vector3 offsetXVec = rotation * Vector3(radius, 0, 0);
        Vector3 offsetZVec = rotation * Vector3(0, 0, radius);
        for (unsigned i = 0; i < 360; i += 45)
        {
            Vector3 p1 = rotation * PointOnSphere(sphere, i, 90) + position;
            Vector3 p2 = rotation * PointOnSphere(sphere, i + 45, 90) + position;
            debug->AddLine(p1, p2, color, depthTest);
            debug->AddLine(p1 + heightVec, p2 + heightVec, color, depthTest);
        }
        debug->AddLine(position + offsetXVec, position + heightVec + offsetXVec, color, depthTest);
        debug->AddLine(position - offsetXVec, position + heightVec - offsetXVec, color, depthTest);
        debug->AddLine(position + offsetZVec, position + heightVec + offsetZVec, color, depthTest);
        debug->AddLine(position - offsetZVec, position + heightVec - offsetZVec, color, depthTest);
    }[/code]

This code based on void DebugRenderer::AddCylinder() with minimal changes

-------------------------

1vanK | 2017-01-02 01:14:17 UTC | #7

Draw cylinder from center:
[code]
    void DrawCylinder(const Vector3& position, float radius, float halfHeight, const Quaternion& rotation, const Color& color, bool depthTest)
    {
        DebugRenderer* debug = scene_->GetOrCreateComponent<DebugRenderer>();

        Sphere sphere(Vector3::ZERO, radius);
        Vector3 halfHeightVec = rotation * Vector3(0, halfHeight, 0);
        Vector3 offsetXVec = rotation * Vector3(radius, 0, 0);
        Vector3 offsetZVec = rotation * Vector3(0, 0, radius);
        for (unsigned i = 0; i < 360; i += 45)
        {
            Vector3 p1 = rotation * PointOnSphere(sphere, i, 90) + position;
            Vector3 p2 = rotation * PointOnSphere(sphere, i + 45, 90) + position;
            debug->AddLine(p1 - halfHeightVec, p2 - halfHeightVec, color, depthTest);
            debug->AddLine(p1 + halfHeightVec, p2 + halfHeightVec, color, depthTest);
        }
        debug->AddLine(position - halfHeightVec + offsetXVec, position + halfHeightVec + offsetXVec, color, depthTest);
        debug->AddLine(position - halfHeightVec - offsetXVec, position + halfHeightVec - offsetXVec, color, depthTest);
        debug->AddLine(position - halfHeightVec + offsetZVec, position + halfHeightVec + offsetZVec, color, depthTest);
        debug->AddLine(position - halfHeightVec - offsetZVec, position + halfHeightVec - offsetZVec, color, depthTest);
    }[/code]

-------------------------

dragonCASTjosh | 2017-01-02 01:14:17 UTC | #8

[quote="1vanK"]Draw cylinder from center:
[code]
    void DrawCylinder(const Vector3& position, float radius, float halfHeight, const Quaternion& rotation, const Color& color, bool depthTest)
    {
        DebugRenderer* debug = scene_->GetOrCreateComponent<DebugRenderer>();

        Sphere sphere(Vector3::ZERO, radius);
        Vector3 halfHeightVec = rotation * Vector3(0, halfHeight, 0);
        Vector3 offsetXVec = rotation * Vector3(radius, 0, 0);
        Vector3 offsetZVec = rotation * Vector3(0, 0, radius);
        for (unsigned i = 0; i < 360; i += 45)
        {
            Vector3 p1 = rotation * PointOnSphere(sphere, i, 90) + position;
            Vector3 p2 = rotation * PointOnSphere(sphere, i + 45, 90) + position;
            debug->AddLine(p1 - halfHeightVec, p2 - halfHeightVec, color, depthTest);
            debug->AddLine(p1 + halfHeightVec, p2 + halfHeightVec, color, depthTest);
        }
        debug->AddLine(position - halfHeightVec + offsetXVec, position + halfHeightVec + offsetXVec, color, depthTest);
        debug->AddLine(position - halfHeightVec - offsetXVec, position + halfHeightVec - offsetXVec, color, depthTest);
        debug->AddLine(position - halfHeightVec + offsetZVec, position + halfHeightVec + offsetZVec, color, depthTest);
        debug->AddLine(position - halfHeightVec - offsetZVec, position + halfHeightVec - offsetZVec, color, depthTest);
    }[/code][/quote]

The results from that are close.

Here is the shape needed:
[img]http://i.imgur.com/4BnJj6f.jpg[/img]

Here is the shape we have
[img]http://i.imgur.com/7RhEW15.jpg[/img]

An alternative i noticed in Frostbites papers is they have debug system in the shader to turn the lights into meshes, not sure how to approach that or if we want to take that path.

-------------------------

1vanK | 2017-01-02 01:14:18 UTC | #9

Hm, void DebugRenderer::AddSphere has error?

[code]void DebugRenderer::AddSphere(const Sphere& sphere, const Color& color, bool depthTest)
{
    unsigned uintColor = color.ToUInt();

    for (unsigned j = 0; j < 180; j += 45)
    {
        for (unsigned i = 0; i < 360; i += 45)
        {
            Vector3 p1 = PointOnSphere(sphere, i, j);
            Vector3 p2 = PointOnSphere(sphere, i + 45, j);
            Vector3 p3 = PointOnSphere(sphere, i, j + 45);
            Vector3 p4 = PointOnSphere(sphere, i + 45, j + 45);

            AddLine(p1, p2, uintColor, depthTest);
            //AddLine(p3, p4, uintColor, depthTest);
            AddLine(p1, p3, uintColor, depthTest);
            //AddLine(p2, p4, uintColor, depthTest);
        }
    }
}
[/code]

comment two lines not affect to result

-------------------------

1vanK | 2017-01-02 01:14:18 UTC | #10

[code]    void DrawCapsule(const Vector3& position, float radius, float halfLength, const Quaternion& rotation, const Color& color, bool depthTest)
    {
        DebugRenderer* debug = scene_->GetOrCreateComponent<DebugRenderer>();

        Sphere sphere(Vector3::ZERO, radius);
        Vector3 halfLengthVec = rotation * Vector3(halfLength, 0, 0);

        unsigned uintColor = color.ToUInt();

        for (unsigned j = 0; j < 180; j += 45)
        {
            for (unsigned i = 0; i < 180; i += 45)
            {
                Vector3 p1 = rotation * PointOnSphere(sphere, i, j) + halfLengthVec + position;
                Vector3 p2 = rotation * PointOnSphere(sphere, i + 45, j) + halfLengthVec + position;
                Vector3 p3 = rotation * PointOnSphere(sphere, i, j + 45) + halfLengthVec + position;
                Vector3 p4 = rotation * PointOnSphere(sphere, i + 45, j + 45) + halfLengthVec + position;

                debug->AddLine(p1, p2, uintColor, depthTest);
                //debug->AddLine(p3, p4, uintColor, depthTest);
                debug->AddLine(p1, p3, uintColor, depthTest);
                debug->AddLine(p2, p4, uintColor, depthTest);
            }

            for (unsigned i = 180; i < 360; i += 45)
            {
                Vector3 p1 = rotation * PointOnSphere(sphere, i, j) - halfLengthVec + position;
                Vector3 p2 = rotation * PointOnSphere(sphere, i + 45, j) - halfLengthVec + position;
                Vector3 p3 = rotation * PointOnSphere(sphere, i, j + 45) - halfLengthVec + position;
                Vector3 p4 = rotation * PointOnSphere(sphere, i + 45, j + 45) - halfLengthVec + position;

                debug->AddLine(p1, p2, uintColor, depthTest);
                //debug->AddLine(p3, p4, uintColor, depthTest);
                debug->AddLine(p1, p3, uintColor, depthTest);
                debug->AddLine(p2, p4, uintColor, depthTest);
            }

            Vector3 p1 = rotation * PointOnSphere(sphere, 0, j) + halfLengthVec + position;
            Vector3 p2 = rotation * PointOnSphere(sphere, 0, j) - halfLengthVec + position;
            debug->AddLine(p1, p2, uintColor, depthTest);
            Vector3 p3 = rotation * PointOnSphere(sphere, 0, j + 180) + halfLengthVec + position;
            Vector3 p4 = rotation * PointOnSphere(sphere, 0, j + 180) - halfLengthVec + position;
            debug->AddLine(p3, p4, uintColor, depthTest);
        }
    }



    void HandlePostUpdate(StringHash eventType, VariantMap& eventData)
    {
        //DrawCylinder(Vector3(0.0f, 5.0f, 0.0f), 5.0f, 10.0f, Quaternion(45.0f, 45.0f, 45.0f), Color::RED, true);
        DrawCapsule(Vector3(0, 10, 0), 5.f, 10.f, Quaternion(45.0f, 45.0f, 45.0f), Color::RED, false);
    }
[/code]

[url=http://savepic.ru/11422230.htm][img]http://savepic.ru/11422230m.png[/img][/url]

-------------------------

Lumak | 2017-01-02 01:14:18 UTC | #11

Why not a cylinder model - [url]https://github.com/urho3d/Urho3D/blob/master/bin/Data/Models/Cylinder.mdl[/url]

-------------------------

1vanK | 2017-01-02 01:14:18 UTC | #12

[quote="Lumak"]Why not a cylinder model - [url]https://github.com/urho3d/Urho3D/blob/master/bin/Data/Models/Cylinder.mdl[/url][/quote]

I already write DrawCylinder function...

-------------------------

Lumak | 2017-01-02 01:14:18 UTC | #13

A flat pill model? [url]https://github.com/Lumak/Urho3D-Assets/tree/master/Urho3DPill[/url]

-------------------------

dragonCASTjosh | 2017-01-02 01:14:18 UTC | #14

[quote="Lumak"]A flat pill model? [url]https://github.com/Lumak/Urho3D-Assets/tree/master/Urho3DPill[/url][/quote]

Im planning to intergrate this into the editor for the debug of area lights.

[quote="1vanK"]I already write DrawCylinder function...[/quote]

The capsule solution you created dosent seam to work as intended and i am not sure why, the size and length just changes the size of the sphere.

-------------------------

1vanK | 2017-01-02 01:14:19 UTC | #15

Do not see any problems in my tests

[code]    void HandlePostUpdate(StringHash eventType, VariantMap& eventData)
    {
        DrawCapsule(Vector3(-10, 10, 0), 1.f, 1.f, Quaternion(45.0f, 45.0f, 45.0f), Color::RED, false);
        DrawCapsule(Vector3(0, 10, 0), 1.f, 2.f, Quaternion(45.0f, 45.0f, 45.0f), Color::RED, false);
        DrawCapsule(Vector3(10, 10, 0), 3.f, 2.f, Quaternion(45.0f, 45.0f, 45.0f), Color::RED, false);
    }[/code]

[url=http://savepic.ru/11501983.htm][img]http://savepic.ru/11501983m.png[/img][/url]

-------------------------

dragonCASTjosh | 2017-01-02 01:14:19 UTC | #16

[quote="1vanK"]Do not see any problems in my tests

[code]    void HandlePostUpdate(StringHash eventType, VariantMap& eventData)
    {
        DrawCapsule(Vector3(-10, 10, 0), 1.f, 1.f, Quaternion(45.0f, 45.0f, 45.0f), Color::RED, false);
        DrawCapsule(Vector3(0, 10, 0), 1.f, 2.f, Quaternion(45.0f, 45.0f, 45.0f), Color::RED, false);
        DrawCapsule(Vector3(10, 10, 0), 3.f, 2.f, Quaternion(45.0f, 45.0f, 45.0f), Color::RED, false);
    }[/code]

[url=http://savepic.ru/11501983.htm][img]http://savepic.ru/11501983m.png[/img][/url][/quote]

I renamed the function to better fit the standards in Urho but results are not as you have shown and im not sure why.

[code]
void DebugRenderer::AddCapsule(const Vector3& position, float radius, float halfLength, const Quaternion& rotation, const Color& color, bool depthTest)
{
 
    Sphere sphere(Vector3::ZERO, radius);
    Vector3 halfLengthVec = rotation * Vector3(halfLength, 0, 0);

    unsigned uintColor = color.ToUInt();

    for (unsigned j = 0; j < 180; j += 45)
    {
        for (unsigned i = 0; i < 180; i += 45)
        {
            Vector3 p1 = rotation * PointOnSphere(sphere, i, j) + halfLengthVec + position;
            Vector3 p2 = rotation * PointOnSphere(sphere, i + 45, j) + halfLengthVec + position;
            Vector3 p3 = rotation * PointOnSphere(sphere, i, j + 45) + halfLengthVec + position;
            Vector3 p4 = rotation * PointOnSphere(sphere, i + 45, j + 45) + halfLengthVec + position;

            AddLine(p1, p2, uintColor, depthTest);
            //debug->AddLine(p3, p4, uintColor, depthTest);
            AddLine(p1, p3, uintColor, depthTest);
            AddLine(p2, p4, uintColor, depthTest);
        }

        for (unsigned i = 180; i < 360; i += 45)
        {
            Vector3 p1 = rotation * PointOnSphere(sphere, i, j) - halfLengthVec + position;
            Vector3 p2 = rotation * PointOnSphere(sphere, i + 45, j) - halfLengthVec + position;
            Vector3 p3 = rotation * PointOnSphere(sphere, i, j + 45) - halfLengthVec + position;
            Vector3 p4 = rotation * PointOnSphere(sphere, i + 45, j + 45) - halfLengthVec + position;

            AddLine(p1, p2, uintColor, depthTest);
            //debug->AddLine(p3, p4, uintColor, depthTest);
            AddLine(p1, p3, uintColor, depthTest);
            AddLine(p2, p4, uintColor, depthTest);
        }

        Vector3 p1 = rotation * PointOnSphere(sphere, 0, j) + halfLengthVec + position;
        Vector3 p2 = rotation * PointOnSphere(sphere, 0, j) - halfLengthVec + position;
        AddLine(p1, p2, uintColor, depthTest);
        Vector3 p3 = rotation * PointOnSphere(sphere, 0, j + 180) + halfLengthVec + position;
        Vector3 p4 = rotation * PointOnSphere(sphere, 0, j + 180) - halfLengthVec + position;
        AddLine(p3, p4, uintColor, depthTest);
    }
}
[/code]

[code]
        case LIGHT_TUBE:
            debug->AddSphere(Sphere(node_->GetWorldPosition(), range_), color, depthTest);
            debug->AddCapsule(node_->GetWorldPosition(), lightSize_, lightLength_, node_->GetWorldRotation() + Quaternion(90,0,0),color, depthTest);
[/code]

-------------------------

1vanK | 2017-01-02 01:14:19 UTC | #17

[quote]node_->GetWorldRotation() + Quaternion(90,0,0)[/quote]

I'm not sure, that it correct

-------------------------

1vanK | 2017-01-02 01:14:19 UTC | #18

try (Quaternion1 * delta).Normalized()

-------------------------

dragonCASTjosh | 2017-01-02 01:14:19 UTC | #19

[quote="1vanK"]try (Quaternion1 * delta).Normalized()[/quote]

There is no delta im drawing it from DrawDebugGeometry starting on line 247 of Light.cpp

-------------------------

1vanK | 2017-01-02 01:14:19 UTC | #20

I mean, u can not just add one quternion to other

-------------------------

dragonCASTjosh | 2017-01-02 01:14:19 UTC | #21

[quote="1vanK"]I mean, u can not just add one quternion to other[/quote]
fair enough :slight_smile: its been way to long since using quternions

-------------------------

