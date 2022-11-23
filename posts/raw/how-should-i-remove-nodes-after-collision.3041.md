RobertoOG | 2017-04-23 22:32:14 UTC | #1

I'd like my character to remove a pickup's node he collides with. 

Currently I listen to collision events in my character and the pickup but if I do Remove(node_) in the pickup sometimes the collision event is not listened by the character. 

I was thinking of having an extra boolean member in the pickup, which is made true in the collision listener, and then remove the node in next update cycle, but I'm wondering if there is a better way.

Thank you!

-------------------------

