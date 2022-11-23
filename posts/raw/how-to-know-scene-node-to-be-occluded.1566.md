Stefans | 2017-01-02 01:08:33 UTC | #1

Hi, developers?

How to know scene node 's staticmodel component  to be occluded? Is there an event to send and be catched? 

Thanks

-------------------------

codingmonkey | 2017-01-02 01:08:34 UTC | #2

hi, i guessing that no such functionality to get result of software occlusion culling.
but earlier I create some crappy functionality in my fork to get query samples from batch when it doing rendering geometry. and it works fine except one thing i have to make "if" barricades and some kind query flag to getting samples not often, otherwise i gotten dramatically low fps.
I think need add special pre pass into engine mechanics to do query samples of objects into low-res depth buffer for HW occlusion queries, and all will be happy)

ps. term "occluded" is for drawables and not for nodes ) nodes may have within, few drawables each of them may be occluded by SW occluder or no

-------------------------

cadaver | 2017-01-02 01:08:34 UTC | #3

Check the Drawable IsInView() functions. Note that it could also return false because you're facing away from it (AABB culling check failed instead of occlusion)

-------------------------

Stefans | 2017-01-02 01:08:34 UTC | #4

thanks.

-------------------------

