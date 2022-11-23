umen | 2017-01-02 00:59:16 UTC | #1

Hey , maybe its more bullet kind of question but i want to try to ask it here . 
i have simple road modeled in blender , its not Terrain i think , please take alook at the picture .
what is the right way to attach it Collision Shape? 
its road that car supposed to be on it ( like the Vehicle example ) .
[img]http://i.imgur.com/AVlvyXV.png[/img]

Thanks!

-------------------------

cadaver | 2017-01-02 00:59:18 UTC | #2

The most straightforward way to match the graphical shape is to choose TriangleMesh shape type in the CollisionShape, and select the same model file as in the graphical (StaticModel) component. Note that you could choose also a different model that for example has less polygons than the visual model.

-------------------------

