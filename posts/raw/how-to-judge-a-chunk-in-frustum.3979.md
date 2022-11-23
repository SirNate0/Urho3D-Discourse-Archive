ChunFengTsin | 2018-02-02 08:07:28 UTC | #1

hello , 
The game like minecraft, every frame should check many chunks.

I want to create and check chunks only in my view, in frustum.
how I get the matrix or infomatin about frustum to judge , when I use Urho3D.
thanks.

-------------------------

Eugene | 2018-02-02 09:04:45 UTC | #2

Don't really understand your question.

Would it be enough to iterate through chunks and test wheter they are in the Frustum? Maybe add some grouping for speed, like Octree does.

-------------------------

ChunFengTsin | 2018-02-02 10:13:39 UTC | #3

I am so sorry for my bad english.
There is a abstract picture I draw:
![temp|666x500](upload://clMxTDm0z5he6AqNkgGnQtEPiHT.png)

describe : red line box is chunk,  
And the chunks in blue area ,should be create and check . 


the game dynamic generation chunks around camera.
those chunks on back of camera should not be create.
how I judge that.

sorry for my bad english again.

-------------------------

Eugene | 2018-02-02 11:11:47 UTC | #4

Then... Frustum gives you an ability to check arbitrary box volume.
So you should just iterate through chunks and create the chunks inside/intersecting the Frustum.

-------------------------

ChunFengTsin | 2018-02-02 11:25:22 UTC | #5

oh,  it may be I'm too persistent in performance .
thanks a lot.

-------------------------

Eugene | 2018-02-03 01:56:50 UTC | #6

Well, performance issues could be solved later by grouping chunks hierarchically, smth like 3D-quadtree.

-------------------------

ChunFengTsin | 2018-02-02 11:29:55 UTC | #7

This is a good idea.

-------------------------

weitjong | 2018-02-03 01:56:50 UTC | #8

Also check Drawable::IsInView() to see if it meets what you need.

-------------------------

