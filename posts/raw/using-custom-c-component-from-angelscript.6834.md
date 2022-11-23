Pacho | 2021-05-06 12:27:06 UTC | #1

Hello,

so it compiles without errors or AngelScript freaking out. I can even create the component inside the editor. However, when I do:

movement = node.CreateComponent("CharacterMovement");

it says: Can't implicitly convert from 'Component@&' to 'CharacterMovement@'

This is how the component is being registered:



void CharacterMovement::RegisterObject(Context* context)
{
    context->RegisterFactory<CharacterMovement>("Physics");
    URHO3D_ATTRIBUTE("Move Speed", float, moveSpeed_, 0.0f, AM_DEFAULT);
    URHO3D_ATTRIBUTE("Move Dir", Vector3, moveDir_, Vector3::ZERO, AM_DEFAULT);
}

CharacterMovement* CharacterMovement::CharacterMovement_CharacterMovement_Context()
{
    Context* context = GetScriptContext();
    return new CharacterMovement(context);
}

void CharacterMovement::RegisterAPI(asIScriptEngine* engine)
{
    engine->RegisterObjectType("CharacterMovement", 0, asOBJ_REF);
    engine->RegisterObjectBehaviour("CharacterMovement", asBEHAVE_FACTORY, "CharacterMovement@+ f()", AS_FUNCTION(CharacterMovement_CharacterMovement_Context), AS_CALL_CDECL);

    RegisterMembers_LogicComponent<CharacterMovement>(engine, "CharacterMovement");

    engine->RegisterObjectMethod("CharacterMovement", "void CreatePhysicsComponents()", asMETHOD(CharacterMovement, CreatePhysicsComponents), asCALL_THISCALL);
}

-------------------------

Dave82 | 2021-05-06 14:40:04 UTC | #2

I only do a 
[code]
Urho3D::RegisterComponent<CharacterMovement>(scriptEngine , "CharacterMovement");
[/code]
This is an automatic process of registering a component. Afterwards you just need to register the component's methods you want to expose to AS.

-------------------------

Pacho | 2021-05-06 15:14:37 UTC | #3

Are you using an older Urho version? RegisterComponent doesn't seem to exist.

-------------------------

Dave82 | 2021-05-06 15:49:44 UTC | #4

I use 1.7. You should include AngelScript\APITemplates.h

-------------------------

Pacho | 2021-05-06 16:10:01 UTC | #5

Ok in master it's not there anymore. I copied the function, but there are still errors...

-------------------------

Dave82 | 2021-05-06 16:31:13 UTC | #6

Ah i see the new version uses some automated process of registering AS functions and stuff. It seems pretty compilcated compared to the old method which was easy to read and understand.
I understand writing new AS functionality can be tedious and people try to automatize the process as much as possible but at first sight i don't like this new procedure at all.

-------------------------

1vanK | 2021-05-06 21:07:08 UTC | #8

https://raw.githubusercontent.com/urho3d/Urho3D/master/Source/Urho3D/AngelScript/Generated_Members.h

```
// class Component | File: ../Scene/Component.h
template <class T> void RegisterMembers_Component(asIScriptEngine* engine, const char* className)
```
Example of usage: https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/AngelScript/ScriptAPI.cpp#L267-L289

-------------------------

1vanK | 2021-05-06 21:12:56 UTC | #9

[quote="Pacho, post:1, topic:6834"]
it says: Can’t implicitly convert from ‘Component@&’ to ‘CharacterMovement@’
[/quote]

Register subclasses

20 characters

-------------------------

1vanK | 2021-05-06 21:15:02 UTC | #10

[quote="Dave82, post:6, topic:6834, full:true"]
Ah i see the new version uses some automated process of registering AS functions and stuff. It seems pretty compilcated compared to the old method which was easy to read and understand.
I understand writing new AS functionality can be tedious and people try to automatize the process as much as possible but at first sight i don’t like this new procedure at all.
[/quote]

At the moment the bindings are more human readable because each binding is commented

-------------------------

1vanK | 2021-05-06 21:23:50 UTC | #11

[quote="Pacho, post:1, topic:6834"]
CharacterMovement* CharacterMovement::CharacterMovement_CharacterMovement_Context()
{
Context* context = GetScriptContext();
return new CharacterMovement(context);
}

engine->RegisterObjectBehaviour(“CharacterMovement”, asBEHAVE_FACTORY, “CharacterMovement@+ f()”, AS_FUNCTION(CharacterMovement_CharacterMovement_Context), AS_CALL_CDECL);
[/quote]

