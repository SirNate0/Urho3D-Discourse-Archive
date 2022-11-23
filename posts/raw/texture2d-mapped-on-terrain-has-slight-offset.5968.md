Lys0gen | 2020-03-05 23:53:55 UTC | #1

Hello again,
sadly I have encountered another problem with my terrain where I am out of ideas.

In addition to the heightmap I have created a colormap with the same size - for testing purposes I used it with the default TerrainBlend material as weight map. And it almost works perfectly, however the texture becomes more and more offset the further bottom/right I go.
I had thought of two potential issues, though neither of them changed anything:
-> The height/colormap are NPOT (currently 2165x1192, resizing them to 2048x2048 changed nothing)
-> The texture2d sampling in the shader gets imprecise coordinates (changing *vTexCoord* and *vDetailTexCoord* to *highp* changed nothing)

Here are some pictures:
Near the top left, offset is quite small (slopes should have the same texture as the top)
https://i.imgur.com/uSpSqts.png

Bottom edge of the terrain, issue becomes very visbile (also artifacts on the terrain edge, apparently trying to sample the undefined parts of the colormap)
https://i.imgur.com/Fv2rjOq.png
https://i.imgur.com/9drP7iE.png

Thanks in advance!

-------------------------

Modanung | 2020-03-06 00:21:35 UTC | #2

Could you show me what the wire frame of your terrain looks like? I have the feeling that a custom component that would generate the geometry could be a *lot* more efficient. Each hexagon could then be represented by a single pixel on the height/color map. Taking that path early will save some wasted effort. This would also get rid of jagged edges. Sample 34 should provide enough information to get you started.

-------------------------

SirNate0 | 2020-03-06 00:59:21 UTC | #3

I think the custom component would probably be a better solution as well. Regarding the issue you're presently experiencing, could it be due to the heights maps needing to have an extra pixel compared to the color maps? (The height maps, as I understand it, give the height of each vertex, while the color is for each square, so you end up with an extra pixel of height (e.g. a 257x257 height map produces 256x256 squares).

-------------------------

Lys0gen | 2020-03-06 02:55:04 UTC | #4

@SirNate0 huh, I did not notice that the sample heightmap has a size of 1025x1025. But sadly this does not seem to be the root of the problem. Or at least adding +1 width & height to the heightmap did not change anything that I can see with my eyes.

You are both likely right that there are lot of unnecessary tris with the terrain right now, though I am not terribly concerned with performance at the moment since aside from the terrain and an GUI there won't be much rendered. Also I might want to put in oddities such as rivers and potentially make the top of the hexes not completely flat at some point in the future. I think having a malleable terrain might be better for that purpose? For my logic the grid is obviously not saved in such a wasteful manner. Thanks for the suggestion though, I will take it into consideration.

-------------------------

Lys0gen | 2020-03-06 13:20:08 UTC | #5

Ok sorry guys, the cause is indeed

> The height/colormap are NPOT (currently 2165x1192, resizing them to 2048x2048 changed nothing)

Trying it with 2048x2048 again **and** giving the heightmap +1|+1 size seems to resolve the issue.

Now my question is, is there a better way to solve this than scaling my map size to the next highest POT?

-------------------------

Modanung | 2020-03-06 15:14:43 UTC | #6

Custom geometry? :slightly_smiling_face:

If you want to keep it simple at first, you could use prismatic placeholder blocks.

-------------------------

