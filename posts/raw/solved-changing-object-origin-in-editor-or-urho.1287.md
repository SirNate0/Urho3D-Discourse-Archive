George | 2017-01-02 01:06:36 UTC | #1

Hi is it possible to change the model object origin coordinate inside the editor?
It would be useful to define rotating coordinate frame or things like robotic arm etc.

Regards
George

-------------------------

rasteron | 2017-01-02 01:06:37 UTC | #2

Hey George,

You're object will be parented to a node, manipulate this instead and this will act as the origin.

Hope that helps.

-------------------------

cadaver | 2017-01-02 01:06:37 UTC | #3

If you actually want to change the origin of a model, then you'll have to re-import with the origin (pivot) set correctly in the modeller program. The child node method is good if you either don't want to do that or want to make dynamic changes to the origin at runtime.

-------------------------

George | 2017-01-02 01:06:38 UTC | #4

Thanks,
The reason I ask is to make sure that it hasn't been done before.

In some of the softwares that I used previously. They allows us to add several coordinate frames on one object. I find this feature particularly useful for multiple applications. E.g. snapping objects by coordinate frames, or creating a coordinate frame on an avatar hand and attaching different node to it.

Regards
George

-------------------------

