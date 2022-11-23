I3DB | 2019-01-09 19:43:14 UTC | #1

I'm trying to convert SkeletalAnimation sharpreality feature sample to run on hololens, and have. This sample uses a 'jack' material which has no material, just a color. You can see in the c# code the line setting material is commented out, but that's because the material file is set for notexture. [Here's the file contents](https://github.com/xamarin/urho-samples/blob/f1bcec78cf8b08c19f5bf29ddfd44181c9e47295/FeatureSamples/Assets/Data/Materials/Jack.xml).

Also noticed [the urho3d feature sample uses the kachujin model](https://urho3d.github.io/samples/06_SkeletalAnimation.html), and I'd like to improve the sharpreality sample to use some material. The sharpreality data folder has various 'jack' techniques, but none appear to be wired up to the jack.mdl. 

So am currently searching for the kachujin files. Where are they?

The Skeletal animation code from Urho3d:
https://github.com/urho3d/Urho3D/blob/30b5a97a14104be90795ba10a3b6a52448f4da5f/Source/Samples/06_SkeletalAnimation/SkeletalAnimation.cpp#L130-L131

The skeletal animation code from SharpReality:
https://github.com/xamarin/urho-samples/blob/f1bcec78cf8b08c19f5bf29ddfd44181c9e47295/FeatureSamples/Core/06_SkeletalAnimation/SkeletalAnimation.cs#L89-L90

-------------------------

I3DB | 2019-01-09 22:16:09 UTC | #2

Found it

https://github.com/urho3d/Urho3D/tree/master/bin/Data/Models/Kachujin

-------------------------

