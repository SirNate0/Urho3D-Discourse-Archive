josuemnb | 2019-08-23 10:16:38 UTC | #1

Hi.
Would be possible to add to Node or Component the property "void* UserData" in C++ and/or "object UserData" in C#.
It's a common property found in other libraries.

-------------------------

Miegamicis | 2019-08-23 10:37:06 UTC | #2

You mean this https://github.com/urho3d/Urho3D/blob/a476f0c40114b92c2637145c24f50ccef6de5d3c/Source/Urho3D/Scene/Node.h#L323 ?

-------------------------

josuemnb | 2019-08-23 10:49:46 UTC | #3

thanks for replying.
I've noticed that on c++, but wasn't sure because i'm using urho on c#, which doesn't contains that paramter for setvar.

only the following:

SetVar(StringHash key, IntRect value);
SetVar(StringHash key, bool value);
SetVar(StringHash key, string value);
SetVar(StringHash key, Vector3 value);
SetVar(StringHash key, float value);
SetVar(StringHash key, Vector2 value);
SetVar(StringHash key, Matrix3x4 value);
SetVar(StringHash key, Matrix4 value);
SetVar(StringHash key, Quaternion value);
SetVar(StringHash key, IntVector2 value);
SetVar(StringHash key, Vector4 value);
SetVar(StringHash key, Color value);
SetVar(StringHash key, int value);

-------------------------

Miegamicis | 2019-08-23 10:54:01 UTC | #4

Sorry, don't know anything about the C# implementation

-------------------------

Modanung | 2019-08-23 11:12:56 UTC | #5

@josuemnb Urho3D does not use C#. Are you talking about a discontinued fork?
Maybe you could try with C++ and AngelScript instead? These are not the UrhoSharp forums.

-------------------------

josuemnb | 2019-08-23 11:15:49 UTC | #6

Thanks.
Wasn't sure of that.

-------------------------

