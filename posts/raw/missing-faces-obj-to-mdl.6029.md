claudeHasler | 2020-03-29 18:18:01 UTC | #1

I'm importing an .obj file via assimp and then displaying it. For some reason some faces of the model arent showing up when rendered. Ive tested the obj file in several different external viewers and they all show these faces no problem.
Urho:
![image|690x462](upload://yiTBvu4uXGrRMwehOyMBQqyzd6J.png) 
Other viewer:
![image|421x500](upload://6rCKlZOpr6pQbF1dnqx1WyoLwfj.png) 

What could be the problem here? Is there a way i can upload my .obj file?

-------------------------

SirNate0 | 2020-03-29 22:21:31 UTC | #2

My guess is that some of the faces might be oriented backwards, potentially. In terms of uploading, you could try a gist on GitHub or maybe PasteBin - .obj is a text file after all.

-------------------------

claudeHasler | 2020-03-30 13:24:56 UTC | #3

You are absolutely right! This did the trick:
[Code]
material->SetCullMode(CullMode::CULL_NONE);
 [/Code]
What disadvantage will i have setting this on all materials by default?

-------------------------

SirNate0 | 2020-03-30 13:30:30 UTC | #4

In general models are constructed with a consistent winding on the triangles. This allows the GPU to quickly discard half of the triangles based solely on the view and the triangle winding without any per-pixel work. Basically, it halves (ish) the amount of work to render a model.

So you'll lose that performance gain, but if you're not pushing the limits with your scenes, it may be worth doing that rather than correcting all of the models.

-------------------------

Dave82 | 2020-03-30 16:13:54 UTC | #5

Flip your normals in your editor before export and all should be fine.

-------------------------

claudeHasler | 2020-03-30 16:23:40 UTC | #6

Im building a kind of 3d viewer for CAD related applications where users will be able to load their own models, so editing is not an option. Ill just have to switch off culling

-------------------------

GodMan | 2020-03-30 17:41:50 UTC | #7

In AssetImporter use the -nf option. Some times Assetimporter thinks some faces are wrong and flips their normals. This way you don't have to disable culling completely.

-------------------------

Dave82 | 2020-03-30 18:00:30 UTC | #8

[quote="claudeHasler, post:6, topic:6029, full:true"]
Im building a kind of 3d viewer for CAD related applications where users will be able to load their own models, so editing is not an option. Ill just have to switch off culling
[/quote]
If you don't plan to use lights in your viewer then that should work. Hovewer disabling the culling will cause wrong lighting since normals are important in light calculations. (Lights will still use your flipped normals to shade faces)

-------------------------

claudeHasler | 2020-03-30 18:05:50 UTC | #9

Sadly the -nf option didnt help.

What do you mean with not use light? Without lights i wont see anything

-------------------------

Dave82 | 2020-03-30 19:28:18 UTC | #10

[quote="claudeHasler, post:9, topic:6029"]
What do you mean with not use light? Without lights i wont see anything
[/quote]
You can see your model without lights because there's always ambient light in the scene defined in your zone... Try adding a spotlight or a directional light and you will see that disabling culling is not a good idea.
EDIT : I just tested it and if normals are flipped in a model the lighting is wrong.

-------------------------

claudeHasler | 2020-03-31 19:00:05 UTC | #11

You're right. Is it possible to use front and back faces?

-------------------------

Dave82 | 2020-03-31 20:41:58 UTC | #12

AFAIK you can't... each vertex has only one normal which can point in one direction only. Lighting uses normals when calcualte light and shadows and it doesn't care about culling. It could be done if you really really need this but it doesn't worth the hassle since it is a very specific situation and it is easier to flip your normals at export or do it dynamically in your viewer. (vertex.normal = -vertex.normal)
Or you can modify the LitSolid shader to fit your needs.

-------------------------

claudeHasler | 2020-04-01 18:44:40 UTC | #13

I cannot influence the model origin, so I'd have to do something when I import the model, however i assumed assetImporter takes care of this.

Im confused, as any program I test the model in, (in .obj form) displays it perfectly, so i don't see why the assetImporter would flip the normals, and also not why when using -nf option in assetImporter the model still doesnt appear correct.

What do you mean with the LitSolidShader?

-------------------------

Dave82 | 2020-04-01 19:12:20 UTC | #14

My guess is you exported your model with a negative scale on one of the axes (maybe the model was mirrored in the editing software ?) and asset importer doesn't take the scale into account at import time. This is just an idea though... 

[quote="claudeHasler, post:13, topic:6029"]
What do you mean with the LitSolidShader?
[/quote]

Can you check your model's scale first ? Or even better : can you upload your model so i can check it if it's not problem ?

-------------------------

claudeHasler | 2020-04-01 20:19:16 UTC | #15

https://filebin.net/glxb28x4y9fwsl3h

Here are the original .obj and the .mdl generated with assetImporter.

Thanks!

-------------------------

Dave82 | 2020-04-01 22:23:15 UTC | #16

Ok i just tried to import your .obj file in 3ds max and the model shows up totally wrong (exactly as the converted mdl in Urho3d)
![kép|320x409](upload://s0gBvmZNqDGmTl4x4N1OURh5zA7.png)

Some faces are randomly flipped... Did you tried exporting your model in another format ?

-------------------------

Lumak | 2020-04-01 22:23:27 UTC | #17

I looked at your obj file in Maya and it looks the same as the result pic in Urho3D -- so many faces are flipped. You might consider importing it to Blender and tweak the faces and re-exporting it.

And, it looks like Dave is seeing the same thing.

-------------------------

claudeHasler | 2020-04-02 14:46:37 UTC | #18

Thanks for taking your time to help me. Sadly manual editing is simply not an option, as the program should display "any" model in a good way, and seeing as the viewers i've tested it in can do that successfully and without manual help that's the benchmark for me.

Ive tried using the unlit shader , and this seems to work, rendering all the faces i require, but now of course all faces are equally lit bright and thus unusable. Can this be refined somehow? Do you see any solution how i could get this to work without manual editing? Performance isnt my highest concern, and besides showing the model, lighting neednt be fancy either.

-------------------------

Lumak | 2020-04-02 15:50:16 UTC | #19

Can your 3D modeling tool export the file in .fbx format or something else that's common?

-------------------------

claudeHasler | 2020-04-02 17:59:44 UTC | #20

yes it can

https://gofile.io/?c=bpANTr 

but afaik assimp doesnt not support this, correct?

-------------------------

Lumak | 2020-04-02 19:29:55 UTC | #21

.fbx file format, what you've provided is .xbf. Not sure what that format is. But most ppl primarily deal with FBX files (3d model sellers, Unity, Unreal, etc.), and yes assimp supports that as well.

-------------------------

claudeHasler | 2020-04-02 20:36:56 UTC | #22

wow you're right, sorry. I tried every other model type that can be exporter by my viewer and then imported it with assimp with the same results sadly.

whats bugging me most about this is that the both the viewer im currently using (based on OpenCascade) as well as the Microsoft 3D viewer open this .obj file just find. What are they doing differently?

Sadly if i cant get this to work i may have to start exploring some other technologies which fit my data source better. (The original data export is a WRL or STP file)

-------------------------

JTippetts | 2020-04-02 21:18:48 UTC | #23

If you want to guarantee being able to load data outside your control, you may have to do a little extra processing/sanitizing. When drawing, whether or not a face is *visible* is based on the winding-order of the vertices; ie, in what order they are fed to the render pipeline. This is what the cull mode specifies. Specifying cull mode=NONE just means that no triangles are culled based on winding order. This means that you are likely to have issues on other engines/frameworks as well. I suspect that the Microsoft viewer is doing additional processing in the background on import, to correct the winding order, which is what you're probably going to have to do to make this work. 

If the model is well-formed (ie, the winding order of all triangles is consistent across all triangles) then you can test to see which way (toward the inside of the model or toward the outside) an arbitrary triangle is facing, and if it is facing the wrong way you can just perform a pass to flip the winding order and normal(s) of all faces.

With a closed model, you can determine whether a given point is *inside* or *outside* the model by using a raycast to some arbitrary point guaranteed to be outside the model. Count how many times the ray intersects the mesh, and if it is an odd number the point is inside, even number means it's outside. By calculating a point from the calculated normal of the face, you can determine whether the face is facing inward or outward, and flip it if necessary by swapping 2 of the vertices of the face, then flipping the normal to correct the lighting. Luckily, Urho3D's Geometry class does provide an [IsInside](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Geometry.h#L110) method for determining if a Ray originates from inside the model.

If the model is not well-formed, then you would have to perform this inside/outside facing test for every face, then re-calculate normals after you have flipped all non-conforming faces. This might occur eg if you are generating a geometry from a vertex soup.

-------------------------

claudeHasler | 2020-04-02 21:28:23 UTC | #24

Ill try to give that ago. What you propose is something i had thought of before, but why would something like this not be implemented in assimp already? I assumed it would be, seeing as i can specifiy the -nf option tells assimpt to NOT flip.

-------------------------

JTippetts | 2020-04-02 21:30:42 UTC | #25

It probably is something that assimp implements. I'm not really well-versed on Urho's assimp tool since I only ever use the Blender exporter, but you might dig around in the AssetImporter code to see if there is some modification you could make.

-------------------------

Lumak | 2020-04-03 17:37:24 UTC | #27

I tested your .obj file in AssetImporter yesterday to see if Assimp or the importer was somehow manipulating the normals, and confirmed neither manipulates it. Turns out the winding order and the face normals match exactly even for the faces that were flipped and something that I tried to detect and add a routine to fix, and passing the -nf (FixInfacingNormals) option had no affect on what Assimp returned: the mesh it generated were exactly the same.
I can assume the problem lies in how the mesh is constructed in your 3D modeling tool, and perhaps, not cleaned (Maya has mesh clean process to correct badly configured geoms).

-------------------------

GodMan | 2020-04-03 18:04:18 UTC | #28

I've been using 3ds max since 2008. I am positive that your issue is the way the model is created. Sometimes when beginners start 3d modeling they don't realize that making 3d geometry has a right way and a wrong way. 

Would you be willing to use a better 3d modeling program?

-------------------------

claudeHasler | 2020-04-03 19:13:21 UTC | #29

Sadly its not down to wanting to use a certain modelling program, as the files im getting are exported from a CAD program, which is my sole source of information. This CAD project will then be imported into my software where the data can be visualized for a specific task. So really i need to find a way to properly use the models i get. Do you see any realistic path to achieving this? I'd be open to solutions which are "lazy", it's just important that the models can be viewed successfully.

Is there a way to use "unlit" shading, but still get a differentiation of brightness depending on the angle of a specific face?

-------------------------

Dave82 | 2020-04-03 21:50:26 UTC | #30

You can modify the Lighting (hlsl or glsl) shader to hack something out but it won't be easy. Find the function called GetDiffuse in the shader and modify the light calculation to your needs.

float GetDiffuse(float3 normal, float3 worldPos, out float3 lightDir)

You can play with the lightDir and normal variables to come up with something. Happy experimenting...
But i still think that there is no real solution for broken models.. Those flipped faces are totally random and unpredictable.

-------------------------

SirNate0 | 2020-04-03 21:53:50 UTC | #31

If the faces don't need to have consistent lighting it should be pretty simple, probably just adding an absolute value on a dot product is my guess.

What CAD program are you using for this? It's possible you can make it output correct geometry.

-------------------------

Lumak | 2020-04-03 23:11:48 UTC | #32

I think Dave's on the right track. You can flip the normals in the vertex shader section of the LitSolid shader file, as an example:
```
void VS()
{
. . .
  vec3 n = cCameraPos - worldPos;
  if (dot(n, vNormal) < 0.0)
  {
    vNormal *= -1.0;
  }
}
```
Of course you'll have to set **cull="none"** in your material, as you've done previously.

Edit: It might be more convenient to write it as:
```
  vNormal = -vNormal;
```

-------------------------

Dave82 | 2020-04-03 23:18:12 UTC | #33

I had the same idea but this should not work in all situations. Consider a plain receiving light from one side and the user views it from the other side. This solution simply lights all faces (faces that are facing towards the light by default will receive light and which are facing away from the light will be flipped which ends up in all faces being lit)

-------------------------

SirNate0 | 2020-04-03 23:32:39 UTC | #34

I believe Lumak's solution (possibly changing worldPos to the worldPos of the vertex, I'm not sure what all the variables are in the shaders) is actually the correct solution lighting-wise. As long as the models don't have holes in them, it should always result in the faces having their normals pointing towards the camera, which should always be "outside" of the model on a closed model (which is presumably the only type of model you would get from a CAD program).

-------------------------

Lumak | 2020-04-04 00:13:09 UTC | #35

ok, that got me curious and I had to test the planes and see how it'll look with the code snippet that I posted:
[img]https://i.imgur.com/5XqO670.png[/img]
every model above the floor plane uses the flippedNormal technique, and I think they look ok, even the plane. 

* one on the left - seeing the side where the normal is not flipped and looking at the lit side.
* one on the right - seeing the back side where the normal is flipped and looking at the unlit side.

edit: 1 more test: flipping one of the planes complete around to face the light -- shading looks the same, however, you'll need not cull the shadow. Need to add it to the material:
```
	<cull value="none" />
	<shadowcull value="none" />
```

-------------------------

Lumak | 2020-04-04 02:23:09 UTC | #36

And Hasler's model:
[img]https://i.imgur.com/b6cHPqn.png[/img]

-------------------------

claudeHasler | 2020-04-04 08:26:49 UTC | #37

Wow, first of all i've got to say i've never seen a community as active and helpful as this one before! Thank you so much!

Ive tried to recreate you solution:
create a new shader file glsl / hlsl:
[Code]
void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vNormal = GetWorldNormal(modelMatrix);
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));

    vec3 n = cCameraPos - worldPos;
    if (dot(n, vNormal) < 0.0)
    {
      vNormal *= -1.0;
    }
...
[/Code]
[Code]
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    oNormal = GetWorldNormal(modelMatrix);
    oWorldPos = float4(worldPos, GetDepth(oPos));

     float3 n = cCameraPos - worldPos;
     if (dot(n, oNormal) < 0.0)
     {
       oNormal *= -1.0;
     }
[/Code]
save it as flippedNormal.hlsl/glsl
Edit my material:
[Code]
<material>
	<technique name="Techniques/FlippedNormalTechnique.xml" />
	<parameter name="MatDiffColor" value="0.6 0.6 0.6 1" />
	<parameter name="MatSpecColor" value="0 0 0 0" />
	<parameter name="MatEmissiveColor" value="0 0 0 1" />
        <cull value="none" />
	<shadowcull value="none" />
</material>
[/Code]

Then edit my technique to include the edited shader

[Code]
<technique vs="flippedNormal" ps="flippedNormal" psdefines="DIFFMAP">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
</technique>

[/Code]

Sadly this isnt working for me yet. Could you upload your material/technique/shader? Sorry I'm new to all this shader stuff

-------------------------

Dave82 | 2020-04-04 10:24:11 UTC | #38

[quote="Lumak, post:32, topic:6029"]
vec3 n = cCameraPos - worldPos;
[/quote]

Ahhh... you used the camera direction. That should work. In my solution i used the light direction... which cause the error i described above. Well done !

-------------------------

Lumak | 2020-04-04 13:24:19 UTC | #39

Gist link: https://gist.github.com/Lumak/59de5b19522b0c1d182e02b838ad4b91
- aFlipNormalTest.xml -- material, place it with your model or in a material folder
- LitSolidFlip.glsl - CoreData/Shaders/GLSL folder. modify HLSL the same if using DX
- NoTextureFlip.xml - CoreData/Techniques folder.

-------------------------

Modanung | 2020-04-04 22:33:05 UTC | #40

Wouldn't it make sense for this to be default behaviour whenever `cull` is set to `none`?

-------------------------

SirNate0 | 2020-04-04 23:20:18 UTC | #41

As long as it is not hard to work around (i.e. disable) that's probably a good choice. There could be some issues if someone is playing tricks with a not-closed model, or has some geometry that they want to be different on one side vs the other in terms of lighting (a plane, grass blades, leaves), but for the general case this is probably desirable behavior.

-------------------------

Lumak | 2020-04-05 14:49:03 UTC | #43

Not really, no. Most no-cull (aka double-sided) are used for unlit or transparent objects where objects are designed to be viewed from both sides and lighting/shading isn't an issue. The normal flipping in this case is required for this purpose, otherwise, the flipped faces due to bad geom construction will get rendered black. Not to mention, less computation performed in shader is always better.

-------------------------

