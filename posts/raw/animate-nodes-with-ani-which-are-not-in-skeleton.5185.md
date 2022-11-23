Dave82 | 2019-05-26 08:15:13 UTC | #1

As i see currently we can use AnimationController and .ani files to either animate nodes in a hierarchical structure or Bones inside an AnimatedModel but we can't have both ! I have an ani file with extra tracks which are not part of the skeleton and it seems that if i load the ani file and play it, these extra nodes are not recognized by AnimationController...

Example : I have an ani file with all the skeleton animation + one extra track called "turnAnimatorNode" this is a simple node which exists in the structure of my character but the AnimationController does not see this node however a track with this name exist in the ani file...
So is there any way to add this node manually to the AnimationController ?
EDIT:  So reading the docs i realized if we want to drive node transformations in a node we cant have AnimatedModel inside the same node... I can live with that but that also mean for every additional non skined animation i need one extra ani file which is a bit annoying

-------------------------

Leith | 2019-05-26 08:15:23 UTC | #2

Hi, Dave82!

Are you using the AssetImporter tool? If so, there's a way to force "non-skinning bones" to be included in the model's skeleton. I think because non-essential bones are stripped out by default, so too are any animation tracks associated with said bones.

[quote]
-s <filter> Include non-skinning bones in the model's skeleton. Can be given a
            case-insensitive semicolon separated filter list. Bone is included
            if its name contains any of the filters. Prefix filter with minus
            sign to use as an exclude. For example -s "Bip01;-Dummy;-Helper"
[/quote]

-------------------------

Dave82 | 2019-05-25 11:13:45 UTC | #3

Thanks ! It seems i missed this when i read the options... Anyway thanks !
EDIT : Still trying to figure out how to mark a post as a "solution"... :thinking:
EDIT2 : For everyone who try to export non skinning nodes , please note : The nodes must be inside the skeleton structure otherwise the -s option won't export it. (e.g if you attach the node directly to your character outside the root node it won't work)

-------------------------

Leith | 2019-05-26 04:33:57 UTC | #4

If you posted this in the subforum Discussions/General Discussions, you would see a "solution checkbox" but that does not appear when we post to the root Discussions category. I don't know why.

-------------------------

Modanung | 2019-05-26 08:15:07 UTC | #5

Actually it's only the _Support_ threads that can be solved.

-------------------------

Leith | 2019-05-27 07:11:14 UTC | #6

I noticed a comment last night in the docs for AssetImporter that mention something about animations on non-skeletal nodes being automatically exported when we use the model or scene modes - that must be the "junk ani" I noticed being dumped out when I exported my models.

-------------------------

