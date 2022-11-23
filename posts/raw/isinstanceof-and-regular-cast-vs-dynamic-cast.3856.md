SirNate0 | 2017-12-17 08:18:11 UTC | #1

Which is better to use, especially performance-wise?

-------------------------

Eugene | 2017-12-17 08:25:41 UTC | #2

InstanceOf should be faster, but I don’t think anybody ever tested it.

-------------------------

SirNate0 | 2017-12-18 04:54:13 UTC | #3

I decided to go ahead and try it. IsInstanceOf was indeed faster, at least in this test (which did only involve one level of inheritance for a correct match, and very possibly has other flaws...). It was only a minor difference (a few percent), but I suppose its worth knowing. (IsInstanceOf: 10486; dynamic_cast: 11040)

```cpp
#pragma once

#include <Urho3D/Container/Ptr.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/Container/Vector.h>
#include <Urho3D/Math/Random.h>
#include <Urho3D/Core/Profiler.h>

#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Physics/RigidBody.h>
#include <Urho3D/Physics/CollisionShape.h>
#include <Urho3D/Graphics/Texture.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/Graphics/Texture3D.h>
#include <Urho3D/Graphics/TextureCube.h>

using namespace Urho3D;

void TestCasting(Context* context)
{
    PODVector<StringHash> types = {Model::GetTypeStatic(),
                RigidBody::GetTypeStatic(),
                Texture2D::GetTypeStatic(),
                Texture3D::GetTypeStatic(),
                TextureCube::GetTypeStatic(),
                CollisionShape::GetTypeStatic()};
    WeakPtr<Texture> tex;
    Timer timer;
    constexpr unsigned COUNT = 10000000;
    for (unsigned i = 0; i < COUNT; ++i)
    {
        int r = Rand() % types.Size();
        StringHash type = types[r];
        SharedPtr<Object> obj = context->CreateObject(type);
        if (!obj)
        {
            LOGWARNING(String("Couldn't create type ") + String(r));
            continue;
        }
        if (obj->IsInstanceOf(Texture::GetTypeStatic()))
            tex = (Texture*)obj.Get();
        else
            tex = nullptr;
    }
    auto t = String(timer.GetMSec(true));
    for (unsigned i = 0; i < COUNT; ++i)
    {
        int r = Rand() % types.Size();
        StringHash type = types[r];
        SharedPtr<Object> obj = context->CreateObject(type);
        if (!obj)
        {
            LOGWARNING(String("Couldn't create type ") + String(r));
            continue;
        }
        tex = dynamic_cast<Texture*>(obj.Get());
    }
    LOGINFO(String(t) + " <- IsInstanceOf | dynamic_cast -> " + String(timer.GetMSec(true)));
}
```

-------------------------

