najak3d | 2022-02-24 23:11:35 UTC | #1

I am seeing this now in two different Urho-based apps that I'm working on.   I see it in Urho.NET which uses the latest Urho3D source code.

I have a shader which scales Text in Screenspace to control size (keeping it readable at all ranges - we increase/decrease size slowly as you get closer/further away).

However, in the View3D and also when we use Render-To-Texture to capture a Screenshot, the result is that the Y-Axis in ScreenSpace is inverted, and our Text ends up Upside-Down.   Everything else about the rendering is correct; the only defect is Y-Axis ScreenSpace is inverted.

Here is a screenshot from our GPS App:  (TOP = Correct;   BOTTOM = Y-Inverted)

![image|402x500](upload://bt783sNAsnafIA5hV8DijJ5oS3V.png)

And from our Game, still with crude graphics, but the Font, rendered inside a View3D, the ScreenSpace is inverted:
![image|570x500](upload://y5KnLf3siZJoKmVuiafdYAfi6Wb.png)

===
This seems like an Urho3D bug, somehow.  I can file this as an issue, if it turns out to be the case.

Our current/kludged workaround is to modify the Y-scalar when inside V3D or doing RTT.

-------------------------

SirNate0 | 2022-02-25 03:10:13 UTC | #2

So, to clarify, you are observing different results when rendering to texture vs when rendering to the screen directly? And are you sure the texture is not just upside down?

-------------------------

GoldenThumbs | 2022-02-25 23:24:16 UTC | #3

OpenGL and DirectX have different standards for which way the Y axis should go (whether it has to be inverted or not), and I don't think Urho abstracts this away. There could be a function that handles this in one of the accompanying shader include files, I'm not sure.

-------------------------

najak3d | 2022-02-25 23:52:25 UTC | #4

@SirNate0 - this happens on both Android and Windows WPF the same (HLSL and GLSL).

The texture is right side up, because EVERYTHING ELSE in the scene is in the correct locations, including the "base location for the text".   For our text, we send the Text shader 4 vertices per letter, all at the same World Location, and use the TexCoord2 to indicate "screenoffset from center" and so the quad gets sized in Screen space.

Here is the vertex shader GLSL:
```
#ifdef COMPILEVS
    uniform mediump vec2 cScale;
    uniform mediump vec3 cWorldPos;
#endif

varying vec2 vTexCoord;

void VS()
{
    vec4 clipPos = GetClipPos(cWorldPos);

    // Now offset the vertex position
    vec2 posOffset = iTexCoord1 * clipPos.w;
    posOffset.x *= cScale.x;
    posOffset.y *= cScale.y;   //  CHANGE TO "*= -cScale.y"  fixes the issue
    clipPos.xy += posOffset;
    gl_Position = clipPos;
    vTexCoord = iTexCoord;
}
```

When we use this for "screen-capture" we have a kludge, to simply toggle polarity shader parameter "Scale.y" for one frame -- capture it, and be done.

However, this is also happening inside the "View3D" windows as well, for which the problem isn't as simple.  We're going to need to have different shaders working in this context.

Sure seems to us like an Urho3D core bug. 

You should be able to validate it yourself, with a simple screen-space vertex shader, running in both normal mode, and the View3D, on both Android and WPF alike.

-------------------------

GoldenThumbs | 2022-02-27 00:50:14 UTC | #5

If I am understanding this code right, why are you using a custom shader for this? Isn't this basically just a billboard? Urho has billboards already. Just like, use a billboard and set the texture to the render texture. Well, that could probably result in an inverted y axis too, not sure. Gonna have to test that. I'll get back to you with my results.

-------------------------

najak3d | 2022-02-27 13:14:49 UTC | #6

We have two contexts where this is happening, neither of which is resolved by a billboard (which as you indicated, though, likely suffers the same defect):

1. GameEditor inside Avalonia Toolset -- accomplished the View3D UI component which has been wrapped to behave as an Avalonia Render Surface.   The basics for this will be released to the public when we're done.

2. Setting up an offscreen camera to capture a scene shot, rendering it to a Texture, then exporting that image via "Texture.GetData()".

When I saw it happen twice for two entirely different contexts, that lead to my belief that this is likely an Urho bug.

-------------------------

GoldenThumbs | 2022-02-27 14:47:09 UTC | #7

Are you using render textures in both cases or just the one? Sorry if my questions seem a bit redundant, I've got to admit I find what you are trying to do a bit confusing. Maybe if I recreate one or both of these cases myself I'll understand better

-------------------------

najak3d | 2022-02-27 18:21:09 UTC | #8

We are using Urho.NET (@elix22 invention).   And we just Create the View3D and then call "SetView(scene, camera)" and it starts rendering just like any other view port.   In this mode, we're not dealing directly with Textures/etc.... it just works  (except for screenspace Y being inverted).

For the other app (which uses UrhoSharp) - here we are doing a RTT.

In both cases, everything else is right-side-up -- just not the screen-spaced fonts, which are upside-down in both cases.

-------------------------

najak3d | 2022-03-04 07:33:17 UTC | #9

@GoldenThumbs - Any luck reproducing this yet?

-------------------------

GoldenThumbs | 2022-03-06 19:11:04 UTC | #11

I wasn't able to get Urho to build. :confused:

-------------------------

George1 | 2022-03-06 23:02:44 UTC | #12

[quote="najak3d, post:6, topic:7208"]
amera to capture a scene sho
[/quote]

Did you change any matrix calculation or inverted any axis?
I think you should attach a small example here.  So some experts can help you.

-------------------------

najak3d | 2022-03-07 00:51:04 UTC | #13

No axes or matrices manipulated.  This is just plain vanilla rendering in View3D in one app, and RTT in the other.   Two different apps; two different techniques, but produced the same inversion on screen space only.    World space is just fine; just not screen space.

I currently don't even know how to manipulate any matrices/etc.

If an expert simply tried vanilla techniques for either of those, and applied a Screen Space shader to something where you can tell if it's upside down -- they'd see it right away.

Our workaround is working fine, since in our app, we are not rendering to both at the same time.  The RTT is for a quick scene capture to image, and the View3D is used for Urholonia only when in the Game Editor mode.

-------------------------

justanotherdev | 2022-03-09 12:15:09 UTC | #14

I believe this may be expected behavior for the OpenGL backend to achieve consistent UV space between OpenGL/DirectX. When the renderer detects that the viewport target is a texture it will flip the camera's Y axis so that the produced texture can be addressed in the same UV space regardless of whether DirectX or OpenGL is being used, [see here](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/View.cpp#L599).

-------------------------

SirNate0 | 2022-03-09 12:27:07 UTC | #15

I'm thinking the solution to the problem may just be exposing whether the view has been flipped as some uniform in the shader like Unity does so that the shader can make the appropriate changes (i.e. multiply by -1).

https://docs.unity3d.com/2018.4/Documentation/Manual/SL-PlatformDifferences.html

-------------------------

