tybandara | 2017-03-02 05:31:14 UTC | #1

Hello experts,

I've imported a biped model from 3ds max and through Urho3d I'm able to rotate the model parts (i.e. arms, legs..) with rotation quaternions.
But it seems, different parts of my model are in different local coordinate systems. For example, the local coordinate system of arm is different to the local coordinate system of legs.

Is there a way to correct this from code itself (i.e. to bring all local coordinate systems alike to one)?
or 
should I try to fix it from 3ds max?

Thanks in advance

-------------------------

slapin | 2017-03-02 07:52:55 UTC | #2

I struggled with this too, and found that I have to convert coodinate system through hierarchy,
from current bone to skeleton. There are shortcuts, but they depend on what you want to do.
You just multiply by intverted transformation. To get fuly global space you need also to multiply by inverse skeleton transform.

-------------------------

tybandara | 2017-03-02 07:59:40 UTC | #3

[quote="slapin, post:2, topic:2838"]
keleton tra
[/quote]

Thanks for the quick answer. Sorry for being low experienced. Are you referring to change the current quaternion rotations by the inverse of a global transformation system. I'm sorry if this is something simple. But I'm finding it difficult to understand. Could you please elaborate a little bit more. It would be very helpful. 

Thank you.

-------------------------

slapin | 2017-03-02 08:16:13 UTC | #4

yes, you subsequently transform your current bone transform by parent inverse transforms

if you gave structure - hand - lowerarm - upperarm,
you get current transform of nand, multiply it by inverse transform of lowerarm, then multiply by inverse transform of
upperarm. if you want to get global space (not skeleton-relative) you then multiply by skeleton inverse transform.
Read docs on Skeleton class, and Bone class for reference. Sometimes you can cheat using global transform of bone nodes, but not very often, but if this shortcut is avaiable to you use it (less computations).

-------------------------

Dave82 | 2017-03-02 10:11:43 UTC | #5

Hi ! I dont know how much it helps but i wrote a biped animation exporter for Urho , so maybe you can look at the code and find something useful

http://discourse.urho3d.io/t/3ds-max-biped-animation-export-script/1071

-------------------------

