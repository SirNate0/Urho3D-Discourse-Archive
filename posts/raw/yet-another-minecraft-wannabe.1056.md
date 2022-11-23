Tinimini | 2017-01-02 01:05:07 UTC | #1

I know it's sow last season to be copying minecraft, but I found this to be a great exercise as this kind of voxel block world has a lot of interesting stuff where I can cut my teeth on 3D programming. I've been fooling around with Unity and jMonkeyEngine before, but only recently found out about Urho3D.
As I said, I'm pretty new to 3D programming and it's been nearly 20 years since I last wrote a line of C++ code, so this is pretty much a learning process for me all around.

Here's a screenshot of what I have currently:

[img]http://i.imgur.com/Cb5I5Xc.png[/img]

-------------------------

GoogleBot42 | 2017-01-02 01:05:07 UTC | #2

It looks good so far. :slight_smile:  Do you use a single combined mesh for each "chunk" or are you using a mesh group for this?  If you use a combined mesh you will get a lot better performance. :wink:

-------------------------

Tinimini | 2017-01-02 01:05:07 UTC | #3

Thanks. It's a single mesh per chunk. With only the outside facing faces of the cubes drawn.
I just got the lighting working. I just need to get the chunk borders to work properly, haven't bothered to do anything about that yet. I'm currently in the middle of refactoring the code to make it a bit easier to move to a mutithreaded terrain generation/light calculation/mesh generation method.

Here's some pics with the lighting. Using DiffUnlitVCol techinque (which is basically just DiffUnlit with vertexcolor defines added. Started to get those white cracks between cubes after starting to use texture atlases. Probably some artifacts caused by floating point imprecisions. Not sure what to do about those yet.
But next I think I'm going to start thinking about multithreading once I get the refactorings out of the way. And after that proper terrain generation.

[img]http://i.imgur.com/iHtrCRO.png[/img]
[img]http://i.imgur.com/KE8W5K6.jpg[/img]

-------------------------

Tinimini | 2017-01-02 01:05:07 UTC | #4

Just finished the first round of restructuring. Most of the stuff (lighting, dynamic chunk loading etc) now stopped working as they don't support the new structure yet, but it looks like the new data structure is much, much better than my old one. First of all, it solved my problem with the chunk boundaries. They are no longer rendered and I don't really have to worry about taking them into account anymore.
And of course the simplified mesh improved the rendering speed and memory consumption quite a lot.
Here's wireframe rendering shots before and after the restructuring.

Before:
[img]http://i.imgur.com/ogfNfJV.jpg[/img]

After:
[img]http://i.imgur.com/x88HrQB.jpg[/img]

-------------------------

Hevedy | 2017-01-02 01:05:09 UTC | #5

Nice work.
You will release something of the code or the project ?

-------------------------

Tinimini | 2017-01-02 01:05:09 UTC | #6

Oh I'm most likely going to make this open source if it actually gets somewhere. I'm still just learning as I go and I don't have too much time to use on this project, so I'm not quite there yet.

-------------------------

umen | 2017-01-02 01:05:23 UTC | #7

Great work ,can you share from where you started , that is what are your references or example source code for you demo?

-------------------------

Teknologicus | 2019-09-10 09:30:19 UTC | #8

@ [Tinimini](https://discourse.urho3d.io/t/yet-another-minecraft-wannabe/1056/3) wrote
> Using DiffUnlitVCol techinque (which is basically just DiffUnlit with vertexcolor defines added.

How would one implement a DiffUnlitVCol Technique?  Can I do it with a custom Technique or to I have to create a custom shader?  Could I please see your code for this?

-------------------------

Tinimini | 2019-09-10 10:51:07 UTC | #9

Oh wow. Talk about a blast from the past :smile: I haven't touched this project in years, but I did still manage to find the source code. It's available here https://bitbucket.org/syvanpera/cubid/
I have no idea whether it even compiles anymore, but for what it's worth, it's all there.

-------------------------

Teknologicus | 2019-09-10 11:06:39 UTC | #10

Awesome!  Thank you! :smiley:

-------------------------

Teknologicus | 2019-09-15 06:43:36 UTC | #11

I just wanted to say think you again.  The Urho3D technique you wrote for vertex colors saved me so much (frustration?).

-------------------------

Tinimini | 2019-09-15 11:44:12 UTC | #12

Nice! I'm glad this is of some use even if I never had the time to continue it.

-------------------------

TheBruhDude | 2020-08-12 17:47:47 UTC | #13

Looks Good. I found this today and wondering if your going to make a pre-release soon for this copy of Minecraft. And what would it be called if you made a game out of it?

-------------------------

Teknologicus | 2020-08-13 18:51:18 UTC | #14

@TheBruhDude at me or @Tinimini?

What I'm working on is showcased at https://discourse.urho3d.io/t/urho3d-cubic-voxel-surfaces .

I still have a ton of work to do before a pre-release.  It's still not even an actual game yet -- right now it's just a cubic voxel engine built on top of Urh3D.  I haven't decided on a name yet.

-------------------------

Modanung | 2020-08-14 01:13:31 UTC | #15

@Teknologicus Have you considered what license to use?

-------------------------

Teknologicus | 2020-08-14 01:38:36 UTC | #16

@Modanung I do plan on open-sourcing (MIT license) it at some point after trying to sell a game made with it.

-------------------------

Teknologicus | 2020-08-14 01:52:25 UTC | #17

PS: I've also considered licensing the code to developers when it's fully functional.

-------------------------

