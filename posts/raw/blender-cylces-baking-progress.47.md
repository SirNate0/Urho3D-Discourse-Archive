friesencr | 2017-01-02 00:57:35 UTC | #1

I am super pumped about this.

[wiki.blender.org/index.php/User: ... ry_30th.29](http://wiki.blender.org/index.php/User:Dfelinto/Foundation#Week_19_.28January_30th.29)

Having a high quality renderer to bake gi sounds wonderful.

-------------------------

JTippetts | 2017-01-02 00:57:38 UTC | #2

Oh, man, that's awesome to hear. I love Cycles, and have used it a lot to pre-render tilesets and animations, but I've been waiting for them to support baking for a long time.

-------------------------

JTippetts | 2017-01-02 00:58:04 UTC | #3

Some user builds with the Cycles baking branch are starting to appear on graphicall: [graphicall.org/1105](http://graphicall.org/1105)

I've tried it out. Even as obviously unfinished as it is, it's awesome. Some things are still in progress (such as tangent-space normal baking) but what has been done rivals or exceeds Blender Internal bake, as far as I'm concerned. This is a pretty awesome development, and it looks like it's getting plenty of user support so DFelinto is really making some progress on it. There is a community discussion thread about it at [blenderartists.org/forum/showthr ... ng-is-here](http://blenderartists.org/forum/showthread.php?326534-Cycles-baking-is-here) if anyone is interested.

-------------------------

friesencr | 2017-01-02 00:58:05 UTC | #4

We've been learning cylces all week.  The results are amazing.  We are having bleeding issues on the bake and don't want to screw up our uvs.  We have to wait until they get bleeding controls (which they might have a couple of days ago).

-------------------------

boberfly | 2017-01-02 00:58:34 UTC | #5

Yeah I've been tracking this for awhile as well. I'm also interested in cycles stand-alone rendering. Nothing would be stopping you from having cycles launch in the background from the Urho3D editor and using Urho's hot-reload function to see the result (especially setting up cycles to write to file every x amount of samples). Pretty cool options here.

Or even have it link directly to Urho3D as it's Apache 2.0 licensed now. Making cycles read the urho scenes and mdl files directly would save you from making a cycles-specific scene file (which is currently all XML, even the model files).

-------------------------

friesencr | 2017-01-02 00:58:37 UTC | #6

I havn't figured out how instanced geometry can get its own uv set for the shadow map.  Does anyone have any insight what a good way to approach this?

-------------------------

cadaver | 2017-01-02 00:58:37 UTC | #7

That would mean "de-instancing" the objects and modifying their models/geometries to for example include a second vertex buffer with the lightmap UV coords data.

If the system would be smart, it could happen in-memory during load time, so the project would not need to actually save the modified models as files on disk.

-------------------------

boberfly | 2017-01-02 00:58:40 UTC | #8

Maybe for heavily instanced geo it is best to just have dynamic lighting on these, and just have cavity/AO. 

Another trick might be to make one large atlas texture (like a sprite-sheet) that holds multiple bakes of the same UVs and just offset the UVs based on index/instance ID in the vertex shader?

-------------------------

