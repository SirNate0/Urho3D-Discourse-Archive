rogerdv | 2017-01-02 01:01:15 UTC | #1

After a quick look at docs, I couldnt find a way to get a node from the scene by its name, is that possible?

-------------------------

friesencr | 2017-01-02 01:01:15 UTC | #2

Scene or Node have a method called GetNode(String name, bool recursive)

-------------------------

Mike | 2017-01-02 01:01:15 UTC | #3

Take also a look at GetChild() function (it is used  in various samples).

-------------------------

rogerdv | 2017-01-02 01:01:16 UTC | #4

According to docs, scene doesnt has such GetNode implementation, only one that uses node id. But node does has GetChild in all flavours.

-------------------------

weitjong | 2017-01-02 01:01:16 UTC | #5

Scene inherits all the GetChild() methods from Node class.

-------------------------

