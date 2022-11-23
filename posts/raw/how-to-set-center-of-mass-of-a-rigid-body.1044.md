abhishek.sinha | 2017-01-02 01:05:02 UTC | #1

I have a rigidbody which is pointed at the end, however it does not fall down flat as it is supposed to. I figured this is due to center of mass not being in middle but is towards the pointed end. Is there any way I can change the center of mass. I see there are APIs to get the center of mass but nothing to change it

-------------------------

cadaver | 2017-01-02 01:05:02 UTC | #2

Presently that is not possible, as the center of mass is always calculated by Bullet from the collision shapes attached to the body (assuming uniform density.) However it should be possible to add.

-------------------------

abhishek.sinha | 2017-01-02 01:05:02 UTC | #3

Thanks for your reply. Looking at the code seems like by default initially urho makes the center of mass of rigidbody to be the origin of the model/body defined. Setting the anchor point of the model to the exact location where I wanted the center of mass to be seemed to work for me.

-------------------------

