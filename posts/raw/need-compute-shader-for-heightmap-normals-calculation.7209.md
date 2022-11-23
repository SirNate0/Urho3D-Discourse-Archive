najak3d | 2022-02-26 04:54:40 UTC | #1

Currently we do all of this on the CPU.   Our GPS app screen is about 1500 x 2000 pixels, and filled with Elevation map data (heightmap transferred to a GrayScale 16bit Texture).

What we do on the CPU is a quite expensive calculation of Normals, so that we can do adequate shading, for a Relief map (see image below).  This is the MOST EXPENSIVE thing we do currently, and is causing hiccups as you pan the map (up 0.1 sec worst case on Android).

We'd like to push these calculations onto the GPU, via a "Compute Shader", which seems to not be supported by Urho3D, currently.

![image|662x428](upload://yJkdKFElTaCISwKlQG9fGQLmRnW.jpeg)

I think we might be able to do this without Compute Shaders if we could do one specific operation using regular Shaders:
1. Create offscreen scene, with Orthographic Camera.
2. In this scene, place a plane that fills the full screen, and is covered by the HeighMap texture (16bpp grayscale).
3. Then use RTT to render to a new texture, same size as the HeightMap.  Matched 1:1.
4. The Vertex Shader outputs varying XY texture position coords (varies per pixel).
5. Pixel Shader Samples the Height Map texture surrounding pixels to calculate the local Slope/Normal, and outputs this into the RTT target, 1:1 pixel matching the HeightMap.
6.  DONE.   Now we can use this RTT target Normals Texture as Input to our TerrainShader.
(We already do #(6), with a Normals Texture generated on our CPU.)

Has anyone else tried anything like this?   Does this seem like a viable approach?  (or am I missing something?)

NOTE: Our Heightmap database is currently 0.5 GB, and the largest DB we have.  If we added Normals to this DB, it would double it's size, which is not a viable option.

Use of a Compute shader technique is the best solution, by far.

-------------------------

Nerrik | 2022-02-26 10:05:48 UTC | #2

[quote="najak3d, post:1, topic:7209"]
ghtmap transferred to a GrayScale 16bit Texture).

What we do on the CPU is a quite expensive calculation of Normals, so that we can do adequate shading, for a Relief map (see image below). This is the MOST EXPENSIVE thing we do currently, and is causing hiccups as you pan the map (up 0.1 sec worst case on Android).

We’d like to push these calculations onto the GPU, via a “Compute Shader”, which seems to not be supported by Urho3D, currently.
[/quote]

here some code snippets from my terrain shader that calculate normal / tangets in the Vertexshader

It's some kind of "dirty" and is still being revised. 

textureLod doesnt work for me under directx9 at Urho3D (only dx11 and opengl), I didn't bother with that any further yet but there are alternatives for.

```
vec3 calculateNormal(vec3 p1, vec2 TexCoord) {
	float delta = 0.5;
	float texturestep = 1.0 / 512.0; // size of texture
	
	vec4 sample1=textureLod(sWeightMap0, vec2(TexCoord.x + texturestep,TexCoord.y),0);
	float p2h = (sample1.r + sample1.g / 100.0) * cTerrainScale;
	
	vec4 sample2=textureLod(sWeightMap0, vec2(TexCoord.x,TexCoord.y - texturestep),0);
	float p3h = (sample2.r + sample2.g / 100.0) * cTerrainScale;
	
	vec3 p2 = (p1 + vec3(delta, 0.0f, 0.0f)) * vec3(1.0f, 0.0f, 1.0f);
	vec3 p3 = (p1 + vec3(0.0f, 0.0f, -delta)) * vec3(1.0f, 0.0f, 1.0f);

	p2.y = p2h;
	p3.y = p3h;

	vec3 u = p2 - p1;
	vec3 v = p3 - p1;

	vec3 normal = vec3(0.0f);
	normal.x = (u.y * v.z) - (u.z * v.y);
	normal.y = (u.z * v.x) - (u.x * v.z);
	normal.z = (u.x * v.y) - (u.y * v.x);

	return normalize(normal);
}



vec3 calculateTan(vec3 norm) {
	vec3 tangent;


	vec3 c1 = cross(norm, vec3(0.0f, 0.0f, 1.0f));
	vec3 c2 = cross(norm, vec3(0.0f, 1.0f, 0.0f));

	if (length(c1) > length(c2))
	{
		tangent = c1;
	}
	else
	{
		tangent = c2;
	}

	tangent = normalize(tangent);

	return tangent;
}

VS: 

vec4 wm=textureLod(sWeightMap0, iTexCoord,0); //heightmap
float hadd=wm.r + wm.g/100.0;
float height=hadd*cTerrainScale;
vec3 worldPos = GetWorldPos(modelMatrix);
worldPos.y+=height;
......
#ifdef NORMALMAP
vec3 mNormal=calculateNormal(worldPos, iTexCoord);
vNormal = normalize(mNormal * GetNormalMatrix(modelMatrix));
#else
vNormal = GetWorldNormal(modelMatrix);
#endif
......

#ifdef NORMALMAP
vec3 mtangent = calculateTan(mNormal);
vec4 tangent = vec4(normalize(mtangent.xyz * GetNormalMatrix(modelMatrix)), 1.0);
vec3 bitangent = cross(tangent.xyz, vNormal) * 0.5;
vTexCoord = vec4(GetTexCoord(iTexCoord), bitangent.xy);
vTangent = vec4(tangent.xyz, bitangent.z);
#else
vTexCoord = GetTexCoord(iTexCoord);
#endif


PS:

    #ifdef NORMALMAP
    mat3 tbn = mat3(vTangent.xyz, vec3(vTexCoord.zw, vTangent.w), vNormal);
	
    vec3 normal = normalize(tbn * DecodeNormal(texture2D(sDetailMap1, vTexCoord.xy)));
....
```
as model iam using a flat plane grid

edit: my heightmap is also some special, so you maybe have to change some calcs, let me know if you need help

also let me know if you have suggestions for a improvement. ;)

