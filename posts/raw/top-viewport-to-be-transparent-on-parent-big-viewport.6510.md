mohamed.chit | 2020-11-08 22:32:35 UTC | #1

Hi everyone,
I have searched, how to make a top small viewport transparent (I mean the drawn models to be transparent), so we can see the top small viewport transparent and as background the main full screen viewport.
I found questions and answers to this question, suggestion was made that do not use clear command in the render path. That does not make drawn models transparent.

I came up with the following render path as a solution:

     <renderpath>

    <rendertarget name="scene_to_target" sizemultiplier="1 1" format="rgba" filter="true" />

    <command type="clear" color="0.0 0.0 0.0 0.0" depth="1.0" output="scene_to_target" />

    <command type="scenepass" pass="base" output="scene_to_target" />

    <command type="quad" vs="transparency_src" ps="transparency_src" blend="multiply" output="viewport">
        <parameter name="transparency" value="0.7 0.7 0.7 0.7" />
    </command>

    <command type="quad" vs="transparency_des" ps="transparency_des" blend="add" output="viewport">
        <texture unit="diffuse" name="scene_to_target" />
        <parameter name="transparency" value="0.3 0.3 0.3 0.3" />
    </command>

    </renderpath>

So, with this render path, we use a render target, we draw the scene on the render target.

then we draw a quad with blend **multiply** and **transparency** 0.7

then we made another draw of a quad with blend **add** and **transparency** 0.3

now I believe the following equation for each pixel has been full-filled

**Final_clr** = **Src_clr**  * 0.7 + **Des_clr** * 0.3

And thus I simulated transparency with linear blending.

Now to my surprise, it is not working, i get solid none-transparent result.

If I use simply this render path:

     <renderpath>

    <command type="quad" vs="transparency_src" ps="transparency_src" blend="multiply" output="viewport" >

    <parameter name = "transparency" value="0.7 0.7 0.7 0.7" />

    </command>

    </renderpath>

I get transparent small viewport, which is one color, but it full-fills the first part of the equation:

**Src_clr** * 0.7

Here are the shaders, pretty simply:

-------- transparency_src

    #include "Uniforms.glsl"

    #include "Samplers.glsl"

    #include "Transform.glsl"

    #include "ScreenPos.glsl"

    uniform vec4 cTransparency;

    void VS()
    {
        mat4 modelMatrix = iModelMatrix;
        vec3 worldPos = GetWorldPos(modelMatrix);
        gl_Position = GetClipPos(worldPos);
    }

       void PS()
    {
        gl_FragColor = cTransparency;
    }


-------- transparency_des


    #include "Uniforms.glsl"

    #include "Samplers.glsl"

    #include "Transform.glsl"

    #include "ScreenPos.glsl"

    varying vec2 vScreenPos;

    uniform vec4 cTransparency;

    void VS()
    {
        mat4 modelMatrix = iModelMatrix;
        vec3 worldPos = GetWorldPos(modelMatrix);
        gl_Position = GetClipPos(worldPos);
        vScreenPos = GetScreenPosPreDiv(gl_Position);
    }

    void PS()
    {
        gl_FragColor = texture2D(sDiffMap, vScreenPos) * cTransparency;
    }

Why when in the second quad command, with blend **add** I get all solid colors?


I cannot explain why i get such results.

-------------------------

Eugene | 2020-11-08 15:01:17 UTC | #2

Viewport overwrites destination region, it’s technically impossible to blend stuff this way. 
What you can do is to use render-to-texture to render small viewport, and then use this texture to render translucent quad in main viewport.

-------------------------

mohamed.chit | 2020-11-08 15:09:21 UTC | #3

thanks for the quick reply, the thing is, it has worked with the first quad command, I got a transparent viewport, why the second is not doing the same.
"Viewport overwrites destination region" , to be honest I still do not get it , especially it worked with the first quad command.

-------------------------

Eugene | 2020-11-08 15:21:57 UTC | #4

