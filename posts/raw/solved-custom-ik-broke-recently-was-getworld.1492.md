ghidra | 2017-01-02 01:08:07 UTC | #1

fixed, a 100% my fault.
juggling of update orders is what got me. I was not calling the IK and or setting positions in the right place.
Fixed now...

[quote]After some digging it appears my initial diagnosis was incorrect. I believe that GetWorldTransform and GetWorldPosition are not to blame for my newfound issue.
But it's something in my IK code.. Updated question/pondering in following post.

[quote]I have a basic Ik set up that I have been successfully using for a little while..
It' been disabled for a while since I was working on some other stuff.
Turned it back on tonight, and noticed some weirdness.

Using "HandleSceneDrawableUpdateFinished" event, every other frame it looks like I am getting invalid results. Not NANs, but inverted transforms is what it looks like.

I have a hierarchy of nodes, I am trying to get a child of a child of a child. It's almost as if one of the parent nodes is at 0,0,0 in transform or rotation is when I get the bogus values.

This result is both the same for GetWorldTransform and GetWorldPosition.

I'm not sure the best way to confirm or replicate this, but wanted to put it out there in case someone has encountered the same thing, or has a simple test case.[/quote][/quote]

-------------------------

ghidra | 2017-01-02 01:08:08 UTC | #2

I've got a custom IK setup that has been in working condition.
It used some methods presented from this old post [url]http://discourse.urho3d.io/t/solved-ik-foot-placement/1010/1[/url].

Notably, the "HandleSceneDrawableUpdateFinished", Which I am lead to believe/ blindly assume there were some changes that might have effected some of my GetWorldPostion calls, to get information on parent bones/nodes. (At least my first and second reaction is to blame the ( awesome) engine)

What is happening, that only on a few frames the math doesnt resolve and I get some frames that wig out, otherwise, all the other frames solve fine. I shall do more digging to try and pinpoint where the math fails, until then...

Again, I have no concrete examples, or proof. I come to the board in hopes that someone might be able to help me diagnose what might have changed so that I might fix this new issue i'm having.

-------------------------

