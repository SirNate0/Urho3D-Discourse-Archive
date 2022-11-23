sergeyv | 2019-09-23 05:35:36 UTC | #1

Simple question  -  to implement usual ZoomFit function need to get bounding box for entire scene.  
Is it correct that the only method to do this is 
- quary octree::GetDrawables()  with maximum bbox 
- parse through all node and calculate result bbox 

Thanks !

-------------------------

Modanung | 2019-09-27 12:54:49 UTC | #2

I think you may be looking for `Octree::GetWorldBoundingBox()`.

-------------------------

