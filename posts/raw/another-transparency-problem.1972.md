Dave82 | 2017-01-02 01:11:58 UTC | #1

I can't figure out what causes this.Transparent sub meshes keep lit/unlit from certain camera angle. i'm using DiffTransparent technique and set reuse shadowmaps to false.  

[video]https://www.youtube.com/watch?v=QLNZZBFifyg[/video]

-------------------------

cadaver | 2017-01-02 01:11:58 UTC | #2

It could be Z fighting or wrong sorting between the hair's base pass and lit pass. I checked the rendering code quickly and if I'm not wrong the base and lit alpha passes get the same distance, which would seem to leave the order up to chance. I remember there used to be a biasing for the base passes, but it could have been lost in a regression.

EDIT: (for anyone who reads only this message) biasing is not necessary, so the speculation above is incorrect. Base passes should be rendered first due to their sort key being set differently, although the distance is same.

-------------------------

Dave82 | 2017-01-02 01:11:59 UTC | #3

Hi ! Well i think the problem is the sorting. The hair is just one single mesh (no hair layers) so it can't be Z fighting.
Any idea how to solve this ? I searched the Renderer class but couldn't find anything where to start.

-------------------------

cadaver | 2017-01-02 01:11:59 UTC | #4

See the sort function in Batch.cpp (CompareBatchesBackToFront). If distance is same, it should compare the sortkey, which is assigned in void Batch::CalculateSortKey(), which *should* set the most significant bit for the base passes to cause them to render first, so theoretically there should be no need for a distance biasing.

Theoretically it could also be a depth test issue, if the base batch and light batch end up having slightly different coordinates in the vertex shader.

-------------------------

Dave82 | 2017-01-02 01:11:59 UTC | #5

Hi ,i tried
[code]if (isBase_) sortKey_ |= 0x80000000;[/code]

and it didn't helped.

[quote]Theoretically it could also be a depth test issue, if the base batch and light batch end up having slightly different coordinates in the vertex shader.[/quote]

Is that possible ? If the passes use the same distances and transforms what could cause them having different coords ? Couldn't it be the opposite ? Having exacly the same coords which also leave depth test up to luck ? Hving some kind of a Z fight between the passes

-------------------------

cadaver | 2017-01-02 01:11:59 UTC | #6

Sortkey is 64bit, so 0x80000000 isn't the MSB. The base pass flag should already be entered into the "shader key" part, which should end up in the highest bits.

If the outputted geometry positions are the same, the result should be deterministic according to the order in which the draw calls are issued, and according to the depth test settings. I recommend debugging with PIX or the like to see the exact order of the draw calls, and if something ends up rejected due to a test.

For typical crude (male) hair meshes, using alpha test can be easier, as that allows to render as opaque geometry.

-------------------------

cadaver | 2017-01-02 01:11:59 UTC | #7

Tested briefly with the 07_Billboards sample, which has multiple spot lights, by setting the mushrooms and floor to use transparent materials (DiffAlpha / DiffNormalPackedAlpha techniques). The batch ordering appears to work right as is, ie. the base pass order is taken care of and those are rendered first.

This would point to it being something specific with your geometry / materials.

-------------------------

Dave82 | 2017-01-02 01:11:59 UTC | #8

[quote="cadaver"]Sortkey is 64bit, so 0x80000000 isn't the MSB. The base pass flag should already be entered into the "shader key" part, which should end up in the highest bits.[/quote]

Yes... i didn't noticed the unsigned long longs... which is funny as there are 3 of them in the same line :slight_smile: And yes ((unsigned long long)shaderID) << 48) should do that already

[quote="cadaver"]If the outputted geometry positions are the same, the result should be deterministic according to the order in which the draw calls are issued, and according to the depth test settings. I recommend debugging with PIX or the like to see the exact order of the draw calls, and if something ends up rejected due to a test.

For typical crude (male) hair meshes, using alpha test can be easier, as that allows to render as opaque geometry.[/quote]

How to enable the alpha test ? I tried with a dds texture (DXT5) and the result is the same... do i need to set some other parameters in the material/technique to use alpha test ?


[quote]This would point to it being something specific with your geometry / materials.[/quote]

The model should be fine.It is a standard Urho mdl. At first i thought it is something wrong with the aabb's of the skinned meshes (not properly updated at some stage or it has some offset and get culled from light point of view...) but it's not the case as all my static models in the scene act the same. The techniques are standard untouched from Urho so it must be the materials... i make materials on the fly at load time.Because i have lots of materials in the whole game and lots of variations , i usually prefer to read all my active materials from one single file rather than have hundreds of xmls.

-------------------------

cadaver | 2017-01-02 01:11:59 UTC | #9

See the AlphaMask family of techniques, e.g. DiffAlphaMask.xml. It works in the pixel shader by discarding the pixel if diffuse texture alpha is < 0.5.

-------------------------

Dave82 | 2017-01-02 01:11:59 UTC | #10

I changed the technique to alpha mask and the issue is gone.Works perfectly for hair or bushes/grass, however this makes "thin" transparent objects (e.g wire fence or tree gobos) invisible at larger distances...
i'll link my texture loader code if you could look into it and see maybe i'm missing something.But i doubt that's the problem either , it simply generates Materials from a file for a specific scene (i sort materials per scene in my editor) so i set exacly the same parameters as loading from xml ("MatSpecColor" , "MatDiffColor" , Technique , and Texture unit(s) )

For now i'm happy with the alpha mask technique as i have lot of other things to finish.

-------------------------

cadaver | 2017-01-02 01:11:59 UTC | #11

Yes, that is expected with alpha masking. You would have to tweak the mipmaps so that alpha values don't decrease below the threshold where not wanted.

-------------------------

boberfly | 2017-01-02 01:12:00 UTC | #12

Hi,

If you're using MSAA you could try enabling [url=https://en.wikipedia.org/wiki/Alpha_to_coverage]Alpha To Coverage[/url].

The engine might need to be patched to support this, I can't remember if Urho allows this out of the box. This will give you cleaner edges when alpha testing.

-------------------------

