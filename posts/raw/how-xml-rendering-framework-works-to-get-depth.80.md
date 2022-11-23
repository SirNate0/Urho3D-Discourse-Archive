GGibson | 2017-01-02 00:57:51 UTC | #1

Hi everyone,

How can I ensure my shader has access to the depthBuffer, and is this what I want if I want to access scene depth information as a sampler2D? I'm also trying to access vert to fragment depth information using the varying vDepth = GetDepth(gl_Position) in the vertex shader. I'm implementing (someone else's) depth of field shader, but suspect I'm not getting the right depth information because the shader behaves as if plane of focus is always 0 from the camera. Also, I am having a hard time understanding from the documentation how the various xml files work together to ensure the shader is invoked with the required information made available (such as depth). If someone could at least point me to a good explanation of how the xml works or explain it, that would be much appreicated. Thanks! Below is my confused xml.

Docs I'm using in addition to the examples:
code.google.com/p/urho3d/wiki/Shaders
code.google.com/p/urho3d/wiki/RenderPaths

Shaders/DOF.xml
[code]
<shaders>
    <shader/>
</shaders>
[/code]

PostProcess/DOF.xml
[code]
<renderpath>
	<rendertarget name="dof" tag="DOF" format="rgba" filter="true"/>
    <command type="quad" tag="DOF" vs="DOF" ps="DOF" output="viewport">
        <texture unit="diffuse" name="viewport" />
        <texture unit="depth" name="viewport" />
    </command>
</renderpath>
[/code]

-------------------------

weitjong | 2017-01-02 00:57:51 UTC | #2

Welcome to the forum. Perhaps you are confused because you are referring to outdated documentation in google-code. The latest documentation can be found in Urho3D website (the URL is in the footer of this forum).
Incidentally Lasse (author of Urho3D) has just recently refactored the code for shaders parsing. I am afraid you will have to re-read the relevant sections in the new documentation (more specifically changes introduced in this commit [github.com/urho3d/Urho3D/commit ... 95531e1246](https://github.com/urho3d/Urho3D/commit/383e248b44627aba1e906af2e757c895531e1246)).

-------------------------

cadaver | 2017-01-02 00:57:51 UTC | #3

Getting depth in vertex shader means the depth of the object currently being rendered. If it's a post-process quad you're rendering, the depth is always 0 (near plane), so in this case I believe you need the depth of the already rendered opaque scene in the pixel shader. 

To sample the per-pixel depth, you will need to use either deferred / light prepass renderpaths, or the ForwardDepth.xml renderpath which performs an additional depth pass first for opaque objects. The latter has not been tested much, so I actually recommend starting with the deferred paths. If your application relies on the default renderpath you get from Renderer subsystem, you can easily reconfigure it with command line options, either -deferred or -prepass

In the renderpath command which needs to sample the depth buffer, add the following texture unit definition (assuming the linear depth buffer is called 'depth' as it is in Deferred.xml, Prepass.xml or ForwardDepth.xml)
[code]
<texture unit="depth" name="depth" />
[/code]

Then, look at the deferred light volume shaders (DeferredLight.glsl or PrepassLight.glgl) for an example of how to access the depth buffer. On OpenGL it's encoded as RGB to ensure all the color targets are same format (needed by 2.0 spec) so you'll have to decode it:
[code]
float depth = DecodeDepth(texture2D(sDepthBuffer, vScreenPos).rgb);
[/code]
where vScreenPos is a screen position texture coordinate calculated in the vertex shader ( vScreenPos = GetScreenPos(gl_Position) )

I'm referring to the post-shader refactor state of the code, so if you're not on the latest master branch revision I recommend to update. Btw. I'm going to nuke the Google SVN so that no-one uses the old docs mistakenly :slight_smile:

-------------------------

GGibson | 2017-01-02 00:57:51 UTC | #4

Thanks to both of you, and a lot more fidling around, I've got it working. Is this the right way though? I'm using deferred shading with a depth clear command in the xml as follows. Without the clear command I get weird depth information in the skybox regions (large vertical alternating bands of 0,1,0... depth values). Even with the clear command the first frame upon execution looks horrible, but is fine after, probably due to the order of commands and persistence of buffer states?

[code]
<renderpath>
	<rendertarget name="dof" tag="DOF" format="rgba" filter="false"/>
	<command type="quad" tag="DOF" vs="DOF" ps="DOF" output="viewport">
		 <texture unit="diffuse" name="viewport" />
		<texture unit="depth" name="depth" />
	</command>
	<command type="clear" color="1 1 1 1" depth="1.0" output="depth" />
</renderpath>
[/code]

Also, thanks for setting me straight about the documentation. And cudos to the person maintaining the build systems - having Urhos3D build out-of-the-box is pretty incredible.

-------------------------

cadaver | 2017-01-02 00:57:51 UTC | #5

Good to hear you got it working.

The deferred renderpath "optimizes" the G-buffer writing by not writing the skybox parts to the albedo/normal/depth buffers. Because opaque geometry is marked to stencil buffer and lights check it, lights will not render incorrectly to the skybox parts. But DOF would naturally need a cleared depth buffer right from the first frame. To have this work correctly you should create a custom deferred rendering renderpath, with the beginning like this:

[code]
<renderpath>
    <rendertarget name="albedo" rtsizedivisor="1 1" format="rgba" />
    <rendertarget name="normal" rtsizedivisor="1 1" format="rgba" />
    <rendertarget name="depth" rtsizedivisor="1 1" format="lineardepth" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="clear" color="1 1 1 1" output="depth" />
[/code]
Note the lack of "depth" attribute in the second clear command, which means the hardware depth buffer and is already reset in the first clear command which writes to the viewport output, so it's not necessary to reset again.

-------------------------

