0x4D3342 | 2018-07-27 11:34:12 UTC | #1

it seems that urho3d is not support morph of collada,the assetimporter has no proof of it,any guy has good way to slove it,thanks a lot

-------------------------

simonsch | 2018-07-27 13:11:42 UTC | #2

As far as i know the AssetImporter can read Collada files and produce a valid urho3d scene from it. This scene contains the joint information needed for the AnimatedModel. The joint weights are applied via shader code.

-------------------------

