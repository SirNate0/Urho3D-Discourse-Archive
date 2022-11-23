cin | 2017-01-29 05:59:29 UTC | #1

I'm restore access to my repositiry of the game.

[bitbucket.org/cin/outbreak/down ... utbreak.7z](https://bitbucket.org/cin/outbreak/downloads/Outbreak.7z) (30.7 Mb)

[bitbucket.org/cin/outbreak](https://bitbucket.org/cin/outbreak)



[url=http://i.imgur.com/ZPe8WwP.jpg][img]http://i.imgur.com/p0f6Fdr.jpg[/img][/url] [url=http://i.imgur.com/WRiQBcY.jpg][img]http://i.imgur.com/ykK29qx.jpg[/img][/url]  [url=http://i.imgur.com/DFnGiK1.jpg][img]http://i.imgur.com/K9g8hQd.jpg[/img][/url]

[spoiler][video]http://www.youtube.com/watch?v=pl2qJHTt5sY[/video][/spoiler]

-------------------------

rasteron | 2017-01-02 01:03:42 UTC | #2

Hey Vladimir,

I remember this project from the old google groups forum and showcase, it looks good  :slight_smile:  definitely will try this!

-------------------------

weitjong | 2017-01-02 01:03:42 UTC | #3

I remember this one too. Thanks for sharing it.

-------------------------

cadaver | 2017-01-02 01:03:43 UTC | #4

Like I probably said before, as a reverse-engineering effort this is excellent. Should also be helpful in real-world performance tuning of Urho.

EDIT: Just to be sure, what is the legal status of the Codename Outbreak assets, seeing that there are converted models in the repository? Do you have permission from the original authors to put them online?

-------------------------

cin | 2017-01-02 01:03:43 UTC | #5

Hmmm.... some source-files is lost. I try to restore it and make compilable version of game.

-------------------------

cin | 2017-01-02 01:03:43 UTC | #6

I'm create new repository - link in post #1.

-------------------------

sabotage3d | 2017-01-02 01:03:43 UTC | #7

Looks really cool :slight_smile:
 Is it playable at the moment ?

-------------------------

cin | 2017-01-02 01:03:45 UTC | #8

May be. =) Player can run over level and shoot. I'm reconstruct only first level. For next level it many manual work of finding corresponding textures and texturing extracted level. I'm cannot doing this by one. No present any type of AI (bots and so on).

-------------------------

cin | 2017-01-02 01:03:47 UTC | #9

Video in first post added.

-------------------------

christianclavet | 2017-01-02 01:06:23 UTC | #10

Thanks for posting this! This was really great to look at to study and learn more about URHO 3D! You made a really great job with the all the sounds!

I was able to load your first level in the URHO editor and saw how you managed to have walk sound changed by walking on a specific object using custom defined variables for nodes!

-------------------------

cin | 2017-01-02 01:08:02 UTC | #11

Time to show my current work. I try to recreate first level of remake from zero - all models created by me. Trees generated in ngPlant. Trees: 5 levels of detail, last level - very simple cross planes with texture.
 Terrain modelled manually. Triplanar texturing. Size of level: 500x1000 meters.
~2 million triangles in frame. 
This is not final picture of scene. Some things is missing - stones, damaged trees, bushes and some buildings. Work in progress.
[url=http://i.imgur.com/HT1SeoC.jpg][img]http://i.imgur.com/nRlzQe9.jpg[/img][/url] [url=http://i.imgur.com/YADUQlH.jpg][img]http://i.imgur.com/Hgjo5DN.jpg[/img][/url][url=http://i.imgur.com/Stsio3y.jpg][img]http://i.imgur.com/JGwrwUk.jpg[/img][/url]

-------------------------

Bluemoon | 2017-01-02 01:08:02 UTC | #12

Simply awesome  :slight_smile:

-------------------------

rasteron | 2017-01-02 01:08:02 UTC | #13

Hey, getting better! really nice work :slight_smile:

-------------------------

cadaver | 2017-01-02 01:08:03 UTC | #14

Very nice "last gen-AAA" (or how I should say that) look.

-------------------------

TheKissingZombie | 2017-01-02 01:14:47 UTC | #15

Could you tell me how you managed to access the files in CO directory? I've been trying everything to rip the models from the game and bring them into Blender but nothing works... is there an SDK or an unpacker for this?

-------------------------

Lumak | 2017-01-14 18:14:48 UTC | #16

There is no license information on bitbucket. I'm wondering if assets are creative-commons (CC) license and can be used for an open source demo?

-------------------------

1vanK | 2017-01-14 18:55:59 UTC | #17

I think assets from original game and not free

-------------------------

Lumak | 2017-01-14 19:43:22 UTC | #18

OK, thx. -- 20 chars

-------------------------

coldev | 2017-05-15 20:20:58 UTC | #20

Thanks to share code.. God Bless You ...

-------------------------

LiamM32 | 2017-09-11 21:06:41 UTC | #21

Thank you for this.  I want to learn from this, as I'm looking for an example of how to structure a big program with multiple source files.

But may someone please give me instructions to compile for Linux?  I didn't manage to get it to work.

-------------------------

1vanK | 2017-09-11 23:46:18 UTC | #22

sources is very old and require many changes for compiling with current version of engine

-------------------------

WangKai | 2017-09-13 01:11:51 UTC | #23

By 'Last gen' you mean diffuse + normal + specular?
Maybe @cin could try PBR workflow to make everything current gen if the target platform is not mobile. Though it even takes more time and hard to create the physically based art assets.

-------------------------

