reFuseN | 2018-03-20 08:53:07 UTC | #1

Hey guys. I'm very new to Urho and Im only using Urhosharp.
Since I cant really get any interface working, Im just coding everything and trying that out. Since Im experienced with using the Unity engine and C#, this worked for me, until I had to implement a new shader...

I have never coded a shader myself and I only got one shader working in Uhro from a tutorial I found.
[Tutorial](http://nervegass.blogspot.de/2014/12/urho-shaders-edge-detection.html)

So I translated the shader I need to implement into HLSL and tried to implement it but nothing worked. Maybe you guys can help me.

Shader:
> sampler MainTex;
> sampler RampTex;
> float Speed = 4f;
> float DeltaTime = 0f;
> 
> struct v2f_img
> {
>     float4 position : SV_POSITION;
>     half2 uv : TEXCOORD0;
> };
> 
> void PS(v2f_img i) : SV_Target
> {
>     float4 col = tex2D(MainTex, i.uv);
>     return tex2D(RampTex, float2(col.r + DeltaTime * Speed, 2));
> }

Technique XML file:
>     <technique ps="Basic">
>       <pass name="MainTex" psdefines="MainTex"/>
>       <pass name="RampTex" psdefines="RampTex"/>
>       <pass name="Speed" psdefines="Speed"/>
>       <pass name="DeltaTime" psdefines="DeltaTime"/>
>     </technique>

Material XML file:
>     <material>
>       <technique name="Techniques/Basic.xml" />
>       <texture unit="MainTex" name="Textures/Background/Main/p13.jpg"/>
>       <texture unit="RampTex" name="Textures/Background/Ramp/g1.jpg"/>
>       <parameter name="Speed" value="4"/>
>       <parameter name="DeltaTime" value="0"/>
>     </material>

In the end this shader should put the colors of the "RampTex" onto the "MainTex" and change that over time to get some kind of kaleidoscope effect.

Can you guys tell me what Im doing wrong, or give me tutorials or anything, so I can understand this topic? Anything would be helpfull.

Thank you very much guys!

-------------------------

Eugene | 2018-03-20 09:02:17 UTC | #2

Vertex shader looks a bit... missing.

-------------------------

reFuseN | 2018-03-20 09:15:57 UTC | #3

Since I have 0 experience with shaders, I thought I can just delete it and the model gets drawn as it is.

-------------------------

Eugene | 2018-03-20 09:41:37 UTC | #4

SInce _some_ hardwares/drivers/API allow it, it doesn't work in general. Urho shareds are low-level (comparing to Unity), so you have to provide both vertex and pixel shaders. Usually some clever copypaste is enough.

-------------------------

reFuseN | 2018-03-20 15:20:01 UTC | #5

So now I just wanna implement any shader into the game and go from there, so I copied the LitSolid shader, renamed it and created the technique, aswell as the material file.
When Im trying to put that new material on my object, the editor breaks. When Im using the old material (which is basically all the same except for the shader name in the technique file and the technique name in the material file) it works.

      <technique vs="Basic" ps="Basic" psdefines="DIFFMAP">
        <pass name="base" />
        <pass name="litbase" vsdefines="NORMALMAP" psdefines="AMBIENT NORMALMAP" />
        <pass name="light" vsdefines="NORMALMAP" psdefines="NORMALMAP" depthtest="equal" depthwrite="false" blend="add" />
        <pass name="prepass" vsdefines="NORMALMAP" psdefines="PREPASS NORMALMAP" />
        <pass name="material" psdefines="MATERIAL" depthtest="equal" depthwrite="false" />
        <pass name="deferred" vsdefines="NORMALMAP" psdefines="DEFERRED NORMALMAP" />
        <pass name="depth" vs="Depth" ps="Depth" psexcludes="PACKEDNORMAL" />
        <pass name="shadow" vs="Shadow" ps="Shadow" psexcludes="PACKEDNORMAL" />
      </technique>
When I cut out the [psdefines="DIFFMAP"] part, it works without a texture added.

Do I have to build the shader before I can try out the project on a device via USB debugging, or am I missing something?

-------------------------

Eugene | 2018-03-20 16:12:40 UTC | #6

[quote="reFuseN, post:5, topic:4108"]
When Im trying to put that new material on my object, the editor breaks
[/quote]

What does it mean?

Maybe your shader has some errors, but they shall be printed in the console/logs in this case.

-------------------------

reFuseN | 2018-03-20 16:52:44 UTC | #7

Since I couldn’t get the editor working and I’m using UhroSharp, I’m coding everything in Visual Studio and running my app from there.
Because of that I also don’t have any error message, other than a unhandled exception debug break. That’s what I meant.

It can’t be some error in the shader, since it’s an exact copy of the build in LitDiffuse shader...

Sorry for my lack of knowledge. Maybe I should search for some more tutorials on setting up the editor correctly.

Thanks for your help.

-------------------------

Eugene | 2018-03-20 18:34:57 UTC | #8

[quote="reFuseN, post:7, topic:4108"]
Since I couldn’t get the editor working and I’m using UhroSharp, I’m coding everything in Visual Studio and running my app from there.
[/quote]

Ahh, this explains something. UrhoSharp is (a bit?) more rough than vanila Urho from the point of support, convinience, stability etc.

[quote="reFuseN, post:7, topic:4108"]
It can’t be some error in the shader, since it’s an exact copy of the build in LitDiffuse shader
[/quote]
Ahh, true, I thought you've changed something...

[quote="reFuseN, post:7, topic:4108"]
other than a unhandled exception debug break
[/quote]
That's bad. Urho mustn't crash in any case. Could you show me the callstack?

-------------------------

reFuseN | 2018-03-21 08:14:28 UTC | #9

[quote="Eugene, post:8, topic:4108"]
Ahh, this explains something. UrhoSharp is (a bit?) more rough than vanila Urho from the point of support, convinience, stability etc.
[/quote]
Yeah I have experenced that, but I think its easier for me to understand, because Im experienced with C# and the implementation of a custom shader should work the same way, shouldnt it?

[quote="Eugene, post:8, topic:4108"]
That’s bad. Urho mustn’t crash in any case. Could you show me the callstack?
[/quote]
In the constructor of the main application class, there is the following event subscription:
[code]
UnhandledException += (s, e) =>
            {
                if (Debugger.IsAttached)
                    Debugger.Break();
                e.Handled = true;
            };
[/code]
That is whats getting called, when Im trying to build my project with the newly implemented shader. Because of this, I dont have any error messages besides that this got called.
Whats bothering me is, that I did everything the same way as in the build-in files, except for a name change of the shader file and of course the name changes in the technique and in the material file...

-------------------------

Eugene | 2018-03-21 08:41:12 UTC | #10

[quote="reFuseN, post:9, topic:4108"]
That is whats getting called, when Im trying to build my project with the newly implemented shader
[/quote]

"when trying to _build_ my project" -- was it intentional or just typo?

[quote="reFuseN, post:9, topic:4108"]
because Im experienced with C# and the implementation of a custom shader should work the same way, shouldnt it?
[/quote]
It should. But I don't know how the asset pipeline is implemented in Urho#.
Are there just some folders like CoreData? Or maybe it packs things into archives?

In vanila Urho I never had any problems with custom shaders, and I made it pretty much like you.

[quote="reFuseN, post:9, topic:4108"]
Because of this, I dont have any error messages besides that this got called.
[/quote]
So you don't have anything in the callstack, do you?..
Could you just copypaste callstack here?
Or maybe test project, IDK.

FYI. There is WIP project of .NET bindings that should suck less than Urho#. I hope so, at least.
[not ready to use] https://github.com/rokups/Urho3DNet

-------------------------

reFuseN | 2018-03-21 08:58:40 UTC | #11

[quote="Eugene, post:10, topic:4108"]
“when trying to build my project” – was it intentional or just typo?
[/quote]

Oh sorry I meant when Im trying to run my project via the start button of Visual Studio.

[quote="Eugene, post:10, topic:4108"]
Are there just some folders like CoreData? Or maybe it packs things into archives?

In vanila Urho I never had any problems with custom shaders, and I made it pretty much like you.
[/quote]
Yes there is a "myData" folder and I also got one custom shader already implemented with this way, but it was a glsl shader. The Objects get also drawn, but without a texture, when I delete the [psdefines="DIFFMAP"] part of my technique file.

[quote="Eugene, post:10, topic:4108"]
So you don’t have anything in the callstack, do you?..

Could you just copypaste callstack here?

Or maybe test project, IDK.
[/quote]

No sadly not, just that the "Debugger.Break" function got called...
Maybe I will find out anything today. If so, I will let you know.

[quote="Eugene, post:10, topic:4108"]
FYI. There is WIP project of .NET bindings that should suck less than Urho#. I hope so, at least.

[not ready to use] https://github.com/rokups/Urho3DNet
[/quote]
Thanks for showing me, but I need to develop an interactive 3D room that I can implement into Xamarin right now, so I cant really wait for something. Maybe learning C++ and using native Urho3D would be an easier option.

-------------------------

Egorbo | 2018-03-21 13:11:53 UTC | #12

@reFuseN
Just try to look at the Exception you got from the UnhandledException event, it should tell you what kind of an error you are experiencing e.g. hlsl compilation error.
UrhoSharp treats all Urho3D Log.Errors as exceptions instead of ignoring them and writing to log, but you can ignore the exception as well by setting `exception.Handled = true`.
> 
> FYI. There is WIP project of .NET bindings that should suck less than Urho#. I hope so, at least.
> [not ready to use] https://github.com/rokups/Urho3DNet

@Eugene  Well, that is quite rude, what made you think UrhoSharp sucks?

-------------------------

Eugene | 2018-03-21 13:38:20 UTC | #13

[quote="Egorbo, post:12, topic:4108"]
@Eugene  Well, that is quite rude, what made you think UrhoSharp sucks?
[/quote]
Well, I don't mean suck _entirely_. Urho# runtime is fine.
But C++ to C# binding generator in Urho# sucks sooo much. So untrivial. So long instructions. So environment-demanding. So hacky. I wonder if there's at least one person except developers who managed to get it working.

-------------------------

Egorbo | 2018-03-21 13:50:07 UTC | #14

@Eugene  the bindings generator is messy yes but it's logical - it was supposed to bind 90% of API and then when all corner cases are found - I was going to rewrite it.
But I am still working on it - on a clean new version with a much more clean architecture (of the binder, not of the UrhoSharp API - it should be the same) - I'll update it once I am sure it doesn't break API.

It relies on a patched version of clang (to provide AST of Urho3D) that works only on macOS, but I almost finished porting it to Linux and Windows (via WSL).
So stay tuned :slight_smile: 

UrhoSharp surfaced 90% of API and doesn't add any significant overhead (if it does - tell me) .
The main issue with Urho3D I've been fighting with - is the fact Urho3D doesn't work with scenarios where you need to render Urho in a subview in an existing application. Because SDL clearly sucks at it - so I had to add lots of hacks for **ALL** platforms to be able to do that and it was the main source of crashes. But I beleive I've fixed all of them and now it's more or less stable. But everytime you guys update the SDL 3rd party - it's a huge pain for me to merge and solve all kind of conflicts and hidden bugs :frowning: when there is no SDL changes it usually takes me an hour to update all bindings and make sure everything is working, all structures have same offsets, etc.

-------------------------

Eugene | 2018-03-21 14:03:28 UTC | #15

TBH I thought that UrhoSharp developement was stopped long time ago...

[quote="Egorbo, post:14, topic:4108"]
It relies on a patched version of clang (to provide AST of Urho3D) that works only on macOS, but I almost finished porting it to Linux and Windows (via WSL).
[/quote]
It's the main reason why I stay away from UrhoShrap by now.
May you elaborate how things are supposed to work there? Just curious.

[quote="Egorbo, post:14, topic:4108"]
scenarios where you need to render Urho in a subview in an existing application
[/quote]
Why is it a problem? I have issues with keybord when doing it with Urho3D, noting more.

-------------------------

Egorbo | 2018-03-21 14:44:12 UTC | #16

> Why is it a problem? I have issues with keybord when doing it with Urho3D, noting more.

On Windows? Yes it works on Windows pretty well - it just needs an external Window Handle.
But it doesn't work at all on all other platforms, for example what should I do if I want to embedd urho as a UIView (or NSView for macOS) ?

> TBH I thought that UrhoSharp developement was stopped long time ago…

I do not work on UrhoSharp full time (working on Mono primary), but I maintain it. E.g. I added built-in support for all AR stuff recently including ARKit, ARCore and HL :slight_smile:

-------------------------

reFuseN | 2018-03-21 15:03:30 UTC | #17

@Egorbo
Thanks for your answer. I now found out that it is really a Shader error, although the shader is an exact copy of the LitDiffuse shader. Any suggestions why this is happening?

    03-21 15:49:01.838 E/mono-rt ( 4158): [ERROR] FATAL UNHANDLED EXCEPTION: System.Exception: Failed to link vertex shader Basic(DIRLIGHT NORMALMAP PERPIXEL) and pixel shader Basic(AMBIENT DIFFMAP DIRLIGHT NORMALMAP PERPIXEL):
    03-21 15:49:01.838 E/mono-rt ( 4158): L0007 Fragment shader uses a varying vTexCoord that has not been declared in the vertex shader

Thanks again for your help guys. Its very appreciated

-------------------------

Eugene | 2018-03-21 15:02:58 UTC | #18

[quote="reFuseN, post:17, topic:4108"]
Any suggestions why this is happening?
[/quote]

Such errors are usually quite simple to debug.
It means that your vertex and pixel shader are unconsistent in their inputs/outputs. Try to add DIFFMAP define for vertex shader too.

In future: just ensure that with given set of defines there's no undefined tails and things...

-------------------------