Are you trying to register a class method as a function?

-------------------------

Dave82 | 2021-05-07 06:15:43 UTC | #12

[quote="1vanK, post:10, topic:6834"]
At the moment the bindings are more human readable because each binding is commented
[/quote]

Those comments doesn't help anything at all and the bindings are all mixed and are all over the place and don't follow any logic.Automatic bindings resulted in 10x more unecessary source files Previously if i want to find a specific binding for let's say ParticleEmitter , just opened the GraphicsAPI.cpp and found it in 3 seconds. Now it is a nightmare to find anything. Especially between function names like : 
[code]
static void DebugLine__DebugLine_constspVector3amp_constspVector3amp_unsigned(DebugLine* _ptr, const Vector3& start, const Vector3& end, unsigned color)
[/code]
I think i'll stick with my older modified 1.7 for now. Even if i update to master it will break all my custom component bindings since all those handy function like RegisterComponent were removed.

-------------------------

Pacho | 2021-05-07 10:45:41 UTC | #13

You're right, but now everything should be by the book. And now Urho3dPlayer just crashes and a minidump is generated. This is the code now:

    engine->RegisterObjectType("CharacterMovement", 0, asOBJ_REF);
    engine->RegisterObjectBehaviour("CharacterMovement", asBEHAVE_FACTORY, "CharacterMovement@+ f()", AS_FUNCTION(CharacterMovement_CharacterMovement_Context), AS_CALL_CDECL);

    RegisterMembers_LogicComponent<CharacterMovement>(engine, "CharacterMovement");

    RegisterSubclass<LogicComponent, CharacterMovement>(engine, "LogicComponent", "CharacterMovement");
    RegisterSubclass<Component, CharacterMovement>(engine, "Component", "CharacterMovement");
    RegisterSubclass<Animatable, CharacterMovement>(engine, "Animatable", "CharacterMovement");
    RegisterSubclass<Serializable, CharacterMovement>(engine, "Serializable", "CharacterMovement");
    RegisterSubclass<Object, CharacterMovement>(engine, "Object", "CharacterMovement");
    RegisterSubclass<RefCounted, CharacterMovement>(engine, "RefCounted", "CharacterMovement");

    engine->RegisterObjectMethod(
        "CharacterMovement", "void CreatePhysicsComponents(PhysicsWorld@+, float, float)",
        AS_METHODPR(CharacterMovement, CreatePhysicsComponents, (PhysicsWorld*, float, float), void), asCALL_THISCALL);


EDIT:

There was an unrelated problem with uninitialized pointers being accessed. It seems to be working now!

-------------------------

1vanK | 2021-05-07 12:36:59 UTC | #14

[quote="Dave82, post:12, topic:6834"]
all over the place and don’t follow any logic
[/quote]

classes are sorted by the depth of inheritance, so that the child classes are defined after the base ones, if the depth of inheritance is the same, then the classes are sorted alphabetically 

[quote="Dave82, post:12, topic:6834"]
Automatic bindings resulted in 10x more unecessary source files
[/quote]

for example?

[quote="Dave82, post:12, topic:6834"]
files Previously if i want to find a specific binding for let’s say ParticleEmitter , just opened the GraphicsAPI.cpp and found it in 3 seconds.
[/quote]

just search "_ParticleEmitter" in bindings. Or do you not use search and will view the file in 3 seconds by hand? 

[quote="Dave82, post:12, topic:6834"]
I think i’ll stick with my older modified 1.7 for now
[/quote]

Dozens mistakes in old bindings.

[quote="Dave82, post:12, topic:6834"]
Even if i update to master it will break all my custom component bindings since all those handy function like RegisterComponent were removed.
[/quote]

Renamed, because they have slightly different functionality now. 

Type registration is taken separately because you must register all types before using them to avoid trying to register a function that uses an unregistered types. 

The default constructors are taken out separately, because you must register them first, otherwise there will be problems if you try to use types in Array \<type\>.

-------------------------

1vanK | 2021-05-07 12:34:53 UTC | #15

[quote="Dave82, post:12, topic:6834"]
Those comments doesn’t help anything at all...
Especially between function names like :

```
static void DebugLine__DebugLine_constspVector3amp_constspVector3amp_unsigned(DebugLine* _ptr, const Vector3& start, const Vector3& end, unsigned color)
```
[/quote]

