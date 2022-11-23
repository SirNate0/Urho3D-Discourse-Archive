sabotage3d | 2017-01-02 01:01:10 UTC | #1

Hello ,

I did some OpenGL ES profiling on IOS device and I cannot get more than 22 FPS on a really simple scene. 
I took Sample 11 Physics and I disabled shadows, materials and specular. I also removed the rbd's from the box stack, I just left them to profile the rendering.
These are the changes I made:

I added these lines and I commented the rigid bodies lines for the rbd stack.
[code]
 renderer->SetDrawShadows(!renderer->GetDrawShadows());
 renderer->SetSpecularLighting(!renderer->GetSpecularLighting());
 renderer->SetMaterialQuality(QUALITY_LOW); [/code]
When I load the sample my load is:
CPU: 21%
Memory: 45.4 MB
FPS: 17-22
If I start moving the FPS drops if I throw a box it lags super heavy for a few frames.
I made a OpenGL ES trace this is my log: [codepad.org/vP8Uj7G6](http://codepad.org/vP8Uj7G6)
I have also uploaded the trace to github it could be replayed in Xcode: [github.com/sabotage3d/urhotrace](https://github.com/sabotage3d/urhotrace)
This is the profiling suggestions and errors:
[img]http://i.imgur.com/bIf3qlq.png[/img]

-------------------------

sabotage3d | 2017-01-02 01:01:11 UTC | #2

Hey guys any thoughts on this ? The draw calls are way too many for such a simple scene.

-------------------------

cadaver | 2017-01-02 01:01:11 UTC | #3

The amount of drawcalls in your trace seems normal. There are two passes: ambient light+environment mapping pass, and directional light pass. I assume you are looking at the box stack, as there's a lot of draws with same state. On OpenGL ES instancing is not being used.

I personally haven't tested the performance of the more complex materials, like environment mapping, on iOS. It might be that the shader is triggering dependent texture reads, which are bad for performance. You could try making the boxes use the default (untextured) material and see whether you get better FPS.

At some point (possibly today) I will have time to test the Physics sample on an iPad2 and see if I can verify the bad performance. On Android I've seen it perform reasonably acceptably, often reaching 60 fps with shadows on, if you're not looking at the boxes from close up. Going close to the environment mapped boxes I noticed lowered FPS.

In general, the samples have been made (and tested on) desktop systems, and we don't make performance guarantees for them, especially for mobile platforms. Your own content will heavily determine your performance. Of course the hope is that Urho itself does not induce systematic (not depending on content) slowdown.

-------------------------

sabotage3d | 2017-01-02 01:01:11 UTC | #4

Thank you for your input on this. I have disabled shadows, materials are set to low quality and the specular is off. The physics are off as well. 
I can see in the profiling that there is GL error: Inavlid Enum and calls from OpenGL that are not supported on the ES version, also there are some redundant calls.
Is it currently possible to use VAO on mobile ? I have to check if the textures are not too heavy for mobile and if they have proper encoding.
On similar scene in Ogre I am getting around 60 fps with VAO enabled.

-------------------------

cadaver | 2017-01-02 01:01:11 UTC | #5

Setting materials to low quality doesn't remove the environment mapping in case of the StoneEnvMap.xml material, so you're still looking at 2 passes. Take a look at the material file:

[code]
<material>
    <technique name="Techniques/DiffNormalPackedEnvCube.xml" quality="1" />
    <technique name="Techniques/DiffEnvCube.xml" quality="0" />
    <texture unit="diffuse" name="Textures/StoneDiffuse.dds" />
    <texture unit="normal" name="Textures/StoneNormal.dds" />
    <texture unit="environment" name="Textures/Skybox.xml" />
    <parameter name="MatSpecColor" value="0.3 0.3 0.3 16" />
    <parameter name="MatEnvMapColor" value="0.1 0.1 0.2" />
</material>
[/code]

When comparing scenes it's important to consider the render techniques being used, otherwise the comparison to eg. an Ogre scene can be a bit meaningless. If you use a simpler material, like diffuse or diffuse normalmapped, Urho is able to combine the ambient and first per-pixel light into one pass, in which case the rendering should be more performant. The error is something to look into, as it can potentially erode performance. 

Urho does not use VAO. But in this case I don't expect it to make a lot of difference, instead the pixel shader & framebuffer blending (memory bandwidth) utilization is likely dominant in the Physics scene.

-------------------------

sabotage3d | 2017-01-02 01:01:11 UTC | #6

I see now it makes sense I will try and remove the environment lighting to see how does it affect the performance.
Is there a particular reason why Urho3d is not using VAO on mobile ?

-------------------------

cadaver | 2017-01-02 01:01:11 UTC | #7

The reason is that Urho's OpenGL renderer is based on OpenGL 2.0 with a few minimal extensions, and it was mapped to OpenGL ES as closely as possible. If I understand right it would be an extension on ES.

Some people have been working on modern OpenGL, see for example [github.com/boberfly/Urho3D/tree/moderngl](https://github.com/boberfly/Urho3D/tree/moderngl) but there is no specific timeline for bringing this to the mainline Urho, because in doing that we will have to ensure that things don't break, and preferably support for old OpenGL versions should also be kept. (I believe the fork/branch in question just "overwrites" old GL support)

-------------------------

sabotage3d | 2017-01-02 01:01:12 UTC | #8

I think the combination of VAO with VBO are a must for optimal performance on Opengl ES . The majority of mobile devices support OpenGL ES 2.0 which supports both VAO and VBO .
I think this is a tutorial toward OpenGL 3 but it looks similar to the ES api: [opengl.org/wiki/Tutorial2:_ ... s_(C_/_SDL](https://www.opengl.org/wiki/Tutorial2:_VAOs,_VBOs,_Vertex_and_Fragment_Shaders_(C_/_SDL))
This one might be more IOS specific: [developer.apple.com/library/ios ... xData.html](https://developer.apple.com/library/ios/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/TechniquesforWorkingwithVertexData/TechniquesforWorkingwithVertexData.html)

-------------------------

cadaver | 2017-01-02 01:01:12 UTC | #9

Ok, have tested 11_Physics on iPad2. Shadow receiver rendering, which induces a dependent texture read in the "high quality" shadow mode, and environment mapping of up close boxes bring the performance down to about 20 FPS or even lower depending of how much screen space they fill (seems totally pixel shader bound.) Switching to Diff.xml technique for the boxes, and turning off shadows allows to run at 50-60 FPS, also when the rigidbodies are awake. Physics takes about 5 ms per frame when under load (when the whole stack is awake) and about 0.5 ms when objects are at rest. It's not ideal, but not worrying either. In conclusion I don't see any unexpected performance problems on iOS.

-------------------------

sabotage3d | 2017-01-02 01:01:12 UTC | #10

Nice :slight_smile: I will able to test it as well when I get home .   Do you know if anyone is working on more specific IOS OpenglES implementation or I will have to pursue that road alone ?
Is the Opengl ES currently unified or there is an option to be more modular like in Irrlicht drivers extensions  which are completely separated from the core engine itself ?

-------------------------

cadaver | 2017-01-02 01:01:12 UTC | #11

I'm not aware of OpenGL ES specific work. The renderer code is fairly monolithic, so you would be looking at Urho core changes to the Graphics class, which manages low-level rendering and the extensions.

-------------------------

sabotage3d | 2017-01-02 01:01:12 UTC | #12

I have set all the materials in the example to:
[code]<technique name="Techniques/Diff.xml" quality="0" />[/code]
My FPS went from 22 to 27. I tried even removing the materials it is was almost the same tops at around 30. If I look only at the sky it goes 50+ if I look at the ground it drops there something really weird as I just ran my Ogre example and it runs on over 55+ FPS . I am doing all my tests on Iphone 4 it is quite old but still should get the job done. I have completely disabled physics in these tests so we are looking at rendering only. 
If you can share you project I can run it on the same device and compare if I am not doing something wrong.

-------------------------

cadaver | 2017-01-02 01:01:12 UTC | #13

I produce projects with unmodified CMake batch files from latest master branch so I don't think there's value in sharing them.

There's nothing weird I believe. It simply looks like that the rendering of the objects (stone material with Diff technique) is still too heavy for your hardware to cope with, while the sky, as it's a very simple unlit shader, is simple enough to yield better performance. Probably the Ogre scene you compare to is rendering everything with a minimally simple shader.

Even the shader used by the Diff.xml technique is quite complex, and the physics scene has a per-pixel directional light being applied to the objects. You could try switching the light to per-vertex mode. See Light::SetPerVertex().

Generally, to optimize performance you will sooner or later have to dig into the shaders for yourself. In this case the poor performance has nothing to do with eg. missing VAO support, just pixel shaders being too complex for your hardware.

-------------------------

sabotage3d | 2017-01-02 01:01:12 UTC | #14

As I did a test where I removed the materials from the objects is the Diff.xml still valid in this case. 
I will try to port the same shaders from Ogre3d to Urho3d and it see how it goes. 
One question though how does the OpenGL to OpenGL ES conversion happens I couldn't figure that out.

-------------------------

cadaver | 2017-01-02 01:01:12 UTC | #15

The untextured default material uses NoTexture.xml instead of Diff.xml, which still maps to the same LitSolid shader minus one texture read for the diffuse texture. The lighting calculations are quite the same (= heavy)

You'll see things that are done differently for OpenGL ES by checking for specific defines:
in the Urho .cpp code, #ifdef GL_ES_VERSION_2_0
in the shader GLSL code, #ifdef GL_ES

-------------------------

sabotage3d | 2017-01-02 01:01:12 UTC | #16

Thanks is there an easy way of using custom shaders. I couldn't find much information in the docs. I guess they have to be exposed as parameters in the material system.

-------------------------

cadaver | 2017-01-02 01:01:13 UTC | #17

There is no concept of custom shaders, just shaders. The documentation is not the most detailed, but the idea is that you are free to define your own material techniques, which reference your own shaders. Something like the LitSolid shader is not ever referenced by hardcoded engine code. There are some conventions however that you need to follow if you want things like forward per-pixel lighting to work properly. See [urho3d.github.io/documentation/H ... ering.html](http://urho3d.github.io/documentation/HEAD/_rendering.html) page.

-------------------------

sabotage3d | 2017-01-02 01:01:13 UTC | #18

Maybe as a quicker test is there a shader I can set for simple textured surface without any diffuse or specular calls ? And I will remove the light from the scene might be causing issues as well.

-------------------------

cadaver | 2017-01-02 01:01:13 UTC | #19

Take a look at the DiffUnlit.xml or NoTextureUnlit.xml techniques. They should be just as cheap as the sky shader.

-------------------------

sabotage3d | 2017-01-02 01:01:13 UTC | #20

Thanks a lot I removed the light and set the shaders to DiffUnlit.xml and it is a lot better it is around 50+ it is comparable to what Ogre gives.

-------------------------

