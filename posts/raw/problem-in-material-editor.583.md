rogerdv | 2017-01-02 01:01:31 UTC | #1

I have been experiencing a weird problem in Material Editor since I started using the editor. When I try to change the Technique using the pick button, it reverts to previous one. I have to manually type the technique name and press enter. Is this a known bug or it happens only to me?

-------------------------

codingmonkey | 2017-01-02 01:01:31 UTC | #2

the file of this material has a read-only attribute ?

-------------------------

rogerdv | 2017-01-02 01:01:31 UTC | #3

Nop, the problem is the same for already created materials or new ones. When I started, I had to manually edit the xml files, until I discovered that I could type the name, which is just marginally better than fixing by hand.

-------------------------

codingmonkey | 2017-01-02 01:01:31 UTC | #4

OK, maybe you need to run the editor under admin rights ?

And when you make changes to the inspector material you click save button ?)

If you save it to another file you have to select it again in the inspector model (repick with new material name)

-------------------------

rogerdv | 2017-01-02 01:01:32 UTC | #5

Save works perfect, the only problem is picking the technique. I will try admin rights to see what happens.

-------------------------

hdunderscore | 2017-01-02 01:01:33 UTC | #6

I noticed this issue today while working on a scene, it seems to occur if you select a technique from a path external from your editors resource path. It should work if you are working from the correct directory.

-------------------------

rogerdv | 2017-01-02 01:01:34 UTC | #7

So, the resource path should be Bin and not Data?

-------------------------

hdunderscore | 2017-01-02 01:01:34 UTC | #8

No, in my case I have Urho3D in multiple locations, so I was running:
F:/Urho3d/[b]Master[/b]/Bin for the editor, but my main installation is:
F:/Urho3d/[b]Engine[/b]/Bin

When I was running the [b]master [/b]version, tried to load a technique, it was automatically searching in: F/Urho3d/[b]Engine[/b]/Bin/Data -- but if I load the technique from there, it won't work.

-------------------------

rogerdv | 2017-01-02 01:01:34 UTC | #9

What I usally do is to set the resource path to the data forlder of the project Im working on. Otherwise I get errors about textures not found.

-------------------------

