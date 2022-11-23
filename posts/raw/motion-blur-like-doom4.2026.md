1vanK | 2017-01-02 01:12:23 UTC | #1

[github.com/1vanK/Urho3DMotionBlur](https://github.com/1vanK/Urho3DMotionBlur)

Use START_DEMO.bat for launch

[img]https://raw.githubusercontent.com/1vanK/Urho3DMotionBlur/master/Preview.gif[/img]

-------------------------

Bananaft | 2017-01-02 01:12:23 UTC | #2

Looks really neat and smooth.
So it uses camera transform and only affected by camera motion? Or it uses full velocity vectors pass, and can blur many separated objects?

-------------------------

1vanK | 2017-01-02 01:12:23 UTC | #3

[quote="Bananaft"]Looks really neat and smooth.
So it uses camera transform and only affected by camera motion? Or it uses full velocity vectors pass, and can blur many separated objects?[/quote]

only camera motion

-------------------------

rasteron | 2017-01-02 01:12:24 UTC | #4

nice.

-------------------------

sabotage3d | 2017-01-02 01:12:24 UTC | #5

Its pretty cool. I am getting bugs on my OSX. The motion blur is jittering and there is motion blur only in some areas of the screen.

-------------------------

1vanK | 2017-01-02 01:12:24 UTC | #6

[quote="sabotage3d"]Its pretty cool. I am getting bugs on my OSX. The motion blur is jittering and there is motion blur only in some areas of the screen.[/quote]

try to turn on vsync (options -v)

-------------------------

1vanK | 2017-01-02 01:12:24 UTC | #7

Also whether you are using the latest version of the engine?

-------------------------

Egorbo | 2017-01-02 01:12:24 UTC | #8

Wow! looks nice, does it work on GLES iOS/Android?

-------------------------

1vanK | 2017-01-02 01:12:25 UTC | #9

[quote="Egorbo"]Wow! looks nice, does it work on GLES iOS/Android?[/quote]

I have not tested

-------------------------

Cpl.Bator | 2017-01-02 01:12:25 UTC | #10

Very nice ! ( with -v that work fine here ) , great job ! what the next ? dof ? :smiley:

-------------------------

1vanK | 2017-01-02 01:12:25 UTC | #11

[quote="Cpl.Bator"]Very nice ! ( with -v that work fine here ) , great job ! what the next ? dof ? :D[/quote]

This shader is not finished yet (it uses an additional forward light pass for weapon and I can not solve a couple of issues). I have reworked version with mask for weapon, but additional texture affects performance

dof already implemented by monkeyfirst [github.com/MonkeyFirst/urho3d-post-process-dof](https://github.com/MonkeyFirst/urho3d-post-process-dof) (but as far as I remember, there is need to improve)

-------------------------

1vanK | 2017-01-02 01:12:26 UTC | #12

Please test updated version. Whether there is a problems WITHOUT vsync? New version render scene to texture and blurs it there, but not just in the viewport

EDIT: for launch still use START_DEMO.bat

-------------------------

Cpl.Bator | 2017-01-02 01:12:26 UTC | #13

work fine without vsync.

-------------------------

1vanK | 2017-01-02 01:12:26 UTC | #14

[quote="Cpl.Bator"]work fine without vsync.[/quote]

ok, but now it is impossible to turn off effect by tag, need use another renderpath without motion blur ...

EDIT: although I have an idea

-------------------------

sabotage3d | 2017-01-02 01:12:26 UTC | #15

It works properly with vsync it looks pretty cool.

-------------------------

1vanK | 2017-01-02 01:12:26 UTC | #16

Have you problems with other shaders (Blur, Bloom) when VSync is disabled?

EDIT: a have a hypothesis that engine on some frames start showing viewport before bluring when vsync is disabled and fps is high
EDIT2: someone can test problem by using WithoutMask.bat in repo (u can change window size to 200x700 for increasing fps)

-------------------------

Modanung | 2017-01-02 01:12:30 UTC | #17

For some reason I had to use [i]-ap[/i] flag for the Urho3DPlayer to locate the CoreData folder and then merge the Final folder into that one and the Data folder for it to find all the resources. Then I saw a baked room (Andrew Price's right?) and a textured pistol, but [u]no blur[/u].
I'm on Xubuntu Linux 64-bit using the proprietary Nvidia drivers. Which - apart from the occasional heavy frame drops - tends to outperform the open Xorg drivers. Switching back to Xorg is a pain though, otherwise I'd be happy to test with those.
I've tried the [i]-v[/i] option; no help.

-------------------------

1vanK | 2017-01-02 01:12:30 UTC | #18

[quote="Modanung"]For some reason I had to use [i]-ap[/i] flag for the Urho3DPlayer to locate the CoreData folder and then merge the Final folder into that one and the Data folder for it to find all the resources. Then I saw a baked room (Andrew Price's right?) and a textured pistol, but [u]no blur[/u].
I'm on Xubuntu Linux 64-bit using the proprietary Nvidia drivers. Which - apart from the occasional heavy frame drops - tends to outperform the open Xorg drivers. Switching back to Xorg is a pain though, otherwise I'd be happy to test with those.
I've tried the [i]-v[/i] option; no help.[/quote]

Any warnings or errors in log?

-------------------------

Modanung | 2017-01-02 01:12:30 UTC | #19

[quote="1vanK"]Any warnings or errors in log?[/quote]
None

-------------------------

1vanK | 2017-01-02 01:12:30 UTC | #20

I have no ideas. Try output in shader intermediate steps.

Weapon maskt:

[code]void PS()
{
    float weaponmask = texture2DProj(sDiffMap, vScreenPos).a;
    
    gl_FragColor = vec4(weaponmask);
}
[/code]

[url=http://savepic.ru/9855112.htm][img]http://savepic.ru/9855112m.png[/img][/url]

Depth:

[code]void PS()
{
    float depth = ReconstructDepth(texture2DProj(sDepthBuffer, vScreenPos).r);
    
    gl_FragColor = vec4(depth * 20);
}
[/code]

[url=http://savepic.ru/9849992.htm][img]http://savepic.ru/9849992m.png[/img][/url]

-------------------------

Modanung | 2017-01-02 01:12:31 UTC | #21

I am getting identical result with those pixel shaders.

Also it turns out the path argument required to be enclosed in quotation marks to get all three folders across.

WithMask: Same as Final
WithoutMask: A screen filling flickering in tones of the room with the occasional contour of a window. The gun is rendered fine.
ViewportAlpha: Like Final, but with a pitch black gun.

-------------------------

1vanK | 2017-01-02 01:12:31 UTC | #22

Try
[code]
void PS()
{
    float weaponmask = texture2DProj(sDiffMap, vScreenPos).a;
    
    //gl_FragColor = vec4(mask);
    //return;
    
    if (weaponmask == 0)
    {
        gl_FragColor = texture2DProj(sDiffMap, vScreenPos).rgba;
        return;
    }

    // HWDEPTH
    float depth = ReconstructDepth(texture2DProj(sDepthBuffer, vScreenPos).r);
    
    

    vec3 worldPos = vFarRay * depth / vScreenPos.w;
    worldPos += cCameraPosPS;

    vec4 oldClipPos = vec4(worldPos, 1.0) * cOldViewProj;
    oldClipPos /= oldClipPos.w;

    vec4 oldScreenPos = vec4(oldClipPos.x * vGBufferOffsets.z + vGBufferOffsets.x * oldClipPos.w,
                        oldClipPos.y * vGBufferOffsets.w + vGBufferOffsets.y * oldClipPos.w,
                        0.0, oldClipPos.w);

    vec4 offset = (vScreenPos - oldScreenPos);
    offset = offset / (cTimeStep * 20.0);
	
    gl_FragColor = offset;
}[/code]

It should show different colors when you move a the mouse

[url=http://savepic.ru/9836552.htm][img]http://savepic.ru/9836552m.png[/img][/url]

Also try to remove all comments from shader. May be it not works with UTF8 comments

-------------------------

1vanK | 2017-01-02 01:12:31 UTC | #23

Also are you using the latest version of the engine?

-------------------------

Modanung | 2017-01-02 01:12:33 UTC | #24

[quote="1vanK"]Also are you using the latest version of the engine?[/quote]
Yep

-------------------------

1vanK | 2017-01-02 01:13:22 UTC | #25

Repo moved to [github.com/1vanK/Urho3DMotionBlur](https://github.com/1vanK/Urho3DMotionBlur)

-------------------------

sabotage3d | 2017-01-02 01:13:41 UTC | #26

Is it possible to use the same technique for a depth of field effect?

-------------------------

1vanK | 2017-01-02 01:13:41 UTC | #27

[quote="sabotage3d"]Is it possible to use the same technique for a depth of field effect?[/quote]

I think there is nothing in common. Even pixel blurring algorithm is other. Easier write a DOF shader from scratch,  than try to take something useful from this

-------------------------

