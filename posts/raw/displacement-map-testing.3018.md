Lumak | 2017-04-17 20:54:30 UTC | #1

Another one of those curiosity project... again.

In the video, it updates the height map from the Terrain class at runtime. The repainted pixel size is approximately the size of the char model's foot, which is not very big compared to the height map, and you don't get the granularity as to see the actual footprint detail. The update calls terrain->ApplyHeightMap() which recreates the entire terrain geometry - every patch, so it's not optimized.

I don't think I'll go any further with this project, as it's not a common game play feature, but know that it is a simple process to implement.

https://youtu.be/WddQlR8MfU8

-------------------------

S.L.C | 2017-04-18 02:54:35 UTC | #2

Well, that's a nice snow effect :D

-------------------------

johnnycable | 2017-04-18 08:49:50 UTC | #3

Good to know it's feasible, some special effects are good if you have power to spend... thank you

-------------------------

yushli1 | 2017-04-18 12:19:41 UTC | #4

Any chance that this source code can be shared? I' like to try it if the code is available

-------------------------

smellymumbler | 2017-04-19 23:35:48 UTC | #5

That would make a great example for Urho. You should PR that to the official repo. People can use this as a base for terrain deformation and also Minecraft-esque games.

-------------------------

