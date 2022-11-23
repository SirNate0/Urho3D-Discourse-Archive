sabotage3d | 2017-01-02 01:08:41 UTC | #1

Hi I am trying to pass an uniform array to GLSL shader. I tried via SetShaderParameter but I couldn't get it to work. For my custom instancing I am trying to pass an array of quaternions or matrices to the shader through C++. Is it currently supported?

-------------------------

cadaver | 2017-01-02 01:08:41 UTC | #2

Look at how the skinning matrix is defined and transferred as an array of floats (Batch.cpp line 245), that at least works.

-------------------------

sabotage3d | 2017-01-02 01:08:44 UTC | #3

Thanks cadaver. I am having some problems getting it to work via the Graphics class. Is there any specific workflow I need to follow in order to bind it to an existing material. If I set a color to red and I call it in the shader with uniform vec4 cmycol  it is not working. I think the Material class is missing the option for arrays. 
[code]
ShaderVariation*  vertexShader_ = graphics->GetShader(VS, "simple");
ShaderVariation*  pixelShader_ = graphics->GetShader(PS, "simple");
graphics->SetShaders(vertexShader_,pixelShader_);
graphics->SetShaderParameter("mycol",Vector4(1.0,0.0,0.0,1.0));
[/code]

-------------------------

cadaver | 2017-01-02 01:08:45 UTC | #4

You're right, for materials you currently have to use single uniforms. I suppose support for e.g. float array data could be added by allowing the VariantVector type in material shader parameters, but it would not be efficient since Graphics would have to reassemble the data from the individual Variants into one memory block before assigning to the GPU.

EDIT: using the Buffer Variant data type would be better, since it's already just a memory blob, but would be more cryptic to assign.

-------------------------

sabotage3d | 2017-01-02 01:08:46 UTC | #5

Thanks cadaver. Is there an example on how to do it with Buffer Variant data type? Does it need changes to the engine?

-------------------------

cadaver | 2017-01-02 01:08:46 UTC | #6

Possibility to set Buffer type Variants (freeform data blob, will be interpreted as float arrays) has been added to Graphics::SetShaderParameter Variant overload in the master branch. These will also be serialized/deserialized in materials, but will look hostile to text editing, so in practice you would have to set them in code.

Use Variant::SetBuffer(const void* data, unsigned size) to set from a memory blob. Or in AngelScript you'd do something like

[code]
    Variant array;
    VectorBuffer buf;
    buf.WriteFloat(1.0);
    buf.WriteFloat(2.0);
    buf.WriteFloat(3.0);
    buf.WriteFloat(4.0);
    ...
    array = buf;
    material.shaderParameters["MyArray"] = array;
[/code]

-------------------------

ghidra | 2017-01-02 01:08:47 UTC | #7

this is great!
Will be very useful!

-------------------------

sabotage3d | 2017-01-02 01:08:47 UTC | #8

Thanks a lot cadaver. It works like a charm.

-------------------------

sabotage3d | 2017-01-02 01:08:48 UTC | #9

I am currently testing animated transforms and the only way I found to get it working is by setting the Clear() method of the VectorBuffer inside the update. Is that efficient or there is a better way?

-------------------------

cadaver | 2017-01-02 01:08:50 UTC | #10

If you are using the Vectorbuffer WriteXXX() functions, then you need to Clear() before writing new data or else it gets appended. Using Variant::SetBuffer() instead with a memory blob that you provide and update (SetBuffer makes a copy of it) is potentially more efficient, at least in terms of function call count.

-------------------------

sabotage3d | 2017-01-02 01:08:51 UTC | #11

Do you have a simple example for a memory blob in C++? I am currently doing something like this inside the update method.
[code]for (int i =0; i<NUMINSTANCES; i++)
{
    _positions[i] += Vector3(0,0.1*sin(i),0);

    _positionbuf.WriteVector4(Vector4(_positions[i].x_, _positions[i].y_, _positions[i].z_,1.0));
}
    
_material->SetShaderParameter("vposition", _positionbuf);
_positionbuf.Clear();[/code]

-------------------------

cadaver | 2017-01-02 01:08:51 UTC | #12

No, I'm assuming competency of C++ pointers and "dirty" data manipulation using reinterpret casts and such, and am not going to explain that, but you should be able to refer to Urho's own vertex data manipulation code.

-------------------------

sabotage3d | 2017-01-02 01:08:55 UTC | #13

Thanks cadaver. I understand know that a memory blob means a void pointer.

-------------------------

