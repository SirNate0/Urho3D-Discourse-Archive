smellymumbler | 2018-06-15 21:36:41 UTC | #1

Does anyone have any idea how to do something like this? 

http://polycount.com/discussion/181140/unreal-4-terrain-blending-tool-inspired-by-star-wars-battlefront/p1

I was looking for a shadertoy example or something so I could at least get a grasp of it, but nothing. :(

-------------------------

TEDERIs | 2018-07-07 02:20:39 UTC | #2

I think it may be simply implemented through vertex painting. You may color vertices that intersect the terrain, then just bake a model and apply your shader that utilizes the colors and blend materials together.

-------------------------

