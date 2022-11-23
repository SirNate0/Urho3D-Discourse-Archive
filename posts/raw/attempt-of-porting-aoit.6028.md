ab4daa | 2020-03-29 07:13:53 UTC | #1

This is my attempt to port [AOIT](https://software.intel.com/en-us/articles/oit-approximation-with-pixel-synchronization) into Urho3D for having as many beams/particles as possible.

It only works in DX11 and forward rendering.

The branch is at:
https://github.com/ab4daa/Urho3D/tree/AOIT

UAV part is ripped from 

https://discourse.urho3d.io/t/rasterized-voxel-based-global-illumination/2115

with some modification to be able to declare shader buffer(UAV) in renderpath xml.

HLSL part is literally 99% copy-paste from the sample in [AOIT](https://software.intel.com/en-us/articles/oit-approximation-with-pixel-synchronization).

### Result
I added two modified original samples 98_AOITLightTest and 99_HugeObjectCountAOIT.
Both can switch renderpath in runtime to check difference.

98_AOITLightTest is modified 07_Billboards to check lighting.
Have to say it is not doing well if there are many transparent objects overlapped.
![圖片|638x499](upload://eQBhJWki8U05hv2SFFol2cMIjw9.jpeg) 
Compare to built-in renderpath:
![圖片|641x500](upload://jZw7ZjbAhHJggiV8jP0HPapMAly.jpeg) 
The FPS is not doing well either because cannot use instancing(~50% FPS of Froward renderpath).

99_HugeObjectCountAOIT is modified 20_HugeObjectCount, which just set transparent material to all boxes.
In scenerio of group on and animation on, the FPS on my laptop:
| Sample | 20 | 99(Forward) | 99(ForwardAOIT) |
| :----: | :----: | :----: | :----: |
| FPS | 73 | 27 | 59 |

Maybe it is worth to merge this to my project to see if it will have FPS gain :yum:.

### Some notes
1. Intel sample has only 1 pass which does all shading/lighting in it, but I am not capable to modify Urho3D to that way. 
I construct visibility function in `aoit` pass, then reuse it in `litaoit` pass, this means if an object only has `litaoit` pass in its technique will produce unexpected result because it does not participate visibility construction. (All transparent objects needs to have `aoit` pass).
But reusing visibility function also produce inaccurate result because some info is already dropped in aoit pass, which always merges furthest pixel into last node. I compensate by a noob way which does not do much.

2. When drawing `litaoit` pass, I don't know why do I have to declare all UAV as ROV.

https://github.com/ab4daa/Urho3D/blob/AOIT/bin/CoreData/Shaders/HLSL/AOIT.hlsl#L210-L218

And check if the depth is used. 
The geometry and world proj view matrix should be all the same in alpha and litalpha pass, isn't it??
So shader should get the same depth in lit pass, but....

https://github.com/ab4daa/Urho3D/blob/AOIT/bin/CoreData/Shaders/HLSL/AOIT.hlsl#L361

Without the two things, lit rendering will look like having race condition problem, but unlit alone is OK. 
I really have no idea....:crying_cat_face: but just put them together to make it work.

-------------------------

