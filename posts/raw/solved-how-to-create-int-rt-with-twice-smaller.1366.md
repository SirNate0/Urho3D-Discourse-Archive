codingmonkey | 2017-01-02 01:07:13 UTC | #1

<renderpath>
    <rendertarget name="newRT" sizedivisor="1 1" format="rgba" />
...

Is it sizedivisor establish this ratio for this? 
I mean if I set sizedivisor="0.5 0.5" new RT will be have a twice smaller than current frame size?

-------------------------

franck22000 | 2017-01-02 01:07:13 UTC | #2

Hello :slight_smile:

sizedivisor="2.0, 2.0" will work better :p 

or you can use sizemultiplier="0.5, 0.5"

-------------------------

codingmonkey | 2017-01-02 01:07:13 UTC | #3

hi )
thanks, I got it.
now I see one object with rendered my custom pass for debug I just copy RT into viewport with helps quad command
[code]<renderpath>
    <rendertarget name="glowRT" tag="glow" sizedivisor="4 4" format="rgba" />
    <command type="clear" tag="glowRT" color="fog" depth="1.0" output="glowRT" />

    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
    
    <command type="scenepass" pass="glowpass" output="glowRT" />
    <command type="quad" tag="glow" vs="CopyFramebuffer" ps="CopyFramebuffer" output="viewport">
        <texture unit="diffuse" name="glowRT" />
    </command>
</renderpath>[/code]

did you know how to add this my RT as light-overlay for main viewport RT ? I guessing that is also needed use the quad command for this

add.
I add blend="add" option for quad command and now it works as overlay
[code]    <command type="quad" tag="glow" vs="CopyFramebuffer" ps="CopyFramebuffer" blend="add" output="viewport">[/code]

this is current glow tech (based of diff.xml)
[spoiler][code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
    <pass name="glowpass" psdefines="GLOW" vs="Glow" ps="Glow"  />
</technique>
[/code][/spoiler]

minimalistic glow shader )
[spoiler][code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    
}

void PS()
{
    vec4 diffColor = cMatDiffColor;
    gl_FragColor = diffColor;
}
[/code][/spoiler]

and that I got after this all
[url=http://savepic.su/6132474.htm][img]http://savepic.su/6132474m.jpg[/img][/url]
now I guess need to do some kind of bluring post process for glowRT by x and y. 
[b]any ideas how to do this? [/b]

-------------------------

codingmonkey | 2017-01-02 01:07:13 UTC | #4

test this with blurred glow
[video]https://youtu.be/4EyelxXuXLA[/video]


this is full RenderPath for ForwardGlow.xml

[spoiler][code]
<renderpath>
    <rendertarget name="glowRT" tag="glow" sizedivisor="1 1" format="rgba" />
    
    <rendertarget name="blurh" tag="Blur" sizedivisor="2 2" format="rgba" filter="true" />
    <rendertarget name="blurv" tag="Blur" sizedivisor="2 2" format="rgba" filter="true" />
    
    <command type="clear" tag="glowRT" color="fog" depth="1.0" output="glowRT" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
    
    <command type="scenepass" pass="glowpass" output="glowRT" />
    
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurh">
        <parameter name="BlurDir" value="1.0 0.0" />
        <parameter name="BlurRadius" value="8.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="glowRT" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurv">
        <parameter name="BlurDir" value="0.0 1.0" />
        <parameter name="BlurRadius" value="8.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="blurh" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurh">
        <parameter name="BlurDir" value="1.0 0.0" />
        <parameter name="BlurRadius" value="4.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="blurv" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurv">
        <parameter name="BlurDir" value="0.0 1.0" />
        <parameter name="BlurRadius" value="4.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="blurh" />
    </command>
    
    
    <command type="quad" tag="BlurredGlowToViewport" vs="CopyFramebuffer" ps="CopyFramebuffer" blend="add" output="viewport">
        <texture unit="diffuse" name="blurv" />
    </command>
</renderpath>
[/code][/spoiler]

Did you also find this strange side effect when glow are disappear on far distances ?

few glow materials on one model
[url=http://savepic.su/6141693.htm][img]http://savepic.su/6141693m.jpg[/img][/url]

-------------------------

rasteron | 2017-01-02 01:07:13 UTC | #5

Finally! :slight_smile: I will definitely test this out.

-------------------------

codingmonkey | 2017-01-02 01:07:14 UTC | #6

Yes, finally) But It has one big problem - glowed objects shine through other solid objects, because this is additive post effect.
and to solve this problem probably needed in some way render other solid objects into glowRT as black colored I guess.  

Is anyone have ideas how to do this ?)

