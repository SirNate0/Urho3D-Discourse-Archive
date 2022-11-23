TikariSakari | 2017-01-02 01:04:37 UTC | #1

I was wondering if it would be possible to somehow use the navigation system in urho to draw a mesh from certain point.

For example lets say that character is at point A[5,5], and it could move in range of 5 units. Now if there are no obstacles this would just become a normal circle. With obstacles the mesh would become something totally different.

If there are no way to get the area for now, I have thought few possible solutions. One would be using some sort of 2d texture, where I would paint the area. This might become quite heavy on calculationwise and maybe pixelated. The idea would be first "drawing" the obstacles into the map, since I am mostly thinking that all my obstacles would be round, then using some sort of flood fill algorithm that keeps distance counted. I could get around corners this way too I think. Altho it might be bit hard to keep correct distance, since flood algorithm would show that point [3,3] would be 6 units away from [0,0]. I suppose it might need quite some calculations. To create the movement area texture, so this might be a bit slow as well.

The other way I thought about going this problem would just be checking points in radius of A. If the path hits walls, then checking the remaining paths from the corner point of obstacle or something along the line of that.

-------------------------

TikariSakari | 2017-01-02 01:04:38 UTC | #2

Thank you, I think this will help me to get started with the problem. Hopefully I will be able to manage to figure this out.

-------------------------

