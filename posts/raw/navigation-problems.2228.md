1vanK | 2017-01-02 01:14:03 UTC | #1

How to avoid vibration, when actor can not find a way?

[youtu.be/Rt6O4H9KGJs](https://youtu.be/Rt6O4H9KGJs)

[video]https://www.youtube.com/watch?v=Rt6O4H9KGJs[/video]


EDIT:

Hmm.
[code]agent->SetNavigationQuality(NAVIGATIONQUALITY_LOW);[/code]

solved this problem.

-------------------------

1vanK | 2017-01-02 01:14:03 UTC | #2

It is possible to use some objects as obstacles without creating NavMesh on top it?

[url=http://savepic.ru/11213637.htm][img]http://savepic.ru/11213637m.png[/img][/url]

Dynamic obstacles does not suit me, because they have cylindrical shape

-------------------------

1vanK | 2017-01-02 01:14:04 UTC | #3

Increasing "Region Min Size" helps in some cases,

[url=http://savepic.ru/11207514.htm][img]http://savepic.ru/11207514m.png[/img][/url]

but NavMesh still exists on walls

-------------------------

1vanK | 2017-01-02 01:15:04 UTC | #4

NavArea with ID = 0 allow cut unnecessary parts of NavMesh

[url=http://savepic.ru/12060397.htm][img]http://savepic.ru/12060397m.png[/img][/url]

-------------------------

