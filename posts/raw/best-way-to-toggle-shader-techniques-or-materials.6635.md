najak3d | 2020-12-27 00:32:40 UTC | #1

In our GPS map app, as you zoom in closer to the ground, we toggle our shader to draw more expensive detail.

Currently, it's kludged, we do it via one of the shader parameters turn on/off the extra detail technique (which shows contour lines based upon elevation).   However, because the 'if" branch is inside the shader, it's performing the cost of this "if" no matter what.   I assume that this kludged method hurts performance enough that we ought to instead have two versions of the shader, and just swap "Shader Technique".

Pixel Shader looks like this:
===
void PS()
{
    vec4 diffColor = texture2D(sDiffMap, vTexCoord);

    vec4 elevNorm = texture2D(sNormalMap, vElevCoord).rgba; // was ra

    float hiByte = elevNorm.x * 65280.0;
    float loByte = elevNorm.y * 255.0;

    float elevFt = hiByte + loByte; // elevNorm * 65535.0;
    elevFt -= cOwnshipAltitudeFt;

    if (cHighlightAlpha > 0.01 && elevFt > -1500.0)   // <<<<= I WANT TO DITCH THIS 'IF' branch
    {
            .... complex logic to show Altitude Highlights, and Contours ....
     }

....
     gl_FragColor = diffColor;
}

====

ALSO, related, we as the user pans/zooms, we like to do a QUICK fade-in (0.15 sec) new content and fade out the old content.   This "fading" effect requires us to use "alpha" pass as follows;

  \<pass name="alpha"  depthwrite="false" blend="alpha" />

I would imagine that calling this the "alpha" pass requires extra CPU work to "sort" the objects in the alpha pass (back to front?), to make it work correctly.   However, we ONLY need this during the 0.15 seconds where we are fading in/out. 

So currently, we're ALWAYS rendering these tiles on the "alpha" pass, so that we can do this fade in/out on-demand  (each material has an "opacity" parameter).

So for efficiency, we're wanting to swap in/out the technique used (from "alpha" password to "base" pass).    What is the most efficient way to swap this techique?

Two cases:
1. Case #1 - same pass, but added shader logic to show "contour lines" as you zoom way in.
2. Case #2 - Want to toggle the pass between "alpha" and "base", and for the "base" pass shader, we would omit use of the "opacity" shader parameter.

What is the best way to toggle techniques on an object to make it most efficient for the CPU/GPU?

Options that I can think of:
1. One Material with advanced settings that allow you to programmatically tell the material which technique to use for rendering.
2. Multiple simple materials, and just assign the material dynamically.
3. One Material, but programmatically use "SetTechnique(..)" to set it's technique.

I'm leaning towards #3 right now, but figured there may be a better way to do it.

-------------------------

Lys0gen | 2020-12-27 00:47:02 UTC | #2

If your primary concern is getting rid of the **if** for performance you should simply use a *step* multiplication as a substitute.


	float trueValue = step(THRESHOLD, INPUT);// 1.0 if INPUT >= THRESHOLD
	useColor = falseColor * (1.0 - trueValue) + trueColor * trueValue;

"If"-checking more values like this is trivial by just adding more of these step multiplications.

If you actually need to swap out the entire material/technique I don't know what is best. You'd probably have to benchmark it yourself.

-------------------------

najak3d | 2020-12-27 01:04:42 UTC | #3

Lys0gen thanks for the response.  Since this is a pixel shader that covers the full-screen, I thought it would be best to remove the 'if' branches from the shader (which will be run for every pixel, every frame).

And for my Case #2 - it's also a matter of "pass", as I believe the "alpha" pass is extra expensive since it requires these passes to be sorted by "distance from camera" which can be costly for the CPU.   99% of the time these tiles are NOT transparent, and only need to be transparent when showing up or hiding (to prevent the abrupt blit, the fade is easier on the eyes and more polished).

-------------------------

Eugene | 2020-12-27 10:57:54 UTC | #4

