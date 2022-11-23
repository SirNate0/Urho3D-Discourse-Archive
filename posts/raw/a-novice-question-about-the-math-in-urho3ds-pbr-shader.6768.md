Elfstone | 2021-03-26 04:05:34 UTC | #1

I was/am struggling to understand the math, and I just read this https://seblagarde.wordpress.com/2012/01/08/pi-or-not-to-pi-in-game-lighting-equation/ to get some idea of whether or not there should be a PI in the calculation.

Now, from what I understand, generally the lightColor's unit in a game is defined in the way so that outColor =  PI * BRDF * materialDiffuse * lightColor * NdotL, which in turn makes the Lambertian diffuse as simple as outColor = materialDiffuse * NdotL * lightColor. Or if the lightColor represents the actual intensity, the equation would be materialDiffuse * NdotL * lightColor / PI.

But while reading Urho3D's shader, I found that its Lambertian term seemingly strangely is divided by PI twice!

See in PBRLitSolid.hlsl: void PS(...)
finalColor.rgb = BRDF * lightColor * (atten * shadow) / M_PI;

and in BRDF.hlsl: LambertianDiffuse(...)
return diffuseColor * (1.0 / M_PI) ;

also in BRDF.hlsl: CustomLambertianDiffuse(...)
return diffuseColor * (1.0 / M_PI) * pow(NdotV, 0.5 + 0.3 * roughness)

How come "/ M_PI" is done twice?
Let's forget the Lambertian term, why is the finalColor BRDF * lightColor / M_PI in the first place?
Should it be "* M_PI" instead?

Excuse me for being a total amateur in CG, but please somebody tell me where did I miss. Or if Urho3D is using some other rendering scheme, could you explain, or is it documented somewhere?

Thanks in advance!

-------------------------

Eugene | 2021-03-26 05:59:19 UTC | #2

As a person who recently worked with PBR in Urho...
I don’t trust anything in Urho PBR shaders and I rewrote them from scratch. There are many weird or wrong places, and I don’t feel like trying to find reason behind it.

If you want to understand maths of PBR, read Filament docs, not Urho shaders.

-------------------------

JSandusky | 2021-03-26 06:11:24 UTC | #3

The PBR shaders are a kitchen sink hell problem. You can toggle this or that and there's then this way or that way things play out (pretty sure Lambert divide is independent of specular and final contribution though). That leads to a lot of redundant math and as in this case, repeated math in the shaders where a more forceful "*you will do it this way*" approach would do things more simply (or at least clearly).

TL;DR the PBR shaders suck and it's partially my fault. Don't trust the shaders.

-------------------------

Elfstone | 2021-03-26 06:18:20 UTC | #4

That's a bit disappointing.
I'll try Filament next. Thanks!

-------------------------

Elfstone | 2021-03-26 06:46:04 UTC | #5

GetBRDF does call Diffuse:
    float3 Diffuse(float3 diffuseColor, float roughness, float NdotV, float NdotL, float VdotH)
    {
        //return LambertianDiffuse(diffuseColor);
        return CustomLambertianDiffuse(diffuseColor, NdotV, roughness);
        //return BurleyDiffuse(diffuseColor, roughness, NdotV, NdotL, VdotH);
    }.
Then it returns diffuseFactor + specularFactor. 
Then the result BRDF gets divided by M_PI again, and as I have said, this line alone is difficult for me to understand:
finalColor.rgb = BRDF * lightColor * (atten * shadow) / M_PI;

-------------------------

Eugene | 2021-03-26 07:02:18 UTC | #6

In case you are curious, this is as close to "Filament shaders in Urho" as we will ever get:
https://github.com/rokups/rbfx/blob/ek/renderer/master/bin/CoreData/Shaders/GLSL/v2/_BRDF.glsl

-------------------------

Elfstone | 2021-03-26 07:57:50 UTC | #8

It looks great!
I wasn’t sure if I understood the equations correctly. Your version seems to have nothing against my understanding.
I guess the devs didn’t agree on where to do the division, thus resulted in an extra one.

-------------------------

WangKai | 2021-03-26 16:44:52 UTC | #9

Correctness comes first. It seems to me PBR should be reworked for Urho.

-------------------------

JSandusky | 2021-03-29 03:31:34 UTC | #10

That one isn't me. I'm not related to the CustomLambertian, I know nothing about it or the reasoning behind it so I have no comment on what it should or shouldn't be doing.

Presently I do Destiny 1 style LUT shading and only target VR so much of this PBR nonsense has exited my brain as pointless, I now do Doom 3 style low-tech tricks and care more about translucent shadowmaps than anyone else.

-------------------------

Elfstone | 2021-03-29 12:50:38 UTC | #12

I had no clue at first, but now I believe somebody tried to extract the common divisor M_PI, from diffuse and specular, but it ended up repeated in multiple places somehow.

PBR.hlsl: GetBRDF(…)
`specularFactor = distTerm * visTerm * fresnelTerm * ndl/ M_PI;`
See, this “M_PI” is extracted from distTerm.

Hopefully someone can check and fix it if it’s indeed wrong.

-------------------------

