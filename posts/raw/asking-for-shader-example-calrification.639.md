ghidra | 2017-01-02 01:01:49 UTC | #1

I am following this thread:
[topic393.html](http://discourse.urho3d.io/t/solved-various-questions-about-shaders/400/1)
(Various questions about shaders)

It's quite helpful.
But now I have my own questions.

I am literally just copying thier example. Where i find my self stuck, is the actual glsl shader.
The given code, is missing a little bit. I got it semi-working, but just adding that to the PS part of the terrain, shader, while leaving everything.
But that doesnt mean i understand it.

I tried to trim it way down, since i assume it is only doing one task

glsl:
[code]#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"

varying vec2 vTexCoord;
varying vec4 vWorldPos;

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vTexCoord = vec3(GetTexCoord(iTexCoord), GetDepth(gl_Position));
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));
}

void PS()
{
    float cx = mod(vWorldPos.x,10);
    float cz = mod(vWorldPos.z,10);
    float e = 0.5;

    if(!((cx > 10.0-e && cx < 10.0+e) || (cz > 10.0-e && cz < 10.0+e)) ) {//inside a square
      float dist = max(abs(cx-5.0), abs(cz-5.0)) / 10.0;
      if(dist > 0.8) dist * 0.5;
      gl_FragColor = vec4(0.0, 0.0, 0.0, dist);
    }else{ //outside a square
      gl_FragColor = normalize(vec4(1.0, 1.0, 1.0, 0.0));
    }
}[/code]

material xml:
[code]<material>
    <technique name="Techniques/TerrainBlend_B.xml" />
</material>[/code]

The errors i get the most are:
"unexpected NEW_IDENTIFIER, expecting $end" or
"unexpected '}', expecting $end"

Just guessing, in all the shaders i notice a lot of ifthen blocks, but i have no idea what that is doing really
[code]  #ifdef PERPIXEL
        #ifdef SHADOW
            ...
        #endif
        #ifdef SPOTLIGHT
           ...
        #endif
    
        #ifdef POINTLIGHT
           ...
        #endif
    #else
        #if defined(LIGHTMAP) || defined(AO)
             ...
        #else
            ...
        #endif     
        #ifdef NUMVERTEXLIGHTS
           ...
        #endif
        #ifdef ENVCUBEMAP
           ...
        #endif
    #endif[/code]
They dont seem to correlate to the technique or the material or render paths xmls.
Thanks everyone.

-------------------------

ghidra | 2017-01-02 01:01:49 UTC | #2

I am setting it up as a basic scene in the editor.
And its not throwing specific line errors. in the editors console and the terminal console i get this exactly:

[code]ERROR: Failed to compile vertex shader TerrainBlend_B():
0:274(2): error: syntax error, unexpected NEW_IDENTIFIER, expecting $end[/code]

I will try to set up a basic example in angelscript to see if i get something more specific.

-------------------------

Mike | 2017-01-02 01:01:49 UTC | #3

The "ifdef" are used by techniques (psdefines) to customize the generic shader.

-------------------------

ghidra | 2017-01-02 01:01:51 UTC | #4

made a fast and dirty scene to test it out, outside the editor, and I am getting the same error, no more info than that.
I know its very vague, the current issue. I'm just not entirely sure where to start debugging it.

-------------------------

reattiva | 2017-01-02 01:01:59 UTC | #5

To pinpoint the error you can use the #line directive [url]https://www.opengl.org/wiki/Core_Language_%28GLSL%29#.23line_directive[/url].
Open the shader in an editor with line numbers, after the #includes add the #line directive specifying its line number. In your case:
[code]4  #include "ScreenPos.glsl"
5
6  #line 6
7
8  varying vec2 vTexCoord;[/code]
Now when you see an error like: "0(NNN) : error ...", the error is at line NNN (the zero is the file index, you can use it like "#line 6 3" where 3 is the file index).
Unfortunately, how this is implemented depends on the vendor, so it could not work. 
Anyway, I could compile the shader above without errors.

-------------------------

