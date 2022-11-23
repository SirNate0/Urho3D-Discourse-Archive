haolly | 2017-12-18 14:38:36 UTC | #1

It was asked in gitter.im [here]( https://gitter.im/urho3d/Urho3D?at=5a351271232e79134d58663c) first, as @rku  suggest me to debug and step into it, so I tried, and found the line https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/ResourceCache.cpp#L584 will always  evaluated to true, maybe it could be write in the form as to the line https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/ResourceCache.cpp#L648
![2017-12-18_213400|690x308](upload://ApMPDHYYHsA3AXVe9XsPWjCHz0y.png)

The picture says `FindResource` returns `noResource`, and the debugger goes though to 587 line

-------------------------

Eugene | 2017-12-19 15:12:18 UTC | #3

I re-read you post twice or thrise and I don't understand where is the bug and how to reproduce it.

-------------------------

haolly | 2017-12-19 15:45:42 UTC | #4

@Eugene Sorry for my foolish :pensive:

Actually , there was no problem.

The one thing I do not know is how `SharedPtr` is converted to boolean value, there was no bool operator in this class

-------------------------

Eugene | 2017-12-19 15:57:31 UTC | #5

[quote="haolly, post:4, topic:3864"]
The one thing I do not know is how SharedPtr is converted to boolean value, there was no bool operator in this class
[/quote]

There is `operator T*`

-------------------------

haolly | 2017-12-19 16:25:17 UTC | #6

@Eugene 
Thanks for you replay.
I learned a new thing : type conversion operator :grinning:

-------------------------

