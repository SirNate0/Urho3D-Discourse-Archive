dragonCASTjosh | 2017-01-02 01:10:14 UTC | #1

After working on PBR for a while i noticed so major performance problems, initially i assumed it to be part of how i was implementing IBL but after checking the implementation with other engines i found that it is not a problem with the the technique. I came to the conclusion it is either an issue with Urho3D's or i was implementing it into the wrong area of the shader for the desired affect. Any help with the problem would greatly. 

Entry to the IBL is at the bottom of the code
Lighting.hlsl
[code]        float radicalInverse_VdC(uint bits)
		{
			bits = (bits << 16u) | (bits >> 16u);
			bits = ((bits & 0x55555555u) << 1u) | ((bits & 0xAAAAAAAAu) >> 1u);
			bits = ((bits & 0x33333333u) << 2u) | ((bits & 0xCCCCCCCCu) >> 2u);
			bits = ((bits & 0x0F0F0F0Fu) << 4u) | ((bits & 0xF0F0F0F0u) >> 4u);
			bits = ((bits & 0x00FF00FFu) << 8u) | ((bits & 0xFF00FF00u) >> 8u);

			return float(bits) * 2.3283064365386963e-10; // / 0x100000000
		}

		float2 Hammersley(uint i, uint n)
		{
			return float2((float)i / (float)n, radicalInverse_VdC(i));
		}

		float3 ImportanceSampleGGX(float2 Xi, float Roughness, float3 N)
		{
			float a = Roughness * Roughness;
			float Phi = 2 * 3.14159 * Xi.x;
			float CosTheta = sqrt((1 - Xi.y) / (1 + (a*a - 1) * Xi.y));
			float SinTheta = sqrt(1 - CosTheta * CosTheta);
			float3 H = 0;
			H.x = SinTheta * cos(Phi);
			H.y = SinTheta * sin(Phi);
			H.z = CosTheta;

			float3 UpVector = abs(N.z) < 0.999 ? float3(0, 0, 1) : float3(1, 0, 0);
			float3 TangentX = normalize(cross(UpVector, N));
			float3 TangentY = cross(N, TangentX);
			// Tangent to world space
			return TangentX * H.x + TangentY * H.y + N * H.z;


		}

		float GGX(float nDotV, float a)
		{
			float aa = a*a;
			float oneMinusAa = 1 - aa;
			float nDotV2 = 2 * nDotV;
			float root = aa + oneMinusAa * nDotV * nDotV;
			return nDotV2 / (nDotV + sqrt(root));
		}

		float G_Smith(float a, float nDotV, float nDotL)
		{

			return GGX(nDotL, a * a) * GGX(nDotV, a * a);
		}

		float3 PrefilterEnvMap(float Roughness, float3 R)
		{
			float3 N = R;
			float3 V = R;

			float3 PrefilteredColor = 0;
			const uint NumSamples = 1;

			float TotalWeight = 0.0000001f;

			for (uint i = 0; i < NumSamples; i++)
			{
				float2 Xi = Hammersley(i * 2 + 0, NumSamples);
				float3 H = ImportanceSampleGGX(Xi, Roughness, N);
				float3 L = 2 * dot(V, H) * H - V;
				float NoL = saturate(dot(N, L));
				if (NoL > 0)
				{
					PrefilteredColor += SampleCubeLOD(ZoneCubeMap, float4(L, 0)).rgb * NoL;
					TotalWeight += NoL;
				}
			}
			return PrefilteredColor / TotalWeight;
		}

		float3 ApproximateSpecularIBL(float3 SpecularColor, float Roughness, float3 N, float3 V)
		{
		/*	float NoV = saturate(dot(N, V));*/
			float3 R = 2 * dot(V, N) * N - V;
			float3 PrefilteredColor = PrefilterEnvMap(Roughness, R);
			//float2 envBRDF = IntegrateBRDF(Roughness, NoV);
			return   PrefilteredColor * (SpecularColor);
		}[/code]

