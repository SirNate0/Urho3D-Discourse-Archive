najak3d | 2021-03-09 07:38:57 UTC | #1

Our map app shows Vector lines in 3D perspective, and the camera is often aligned to a line (e.g. a route line you are traveling).   The goal is that these lines are all fixed-screen-width no matter how far they are from the camera in 3D space.  To make the lines standout and look anti-aliased, we employ a gradient for both color (fade to black) as well as fade Alpha at the edges.  The end result looks fantastic, with one caveat -- When the camera is close-up and aligned to one of these lines, it's easy to notice a gradient-interpolation defect.

Each line consists of 2 triangles, where the left-side gradient coordinate is 0 and the right-side is 1.   This looks perfect from top-down or side-views.  But when looking at it straight on, since we are contorting the line segment to maintain fixed-width in screen space, the gradient is grossly messed up, and you can see the triangles now...   (see image #2 below).

What we want to achieve is for the gradient to occur in Screen-Space, not Clip-Space (because the W values still vary wildly -- as the far segment of the line is further away).   The virtual effect in 3D space is that we've enlarged the width of the line at far distances, to make them have fixed-width (although we do all of these manipulations in ClipSpace/ScreenSpace).

How do we make the Gradient Interpolation in the Fragment Shader ALSO occur in ScreenSpace, instead of ClipSpace (where the W value let's it know the true spacing in 3D, vs. Screen space, and thus contorts our gradient!).

Screenshot #1 - show the top view -- gradient looks fine.
![image|614x500](upload://8dRON5SqZo3qXbqiip0hdy3ABa7.jpeg) 

Screenshot #2 shows the ground-view aligned with line - here Gradient is CONTORTED:
(the camera is near ground, looking right down the barrel of this line, almost - just above it)
![image|664x223](upload://yKZhpDA74Xw0pm55ZCQnVhc6ARi.png) 

NOTE - I have widened this line segment for illustration only.  It's going to be skinnier, but even when skinny, the contortion of gradient looks very bad.  So we need to fix this.

And here is our Shader code that produces this contorted result:

// Every Line Segment consists of 4 unique (non-reused vertices).
//    Vertices 1-2:  Both are StartPoint, one for each Side of the line (worldPos.Y polarity = Side.   -1=Left,  +1=Right side.
//        worldPos2 - is the coordinate for the EndPoint of the line segment.    Y component = +1, to indicate that the vertices are the StartPoint.
//        sideSelect = -1 for 1st Vertex, and +1 for 2nd Vertex (left side, and right side)
//        endSelect = +1 for both of these vertices (indicates that we're at teh Start Point).
//
//    Vertices 3-4:  Both are EndPoint, one for each Side of the line (worldPos.Y polarity = Side.   -1=Left,  +1=Right side.
//        worldPos2 - is the coordinate for the StartPoint of the line segment.    Y component = -1, to indicate that the vertices are the End Point
//        sideSelect = -1 for 3rd Vertex, and +1 for 4th Vertex (left side, and right side)
//        endSelect = -1 for both of these vertices (indicates that we're at the EndPoint)
//
void VS(float4 worldPos : POSITION, // Position of current line Endpoint in WorldSpace.   Y component == sideSelect, used for vertex offset
    float3 worldPos2 : NORMAL0, // Position of the Next EndPoint in WorldSpace     Y component == polarity (+1 = StartPoint, -1 = End Point)
    out float oFade : TEXCOORD0, // Used to create the Left-to-Right Gradient for this line
    out float4 clipPos : OUTPOSITION) // Position of this Vertex in ClipSpace
{
    float sideSelect = sign(worldPos.y); // -1 for LeftSide of Line;  +1 for RightSide of line  (used to control gradient, and perpendicular offset)
    float endSelect = sign(worldPos2.y); // +1 for StartPoint, and -1 for EndPoint.  (used below to select the opposite Perpendicular offset)

    worldPos.y = abs(worldPos.y);   // Y position is always positive.   The polarity for this Y component used above to indicate 'sideSelect'
    worldPos2.y = abs(worldPos2.y); // Y position is always positive.   The polarity for this Y component used above to indicate 'endSelect'

    clipPos = GetClipPos(worldPos);
    float2 screenPos = clipPos.xy / (clipPos.w);

    float4 clipPos2 = GetClipPos(worldPos2);
    float2 screenPos2 = clipPos2.xy / (clipPos2.w);

    float2 sDir = screenPos2 - screenPos;
    float2 nDir = normalize(sDir);

    float halfWidth = endSelect * 0.1 * clipPos.w;
    float2 posOffset = float2(sideSelect * halfWidth * nDir.y, -sideSelect * halfWidth * nDir.x); // Select the Left/Right Perpendicular offset from end point

    clipPos.xy += posOffset;

    if (sideSelect < 0) // Left Side, White
        oFade = 1.0;
    else // Right-Side, fades to Black
        oFade = 0.0;
}

void PS(
    float oFade : TEXCOORD0,
    out float4 oColor : OUTCOLOR0)
{
    oColor = float4(oFade, oFade, oFade, 1.0);
}

====


NOTE: If I modified the Vertex Shader line to be:
   float halfWidth = endSelect * 0.1; // stop multiplying by this: * clipPos.w;

Then the end result is that it gets smaller as it gets further away (perspective mode), then the Gradient fixes itself.   BUT, we cannot have our lines fade; they must maintain fixed width -- and thus the Gradient gets cortorted.   Here's what the ground-view looks like of this line if I make the above edit to the vertex shader: (BUT we aren't permitted to do this, so this is only for illustration of the Gradient technique working for perspective mode)
![image|583x340](upload://eKnNR5bjJVWMXdfh7eAAJUqn0yZ.jpeg)
.
.
Since we must used Fixed-Width lines, in ground-view, our lines instead look like this (BAD):
![image|690x233](upload://bGwBfNlS3ymwgSCW1CsYHjtLttm.jpeg)
.
.
Here's another view of the defect Ground-View for this line, but this one is skinnier, so it looks more like a line.  Here you can still see the impact of gradient contortion in ClipSpace:
![image|621x365](upload://wvcJ0SOzhkJGQBQhURM5zdr4nwr.jpeg)
.
.
**SUMMARY**: Our end goal is to figure out how to tell the Fragment (pixel) shader to apply the Gradient in ScreenSpace, not ClipSpace, so that it's even and looking good.

-------------------------

JSandusky | 2021-03-10 10:41:59 UTC | #2

Probably the division by W the hardware does on interpolants. Do the Z-division by W so the hardware doesn't have to (double check me on that, I could be brainfarting and it's not needed) and then set `clipPos.w = 1.0;` after you add your offset. I'm guessing warped perspective divide is munging your TEXCOORD0 interpolant.

Clipspace stuff generally doesn't work with interpolants though if you can't make work with W = 1 as calculating a new W is mind-boggling (to me at least).

You probably really do need GS for what you're doing because none of that looks like simple lines.

-------------------------

glebedev | 2021-03-10 08:16:45 UTC | #3

if you pass clip pos to the pixel shader then

hlsl
screenSpaceUV = (iClipPos.xy / iClipPos.w) * float2(cGBufferInvSize.y / cGBufferInvSize.x, 1.0)

glsl
screenSpaceUV = (vClipPos.xy / vClipPos.w) * vec2(cGBufferInvSize.y / cGBufferInvSize.x, 1.0)

-------------------------

najak3d | 2021-03-10 10:44:30 UTC | #4

@JSandusky :
Your concept worked.  I set the coordinates to screenspace (divided by W) then set W to 1.0, and it now does the gradient correct-enough to look good.

I'll post the shader code once I get it cleaned up.

-------------------------

najak3d | 2021-03-10 20:33:48 UTC | #5

The corrected vertex shader code looks like this:
===


```
void VS(float4 worldPos : POSITION, // Position of current line Endpoint in WorldSpace. Y component == sideSelect, used for vertex offset
float3 worldPos2 : NORMAL0, // Position of the Next EndPoint in WorldSpace Y component == polarity (+1 = StartPoint, -1 = End Point)
out float oFade : TEXCOORD0, // Used to create the Left-to-Right Gradient for this line
out float4 clipPos : OUTPOSITION) // Position of this Vertex in ClipSpace
{
float sideSelect = sign(worldPos.y); // -1 for LeftSide of Line; +1 for RightSide of line (used to control gradient, and perpendicular offset)
float endSelect = sign(worldPos2.y); // +1 for StartPoint, and -1 for EndPoint. (used below to select the opposite Perpendicular offset)

worldPos.y = abs(worldPos.y);   // Y position is always positive.   The polarity for this Y component used above to indicate 'sideSelect'
worldPos2.y = abs(worldPos2.y); // Y position is always positive.   The polarity for this Y component used above to indicate 'endSelect'

clipPos = GetClipPos(worldPos);
float2 screenPos = clipPos.xy / (clipPos.w);

float4 clipPos2 = GetClipPos(worldPos2);
float2 screenPos2 = clipPos2.xy / (clipPos2.w);

float2 sDir = screenPos2 - screenPos;
float2 nDir = normalize(sDir);

float halfWidth = endSelect * 0.1 * clipPos.w;
float2 posOffset = float2(sideSelect * halfWidth * nDir.y, -sideSelect * halfWidth * nDir.x); // Select the Left/Right Perpendicular offset from end point

clipPos.xy += posOffset;

// these next two lines maintain the screen position of my vertices (and even the depth buffer, but now interpolation of the gradient is now done in screenspace
clipPos.xyz /= clipPos.w;
clipPos.w = 1.0;

if (sideSelect < 0) // Left Side, White
    oFade = 1.0;
else // Right-Side, fades to Black
    oFade = 0.0;

}

...

-------------------------