You can set multiple techniques for Material based on distance, [see docs](https://urho3d.github.io/documentation/HEAD/_materials.html)

-------------------------

najak3d | 2020-12-27 18:43:54 UTC | #5

Eugene, I did see that.   It looks like those options will have issue, and will incur extra CPU-load per object.

It looks to me like I can't programmatically tell Urho which quality level to use on an object-by-object basis.... it's a "Renderer" setting.   And if I tell it to sort by distance, then I'm just giving Urho more-work-to-do (CPU) per frame by making it calculate Camera-Distance-to-each-object, and then sifting through the techniques.   I'm not sure how efficient Urho is at doing this.

ISSUE: I determine LOD for an entire group of tiles based on Camera Y-Position.   So when Y drops below 100, I want to change the Technique for 100 tiles all at once.   I'd prefer to not have Urho doing "distance math" for all 100 tiles every frame, to determine if I'm close enough -- PLUS -- that math will NOT do it consistently for all tiles at once.. because the tiles directly below the camera will be closer that those near to the edge of the screen... so Distance-based Technique Switching is bad, because the centered tiles will switch over before those at the edge, and this'll look funny, since it's one contiguous map.

If I opt for Quality-based switching, then I am limited to 3 quality levels (0 to 2) for all tiles... AND then lose the ability for users to toggle up/down the quality of rendering based upon their device specs.

===
So I think I need something different than both of those.   In the absence of alternate advice, I am considering just using the "SetTechnique()" for each object when the camera crosses that threshold.  So I make 100 calls at the Y-threshold, and then am done.   Does this sound efficient/reasonable? 

I think that may be a better approach than using "SetMaterial" to get the job done.

I can either call "Model.SetMaterial()" 100x for the switch, or "Material.SetTechnique()" 100x.

New Idea:
Currently each tile has it's own Material instance (clone).  I think this might be a case where I can assign the SAME material to all 100 objects.  And then, to switch the technique, it only requires ONE call to Material.SetTechnique().

EDIT:   New Idea won't work, at least not without added complexity.  Currently there are various raster tiles that overlay each other (e.g.. the more detailed city map overlays the lower-detail state map), and so I deal with this using "RenderOrder" (so I'd need to have at least one material per RenderOrder).

Then there is the matter of Fading In/Out -- which is another ShaderParameter, that is dynamically set upon Fading-in/out.    So it's not as simple as using one Material for all tiles.   At minimum, I'd need to have one material for each RenderOrder used, and a separate materials for batches of tiles as they fade in/out.   

I may still go this route, but it's not as simple as just having "one material for all tiles".

-------------------------

JTippetts1 | 2020-12-28 01:22:19 UTC | #6

[quote="najak3d, post:5, topic:6635"]
Eugene, I did see that. It looks like those options will have issue, and will incur extra CPU-load per object.
[/quote]

Have you profiled to see if its actually a problem, or is this a case of premature optimization? There is going to be CPU utilization in a task like this, so your best bet is to implement a solution and profile it to see if it will be acceptable.

-------------------------

najak3d | 2020-12-28 01:48:49 UTC | #7

JTippetts1, thanks!  I may tend to optimize prematurely.  But in general, I just like to design an approach that isn't wasteful.   By doing a reasonable amount of optimization as you go, you don't have to rework things later.  When you can reduce 150 materials down to 10 materials to manage, for not much extra work, it seems like a no-brainer.

We're working with .NET, which has a Garbage-Collector (GC), which has to do more work if there are more objects on the heap.   So reduction of object counts tends to be a good practice to eliminate the occasional hiccups that can happen if the GC takes too long.

Also, this'll be lower CPU load.   We modify Shader Parameters per-frame, for our throbbing effect.   So right off the bat, reducing 150 materials down to 10, reduces the "SetShaderParameter()" calls from 150 to 10, per frame, for this one throbbing effect.

So it seems to be a no-brainer, IMO, to do the "easy optimizations" upfront.   That's why I ask the questions now, so that I can make smarter upfront decisions, and save unnecessary headaches later-on.

-------------------------