LitSolid.hlsl
[code] #elif defined(DEFERRED)
        // Fill deferred G-buffer
        float specIntensity = specColor.g;
        float specPower = cMatSpecColor.a / 255.0;

        float3 finalColor = iVertexLight * diffColor.rgb;
        #ifdef AO
           #ifdef IBL
               const float aoFactor = Sample2D(EmissiveMap, iTexCoord).r;
           #else
               // If using AO, the vertex light ambient is black, calculate occluded ambient here
               finalColor += Sample2D(EmissiveMap, iTexCoord2).rgb * cAmbientColor * diffColor.rgb;
           #endif
        #endif
        
        #if defined(PBR) && defined(IBL)
        
            const float3 toCamera = normalize(iWorldPos.xyz - cCameraPosPS);

		    const float3 reflection = normalize(reflect(toCamera, normal));
            float3 cubeColor = iVertexLight.rgb;
            float3 iblColor = ApproximateSpecularIBL( specColor, normal, -toCamera);
            
            float horizonOcclusion = 1.3;
            float horizon = saturate(1 + horizonOcclusion * dot(reflection, normal));
            horizon *= horizon;
            
            #ifdef AO
                finalColor += LinearFromSRGB(iblColor * aoFactor * horizon * cubeColor);
            #else                            
                finalColor += LinearFromSRGB(iblColor * horizon * cubeColor);
            #endif
        #endif[/code]

-------------------------

sabotage3d | 2017-01-02 01:10:14 UTC | #2

Is the problem only with DirectX as you posted only hlsl version of the shader?

-------------------------

dragonCASTjosh | 2017-01-02 01:10:14 UTC | #3

[quote="sabotage3d"]Is the problem only with DirectX as you posted only hlsl version of the shader?[/quote]
I only have the affect in DirectX at the moment

-------------------------

cadaver | 2017-01-02 01:10:15 UTC | #4

If I understand right, you're doing a sampling-heavy operation in the G-buffer pass (before lighting), so it would be done for every visible pixel of every solid object.

Both the good and the bad news is that there should be nothing Urho-specific in optimizing that. Can't help you more specifically.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:15 UTC | #5

[quote="cadaver"]If I understand right, you're doing a sampling-heavy operation in the G-buffer pass (before lighting), so it would be done for every visible pixel of every solid object.

Both the good and the bad news is that there should be nothing Urho-specific in optimizing that. Can't help you more specifically.[/quote]

you are correct about how the affect works, do you have any suggestions on better places to implement IBL within Urho's shader pipleine

-------------------------

cadaver | 2017-01-02 01:10:15 UTC | #6

If it needs material properties that are not stored into the G-buffer, then I can't see other places for it. Otherwise you could do the heavy sampling in a fullscreen quad postprocess pass, it maybe has better sampling coherency, or then maybe not.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:15 UTC | #7

[quote="cadaver"]If it needs material properties that are not stored into the G-buffer, then I can't see other places for it. Otherwise you could do the heavy sampling in a fullscreen quad postprocess pass, it maybe has better sampling coherency, or then maybe not.[/quote]

Ill see what i can do with it, id likely need to add roughness to the G-Buffer for it to work but roughness is fairly common in the G-Buffer these days

-------------------------

hdunderscore | 2017-01-02 01:10:16 UTC | #8

I believe you missed the key idea of the approach. The idea for the 'PrefilterEnvMap' and also the 'IntegrateBRDF' functions are for them to be precomputed offline. The referenced paper is ambiguous by not providing example usage of the prefiltered cubemaps, but mentions the key on this line: 
[quote][url]http://blog.selfshadow.com/publications/s2013-shading-course/karis/s2013_pbs_epic_notes_v2.pdf[/url]
We pre-calculate the first sum for different roughness values and store the results in the mip-map levels of a cubemap. This is the typical approach used by much of the game industry [1, 9].[/quote]

