JoshuaBehrens | 2017-01-02 00:58:42 UTC | #1

I tried to use the sensors with the 2D physics, but they are not implemented (due to undefined reference: Urho3D::CollisionShape2D::SetSensor(bool) and I didn't find it in the source). Maybe it is not implemented yet due to the "premature" 1.31 release. I just wanted to mention this.

Yours, Josh

-------------------------

Azalrion | 2017-01-02 00:58:42 UTC | #2

It was refactored recently to SetTrigger and IsTrigger to match the 3d version.

-------------------------

JoshuaBehrens | 2017-01-02 00:58:42 UTC | #3

Thanks for your reply. I thought the "trigger" had a different meaning. But I still think due to the early 1.31-version there are some "errors" still in the implementation of Box2D. When it is fully integrated maybe you should add a page in the documentation for those who try to "convert" a Box2D tutorial on Urho2D.

-------------------------

aster2013 | 2017-01-02 00:58:43 UTC | #4

[quote="JoshuaBehrens"]But I still think due to the early 1.31-version there are some "errors" still in the implementation of Box2D. [/quote]
If you find error(bug) you can report issue on GitHub. Thanks.

-------------------------

JoshuaBehrens | 2017-01-02 00:58:43 UTC | #5

Ok, I going to do that.

-------------------------

