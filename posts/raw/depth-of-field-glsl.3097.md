godan | 2017-05-03 17:28:22 UTC | #1

I'm trying to implement a depth of field post processing shader. From the interwebs, I found this approach:

https://www.youtube.com/watch?v=VIl69Ik3A2k

```

#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"
#include "ScreenPos.glsl"
#include "Lighting.glsl"

varying vec2 vScreenPos;
varying vec2 vTexCoord;
varying vec2 vScreenPosFull;

#ifdef COMPILEPS

uniform float cBlurClamp;  // max blur amount
uniform float cBias; //aperture - bigger values for shallower depth of field
uniform float cFocus;  // this value comes from ReadDepth script.

#endif


void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    vScreenPos = GetScreenPosPreDiv(gl_Position);
    vTexCoord = GetQuadTexCoord(gl_Position);
    vScreenPosFull = GetScreenPos(gl_Position).xy;
}

void PS()
{

    float aspectratio = 800.0/800.0;
    vec2 aspectcorrect = vec2(1.0,aspectratio);
    aspectcorrect *= 0.1;
    
    float depth = 100.0 * DecodeDepth(texture2D(sDepthBuffer, vTexCoord).rgb);
    float factor = ( depth - cFocus );     
    vec2 dofblur = vec2 (clamp( factor * cBias, -cBlurClamp, cBlurClamp ));
    vec4 col = vec4(0.0);
    
    col += texture2D(sDiffMap, vScreenPos);
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.0,0.4 )*aspectcorrect) * dofblur);
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.15,0.37 )*aspectcorrect) * dofblur);
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.29,0.29 )*aspectcorrect) * dofblur);
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.37,0.15 )*aspectcorrect) * dofblur);    
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.4,0.0 )*aspectcorrect) * dofblur);   
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.37,-0.15 )*aspectcorrect) * dofblur);    
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.29,-0.29 )*aspectcorrect) * dofblur);    
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.15,-0.37 )*aspectcorrect) * dofblur);
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.0,-0.4 )*aspectcorrect) * dofblur);  
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.15,0.37 )*aspectcorrect) * dofblur);
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.29,0.29 )*aspectcorrect) * dofblur);
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.37,0.15 )*aspectcorrect) * dofblur); 
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.4,0.0 )*aspectcorrect) * dofblur);  
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.37,-0.15 )*aspectcorrect) * dofblur);   
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.29,-0.29 )*aspectcorrect) * dofblur);   
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.15,-0.37 )*aspectcorrect) * dofblur);
    
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.15,0.37 )*aspectcorrect) * dofblur*0.9);
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.37,0.15 )*aspectcorrect) * dofblur*0.9);        
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.37,-0.15 )*aspectcorrect) * dofblur*0.9);        
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.15,-0.37 )*aspectcorrect) * dofblur*0.9);
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.15,0.37 )*aspectcorrect) * dofblur*0.9);
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.37,0.15 )*aspectcorrect) * dofblur*0.9);     
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.37,-0.15 )*aspectcorrect) * dofblur*0.9);   
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.15,-0.37 )*aspectcorrect) * dofblur*0.9);    
    
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.29,0.29 )*aspectcorrect) * dofblur*0.7);
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.4,0.0 )*aspectcorrect) * dofblur*0.7);   
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.29,-0.29 )*aspectcorrect) * dofblur*0.7);    
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.0,-0.4 )*aspectcorrect) * dofblur*0.7);  
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.29,0.29 )*aspectcorrect) * dofblur*0.7);
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.4,0.0 )*aspectcorrect) * dofblur*0.7);  
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.29,-0.29 )*aspectcorrect) * dofblur*0.7);   
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.0,0.4 )*aspectcorrect) * dofblur*0.7);
             
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.29,0.29 )*aspectcorrect) * dofblur*0.4);
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.4,0.0 )*aspectcorrect) * dofblur*0.4);   
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.29,-0.29 )*aspectcorrect) * dofblur*0.4);    
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.0,-0.4 )*aspectcorrect) * dofblur*0.4);  
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.29,0.29 )*aspectcorrect) * dofblur*0.4);
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.4,0.0 )*aspectcorrect) * dofblur*0.4);  
    col += texture2D(sDiffMap, vScreenPos + (vec2( -0.29,-0.29 )*aspectcorrect) * dofblur*0.4);   
    col += texture2D(sDiffMap, vScreenPos + (vec2( 0.0,0.4 )*aspectcorrect) * dofblur*0.4);   
            
    gl_FragColor = col/41.0;
    gl_FragColor.a = 1.0;
}

```

It works ok, but I'm not sure I like how distinct the overlays are (i.e. its not blurry enough...). Anyone have any experience with this type of shader?

Also, I'm pretty sure I can get the current viewport dimensions in the fragment shader, but can't remember how. Is int ScreenPos()?

-------------------------

Victor | 2017-05-03 19:23:07 UTC | #2

Sorry I don't have an answer for you, but you just made me realize a very good and beneficial use for IOGRAM. For a while now I've been trying to figure out the best use-case for my project, and doing shaders is definitely the best case to make this part of my workflow. Thanks so much godan for your product!

**edit**: I'm not sure why it took me so long to realize this...

-------------------------

johnnycable | 2017-05-03 22:27:24 UTC | #3

Yes, this seems to be going to be quite good. Go ahead!

-------------------------

artgolf1000 | 2017-05-04 00:02:22 UTC | #4

Monkey First had achieved a DOF shader two years ago: https://github.com/MonkeyFirst/urho3d-post-process-dof

-------------------------

sabotage3d | 2017-05-04 14:22:38 UTC | #5

The question is which method is faster :slight_smile:

-------------------------

godan | 2017-05-04 15:18:50 UTC | #6

@Victor Great to hear that IOGRAM is useful to you! Indeed, I find that developing shaders/renderpaths is MUCH easier with iogram that otherwise. However, I think there is work to be done - definitely let me know if you have any suggestions regarding ui or workflow. So far, we have:

Create Material:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/900eeb839e7ba95f606d639cdca9319cf391b2e5.png" width="690" height="268">

Create Standard (PBR) Material:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d813cd6498f28c20f452a29d2f3b118cfff16c8b.png" width="690" height="251">

And AppendRenderPath:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a80e954f4f30b1f9561c49ac55fc4319e903851b.png" width="680" height="287">

-------------------------

Victor | 2017-05-04 17:09:49 UTC | #7

Last night I started to watch your 'Getting Started' video. Tomorrow/weekend I will dive into it a bit more. Just finishing up some vegetation stuff beforehand. I'm really excited about working with it. I plan to create a foliage shader using it, and a lot of other things.

Thanks again for this tool!

-------------------------

