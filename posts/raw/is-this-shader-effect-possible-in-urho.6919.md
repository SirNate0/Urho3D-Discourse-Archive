shifttab | 2021-07-14 09:20:03 UTC | #1

I'm trying to recreate this [fluffy foliage](https://www.youtube.com/watch?v=iASMFba7GeI) shader. Is this possible to do in urho?

The effect doesn't seem to be that complicated and his node tree is fairly small but I just suck at shaders in general :p 

I'm already stuck in the beginning. This is what I tried:


```
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Fog.glsl"

varying vec2 vTexCoord;
varying vec4 vWorldPos;
#ifdef VERTEXCOLOR
    varying vec4 vColor;
#endif
#
varying vec4 vUVColor;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = ((iPos + vec4(iTexCoord, 0, 0))  * modelMatrix).xyz;
    gl_Position = GetClipPos(worldPos);
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));

    vUVColor = vec4(iTexCoord, 0.0, 1.0);
}

void PS()
{
    vec4 diffColor = vUVColor;

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

![Image|690x323](upload://kFRXp87AWD7H3yleu4wHZQ3MLCy.png)


It's a round mesh but I'm confused because it is visible from the back but not from the front when I transform the vertices and it looks all wrong.

-------------------------

SirNate0 | 2021-07-14 14:39:29 UTC | #2

I suspect the model is only visible from one side because of the culling of the triangles (CW or CCW). You don't yet have the quads facing the camera, I'm pretty sure, so I would expect the faces to be culled when they are facing the wrong way. What are you thinking looks wrong with it? It looks similar to the intermediate results in the video to me.

-------------------------

WangKai | 2021-07-16 03:08:46 UTC | #3

I suggest you check the debug/console output. And you can use RenderDoc to validate the pipeline - 
https://renderdoc.org/

-------------------------

SirNate0 | 2021-07-22 15:50:21 UTC | #4

@shifttab will you be sharing the completed port to Urho when you're finished? It's fine either way, I just want to know if I should try porting it myself.

-------------------------

shifttab | 2021-07-24 11:21:17 UTC | #5

I can't make it look the camera so I ditched it. I'm too noob for it. :confused:

-------------------------

SirNate0 | 2021-07-27 00:25:30 UTC | #6

Got it working! Will post a better version of the code later, but for now, the key is basically just adding this displacement to the world position of the LitSolid shader and enabling ALPHAMASK. Note that I cycle through different scales for the displacment so you can see what works for you (between 0 and 1).

```

    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
  
    // displacement from the UV coordinate
    vec3 displacement = vec3(iTexCoord.y,iTexCoord.x,0)*2-1;
	displacement = (vec4(displacement,0) * cViewInv).xyz * fract(cElapsedTime*0.1);  
    
    // add displacement to the world position
    gl_Position = GetClipPos(worldPos + displacement);
```

**Bush after displacment**
![image|379x251](upload://sllDaWvuCAAlqHceDpGYq7jaNHW.png)

**Bush with almost no displacement or alpha masking**
![image|188x102](upload://kJybpsrDCmjphTfuC246nI0jC6W.png)

**Bush in Blender** (orientation and scale may differ)
![image|393x216](upload://cFIa6WlvC1P56Ck18ldUB1PIiKQ.png)

---

**Update 1:**
Threw it on a large mesh I had that had suitable UV coordinates, though often backwards normals, and even with around 1 million triangles in a model using it I'm getting ~120 FPS, down from 200 FPS with just the bush. Note that this is with a second viewport, though the model isn't visible in it.
![image|665x500](upload://17ce8BnR5QghNBTa1nlzRpC41GY.jpeg)

-------------------------

