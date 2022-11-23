codingmonkey | 2017-01-02 01:08:21 UTC | #1

Hi folks!
How I may to render some of scene's object into MRT-render target ?
I tried to create an tech NoTextureUnlitMRT1.xml
[code]
<technique vs="Unlit" ps="Unlit" psdefines="MRT1" vsdefines="NOUV" >
    <pass name="base" />
    <pass name="prepass" psdefines="PREPASS" />
    <pass name="material" />
    <pass name="deferred" psdefines="DEFERRED" />
</technique>
[/code]

then i add MRT1 checking with (#if #else #end) barricades in unlit.glsl shader

[code]
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
        #ifndef MRT1 
            gl_FragColor = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
        #else
            gl_FragData[0] = vec4(GetFog(diffColor.rgb, fogFactor), diffColor.a);
            gl_FragData[1] = vec4(1.0);
        #endif
    #endif
[/code]

fix Transform.glsl to avoid gl_FragData boundary error
[code]
// Silence GLSL 150 deprecation warnings
#ifdef GL3
#define varying in

// \todo: should not hardcode the number of MRT outputs according to defines
#if defined(DEFERRED)
out vec4 fragData[4];
#elif defined(PREPASS)
out vec4 fragData[2];
#else
#ifdef MRT1
out vec4 fragData[2];
#else 
out vec4 fragData[1];
#endif
#endif
[/code]

and finally I got a Render Path
[code]
<renderpath>
    <rendertarget name="MRT" sizedivisor="1 1" format="rgba" filter="true" />
    
    <command type="clear" color="fog" depth="1.0" stencil="0" >
        <output index="0" name="viewport" />
        <output index="1" name="MRT" />
    </command>
        
    <command type="scenepass" pass="base" vertexlights="true" metadata="base" >
        <output index="0" name="viewport" />
        <output index="1" name="MRT" />
    </command>
    <command type="forwardlights" pass="light" />
    
    <command type="scenepass" pass="postopaque" />
    <command type="scenepass" pass="refract">
        <texture unit="environment" name="viewport" />
    </command>
    <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha" />
    <command type="scenepass" pass="postalpha" sort="backtofront" />
    
    <!-- preview MRT -->  
    <command type="quad" tag="MRTTag" vs="CopyFramebuffer" ps="CopyFramebuffer" blend="replace" output="viewport">
        <texture unit="diffuse" name="MRT" />
    </command>
    
</renderpath>
[/code]

In last RP commands I just copy MRT into screen for debug view.
but this is not working properly, if I try to decrease size of MRT for example to sizedivisor="2 2".
[url=http://savepic.su/6638466.htm][img]http://savepic.su/6638466m.png[/img][/url]

How to fix this? 
Is it possible to use MRT various size ?

-------------------------

1vanK | 2017-01-02 01:08:21 UTC | #2

> Is it possible to use MRT various size ?

buffers should be same size

[spoiler]http://steps3d.narod.ru/tutorials/mrt-tutorial.html

???????? ????????, ??? ?????? ?????? ???? ?????? ??????? ? ?? ??????????? ????????????? ?????? ? ??????????? gl_FragColor ? gl_FragData.[/spoiler]

-------------------------

codingmonkey | 2017-01-02 01:08:21 UTC | #3

>buffers should be same size
 :cry:

current process with mrt
[url=http://savepic.su/6630193.htm][img]http://savepic.su/6630193m.png[/img][/url]
you may finding this there: [github.com/MonkeyFirst/urho3d-light-scattering](https://github.com/MonkeyFirst/urho3d-light-scattering)
main changes:
shaders\Transform.glsl (fixed with adding - out vec4 fragData[2];) 
shaders\Unlit.glsl (fixed for #ifdef MRT) 
shaders\SunMRT.glsl (added)
ForwardSun.xml (added)
ForwardSunFast.xml (added)

-------------------------

Modanung | 2017-01-02 01:08:36 UTC | #4

Looking good! :slight_smile:

-------------------------

