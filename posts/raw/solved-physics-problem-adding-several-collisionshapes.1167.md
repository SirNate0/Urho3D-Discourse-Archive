esak | 2017-01-02 01:05:50 UTC | #1

I have a problem with Bullet physics. My scenario is the following:
When node B (containing a rigidbody + box shape) hits node A (with exact the same setup) I remove the rigidbody + shape from node B and set it's parent to node A.
Then I create another box shape to node A with the position and rotation from node B.
The issue I face is that the first time it seems to work, but on the second, third, fourth or the fifth time the previously added collisionshapes are gone (just the first and the last shape are left).
Also, on some occasions my program freezes completely for some seconds.
Any idea what's going on here? Or some suggestion of what I should try?

-------------------------

esak | 2017-01-02 01:05:56 UTC | #2

I solved this issue, it was a problem with my code.  :frowning:

-------------------------

