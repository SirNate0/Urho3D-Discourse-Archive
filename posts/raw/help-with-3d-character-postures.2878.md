savindrap | 2017-03-09 19:44:08 UTC | #1

Hello, I have a 3D character loaded to urho3D and I am able to access each bone node of the 3D character and set them in different postures by applying rotations. Also I have a floor plane loaded as a static model and character is placed on the floor. Now when I try to make my character in sitting on a chair posture, feet are not in contact with the floor and it looks unnatural (refer image).

[http://prnt.sc/ehzibw](http://prnt.sc/ehzibw)

Is there way to get character in expected view? I am not looking into use AnimationController since I want to have different postures like sitting on the ground, squatting and etc by applying quaternion rotation for bones. In simply, I want to keep the character in contact with the floor despite of it's posture. Reference to any feature sample which has implemented this would be great.

Thanks.

-------------------------

1vanK | 2017-03-09 19:56:00 UTC | #2

1) Place ass bone (root?) on chair
2) Use IK for place feet on ground (look for Inverse Kinematics on forum)

-------------------------

slapin | 2017-03-09 23:39:46 UTC | #3

Well, looking for inverse kinematics on this forum might be too far fetched,
as AFAIK there were no working feet IK published (at least not with recent version of Urho).
Hope somebody could update or explain how it works.

-------------------------

savindrap | 2017-03-10 06:36:04 UTC | #4

@1vanK
Thank you for your answer, I'll check on IK.

@slapin
Yeah I went through the same and yeah it would be great to see working example of IK in Urho.

-------------------------

