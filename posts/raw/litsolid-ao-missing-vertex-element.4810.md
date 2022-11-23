I3DB | 2019-01-12 00:52:24 UTC | #1

I'm converting the Basic Rendering Techniques sample to run on hololens. Currently have all the techniques working but two. 

ERROR: Failed to create input layout for shader LitSolid(AO) due to missing vertex element(s) (HRESULT 80070057)

System.Exception: Failed to create blend state (HRESULT 80070057).

That technique is defined here: https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Sample43/MatDiffAO.xml

The code using it is here: https://github.com/xamarin/urho-samples/tree/master/FeatureSamples/Core/43_BasicTechniques

Specifically: https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/FeatureSamples/Core/43_BasicTechniques/BasicTechniques.cs#L104

As an aside, the other technique not working is the CustomShader technique which is missing the HLSL shader. Can anyone offer how to get the HLSL shader given the GLSL shader? 

It's not complex: https://github.com/xamarin/urho-samples/blob/master/FeatureSamples/Assets/Data/Shaders/GLSL/Sample43CustomShader.glsl

This sample works on other platforms.

-------------------------

GodMan | 2019-01-11 17:27:50 UTC | #2

So do you need someone to convert that opengl shader to hlsl?

-------------------------

Modanung | 2019-01-11 17:37:42 UTC | #3

https://docs.microsoft.com/en-us/windows/uwp/gaming/glsl-to-hlsl-reference

-------------------------

I3DB | 2019-01-11 18:09:32 UTC | #4

[quote="GodMan, post:2, topic:4810, full:true"]
So do you need someone to convert that opengl shader to hlsl?
[/quote]

I didn't know if there is an easy way to do it, for instance with a tool. But it looks like not.

When I get time I'll work through it as per the link @Modanung provided. 

I just wanted to get all those materials in the sample code working on hololens.

Getting to the root cause of the DiffAO material or shader issue is the more important issue  because root cause of the error is not yet known, whereas the CustomMaterial related error just needs the GLSL to HLSL conversion.

-------------------------

I3DB | 2019-01-11 21:58:48 UTC | #6

I wiped out the code and started fresh. Whereupon the DiffAO related object at least paints, but still throws the error about the missing vertex.

Also, modified the TechniqueCustomShader.xml file from:
```

<!--Sample23CustomShader.glsl-->
<technique vs="Sample43CustomShader" ps="Sample43CustomShader" vsdefines="NOUV" >
    <pass name="alpha" depthwrite="false" blend="alpha" />
</technique>
```
to 
```
<!--Sample23CustomShader.glsl for open GL systems, but on D3D it will go for the HLSL file -->
<technique vs="CustomLitSolid" ps="CustomLitSolid" vsdefines="NOUV" >
    <pass name="alpha" depthwrite="false" blend="alpha" />
</technique>
```

Why? Because I'm just not a shader guru and don't aspire to be one. And would just like the SharpReality c# samples to run on a hololens. And the CustomListSolid is a fairly interesting technique to view, but can't put into words just what it is doing.

-------------------------

I3DB | 2019-01-12 00:54:06 UTC | #7

Just wanted to keep the error that's occuring:

[4] [Fri Jan 11 19:40:33 2019] ERROR: Failed to create input layout for shader LitSolid(AO) due to missing vertex element(s) (HRESULT 80070057)
System.Exception: Failed to create blend state(HRESULT 80070057). You can omit this exception by subscribing to Urho.Application.UnhandledException event and set Handled property to True.
ApplicationOptions: args -w -nolimit -x 1268 -y 720 -p "CoreData;Data" -touch -hd -landscape -portrait
[4][Fri Jan 11 19:40:39 2019] ERROR: Failed to create blend state (HRESULT 80070057)

-------------------------

I3DB | 2019-01-12 01:42:09 UTC | #8

In the urho3d docs, there is this:

## Inbuilt compilation defines

When rendering scene objects, t_he engine expects certain shader permutations to exist_ for different geometry types and lighting conditions. These correspond to the following compilation defines:

