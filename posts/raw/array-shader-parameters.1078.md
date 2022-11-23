friesencr | 2017-01-02 01:05:16 UTC | #1

It looks like there is no api to pass an array to material shader parameters.

-------------------------

friesencr | 2017-01-02 01:05:16 UTC | #2

i am playing with a hacky aproach right now:

[code]
void Graphics::SetShaderParameter(StringHash param, const VariantVector& variantVector)
{
	if (variantVector.Size() == 0)
		return;

	// base logic on the first parameter
	Variant first = variantVector.Front();

	// only float types allowed
	switch (first.GetType())
	{
		case VAR_FLOAT:
		case VAR_VECTOR2:
		case VAR_VECTOR3:
		case VAR_VECTOR4:
		case VAR_MATRIX3:
		case VAR_MATRIX4:
			break;
		default:
			return;
	}

	PODVector<unsigned char> data;

	// validate that all parameters are the same as the first
	for (unsigned i = 0; i < variantVector.Size(); ++i)
	{
		if (variantVector[i].GetType() != first.GetType())
			return;

		data += variantVector[i].GetBuffer();
	}

	SetShaderParameter(param, (float*)&data, variantVector.Size());

}
[/code]

-------------------------

friesencr | 2017-01-02 01:05:16 UTC | #3

I thought get buffer meant shut up and give me my data but it does type checking.

Now with more phat.

