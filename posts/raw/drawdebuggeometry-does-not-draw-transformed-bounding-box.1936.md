George | 2017-01-02 01:11:40 UTC | #1

I found that DrawDebugGeometry draw a non orientate bounding box.
Also when the node rotate, the bounding box changes it's min max scale. Is this a feature? Do we have option to debug draw the transformed bounding box?

-------------------------

rku | 2017-01-02 01:11:40 UTC | #2

This is axis-aligned bounding box. Calculations with such BB are faster so yeah you can call it a feature.

-------------------------