> Viewport overwrites destination region” , to be honest I still do not get it

Oh, there was miscommunication. I was talking about `Viewport`s, not "viewports".

I'm trying to read the code, but it's just too much. I'll try later.
I'd suggest to format code properly and add some screenshots maybe, because in current form I cannot really make any sense of it. And I spent 5 mins reading

-------------------------

mohamed.chit | 2020-11-08 15:22:16 UTC | #5

thanks again for the reply, trust me I did try that, I am new here i did not know how to format, i will try again, hopefully I will make it more readable for you guys.

-------------------------

Eugene | 2020-11-08 15:29:58 UTC | #6

Also, it would help if you explain what exactly you want to achieve.
Because now I can think of two very different tasks that both fit your description.

Do you want top viewport to be uniformly transparent, like this:
![image|250x161](upload://rhfWwVsVawnBznPyLl7F1inEkZk.png) 

Or you want top viewport trasnparent depending on its content? I.e. have solid objects in top viewport and main viewport as background for these objects.

-------------------------

mohamed.chit | 2020-11-08 15:33:41 UTC | #7

The top viewport should be uniformly transparent.

With the first quad command i get it uniformly transparent, but in the second, I get none-sense result.

I did reformatted, hope it is better, please let me know if you would me to do more to it.

-------------------------

mohamed.chit | 2020-11-08 21:55:03 UTC | #8

Here is another render path pipeline, which can blend successfully:

    <renderpath>

    <command type="quad" vs="transparency_src" ps="transparency_src" blend="multiply" output="viewport">
        <parameter name="transparency" value="0.7 0.7 0.7 0.7" />
    </command>

    <command type="quad" vs="transparency_src" ps="transparency_src" blend="add" output="viewport">
        <parameter name="transparency" value="0.0 0.3 0.0 0.0" />
    </command>
      
    </renderpath>

So first quad multiplies and second adds, and it works.

But it does not work when I use render target, and I cannot explain it.

here is the shader user in the above render path:

    #include "Uniforms.glsl"
    #include "Samplers.glsl"
    #include "Transform.glsl"
    #include "ScreenPos.glsl"

    uniform vec4 cTransparency;

    void VS()
    {
        mat4 modelMatrix = iModelMatrix;
        vec3 worldPos = GetWorldPos(modelMatrix);
        gl_Position = GetClipPos(worldPos);
    }

    void PS()
    {
        gl_FragColor = cTransparency;
    }

-------------------------

mohamed.chit | 2020-11-08 21:56:15 UTC | #9

In my previous reply i sent you a render path with a successful blending, again to my suprise if I modify it as follows:

    <renderpath>

    <rendertarget name="scene_to_target" sizemultiplier="1 1" format="rgba" filter="true" />

    <command type="clear" color="0.0 0.0 0.0 0.0" depth="1.0" output="scene_to_target" />

    <command type="scenepass" pass="base" output="scene_to_target" />

      

    <command type="quad" vs="transparency_src" ps="transparency_src" blend="multiply" output="viewport">
        <parameter name="transparency" value="0.7 0.7 0.7 0.7" />
    </command>


    <command type="quad" vs="transparency_src" ps="transparency_src" blend="add" output="viewport">
        <parameter name="transparency" value="0.0 0.3 0.0 0.0" />
    </command>

    </renderpath>


once there is a render target in the render path, even without using it, blending does not work any more, it does not make any sense, and I think this should be considered as a bug.

-------------------------

Eugene | 2020-11-08 16:43:36 UTC | #10

[quote="mohamed.chit, post:9, topic:6510"]
once there is a render target in the render path, even without using it,
[/quote]
But you use it. You clear it and your render scene to it, probably changing contents of global depth buffer.

Can you explain how exactly you render top viewport to parent viewport?
What operation causes actual final rendering of top viewport?
For some reason I cannot understand it from your code.

-------------------------

mohamed.chit | 2020-11-08 21:03:36 UTC | #11

Hi,
I meant I do not use it in the second quad command, and it changes the result, before declaring the render target, transparency worked, after declaring the target, transparency was gone, even it was not used in the second quad.
Having multiple viewports is exactly identical to sample number 09: MultipleViewports.cpp

https://github.com/urho3d/Urho3D/blob/master/Source/Samples/09_MultipleViewports/MultipleViewports.cpp.

I believe if you just try the path renders i provided and the shaders, you will get the same result.

I hope if this an issue in Urho3d to be fixed, I like Urho3d, but this is a bit frustrating, especially it is not understood why it is happening. at least from my side.

-------------------------

Eugene | 2020-11-08 21:08:18 UTC | #12

You don’t use color buffer filled by scene rendering, true. Are you certain you don’t use depth buffer? I’m not. Render paths are obscure thing, I have never really liked debugging them.

The point is, your render paths are beyond complex and I have no clue what exactly they are doing.
Whereas your initial task requires no render path modification at all.
Default render path should work just fine.

-------------------------

mohamed.chit | 2020-11-08 21:21:49 UTC | #13

I render the scene to the render target, then I use the render target as a texture in the second quad command.
The second quad command uses the blend **add**, but it is not behaving this way.
When I do not use a render target, the concept works. there is no clear explanation why this is happening.
I am not using any depth information from the drawn scene in the render target, I get only the texture colors.

-------------------------

Eugene | 2020-11-08 21:30:13 UTC | #14

You are not using depth information explicitly, but it may be used by default. I don’t really remember all the defaults. I think every command uses depth information by default, but I may be wrong. 

Also, my previous question stands. How exactly do you render small viewport on top of parent viewport? I checked previous replies several times but I didn’t find an answer.

-------------------------

mohamed.chit | 2020-11-08 21:32:27 UTC | #15

for the parent/child viewport, I use the renderer,
I set the num of view to 2
**renderer->SetNumViewports(2);**

the parent has the index 0

**renderer->SetViewport(0, main_viewport);**

the child has the index 1 

**renderer->SetViewport(1, second_viewport);**

I tried as well between the first quad command and the second quad command to clear the depth buffer only on the viewport, that does not help as well.

-------------------------

Eugene | 2020-11-08 21:39:50 UTC | #16

I see. I’ll think about it a bit more. BTW, have you tried actual “alpha” blend in that first render path in second quad command?

-------------------------

mohamed.chit | 2020-11-08 21:53:28 UTC | #17

I tried that already, it did not work.
In concept, I have provided the equation above, it shows how the two quad commands should make transparent result, it should work.
For now it works only without render target, but Using render target is making the problem for some reason.
Using two quad commands with blend **multiply** and **add** respectively should be correct.

-------------------------

Eugene | 2020-11-08 21:58:53 UTC | #18

[quote="mohamed.chit, post:17, topic:6510"]
but Using render target is making the problem for some reason.
[/quote]
Yep, I see the problem now. Render path evaluation is tricky thing that may depend on your exact hardware, application code and launch configuration. I may try to debug it later _if_ I reproduce this issue.
Try debugging it yourself too, RenderDoc is quite easy to use. Doesn’t work on OpenGL 2 tho.

-------------------------

Eugene | 2020-11-09 09:56:23 UTC | #19

So, I have good news and bad news.

Good news is that I understand why it doesn't work.
Bad news is that I have no clue what to do about it.

You see, Urho has "render target substitution" mechanism.
Render path, generally speaking, doesn't always write into output texture directly.
Sometimes it chooses to use intermediate buffer.
Exact conditions are beyond my understanding.

So, you cannot expect "viewport" to contain anything reasonable at the beginning of render path.
I don't know if it was done to simplify things, or if it was intentional decision to isolate render paths so output of one render path does not affect another render path.

Anyway, I don't see how you can make it work with separate `Viewport`s.

You may consider using UIElement for 3D scene view to get what you want.

-------------------------

