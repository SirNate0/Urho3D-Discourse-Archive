vivienneanthony | 2017-01-02 01:08:35 UTC | #1

Hi,

Is there any way to do or similiar in Angelscript or C++ outside the RegisterObject (bottom part)? The example class is added through a register factory.  The class is made as a template that it is registered into the system by a class that registers it.

Vivienne

I declared access to a component as such
[code]
 RegisterComponent<GameAssetEngineLight>(engine, "GameAssetEngineLight");
    engine->RegisterObjectType("GameAssetEngineLight",0, asOBJ_REF);

    // Passed Urho3D parameters
    engine->RegisterObjectMethod("GameAssetEngineLight", "void SetLightType(LightType SetLight)", asMETHOD(GameAssetEngineLight, SetLightType), asCALL_THISCALL);
    engine->RegisterObjectMethod("GameAssetEngineLight", "void SetBrightness(float SetBright)", asMETHOD(GameAssetEngineLight, SetBrightness), asCALL_THISCALL);
[/code]

Code in StaticModel.CPP

[code]
    URHO3D_ACCESSOR_ATTRIBUTE("Is Enabled", IsEnabled, SetEnabled, bool, true, AM_DEFAULT);
    URHO3D_MIXED_ACCESSOR_ATTRIBUTE("Model", GetModelAttr, SetModelAttr, ResourceRef, ResourceRef(Model::GetTypeStatic()), AM_DEFAULT);
    URHO3D_ACCESSOR_ATTRIBUTE("Material", GetMaterialsAttr, SetMaterialsAttr, ResourceRefList, ResourceRefList(Material::GetTypeStatic()),
        AM_DEFAULT);
    URHO3D_ATTRIBUTE("Is Occluder", bool, occluder_, false, AM_DEFAULT);
    URHO3D_ACCESSOR_ATTRIBUTE("Can Be Occluded", IsOccludee, SetOccludee, bool, true, AM_DEFAULT);
    URHO3D_ATTRIBUTE("Cast Shadows", bool, castShadows_, false, AM_DEFAULT);
    URHO3D_ACCESSOR_ATTRIBUTE("Draw Distance", GetDrawDistance, SetDrawDistance, float, 0.0f, AM_DEFAULT);
    URHO3D_ACCESSOR_ATTRIBUTE("Shadow Distance", GetShadowDistance, SetShadowDistance, float, 0.0f, AM_DEFAULT);
    URHO3D_ACCESSOR_ATTRIBUTE("LOD Bias", GetLodBias, SetLodBias, float, 1.0f, AM_DEFAULT);
    URHO3D_COPY_BASE_ATTRIBUTES(Drawable);
    URHO3D_ATTRIBUTE("Occlusion LOD Level", int, occlusionLodLevel_, M_MAX_UNSIGNED, AM_DEFAULT);[/code]

-------------------------

vivienneanthony | 2017-01-02 01:08:44 UTC | #2

It crashes on this line code (last call stack)

[b]	(((asCSimpleDummy*)obj)->*f)();[/b] // CRASH HERE

Code in Urho3D

[code]void asCScriptEngine::CallObjectMethod(void *obj, asSSystemFunctionInterface *i, asCScriptFunction *s) const
{
#if defined(__GNUC__) || defined(AS_PSVITA)
	if( i->callConv == ICC_GENERIC_METHOD )
	{
		asCGeneric gen(const_cast<asCScriptEngine*>(this), s, obj, 0);
		void (*f)(asIScriptGeneric *) = (void (*)(asIScriptGeneric *))(i->func);
		f(&gen);
	}
	else if( i->callConv == ICC_THISCALL || i->callConv == ICC_VIRTUAL_THISCALL )
	{
		// For virtual thiscalls we must call the method as a true class method
		// so that the compiler will lookup the function address in the vftable
		union
		{
			asSIMPLEMETHOD_t mthd;
			struct
			{
				asFUNCTION_t func;
				asPWORD baseOffset;  // Same size as the pointer
			} f;
		} p;
		p.f.func = (asFUNCTION_t)(i->func);
		p.f.baseOffset = asPWORD(i->baseOffset);
		void (asCSimpleDummy::*f)() = p.mthd;
	[b]	(((asCSimpleDummy*)obj)->*f)();[/b] // CRASH HERE
	}
	else /*if( i->callConv == ICC_CDECL_OBJLAST || i->callConv == ICC_CDECL_OBJFIRST )*/
	{
		void (*f)(void *) = (void (*)(void *))(i->func);
		f(obj);
	}[/code]


Last Call

[code]void RefCounted::ReleaseRef()
{
    assert(refCount_->refs_ > 0);
    (refCount_->refs_)--;
    if (!refCount_->refs_)
        delete this;
}
[/code]

-------------------------

