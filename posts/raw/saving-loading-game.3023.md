smellymumbler | 2017-04-18 14:32:42 UTC | #1

How would you guys approach a system for loading/saving a game? Just save the entire scene serialized?

-------------------------

Modanung | 2017-04-19 00:12:21 UTC | #2

[quote="smellymumbler, post:1, topic:3023"]
Just save the entire scene serialized?
[/quote]
If you have all the required information stored in component properties. Then maybe.
But in most cases you won't need that much information (but probably also more) since a base scene might already be present with its set save and load points.
You're probably best off figuring out what information is essential to store in your situation and then writing SaveGame and LoadGame methods that handle and complement that.

-------------------------

Sinoid | 2017-04-19 01:55:27 UTC | #3

Place the things that need to be saved under a "DynamicObjects" node in the scene which is treated like a "folder."

When saving just save that node and it's children out to XML/binary. 

When reloading just overwrite the existing DynamicObjects node.

-------------------------

