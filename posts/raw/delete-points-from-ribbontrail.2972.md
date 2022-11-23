sabotage3d | 2017-03-30 20:53:34 UTC | #1

I am trying to delete points from RibbonTrail, but I am getting artefacts. In my test I am drawing a circle and removing some points, but I am getting a line inside the gap. The yellow is the trail the red is the area where I am deleting. My approach is inside the UpdateTrail method, if I press a button to delete a range of points. What would be the correct way of approaching this?

`points_.Erase(points_.Begin()+10, points_.End()-5);`

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/7a08f3f47c9d20b4f6e69752b849e7e778621182.png'>

-------------------------

