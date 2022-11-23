slapin | 2017-04-04 05:03:57 UTC | #1

Hi, all!

How can I implement animation [b]modification[/b]?

I know I can change speed of animation, and use LODs, combine antimations
in different ways, but I want to go as far as [b]removing keyframes[/b].

I have a set of animations, where I want to remove translation from all bones, except root bone,
but keep rotations. How can I do this?
This is needed to [b]retarget[/b] antimations for different size character.

-------------------------

Dave82 | 2017-04-04 08:16:48 UTC | #2

Well i think what you need is 
yourAnimation->GetTrack("BoneName");

Which returns an AnimationTrack* where you can add , remove , modify all keys assigned to this bone.
Be sure you also modify the keyset bitmask if you remove a key channel completely (e.g if you remove the position channel , remove CHANNEL_POSITION from bitmask)

-------------------------

