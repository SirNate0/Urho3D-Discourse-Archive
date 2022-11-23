Modanung | 2017-04-26 13:19:18 UTC | #1

Is there a reason why morph weights are limited between 0 and 1, other than protecting us from unintended results? If so I would like to propose lifting this limitation altogether (and getting the same result with a `Clamp`) or being able to set the `min` and `max` for each weight (like in Blender), defaulting to 0 and 1.
There are situations where a weight greater than 1 - or even negative - is very useful. Since morphs are merely vertex offsets, the effect can easily be multiplied by any scalar.
It seems removing [this line](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/AnimatedModel.cpp#L562) would be the simplest solution.

-------------------------

cadaver | 2017-04-27 09:53:39 UTC | #2

Could be removed, just need to change the check above to check for anything else than 0 and generate the morph VBs in that case.

-------------------------

Modanung | 2017-04-27 10:35:02 UTC | #3

Right, [this check](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/AnimatedModel.cpp#L1372).

Will do. Maybe tonight. But don't let this stop anyone else.

-------------------------

cadaver | 2017-04-27 12:58:05 UTC | #4

I already pushed a change to master, but missed that check. Will update.

-------------------------

Modanung | 2017-04-28 00:26:40 UTC | #5

Awesome! :grin:
Thanks again

-------------------------

hicup_82017 | 2017-09-19 14:31:00 UTC | #6

hi @Modanung/ All 
I am planning to experiment on negative weights for vertices. Even though I tried to add a negative weights through script in blender, it just gets clamped between 0 and 1. 
So I thought to adjust the vertex.weights buffer parameter in Reattiva exporter. 

Now, **Does Urho supports negative weights?** My weights will be of order -1 to 1 float.

-------------------------

Modanung | 2017-09-20 02:24:15 UTC | #7

In Blender there's two field under _Range_, namely _Min_ and _Max_ that set the limits per key. By default they are set to 0 and 1 respectively.
Urho's morph weights used to get clamped between 0 and 1, but can now be set to any value. You can use the `Clamp` function to apply limits.

-------------------------

hicup_82017 | 2017-09-20 07:34:08 UTC | #8

That helps me.
By any chance do you guys aware of any algorithm or procedure to select the best 4 weights from -1 to 1 weight. 

**My analysis:**
1. I verified Reativa exporter for the answer, I found exporter finds the largest four weights and then normalizes them to get the sum of the 4 best weights to 1. This gave me decent understanding about approximation of positive weights, but I could not understand how to approximate combination of both positive and negative weights.
2. I thought to take best negative and best positive weights, to make a total of 4 and then normalize them using unity-based normalization.

-------------------------

Modanung | 2017-09-20 10:43:24 UTC | #9

I must say I'm not quite following you.
What are you trying to achieve?

-------------------------

hicup_82017 | 2017-09-20 14:09:29 UTC | #10

I am trying to use bone influences which are both negative and positive (these are weights) for vertices.
Now, Game engines want only 4 of these bone influences to effect a vertex. In my application I might have more bones effecting a vertex, but I should make a choice of selecting best 4 weights out of the total weights.
**So, All I am trying to do is, finding the best 4 weights from both negative and positive weights**. 
After I found the best 4, I can normalize and get them to Urho.

-------------------------

Modanung | 2017-09-20 14:24:55 UTC | #11

Hm, could it be that you are confusing bone weights (vertex groups in Blender) with morph weights (shape key values in Blender)?
Or are their limitations related in a way I'm unaware of?

-------------------------

hicup_82017 | 2017-09-20 14:48:15 UTC | #12

 :slight_smile: I think I found the wrong thread.
I am targeting bone weights to experiment with mesh deformation algorithms.

-------------------------

Modanung | 2017-09-20 14:50:42 UTC | #13

That resolves my confusion. :upside_down_face:

-------------------------

