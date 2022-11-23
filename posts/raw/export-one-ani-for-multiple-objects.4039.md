berrymooor | 2018-02-22 18:58:46 UTC | #1

Hi, I make the animation group of falling cubes in Cinema4D and export baked keyframes animation to
fbx > Blender > AssetImport as a result I got bunch of .ani files that relate specifically to one cube in all model, but not overall animation *.ani

So, question is how to merge or combine all keyframe tracks together and get one *.ani  (cause i implement scene animation in ActionScript)

![Screen%20Shot%201|356x457](upload://vg14kZNZJkY9Lr6kc4c9RAathu5.png)![Screen%20Shot|511x500](upload://uD5MmR9FAAoOxDZrF57ct44y76j.png)

-------------------------

SirNate0 | 2018-02-23 00:42:59 UTC | #2

You could try the blender exporter plugin and see if that gives better results.

-------------------------

RCKraken | 2018-03-27 06:14:56 UTC | #3

As long as you are only editing one action using the action editor, and you are exporting the models as .fbx, then I believe it should output only one animation. Normally I import only animations on rigged models, however I think that using LocRot or LocRotScale will work and create shared keyframes among all the models selected. In the picture below, I am using LocRot keyframes, and am using a single action, which should get exported as one .ani file.

![Capture|690x428](upload://1v7LXcIDW0jcYTkyknGZZC1HuXB.PNG)

-------------------------

slapin | 2018-04-02 02:11:08 UTC | #4

AFAIK you can't do that.

-------------------------

