JTippetts | 2017-01-02 01:12:06 UTC | #1

For awhile, I've noticed that when I enable shadows on my scene's directional lights, I get banding and moire patterns on many surfaces:

[img]http://i.imgur.com/YgYURBI.png[/img]
[img]http://i.imgur.com/4NfO2YC.png[/img]
[img]http://i.imgur.com/20ffItg.png[/img]

It occurs even on flat, non-normal-mapped surfaces (such as the Siegebreaker's hammer in the third pic).

The banding goes away if I disable shadows, so I'm sure that there is some tweaking I can do. Sadly, I don't really understand the shadow process, so I'm not sure exactly which parameters to tweak or what values to shoot for. Changing things at random doesn't really seem to get me anywhere, and the documentation isn't really very descriptive about exactly what changes I can expect from tweaking which parameters. I'm guessing I need to modify Bias and/or Focus parameters. Can anyone point me in the right direction?

-------------------------

rasteron | 2017-01-02 01:12:06 UTC | #2

I had this problem before. It's the camera far distance and bias so try playing around with those values. I'd focus more on bias if you could not change your far distance due to some game visual reasons. If you're also working on an isometric camera then decreasing the far distance a bit would not be a problem.

-------------------------

Enhex | 2017-01-02 01:12:09 UTC | #3

Implementing Shadow Map Normal Offset Bias could virtually solve it.
[topic1991.html](http://discourse.urho3d.io/t/shadow-map-normal-offset-bias/1904/1)

-------------------------

Bananaft | 2017-01-02 01:12:09 UTC | #4

It's called shadow acne. And apart from bias settings there is also a very effective way to fight it: In all your materials set shadow cull mode to CW(opposite to view cull mode). Then you can set bias to 0, or even negative value to prevent light leaks.

-------------------------

