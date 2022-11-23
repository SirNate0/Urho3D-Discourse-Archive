JTippetts | 2018-01-13 21:01:32 UTC | #1

Some images as of Jan 2018
https://i.imgur.com/RjcaIK0.jpg
https://i.imgur.com/8kZEB4t.jpg

Some recent images:
https://i.imgur.com/ETnUnA0.jpg
https://i.imgur.com/K29Wt2D.jpg

Edit to the title as well; it suddenly wants a title to be 15 characters.

Edit:
Another recent image:

[url=http://i.imgur.com/UINbrwc.jpg][img]http://i.imgur.com/3VcNDYG.png[/img][/url]

Edit:
Updated with some recent images.
[url=http://i.imgur.com/RO6Bkky.jpg][img]http://i.imgur.com/F9Jytpo.png[/img][/url]
[url=http://i.imgur.com/xQgetsf.jpg][img]http://i.imgur.com/hU7ENNX.png[/img][/url]
[url=http://i.imgur.com/iZNy5j3.jpg][img]http://i.imgur.com/4hfXxPc.png[/img][/url]

While waiting for Azalrion to finish an overhaul of the DetourCrowd stuff scorvi proposed (wink wink, nudge nudge) I started working a little bit on a simple terrain editor for Urho3D. It's pretty basic right now, only a few hours into it mostly on weekends when I'm not working IRL. You can find it at [url=https://github.com/JTippetts/U3DTerrainEditor]this clicky right here[/url] if you are interested in running rough, unpolished code. It'll run from unmodified Urho3DPlayer if you like. Just copy the TerrainEditorData to the Bin directory and add it as a Resource Directory. (Disclaimer: not currently tested from a vanilla Urho3DPlayer; also not tested in OpenGL. If you try it and run into problems, let me know.) To run, execute the file LuaScripts/testterrainedit.lua. (Did I mention it requires Lua support to be built in?)

[url=http://i.imgur.com/yEUL4Bi.jpg][img]http://i.imgur.com/uZZmNsU.png[/img][/url]

Additionally, it comes with the framework code for an enhanced player app that includes built in support for the [url=https://code.google.com/p/accidental-noise-library/source/browse/?name=vm]vm branch of the Accidental Noise Library[/url] for noise function support.

The program supports a basic set of brushes: edit height, smooth height, 4 detail blend layers (using an enhanced version of the default TerrainBlend shader to support a detail layer in the alpha channel of the blend texture) masking and filters. The height editing is fairly reminiscent of the old Age of Mythology editor. It's serviceable, but the real power of a thing like this is in procedural support which is where the Filters come in, accessible via the toolbar menu.

[url=http://i.imgur.com/ggI2WmP.jpg][img]http://i.imgur.com/dJEAPiT.png[/img][/url]

Filters are implemented as Lua scripts held in a certain directory that is scanned at startup. They specify parameters that can be tweaked, and upon a press of the execute button will perform their scripted action.

[url=http://i.imgur.com/09TxRft.jpg][img]http://i.imgur.com/IyZCnRV.png[/img][/url]

So far, I've only implemented a small handful of test filters: one to Cliffify terrain (ie, set terrain to a cliff texture based upon its steepness), one to generate a fractal-based mottled pattern of dirt and grass and one to generate a generic fractal-based terrain with some tweakable parameters. As I refine this thing (and especially as I use it for other projects) that filter list is certain to grow. In order to use the included filters, the Urho3D player needs to be built with the ANL noise support.

[url=http://i.imgur.com/vPi0IP4.jpg][img]http://i.imgur.com/sk7OJhm.png[/img][/url]

The program is really very simple. An editor component is implemented as a script object (it'll probably be done as a C++ component very soon) exposing some methods for painting to the various layers, and a UI component instances the UI widgets and hooks them all up. The UI is currently VERY unpolished and will certainly change as time goes by. There are a few issues (such as changing filter parameters not being persistent between sessions at the filters window) but for the most part it is functional. As of the time of this initial posting, importing and exporting from PNGs is not fully supported; you can do an export of the terrain map by pressing 's' and the blend map by pressing 'd'. 'a' takes a screenshot. I'm working on the New Terrain and Import/Export dialogs pretty much as we speak, though.

Anyway, if you're interested take a look. It'll be a project I work on occasionally as I require features, but it won't be a main focus item (especially once Azalrion gets moving).

-------------------------

vivienneanthony | 2017-01-02 01:02:45 UTC | #2

I'm going follow this. It seems like its something I am trying to implement on a different level.

-------------------------

weitjong | 2017-01-02 01:02:45 UTC | #3

Cool. I will definetely take a closer look. At first glance I see your include dirs in the main CMakeLists.txt are still hardwired for Lua and tolua++. The latest Urho master branch already contains the changes you requested in Urho GitHub Issues sometime ago.

-------------------------

devrich | 2017-01-02 01:02:45 UTC | #4

This is Awesome! Many thanks for working on this  :smiley:

-------------------------

rogerdv | 2017-01-02 01:02:54 UTC | #5

Great! Why isnt it part of the official editor? Because it is written in Lua? Is there going to be texture painting?

-------------------------

JTippetts | 2017-01-02 01:02:55 UTC | #6

I had thought about writing it as part of the editor, but decided not to because:

a) The editor is getting pretty complex, and I have only the tiniest familiarity with AngelScript and no desire to plunge into that codebase to integrate it, and
b) I decided I preferred a standalone approach rather than further complicating the editor. The editor UI is getting quite 'busy' and I didn't really want to deal with all that just for simple height editing.

I've made a few recent commits. A quick hack to implement the basic editing tasks in C++ rather than Lua, for better performance. Modified the test filters to use the mask layer (toggled with a check flag). For example, you can paint an area with the mask tool:

[url=http://i.imgur.com/hSuldoa.jpg][img]http://i.imgur.com/s4g8N52.png[/img][/url]

then run the genericfbm fractal filter, with Use Mask selected, to apply the filter only to the masked area:

[url=http://i.imgur.com/kmp27w1.jpg][img]http://i.imgur.com/50U7f0e.png[/img][/url]

And the result is that the filter is applied only in the selected region:

[url=http://i.imgur.com/PTeTwiv.jpg][img]http://i.imgur.com/F4aclhe.png[/img][/url]

Currently in the works is the ability to select a brush that will add checkpoints, or waypoints, to a list as you click. Filters can access the checkpoint list to do tasks such as road-building, ie by interpolating the curve formed by the checkpoints and smoothing/raising/lowering the terrain along the curve. Or tasks such as interpreting the checkpoint list as a closed region and converting it to a mask. Stuff like that.

-------------------------

setzer22 | 2017-01-02 01:02:56 UTC | #7

THANK YOU! :smiley:

I heavily rely on terrains for my Project and this is editor is going to be a huge time saver!

-------------------------

rogerdv | 2017-01-02 01:02:57 UTC | #8

Aboutr the editor UI getting too crowded, I have been thinking to propose to separate editor functions like Torque does. Torque editor has different screens for different tools: one mode for UI editing, one for scene editing, one for terrain, and so on.

-------------------------

JTippetts | 2017-01-02 01:02:57 UTC | #9

I've been working on a draft of a Road Builder filter. The current waypoint system lacks a UI; you add waypoints with the W key and remove with the Q key. When I get to polish stage I'll add a real UI for it. The Road Builder filter requires at least 4 waypoints (to feed to a cubic spline). So once you have built a terrain, you use W to add a few waypoints:

[url=http://i.imgur.com/IE6DWJ2.jpg][img]http://i.imgur.com/UslVlyy.png[/img][/url]

The road builder filter gives you a few options to control things such as road width, fadeout distance of the road bed and paving texture, which detail texture layer to use for the paving, and the number of steps to tessellate each segment of the spline.

[url=http://i.imgur.com/PzHIuNb.jpg][img]http://i.imgur.com/6dDiYxa.png[/img][/url]

 After tweaking the parameters to your taste, hit execute and wait for a little while. (The procedure is currently non-optimized, requiring three rasterization passes.) And the result:

[url=http://i.imgur.com/5p1Y6Gt.jpg][img]http://i.imgur.com/cMsH1qE.png[/img][/url]

Grab the smooth brush and go to town on the rougher spots to make it nicer:

[url=http://i.imgur.com/4CjRDKm.jpg][img]http://i.imgur.com/1qk08D7.png[/img][/url]

Note that you do have to consider your waypoint placement carefully. The filter gets elevation heights at the spline knots (waypoints) and interpolates between them, so it will happily bridge and carve the hell out of things:

[url=http://i.imgur.com/2Mwllco.jpg][img]http://i.imgur.com/9E8SmTD.png[/img][/url]

Working on this brings back memories, as I am digging through my archives all the way back to [url=http://www.gamedev.net/blog/33/entry-600044-and-more-roads/]2005[/url] to a nearly identical project I was working on using a custom engine. Urho3D makes it a lot easier to add new features, though.

-------------------------

devrich | 2017-01-02 01:02:57 UTC | #10

Brilliant! :smiley:

Many thanks JTippetts for working on this ( i know i said that already but this is great! ) :smiley:

-------------------------

vivienneanthony | 2017-01-02 01:02:57 UTC | #11

Hello

How are you calculating the matterials? It is something I need badly. I'm looking all over the place. I'm not sure how to modify shaders code to do it with a procedural terrain.

Vivienne


[quote="JTippetts"]I've been working on a draft of a Road Builder filter. The current waypoint system lacks a UI; you add waypoints with the W key and remove with the Q key. When I get to polish stage I'll add a real UI for it. The Road Builder filter requires at least 4 waypoints (to feed to a cubic spline). So once you have built a terrain, you use W to add a few waypoints:

[url=http://i.imgur.com/IE6DWJ2.jpg][img]http://i.imgur.com/UslVlyy.png[/img][/url]

The road builder filter gives you a few options to control things such as road width, fadeout distance of the road bed and paving texture, which detail texture layer to use for the paving, and the number of steps to tessellate each segment of the spline.

[url=http://i.imgur.com/PzHIuNb.jpg][img]http://i.imgur.com/6dDiYxa.png[/img][/url]

 After tweaking the parameters to your taste, hit execute and wait for a little while. (The procedure is currently non-optimized, requiring three rasterization passes.) And the result:

[url=http://i.imgur.com/5p1Y6Gt.jpg][img]http://i.imgur.com/cMsH1qE.png[/img][/url]

Grab the smooth brush and go to town on the rougher spots to make it nicer:

[url=http://i.imgur.com/4CjRDKm.jpg][img]http://i.imgur.com/1qk08D7.png[/img][/url]

Note that you do have to consider your waypoint placement carefully. The filter gets elevation heights at the spline knots (waypoints) and interpolates between them, so it will happily bridge and carve the hell out of things:

[url=http://i.imgur.com/2Mwllco.jpg][img]http://i.imgur.com/9E8SmTD.png[/img][/url]

Working on this brings back memories, as I am digging through my archives all the way back to [url=http://www.gamedev.net/blog/33/entry-600044-and-more-roads/]2005[/url] to a nearly identical project I was working on using a custom engine. Urho3D makes it a lot easier to add new features, though.[/quote]

-------------------------

JTippetts | 2017-01-02 01:02:57 UTC | #12

The [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditorData/Materials/TerrainEdit.xml]material[/url] simply uses the [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditorData/Techniques/TerrainBlendEdit.xml]TerrainBlendEdit[/url] technique which is a slight modification of the default [url=https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Techniques/TerrainBlend.xml]TerrainBlend[/url] technique. The modifications I made to the shader can be seen [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditorData/Shaders/HLSL/TerrainBlend4Edit.hlsl]here[/url] and include 1) Adding a 4th detail texture, mapped by the alpha channel of the blend texture and 2) Adding visualization for the mask texture. If you do not need the mask, the [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditorData/Shaders/HLSL/TerrainBlend4.hlsl]TerrainBlend4[/url] shader includes only the 4th detail texture addition to the default TerrainBlend shader.

-------------------------

vivienneanthony | 2017-01-02 01:02:59 UTC | #13

[quote="JTippetts"]The [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditorData/Materials/TerrainEdit.xml]material[/url] simply uses the [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditorData/Techniques/TerrainBlendEdit.xml]TerrainBlendEdit[/url] technique which is a slight modification of the default [url=https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Techniques/TerrainBlend.xml]TerrainBlend[/url] technique. The modifications I made to the shader can be seen [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditorData/Shaders/HLSL/TerrainBlend4Edit.hlsl]here[/url] and include 1) Adding a 4th detail texture, mapped by the alpha channel of the blend texture and 2) Adding visualization for the mask texture. If you do not need the mask, the [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditorData/Shaders/HLSL/TerrainBlend4.hlsl]TerrainBlend4[/url] shader includes only the 4th detail texture addition to the default TerrainBlend shader.[/quote]

Ah. I just have to figure out how to convert the terrain to a RGB weightmap or convert the BG(bw) to RGB(rgba) weight map. It looks like it doesn't work by slope if I read it right (TerrainBlend4.). I might be wrong.

I found this thread.
[truevision3d.com/forums/prin ... pic=5652.0](http://www.truevision3d.com/forums/printpage.html;topic=5652.0)

Couldn't something like that be used to help create a slope based height?

I don't see anything in the HLSL shader that could be used to get height information from different points from geomotry?

-------------------------

JTippetts | 2017-01-02 01:03:00 UTC | #14

No, the shader doesn't work by slope. It doesn't work by elevation or any hard-coded rules. It doesn't need to; you can do all of that stuff outside the shader. It doesn't make much sense to do it inside the shader because 1) You might want to have some places where slope DOESN'T affect the detail texture and 2) Sampling the normal from the heightmap itself might result in an incorrect normal if you don't account for the values passed to Terrain::SetSpacing().

The shader merely uses the blend texture to determine what detail textures to draw for a given fragment; the contents of the blend texture are entirely up to you. You can set a texel in the blend map with a value derived from the slope of the terrain normal, or with one derived from the elevation, or with one derived from a noise function, or with one derived from the phase of the moon. It doesn't matter how you generate the blend values.

For example, look at how the [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/Bin/TerrainEditFilters/cliffify.lua]cliffify[/url] filter works. It iterates on x and y through the image associated with the blend texture, and for each texel it calculates the World coordinates of the respective location, and uses those world coordinates to query the Terrain directly for the normal at that location. A simple dot product with the vertical vector (and some additional calculation to apply cutoff and fade values) and the result is a value that can be used to Lerp between whatever color is already in the blend texture and the color representing the detail layer for cliff texture. And just like that, you have cliffs. No monkeying with the shader itself is necessary.

-------------------------

vivienneanthony | 2018-01-29 15:39:58 UTC | #15

Hello

I kinda get what you are saying. Thanks for your information.

I find these two links online. Are they good examples of what you mean Dot and Lerp?

Vivienne

Lerp is bassically [keithmaggio.wordpress.com/2011/ ... and-nlerp/](https://keithmaggio.wordpress.com/2011/02/15/math-magician-lerp-slerp-and-nlerp/)
Dot product concept [rosettacode.org/wiki/Dot_product](http://rosettacode.org/wiki/Dot_product)

-------------------------

JTippetts | 2017-01-02 01:03:01 UTC | #16

Sure, those look about right.

The purpose of the dot product is to determine how steep the terrain is. If you take the dot product of the terrain normal and the vector representing "UP" the result is the cosine of the angle between the vectors (assuming both vectors are of length 1, or unit length). So if the normal is parallel with UP, the dot product will equal 1 ( or cosine(0)) whereas if the normal is perpendicular to UP, the dot product will be equal to 0 (cosine(90)). Thus, the dot product gives you a good function for "steepness" of terrain. As the terrain gets steeper, the dot product gets closer to 0.

Now, with this dot product in hand you are able to use it to interpolate (lerp) between colors. The most basic operation would be to use it as-is, but that doesn't necessarily get you a good cliff. That gets the cliff texture spread across the entire continuum of normals, lighter on the more horizontal spots and fading in gradually to full cliff at the vertical spots. So instead, I apply some math to specify a threshold cutoff. Any slope below this threshold gets no cliff terrain blended in. Anything above the cutoff gets full cliff. I also specify a fade value that lets me gradually fade from cliff to non-cliff in a narrow band centered on the cutoff threshold. This softens the cutoff as desired.

If Use Mask is enabled for the cliffify filter, then I can scale the final Cliff value with the mask value, enabling me to mask out places where I don't want there to be cliff even if the terrain is steep enough for it.

-------------------------

vivienneanthony | 2018-01-29 15:39:17 UTC | #17

I did this code so far. I'm just not sure about if I should be doing per vertices.
[code]
float cutoff(float inputvalue, float pointmid, float range)
{

    /// Create valuables to calculate
    float midpoint=pointmid;

    float midpoint_low=midpoint-range;
    float midpoint_max=midpoint+range;

    float midpoint_range;
    float result;

    if(midpoint_low<0){ midpoint_low=0;}

    if(midpoint_max>1){midpoint_max=1;}

    midpoint_range=midpoint_max-midpoint_low;

    /// Calculate value to range

    if(inputvalue<midpoint_low)
    {
        result=0;
    }
    else if(inputvalue>midpoint_max)
    {
        result=1;
    }
    else
    {
        result=(inputvalue-midpoint_low)/midpoint_range;
    }

    return result;
}

int main()
{

    /// Get terrain size
    IntVector2 terrainSizeV2 = terrain-> GetNumVertices ();
    Vector3 terrainSize;
    
    terrainSize.x_= terrainSizeV2.x_;
    terrainSize.y_= terrainSizeV2.y_;
    
    
    /// loop vertices
    for(ix=0; ix<terrainSize.x_; ix++)
    {
        for(iy=0; iy<terrainSize.y_; iy++)
        {
            /// get steepness
            Vector3 normalvalue=terrain ->GetNormal(worldposition);
            float steep=math.abs(normalvalue.DotProduct(Vector3(0,1,0)));

                                 float percentlerp=cutuff(steep,.5,.2);
                                 
                                 
            /// Choose between material, blend, color. Not sure yet.
             }
       }

      return 1;
}

[/code]

-------------------------

JTippetts | 2017-01-02 01:03:01 UTC | #18

There is no restriction that the blend texture be the same resolution as the heightmap texture. In fact, you probably get a better visual result (in my opinion) if you use a blend texture with a larger resolution than the heightmap. So rather than iterate on the heightmap size, you'll want to iterate on the blend map size. If you do that, though, then you will need a way to convert the blend map coordinate to an actual real-world location in order to get the terrain normal. For this, I wrote the [url=https://github.com/JTippetts/U3DTerrainEditor/blob/master/TerrainEdit.cpp#L21]NormalizedToWorld()[/url] function which takes a pair of coordinates in the range 0 to 1 and converts them to a world location. The function directly rips off the way the Terrain component internally does it. To use, simply divide the blend map pixel coordinate by the image dimensions (to get the normalized coordinates) then pass to the NormalizedToWorld() function to obtain world coordinates.

(Converting between spaces like this is about the trickiest part. In the editor, the heightmap blend map and mask can all have different resolutions, so I am constantly converting. Luckily, the Image class makes sampling from other spaces easy with the GetPixelBilinear() method, which takes normalized input coords to start with.)

-------------------------

vivienneanthony | 2018-01-29 15:40:23 UTC | #19

I used your code a little then I'm going add my function.. The code I put was. You can tell me if its correct so far. I put [b]steepness = 1-[/b]  so 0 can the flatter and 1 would be the highest steepness.

Does that make any sense?

[code]
    /// Testing
    float bw=2048.0f;
    float bh=2048.0f;
    float x=1024.0f;
    float y=1024.0f;

    /// Get steepness
    Vector2 nworld=Vector2(x/bw, y/bh);
    Vector3 worldvalue=NormalizedToWorld( producedHeightMapImage,terrain,nworld);
    Vector3 normalvalue=terrain ->GetNormal(Vector3(wordvalue));
    float steep=1.0f -abs(normalvalue.DotProduct(Vector3(0,1,0)));

    cout << steep << " "<< normalvalue.x_<< " " << normalvalue.y_ << " " << normalvalue.z_;
[/code]

-------------------------

JTippetts | 2017-01-02 01:03:10 UTC | #20

[url=http://i.imgur.com/R8tSoEN.jpg][img]http://i.imgur.com/kVMfKe7.png[/img][/url]

I've gotten some performance issues worked out, so I've started working on the TODO list to start polishing this thing. Things on the TODO list include a UI revamp, a modal option to switch to a first person view to explore the map from the ground, a revamp of the filter options to include a slider option type, implementation of a Navigation mesh test so that you can see how navigable the heightmap is (This option will construct a navmesh and display its debug geometry as a partially transparent overlay so that you can see areas of movability and make any necessary changes), implementation of a preview mode for waypoint line lists plus a UI and editing options for waypoints (ability to drag waypoints around, etc... and a preview mode that shows the waypoint linelist/curve as a partially transparent ribbon, updated in real time as waypoints are added or moved; this should help visualize roads better as they are built), real file save/load dialogs so I can quit using hotkeys, a real New Terrain dialog with appropriate options. And a few other things.

-------------------------

vivienneanthony | 2018-01-29 15:40:58 UTC | #21

How did you avoid the repeated texture look for the cliffs?

I found this link. [forum.unity3d.com/threads/improv ... ng.116509/](http://forum.unity3d.com/threads/improved-terrain-texture-tiling.116509/)

I'm not sure if something like that can be implemented.

-------------------------

JTippetts | 2017-01-02 01:03:10 UTC | #22

I didn't do anything in particular to avoid repetition; the repetition is there if you look closely enough.

Something like what the link you posted is definitely possible, if you're okay with the additional texture sampling and instruction count. I'm not sure I would advocate the exact method they use, though, of multiplying the detail texture against a larger version of itself. That tends to over-saturate the texture, as in this shot: [url=http://i.imgur.com/Aic7x7B.jpg][img]http://i.imgur.com/obydfdn.png[/img][/url]

Instead, I would think that a simple 50/50 blend (sum them together and multiply by 0.5) would be more appropriate, as it would at least conserve the overall coloration of the texture: [url=http://i.imgur.com/pwhaCse.jpg][img]http://i.imgur.com/Enbp0Rw.png[/img][/url]

And, of course, the results would vary depending on the texture itself. For instance, that rock texture doesn't really work that well, but a more "natural" stone texture would probably look pretty good.

-------------------------

JTippetts | 2017-01-02 01:03:12 UTC | #23

So in the interest of procrastinating all of the boring TODO items delineated above, today I went ahead and took a stab at an experiment to implement the texture packing detailed [url=http://udn.epicgames.com/Three/TerrainAdvancedTextures.html#Texture%20Packing:%20Implementing%20large%20texture%20tile%20sets]here[/url]. My thinking was "if 4 terrain types is the bare minimum I need, then surely 8 types would be even better!" So I wrote a shader (HLSL only for now, I'll do a GLSL in a little while). This shader implements both the ability to use 8 types (drawn from 2 composite textures each containing 2x2 types) as well as the extra-detail tiling reduction from earlier. It's a first stab which simply scales the fractional part by 0.5 and adds 0.5 offsets depending on type, so it does nothing to eliminate the 1 pixel wide "border" at texture seams caused by bilinear sampling. That fix should be relatively easy to make, though, and I just wanted to get this going as a proof of concept.

Ideally, I'd like the user to be able to specify which terrain blending scheme they would like to use: 3 types, 4 types or 8 types. I could do a 12 types version (the 8 types actually reduces the number of detail textures by 2, freeing up 2 slots that I could use for another composite texture + blend map) but already it's getting kind of heavyweight, at least for my modest little machine from Costco. It's still interactive framerates, though, so I reckon a 12 type shader would be doable at some point. If I find it necessary, that is, because really 8 types is quite a bit and allows for a decent amount of variety.

Anyway, here is a quick screenshot of it in action: [url=http://i.imgur.com/8APnFgV.jpg][img]http://i.imgur.com/dTDs4yB.png[/img][/url]

-------------------------

szamq | 2017-01-02 01:03:13 UTC | #24

Nice! looks like we have great tool here. 8 or 12 different textures is very much, I wonder if it would be possible to trade of some of the diffuse textures to normal map textures, each one for different type of terrain.

-------------------------

rogerdv | 2017-01-02 01:03:13 UTC | #25

For hughe terrains, 12 textures is not too much. But I would also like to have 12 textures with their corresponding normal maps.

-------------------------

JTippetts | 2017-01-02 01:03:13 UTC | #26

Depending on how many detail textures you want to pack into a single texture, you could probably do 12 detail+normal maps. (AFAIK, anyway. I don't know about instruction counts.) But holy shit, that would bring my poor compy to its knees.

I could probably pull off 4 detail+4 normal. 8 detail+normal would be pushing it performance-wise for me (again: Costco computer). I am kind of curious now, though. Let me scrap together some detail textures with normal maps and a shader and see how it goes.

-------------------------

JTippetts | 2017-01-02 01:03:13 UTC | #27

So, I did a quick hack version with 8 detail+normal (Crappy Gimp plug-in produced normals, rather than "real" normals, so pardon the shitty appearance.).

[url=http://i.imgur.com/POqKMj1.jpg][img]http://i.imgur.com/09nVeYY.png[/img][/url]

It actually doesn't bring my compy to its knees nearly as bad as I was expecting. However, that bleeding border problem is kind of a tough one. The UDK article wasn't really lying when they said that this method was fairly limited in where it should be used. There is always going to be some border bleeding at different mip levels, no matter what kind of offset and shrinking you do. The normal mapping only seems to compound the problem in some instances. I could see maybe using separate textures for the detail color and a packed texture for the normal map, though; at least then you wouldn't get any color bleeding.

-------------------------

friesencr | 2018-01-29 15:44:35 UTC | #28

I was working on implementing texture array; it has opengl extension support and has good support. If people don't have that I was going to let them suffer mip map bleeding.   I am also going to implement padding fills on my sprite packer.

[github.com/urho3d/Urho3D/pull/481](https://github.com/urho3d/Urho3D/pull/481)

The fills will be mirror/reverse/copy nearest pixel.  With a generous padding and texture lookup offets I was hoping it would be decent.

-------------------------

JTippetts | 2017-01-02 01:03:13 UTC | #29

This little tangent has served as a reminder of why I don't usually do (or play) games with heightmapped terrains... Getting a good result is pretty tough.

-------------------------

friesencr | 2017-01-02 01:03:13 UTC | #30

[quote="JTippetts"]This little tangent has served as a reminder of why I don't usually do (or play) games with heightmapped terrains... Getting a good result is pretty tough.[/quote]

I am pretending to write an rts right now and havn't gotten the performance out of tilemaps when the camera tilts and to the horizon and picks up all those drawables.  The heightmap performed well but I havn't gotten anywhere near the quality of art from it I want.  I do think there is a lot of value for something like this.  A newcomer can make a terrain, add a character controller, start running around,  and can take joy in it and make further steps in their gamedeving.

-------------------------

JTippetts | 2017-01-02 01:03:14 UTC | #31

Here is another little experiment:

[url=http://i.imgur.com/DLCoPY9.jpg][img]http://i.imgur.com/jJPttVC.png[/img][/url]

This one simply implements a whole-terrain colormap and a set of 8 detail normal map textures. Painting with a terrain paints random speckles of color into the colormap and blends in detail from the normal maps. It's not exactly a photorealistic technique, but I think that with good color selection and better normalmaps than these crappy filter-generated things, it could produce some pretty interesting results.

-------------------------

JTippetts | 2017-01-02 01:03:14 UTC | #32

Alright, that was a fun tangent but back to work. I've switched back to the original 4-detail no-normal material, since right now it still looks the best without any cracks or seams.
[url=http://i.imgur.com/QAqdghg.jpg][img]http://i.imgur.com/jUl9fZ6.png[/img][/url]

That actually looks like a map I could have fun exploring, I think.

I've encountered some occasional bugs in the road tool, so I need to add that onto the TODO list. I'll probably just move the quad-strip rasterization into C++ anyway, since any kind of "inner loop" construct that does mass data moving (iterating a buffer and setting pixels, etc...) should probably be streamlined. At some point, I might revisit the method for turning a line list into a quadstrip as well, to see if I can smooth out some of the artifacts.

In the road tool, I've been using the Green and Blue channels of the mask image as a scratch-pad of sorts, but I might want to rethink that and use dedicated buffer objects based on float instead. Using image channels forces a conversion to unsigned char, so I lose detail when I rasterize the road strips. After I run the road builder, I have to go back with a smooth brush and polish off the stair-steps and sharp edges. I'd probably get much better performance due (given all of the buffer clearing and iterating the tool does) so that will probably be my project for today until I have to go to work.

I've been sketching (on paper, old skewl style!) some ideas for the improved UI. If I decide to support the various kinds of materials I have been tinkering with, then I'll probably want to figure out a way of handling the various types of terrain paint palettes elegantly. If I support the color+detail normals material, then I'll probably need to do a color chooser UI widget as well.

-------------------------

rogerdv | 2017-01-02 01:03:14 UTC | #33

I know its a bit early to ask this, but there is going to be a binary release? Im having troubles to compile Lua support and cant test this tool in my PCs.

-------------------------

JTippetts | 2017-01-02 01:03:22 UTC | #34

In order to continue with procrastinating the UI polish, I started work on a river builder tool. It is a slight modification of the road builder, one that limits elevation changes so that they only proceed downhill from the start of the waypoint chain. While tweaking and fiddling with it, I ran up against several instances of bugs in the curve tessellation/quadstrip construction code. The curves use cubic spline interpolation to ensure that the curve passes through the control points, but the result of this can sometimes be a little bit dodgy. And when you combine a dodgily constructed curve with a quadstrip production routine, the result (of course) is dodgy quadstrips that can result in some pretty hideous degenerate faces. So in order that I not hit that Execute button on a road/river filter blindly, I constructed a custom geometry widget that shows a preview of the waypoint curve as an alpha-blended strip overlaid with no depth testing on the scene. This way you can tweak the curve until any degeneracy is gone before hitting Execute on a filter. Some images:

[url=http://i.imgur.com/KsEH8DB.jpg][img]http://i.imgur.com/GlnqSFQ.png[/img][/url]
[url=http://i.imgur.com/3KcoBSN.jpg][img]http://i.imgur.com/Q26oaJN.png[/img][/url]

This push, I also started moving the curve tessellation and rasterization into C++ for a quite significant speedup. It's still a relatively heavy operation, especially on a 2049x2049 heightmap, but is much faster than it was before.

Edit: I also did some minor tweaks to the camera to enable you to better see what the terrain is going to look like from ground level:

[url=http://i.imgur.com/oYpo4Ik.jpg][img]http://i.imgur.com/kvgE8NM.png[/img][/url]

You can use the Right mouse button to drag the scene, and while the scene is dragging the looked-at point will follow the surface of the terrain with a small vertical offset. Mouse wheel up will zoom in, and you can zoom all the way in then use Middle mouse button to spin the view around, up and down. Zoom back out to get to editing perspective. (editing is still possible in this 'first person' view, but difficult due to the cursor following elevation.)

rogerdv: I don't really want to encumber the git repo with a binary exe, but maybe I can upload one to google drive and share it with you or something. What is your problem with building Lua support, if I might ask?

-------------------------

JTippetts | 2017-01-02 01:03:48 UTC | #35

Lately I've been split between a few different projects: working on a game I had sort of laid aside for awhile, playing Divinity: Original Sin, fixing some long-standing issues in the Accidental Noise Library, and working on porting the noise and terrain editing stuff to AngelScript bindings. It might be more appropriate to build this terrain tool for AngelScript, given that the official editor is AS. I don't really like AS, though, so it's been slow going.

A couple hours ago, I stumbled across a thread on gamedev.net that reminded me of [url=http://www.gamedev.net/page/resources/_/technical/graphics-programming-and-theory/advanced-terrain-texture-splatting-r3287]this[/url] terrain texturing technique. I remember seeing this one some years ago and thinking it looked neat. So this morning I put together a quick shader test to see how it works.

Regular blending:
[url=http://i.imgur.com/3gOB2cz.jpg][img]http://i.imgur.com/prGZNM1.png[/img][/url]

Using the depth blending technique:
[url=http://i.imgur.com/e0HpNU0.jpg][img]http://i.imgur.com/MoHiFtX.png[/img][/url]

Even with throwaway depth channels in the textures (simple noise fractals of varying frequencies), the result looks pretty okay. With correct depth channels, the results can be very nice, much nicer than generic gradient blends. Of course, this technique complicates the texture creation process somewhat, as you now have to create image-appropriate depth maps for the textures. (Of course, if you own CrazyBump then it's not that big a deal, I understand. I don't own it, however... yet.) This afternoon, I'll try to create some better textures in Blender and see how I like it then.

Edit:
Ooh, an unanticipated benefit of having the depth map in alpha channel means you can get bump-mapping "for free" (some terms and conditions may apply, see store for details) without having to provide a normal map.

Without bump:
[url=http://i.imgur.com/9jgl3K5.jpg][img]http://i.imgur.com/Eh3kyu1.png[/img][/url]

With:
[url=http://i.imgur.com/Z65vq4X.jpg][img]http://i.imgur.com/aouVdBd.png[/img][/url]

Again, the textures are quickies (heightmap from luminance of texture this time around), but even so the effect is fairly nice.

-------------------------

szamq | 2017-01-02 01:03:49 UTC | #36

The new texturing technique looks awesome, it makes the terrain look not repeating

-------------------------

codingmonkey | 2017-01-02 01:03:49 UTC | #37

Yeah, good work )
Earlier i was trying to run editor but not understand how it must start running. 
Or how i'm must merge it with urho master for running.

-------------------------

JTippetts | 2017-01-02 01:03:50 UTC | #38

The project as it stands isn't really meant to be merged with Urho3D master. Rather, it is set up as a project that uses Urho3D as an external library. The root CMakeLists.txt expects URHO3D_HOME to be set, and will build a stand-alone .EXE much like the vanilla Urho3DPlayer.exe, with some modifications. The modifications are: 1) The inclusion of the stuff in TerrainEdit.cpp as well as the Lua bindings for it in BindTerrainEdit.cpp that expose these utility functions to Lua, and 2) The inclusion of the VM branch of my [url=https://code.google.com/p/accidental-noise-library/source/browse/?name=vm]noise library[/url] along with a set of bindings for Lua to make it accessible. Without these modifications it won't work, so the vanilla Urho3DPlayer.exe is no longer sufficient to run it. I update my Urho3D to head quite frequently, so you'll probably need to grab the latest from git to use, rather than building against 1.32. (I haven't tested a build against 1.32 so it might work, it might not.)

Building is done per [url=http://urho3d.github.io/documentation/HEAD/_using_library.html]the docs[/url]. Note that Lua support must be enabled. Once built, change to the root directory (the one with CoreData, Data and TerrainEditorData, of course) and execute [b]TEdit.exe LuaScripts/terraineditor.lua[/b]. The .exe accepts all of the default command line parameters.

Once running, the program creates a default terrain 2049x2049 with associated blend texture and mask texture. It sets up a rudimentary UI with a toolbar. Choose from Edit Height (to apply elevation), Smooth Height, 8 different Terrains (only 4 enabled for the currently set shader), Edit Mask and Filter. If you choose a brush tool (Edit Height, Smooth, Terrains, Edit Mask) then you are presented with a widget and sliders allowing you to adjust certain parameters.

For Edit Height, you can set Power (strength of the brush applied per update), radius (size), max (maximum elevation value the brush tends toward) and hardness (the "fuzziness" of the brush). Other brushes have similar options. Left click to apply a brush, "painting" with the current tool. The brushes are applied iteratively each update, with the strength set by Power. A lower power results in a more gradual application of the brush. When you are in Edit Height, you can also CTRL+Left Click on the terrain to select the elevation at the cursor.

Brushes are applied at the floating white fuzzy dot cursor. The mouse cursor is projected against the 0 plane, then the white dot is adjusted to the elevation around the projected location. This is necessary, because if you allow terrain editing at the mouse cursor itself then elevation tends to build or grow toward the viewer, making it difficult to build hills that aren't long, weird globs extending toward the camera unless you spin the camera to directly overhead.

Anything that is not a brush (waypoint adding, height selecting) is done at the mouse cursor itself.

To move the view (panning) you can either move the cursor near the edges of the screen to pan in that direction, or right-click and hold somewhere on the terrain and drag to move. Note that dragging will cause the camera look-at point to track the surface of the terrain. You can zoom in/out using the mouse wheel. Zooming all the way in will place you at an approximate first-person viewpoint so you can see what things look like from the ground. To spin the view, hold the middle mouse button and move up/down to alter pitch, left/right to spin around the view center. Pitch is constrained to +/-89 degrees to keep weirdness from happening if the camera goes fully vertical. Spin is unlimited.

Click on the Filters button to display a list of filters. Filters are scanned from the Bin/TerrainEditFilters folder as Lua scripts. The scripts take a particular format. They simply return a table that has 4 members: name (the display name for the options window), description (a textual description of the filter), options (a table of options) and execute(the function that executes the filter).

You can use the 'w' key to add a waypoint and the 'q' key to remove a waypoint. After at least 4 waypoints are created, a translucent blue ribbon will appear linking the waypoints as a representation of the Catmull-Rom spline between the knots. The filters Road Builder v2.0 (use this one, rather than v1.0) and River Builder 1.0 require at least 4 waypoints.

Currently, there are only a small handful of rudimentary filters: Cliffify (scan the terrain testing slopes and applying a cliff terrain to steep areas), Perlin Fractal Terrain Types (iterate the terrain and set grass to areas determined by a noise fractal), Generic Perlin Terrain (iterate the terrain, setting heights from a customizable Perlin noise fractal), Road Builder v2.0 (create a road from a list of waypoints) and River Builder 1.0 (create a river bed from waypoints). The remaining filters can be safely ignored. (Some debug stuff, some useless cruft.)  Note that the Filter window is a lying bastard. It has a Close button, but that button does nothing. You have to click Filter- on the toolbar again to close the window.

You can take a screenshot using 'a'. You can quicksave the current terrain with 's' and the current blend texture with 'd'. You can quickload a previously saved terrain texture with 'k' and blend texture with 'l'.

All of this stuff is testing code. Nothing here is final. Right now, I'm thrashing around with technical stuff rather than usability, so things can/will change all the time. At some point, I WILL do a UI push to clean things up, add widgets for things that need them, etc... But in the meantime, it's not really user-friendly.

You can choose the Edit Mask brush to apply mask to areas. Masking works as a gradient from 0 to 1. Some filters can have an option to use the mask for applying the filter, meaning that anyplace that is covered by the mask will not be affected by the filter, or will be affected only to a certain degree based on the strength of the mask. Similarly, the editing brushes can elect to use the mask, meaning that the brush will be applied based on the inverse strength of the mask. Mask areas can be cleared by setting the mask Max to 0 and applying the brush. Future iterations will provide support for generating a mask from a region defined by a set of waypoints, from noise fractals, and so forth.

Workflow:

On a large terrain such as 2049x2049, the individual brushes really aren't all that useful for large features. The radii of the brushes are maxed small to avoid large performance hits while editing. You could probably tweak the radius values in the UI if you like, but the fact remains that when it comes to creating large terrains, hand brushes are non-optimal. My workflow tends to prefer procedural stuff to fill in the meat of a map, and hand-editing for the details. So when I open up the editor and am faced with a new terrain, my first action is usually to go right to Filters->Generic Perlin Terrain to fill in the map with some stuff. Then I'll use height editing to smooth out and prepare locations for things I might want to add later: castles, houses, and so forth. My next step is usually to place rivers across the terrain, with an eye toward following valleys for a more natural feel. After that, I'll add roads. The final stage is the cliffify tool to set cliffs. Since Undo functionality is not supported, save often. Note that there is a glitch in the road builder that causes terrain at the first and last endpoints of the quadstrip to be sunken below grade; I usually have to smooth roads out with the smooth brush anyway, but it's something I'll have to track down at some point.

I do plan on allowing you to choose from a range of materials for the editor. The bump-mapped and height-scaled shader in the current iteration is a tad heavy-weight for my poor compy, resulting in an average framerate of about 26. (Mostly due to the bump-mapping, which adds a lot of additional texture samples to the shader.) I probably won't do any shader finalizing until the rumored upcoming refactor of the shader texture ordering is merged into master.

-------------------------

codingmonkey | 2017-01-02 01:03:51 UTC | #39

Thank you for detail instructions )
I got it to run. truth on vc2008 were errors associated with std: isnan; std::isinf ; std::ceil - functions(i guess that vs2008 have this fn in other headers and namespaces). so I had to compile both(engine and then your terrain-editor) under vs2013. 
On vs2013 project compiles without problems with the last Urho-master.
I play a bit, it's very cool! But the generators (filters) are very slow, it's probably because that they are written in the script ?
I have a small question: how to use the saved landscape in Urho-engine? To do this, perhaps we need something extra copy of shaders, materials or something else from tarrain-editor to urho-master ?

-------------------------

JTippetts | 2017-01-02 01:03:52 UTC | #40

It's slow mostly because it's using a single core of the CPU to evaluate a noise function that is a combination of 2 6-octave perlin noises across a domain that is 2049x2049 in size. Noise is an ideal candidate for the massive parallelization that GPUs offer, but that is a rabbit hole I have yet to go down.

The isnan, isinf stuff was debug cruft left in there from a time when I was tracking down a bug. I can take it out.

The saved landscape and blend should be usable in vanilla Urho3D TerrainBlend shader, as long as you don't use the Terrain 4 layer. The vanilla shader only uses 3 detail textures and the RGB channels of the blend texture. Otherwise, you can copy the shader from the TerrainEditData folder. The currently active iteration uses the TerrainEdit.xml material in TerrainEditData/Materials. This material references the technique TerrainBlend4BumpEdit. This technique references the shader TerrainBlend4EditDetailHeight.hlsl (HLSL version only available right now.) It's kind of a mess at the moment. Once the shader merge happens in master that cadaver has talked about, then I'll rewrite the shaders (probably as one or two uber shaders with #ifdefs, rather than the current approach of multiple shaders). If you want to use the shader in-game, you can use the TerrainBlend4Bump technique. In the newly updated github, the shader has been updated with #ifdef constructs for the mask texture sampling and blend, so that by simply not defining USEMASKTEXTURE in the technique you can exclude those parts. Similarly with the bumpmapping. If you don't want the bump mapping, just remove the BUMPMAP defines from the technique definition. (I know that I get a noticeable speedup when I undef the bumpmapping, since bumpmapping adds another2  samples per terrain layer. Also, I modified the bumpmapping in the current git version to do only 2 extra samples per layer instead of the 4 I had previously; you might want to update.)

I do apologize for the messy state of things. Like I said, I'm thrashing around on technical details and usability is still a more distant goal. As a matter of fact, my project for today (kids allowing) is to revisit the 8+ detail texturing I was experimenting with before, to try to eliminate the seam artifacts. I really, really would like to have more than 4 detail textures available, even if bumpmapping on 8 or 12 or 16 of them would make my poor graphics card cry.

-------------------------

JTippetts | 2017-01-02 01:03:52 UTC | #41

Okay, this morning I was able to re-implement the 8-detail texture technique, with bump-mapping, and eliminate the seams. And although there is a noticeable slowdown on my compy, while editing I'm still getting about 26 fps with 2 directional lights. So this is good.

Some years ago, I had bookmarked [gamedev.net/blog/73/entry-16 ... explained/](http://www.gamedev.net/blog/73/entry-1692117-terrain-texturing-explained/) and ran across it again while browsing my bookmarks a few days ago. It pretty much sums up the method I used today for seam-elimination.

First, I wrote a Lua routine to hand-build the mipmap levels for a composite texture by specifying 4 base textures. I hand build them so that when they are downsampled, I downsample each texture individually then pack them together for the composite, rather than the default behavior of downsampling the packed texture as a whole. This way, when the texture is downsampled it doesn't "bleed" pixels between tile types.

The shader routine described by Ysaneya in the link above then calculates the mip level manually, and adjusts the scaling of the sampled texture area dynamically based on the mip level, rather than fudging it with a constant based on the 0 level pixel size as my previous version was doing. This means that whatever the mip level, the tile area is "shrunk" by one pixel on each border, ensuring that filtering does not occur across tile boundaries. And the seams are gone.

[url=http://i.imgur.com/tkYqKab.jpg][img]http://i.imgur.com/8PbAVED.png[/img][/url]

I am quite happy with the result. The one blip I have is that the calculation of blending factors using the local depthmap for each terrain type can sometimes result in "bleeding" of adjacent terrain types into their neighbors. But it is an organic bleeding that looks relatively natural, and is a consequence of the fact that even if a particular terrain type is 0 in the blend map, that terrain type becomes 0+depth in the blend, and if the terrain type's 0+depth is greater than its neighbor's blend+depth then that texture will bleed through. In the shader, I calculate the contribution of a particular detail type as a blend between it and its neighbor, then I calculate the blend between these blended pairs, and yet another blend between these blends of blended pairs (an exponential lerp chain, in other words). So if Type A is first blended with Type B, then anywhere that 0+TypeADepth is greater than TypeBBlend+TypeBDepth will result in a contribution from Type A at that pixel even though TypeABlend was equal to 0. This results in the random-ish scattering of different terrain pixels you can see in the above image, especially at the fringes of a swatch of terrain where its blend value decreases toward 0.

Even with that glitch, though, the terrain looks good to me. I especially like that it gives me no seams now, no matter the view distance.

-------------------------

JTippetts | 2017-01-02 01:03:56 UTC | #42

I updated the first post to show some of the recent images:

[url=http://i.imgur.com/RO6Bkky.jpg][img]http://i.imgur.com/F9Jytpo.png[/img][/url]
[url=http://i.imgur.com/xQgetsf.jpg][img]http://i.imgur.com/hU7ENNX.png[/img][/url]
[url=http://i.imgur.com/iZNy5j3.jpg][img]http://i.imgur.com/4hfXxPc.png[/img][/url]

I am really liking that new terrain type blending scheme. Rather than ugly gradual fades from one type to the next you get a nice transition where it seems like stones are covered in grass, grass is growing on dirt, etc... Looks pretty cool, even with these cruddy textures. And it's super nice having 8 terrain types. The scheme could easily be extended to 12 or more, but I'm good with 8 for now.

Did some tweaking on the shader. Turns out, I don't need to manually generate my mipmap levels. The default mip generation works just fine. I've altered the filters to take advantage of the new texturing scheme, and removed some of the cruft. There are still a lot of things I need to do to clean it up, though. But I feel like I am getting to a point where I can start doing that cleanup. I have a pretty good handle on how I want this thing to operate, and I'm pretty happy with this texturing scheme.

-------------------------

rogerdv | 2017-01-02 01:03:58 UTC | #43

Im getting an error when compilong under linux. I do cmake . and then make:

[code]roger@gaara ~/projects/U3DTerrainEditor $ make
[ 42%] Built target ANLVM
Scanning dependencies of target TEdit
[ 50%] Building CXX object CMakeFiles/TEdit.dir/bind_anl.cpp.o
In file included from /home/roger/projects/U3DTerrainEditor/bind_anl.cpp:11:0:
/home/roger/projects/Urho3D/include/Urho3D/ThirdParty/toluapp/tolua++.h:45:17: fatal error: lua.h: No such file or directory
 #include "lua.h"
                 ^
compilation terminated.[/code]

-------------------------

JTippetts | 2017-01-02 01:03:58 UTC | #44

I'm not really the best one to ask for building advice. Especially on Linux, since it's been years since I last used Linux. But for the sake of thoroughness:

1) Make sure URHO3D_HOME is set, and points to the proper location
2) Make sure Lua support is enabled in both this project and the Urho3D library.

Seeing your actual cmake invokation and what defines you specify for both the library and the terrain editor would be a help.

-------------------------

rogerdv | 2017-01-02 01:03:58 UTC | #45

The variable is set, and Urho3D has Lua support (luajit, actually), the build command is:

[code] ~/projects/Urho3D -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DURHO3D_LUAJIT=1[/code]

Do I have to use the Urho build scripts to compile the terrain editor?

-------------------------

JTippetts | 2017-01-02 01:03:58 UTC | #46

You need to use the included CMakeLists and pass it the same defines that you pass to build Urho3D.

One note, though, is that I have not yet written any of the shaders for GLSL, so it's not going to work on Linux with OpenGL. That is a project for a future date, I'm afraid.

-------------------------

devrich | 2017-01-02 01:04:19 UTC | #47

[quote="JTippetts"]One note, though, is that I have not yet written any of the shaders for GLSL, so it's not going to work on Linux with OpenGL. That is a project for a future date, I'm afraid.[/quote]

 :cry: 

Please?  *angel smilie goes here *

-------------------------

vivienneanthony | 2018-01-29 15:43:44 UTC | #48

Hello,

Does the TerrainBlendEdit xml both hlsl glsl still work for Urho3D 1.40? I at the point where I am mixing the textures to get the cliff texture, etc? The old method isn't working.

This was the old method.


```
 /// Set component
    terrainProcedural -> Initialize();
    terrainProcedural -> SetDimensions(DEFAULTSIZE,DEFAULTSIZE);
    terrainProcedural -> SetWorldType(terrainrule.worldtype, terrainrule.subworldtype, terrainrule.sealevel, terrainrule.creationtime);
    terrainProcedural -> SetOctaves(override, octaves,  persistence, octave1,octave2,octave3,octave4,octave5,octave6,octave7,octave8);

    /// Generate Produracel map
    terrain->GenerateProceduralHeightMap(terrainrule);

    Image * producedHeightMapImage = new Image(context_);
    producedHeightMapImage -> SetSize(DEFAULTSIZE+1,DEFAULTSIZE+1, 1, 4);
    producedHeightMapImage -> SetData(terrain->GetData());

    terrain->SetMaterial(cache->GetResource<Material>("Materials/TerrainEdit.xml"));

    /// Get heightmap for texture blend
    Image * terrainHeightMap= new Image(context_);

    terrainHeightMap->SetSize(DEFAULTSIZE+1,DEFAULTSIZE+1,1,4);
    terrainHeightMap ->SetData(terrain -> GetHeightMap () -> GetData());

    terrainHeightMap -> FlipVertical();

    /// Generte image

    /// Define heightmap texture
    int bw=DEFAULTSIZE+1,bh=DEFAULTSIZE+1;

    Texture2D * blendtex=new Texture2D(context_);
    blendtex -> SetNumLevels(1);
    blendtex -> SetSize(0,0,0,TEXTURE_DYNAMIC);
    terrain-> GetMaterial() -> SetTexture(TU_DIFFUSE ,blendtex);

    /// Shared pointer for blend texture
    SharedPtr<Image> blend;
    SharedPtr<Image> blendMap;

    blend = new Image(context_);
    blend -> SetSize(bw,bh,1,4);
    blend -> Clear(Color(1,0,0,0));

    blendMap = new Image(context_);
    blendMap -> SetSize(bw,bh,1,4);
    blendMap -> Clear(Color(0,0,0,0));


    float steep=0.0f;
    float steepforlerp=0.0f;

    /// create blend here
    for(unsigned int x=0; x<bw; x++)
    {
        for(unsigned int y=0; y<bh; y++)
        {

            Color terrainHeightvalue=terrainHeightMap->GetPixel(x,y);

            switch(terrainrule.worldtype)
            {
            case WORLD_DESERT:
            {
                Color currentcolor = blend -> GetPixel(x,y);
                Color resultcolor=currentcolor.Lerp(Color(0.0f,1.0f,0.0f,0.0f), 1.0f);
                blend-> SetPixel(x,y,resultcolor);
            }
            break;
            default:
                /// Compare to sealavel
                if(terrainHeightvalue.r_<terrainrule.sealevel)
                {

                    Color currentcolor = blend -> GetPixel(x,y);

                    //               float mix=1.0f-((float)terrainHeightvalue.r_/terrainrule.sealevel);
                    float mix=(float)terrainHeightvalue.r_/terrainrule.sealevel;

                    float sterpforlerp=cutoff(mix,0.05f,0.040f,false);

                    Color resultcolor=currentcolor.Lerp(Color(0.0f,1.0f,0.0f,0.0f), sterpforlerp);

                    blend-> SetPixel(x,y,resultcolor);

                }
                break;
            }

            /// blend cliff
            Vector2 nworld=Vector2(x/(float)bw, y/(float)bh);
            Vector3 worldvalue=NormalizedToWorld( producedHeightMapImage,terrain,nworld);
            Vector3 normalvalue=terrain->GetNormal(worldvalue);

            steep=1.0f-normalvalue.y_;
            steepforlerp=cutoff(steep,0.05f,0.040f,false);

            Color currentcolor = blend -> GetPixel(x,y);

            int mixfactor=rand()%99;

            float mix=(float)(mixfactor+1)/100;

            // Color resultcolor=currentcolor.Lerp(Color(0,0,mix,1.0f-mix), steepforlerp);
            Color resultcolor=currentcolor.Lerp(Color(0,0,mix,1.0f-mix), steepforlerp);

            blend-> SetPixel(x,y,resultcolor);

        }
    }

    /// Rotate image and assign texture
    blend -> 	FlipVertical ();

    environmentbuild_ -> SetTextureMap(blend);

    blendtex ->SetData(blend, true);

    RigidBody* terrainbody = terrainNode->CreateComponent<RigidBody>();

    CollisionShape* terrainshape = terrainNode->CreateComponent<CollisionShape>();

    terrainbody->SetCollisionLayer(1);
    terrainshape->SetTerrain();

    Vector3 position(0.0f,0.0f);
    position.y_ = terrain->GetHeight(position) + 1.0f;

    /// Add node
    manager_->AddGeneratedObject(terrainNode);


    /// Position character
    Node * characternode_ = Existence->scene_->CreateChild("Character");
    characternode_->SetPosition(Vector3(0.0f, position.y_ , 0.0f));

    /// Get the materials
    Material * skyboxMaterial = skybox->GetMaterial();

    /// Change environment
    Existence->GenerateSceneUpdateEnvironment(terrainrule);
    /// Set component
    terrainProcedural -> Initialize();
    terrainProcedural -> SetDimensions(DEFAULTSIZE,DEFAULTSIZE);
    terrainProcedural -> SetWorldType(terrainrule.worldtype, terrainrule.subworldtype, terrainrule.sealevel, terrainrule.creationtime);
    terrainProcedural -> SetOctaves(override, octaves,  persistence, octave1,octave2,octave3,octave4,octave5,octave6,octave7,octave8);

    /// Generate Produracel map
    terrain->GenerateProceduralHeightMap(terrainrule);

    Image * producedHeightMapImage = new Image(context_);
    producedHeightMapImage -> SetSize(DEFAULTSIZE+1,DEFAULTSIZE+1, 1, 4);
    producedHeightMapImage -> SetData(terrain->GetData());

    terrain->SetMaterial(cache->GetResource<Material>("Materials/TerrainEdit.xml"));

    /// Get heightmap for texture blend
    Image * terrainHeightMap= new Image(context_);

    terrainHeightMap->SetSize(DEFAULTSIZE+1,DEFAULTSIZE+1,1,4);
    terrainHeightMap ->SetData(terrain -> GetHeightMap () -> GetData());

    terrainHeightMap -> FlipVertical();

    /// Generte image

    /// Define heightmap texture
    int bw=DEFAULTSIZE+1,bh=DEFAULTSIZE+1;

    Texture2D * blendtex=new Texture2D(context_);
    blendtex -> SetNumLevels(1);
    blendtex -> SetSize(0,0,0,TEXTURE_DYNAMIC);
    terrain-> GetMaterial() -> SetTexture(TU_DIFFUSE ,blendtex);

    /// Shared pointer for blend texture
    SharedPtr<Image> blend;
    SharedPtr<Image> blendMap;

    blend = new Image(context_);
    blend -> SetSize(bw,bh,1,4);
    blend -> Clear(Color(1,0,0,0));

    blendMap = new Image(context_);
    blendMap -> SetSize(bw,bh,1,4);
    blendMap -> Clear(Color(0,0,0,0));


    float steep=0.0f;
    float steepforlerp=0.0f;

    /// create blend here
    for(unsigned int x=0; x<bw; x++)
    {
        for(unsigned int y=0; y<bh; y++)
        {

            Color terrainHeightvalue=terrainHeightMap->GetPixel(x,y);

            switch(terrainrule.worldtype)
            {
            case WORLD_DESERT:
            {
                Color currentcolor = blend -> GetPixel(x,y);
                Color resultcolor=currentcolor.Lerp(Color(0.0f,1.0f,0.0f,0.0f), 1.0f);
                blend-> SetPixel(x,y,resultcolor);
            }
            break;
            default:
                /// Compare to sealavel
                if(terrainHeightvalue.r_<terrainrule.sealevel)
                {

                    Color currentcolor = blend -> GetPixel(x,y);

                    //               float mix=1.0f-((float)terrainHeightvalue.r_/terrainrule.sealevel);
                    float mix=(float)terrainHeightvalue.r_/terrainrule.sealevel;

                    float sterpforlerp=cutoff(mix,0.05f,0.040f,false);

                    Color resultcolor=currentcolor.Lerp(Color(0.0f,1.0f,0.0f,0.0f), sterpforlerp);

                    blend-> SetPixel(x,y,resultcolor);

                }
                break;
            }

            /// blend cliff
            Vector2 nworld=Vector2(x/(float)bw, y/(float)bh);
            Vector3 worldvalue=NormalizedToWorld( producedHeightMapImage,terrain,nworld);
            Vector3 normalvalue=terrain->GetNormal(worldvalue);

            steep=1.0f-normalvalue.y_;
            steepforlerp=cutoff(steep,0.05f,0.040f,false);

            Color currentcolor = blend -> GetPixel(x,y);

            int mixfactor=rand()%99;

            float mix=(float)(mixfactor+1)/100;

            // Color resultcolor=currentcolor.Lerp(Color(0,0,mix,1.0f-mix), steepforlerp);
            Color resultcolor=currentcolor.Lerp(Color(0,0,mix,1.0f-mix), steepforlerp);

            blend-> SetPixel(x,y,resultcolor);

        }
    }

    /// Rotate image and assign texture
    blend -> 	FlipVertical ();

    environmentbuild_ -> SetTextureMap(blend);

    blendtex ->SetData(blend, true);

    RigidBody* terrainbody = terrainNode->CreateComponent<RigidBody>();

    CollisionShape* terrainshape = terrainNode->CreateComponent<CollisionShape>();

    terrainbody->SetCollisionLayer(1);
    terrainshape->SetTerrain();

    Vector3 position(0.0f,0.0f);
    position.y_ = terrain->GetHeight(position) + 1.0f;

    /// Add node
    manager_->AddGeneratedObject(terrainNode);


    /// Position character
    Node * characternode_ = Existence->scene_->CreateChild("Character");
    characternode_->SetPosition(Vector3(0.0f, position.y_ , 0.0f));

    /// Get the materials
    Material * skyboxMaterial = skybox->GetMaterial();

    /// Change environment
    Existence->GenerateSceneUpdateEnvironment(terrainrule);
```

-------------------------

Bananaft | 2017-01-02 01:05:43 UTC | #49

whoa, roads looks sexy. Seeing it, I want to drop everything and make another rally game.

-------------------------

JTippetts | 2017-01-02 01:05:48 UTC | #50

I'm in the process of updating this project (after a long hiatus) to work with the recent updates to Urho3D, including conditionals for D3D11 shaders and GLSL versions of the various terrain shaders.

-------------------------

JTippetts | 2017-01-02 01:05:48 UTC | #51

The project repo ( [github.com/JTippetts/U3DTerrainEditor](https://github.com/JTippetts/U3DTerrainEditor) ) now has an 8-terrain shader that works for D3D9, D3D11 and GLSL. It successfully builds against the latest Urho3D (pulled yesterday, 7-4). Since I walked away from the project for so long, I'm not really sure where it stands, refactor-wise. I'll probably eliminate most of the experimental shaders I was tinkering with for simplicity, and try to add flexibility to the ones in existence. Additionally, I have a tri-planar shader I'm working on. I'll try to build a new terrain dialog that gives control over shader choice to make it easier to play with.

Edit:
The repo now has the HLSL and GLSL versions of the 8-detail triplanar shader. It's pretty heavyweight, but even on my potato it's still functional in the editor. The tri-planar shader uses the detail blending between layers described in previous posts, along with normal-mapping (enabled by the BUMPMAP option). You can see the difference between the tri-planar shader and the normal shader:

Normal:
[url=http://i.imgur.com/Ke9XpqB.jpg][img]http://i.imgur.com/LAAHqsk.png[/img][/url]

Triplanar:
[url=http://i.imgur.com/YgW1ORr.jpg][img]http://i.imgur.com/qTwPdsh.png[/img][/url]

-------------------------

vivienneanthony | 2017-01-02 01:05:50 UTC | #52

Is this correct?
[code]
<material>
<technique name="Techniques/TerrainBlend8EditTriplanar.xml" />
<texture unit="1" name="Textures/TerrainBlend4/Grass0126_2_S.jpg"/>
<texture unit="2" name="Textures/TerrainBlend4/Desert2.jpg" />
<texture unit="3" name="Textures/TerrainBlend4/Cliff2.jpg" />
<texture unit="4" name="Textures/TerrainBlend4/Cliff3.jpg" />
<parameter name="MatSpecColor" value="0 0 0 1" />
<parameter name="DetailTiling" value="1024 1024" />
<parameter name="BumpStrength" value="128" />
<parameter name="PackTexFactors" value="0.25 0.5 512 9" />
</material>
[/code]

I asked because I'm getting this response.
[code][Wed Jul  8 14:55:51 2015] ERROR: Failed to compile pixel shader TerrainBlend8EditDetailTriplanar(BUMPMAP DIRLIGHT PERPIXEL):
0(1021) : error C7506: OpenGL does not define the global function mul[/code]


[img]http://i.imgur.com/OwehQQ1.png[/img]

-------------------------

Mike | 2017-01-02 01:05:51 UTC | #53

mul(x, y) should be replaced by x * y in OpenGL

-------------------------

vivienneanthony | 2017-01-02 01:05:51 UTC | #54

[quote="Mike"]mul(x, y) should be replaced by x * y in OpenGL[/quote]

The line I see in the glsl file is. Are you refering to that?

[code]
		vec3 normal=normalize(mul((bump1*b1+bump2*b2+bump3*b3+bump4*b4+bump5*b5+bump6*b6+bump7*b7+bump8*b8)/bsum,tbn));
		[/code]

-------------------------

Mike | 2018-01-29 15:46:42 UTC | #55

Yes, replace by:
[code]
vec3 normal = normalize(tbn * (bump1*b1+bump2*b2+bump3*b3+bump4*b4+bump5*b5+bump6*b6+bump7*b7+bump8*b8) / bsum);
[/code]

-------------------------

JTippetts | 2017-01-02 01:05:52 UTC | #56

I pushed the changes as Mike suggested. Mike: Is there a chance that some implementations of GLSL might, in fact, provide mul()? I'm no expert at that sort of thing, but I never encountered any errors with the use of mul() while doing my own testing.

[quote]
Is this correct?

[code]
<material>
<technique name="Techniques/TerrainBlend8EditTriplanar.xml" />
<texture unit="1" name="Textures/TerrainBlend4/Grass0126_2_S.jpg"/>
<texture unit="2" name="Textures/TerrainBlend4/Desert2.jpg" />
<texture unit="3" name="Textures/TerrainBlend4/Cliff2.jpg" />
<texture unit="4" name="Textures/TerrainBlend4/Cliff3.jpg" />
<parameter name="MatSpecColor" value="0 0 0 1" />
<parameter name="DetailTiling" value="1024 1024" />
<parameter name="BumpStrength" value="128" />
<parameter name="PackTexFactors" value="0.25 0.5 512 9" />
</material>
[/code]
[/quote]

GLSL compilation errors aside, that isn't the correct usage of the shader. Perhaps a bit more explanation of it is in order.

The shader (either 8Detail or 8DetailTriplanar) only uses 3, 4 or 5 texture units. The number used depends on whether or not BUMPMAP and USEMASKTEXTURE are specified as options.

Slot 0: Weight map for terrain types 0,1,2 and 3
Slot 1: Weight map for terrain types 4,5,6 and 7
Slot 2: Terrain texture atlas (more on its format/layout in a bit)
Slot 3: Normal map of terrain texture atlas
Slot 4: Mask texture (provided to allow for visualization of the editing mask in the terrain editor).

The weight maps are straightforward: a value of 0 for a given component corresponding to a terrain type means that terrain type provides no contribution, a value of 1 means it provides full contribution. All weights are balanced in the shader so they add up to 1.

The terrain texture atlas is constructed as an atlas of 8 terrain types. Each type provides the diffuse color in RGB and the height of the texture in A. The height channel is used to alter the blending weight as described earlier in the thread, achieving the effect of terrain such as raised stones more realistically combining with terrain such as dirt, so that dirt tends to fill in the cracks around the stones rather than just simply fading from one to the other. The terrain texture provided with the editor can be found in Bin/TerrainEditorData/Textures/diff.png with the normal map at normal.png. It is laid out in a 4x2 pattern of textures (4 across, 2 down), and each texture is 512 pixels in size. This is important. The  PackTexFactors passed to the shader as a float4/vec4 describes this layout, and must be edited if the layout is changed. The first float, 0.25, describes the width of a single terrain texture in comparison to the entire texture. ie, 0.25 (1/4, given that the texture is 4 terrain types wide). The second float, 0.5, describes the height of a single terrain texture in relation to the height of the whole texture. In this case, 0.5 given that the texture is 2 terrain types high. The third float is the size, in pixels, of a single terrain type texture. The final float is the exponential size, of the top level terrain texture dimensions. ie, 9 in this case, given that 2^9=512. This exponent is used in the calculation of the mip-map level in a custom fashion described earlier in the thread.

The mask texture specifies a texture that is mapped across the entire terrain. The red channel is currently the only mask channel used, though I might provide for the ability to use up to 4 mask layers in a layer iteration of the editor. The mask value is used to mix between the final diffuse texture color and a reddish mask color, to give a visual indicator of where your mask is applied. The mask texture only really makes sense in the context of the editor, and in a real game usage should probably be omitted.

The BumpStrength shader uniform is a bit of legacy cruft that is no longer used, and can safely be omitted.

-------------------------

Mike | 2017-01-02 01:05:52 UTC | #57

I'm not expert either, I'm using this [url=http://dench.flatlib.jp/opengl/glsl_hlsl]sheet[/url] for reference. Maybe 'mul' has been added recently to GLSL.

BTW, I've sent a PR to fix the issue reported by rogerdv when building with LuaJit enabled.

-------------------------

krstefan42 | 2017-01-02 01:05:53 UTC | #58

GLSL doesn't have a function called "mul". Some compilers may allow it, but it's not in the GLSL specification, so don't expect it to work on every computer.

-------------------------

Lichi | 2017-01-02 01:10:16 UTC | #59

I updated terraineditUIOriginal.lua to work in Urho 1.5
(Only need edit to the lines that use GetPtr function) :slight_smile:
[url]http://pastebin.com/qCENVAyD[/url]

-------------------------

George | 2017-01-02 01:10:18 UTC | #60

Hi
Can you post a sample project using this?

thanks

-------------------------

Lichi | 2018-01-29 15:47:46 UTC | #61

[quote="George"]
Hi
Can you post a sample project using this?

thanks
[/quote]

You have to compile the source and replace the file located at "Data/LuaScripts/terraineditUIOriginal.lua"
(don't forget to update the bind_anl.cpp and BindTerrainEdit.cpp using tolua++ tool)
PS: here's the new file, i forgot to edit some lines: [pastebin.com/V1dcvuDh](http://pastebin.com/V1dcvuDh)
PS2: works everithing except the filters, i could not fix the error :/

Update: 
bind_anl.cpp: [pastebin.com/JCtXsF0q](http://pastebin.com/JCtXsF0q)
BindTerrainEdit.cpp: [pastebin.com/73QQ9Hdr](http://pastebin.com/73QQ9Hdr)

-------------------------

JTippetts | 2017-01-02 01:11:35 UTC | #62

I've updated the project to build with the latest head. I've also updated to the latest version of the Accidental Noise Library for the filters. I am currently in the process of performing the long-procrastinated UI updates I had started working on, including proper load/save/new dialogs. I'm also re-working the filters system a bit, to make it easier to use. Note that it has been several months since I worked on it, so I'm currently unaware of which parts are horribly broken. If anyone runs across anything, let me know, and I'll try to fix as I get reacquainted with the codebase.

-------------------------

weitjong | 2017-01-02 01:11:35 UTC | #63

That's good news. Thanks in advance.

-------------------------

JTippetts | 2017-01-02 01:11:36 UTC | #64

I've pushed some commits that add basic save/load functionality for the heightmap and the 2 blend maps. Right now, they are disconnected bits accessed via a menu in the upper left corner, since there isn't as yet any kind of unifying project structure for a terrain. Each button opens a FileSelector to complete the selected operation. At some point, I imagine I'll implement a project structure that can collect a terrain, its material selection and its blend maps into a single data description that can be loaded and saved, rather than forcing the user to load and save each image (heightmap, blend 1 and blend 2) individually as at present.

There are some bugs. Loading a blend map that is a different dimension from the current can cause a little bit of weirdness. I'm not too interested in tracking that down exactly, since the way I'm handling some things is going to change in the near future.

-------------------------

JTippetts | 2017-01-02 01:11:36 UTC | #65

I've been fiddling with the terrain textures a little bit today. In the process, I wrote up a journal entry at my devlog about a process I use to create stony-soil dirt textures for terrain: [gamedev.net/blog/33/entry-22 ... e-systems/](http://www.gamedev.net/blog/33/entry-2261900-dirt-and-rock-textures-using-blender-particle-systems/)

The technique uses Blender particle systems, and Blender Cycles node setups to facilitate baking AO/displacement/normal from a particle system. If anyone is interested, feel free to check it out. Some of the results can be seen in recent commits of the terrain editor, and the devlog entry contains a link to the .blend file used to generate one of the dirt textures.

-------------------------

JTippetts | 2017-01-02 01:11:38 UTC | #66

I've been re-working the filters UI. I added a DropDownList option type to allow selecting from a list of options. To demonstrate it, the Generate Noise Heightmap and Generate Noise Blend Layer filters were added (replacing some earlier filters). The new filters use a drop-down list to select a noise function type for generating a heightmap or a blend layer, respectively.

Image of the filter drop-down selection:
[url]http://i.imgur.com/XchuPU4.jpg[/url]

I implemented some performance fixes to speed up the process of generating a heightmap or blend layer map from a noise kernel, eliminating some redundancy and taking advantage of the ANL option USETHREAD in order to use multi-threading during kernel mapping.

I'm still working on how I want to handle file handling: save, load, new. Common sense would dictate that I implement a project structure of sorts, and encapsulate all of the various data (heightmap, blend maps, brush settings, material settings, etc...), so I'm working on a design for that. Also working on designs for the tool bar, and a rework of the brush dialog and the terrain layer selection dialog. (Man, I hate UI development. Hate it.)

-------------------------

JTippetts | 2017-01-02 01:11:39 UTC | #67

A shot showing some of the textures I've been creating:


[url=http://i.imgur.com/JFElgW4.jpg][img]http://i.imgur.com/MmLYsvM.png[/img][/url]

-------------------------

JTippetts | 2017-01-02 01:11:44 UTC | #68

I've updated the tri-planar 8-type editing shader to use texture arrays. This eliminates the hackish texture-atlas method, with all its drawbacks, and simplifies the specification of terrain tile sets. Sadly, it doesn't work for D3D9. I've kept the D3D9 path in the HLSL shader for now, though currently there is some stuff in LuaScripts/terraineditor.lua that needs to be un-commented in order to make the D3D9 path work again. And... uh... I actually haven't tested to see if that path works. But anyway...

Edit:

I've also update the terrain brush UI to allow brush selection based on texture swatches. The brush UI provides a preview pane and a grid of terrain layers to choose from. Here is a shot of the new brush UI:

[url=http://i.imgur.com/SUzROfU.jpg][img]http://i.imgur.com/FfhPUns.png[/img][/url]

-------------------------

Dal | 2017-01-02 01:14:05 UTC | #69

This doesn't seem to work with the latest engine again... or at least I can't get it to work. :frowning:

-------------------------

smellymumbler | 2017-02-28 23:38:32 UTC | #70

I can't either. Is this still updated? It should be merged to master, it's amazing!

-------------------------

JTippetts | 2017-09-22 21:05:14 UTC | #71

Somebody reminded me that this is still a thing of mine, so I've done a few updates.

Added the D3D11 shader. Doesn't support D3D9; I doubt it ever will, to be honest, since I'd have to go back to a texture atlas for that path.

Started work on allowing to swap out texture layers. Made the thumbnails on the terrain brush widget actually accurate. Generates the thumbnails from selected layers. Allows using a file chooser to pick diffuse and normal textures for a layer.

Terrain layer edit UI supports specifying a layer scale factor for the layer, to allow to make the textures larger or smaller on a given layer.

Some (currently nonfunctional) additions to the terrain brush widget to allow controlling material parameters Smooth Blend, Triplanar, and Normal Mapping. These will eventually allow the user to enable/disable these three aspects of the material at run-time.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/df29636d1dfc172daf4f76318682d68e84659360.jpg'>

-------------------------

smellymumbler | 2017-09-26 16:44:26 UTC | #72

This is amazing news! Your terrain shader is amazing. Glad to know you are still working on it. Even though i don't use the editor, i benefit a lot from it by creating custom masks and using tons of textures.

It looks amazing combined with stuff like World Machine.

-------------------------

Victor | 2017-09-26 19:26:23 UTC | #73

I had to double check to make sure I 'liked' your post @JTippetts haha. Very nice work!

-------------------------

smellymumbler | 2017-09-27 16:07:39 UTC | #74

You should setup a Patreon page or a PayPal donation page. I would love to give some beer money back to you.

-------------------------

JTippetts | 2017-10-09 14:05:10 UTC | #75

My wife tells me I should set up a Patreon, too. She thinks I spend way too much time doing this stuff for free. :smiley:

Here is a shot of my current project:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1b3865ab2ba815117d45cc3c7f57bde855016d75.png'>

This is something I've been wanting to work on for a long time. The terrain editor embeds the [Accidental Noise Library](https://github.com/JTippetts/accidental-noise-library) for noise generation, and I've wanted to build a visual node-based editor for it for several years now. Decided to finally get started on it. It's working pretty well so far, though I haven't built node types for all the functions yet. Eventually, it will hook in to a revised filter system so that you can build node chains then have them output to the heightmap or the terrain blend layers or even the mask layers.

The node graph makes use of some custom UI components, notably the connection slots and the spline links. It's still a work in progress, though, and I have some refinements planned. As always, the current source can be found in the github repo. Currently, you need to press 'n' to open the node window and 'm' to close it. It creates an Output node for you. Press Spacebar to open the create node menu. Click the buttons in the menu to create a node of the given type. The window is sized to 2x2 screens worth of space, so you can drag nodes around and pan the window with the left mouse button as needed. Click and drag on output links to make connections. When done, press 'b' and it will output the node chain to a 256x256 image in the root folder called 'noise.png'. Like I said, it's still very much a work in progress. Once all the function types are implemented, I will start work on the public facing UI for handling node groups and hooking them up to the terrain. Also, if you play around with it, watch out for bugs. Much of the code for generating the noise chain hasn't been fully tested yet.

-------------------------

JTippetts | 2017-10-12 17:43:25 UTC | #76

I've implemented preliminary functionality to map output from a node chain to terrain height, layer blends or masks.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/56d514185a6cf22c460e1f140b5110e4ef5651ee.jpg'>

Currently, only the Map, New and Edit buttons actually do anything. But you can click new to create a new node group, Edit to edit the node graph, then click Map Output to open a dialog that allows you to choose some options. The drop-down list lets you choose from Terrain, any of the 8 layers, and any of the 3 masks as target. You can also choose the range to re-map the output to, and you can select to use any of the 3 masks to mask off the output. (Mask selections are ignored when writing to a mask layer.) Clicking Make it happen! will perform the operation.

I've also written a routine to generate a cavity map from the heightmap. It is still in testing stage in these shots, but I'll make it a filter with more flexibility after the wife and I get back from lunch today. The cavity mapper works a lot like a SSAO shader, only implemented in software and operating on the heightmap. You specify a radius size, and it samples random samples around each pixel in the heightmap and tests occlusion, building an occlusion factor for the pixel and writing it to an output buffer. This output buffer can then be used for things such as writing layer blend values:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/212f3b56bd167726f9bbad67853271953c396718.jpg'>

Combined with an erosion filter (in the works) this can create some interesting terrain variation.

I've got projects in process for setting up waypoint groups/spline groups for road and river filters, to make that process a little more flexible. Plus, I'm working on revamping the toolbar to use an actual icon toolbar, and working on the terrain and blend resizing/loading/saving stuff to make it a little better. (It's fully broken right now, due to a refactor.)

Some notes on graph node generation:

One of the more useful graph nodes is the Fractal node. Supply it with a basis function to use for the octave layers, plus some other parameters, and it generates a layered noise fractal useful for generating terrain. The Accidental Noise Library supplies some functionality to help the process generate some interesting effects. Here is a sample node graph using Fractal:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/99d360b3dd4827443dba75f933ed49a5068248e8.png'>

In this image, a Gradient noise basis is passed through an Abs function then through a Rotate Domain function (which applies a rotation of the input coordinates around an axis). This is set as the Layer input for the fractal. The Angle parameter of the Rotate Domain is fed from a Randomizer node; a Randomizer node randomizes a value from a range based on a given seed.

The way Fractal works is, it iterates over numoctaves, and for each layer it re-seeds the Layer input chain with a new random seed. Re-seeding iterates through the source tree, and overwrites a new random seed for every Seed node in the chain. This re-seeds the Gradient basis and the Randomizer for Angle for each layer, causing each fractal octave layer to generate a different pattern, rotated by a different angle around the vertical axis. This rotation prevents grid-aligned artifacts in the input noise from aligning with/amplifying each other, something that is especially useful for ridged or billow noise.

Any of the inputs can be overridden by attaching a node graph link to the input. This makes it possible to perform some pretty complex functions. You can specify the frequency from a node graph chain, for example, to vary the frequency of the noise fractal based on some input pattern. You can specify as complex a node graph for any input as you desire, limited only by how long you want to sit and wait for it to execute.

Also provided is an Expression node, which evaluates a string expression into a node graph:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bef8890d0c8428cdc8eed91c625c3e8e6b215d5b.png'>

In the works is a format to allow saving and loading node graphs. Also, I would like to implement some sort of grouping functionality, to provide the ability to create libraries of node graphs that can be imported into a node graph, and used as a sort of 'black box' function. ANL provides a Seeder node that performs similarly to how the Fractal re-seeds its input layer parameter. You can attach the output of a node graph module to any number of Seeder modules, to enable re-using the node graph with different seeds for different tasks.

-------------------------

JTippetts | 2019-05-23 13:20:02 UTC | #77

So I've been working on this some more.

Mostly, I'm working on the UI. It's still a pieced-together mess of prototyping code, but it's getting better. I've added a toolbar now, with check buttons for the various tools:

![New toolbar](upload://6IdZY9tyoa9pN19RsbZcS2222ls.jpg)

The tools are: Terrain Settings (where you can save/load/clear and change the size and spacing of the heightmap, the size of the blend layers and masks, etc...), Edit Height, Smooth Height, Edit Layers, Edit Masks, Edit Node Graphs, Edit Splines (still mostly unimplemented), Filters, and Help (TODO: Add a help page.)

I've compressed the size of the nodes for the Node Graphs screen as well:

![Smaller nodes](upload://pwCuKoBZCgIIRjh3unYM3Uf2Msz.png)

Gives you more efficient use of screen real estate. Have also now implemented all relevant ANL kernel functions.

Introduced a simple Erosion filter to the filters page, and cleaned out the filters that have been superseded by the Graph Nodes or other functionality. And of course I am in the process of doing various other cleanup bits.

I've also updated the Readme at the [Github repo](https://github.com/JTippetts/U3DTerrainEditor) to provide some instructions and an overview of the tools.

-------------------------

JTippetts | 2017-10-28 00:19:27 UTC | #78

Some recent work on the editor:

Preliminary work on letting the user create custom nodes and save them. As an example:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5ddba26b936b8421aa5909b400636f53aff5774b.png'>

In this shot, I have set up a node chain to create an island heightmap. The node chain uses a fuzzy disk node, passes it's output through chained Translate nodes. The Translate nodes use a basic noise fractal to modify the input coordinate, applying domain distortion to the fuzzy disk. The output can be seen in the preview window. I created a small number of constant and seed nodes. The Constant and Seed nodes have edit boxes with which the nodes can be renamed. By tweaking the parameters of these constant/seed nodes, the output of the island generator can be modified.

Once the chain is setup, you can enter a name for the node group and hit Store on the output node, next to the Preview button. This will construct a compound node type from the chain, with named input parameters based on the constants I set up in the initial chain:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/af0ba96c6a4559c6f66997069e647605b7eca5b9.png'>

This Island node now contains all of the functionality of the earlier graph, condensed down into a single tweakable node. Output the result to the terrain, apply a few erosion, cliff and cavity filters, and see how it looks:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d36972e27b88c09d48b9c10606cd06c654dbd348.jpg'>

I don't currently have any good means for saving these nodes. I'll probably need to write another small UI system for it, to allow saving/loading library nodes, etc... (As if I don't already have enough unfinished UI stuff sitting around in there, right?)

I did get rid of the big ugly menu of node create buttons, in favor of a more menu-like + button with menu categories:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/278cd1dd98e7a3367876ee41537640bb8165a8d1.png'>

I have a built-in library category for compound functions I find useful. fuzzydisk is one of these I have already made, which uses a radial function, a radius constant and some math to create a fuzzy disk primitive as a base for islands. Anything stashed using the Store button gets placed in the user category, but at the moment it's not persistent between sessions. I'll probably want to start implementing some kind of user or project settings to make some stuff persistent between sessions, as it's likely that users will want to build their own libraries. For that kind of stuff, I'll probably want to put a little more thought and design into it.

-------------------------

johnnycable | 2017-10-28 15:33:52 UTC | #79

Nice. The terrain has some fuzzy natural feeling in it, without getting too much overdrawn. Go on.

-------------------------

Eugene | 2017-10-28 16:46:11 UTC | #80

Unreal Engine default terrain use low-frequency noise textures to remove "tiling". Have you tried this approach?

-------------------------

JTippetts | 2017-10-28 18:14:21 UTC | #81

I haven't really tried with a detail texture, but I have tried with duplicating each terrain layer with a lower-scaled UV and blending that in, as was discussed much earlier in this thread:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/30241292841c6e0ff11427ec8e6453a912aebbe5.jpg'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/38b3f0f3598d41f7c995b4bade4feeb744207f6e.jpg'>

It works fairly well, although it doesn't eliminate the repeating pattern completely, since it still exists at the higher scale:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b4f608c5370aae957bc8234990dff88ac57a8126.jpg'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/da21c33cf49ca1d48b5abcd87183b1f26f7392e9.jpg'>

It's far less obvious from the ground, at least, and that's really what counts. Of course, in a tri-planar mapping texture like this, doubling the number of texture samples might not be what you really want to do. Not only does it add even more blending to the texture, it also can impact performance. Still, even on my crappy lappy I still get about 40 FPS on this scene with the tiling reduction enabled.

I pushed a commit to provide a toggle for enabling/disabling tiling reduction. Go to the terrain layer brush, and there is now a toggle in the group with the other material settings.

-------------------------

smellymumbler | 2017-10-29 16:49:00 UTC | #82

Some insight on how UDK does it:

https://docs.unrealengine.com/udk/Three/TerrainAdvancedTextures.html

And UE4:
https://docs.unrealengine.com/latest/INT/Engine/Rendering/Materials/HowTo/DetailTexturing/

And CE:
http://docs.cryengine.com/display/SDKDOC2/Detail+Maps
http://docs.cryengine.com/display/SDKDOC2/Terrain.Layer+Shader

-------------------------

JTippetts | 2017-10-29 19:20:31 UTC | #83

The method I just pushed to the repo was derived from the Multi-UV Mixing section of the UDK document. I am sorta curious on what kind of performance other people get out of this shader with triplanar, normal-mapping and tiling reduction all enabled. My knowledge of shaders and performance characteristics is spotty at best, but I'm actually surprised that it works as well as it does.

8 terrain layers. 3 axes for triplanar, and 2 samples per axis (for tiling reduction) comes out to 48 texture samples for the diffuse, and another 48 for the normal maps. 96 samples, plus the 2 samples for the blend maps. Everything I always heard about shaders has led me to believe that 98 texture samples should bring my lappy to its knees, so the fact that it doesn't kinda surprises me.

-------------------------

Bananaft | 2017-11-14 15:08:56 UTC | #84

That erosion effect looks super sexy.  Almost like world machine on lesser resolution. Saying that, I'm thinking that this could be a very usefull tool for making height and blend maps for other engines or even non game projects.

-------------------------

smellymumbler | 2017-11-14 17:07:47 UTC | #85

This is the best thing that ever happened to Urho. Your work is amazing, @JTippetts. :heart_eyes::heart_eyes::heart_eyes:

-------------------------

JTippetts | 2017-11-14 20:53:27 UTC | #86

It's kinda been my idea all along to keep it sorta engine-neutral, at least as far as the actual terrain editing goes. However, lately I've been looking at adding some Urho3D-specific functionality: spawning forests and other vegetation and doodads from noise module density layers, using splines to generate road pieces, maybe some basic point-click object placement, generating rocks and cliffs to cover steep slopes, etc... Most of that, though, would be tied pretty tightly to the Urho3D engine, not that that is a bad thing IMO. 

@smellymumbler Thanks, I appreciate that. :blush:

-------------------------

Modanung | 2017-11-16 10:10:18 UTC | #87

The results are increasingly impressive, indeed. :slight_smile:

-------------------------

Victor | 2017-11-16 14:03:51 UTC | #88

Wow, nice work! I love seeing the progress of this editor :)

-------------------------

rasteron | 2017-11-17 02:19:43 UTC | #89

Looking great @JTippetts keep it up :+1:

-------------------------

JTippetts | 2018-01-13 20:06:26 UTC | #90

I have setup a [project page](https://www.gamedev.net/projects/45-u3dterraineditor/) for U3DTerrainEditor at gamedev.net. Project includes a ZIP with executables for Windows: an OpenGL build and a D3D11 build. Again, the project is still very much in progress, and a lot of stuff is still broken/unpolished/stupid. I'm working on it gradually. (Cut me some slack, will ya? I'm just a lowly factory worker and dad trying to make time for this stuff.)

-------------------------

davidpox | 2018-02-07 04:20:32 UTC | #91

Thanks for the executables! Playing around with the source killed me, and this worked instantly :) Good work!

-------------------------

burt | 2018-02-14 14:52:06 UTC | #92

Thanks a lot, this project is amazing! It is the only reason I've chosen Urho :grinning:

How big the terrains can be? Can I stitch them together? Does Urho apply any kind of dynamic LOD to the terrains?

-------------------------

Eugene | 2018-02-14 15:32:06 UTC | #93

You can connect as much `Terrain`s as you need, connecting them as neighbors. LODs are seamlessly connected.
Beware that standard terrain normals suck because of two reasons, so it's better to bake all normals into texture and use custom terrain shader.

-------------------------

burt | 2018-02-16 22:47:35 UTC | #94

Are the LODs auto-generated by the terrain system? Is there any kind of culling system tied to the terrain system so it also affects entities placed on top of that terrain?

-------------------------

Don | 2018-02-17 07:00:43 UTC | #95

No, they are not. To achieve that, you have to export the models with different LOD versions that specify the distance at which they switch.

-------------------------

Eugene | 2018-02-17 08:32:22 UTC | #96

[quote="burt, post:94, topic:765"]
Are the LODs auto-generated by the terrain system?
[/quote]
If you talk about terrain geomipmapping, there is. 

[quote="burt, post:94, topic:765"]
Is there any kind of culling system tied to the terrain system so it also affects entities placed on top of that terrain?
[/quote]
Drawables are always culled separately. I have no idea why one want to cull them by terrain patches.

-------------------------

JTippetts | 2018-10-20 19:13:11 UTC | #97

There have been a few updates lately. First of all, from the Terrain Settings menu you can now save or load the whole project, which will save any Node groups, Spline groups, terrain layers, and will also export a normal map for the terrain. From the Terrain Settings menu, you can also adjust colors/brightness for the Main and Back lights (directional lighting), as well as colors for Ambient and Fog. There are also sliders for fog Near and Far distances.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/2/29cd9aa68b324483ce6abd5a3774a21d0969242c.jpeg[/img]

Clicking on the color swatches opens up a color wheel to choose a color. The color wheel has a separate brightness slider next to the value slider (TODO: labeling on color chooser) that allows you to choose over-bright (up to 2x brightness) for light colors if desired.

There are a few more tools in the Filters menu, for things such as basin filling. I've also added an experimental water layer that can be edited using filters or a brush. The water layer is implemented as a separate Terrain with a water material applied, that sits at a small negative offset 'underneath' the main terrain. The water terrain can be edited, and will be visible wherever it protrudes above the main terrain. I am experimenting with water shader technology to make the water look better; in the current repo, the editor will calculate a full-terrain depth texture as the difference between the water height and the terrain height, and use that depth texture to blend in a foam texture in shallower water. I don't know much about water shaders, so that'll be a point of research in the future.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/835cb043f45c758c1cd800aadcd2454026597e9e.jpeg[/img]
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/e/ee243651e957f5be00207bb9aa3e20c2cbff5fe6.jpeg[/img]

Making the water from a Terrain rather than just a simple plane allows you to have water on varying elevations. In the Filters menu there is a filter, Fill Basins with Water, that will calculate a depression map, and fill the depressions with water. It's still a little wonky at the edges, so I'll definitely need to make improvements there. The depression fill will simulate water filling up the basins, so the water will exist on many different levels, something that would be more difficult to achieve with water planes.

I definitely will need to work on more/better water tooling if I continue with this experiment. I would like to implement a flow map texture to allow you to edit the way the foam and ripples flow. That shouldn't be too technically difficult; tooling and operations will be the trickiest part, I think. I'll probably also modify the shader to also use the depth to darken the color of the water. There are some pretty cool tricks to be done with water, and like I said I'm no expert with them.

I've sorta lost track of what other additions there have been since I last updated, so if you're curious go ahead and grab the latest repo. This weekend, time allowing, I'll try to get a binary build uploaded.

Edit: Also have implemented alpha brushes for height and terrain texture editing:

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/a/a57cd4ec2e942be5c8c6071cc273f614a7ef3c5b.jpeg[/img]

The alphas are scanned from a folder of .PNG images. They orient to the camera, so by rotating the camera you can apply the alpha at different orientations. As part of this process, I got rid of the old CustomGeometry-based brush cursor, and implemented the brush cursor as part of the terrain shader, so I could show a preview image of the alpha overlaid on the terrain. The alpha image is multiplied by the circular brush before application.

-------------------------

burt | 2018-11-10 02:01:29 UTC | #98

This thing just keeps getting better and better. BEST URHO PROJECT EVER

-------------------------

Valdar | 2019-09-03 00:28:50 UTC | #99

Does anyone know if there any problems with the current GitHub source? I've tried to build and I get the following error from CMake.

> CMake Error at CMake/Modules/FindUrho3D.cmake:343 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree or in Android library.  Use URHO3D_HOME environment variable or
  build option to specify the location of the non-default SDK installation or
  build tree.  Ensure the specified location contains the Urho3D library of
  the requested library type. > 

I've double-checked that my URHO3D_HOME environment variable is correct, and also tried to tell CMake where the path is manually, but I still get the error.

-------------------------

JTippetts | 2019-09-03 02:54:25 UTC | #100

It is building fine with current master. That CMake error says that it's not actually finding the correct Urho3D library at the specified URHO3D_HOME location. Check to make sure the built library corresponds to your specified build target (ie, built using the same flags).

-------------------------

