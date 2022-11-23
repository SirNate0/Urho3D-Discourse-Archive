Jedive | 2017-01-14 21:58:38 UTC | #1

Hello everyone.

I have just discovered Urho3D and I am very impressed with it. As a quick test, I have tried to convert one animated mesh using AssetImporter, but animations don't work. It is this model file:

https://dl.dropboxusercontent.com/u/502828/swat_walk.zip

I am exporting it using:

`AssetImporter model swat_walk.3ds swat.mdl`

I get the following output from the console:

    Reading file swat_walk.3ds
    Writing model <3DSRoot>
    Writing geometry 0 with 31 vertices 150 indices
    Writing geometry 1 with 55 vertices 258 indices
    Writing geometry 2 with 40 vertices 168 indices
    Writing geometry 3 with 22 vertices 96 indices
    Writing geometry 4 with 18 vertices 72 indices
    Writing geometry 5 with 212 vertices 408 indices
    Writing geometry 6 with 40 vertices 168 indices
    Writing geometry 7 with 22 vertices 96 indices
    Writing geometry 8 with 18 vertices 72 indices
    Writing geometry 9 with 16 vertices 60 indices
    Writing geometry 10 with 58 vertices 252 indices
    Writing geometry 11 with 42 vertices 234 indices
    Writing geometry 12 with 22 vertices 120 indices
    Writing geometry 13 with 31 vertices 144 indices
    Writing geometry 14 with 38 vertices 168 indices
    Writing geometry 15 with 27 vertices 84 indices
    Writing geometry 16 with 31 vertices 144 indices
    Writing geometry 17 with 38 vertices 168 indices
    Writing geometry 18 with 27 vertices 84 indices
    Writing animation 3DSMasterAnim length 0.00520833
    Warning: differing amounts of channel keyframes, skipping animation track Waist
    Writing material Material #1
    Copying material texture SWAT.BMP

The file "swat.mdl" and an animation file "swat_3DSMasterAnim.ani" are created (together with the material and texture files), but when I modify the 06_SkeletalAnimation example to use this animated model instead of the Jack one, I get a black screen with the logo on the corner. I can see the static model correctly if I comment out the part of the script where it attaches the AnimationState.

Do the animations need to have a special format?

Thank you very much in advance.

-------------------------

jmiller | 2017-01-15 03:05:24 UTC | #2

Hello Jedive,
I'm unfamiliar with AssetImporter, but maybe this helps explain?

[`https://github.com/urho3d/Urho3D/blob/master/Source/Tools/AssetImporter/AssetImporter.cpp#L1409`](https://github.com/urho3d/Urho3D/blob/master/Source/Tools/AssetImporter/AssetImporter.cpp#L1409)
[code]
// Currently only same amount of keyframes is supported
// Note: should also check the times of individual keyframes for match
if ((channel->mNumPositionKeys > 1 && channel->mNumRotationKeys > 1 && channel->mNumPositionKeys != channel->mNumRotationKeys) ||
    (channel->mNumPositionKeys > 1 && channel->mNumScalingKeys > 1 && channel->mNumPositionKeys != channel->mNumScalingKeys) ||
    (channel->mNumRotationKeys > 1 && channel->mNumScalingKeys > 1 && channel->mNumRotationKeys != channel->mNumScalingKeys))
{
    PrintLine("Warning: differing amounts of channel keyframes, skipping animation track " + channelName);
    outAnim->RemoveTrack(channelName);
    continue;
}[/code]

-------------------------

Jedive | 2017-01-15 11:43:19 UTC | #3

Ok, that seems to be the cause. The model has different number of keyframes on its position, rotation and scale. I hope that the requirement that the same amount of keyframes is required is removed in the future.

-------------------------

Modanung | 2017-01-17 18:25:27 UTC | #4

Until then you could try using the [Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender) exporter.

-------------------------

