Jens | 2022-09-19 17:51:43 UTC | #1

Just wondered if assigning a non-changed value to AnimationState.Time will incur any expense, or should there be a condition to check before doing this in OnUpdate()?

-------------------------

SirNate0 | 2022-09-20 14:02:07 UTC | #2

A very minimal cost as AnimationState.SetTime has the condition check inside it:

https://github.com/urho3d/Urho3D/blob/d4c94ad8104ae3d14eb6d6e4ed0fbfad828e08f4/Source/Urho3D/Graphics/AnimationState.cpp#L172-L184

-------------------------

Jens | 2022-09-20 17:58:01 UTC | #3

Thanks SirNate. I kind of guessed and feel slightly embarrassed I didn't look that up. However, while I've got you on the line as it were, do you think animating a single bone would be much more expensive than the corresponding manual operations, eg. get position/rotational data from other bones and then use to position and rotate the single bone? My guess (or rather hope) is that animating the bone might even be less expensive.
​​
​​​​​​​​​​​

-------------------------

SirNate0 | 2022-09-21 02:57:20 UTC | #4

Not sure exactly what you mean, but it's probably comparable.

It sounds to me that you want to create an animation from one bone and then apply it to another bone. It's probably about the same cost as doing it all "manually". Unless you are doing thousands of these, the performance probably doesn't matter either way. Unless you have good reason to believe this will be the performance bottleneck, just get it done first however and optimize it later if it is in fact an issue. I suspect if it ends up being an issue you will want to use C++ for it and do the optimization there in any case.

-------------------------

Jens | 2022-09-22 11:28:01 UTC | #5

Ok thanks, I guess it is only one bone anyway.
It does not really matter now, since the 4 animations (2 for the character and 2 for the object he is holding) are not aligning properly - close, but not good enough. So, I'm back to doing it the original way - the problem there, that made me try animating the held object in the first place, has been made into a [new post](https://discourse.urho3d.io/t/is-it-possible-to-get-new-bone-positions-directly-after-animationstate-addtime-called/7330).

-------------------------

