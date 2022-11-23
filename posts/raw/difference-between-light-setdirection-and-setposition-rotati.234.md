umen | 2017-01-02 00:59:03 UTC | #1

what is the difference between when i set light rotation and direction ? 
is the light setDirection is the end target for which the the light is pointing at ? 
so i don't need to set the rotation ?

-------------------------

cadaver | 2017-01-02 00:59:03 UTC | #2

SetDirection() and SetRotation() are just different ways of achieving the same thing: setting the scene node's orientation in space. The light always shines in the direction of its scene node's local forward (positive Z) axis.

-------------------------

umen | 2017-01-02 00:59:04 UTC | #3

Thanks for your quick answer

-------------------------

