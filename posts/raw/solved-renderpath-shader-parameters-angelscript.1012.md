ghidra | 2017-01-02 01:04:48 UTC | #1

I am trying to manipulate a renderpaths command shader parameter with anglescript.
Based on the docs, it looks like I should be able to access the value and change it.
However, based on how I succesfully am able to manipulate a materials shader parameters, I am not able to do wo with the renderpaths.

as an example:
[code]
Quaternion rot = cameraNode.rotation;
float pitch = rot.pitch;
renderer.viewports[0].renderPath.commands[2].shaderParameters["CameraPitch"]=Variant(pitch);
[/code]

the error i get is:
Non-const method call on read-only object reference
void RenderPathCommand::set_shaderParameters(const String&in, const Variant&in)

It looks like it is trying, but I must be doing something off.

-------------------------

cadaver | 2017-01-02 01:04:49 UTC | #2

The render path commands are value types, so you can't modify their parameters directly. Instead you'll have to "get" the command first to a local variable, modify it, then "set" it back.

-------------------------

ghidra | 2017-01-02 01:04:49 UTC | #3

That did it. Thank you.

[code]
RenderPathCommand pt = renderer.viewports[0].renderPath.commands[2];
pt.shaderParameters["CameraPitch"]=Variant(pitch);
pt.shaderParameters["CameraYaw"]=Variant(yaw);
pt.shaderParameters["CameraRoll"]=Variant(roll);
renderer.viewports[0].renderPath.commands[2] = pt;
[/code]

as a sidenote, i know that there is a uniform that has the camera rotation matrix, this is all because i'm porting a shader that expects it in this format, and I'm too lazy to extract it in the shader from the matrix. (actually i tried and failed, and this works, so yeah)

-------------------------

