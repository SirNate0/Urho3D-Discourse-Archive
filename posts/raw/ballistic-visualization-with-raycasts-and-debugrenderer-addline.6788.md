lebrewer | 2021-04-06 22:56:15 UTC | #1

I'm writing a small piece of code to help me start with a ballistics simulator inside Urho. So far, here's my code: 

    void HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {
        using namespace KeyDown;
        int key = eventData[P_KEY].GetInt();

        if (key == KEY_SPACE) {
            int feetTick = 5;
            PhysicsRaycastResult raycastResult;
            Vector3 muzzle = barrelNode->GetWorldPosition() + Vector3(2, 0, 0);
            Ray departureLine(muzzle, Vector3::FORWARD);
            scene_->GetComponent<PhysicsWorld>()->RaycastSingle(raycastResult, departureLine, feetTick, 2);
            rays.Push(std::make_tuple(departureLine, departureLine.origin_ + Vector3(feetTick, 0, 0)));

            int dropAngle = 20;
            Vector3 nextFeet(feetTick, 0, 0);
            URHO3D_LOGINFO("Drop angle: " + String(dropAngle));
            while (dropAngle > 0) {
                Ray ray(muzzle + nextFeet, Vector3::UP);
                scene_->GetComponent<PhysicsWorld>()->RaycastSingle(raycastResult, ray, feetTick, 2);
                rays.Push(std::make_tuple(ray, ray.origin_ + nextFeet));

                nextFeet.x_ += feetTick;
                dropAngle -= 10;
            }
        }
    }

Rays is basically this:

    PODVector<std::tuple<Ray, Vector3>> rays;

Which I use to render the lines like this:

    void HandlePostRenderUpdate(StringHash eventType, VariantMap & eventData)
    {
        auto* debug = scene_->GetComponent<DebugRenderer>();
        debug->SetLineAntiAlias(true);

        for (unsigned i = 0; i < rays.Size(); ++i) {
            Color color = i % 2 ? Color::YELLOW : Color::MAGENTA;
            debug->AddLine(std::get<0>(rays[i]).origin_, std::get<1>(rays[i]), color, false);
        }
    }

Unfortunately, since the rays never hit anything, I'm not able to get the position the ray "ended", so I can't AddLine to the proper angled origin (note that I'm angling the ray a little bit each time). Any ideas how I can get the "end" of a raycast without hits?

-------------------------

Modanung | 2021-04-06 23:13:25 UTC | #2

Add all the bits?
```
Vector3 tip{ muzzle };

for (every step)
    tip += step;
```

Also, since `Ray`s have both an origin and direction, all you'd need in your `tuple` is a `float` for distance/length, instead of a `Vector3`.

-------------------------

lebrewer | 2021-04-07 17:35:16 UTC | #3

With an origin and direction, I can't know the end point of the raycast, therefore I'm missing the second argument to AddLine.

-------------------------

Modanung | 2021-04-07 18:48:38 UTC | #4

That would then be `rayStart + rayDirection * distance`. :slight_smile:

-------------------------