The citations:
[quote][1] AMD, CubeMapGen: Cubemap Filtering and Mipchain Generation Tool. [developer.amd](http://developer.amd).
com/resources/archive/archived-tools/gpu-tools-archive/cubemapgen/
[9] Hoffman, Naty, ?Background: Physics and Math of Shading?, part of ?Physically Based Shading
in Theory and Practice?, SIGGRAPH 2013 Course Notes. [blog.selfshadow.com/publications ... ng-course/](http://blog.selfshadow.com/publications/s2013-shading-course/)[/quote]

Here are tools that do a similar task:
[seblagarde.wordpress.com/2012/0 ... rendering/](https://seblagarde.wordpress.com/2012/06/10/amd-cubemapgen-for-physically-based-rendering/)
[github.com/dariomanesku/cmft](https://github.com/dariomanesku/cmft)

The slides hints at how to use the prefiltered map (page 12): [blog.selfshadow.com/publications ... slides.pdf](http://blog.selfshadow.com/publications/s2013-shading-course/karis/s2013_pbs_epic_slides.pdf)

Here is a useful post on using prefiltered cubemaps: [seblagarde.wordpress.com/2011/0 ... llo-world/](https://seblagarde.wordpress.com/2011/08/17/hello-world/)

-------------------------

dragonCASTjosh | 2017-01-02 01:10:16 UTC | #9

[quote="hd_"]I believe you missed the key idea of the approach. The idea for the 'PrefilterEnvMap' and also the 'IntegrateBRDF' functions are for them to be precomputed offline. The referenced paper is ambiguous by not providing example usage of the prefiltered cubemaps, but mentions the key on this line: 
[quote][url]http://blog.selfshadow.com/publications/s2013-shading-course/karis/s2013_pbs_epic_notes_v2.pdf[/url]
We pre-calculate the first sum for different roughness values and store the results in the mip-map levels of a cubemap. This is the typical approach used by much of the game industry [1, 9].[/quote]

The citations:
[quote][1] AMD, CubeMapGen: Cubemap Filtering and Mipchain Generation Tool. [developer.amd](http://developer.amd).
com/resources/archive/archived-tools/gpu-tools-archive/cubemapgen/
[9] Hoffman, Naty, ?Background: Physics and Math of Shading?, part of ?Physically Based Shading
in Theory and Practice?, SIGGRAPH 2013 Course Notes. [blog.selfshadow.com/publications ... ng-course/](http://blog.selfshadow.com/publications/s2013-shading-course/)[/quote]

Here are tools that do a similar task:
[seblagarde.wordpress.com/2012/0 ... rendering/](https://seblagarde.wordpress.com/2012/06/10/amd-cubemapgen-for-physically-based-rendering/)
[github.com/dariomanesku/cmft](https://github.com/dariomanesku/cmft)

The slides hints at how to use the prefiltered map (page 12): [blog.selfshadow.com/publications ... slides.pdf](http://blog.selfshadow.com/publications/s2013-shading-course/karis/s2013_pbs_epic_slides.pdf)

Here is a useful post on using prefiltered cubemaps: [seblagarde.wordpress.com/2011/0 ... llo-world/](https://seblagarde.wordpress.com/2011/08/17/hello-world/)[/quote]

I guess i did miss the point thinks for noticing, ill look into the resources you linked to see what i can do

-------------------------

boberfly | 2017-01-02 01:10:20 UTC | #10

[quote="dragonCASTjosh"][quote="cadaver"]If it needs material properties that are not stored into the G-buffer, then I can't see other places for it. Otherwise you could do the heavy sampling in a fullscreen quad postprocess pass, it maybe has better sampling coherency, or then maybe not.[/quote]

Ill see what i can do with it, id likely need to add roughness to the G-Buffer for it to work but roughness is fairly common in the G-Buffer these days[/quote]

Just to note doing heavy stuff in the g-buffer is bad because you don't have a z pre-pass like you might have with a forward renderer (z pre-pass helps performance with heavy pixel/fragment shaders as the rasterizer doesn't need to draw occluded surfaces by depth-testing against the zbuffer first), so the lighter the g-buffer is in terms of pixel/fragment shader complexity the better. It's why cadaver suggested doing the complexity in a fullscreen quad (and just read the g-buffer's data for your lighting inputs). 

The only lighting stuff I'd put in a g-buffer would be baked stuff like UV lightmaps, which need to be with the scene pass to map onto UVs.

-------------------------