this is joke? 

```
// DebugLine::DebugLine(const Vector3& start, const Vector3& end, unsigned color)
static void DebugLine__DebugLine_constspVector3amp_constspVector3amp_unsigned(DebugLine* _ptr, const Vector3& start, const Vector3& end, unsigned color)
{
    new(_ptr) DebugLine(start, end, color);
}
```
```
static void Register_DebugLine(asIScriptEngine* engine)
{
    // DebugLine::DebugLine(const Vector3& start, const Vector3& end, unsigned color)
    engine->RegisterObjectBehaviour("DebugLine", asBEHAVE_CONSTRUCT, "void f(const Vector3&in, const Vector3&in, uint)", AS_FUNCTION_OBJFIRST(DebugLine__DebugLine_constspVector3amp_constspVector3amp_unsigned), AS_CALL_CDECL_OBJFIRST);

```

-------------------------

1vanK | 2021-05-07 12:56:04 UTC | #16

In fact, you don't even need to read the automatic bindings. You don't read the generated Lua bindings for example.

-------------------------

Dave82 | 2021-05-07 13:54:23 UTC | #17

Well first of all i don't try to attack anything. I perfectly understand that these changes are for some "greater good". I just think as much problem automatic binding solves, same amount of new problems will arise.

[quote="1vanK, post:16, topic:6834, full:true"]
In fact, you don’t even need to read the automatic bindings. You don’t read the generated Lua bindings for example.
[/quote]

In that case shouldn't be there an official AngelscriptIDE ? Or tutorials how to setup popular IDEs like VisualCode , Code::Blocks , etc for Angelscript ? (autocompletion , type checking , etc)? If there is no easy way to find the binding of a bult in component manually, shouldn't the code editing be automated too ?
E.g so far i needed a Quaternion function and it's parameterlist i just opened the MathAPI.cpp and scrolled the file to RegisterQuaternion function and there were all the Quaternion bindings in one place. Easy to read and easy to find. Now i can't find anything.

[quote="1vanK, post:15, topic:6834"]
```
// DebugLine::DebugLine(const Vector3& start, const Vector3& end, unsigned color)
static void DebugLine__DebugLine_constspVector3amp_constspVector3amp_unsigned(DebugLine* _ptr, const Vector3& start, const Vector3& end, unsigned color)
{
    new(_ptr) DebugLine(start, end, color);
}
```
[/quote]
Again that comment doesn't say much. Reading the original function with the long name reveal the same information about the function as the comment so i don't see how it is helpful ?

[quote="1vanK, post:14, topic:6834"]
for example?
[/quote]

In my older 1.7 there are 22 files in the Angelscript directory.All named exactly what it contains (MathAPI.cpp math bindings. GraphicsAPI.cpp graphics bindings etc) Now there are 60 and the filenames are confusing don't know what's their purpose.

-------------------------

1vanK | 2021-05-07 14:07:08 UTC | #18

you are just annoyed that something has changed and are making up all sorts of things 

[quote="Dave82, post:17, topic:6834"]
If there is no easy way to find the binding of a bult in component manually, shouldn’t the code editing be automated too ?
[/quote]

Docs\AngelScriptAPI.h

[quote="Dave82, post:17, topic:6834"]
E.g so far i needed a Quaternion function and it’s parameterlist i just opened the MathAPI.cpp and scrolled the file to RegisterQuaternion function and there were all the Quaternion bindings in one place. Easy to read and easy to find. Now i can’t find anything.
[/quote]

the list of parameters is the same as in the engine 

 https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Math/Quaternion.h

[quote="Dave82, post:17, topic:6834"]
Again that comment doesn’t say much. Reading the original function with the long name reveal the same information about the function as the comment so i don’t see how it is helpful ?
[/quote]

What other information do you need? Can't you see that this is a constructor? What information is missing compared to the old version? 

[quote="Dave82, post:17, topic:6834"]
In my older 1.7 there are 22 files in the Angelscript directory.All named exactly what it contains (MathAPI.cpp math bindings. GraphicsAPI.cpp graphics bindings etc) Now there are 60 and the filenames are confusing don’t know what’s their purpose.
[/quote]

Ask about a specific file that you do not understand, and I will explain it to you.

-------------------------

1vanK | 2021-05-07 14:13:22 UTC | #19

 https://urho3d.github.io/documentation/HEAD/_script_a_p_i.html

-------------------------

