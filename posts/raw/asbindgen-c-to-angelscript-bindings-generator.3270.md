KonstantTom | 2017-06-19 10:43:54 UTC | #1

Hi!  IMHO, AngelScript bindings writing is so boring and trivial, but I couldn't find tool for **automatic** bindings generation. So I created tool for it myself. :slight_smile:

## GitHub repository
[https://github.com/KonstantinTomashevich/as-bind-gen](https://github.com/KonstantinTomashevich/as-bind-gen)

## Short overview
ASBindGen is lua script (from several files). It reads project configuration from special file ([example file cmake template](https://github.com/KonstantinTomashevich/as-bin-gen-sample-project/blob/master/ASBindGenConfiguration.lua.cmake)), then parses specified headers, then writes bindings for them. It **doesn't** generates AST, parsing is ruled by special command-comments.

Example header:
```c++
#pragma once
#include <Urho3D/Core/Object.h>
#include <SampleProject/SampleObject.hpp>

//@ASBindGen Class ObjectType=Ref
class SampleContainer : public Urho3D::Object
{
URHO3D_OBJECT (SampleContainer, Object)
protected:
    Urho3D::Vector <Urho3D::SharedPtr <SampleObject> > objects_;

public:
    //@ASBindGen Constructor UseUrho3DScriptContext_arg0
    SampleContainer (Urho3D::Context *context);
    virtual ~SampleContainer ();

    //@ASBindGen Function ReturnHandleArray
        Urho3D::Vector <Urho3D::SharedPtr <SampleObject> > GetObjects () const;
        //@ASBindGen Function OverrideName=get_objectsCount
        unsigned GetObjectsCount () const;
        //@ASBindGen Function AddRef_arg0
        void AddObject (SampleObject *object);
        //@ASBindGen Function AddRef_arg-1
        SampleObject *GetObjectByIndex (unsigned index) const;
        //@ASBindGen Function AddRef_arg0
        bool RemoveObject (SampleObject *object);
};
```

Bindings code, generated from this header:
```c++
#pragma once
#include <Urho3D/AngelScript/Script.h>
#include <Urho3D/ThirdParty/AngelScript/angelscript.h>
#include <Urho3D/AngelScript/APITemplates.h>
#include <SampleProject/SampleContainer.hpp>

namespace Bindings
{
SampleContainer * wrapper_SampleContainer_constructor ()
{
    return new SampleContainer (Urho3D::GetScriptContext ());
}

Urho3D::CScriptArray * wrapper_SampleContainer_GetObjects (SampleContainer* objectPtr)
{
    Urho3D::Vector <Urho3D::SharedPtr <SampleObject> > result = objectPtr->GetObjects ();
    return Urho3D::VectorToHandleArray <SampleObject> (result, "Array <SampleObject @>");
}

template <class T> void RegisterSampleContainer (asIScriptEngine *engine, const char *className, bool registerConstructors)
{
    Urho3D::RegisterObject <T> (engine, className);

    if (registerConstructors)
        {

            engine->RegisterObjectBehaviour (className, asBEHAVE_FACTORY, (Urho3D::String (className) + "@+ f ()").CString (), asFUNCTION (wrapper_SampleContainer_constructor), asCALL_CDECL);
        }

        engine->RegisterObjectMethod (className, "Array <SampleObject @> @ GetObjects () const", asFUNCTION (wrapper_SampleContainer_GetObjects), asCALL_CDECL_OBJFIRST);
        engine->RegisterObjectMethod (className, "uint get_objectsCount () const", asMETHOD (T, GetObjectsCount), asCALL_THISCALL);
        engine->RegisterObjectMethod (className, "void AddObject (SampleObject @+ object) ", asMETHOD (T, AddObject), asCALL_THISCALL);
        engine->RegisterObjectMethod (className, "SampleObject @+ GetObjectByIndex (uint index) const", asMETHOD (T, GetObjectByIndex), asCALL_THISCALL);
        engine->RegisterObjectMethod (className, "bool RemoveObject (SampleObject @+ object) ", asMETHOD (T, RemoveObject), asCALL_THISCALL);
}

}
```

Also it generates bindings hub like this:
```c++
#include <Urho3D/ThirdParty/AngelScript/angelscript.h>
#include <Urho3D/AngelScript/APITemplates.h>
#include "Bindings.hpp"
#include <SampleProject/AngelScriptBindings/SampleContainer.hpp>
#include <SampleProject/AngelScriptBindings/SampleObject.hpp>

namespace Bindings
{
void RegisterAnything (asIScriptEngine *engine)
{
    RegisterClassesForwardDeclarations (engine);
    RegisterEnums (engine);
    RegisterConstants (engine);
    RegisterFreeFunctions (engine);
    RegisterUrho3DSubsystems (engine);
    RegisterClasses (engine);
}

void RegisterClassesForwardDeclarations (asIScriptEngine *engine)
{
    engine->RegisterObjectType ("SampleContainer", 0, asOBJ_REF);
    engine->RegisterObjectType ("SampleObject", 0, asOBJ_REF);
}

void RegisterEnums (asIScriptEngine *engine)
{
}

void RegisterConstants (asIScriptEngine *engine)
{
}

void RegisterFreeFunctions (asIScriptEngine *engine)
{
}

void RegisterUrho3DSubsystems (asIScriptEngine *engine)
{
}

void RegisterClasses (asIScriptEngine *engine)
{
    RegisterSampleContainer <SampleContainer> (engine, "SampleContainer", true);
    RegisterSampleObject <SampleObject> (engine, "SampleObject", true);
}

}
```

## Example CMake project
[https://github.com/KonstantinTomashevich/as-bin-gen-sample-project](https://github.com/KonstantinTomashevich/as-bin-gen-sample-project)

Also it perfectly works in my game:
[https://github.com/KonstantinTomashevich/colonization](https://github.com/KonstantinTomashevich/colonization)

-------------------------

coldev | 2017-06-24 22:06:40 UTC | #2

thanks for share nice asset

-------------------------

