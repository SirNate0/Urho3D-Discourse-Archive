codingmonkey | 2017-12-22 10:58:50 UTC | #1

Hi folks) 
Earlier I wrote GS-shaders support on GL renderer but I have some strange bug then I try to edit these GS shaders in liveEdit manner. I got an double linkage error.
But today, I found what my bug with GS-shaders are gone somewhere )
so I decided to share this, GS shaders seems quite working
just an example:

Techniques: DiffGS.xml
[code]
<technique vs="UnlitGS" ps="UnlitGS" gs="UnlitGS" psdefines="DIFFMAP">
    <pass name="base" />
</technique>
[/code]

[details="Shader: UnlitGS.glsl"]
https://pastebin.com/pyHtvanq
[/details]  

https://youtu.be/4R39AavxWSg

https://github.com/MonkeyFirst/Urho3D/tree/gs-shader-gl

-------------------------

sabotage3d | 2017-01-02 01:09:01 UTC | #2

That was in my wishlist. Awesome work!

-------------------------

Mike | 2017-01-02 01:09:02 UTC | #3

Simply awesome  :stuck_out_tongue: 
Many thanks for sharing.

-------------------------

codingmonkey | 2017-12-23 17:33:36 UTC | #4

thanks guys )
now I add "primitive mode" selection in material for properly input GS layout work:
I mean this GS input layouts:
>layout (points) in;
>layout (lines) in;
>layout (triangles) in;

test with GS shades : UnlitGSPointsToQuads.glsl
[url=http://savepic.su/6899872.htm][img]http://savepic.su/6899872m.png[/img][/url]
https://youtu.be/fliHze4-JN0

-------------------------

franck22000 | 2017-01-02 01:09:03 UTC | #5

Nice job :slight_smile: Can we expect this for DX11 ? :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:09:03 UTC | #6

I would like also to see a similar on dx11, but I do not know much dx11( so maybe someone who knows someday implement similar stuff.
Also, why you do not do this yourself ? :slight_smile:

-------------------------

rasteron | 2017-01-02 01:09:03 UTC | #7

nice one! :slight_smile:

-------------------------

weitjong | 2017-01-02 01:09:04 UTC | #8

Thanks for sharing. Really interesting.

-------------------------

codingmonkey | 2017-01-02 01:09:05 UTC | #9

>Thanks for sharing. Really interesting.
No problems) I hope sometime urho3D will be fully support GS shaders on both gapi DX11/GL )

few new additions:
- Add oriented billboards example shader, it can rotates around eye axis by uniform "angle" and change size of billboards by "offset" uniform
- Add wireframe shader example (no needed second geometry passes draw with lines) We add new attributes for vertexes in GS shader to calc wireframe lines in PS.
 [url=http://savepic.su/6929408.htm][img]http://savepic.su/6929408m.png[/img][/url]

-------------------------

rasteron | 2017-01-02 01:09:06 UTC | #10

[quote]- Add wireframe shader example (no needed second geometry passes draw with lines) We add new attributes for vertexes in GS shader to calc wireframe lines in PS.[/quote]

Great update codingmonkey! I like the wireframe shader, is it easy to add other textures other than diffuse?  :slight_smile:

-------------------------

franck22000 | 2017-01-02 01:09:06 UTC | #11

Im trying to implement it for DX11 right now :slight_smile: 

If i need any help i will ask it here. With your great work CodingMonkey it's time to add geometry shaders support in Urho3D !

-------------------------

codingmonkey | 2017-01-02 01:09:06 UTC | #12

>Im trying to implement it for DX11 right now
good news) it will be awesome to have similar stuff on dx11 also

