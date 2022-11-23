extobias | 2019-10-24 19:10:06 UTC | #1

Hi there,
Shouldn't the PBRDiffNormalEmissive.xml technique have the base pass enabled?


[https://github.com/urho3d/Urho3D/pull/2531](https://github.com/urho3d/Urho3D/pull/2531)

-------------------------

extobias | 2019-10-20 12:44:38 UTC | #2

I've got some captures. On left is the actual technique, and in right is with the base pass.
I think some of the techniques (like alpha's) shouldn't use the base pass, but I don't know why they aren't in this one.

![image|690x224,75%](upload://tgalGPRQHEpHkHeDmIzwCQZvmNT.jpeg)

-------------------------

Modanung | 2019-10-23 09:51:15 UTC | #3

Seems like it needs that pass.  Could you PR'ify?

-------------------------

extobias | 2019-10-24 18:01:12 UTC | #4

I've submit a draft PR. Should I do anything more?

-------------------------

Modanung | 2019-10-24 18:21:08 UTC | #5

Link to it. :slight_smile:

-------------------------

