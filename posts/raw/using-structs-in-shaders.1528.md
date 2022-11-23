franck22000 | 2017-01-02 01:08:18 UTC | #1

Hello, is it possible to do some refractoring in shaders system to use structs instead of that: 

[code]void VS(float4 iPos : POSITION,
    #ifndef BILLBOARD
        float3 iNormal : NORMAL,
    #endif
    #ifndef NOUV
        float2 iTexCoord : TEXCOORD0,
    #endif
...
...
[/code]

That would be much more nicer and easier to write shaders :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:08:18 UTC | #2

Yes it possible )
at first of all you will need going to Shader.cpp and fix it in CommentOutFunction  
[code]
bool Shader::BeginLoad(Deserializer& source)
{
    Graphics* graphics = GetSubsystem<Graphics>();
    if (!graphics)
        return false;

    // Load the shader source code and resolve any includes
    timeStamp_ = 0;
    String shaderCode;
    if (!ProcessSource(shaderCode, source))
        return false;

    // Comment out the unneeded shader function
    vsSourceCode_ = shaderCode;
    psSourceCode_ = shaderCode;
    //CommentOutFunction(vsSourceCode_, "void PS(");
    //CommentOutFunction(psSourceCode_, "void VS(");
    CommentOutFunction(vsSourceCode_, "PS_OUTPUT PS(");
    CommentOutFunction(psSourceCode_, "VS_OUTPUT VS(");

    // OpenGL: rename either VS() or PS() to main()
#ifdef URHO3D_OPENGL
    vsSourceCode_.Replace("void VS(", "void main(");
    psSourceCode_.Replace("void PS(", "void main(");
#endif

    RefreshMemoryUse();
    return true;
}
[/code]

and then you are free to use structs in shaders
little example:
[spoiler][pastebin]pjRA4tZ5[/pastebin][/spoiler]
actually I rewrite most of them in this style (except some part of post effect shaders), but now I want do some refactoring with names
because the Output or Input it's very long names(IMO), instead these names I want to change it to OUT and IN 
also I checking this shaders on DX9 by running std urho's examples and it seams that all run OK even on DX9

-------------------------

codingmonkey | 2017-01-02 01:08:19 UTC | #3

there is fixed names(OUT/IN) version.
[github.com/MonkeyFirst/urho3d-s ... 11-structs](https://github.com/MonkeyFirst/urho3d-shaders-dx11-structs)

[code]
#includes...

#ifdef COMPILEVS

struct VS_INPUT
{
    //vars
};

struct VS_OUTPUT
{
    //vars
};

VS_OUTPUT VS(VS_INPUT IN)
{
    VS_OUTPUT OUT;
    //code
    return OUT;
}
#endif

#ifdef COMPILEPS

struct PS_INPUT
{
    //vars
};

struct PS_OUTPUT
{
    //vars
};

PS_OUTPUT PS(PS_INPUT IN)
{
    PS_OUTPUT OUT;
    //code
    return OUT;
}
#endif

[/code]

-------------------------

