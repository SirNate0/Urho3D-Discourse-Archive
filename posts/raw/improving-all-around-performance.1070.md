vivienneanthony | 2017-01-02 01:05:14 UTC | #1

Hey,

Question. What is some good ways to improve all around performance? When I load the hanger the fps drops a lot so I am thinking maybe the texture sizes,  too many subscribed events, and other issues?

I am thinking of maybe either the UI reload on specific changes, time interval, or some other measure.

I added some more UI elements and starting to separate the .cpp files to  organize function into groups of what they are for.

[jolievivienne.imgur.com/all/](http://jolievivienne.imgur.com/all/)

Vivienne

-------------------------

thebluefish | 2017-01-02 01:05:14 UTC | #2

[quote]jolievivienne's images are not publicly available.[/quote]

-------------------------

vivienneanthony | 2017-01-02 01:05:14 UTC | #3

[imgur.com/gallery/IZzeu/new](http://imgur.com/gallery/IZzeu/new)

Problems I have.
1. Making sure the UI windows are clickable and update based on time like every 5 seconds, on event change, or from a queue of updates, and refreh button
2. TerrainBlend doen't work it seems so figuring out why! Getting the procedural terrain to fully work again with 1.40
3. Adding health to one of the additional information.
4. Creating a rank to experience.
5. Creating GetAlliance and Faction function so it's standardized and future be pulled from a XML or DB
6. Separatin console and create character code  into a separate file. (Might be a good idea).
Clean up ad-hoc code.

I'm separating the code just in case someone would like to help and parts of it can be done by different people. I separated the models and resources for textures etc into a separate folder.

[github.com/vivienneanthony/Urho ... -Existence](https://github.com/vivienneanthony/Urho3D-Mastercurrent-Existence)

-------------------------

JTippetts | 2017-01-02 01:05:14 UTC | #4

None of those images contain profiling information, so it's pretty hard to say where your bottlenecks are. I'd recommend enabling the debug profiling console. It'll show you how much frame time is being spent in render, in update, etc...

-------------------------

vivienneanthony | 2017-01-02 01:05:14 UTC | #5

[quote="JTippetts"]None of those images contain profiling information, so it's pretty hard to say where your bottlenecks are. I'd recommend enabling the debug profiling console. It'll show you how much frame time is being spent in render, in update, etc...[/quote]

I thiink I had added it before. I have to check later. 

Have you gotten Terrainblend to work with 1.40? Since it worked before, I'm not sure if any mapping was changed.

-------------------------