[code]
void Graphics::SetShaderParameter(StringHash param, const VariantVector& variantVector)
{
	if (variantVector.Size() == 0)
		return;

	// base logic on the first parameter
	Variant first = variantVector.Front();
	VariantType type = first.GetType();
	int size;

	// only float types allowed
	switch (type)
	{
		case VAR_FLOAT:
			size = sizeof(float);
			break;
		case VAR_VECTOR2:
			size = sizeof(Vector2);
			break;
		case VAR_VECTOR3:
			size = sizeof(Vector3);
			break;
		case VAR_VECTOR4:
			size = sizeof(Vector4);
			break;
		case VAR_MATRIX3:
			size = sizeof(Matrix3);
			break;
		case VAR_MATRIX4:
			size = sizeof(Matrix4);
			break;
		default:
			return;
	}


	// validate that all parameters are the same as the first
	for (unsigned i = 1; i < variantVector.Size(); ++i)
	{
		if (variantVector[i].GetType() != type)
			return;
	}

	PODVector<unsigned char> data;
	data.Resize(variantVector.Size() * size);

	if (type == VAR_FLOAT)
	{
		float* dataPtr = (float*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetFloat();
	}
	else if (type == VAR_VECTOR2)
	{
		Vector2* dataPtr = (Vector2*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetVector2();
	}
	else if (type == VAR_VECTOR3)
	{
		Vector3* dataPtr = (Vector3*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetVector3();
	}
	else if (type == VAR_VECTOR4)
	{
		Vector4* dataPtr = (Vector4*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetVector4();
	}
	else if (type == VAR_MATRIX3)
	{
		Matrix3* dataPtr = (Matrix3*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetMatrix3();
	}
	else if (type == VAR_MATRIX4)
	{
		Matrix4* dataPtr = (Matrix4*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetMatrix4();
	}

	SetShaderParameter(param, (float*)&data.Front(), variantVector.Size());
}
[/code]

-------------------------

cadaver | 2017-01-02 01:05:16 UTC | #4

If you feel like committing that in (remember all render backends) go ahead.

Alternative would be to add VariantVector handling already to the overload with Variant parameter. (ie. check if type of variant is vector)

-------------------------

sabotage3d | 2017-01-02 01:08:44 UTC | #5

Hey guys it seems this topic is related to mine: [topic1647.html](http://discourse.urho3d.io/t/passing-uniform-arrays-to-glsl-shader/1584/1) . I am currently struggling to do it but I can't figure how without modifying the engine. Any chance for a PR of this solution? As I am trying to pass an array of quaternions to the shader.

-------------------------

friesencr | 2017-01-02 01:08:45 UTC | #6

Sorry I haven't done this yet.  Work has been very demanding lately :frowning: :frowning:.  The snippet I shared earlier has a bug if I remember.  I think it calculated the float size incorrectly.  My voxel renderer code has a working implimenation.  I found a pretty big weakness this approach and that is that the variant array it not efficient, and not capable of reusing data.  In my voxel renderer which has a sizable normal lookup table ~4-5% of gpu time was spent in this method. 

I think this code is good.  You have to replace the functions in OGLGraphics.cpp

[code]
void Graphics::SetShaderParameter(StringHash param, const VariantVector& variantVector)
{
	if (variantVector.Size() == 0)
		return;

	// base logic on the first parameter
	Variant first = variantVector.Front();
	VariantType type = first.GetType();
	int size;

	// only float types allowed
	switch (type)
	{
		case VAR_FLOAT:
			size = sizeof(float);
			break;
		case VAR_VECTOR2:
			size = sizeof(Vector2);
			break;
		case VAR_VECTOR3:
			size = sizeof(Vector3);
			break;
		case VAR_VECTOR4:
			size = sizeof(Vector4);
			break;
		case VAR_MATRIX3:
			size = sizeof(Matrix3);
			break;
		case VAR_MATRIX4:
			size = sizeof(Matrix4);
			break;
		default:
			return;
	}


	// validate that all parameters are the same as the first
	for (unsigned i = 1; i < variantVector.Size(); ++i)
	{
		if (variantVector[i].GetType() != type)
			return;
	}

	PODVector<unsigned char> data;
	unsigned numFloats = variantVector.Size() * size / 4;
	data.Resize(variantVector.Size() * size);

	if (type == VAR_FLOAT)
	{
		float* dataPtr = (float*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetFloat();
	}
	else if (type == VAR_VECTOR2)
	{
		Vector2* dataPtr = (Vector2*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetVector2();
	}
	else if (type == VAR_VECTOR3)
	{
		Vector3* dataPtr = (Vector3*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetVector3();
	}
	else if (type == VAR_VECTOR4)
	{
		Vector4* dataPtr = (Vector4*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetVector4();
	}
	else if (type == VAR_MATRIX3)
	{
		Matrix3* dataPtr = (Matrix3*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetMatrix3();
	}
	else if (type == VAR_MATRIX4)
	{
		Matrix4* dataPtr = (Matrix4*)&data.Front();
		for (unsigned i = 0; i < variantVector.Size(); ++i)
			*dataPtr++ = variantVector[i].GetMatrix4();
	}


	SetShaderParameter(param, (float*)&data.Front(), numFloats);
}


void Graphics::SetShaderParameter(StringHash param, const Variant& value)
{
    switch (value.GetType())
    {
    case VAR_BOOL:
        SetShaderParameter(param, value.GetBool());
        break;

    case VAR_FLOAT:
        SetShaderParameter(param, value.GetFloat());
        break;

    case VAR_VECTOR2:
        SetShaderParameter(param, value.GetVector2());
        break;

    case VAR_VECTOR3:
        SetShaderParameter(param, value.GetVector3());
        break;

    case VAR_VECTOR4:
        SetShaderParameter(param, value.GetVector4());
        break;

    case VAR_COLOR:
        SetShaderParameter(param, value.GetColor());
        break;

    case VAR_MATRIX3:
        SetShaderParameter(param, value.GetMatrix3());
        break;

    case VAR_MATRIX3X4:
        SetShaderParameter(param, value.GetMatrix3x4());
        break;

    case VAR_MATRIX4:
        SetShaderParameter(param, value.GetMatrix4());
        break;

    case VAR_VARIANTVECTOR:
	SetShaderParameter(param, value.GetVariantVector());
	break;
    default:
        // Unsupported parameter type, do nothing
        break;
    }
}
[/code]

-------------------------

sabotage3d | 2017-01-02 01:08:46 UTC | #7

Thanks friesencr. I will try it out.

-------------------------