Vertex shader:

*** NUMVERTEXLIGHTS=1,2,3 or 4: number of vertex lights influencing the object**


Could this be what the error is referring to? There is a missing vertex light?

-------------------------

I3DB | 2019-01-25 22:34:12 UTC | #9

Got the urho logging going, so getting a bit more info, but not much. Here's some of the log when loading the basic rendering techniques sample:
```
1:)  [Fri Jan 25 17:25:27 2019] DEBUG: Loading resource Shaders/HLSL/CopyFramebuffer.hlsl
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Compiled vertex shader CopyFramebuffer()
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Compiled pixel shader CopyFramebuffer()
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Compiled vertex shader Water()
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Compiled pixel shader Water()
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Loaded cached vertex shader CustomLitSolid(NOUV)
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Loaded cached pixel shader CustomLitSolid()
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Compiled vertex shader LitSolid(AO)
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Compiled pixel shader LitSolid(AO DIFFMAP)
4:)  [Fri Jan 25 17:25:28 2019] ERROR: Failed to create input layout for shader LitSolid(AO) due to missing vertex element(s) (HRESULT 80070057)
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Compiled pixel shader LitSolid(DIFFMAP DIRLIGHT PERPIXEL SPECULAR)
1:)  [Fri Jan 25 17:25:28 2019] DEBUG: Compiled pixel shader LitSolid(DIFFMAP)
1:)  [Fri Jan 25 17:25:30 2019] DEBUG: Compiled vertex shader Unlit(NOUV)
1:)  [Fri Jan 25 17:25:30 2019] DEBUG: Compiled pixel shader Unlit()
1:)  [Fri Jan 25 17:25:30 2019] DEBUG: Compiled pixel shader LitSolid(AMBIENT DIRLIGHT NORMALMAP PERPIXEL)
Failed to create blend state (HRESULT 80070057). You can omit this exception by subscribing to Urho.Application.UnhandledException event and set Handled property to True.
ApplicationOptions: args -w -nolimit -x 1268 -y 720 -p "CoreData;Data" -touch -hd -landscape -portrait :Error
4:)  [Fri Jan 25 17:25:30 2019] ERROR: Failed to create blend state (HRESULT 80070057)
1:)  [Fri Jan 25 17:25:31 2019] DEBUG: Removed unused screen buffer size 1268x720 format 10
```

Trying to understand the root cause of this error:


[quote="I3DB, post:9, topic:4810"]
4:) [Fri Jan 25 17:25:28 2019] ERROR: Failed to create input layout for shader LitSolid(AO) due to missing vertex element(s) (HRESULT 80070057)
[/quote]

**`E_INVALIDARG` :**  One or more arguments are not valid ( `0x80070057` )

-------------------------

lezak | 2019-01-25 23:22:50 UTC | #10

From LitSolid.hlsl:

> #ifdef AO
            // If using AO, the vertex light ambient is black, calculate occluded ambient here
            finalColor += Sample2D(EmissiveMap, iTexCoord2).rgb * cAmbientColor.rgb * diffColor.rgb;
        #endif

AO uses second UV map and probably that's what You're missing.

-------------------------

I3DB | 2019-01-27 03:42:34 UTC | #11

Ok. But not sure what to do to fix that.

Experimented (did little changes all over the code, in the material file, the hlsl shader file, etc) trying to get some change in the error message. Nothing I did changed that error message. 

Also noted that DiffAO.xml won't show anything, but DiffAOAlpha.xml gives the exact same error but does show some of the material. 

