cadaver | 2017-01-02 00:57:38 UTC | #1

I'm thinking of how to make shader & technique authoring more pleasant. Currently there are rather many moving parts to this. You need to author the shader description xml file, then refer to the correctly named shader permutations in a technique, which is not very obvious. Some of this complexity is necessary, as you need to be able to specify different passes from the same shader (for example per pixel lighting with or without ambient.) But part of this can be improved. I'm thinking of the following and would like to hear opinions:

- Get rid of the shader description XML's 
- Consequently, it becomes impossible to enumerate all possible permutations of a shader beforehand. But this shouldn't be a big loss.
- D3D mode only: ShaderCompiler utility is removed and instead engine takes direct dependency to the shader compiler DLL. Like before, the encountered shader variations will be compiled to binaries so that later loading is quicker.
- Advantage to the above is that we can see HLSL compile errors in the engine log, just like we see GLSL errors
- Techniques don't refer to shader permutation names anymore. Rather, they refer to the shader resource, and give compilation defines directly. Shader reference & compilation defines can be also global to the technique to avoid repeated specifying in every pass. An example:

Old way:
[code]
<technique>
    <pass name="base" vs="LitSolid" ps="LitSolid_Diff" />
    <pass name="litbase" vs="LitSolid" ps="LitSolid_DiffAmbient" />
    <pass name="light" vs="LitSolid" ps="LitSolid_Diff" depthtest="equal" depthwrite="false" blend="add" />
</technique>
[/code]
New way:
[code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP" />
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
</technique>
[/code]
- Internally, the engine specifies more compilation defines, such as SKINNED or INSTANCED, so there are actually more permutations than specified in the technique (just like before)
- Finally, go through the existing shaders and where it makes sense, break them up + refactor common operations into functions. The LitSolid shader is already quite monstrous.

-------------------------

cin | 2017-01-02 00:57:38 UTC | #2

... and use [i]technique[/i] extension for technique files. =)

-------------------------

Azalrion | 2017-01-02 00:57:39 UTC | #3

From the sounds of it the shaders would still require the use of ifdef for the defines but would they still need the 'required permutations'?

-------------------------

cadaver | 2017-01-02 00:57:39 UTC | #4

You mean the in-engine permutations, like skinning, point/dir/spotlight, low/highquality shadows, yes they would be required depending in which pass the shader is being used.

But much of them can be hidden inside functions, like eg. the GetModelMatrix() function already does, and for example per-pixel lighting could be hidden better. Sometimes it's hard to hide everything, for example when different lighting needs different varyings to be transmitted from VS to PS, or when different vertex inputs are needed. But it's also possible to "undo" some of the trickier (and to be honest, not so necessary on current hardware) optimizations in favor of easier to understand shaders, for example calculating the tangent basis in pixel shader, and always just transmitting a world position (instead of eg. an eye vector) to the PS for light calculations.

-------------------------

primitivewaste | 2017-01-02 00:57:39 UTC | #5

Internalizing shadercompiler sounds good, better HLSL debugging is reason enough.
The proposed new technique setup does seem more intuitive.

-------------------------

cadaver | 2017-01-02 00:57:39 UTC | #6

If the shader compiler is supplied a define that's not actually used, it would result in the same binary shader code being compiled and stored twice as two "different" permutations.

There could be a check (at least in debug mode) by simply searching the shader source code for all the expected defines, and outputting a warning if not all are present. Usually that also results in a visual artifact, like missing proper fog in your example, so with properly authored shaders this should not normally happen.

-------------------------

weitjong | 2017-01-02 00:57:40 UTC | #7

I am wondering whether the compiling and linking of some pre-selected shader variations can be *requested* to be done fully or incrementally after the game engine starts (e.g. in the game loading stage), rather than compiling and linking when they are first encountered during the game play. Although I have not really profiled it, I used to be able to observe a slight lag in OpenGL mode at the beginning of a heated battle (in NinjaSnowWar :slight_smile: ), but the lag is less observable now after recent optimization (evaluates shader combination on demand).

I know this topic is only about shader refactoring but I am wondering again whether RenderPaths description XML is in the scope. I often find myself need to "extend" the existing RenderPaths with just some small modification (e.g. inserting/deleting command in between). Although it can be done programmatically, but do you think it makes sense to enhance the XML to include new elements that give the option to a) extend from an existing RenderPath and b) specify modification instructions. With this, the PrepassHDR.xml can be described with fewer elements extending from Prepass.xml and easier to maintain in the long run because no code duplication.

-------------------------

cadaver | 2017-01-02 00:57:40 UTC | #8

Yes, the frame hitch is a problem and there should be a function to ensure for a material that its shaders are all compiled. NinjaSnowWar is a good test case because simply ensuring shaders for the scene materials isn't enough, also the objects (ninja, potions etc.) have to be preloaded.

I haven't planned renderpath extending / inheriting directly in XML myself but if you find a nice way or syntax to do it, feel free to go ahead with it.

-------------------------

weitjong | 2017-01-02 00:57:40 UTC | #9

[quote="cadaver"]I haven't planned renderpath extending / inheriting directly in XML myself but if you find a nice way or syntax to do it, feel free to go ahead with it.[/quote]

It turns out to be easier than I thought. Thanks to Alex Parlett's RFC 5261 patching mechanism. I have created a new branch containing a single commit for the refactored code here: [github.com/weitjong/Urho3D/tree/RenderPaths](https://github.com/weitjong/Urho3D/tree/RenderPaths) for your review. If you are OK with that, I will merge that into main Urho3D repository.

Sorry for off-topic discussion.

-------------------------

cadaver | 2017-01-02 00:57:40 UTC | #10

Yes, it looks straightforward and clean. It's OK to merge.

-------------------------

