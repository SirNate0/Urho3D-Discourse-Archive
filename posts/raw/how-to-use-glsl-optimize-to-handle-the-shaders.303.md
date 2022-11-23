hualin | 2017-01-02 00:59:30 UTC | #1

HI,
Currently I can't use glsl-optimize to optimize the shaders, it says that 

Failed to compile Uniforms.glsl:
0:69(1): error: syntax error, unexpected $end

or

Failed to compile Basic.glsl:
0:1(3): preprocessor error: Invalid tokens after #
0:2(2): preprocessor error: Invalid tokens after #
0:3(2): preprocessor error: Invalid tokens after #
.

Can I use the optimizer to handle the shaders for mobile platform?

Thanks in advance.

-------------------------

boberfly | 2017-01-02 00:59:30 UTC | #2

Hi hualin,

Urho3D's GLSL shader files are not standard GLSL. When the files are parsed in-engine all the includes are resolved by the engine itself and doesn't use a GLSL extension to do that. Also the vertex shader and the fragment shader are contained in the one file, and their main function are renamed from VS()/PS() to main(), as well as all the parts that don't make sense for the pipeline stage are commented out like all the attribute defines in the fragment shader, and then they are split in-engine before sent to the GL implementation.

A better approach perhaps would be to embed glsl-optimize into the engine itself in this part if possible, or get Urho3D to dump the GLSL it generates itself, I think [code]graphics.BeginDumpShaders(const String&)[/code] should do it in AngelScript? Or in C++ [github.com/urho3d/Urho3D/blob/m ... s/Shader.h](https://github.com/urho3d/Urho3D/blob/master/Source/Engine/Graphics/Shader.h) has: [code]const String& GetSourceCode(ShaderType type)[/code]

Cheers
-Alex

Edit: I meant attributes are commented out in the fragment shader not vertex shader... :slight_smile:

-------------------------

cadaver | 2017-01-02 00:59:30 UTC | #3

Yes, I second what boberfly said, to make glsl-optimize work properly it practically has to be embedded into the engine. During runtime, shaders are requested with various compilation defines (these are usually not known beforehand), and the shader code with those defines should be fed to glsl-optimize. The optimized code for that particular shader variation could then be written to disk and loaded directly on subsequent runs.

However when you're doing this to optimize mobile shaders, the problem is that the desktop shader code and defines are not the same, and actually getting optimized shader code back from a device would not be convenient. Maybe you could make the desktop version also optimize and spit out the corresponding mobile shader, but this will take some hacking. The define GL_ES differentiates desktop & mobile mode in the shaders.

-------------------------

hualin | 2017-01-02 00:59:31 UTC | #4

Thank you, boberfly, and cadaver.
I see now.
Maybe I will try to do this.

-------------------------

