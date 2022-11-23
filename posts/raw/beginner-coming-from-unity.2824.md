smellymumbler | 2017-02-28 18:46:32 UTC | #1

Hello! I'm currently migrating from Unity to Urho3D, mostly because i don't want me or my modders to be restricted by licenses. I want everyone to be able to hack the game and the best way to do that is to use an open-source engine. Since my game is not very graphics-demanding, Urho seems like a great choice. 

Anyway, i'm just beginning and i'm a little curious about how things work. Is there any book on the engine and how to make small games with it? I'm looking for something focusing on game logic architecture and implementation, not cookbooks or something like that. Also, any tips on how to implement a basic FPS controller on the engine? Do you guys use capsule colliders with a camera attached?

-------------------------

1vanK | 2017-02-28 19:44:51 UTC | #2

Have you seen an example 18_CharacterDemo?

-------------------------

smellymumbler | 2017-02-28 20:11:01 UTC | #3

Yes, i did. That example uses raycasts, right? I was looking for something along the lines of this:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/46a5baca182924a414e6172006cd20f237e00843.png" width="220" height="202">

Raycasts can be a problem with stairs, moving platforms, etc.

-------------------------

jmiller | 2017-02-28 20:14:16 UTC | #4

Hello!

I found the Urho sample programs (CharacterDemo, NinjaSnowWar) to be concise references.

The wikis have some HowTos and recently-updated links to some of the most common forum topics.
https://github.com/urho3d/Urho3D/wiki
[ http://urho3d.wikia.com/wiki/Unofficial_Urho3D_Wiki](http://urho3d.wikia.com/wiki/Unofficial_Urho3D_Wiki)

The various subforums also have a fair bit of contributed code and projects, topics on [url=http://discourse.urho3d.io/search?q=controller]controllers[/url] like http://discourse.urho3d.io/t/character-controller/1468/28 ..

-------------------------

