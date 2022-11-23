codingmonkey | 2017-01-02 01:15:12 UTC | #1

Hi there! 
after read this article [hownot2code.com/2016/08/25/long ... /#more-977](https://hownot2code.com/2016/08/25/long-awaited-check-of-cryengine-v/#more-977)
I just curious about same typos and issues in Urho3d project.
and I find few issue or mb typos

for example this:
>autoLoadPaths[0]
mb this need to fix to autoLoadPaths[i]? because it in for-loop
[url=http://savepic.ru/12231960.htm][img]http://savepic.ru/12231960m.png[/img][/url]

also you may download this plugin([viva64.com/us/pvs-studio/](http://www.viva64.com/us/pvs-studio/)) and may see another typos and some troubles in code

add:
matrix2.h have float m02_ but no used anywhere anymore

-------------------------

cadaver | 2017-01-02 01:15:19 UTC | #2

In the autoloadpath example the intention is to compare the first element.

But thanks for the matrix2 unused variable spotting.

-------------------------