-------------------------

najak3d | 2022-02-26 13:01:35 UTC | #3

Nerrik, thank you for your answer.  This looks similar to what we're doing now in C# on the CPU now.

Is this a regular Terrain shader, which re-executes all of this logic "per render frame" for the terrain?  Or have you found a way to output this result to another Texture in the GPU, which then can be re-used by a Terrain shader which no-longer needs to recalculate these normals each frame (as it uses this shader-generated Normals Texture).

Our app is designed for mobile devices, and so we're trying hard to maintain "no hiccups" while at same time minimizing the power-usage (which goes up as you pound the CPU/GPU with extra work).  Therefore, we're really interested an optimization that would avoid these rather expensive per-vertex calculations every frame.

Has anyone else used Urho3D Shaders to do something like this?   I'm just not positive about the best way to essentially do this 1:1 translation between HeightMap Texture to NormalMap texture.

-------------------------

Nerrik | 2022-02-26 13:41:07 UTC | #4

hi, it reexecute this logic every frame / vertex. In my case the HM changes often because its only a cutted part of a very bigger hm so it does not bother me and on PC it is not a "noticeable calculation". 

I also experimented with https://github.com/eugeneko/Urho3D/commits/GeometryShaders and implemented it into the current branch for a grass geometry / vegetation shader. It worked but i discarded it because of some problems with the shader defines(in the geometry PS). As I remember there was also an compute shader support included.

-------------------------

JTippetts1 | 2022-03-01 15:37:45 UTC | #5

You should be able to do this pretty much the way you describe. Create a custom shader, draw a full-screen quad, render to a texture then you can save the texture data as an image when finished.

You can sample from your input heightmap texture in the vertex shader to do the normal computation right there. In GLSL you can use `textureSize(sampler, lod)` to get the size of a texture and `texelFetch(sampler, ivec2, lod)` to get a pixel at a specified coordinate. Using texelFetch it is trivial to write a vertex shader that samples the top/right/bottom/left adjacent pixels and calculates a normal, which can be passed in a varying to the pixel shader to convert it to a color and draw the fragment. In HLSL, I believe the equivalent functions are `GetDimensions()` and `Load()` but I'm not 100% sure about that. If you draw a unit size quad in the scene, you can multiply the input coordinate position by textureSize to obtain a pixel coordinate, then perform your normal calculation.

My house is in your example map image btw.

-------------------------

najak3d | 2022-03-01 18:26:36 UTC | #6

Thank you very much for the advice!  I'll give this a shot.

-------------------------

JSandusky | 2022-03-06 05:00:43 UTC | #7

