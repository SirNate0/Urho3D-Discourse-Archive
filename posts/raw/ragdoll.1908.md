Dave82 | 2017-01-02 01:11:25 UTC | #1

Hi ! Did anyone managed to build a ragdoll for a custom (non Jack :smiley: ) model ? I'm struggling with it approximately 6 hours and every parameter i change makes the ragdoll worst :smiley:
Because there are so many parameters to change , i found it nearly impossible to get my ragdoll working by trial and error.Either the constraint rotations are totaly wrong or the character is twiching , but i swear i tried all possible axis combinations and my model still looks like  when the girl form "the exorcist" walks down the stairs upside down :smiley:

Is there any tutorial for this ? Or is it possible to calculate the axes and the high/low limit from some available parameters ? (bone local transform , bone size , etc )

-------------------------

yushli | 2017-01-02 01:11:25 UTC | #2

This may be related to your issue: [topic1969.html](http://discourse.urho3d.io/t/solved-distinguish-collision-of-diff-parts-in-animatedmodel/1882/1)

-------------------------

Dave82 | 2017-01-02 01:11:26 UTC | #3

Thanks ! Well i got the CollisionShapes' position and rotation offsets right , but still struggling with it.It seems that the Constraint params are wrong. Either the bones are rotated in the wrong direction or the upper lower limits are wrong i don't know.... The next thing we need in Urho Editor is a Ragdoll editor... because tweaking like this is a nightmare...

Something like this :

[video]https://www.youtube.com/watch?v=dCwNaE_eVsM[/video]


EDIT :
I checked my models against Jack and it seems that i export my models facing backwards (180 degs offset on y axis) . Have anyone any idea how to modify the ragdoll creation code to generate everything (Constraints , RigidBodies) to face in the oposite direction ?

-------------------------

cadaver | 2017-01-02 01:11:27 UTC | #4

I think the problem is that there is no convention for the coordinate axes of a character's skeleton (such as the simple "positive Z is forward" we'd usually use for scene nodes) and setting up a ragdoll properly requires taking these into account. The ragdoll sample is basically only valid for the Jack model and you shouldn't read too much into it. However if you can pinpoint that there's an actual bug in Urho's constraints that would prevent e.g. certain axes or limits to be used, then by all means submit an issue to github.

-------------------------

Dave82 | 2017-01-02 01:11:27 UTC | #5

Yess i got it ! Works perfectly now. I had to "visualize" the rotation of the parent and child bodies , and now i understand what they exacly do... 
works perfectly !

-------------------------

cadaver | 2017-01-02 01:11:28 UTC | #6

Good to hear!

-------------------------

