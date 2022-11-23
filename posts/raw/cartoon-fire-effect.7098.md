SirNate0 | 2021-12-10 04:08:49 UTC | #1

Hello, I am looking to achieve a nice looking cartoon fire effect. Similar to what was done in this video for the flame on Charizard.

https://youtu.be/bykTkjPfKsw

I believe I could implement that effect in Urho by using the stencil buffer - does anyone have any tips/code for how that can be done? Or any suggestions about how else a similar quality effect could be achieved? It doesn't need to be super realistic, it just has to be fairly performant (e.g. 50000 particles for one fire is a no) and it should look nice on more than just a black background (a lot of particle fire effects seem to rely on having a dark background).

My other thought for the above effect is that it might be possible to not use the stencil buffer and just add a second UV map to the fire core to get the yellow coloration, though I've not looked into the details of how that might work yet.

-------------------------

Modanung | 2021-12-10 12:29:25 UTC | #2

You could also read the same texture twice, once with UVs shifted and treat green as yellow. Then maybe tone down the yellow based on the fragment's normal.
In short: Write a shader.

-------------------------

Modanung | 2021-12-10 13:00:07 UTC | #3

A texture to experiment with:

![Plasma|500x500](upload://7B8fWhrJDywOs0DYeffk7RFqaG0.png)

Hereby CC0'd.

-------------------------

Modanung | 2021-12-10 16:31:12 UTC | #4

https://luckeyproductions.nl/videos/fire2.mp4

Using `cElapsedTimePS` to offset the UVs per channel and a Fresnel factor to tone it down.

-------------------------

GodMan | 2021-12-10 16:49:37 UTC | #5

I agree with @Modanung. This can be easily done with a shader.

-------------------------

SirNate0 | 2021-12-12 02:49:51 UTC | #6

Not exactly what the original was, but I think I'm liking it.
![FX-Flame|116x156](upload://qxWTrLzkltsa6ZLP7h6AzafHq6f.gif)

The shader, if anyone wants it (it's basically just Unlit.glsl)
```
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Fog.glsl"

// Based on Unlit.glsl

varying vec2 vTexCoord;
varying vec4 vWorldPos;
#ifdef VERTEXCOLOR
    varying vec4 vColor;
#endif
varying float vHeight;
varying vec3 vNormal; // So we can only change the color towards the edge of the model
varying float vNdotV; // Camera to world pos
varying float vNdotY;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = GetTexCoord(iTexCoord);
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));
    vNormal = GetWorldNormal(modelMatrix);
	vec3 cameraDir = normalize(worldPos - cCameraPos);
	vNdotV = dot(cameraDir,normalize(vNormal));
	vNdotY = vNormal.y;


    #ifdef VERTEXCOLOR
        vColor = iColor;
    #endif
    
    vHeight = iPos.y;

}

void PS()
{
    // Get material diffuse albedo
    #ifdef DIFFMAP
		#ifdef SHELL
			float h = cElapsedTimePS;
		#else
			float h = 0;
		#endif
        vec4 diffColor = cMatDiffColor * //texture2D(sDiffMap, vTexCoord + vec2(0,2.5*cElapsedTimePS));
				min(texture2D(sDiffMap, vTexCoord + vec2(h,2.5*cElapsedTimePS)) + texture2D(sSpecMap, vTexCoord + vec2(1.3*h,3*cElapsedTimePS)),vec4(1.0,1.0,1.0,1.0));
        #ifdef ALPHAMASK
            if (diffColor.a < 0.5)
                discard;
        #endif
        #ifdef REDMASK
            if (diffColor.r < 0.9) // With 0.5 we get some dark lines at the edges of the flame threads
                discard;
        #endif
    #else
        vec4 diffColor = cMatDiffColor;
    #endif
    
	vec3 normal = normalize(vNormal);
    
    diffColor.g += vHeight*10;
    #ifdef SHELL
		diffColor.g = 0.9*pow(1 - pow(vNdotV,2),0.9);
    #else
		diffColor.g = mix(0.7,1.0,vNdotY)*pow(1 - vTexCoord.x*pow(vNdotV,2),0.9);
    #endif
//     diffColor.g = pow(1 - vTexCoord.x*abs(vNdotV),1);
    diffColor.b = 0;//abs(vNdotV); //normal.z;
//     diffColor.rgb = abs(vec3(vNdotV,0,max(vNdotY,0)));//0.5-0.5*normal;

    #ifdef VERTEXCOLOR
        diffColor *= vColor;
    #endif

    // Get fog factor
    #ifdef HEIGHTFOG
        float fogFactor = GetHeightFogFactor(vWorldPos.w, vWorldPos.y);
    #else
        float fogFactor = GetFogFactor(vWorldPos.w);
    #endif

    #if defined(PREPASS)
        // Fill light pre-pass G-Buffer
        gl_FragData[0] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[1] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #elif defined(DEFERRED)
        gl_FragData[0] = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        gl_FragData[1] = vec4(0.0, 0.0, 0.0, 0.0);
        gl_FragData[2] = vec4(0.5, 0.5, 0.5, 1.0);
        gl_FragData[3] = vec4(EncodeDepth(vWorldPos.w), 0.0);
    #else
        gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
    #endif
}
```

-------------------------