update:
I try figure out how they do this glow in this article: [gamasutra.com/view/feature/1 ... php?page=2](http://www.gamasutra.com/view/feature/130520/realtime_glow.php?page=2)
and now I guessing that need to use alpha channel of diffuse TU (viewport) to store glow mask.
if material has glowpass then it write into alpha channel on renderpath executing scenepass ="glowpass"

-------------------------

George | 2017-01-02 01:07:14 UTC | #7

I think Bananaft know how to do it.
See topic below. You might want to ask him or look at his shader code.
[topic1301.html](http://discourse.urho3d.io/t/zarevo-landscape-experiments/1256/1)

-------------------------

codingmonkey | 2017-01-02 01:07:14 UTC | #8

I think he use some kind of bloom post effect not glow

I have a new question:
to write into binded MRT I make this fix for ForwardGlow2.xml
just bind glowRT as MRT with index 6 = "custom1"
[code]
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" >
        <output index="0" name="viewport" />    
        <output index="6" name="glowRT" />
    </command>
[/code]

and add few lines to LitSolid.glsl (before per-pixel and deferred preprocessor definitions)

    #ifdef GLOW
        gl_FragData[6] = vec4(vec3(cMatDiffColor.rgb), 1.0);
    #else
        gl_FragData[6] = vec4(vec3(0.0), 0.0);
    #endif

and my question: [b]is this index gl_FragData[6] and output index="6" means the same thing?[/b]
my new strategy with rendering is that all objects in scene must write color to glowRT(default black) but only glowed objects write to this RT own color.

and second question: [b]in what scenepass I can processing all visible objects [/b]?

-------------------------

codingmonkey | 2017-01-02 01:07:14 UTC | #9

I drop previous render strategy with using MRT, because there are have some issues. (gl_FragData[6] - not worked, I got some results only if I put glowRT in gl_FragData[1] (output index="1") )

Now a revert to additive post effect, but with some changes.
The first problem what I found: Why we are not able to attach DepthBuffer from main viewport to custom user RT ?
also I trying use ForwardHWDepth with I guessing works fine in case passing DepthBuffer to other RT. But on my custom pass - depth "equal"  I do not see anything on screen, and only on "always" it's draw something.

So I think if I do not have ability to use DepthBuffer with my RT, why I do not use main viewport for this. But at first I save a frame to new tempRT (only color data).
Then I clear only color data in main viewport.
Then I render my custom pass into viewport without changing DepthBuffer data, use it only for "equal" test.
After this I got glowMask in viewport RT (clipped by non-glowed obstacles, other scene objects)  
And then I copy this mask into glowRT and  tempRT back to viewport.
In this case it work without shining though scene solid objects.

DiffGlow.xml
[spoiler][code]
<technique vs="LitSolid" ps="LitSolid" psdefines="DIFFMAP">
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
    <pass name="light" depthtest="equal" depthwrite="false" blend="add" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
    <pass name="deferred" psdefines="DEFERRED" />
    <pass name="depth" vs="Depth" ps="Depth" />
    <pass name="shadow" vs="Shadow" ps="Shadow" />
    
    <pass name="glowpass" vs="Glow" ps="Glow" depthtest="equal" depthwrite="false" />
</technique>
[/code][/spoiler]

ForwardGlow.xml
[spoiler][code]
<renderpath>
    <rendertarget name="glowRT" tag="glow" sizedivisor="2 2" format="rgba"  filter="true" />
    <rendertarget name="tempViewport" tag="tempRT" sizedivisor="1 1" format="rgba" />
    
    <rendertarget name="blurh" tag="Blur" sizedivisor="2 2" format="rgba" filter="true" />
    <rendertarget name="blurv" tag="Blur" sizedivisor="2 2" format="rgba" filter="true" />
    
    <command type="clear" tag="glowRT" color="fog" depth="1.0" output="glowRT" />
    <command type="clear" color="fog" depth="1.0" stencil="0" />
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
    <command type="forwardlights" pass="light" />
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
    
    <command type="quad" tag="CopyColorToTemp" vs="CopyFramebuffer" ps="CopyFramebuffer" blend="replace" output="tempViewport">
        <texture unit="diffuse" name="viewport" />
    </command>
    
    <command type="clear" color="fog" />
    
    <command type="scenepass" pass="glowpass" output="viewport" />
    
    <command type="quad" tag="CopyViewportGlowToGlowRT" vs="CopyFramebuffer" ps="CopyFramebuffer" blend="replace" output="glowRT">
        <texture unit="diffuse" name="viewport" />
    </command>
    
    <command type="quad" tag="CopyTempColorToViewport" vs="CopyFramebuffer" ps="CopyFramebuffer" blend="replace" output="viewport">
        <texture unit="diffuse" name="tempViewport" />
    </command>
    
    
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurh">
        <parameter name="BlurDir" value="1.0 0.0" />
        <parameter name="BlurRadius" value="4.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="glowRT" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurv">
        <parameter name="BlurDir" value="0.0 1.0" />
        <parameter name="BlurRadius" value="4.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="blurh" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurh">
        <parameter name="BlurDir" value="1.0 0.0" />
        <parameter name="BlurRadius" value="2.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="blurv" />
    </command>
    <command type="quad" tag="Blur" vs="Blur" ps="Blur" psdefines="BLUR3" output="blurv">
        <parameter name="BlurDir" value="0.0 1.0" />
        <parameter name="BlurRadius" value="2.0" />
        <parameter name="BlurSigma" value="2.0" />
        <texture unit="diffuse" name="blurh" />
    </command>
    
    
    <command type="quad" tag="BlurredGlowToViewport" vs="CopyFramebuffer" ps="CopyFramebuffer" blend="add" output="viewport">
        <texture unit="diffuse" name="blurv" />
    </command>
</renderpath>
[/code][/spoiler]

Glow.glsl (for glowpass in material)
[spoiler][code]
#include "Uniforms.glsl"
#include "Samplers.glsl"
#include "Transform.glsl"

void VS()
{
    mat4 modelMatrix = iModelMatrix;
    vec3 worldPos = GetWorldPos(modelMatrix);
    gl_Position = GetClipPos(worldPos);
    
}

void PS()
{
    vec4 diffColor = cMatDiffColor;

    gl_FragColor = diffColor;
}
[/code][/spoiler]

last screens
[url=http://savepic.su/6151685.htm][img]http://savepic.su/6151685m.jpg[/img][/url]
[url=http://savepic.su/6138373.htm][img]http://savepic.su/6138373m.jpg[/img][/url]
[video]https://youtu.be/tRxgS1A1ehg[/video]

update:

DiffUnlitGlow.xml
[spoiler][code]
<technique vs="Unlit" ps="Unlit" psdefines="DIFFMAP" >
    <pass name="base" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" />
    <pass name="deferred" psdefines="DEFERRED" />
    
    <pass name="glowpass" vs="Glow" ps="Glow" depthtest="equal" depthwrite="false" />
</technique>
[/code][/spoiler]

update:
Little optimization for RenderPath. Remove Clear command for glowRT.
Now I made two version. with downsampled glowRT and without it.
1. ForwardGlow(with twice downsampled glowRT)
[spoiler][pastebin]XtFp8hAV[/pastebin][/spoiler]

2. ForwardGlow(without glowRT)
[spoiler][pastebin]0zPTmVXi[/pastebin][/spoiler]

In my test the first RenderPath is little % faster 315fps(1) Vs 305fps(2)

add new tech for using Glow with AlphaMask textures
DiffAlphaMaskGlow.xml
[spoiler][pastebin]VciQTPv7[/pastebin][/spoiler]

DiffUnlitAlphaMaskGlow.xml
[spoiler][pastebin]ggmkpBY5[/pastebin][/spoiler]

and update  Glow.glsl shader
[spoiler][pastebin]FEWsvXQT[/pastebin][/spoiler]

Update2:
- fix couters on non-glow objects by additional additive blend from original glowRT into blurred glow RT. In this case we got strong glow on border (non-glow-object <-> glow object)
- add one common "Glow" tag. For enable/disable glow RenderPath from code side

[pastebin]2pafCn5U[/pastebin]

lastest ForwardGlow.xml
[spoiler][pastebin]nPk4Tqra[/pastebin][/spoiler]

[url=http://savepic.su/6124090.htm][img]http://savepic.su/6124090m.jpg[/img][/url]

-------------------------

