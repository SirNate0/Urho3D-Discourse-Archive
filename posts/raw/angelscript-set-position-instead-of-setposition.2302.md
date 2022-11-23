TheComet | 2017-01-02 01:14:35 UTC | #1

I noticed that a lot of Node methods use lowercase+underscore instead of camel case. See [b]AngelScript/APITemplates.h:732[/b] for example.

[code]    // -- SNIP --

    engine->RegisterObjectMethod(className, "Vector2 LocalToWorld2D(const Vector2&in) const", asMETHODPR(T, LocalToWorld2D, (const Vector2&) const, Vector2), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "Vector3 WorldToLocal(const Vector3&in) const", asMETHODPR(T, WorldToLocal, (const Vector3&) const, Vector3), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "Vector3 WorldToLocal(const Vector4&in) const", asMETHODPR(T, WorldToLocal, (const Vector4&) const, Vector3), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "Vector2 WorldToLocal2D(const Vector2&in) const", asMETHODPR(T, WorldToLocal2D, (const Vector2&) const, Vector2), asCALL_THISCALL);

    // After this point, we just decide to switch to lowercase + underscore?

    engine->RegisterObjectMethod(className, "void set_position(const Vector3&in)", asMETHODPR(T, SetPosition, (const Vector3&), void), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "const Vector3& get_position() const", asMETHOD(T, GetPosition), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "void set_position2D(const Vector2&in)", asMETHODPR(T, SetPosition2D, (const Vector2&), void), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "Vector2 get_position2D() const", asMETHOD(T, GetPosition2D), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "void set_rotation(const Quaternion&in)", asMETHODPR(T, SetRotation, (const Quaternion&), void), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "const Quaternion& get_rotation() const", asMETHOD(T, GetRotation), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "void set_rotation2D(float)", asMETHODPR(T, SetRotation2D, (float), void), asCALL_THISCALL);

    // -- SNIP --[/code]

It took me a while to figure out how to position a scene node because of this. Is this intentional, or can it be changed?

-------------------------

cadaver | 2017-01-02 01:14:35 UTC | #2

This was an intentional decision long ago to favor properties instead of setters / getters for brevity of code. It's explained on the scripting documentation page, and you'd see it also in the scripting API reference.

Note that the Lua bindings intentionally expose both setters / getters, and properties. This could be done on the AngelScript side too, with the potential downside of scripting subsystem initialization taking a longer time, and consuming more memory / making the exe bigger.

-------------------------

TheComet | 2017-01-02 01:14:36 UTC | #3

Ah, didn't see that. Thanks!

-------------------------

