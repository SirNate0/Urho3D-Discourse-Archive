GoldenThumbs | 2018-12-17 15:40:09 UTC | #1

I modified some Parallax Mapping samples I found online to work with Urho3D. Feel free to give me some suggestions and other stuff.![Brick_Screenie_23|690x223](upload://5m1iOcAmlftg1PqlD7s9JH2aWVZ.png) 

Older Version (Height Map from Diffuse Alpha):
https://drive.google.com/file/d/1pejKXIGhBh5QYQqDdF6-CVWByygpztG2/view?usp=sharing

Slightly revised version (Height Map from Normal Map Alpha):
https://drive.google.com/file/d/1aQBfmt4lJ-zcN9Xr4i8GYdOVbev9oq8M/view?usp=sharing

Right now there is
-Normal Parallax Mapping
-Steep Parallax Mapping
-Parallax Occlusion Mapping
-Relief Parallax Mapping

-------------------------

S.L.C | 2018-12-16 20:46:43 UTC | #2

You ought to use something like Github. So others could contribute and perhaps prevent your share from dying.

Other than that. It looks neat so far.

-------------------------

Modanung | 2018-12-17 00:33:10 UTC | #3

Maybe even merge it into the PBR sample?

-------------------------

GoldenThumbs | 2018-12-17 13:26:28 UTC | #4

Switched the height map from the diffuse map alpha channel to the normal map alpha channel.![Rocks_normal|500x500](upload://5SJwd8tMAc6wPiehfvP11VKTsV6.png)

-------------------------

smellymumbler | 2018-12-17 16:09:38 UTC | #5

There's some strong sawtooth with a gray border there. Is it an asset issue? Could MSAA fix it?

-------------------------

GoldenThumbs | 2018-12-17 20:40:50 UTC | #6

Not sure TBH. I know that the sawtooth is because of how the parallax is done, but I'm not sure how noticeable it would be with a better height map. The gray border could be cause by the post effects I'm using, probably the FXAA. MSAA could fix it, but I think it's unlikely. Could turn up the maxLayers to maybe get rid of it, at the cost of performance. I'll look into it.

-------------------------

GoldenThumbs | 2018-12-18 15:10:57 UTC | #7

Video:
https://www.youtube.com/watch?v=btjsFsvP8BI

-------------------------

GoldenThumbs | 2018-12-23 05:14:05 UTC | #8

Doubt the shader is good enough to be merged. Would be cool but someone who is better at this than I am would have to redo some bits, I'm sure.

-------------------------

Modanung | 2018-12-23 11:26:02 UTC | #9

I didn't necessarily mean "right away" or "unedited", but rather I meant merging as an extension of the steps proposed by @S.L.C. It becomes easier with a git repository.

-------------------------

