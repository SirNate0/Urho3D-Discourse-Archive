ghidra | 2017-01-02 02:19:26 UTC | #1

I'm starting to get somewhere with my small "simple" project, and thought I could document some of the progress.
Chmup, is a top down shooter, a shmup. It's more or less a playground to test some silly thing. But maybe eventually it will be at least one complete level.

[url=http://i.imgur.com/TbJJde8.gifv][img]http://i.imgur.com/TbJJde8.gif[/img][/url]

And older gif with really bad color depth caused by the glow effect:
[url=http://i.imgur.com/ZpLPrIQ.gifv][img]http://i.imgur.com/ZpLPrIQ.gif[/img][/url]

An even older image that show the glow a bit better:
[url=http://i.imgur.com/0n6Dx0Q.png][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bc91c3f8addf77fc582146499e258b7a0e6db925.png[/img][/url]

Progress shot of outline (edge detection) shader and some shader based running lights.. On an old model that is no longer part of the project...
[url=http://imgur.com/0Yy8VYR][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/62b8bccc861eba5d2c73177c53201c1373c18a08.gif[/img][/url]

Progress shot of the glow effect. using a method similar to unreal. In that it uses 4 buffers of diminishing resolution added together.
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ffbc1723344e6d14fa5fbd71f7ae01c83fa12a87.png[/img]

There are a few other cool effects that I dont really have progress shots on..
There is a LBM 2d fluid simulation that I am using to get the fluidy look on stuff in the top gif.
The edge shader, I could probably do to break down a bit better. And go over in a little more depth.
I will do that in the next post.

-------------------------

Lumak | 2017-01-02 01:15:30 UTC | #2

Impressive looking images. I like the fluid sym effect and your glow looks great as well. The glow seems more radiant than Urho3D's glow.

-------------------------

sabotage3d | 2017-01-02 01:15:30 UTC | #3

Looks great! What is the glow shader based on?

-------------------------

rasteron | 2017-01-02 01:15:30 UTC | #4

Nice work there ghidra! The first image kinda reminds me of Ghost In the Shell effect. keep it up! :slight_smile:

-------------------------

dakilla | 2017-01-02 01:15:30 UTC | #5

Nice

-------------------------