Also verified the [UWP Feature Sample](https://github.com/xamarin/urho-samples/tree/master/FeatureSamples/Core/43_BasicTechniques) behaves identically as my converted Hololens sample, and it does. Both generate the exact same message for UWP.

To verify that this feature sample creates the error, did a simple change and then ran it.

The change was to allow the sample to be included, the author's of the UWP sample purposely excluded the Basic Techniques sample for UWP. In the file MainPage.XAML.cs, added the comment characters to allow Basic Techniques to be included. :
```
		public MainPage()
		{
			Urho.Application.UnhandledException += (s, e) => e.Handled = true;
			InitializeComponent();
			GameTypes = typeof(Sample).GetTypeInfo().Assembly.GetTypes()
				.Where(t => t.GetTypeInfo().IsSubclassOf(typeof(Application)) 
					&& t != typeof(Sample) //&& t != typeof(BasicTechniques) 
					&& t != typeof(PBRMaterials) && t != typeof(DynamicGeometry))
				.Select((t, i) => new TypeInfo(t, $"{i + 1}. {t.Name}", ""))
				.ToArray();
			DataContext = this;
		}
```

-------------------------

lezak | 2019-01-26 21:34:29 UTC | #12

[quote="I3DB, post:11, topic:4810"]
Ok. But not sure what to do to fix that.
[/quote]

Are You using model with second UV map? If not, don't use technique that require second UV with model that don't have it.

-------------------------

I3DB | 2019-01-26 22:52:25 UTC | #13

Well, I just don't know if it has the second UV map. I'm not experienced with materials, or models or blender. I'm coming at this from a code first approach, and this is one of the few things I've not gotten past. Shadows is a second.

But here is what I do know:

The feature samples provided with SharpReality, can run this without the error, when run on WPF or WinForms platforms. It fails with UWP.

Because two platforms run this same model, and don't have the error, it would seem it's not a missing UV map in the model. Again, newbie assumption here I'm making.

The only difference, besides possible platform differences, and  that I can find with my beginner eyes, is the UWP platform sample includes it's own Data file. 

So I took all those files, and added to them all the files in Data/Assets folders I could find, those files used by the WPF and WinForms samples. My Data folder is now about .5 GB in size, bursting with every file found. And I don't get any messages about missing files (except one custom hlsl shader, that is unrelated to this).

Now, my assumption all along is that some file is missing, because it works fine on WPF and winforms.

If I could find some way to relate that error message to something tangible, something to do other than hope, then maybe I'll make progress. Have reviewed all I know to review, but in the end, it will surely be something totally simple. That's just how it goes.

Edit: Here's another difference. The WPF and Winforms samples must be running OpenGL, because they also show the CustomMaterial, and it's shader is only provided in the GLSL version.

So apparently the DiffAO works only on OpenGL, and there must be some difference in the HLSL file or there is something else missing.

-------------------------

lezak | 2019-01-27 02:06:00 UTC | #14

[quote="I3DB, post:13, topic:4810"]
So apparently the DiffAO works only on OpenGL, and there must be some difference in the HLSL file or there is something else missing.
[/quote]
This is not true. I've downloaded model used in the sample and on neather Directx nor OpenGL this material doesn't work properly, it's because of what I've said earlier - model don't have second UV set, OpenGL just doesn't log any error. Just to be clear I'm using 'normal' C++ Urho, but this shouldn't make a difference. 
As for Your "code first approach", this not a way to go with this error. <a href="https://urho3d.github.io/documentation/HEAD/_vertex_buffers.html">Here is the list </a> of vertex elements and before that there is important, in this case, sentence: " Each of the following elements may or may not be present". Error under discussion means that shader require element that is not present. If You want to fix it only from code, here is what You should do to make this sample work as it supposed to: calculate uv coordinates for every vertex of each geometry (this model have 3 of them) and place them in right place in vertex buffers. It can be done, but good luck with that (ok, in this particular case it may not be that hard, since You'd propably want to use same coordinates as UV1).
Now, here are realistic and much simpler  solutions: don't use this technique, since it's not suitable for this model, modify shader to use only one UV or use 3d modelling software to add missing vertex elements. You can also remove all "defines="AO" from "DiffAO" technique xml, but then it will be the same as "Diff.xml" technique.
To make it even more clear: nornal map can be another example - using normal map require tangent vertex element, if it's not present You'll get the same error on DirectX and on OpenGL material will be displayed without normal map. 
And for the reference, here is how this material look on model with second UV:![Screenshot_Sun_Jan_27_02_39_13_2019|690x356](upload://luIxM9IyBHyrGwVXKOc1aV3fsq.png)

-------------------------

I3DB | 2019-01-27 03:01:39 UTC | #15

That is how the material looks in the feature samples when run on the WPF and WinForms platforms. Those two platforms run all the materials in the Basic Techniques seemingly perfectly. I didn't know what DiffAO looked like until viewing on those. But, my eyes may not see enough detail, perhaps they are not right.

The UWP sample fails and there is nothing visible at all. 

I thought all three WPF, UWP and WInForms would be D3D11. But I don't understand where they get the HLSL shader for the CustomMaterial, so propose the WPF and WInForms samples run on GLSL not HLSL, and that is why they work. 

Here's the UWP, then WPF samples. The WPF sample also runs the CustomMaterial without error and only the GLSL shader is provided for it.

![PNG|573x500](upload://kc2oxotVTnHq2JuxE7zhsjgSq8b.jpeg) 

and now WPF
![WPF|690x394](upload://3sa2IV8dUIDowOptIcNA7WFKL3G.png)

Also on the UWP sample it looks like NoTextureMultiply isn't working right either.

-------------------------

I3DB | 2019-01-27 03:48:22 UTC | #16

[quote="lezak, post:14, topic:4810"]
And for the reference, here is how this material look on model with second UV:
[/quote]

Is that model available online? I'll try to run it and see how it goes. Or another model I can use with 2nd UV map.

But also think you're running OpenGL and that is why it is working. There isn't a working instance of DiffAO on HLSL shaders that I've found.

The current model used is the Urho.Shapes.Sphere and this is the material:
```
<material>
    <technique name="Techniques/DiffAO.xml" />
	<texture unit="diffuse" name="Sample43/Earth.jpg" />
	<texture unit="emissive" name="Sample43/Earth_SpecularMap.png" />
    <parameter name="MatSpecColor" value="0.3 0.3 0.3 1" />
</material>
```

[Read the link provided](https://urho3d.github.io/documentation/HEAD/_vertex_buffers.html), and checked the vertex buffers of a model that is working:
![VertexBuffersOfWorkingModel|690x393](upload://131GwPqeoKY4rbD4so79MgZFjy5.png) 

Not sure how visible it is, there  is a single buffer.

The element mask is Position | Normal | Color | TexCoord1 | Tangent.

Here's the same for a not working model, same model, but on UWP platform, and not working:
![NotWorkingModelWithAO|690x388](upload://roXOSqthJkzhtJ41y2u4LcP4IkP.png)

-------------------------

I3DB | 2019-01-27 17:29:54 UTC | #17

Have verified the WPF and Winforms samples are running the GLSL shaders.

So the primary difference between the working samples, and the NOT working sample is the working samples use LitSolid.GLSL and the NOT working sample uses the LitSolid.HLSL shader.

**I propose the LitSolid.HLSL shader does not work with AO. That it is faulty.**

[Similar but slightly different thread](https://discourse.urho3d.io/t/failed-to-create-input-layout-for-shader-litsolid-dirlight-normalmap-perpixel-due-to-missing-vertex-element/4538), not for AO.

-------------------------

I3DB | 2019-01-27 17:15:37 UTC | #18

[quote="GodMan, post:2, topic:4810, full:true"]
So do you need someone to convert that opengl shader to hlsl?
[/quote]

Exploring why the LitSolid.hlsl shader doesn't work with AO would be valuable, if you have time. As per my thesis ...

[quote="I3DB, post:17, topic:4810"]
I propose the LitSolid.HLSL shader does not work with AO. That it is faulty.
[/quote]

-------------------------

lezak | 2019-01-27 19:44:03 UTC | #19

I don't want to repeat, but once again: this material doesn't work properly with this model no matter what graphics API You are using. Screenshot of Your "working" version just confirms that, because the material is not displayed correctly. Here' s the tip if You don't see any difference between screenshot I posted and what You think is correct: look closer at the part of sphere that is occluded from the light, there is a quite noticeable diffrence in looks of continents and oceans. 
As for the model, I cannot upload it to the forum directly, but it's just a sphere with the same uv map in two slots made in blender.

-------------------------

I3DB | 2019-01-27 19:46:50 UTC | #20

Ok, is there any model anywhere ... anywhere obtainable, with two uv maps?

I'm not ready to learn blender yet.

[quote="lezak, post:19, topic:4810"]
Screenshot of Your “working” version just confirms that, because the material is not displayed correctly.
[/quote]

I've found that if I disable the vertex shading portion and just do the pixel shading of LitSolid.hlsl, then it will paint an output in UWP that looks very similar to the OpenGL version. So I am thinking that the glsl silently ignores VS, and just does PS for AO, at least for the model I'm using.

Alternatively,

[quote="lezak, post:14, topic:4810"]
modify shader to use only one UV
[/quote]

Is that easy? I looked through the file, and am not sure where the first UV map is being accessed, not to mention the second.

-------------------------

I3DB | 2019-01-28 00:02:43 UTC | #21

[quote="lezak, post:14, topic:4810"]
here is what You should do to make this sample work as it supposed to: calculate uv coordinates for every vertex of each geometry (this model have 3 of them) and place them in right place in vertex buffers. It can be done, but good luck with that (ok, in this particular case it may not be that hard, since You’d propably want to use same coordinates as UV1).
[/quote]

[So following the code as shown here](https://github.com/urho3d/Urho3D/wiki/How-to-define-3D-object-in-code) ... what I'd need to do is define another TexCoord on each vertex? 

Is that what will fix the model?

-------------------------

I3DB | 2019-02-02 23:45:43 UTC | #22

[Found an example of rewriting PS() in the litsolid shader](https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/HoloLens/02_HelloWorldAdvanced/Data/Shaders/HLSL/CustomLitSolid.hlsl#L1). This sample explains it enough to be able to provide a custom shader for the AO implementation.

This is enough to figure out a workaround. 

Still, at the point of use of the material in the code (mat = Material.FromImage(imageWithOneUVmap);), I suspect there is a simple way to correct this missing UV layer problem.

-------------------------

I3DB | 2019-02-03 23:47:47 UTC | #23

[This is the line causing that error message to appear](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Urho3D/CoreData/Shaders/HLSL/LitSolid.hlsl#L19).

If TEXCOORD1 is changed to TEXCOORD0, it will successfully paint the object, but the result is apparently is not proper AO.

![PNG|481x500](upload://hw5Q3K8zbSvIFryvsZGHDnhXIP1.jpeg) 

Still haven't got around to fixing CustomShader or NoTextureMultiply. The CustomShader in the sample is missing the HLSL shader, and not sure what is wrong with NoTextureMultiply.

-------------------------

I3DB | 2019-02-03 23:49:52 UTC | #24

[quote="I3DB, post:20, topic:4810"]
modify shader to use only one UV
[/quote]

That is what I've done at this point.

-------------------------

Leith | 2019-02-04 03:43:53 UTC | #25

Modify geometry to have two UV maps sounds like what you really want.

The vertex data in your model requires more than one UV per vertex - so go back to your modelling app, and add a second UV map, save the asset, and reimport it. You should not be hacking the AO shader to suit the model, you should be hacking the model to suit the shader.

-------------------------

I3DB | 2019-02-04 14:43:27 UTC | #26

[quote="Leith, post:25, topic:4810"]
Modify geometry to have two UV maps sounds like what you really want.
[/quote]

Yes, @lezak has been making that same point.

[quote="lezak, post:12, topic:4810"]
Are You using model with second UV map? If not, don’t use technique that require second UV with model that don’t have it.
[/quote]

[quote="lezak, post:14, topic:4810"]
As for Your “code first approach”, this not a way to go with this error.
[/quote]

[quote="lezak, post:14, topic:4810"]
use 3d modelling software to add missing vertex elements
[/quote]

To which I responded:


[quote="I3DB, post:20, topic:4810"]
I’m not ready to learn blender yet.
[/quote]

[quote="I3DB, post:13, topic:4810"]
I’m coming at this from a code first approach
[/quote]

In conclusion, was able to make a very simple change to an existing shader, and provided a custom shader for the particular problem, so I could continue to use the materials supplied with the original sample, and get close to a fully working sample. 

Going through the process in the code allowed me to grasp the linkages between the .xml material file, the techniques, textures and shaders.  Blender use hasn't yet transferred that knowledge to me (what I have gleaned from blender is I don't know it well enough to use it effectively yet, and it's just not yet the right time to begin to fully consume it with my mind, but have been slowly trodding that path, just not with determination, only curiosity)

Apparently, those much more experienced in graphics/3D world tech don't agree. That's fine, we all don't have to agree.

My next steps for this are to write a custom shader by converting the glsl custom shader to an hlsl shader. Then figure out why the NoTextureMultiply sample isn't working.

------

While @lezak points out the obvious differences between his AO display and mine, it would seem the edit I did and described above, produces identical results to his when ASSUMING the lighting, the ambient lighting, and material's settings and zone settings are defined identically.

Because in the custom shader I did, it uses the first UV map as the second. In the custom model he did, he created a second UV map by copying the first.

It would be great if all the samples just worked on all the platforms. But learning blender won't give me enough (or any) details on how to get the samples running on hololens without code changes. Digging into the code and actually getting the samples running on hololens does. But this code-first implementation is more about the hololens binding implementation than it is about urho3d (shadows not working on hololens).  But ultimately, without useful bindings, what good is urho3d?

-------------------------

lezak | 2019-02-05 02:07:31 UTC | #27

Rather sonner then later You'll reach the point where You'll have to use 3d modelling software, I would even say, that because we'll still discussing in this topic, You've already reached that point.
The thing about ambient occlusion texture is that it shouldn't be using overlapping UVs and that's why it's good to have it on the second UV, but if there is no overlapping (for example this case) there is no harm in using the same UV. 

[quote="I3DB, post:23, topic:4810"]
[This is the line causing that error message to appear ](https://github.com/xamarin/urho/blob/050fdf9943b154549e7928b32f398e727191202a/Urho3D/CoreData/Shaders/HLSL/LitSolid.hlsl#L19).

If TEXCOORD1 is changed to TEXCOORD0, it will successfully paint the object, but the result is apparently is not proper AO.
[/quote]
Just to be clear - it's not this line causing error, it's wrong model, but this solution should work  just fine. I would also suggest using <a href="https://earthobservatory.nasa.gov/features/NightLights"> different AO texture </a>, to make it look better (I've used default sphere and shader modified same way as You did):
![Screenshot_Tue_Feb__5_02_51_03_2019|690x356](upload://tJUihMWVJ5Hr1I0DuSGZuqnJHC8.jpeg) 

[quote="I3DB, post:26, topic:4810"]
It would be great if all the samples just worked on all the platforms.
[/quote]
Wrong forum for this part. Maybe You should create issue on github/forum dedicated to urhosharp?

-------------------------

I3DB | 2019-02-05 17:33:03 UTC | #28

[quote="lezak, post:27, topic:4810"]
I would also suggest using [ different AO texture ](https://earthobservatory.nasa.gov/features/NightLights),
[/quote]

Not sure which texture you were referring to? I usually get them [from here](https://visibleearth.nasa.gov/view_cat.php?categoryID=1484).

-------------------------

I3DB | 2019-02-05 21:41:11 UTC | #29

Got the customshader sample running, in case anyone is interested.

![PNG|544x500](upload://pBBLHQNdQRgeXnUNItLXi8By6Qa.jpeg) 

The HLSL shader code is:
```
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"

void VS(float4 iPos : POSITION,
	float3 iNormal : NORMAL,
	float4 iTangent : TANGENT,
	float2 iTexCoord : TEXCOORD0,
	out float2 oTexCoord : TEXCOORD0,
	out float3 oNormal : TEXCOORD1,
	out float4 oWorldPos : TEXCOORD2,
	out float4 oTangent : TEXCOORD3,
	out float4 oEyeVec : TEXCOORD4,
	out float4 oScreenPos : TEXCOORD5,
	out float4 oPos : OUTPOSITION)
{
	float3 worldPos = GetWorldPos(iModelMatrix);
	oPos = GetClipPos(worldPos);
	oNormal = GetWorldNormal(iModelMatrix);
	oWorldPos = float4(worldPos, GetDepth(oPos));
	float3 tangent = GetWorldTangent(iModelMatrix);
	float3 bitangent = cross(tangent, oNormal) * iTangent.w;
	oTexCoord = float4(GetTexCoord(iTexCoord), bitangent.xy);
	oEyeVec = float4(cCameraPos - worldPos, GetDepth(oPos));
}

void PS(
	float4 iTexCoord : TEXCOORD0,
	float3 iNormal : TEXCOORD1,
	float4 iWorldPos : TEXCOORD2,
	float4 iTangent : TEXCOORD3,
	float4 iEyeVec : TEXCOORD4,
	float4 iScreenPos : TEXCOORD5,
	out float4 oColor : OUTCOLOR0)
{
	float f = dot(normalize(iEyeVec.xyz), normalize(iNormal));
	oColor = float4(1,1,1,1-f);
}
```

First shader I've ever written. But it was mostly cut and paste.

There is something interesting in the rewrite. 

The technique defines NOUV, which acts in the other shaders  to make iTexCoord a float2. But when I left it this way, the shader didn't work. So I stipped out the float2 definition, and left it as a float4, and then in the VS part,  also calculated as a float4 as shown. Otherwise, it would have been just (GetTexCoord(iTexCoord)).

-------------------------

I3DB | 2019-02-05 22:02:49 UTC | #30

The last issue in that sample is the NoTextureMultiply doesn't work.

This is the error generated:
ERROR: Failed to create blend state (HRESULT 80070057)

The hresult decodes as: E_INVALIDARG	One or more arguments are not valid

Not sure what this could be. The only way this particular sample varies from the NoTextureAdd sample is in the technique file:

NoTextureAdd.xml
```
<technique vs="Unlit" ps="Unlit" vsdefines="NOUV" >
    <pass name="alpha" depthwrite="false" blend="add" />
</technique>
```

And NoTextureMultiply:
```
<technique vs="Unlit" ps="Unlit" vsdefines="NOUV" >
  <pass name="alpha" depthwrite="false" blend="multiply" />
</technique>
```

Not sure how to approach this to solve it. Tried re-writing the shader, as per the CustomShader rewrite described above (by setting the iTexCoord to a float4).

So the blend state alpha pass of multiply doesn't work, but add works.

Can anyone offer a clue how to solve or find more info?

edit: also, if a new material for DiffMultiply is added, using the technique DiffMlutiply.xml, the same error is emitted.

-------------------------

I3DB | 2019-02-12 17:10:53 UTC | #31

[quote="I3DB, post:29, topic:4810"]
The HLSL shader code is:
[/quote]

That shader doesn't quite work correctly. Viewed through a stereoscopic display (such as hololens), each of the lenses gets a slightly different output depending on orientation. Moving left to right across the object highlights the issue. 

Still researching, and[found this resource](https://github.com/reattiva/Urho3D-Blender/blob/master/guide.txt) which has a lot of info, but[explains uv maps](https://github.com/reattiva/Urho3D-Blender/blob/8a95ce7a8e7b8488e0b164762d050b1f95b318fd/guide.txt#L186) and materials from urho3d's viewpoint. The [sections on UV](https://github.com/reattiva/Urho3D-Blender/blob/8a95ce7a8e7b8488e0b164762d050b1f95b318fd/guide.txt#L78) and [on Materials](https://github.com/reattiva/Urho3D-Blender/blob/8a95ce7a8e7b8488e0b164762d050b1f95b318fd/guide.txt#L240) explain it well.

-------------------------

