Bluemoon | 2017-01-02 01:00:13 UTC | #1

What seems to be the difference between creating a scene node as REPLICATED or creating it as LOCAL. When and where should these node creation modes be used

-------------------------

setzer22 | 2017-01-02 01:00:13 UTC | #2

Seems to be a networking-related thing. Replicated ones are sent over the network.

Apparently for a single player game you should go with local nodes (in case replicated ones carry some kind of overhead). In an online game it's trickier.

Check this out: [topic221.html](http://discourse.urho3d.io/t/replicated-vs-local-node/235/1)

PD: Thanks! I didn't know that either so I guess we both have learnt something.

-------------------------

Bluemoon | 2017-01-02 01:00:13 UTC | #3

:frowning:  My Bad, of all the times I use this forums search engine I just forgot to do so this time around making me duplicate an already solved request  :blush: 

Thanks so much for the link

-------------------------

