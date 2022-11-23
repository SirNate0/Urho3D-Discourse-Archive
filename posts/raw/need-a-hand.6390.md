Modanung | 2020-09-14 01:02:13 UTC | #1

[![](https://www.luckeyproductions.nl/images/hand.png)](https://hands.luckeyproductions.nl/)

I plan to extend the model with keyshapes/morphs for some variation along with a [hand IK component](https://gitlab.com/Modanung/hantik) that knows enough gestures to speak some sign language and can grab basic shapes of various dimensions.

-------------------------

Modanung | 2020-09-15 18:21:21 UTC | #2

The fingers now have control bones which through their XY scale can bend and spread fingers. This essentially condenses the bones into sinews - defined by two floats - and allows for a human readable [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)-like format that I think I'll call **PiRMIT**.

![Sinews|631x500](upload://2MPfQbuU58KiawiJxFu7FnlUVC1.png)

Currently I'm thinking of using a structure that (in Regex terms) looks something like this:

```
([A-Z]+([0-7]+[a-h]+)*)+
```

Which would make `P0aR0aM0aI0aT7h` a thumbs up, or even `PRMI0aT7h`. But please share you're thoughts if you see ways in which the format could be improved.

Alternating numbers with letters allows for arbitrary precision as well as an extensible number of variables. Seperating (or post-/suffixing) values with a colon could imply a range or keyframes.
Using unique capital letters makes it possible to group values in any order. For instance, a peace sign could be `IM7hPRT0a`. W may control the wrist. Considering a default value of `0a` - a fist - we get `T7h` for a thumbs up and `MI7h` for peace... along with the possibility of doing math:

`T7h + MI7h = MIT7h`

-------------------------

SirNate0 | 2020-09-15 17:03:43 UTC | #3

Can you explain the 0-7 and a-j portions? And I find it odd that you chose the 10 digit portion to be letters and the numbers to be base 8. But perhaps it will make sense when you explain.

-------------------------

Modanung | 2020-09-15 18:07:57 UTC | #4

You're right; a fumble in the conceptual juggling. Thanks, fixed.

I think I settled on octal. :slightly_smiling_face:

-------------------------

SirNate0 | 2020-09-15 18:33:49 UTC | #5

It would be weird, but I think base 9 would actually be better, assuming they are linearly spaced - then you have positions that are half way between the others (4 is halfway between 0 and 8, 2 halfway between 0 and 4, etc.). If you do multiple digits I'd actually recommend a modified base 8 where the digit 8 would be equivalent to adding 1 to the higher order, s.t. 10 and 8 would be equivalent numbers. Though I'm assuming they're all fractional in practice, so it would be better to say that 1.0=0.8 and 0.2=0.20=0.18.

-------------------------

Modanung | 2020-09-16 01:48:44 UTC | #6

Wouldn't you want to add 1 to the _lowest_ order within the modified system your suggesting? Furthermore a value of 1.0 does not need any precision and could therefor be represented by a special character, like `^`.

-------------------------

Modanung | 2020-09-16 08:41:52 UTC | #7

This way we get:

char | value
---|---
0 / a | 0.0
1 / b | 0.125
...|...
4 / e | 0.5
...|...
7 / h | 0.875
01 / ab | 0.015625
71 / hb | 0.890625
^ | 1.0

-------------------------

Modanung | 2020-09-16 12:30:11 UTC | #8

If it works for hands, it may also be useful for faces or entire bodies. This would make it convenient to allow grouping. For instance `Hr[T^h]Hl[IM^^]F[M4dB6c]` could pose two hands, the mouth and brow. As sign language often uses more than just one hand, it would also require such a feature.

I see no reason to be picky about brackets; using `()`, `[]` and `{}` could be equivalent. But that might change with the introduction of other features.

However `<>` may be used to define interpolation methods:

char | Interpolation
---|---
 `<>` | Default
 `</>` | Linear
 `<->` | Ease in
 `<+>` | Ease out
 `<-+>` / `<+->` | Ease in and out
 `<-[0-^][a-^]+[0-^][a-^]>` | Cubic bezier curve

-------------------------

Modanung | 2020-09-17 14:02:21 UTC | #9

To communicate a model's limits - i.e. the meaning of these normalized values in angles for each bone in the chain - a similar format would be handy. Knowing these angles allows for calculating the required values for setting the chain endpoints - based on the bend ratios that can be derived from them - to a certain distance from its local root. These _forward_ kinematics could simplify the _inverse_ kinematics, effectively reducing each chain to a single bone within the problem.

-------------------------

Modanung | 2020-09-17 09:31:31 UTC | #10

For polylimbed entities the `'` could be used for specificity; for instance `H[IM7h]Hr'[$Vulcan]` would set Shiva's hands to peace signs, with the exception of his first right hand.

-------------------------

Modanung | 2020-09-21 00:58:29 UTC | #11

The latest PiRMIT definition can be found [here](https://gitlab.com/Modanung/hantik/-/tree/master/pirmit). Feel free to submit suggestions and feature requests as issues or PRs, or to extend the [Holodex](https://gitlab.com/luckeyproductions/hantik/-/wikis/Holodex).

-------------------------

Modanung | 2020-09-21 01:01:14 UTC | #12

[PiRMIT molds](https://gitlab.com/luckeyproductions/hantik/-/blob/master/pirmit/red.md#molds) could be included with a model and provide enough information to generate a ragdoll. These molds form a translation layer between normalized animations (or poses) and a model's bone transforms. I imagine this should make animations quite transferable between characters and easier to define, as the molds map bones to a more overseeable (and agreeable) tendon-like structure.
This means PiRMIT *poses* basically do not care about the hierarchy and names of bones, as it is the *mold* that translates the meaning of e.g. a fully stretched finger to a collection of bone transforms.

[![](https://gitlab.com/luckeyproductions/hantik/-/raw/master/pirmit/overview.svg)](https://gitlab.com/luckeyproductions/hantik/-/blob/master/pirmit/README.md)

-------------------------