>is it easy to add other textures other than diffuse?
Did you mean LitSolid shader and all variants of it? Probably yes, it possible.
But first of all, we need began use structs in shaders, for solve one interface block issue with passing through VS<->GS (vec4 vShadowPos[NUMCASCADES];)
See this topic for clarify: [opengl.org/discussion_board ... ing-arrays](https://www.opengl.org/discussion_boards/showthread.php/175872-geometry-shaders-and-varying-arrays) (post #4 from Alfonse Reinheart)
I try to create std LitSolid shader (without GS part) with using structs (IN/OUT) but it's not working properly. 
[spoiler][pastebin]q6mXQ3X7[/pastebin][/spoiler]

Model(Jack) - is fully black colored. I do not know why. Probably I create an Issue for figure out with this.

-------------------------

franck22000 | 2017-01-02 01:09:06 UTC | #13

I have spotted an issue in shaderprecache.cpp in your branch. at line 142: 

ShaderVariation* gs = graphics->GetShader(GS, shader.GetAttribute("gs"), psDefines);

"psDefines" should be "gsDefines" i think ? :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:09:06 UTC | #14

oh, yes. thanks, i'm fix this)

-------------------------

franck22000 | 2017-01-02 01:09:06 UTC | #15

I have made my DX11 geometry shader branch based on CodingMoney work. Im still working on this (make an HLSL shader and testing it)

[github.com/OldSnake22/Urho3D/tr ... tryShaders](https://github.com/OldSnake22/Urho3D/tree/DX11GeometryShaders)

Feel free to take a look and spot my eventual mistakes.

Please note that the code tabs formating issue will be of course fixed.

-------------------------

codingmonkey | 2017-01-02 01:09:06 UTC | #16

[quote]// TODO: Change this  
1021 1049  Pair<ShaderVariation*, ShaderVariation*> key = MakePair(vertexShader_, pixelShader_);  [/quote]

I guess you need also create second level of pair for this : 
like so
        Pair<ShaderVariation*, ShaderVariation*> baseCombination(vs, ps);
        Pair<ShaderVariation*, Pair<ShaderVariation*, ShaderVariation*>> combination(gs, baseCombination);

-------------------------

franck22000 | 2017-01-02 01:09:06 UTC | #17

Yes thank you for your advice :slight_smile:

I have also spotted that if i am right you do not check "gs" pointer validity in this function ShaderPrecache::StoreShaders()

-------------------------

codingmonkey | 2017-01-02 01:09:07 UTC | #18

ok, now look at this 
[code]
void ShaderPrecache::StoreShaders(ShaderVariation* vs, ShaderVariation* ps, ShaderVariation* gs)
{
    if (!vs || !ps)
        return;

    // Check for duplicate using pointers first (fast)
    Pair<ShaderVariation*, ShaderVariation*> shaderPair = MakePair(vs, ps);
    Pair<ShaderVariation*, Pair<ShaderVariation*, ShaderVariation*>> shaderCombination = MakePair(gs, shaderPair);
    if (usedPtrCombinations_.Contains(shaderCombination))
        return;
    usedPtrCombinations_.Insert(shaderCombination);

    String vsName = vs->GetName();
    String psName = ps->GetName();
    String gsName = gs != 0 ? gs->GetName() : "";
    const String& vsDefines = vs->GetDefines();
    const String& psDefines = ps->GetDefines();
    const String& gsDefines = gs != 0 ? gs->GetDefines() : "";
    // Check for duplicate using strings (needed for combinations loaded from existing file)
    String newCombination = "";
    if (!gsName.Empty())
        newCombination = vsName + " " + vsDefines + " " + psName + " " + psDefines + " " + gsName + " " + gsDefines;
    else
        newCombination = vsName + " " + vsDefines + " " + psName + " " + psDefines;

    if (usedCombinations_.Contains(newCombination))
        return;
    usedCombinations_.Insert(newCombination);

    XMLElement shaderElem = xmlFile_.GetRoot().CreateChild("shader");
    shaderElem.SetAttribute("vs", vsName);
    shaderElem.SetAttribute("vsdefines", vsDefines);
    shaderElem.SetAttribute("ps", psName);
    shaderElem.SetAttribute("psdefines", psDefines);
    
    if (!gsName.Empty()) 
    {
        shaderElem.SetAttribute("gs", gsName);
        shaderElem.SetAttribute("gsdefines", gsDefines);
    }
}
[/code]

GS is optional part of shader that's why we do not need check it  similar as - if (!vs || !ps) return.

-------------------------

codingmonkey | 2017-01-02 01:09:08 UTC | #19

well, with my trying to bring litSolid shader on GS-rails gives some results
but i found what GS shader also need copy all VSdefinitions to pass all varyings(output variables) through GS shader into PS properly.
the problem with passing vShadowPos[NUMCASCADES]; through GS shader into PS i try to solve with mat4 without using structs in shaders (actually structs also working well), to avoid additional index in data.
VS write in mat4:
[code]    #ifdef PERPIXEL
        #ifdef SHADOW
            out mat4 vShadowPos;
        #endif[/code]

[code]
        #ifdef SHADOW
            // Shadow projection: transform from world space to shadow space
            for (int i=0; i < NUMCASCADES; i++) 
                vShadowPos[i] = GetShadowPos(i, projWorldPos);
            
        #endif
[/code]
in GS we have 3 matrixes input, by one for each vertex output
[code]
#ifdef PERPIXEL
    #ifdef SHADOW
        in mat4 vShadowPos[3];
[/code]

and one for output into PS
[code]
#ifdef PERPIXEL
    #ifdef SHADOW
        out mat4 gsShadowPos;
    #endif
[/code]
GS emit shadow mat4 for vertex
[code]
        #ifdef PERPIXEL
            #ifdef SHADOW
                gsShadowPos = vShadowPos[i];
            #endif
[/code]

after all PS gets one matrix and parse it
[code]    #ifdef PERPIXEL
        #ifdef SHADOW
            in mat4 gsShadowPos;
        #endif[/code]

[code]
        #ifdef SHADOW
            vec4 vShadowPos[NUMCASCADES];
            for (int i=0; i < NUMCASCADES; i++)
                vShadowPos[i] = gsShadowPos[i];
            diff *= GetShadow(vShadowPos, gsWorldPos.w);
        #endif
[/code]

but still i have some visual bugs with shading of model.


Edit:
I'am restore my brunch with GS with current master 
now actual repo: [github.com/MonkeyFirst/Urho3D/tree/gs-shader-gl](https://github.com/MonkeyFirst/Urho3D/tree/gs-shader-gl)
[url=http://savepic.net/7845374.htm][img]http://savepic.net/7845374m.png[/img][/url]

Known bugs:
bug1: [solved (with adding "gsi" to same place with vsi, psi )]forward renderer material based on DiffNormal+Packed tech some light problems (dark objects), DS work fine in this case.
bug2: CustomGeometry bug glitch of mesh (for example editor grid)

-------------------------

Bananaft | 2017-01-02 01:12:44 UTC | #20

Hi, what is the status of this work? Are you planing to do a PR?

-------------------------

codingmonkey | 2017-01-02 01:13:01 UTC | #21

Hi, currently it frozen. Also I guess render has a lot new changes and i'm not familiar with this new changes yet. 
Maybe later I start new work for rewrite old GS-brunch for new gl-renderer and mb also for PR.

-------------------------

cadaver | 2017-01-02 01:13:02 UTC | #22

Right now I've a branch going where I unify all graphics APIs to use the same header files (API-specific details should be hidden inside unions or pimpl when necessary), and put API-independent parts of the graphics classes (e.g. calculating vertex element offsets) in their own files. This probably affects your work too, but hopefully will make writing for multiple APIs less tedious in the future. This should be ready in a week or so.

-------------------------

codingmonkey | 2017-01-02 01:13:02 UTC | #23

ok, I will be waiting for PR, and then try to figure out with new changes in renderer, and how I may inject my previous gs-brunch into it.

-------------------------

najak3d | 2020-04-22 15:36:11 UTC | #24

We really would like to have geometry shaders for Urho.  We want to use it for smooth line drawing (so that we can translate a simple array of Line Points into a 3D line with thickness and smoothed edges).  So the geometry would preserve the mid-line, and also create two outlines -- and then the pixel shader would do a transparency falloff as it neared the edges.  This would create the smoothing effect desired.  (This is one implementation.)

Without Geometry shaders, we'll have to generate 4 triangles per line segment manually. We can do this too, but I think it's more appropriate (and efficient) to instead just feed in a simple array of points.

What is the difficulty of getting Geometry shaders implemented in Urho?  We could supply some funding for it, if the cost is reasonable, and it helps get the job done.

-------------------------

