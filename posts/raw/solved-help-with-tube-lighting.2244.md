dragonCASTjosh | 2017-01-02 01:14:12 UTC | #1

As many of you know i have been working on tube lighting for the past week but i have hit a roadblock that i cant seam to solve so i have decided its time to ask for help of fixing this issue. For tube lights i am following epics PBR paper [url]http://blog.selfshadow.com/publications/s2013-shading-course/karis/s2013_pbs_epic_notes_v2.pdf[/url]. But currently all tube lights act the same as sphere lights with both the radius and length changing the size of the sphere.

All the source code for the area lighting can be found on my fork on urho [url]https://github.com/dragonCASTjosh/Urho3D/blob/master/bin/CoreData/Shaders/HLSL/PBR.hlsl[/url]

-------------------------

cadaver | 2017-01-02 01:14:12 UTC | #2

Do you need new uniforms for lights? In that case check where in the code e.g. the light color uniform is being set, and add there. (Search PSP_LIGHTCOLOR in Batch.cpp)

Note that it'd be preferable to not take the performance hit for setting extra uniforms when non-PBR lighting is used, but that isn't an absolute requirement.

-------------------------

dragonCASTjosh | 2017-01-02 01:14:12 UTC | #3

[quote="cadaver"]Do you need new uniforms for lights? In that case check where in the code e.g. the light color uniform is being set, and add there. (Search PSP_LIGHTCOLOR in Batch.cpp)

Note that it'd be preferable to not take the performance hit for setting extra uniforms when non-PBR lighting is used, but that isn't an absolute requirement.[/quote]

currently its not using uniforms the values are hard coded but they are not having the intended affect and im lost on where its gone wrong.

for reference the section in the paper starts end of page 16 for tube lighting, and the tube lighting method in the shader i linked is my implementation.

-------------------------

dragonCASTjosh | 2017-01-02 01:14:12 UTC | #4

For better reference here is the affect in unreal and the the results of it in urho, it should show what the problem is.

Unreal:
[img]http://i.imgur.com/bwJ0Ilm.png[/img]

Urho:
[img]http://i.imgur.com/1bt7uaL.png[/img]

-------------------------

dragonCASTjosh | 2017-01-02 01:14:14 UTC | #5

Multiplying Pos into [url]https://github.com/dragonCASTjosh/Urho3D/blob/master/bin/CoreData/Shaders/HLSL/PBR.hlsl#L40[/url] causes more of a tube effect, but this is still incorrect results as the tube always points at the player and changes shape. 

[img]http://i.imgur.com/BLhctTQ.jpg[/img]
[img]http://i.imgur.com/iEcYZNO.jpg[/img]

-------------------------

dragonCASTjosh | 2017-01-02 01:14:15 UTC | #6

I think i know where the errors lay although im not sure how to fix it. The following code should work out each end of the tube. L0 and L1 are points at eaither side of the tube, but i feel its calculating it wrong.

[code]
        float3 pos   = (cLightPosPS.xyz - worldPos);
        float3 L01 = lightVec * LightLengh;
        float3 L0 = pos - 0.5 * L01;
        float3 L1 = pos + 0.5 * L01;
[/code]

-------------------------

dragonCASTjosh | 2017-01-02 01:14:15 UTC | #7

Solved, turns out lightVec should be vector you want the tube to point and not the vector of the light from the tube.

[img]http://i.imgur.com/AGrszlW.jpg[/img]

-------------------------

Modanung | 2017-01-02 01:14:16 UTC | #8

Chool

-------------------------