If you want to smash in compute yourself you can refer to my pull for RBFX [https://github.com/rbfx/rbfx/pull/203](https://github.com/rbfx/rbfx/pull/203). If you don't have any complicated requirements it's not hard to plug in compute for GL as it you don't have to fuss with UAVs. Things only start to get crazy when you need to deal with structured buffers.

Unsure if there's any GLES specific issues though, I only wrote for desktop GL.

-------------------------

najak3d | 2022-03-06 06:46:04 UTC | #8

For the project where we are needing this, we're currently stuck on UrhoSharp, which builds off Urho3D from 2019, and we don't have the option to change anything.   UrhoSharp appears currently unbuildable and unmaintainable even by @Egorbo  who wrote it.   It's dormant and dying, from what I can tell.

We can't use Urho.NET yet for that project, because it doesn't support Xamarin Forms.

So we're stuck with vanilla Urho3D from 2019 for this project.  Our needs are relatively easy, so it seems to be working for us well enough.   I'm hoping I can get this kludge technique using Ortho Camera to work well enough.   It doesn't need to be elegant, it just needs to work, so that we can stop doing this heavy computing on the CPU, which is causing hiccups, or lag.

-------------------------

Nerrik | 2022-03-09 10:59:07 UTC | #9

Just a theoretical thought,

I would try to use a blank transparent rgba texture/image for the normaldata, and sample it in the vertexshader.

If the sample is blank (alpha=0) using my calculateNormal function and write the result into the texture/image with [imageStore](https://www.khronos.org/registry/OpenGL-Refpages/es3.1/html/imageStore.xhtml)  with vec4(normal.x, normal.y, normal.z, 1.0f) at the pixel-uvposition. 

So it have to do this caluclation only in the first frame.

edit: never used imageStore in the vertexshader with urho3d, so its just  theoretical because of https://www.khronos.org/opengl/wiki/Memory_Model#Incoherent_memory_access and the binding, you maybe have to implement this for your self also.

-------------------------

najak3d | 2022-03-09 15:37:28 UTC | #10

In short, are you suggesting that we can then do it with one-shader?  And so when the first vertex comes in and samples "0" is found, then we sample the ENTIRE source texture and create the entire normal map all from this first vertex sample?   If not, then I'm not understanding your proposal.

-------------------------

SirNate0 | 2022-03-09 16:05:00 UTC | #11

I think that is the suggestion. I wouldn't recommend it, though, as it would incur a small performance penalty every frame for the conditional verses the single cost at the start and the additional complexity in the c++ code to set up the initial run that occurs only once.

-------------------------

najak3d | 2022-03-09 16:39:17 UTC | #12

My other concern is that there is no such thing as "first vertex", because the first batch of vertices will come in unison, and in unison, they'll all be trying to create this Normal Map.

The original idea also permits the normal map to be produced using the parallel cores with 100% efficiency, rather than putting all of that load onto a single GPU core (would be essentially single-threaded for normals processing).

When I get time to do this, I'm going to attempt the solution from @JTippetts1 .

-------------------------

Nerrik | 2022-03-09 23:24:05 UTC | #13

I mean to write the calculated normal permanent into the textureimage if the normal is missed at this textureposition (blank) **one time** with imageStore. So u dont need a compute shader for the normaltexture to create.

something like 

Pseudocode:
```
vec4 hm_data = textureLod(hm_data_image, vec2(TexCoord.x,TexCoord.y),0); // imageLoad(hm_data_image...) in this case;

if (hm_data.a==0)
{
vec3 new_normal = calculateNormal(worldPos, iTexCoord);
hm_data = vec4(new_normal , 1.0f);
ivec2 coord=ivec2(iTexCoord.x * texturesize, iTexCoord.y * texturesize);
imageStore( hm_data_image, coord, hm_data ); 
}

```
So each Vertexcall create its own "normaldata pixel" permanent if its not happend yet (blank), what happens only in the first call - after that it uses the pixeldata from the texture without any further calculations.

But i have looked into OGLGraphics and Urho3d dont do glBindImageTexture calls so there is no support for image2D. 

So you have to extend it :/

It was just an untestet fast Idea ;)

-------------------------

najak3d | 2022-03-10 00:07:52 UTC | #14

I appreciate the brainstorm.    I think for our situation this too won't work great, because need normals for the Pixel Shader, not Vertex Shader.   So between two vertices, our Pixel Shader will sample many many normals (potentially, depending upon how close camera is to the geometry).

I think @JTippetts1  approach might still be our best option.

-------------------------

