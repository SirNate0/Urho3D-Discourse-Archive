smellymumbler | 2017-04-17 23:10:56 UTC | #1

How easy it is to replace the existing XML parser with any other format? I mean, i intend to use something like https://github.com/mayah/tinytoml or https://github.com/jbeder/yaml-cpp, but i want to know if there's a common file-loading interface or any documentation on that.

-------------------------

Sinoid | 2017-04-18 01:35:34 UTC | #2

There's nothing that's top-level shared. Binary, XML, and JSON are each their own separate paths.

It's just a matter of the volume of work. As long as you support Variant, then the Node, UI, and Component derived types are little effort. However, there's a fair bit going on with techniques, texture XML config, materials, particle effects, etc that will require much more work. Probably quite a bit in Urho2D as well.

It adds up to an awful lot of possible paths to test and confirm.

-------------------------

smellymumbler | 2017-04-18 14:40:58 UTC | #3

https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/Scene.cpp#L190

Hmm, so each class is responsible for defining how it is created via any serialized format. Would you guys accept some sort of PR that changes this? I mean, IMHO, having a `Parser` interface that `JSON` and `XML` can implement, with factory methods responsible for creating the objects, would allow developers to choose any format or easily develop their own (or even switch the parser, like from Pugi to RapidXML).

-------------------------

