empirer64 | 2017-01-02 01:10:21 UTC | #1

Hi all, 
I created some simple models (made out of planes) in Blender and exported it using the Blender exporter to .mdl, but the issue is that when I assign a material which uses the AlphaMask technique to that model, it is invisible. If I use Alpha technique it is just semi transparent and green (my texture is partly green and partly alpha). What should I do if I want to use AlphaMask technique for custom models ?

-------------------------

rasteron | 2017-01-02 01:10:21 UTC | #2

Hi, you could post the textures that seems questionable or better yet upload the full blend file for others to check out. I'm guessing this has something to do with the alpha channel missing.

-------------------------

empirer64 | 2017-01-02 01:10:22 UTC | #3

Ok, so here is the blend, material and texture. [url]https://mega.nz/#F!INQnHJDb!f_MFd4LpWfODilaRRNK5VQ[/url]

-------------------------

rasteron | 2017-01-02 01:10:22 UTC | #4

Nice. I got to check your stuff and I saw no problems with your texture alpha, so it should be the model or the conversion process. I would also suggest getting and trying out some existing models first if you're fairly new to the engine's pipeline.

As for the Blender exporter, it works great overall, but I only use it for static and prop models like lightmapped levels (no alphas). I'll rectify this and let you know when I get a chance.

-------------------------

empirer64 | 2017-01-02 01:10:23 UTC | #5

Blender exporter works ok for me too, but when I use Alpha material with custom model, it doesnt work at all.

-------------------------

empirer64 | 2017-01-02 01:10:23 UTC | #6

So thanks to carnalis from irc, I found out that the problem was with UV. I unwrapped the model and set the UV and now it works.

-------------------------

rasteron | 2017-01-02 01:10:23 UTC | #7

[quote="empirer64"]So thanks to carnalis from irc, I found out that the problem was with UV. I unwrapped the model and set the UV and now it works.[/quote]

Hey, glad you got it sorted out with Carnalis and I did not see this coming, it is really necessary to unwrap your model uv, regardless of engine.  :wink:

-------------------------

