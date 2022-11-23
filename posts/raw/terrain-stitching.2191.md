monkeyface | 2017-01-02 01:13:48 UTC | #1

Has anyone got code to stitch 2 terrain tiles together?

If not, as a quick hack I can just set the LOD of the patches at the edge of the terrain to just fix to max LOD, so they will always match up. Is there a way to do that?

Thanks.

-------------------------

cadaver | 2017-01-02 01:13:48 UTC | #2

The terrain patches update on their own, so you need engine changes for that. A pull request is welcome, I can also look into it at some point, it shouldn't be difficult.

-------------------------

monkeyface | 2017-01-02 01:13:49 UTC | #3

[quote="cadaver"]The terrain patches update on their own, so you need engine changes for that. A pull request is welcome, I can also look into it at some point, it shouldn't be difficult.[/quote]

Thanks!
Would be awesome if you could implement something in the core for that... perhaps you could just add a way that the terrain itself can have neighbours too...and it ensures the LODs match up along that edge. I guess that wouldn't take you more than an hour or two with your ninja powers? :smiley:
That way we could have really huge terrains without needing all the data in memory at the same time.

-------------------------

cadaver | 2017-01-02 01:13:50 UTC | #4

Done in the master branch. You can now set neighbor terrains. For it to work properly, they must have the same number of patches at the edge and the neighbors have to be set both ways (e.g. A's south neighbor is B, B's north neighbor is A)

-------------------------

monkeyface | 2017-01-02 01:13:50 UTC | #5

Wow, that was fast. Thank you! I will give it a try :slight_smile:

-------------------------

