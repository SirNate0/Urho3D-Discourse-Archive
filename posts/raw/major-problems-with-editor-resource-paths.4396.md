solorvox | 2018-07-17 16:38:24 UTC | #1

Hello, I’m having a lot of problems with Editor and materials/resource paths.  

Here are my actions to get breakage:

Run Editor.sh from local "Project/Resources" directory containing “Local”, “CoreData” and “Data.” 

1) View/Material Editor
2) [New] (new material button very bottom left)
3) Under Techniques select [Pick]
4) Browse to “CoreData/Techniques” that is in the local Resource directory
5) Select Diff.xml and press [OK]

Result, no changes to technique.  No changes can be made to material.  Existing bugs show this might be problem with resource path.

6) File/Set resource path...
7) Don’t change anything, just press [Set]
8) Material editor starts working


This is fine until you load a scene.

9) Open scene..., Select scene “Local/Player.xml” and [Open]
10) Editor has changed resource path to the current directory of the scene.  File/Set resource path... now shows “Resources/Local/” instead of Resources/
11) Material editor is broken again.

Sometimes I can get editor working but then the paths to materials/textures/models is incorrect due to relative path changes when I then try and load the scene in the C++ compiled game.

I've tried almost every possible combination of Editor.sh -p/-pp with full and relative paths and all break in some at some point.  Almost always after loading any scene.  Tried with and without remember resource path, and launching Editor.sh from different directories.

Tested on 1.7 stable and latest version git master updated July 18 2018. 
commit b0f2b5a94f567465bfb1f88427e5e2924552a2bb

Linux Mint 18.3 64Bit

Can anyone help?

-------------------------

Lunarovich | 2021-02-06 09:48:51 UTC | #2

Is there any update on this? I have the same problems and have tried the same solutions and practically nothing works.

The only thing that works is to launch the Editor from the *bin/* directory and to set a path to the *bin/* directory. Both of this steps are necessary.

To be clear, my goal is to use *bin/* as a resource path.

-------------------------

Eugene | 2021-02-06 13:17:53 UTC | #3

Every time I worked with Editor I used to explicitly configure necessary folders as command line arguments.

-------------------------

throwawayerino | 2021-02-06 15:42:48 UTC | #4

Maybe ensure you're using master branch and remove any `Data.pak` files? They come with a default bin folder and are loaded automatically.

-------------------------

Lunarovich | 2021-02-08 19:39:59 UTC | #5

[quote="throwawayerino, post:4, topic:4396"]
lly.
[/quote]

Thnx. Wasn't able to compile the Urho3D, so I'm using 1.8 alpha 2. Will try it though, since Editor greatly enhance my workflow.. Hopefully it works.

-------------------------

