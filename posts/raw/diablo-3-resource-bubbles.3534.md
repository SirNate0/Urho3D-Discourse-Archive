JTippetts | 2017-09-07 03:40:28 UTC | #1

I wrote a blog post about recreating Diablo 3's resource bubbles (as talked about at https://simonschreibt.de/gat/diablo-3-resource-bubbles/ ). You can find the blog post, with a link to a zipped up working example, at https://www.gamedev.net/blogs/entry/2263632-diablo-3-resource-bubbles/

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bfaaa0cd92bf320b0cede190d2b023c218ac546f.png'>

The linked example includes GLSL shader code to implement the effect. A shader uniform, Level, is specified in the range of 0,1 and determines the level of fluid in the bubble. A scrolling noise texture provides lively surface froth for the top of the fluid. The bubble could be rendered to a texture for actual display on the UI, though the example doesn't include such functionality. It's an example of a relatively simple effect that has pretty nice visual impact.

Edit: github repo link: https://github.com/JTippetts/D3ResourceBubbles

-------------------------

Lumak | 2018-05-17 20:57:28 UTC | #2

I got tired of trying get UI blending working properly for hours on end... and finally gave up.  Instead, I moved ahead and added a custom shader functionality in UI and UIElement.  See the pic below. This basic class that I created basically parses a mdl file and creates UIBatch from it, ~~creates shader from~~ uses material like any other class that deals with mdl file, and renders at UI render cycle. Just got the initial phase done, and no where near polished.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/d7718bcdea7caccb366a67a8fc5188984e5cf6d7.png[/img]

edit: bah, it doesn't create shader, but used material.

-------------------------

Lumak | 2018-05-17 21:17:06 UTC | #3

discarding mask:

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/54587b8966cb417022f441d48e44cf8dd3aba2ef.png[/img]

-------------------------

Lumak | 2018-05-18 07:35:31 UTC | #4

@JTippetts, I got most of the features worked out including something that I needed for my game.  And since you provided the bubble resource I'm guessing that's something you want/need to add to the game you're making. The code that I'm working is in my personal sandbox but I can integrate it to 1.7 and email it to you.

Here's a sample:

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/b/b21c18997e964b1ff01a71b38ee8740cd8631408.gif[/img]

edit: replace the gif w/ a smaller image

-------------------------

