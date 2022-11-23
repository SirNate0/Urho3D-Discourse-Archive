sabotage3d | 2017-01-02 01:09:16 UTC | #1

I was looking at UrhoSharp documentation and I found that it supports action system with numerous basic actions like fade in and fade out. Is it a good idea to backport it to Urho3d? Do you think this would be useful addition?
[b]UrhoSharp Actions[/b]
[url]http://developer.xamarin.com/guides/cross-platform/urho/using/#Actions[/url]
[url]http://developer.xamarin.com/guides/cross-platform/urho/using/#Basic_Actions[/url]

-------------------------

codingmonkey | 2017-01-02 01:09:16 UTC | #2

>Do you think this would be useful addition?
I think yes, it maybe useful)

-------------------------

yushli | 2017-01-02 01:09:16 UTC | #3

Definitely Yes. That will be a great addition.

-------------------------

greenhouse | 2017-01-02 01:09:17 UTC | #4

+1  :slight_smile:

-------------------------

1vanK | 2017-01-02 01:09:17 UTC | #5

Who will do it? )

-------------------------

greenhouse | 2017-01-02 01:09:18 UTC | #6

I guess the one who proposed it, no?  :wink:

-------------------------

glebedev | 2021-02-21 23:39:17 UTC | #7

https://github.com/mobius3/tweeny
https://mobius3.github.io/tweeny/

https://github.com/sasq64/tween
etc...

-------------------------

WangKai | 2021-02-22 03:10:19 UTC | #8

Combine/redesign/integrate (Easing/Action + Attribute Animation) will be really powerful.

https://github.com/xamarin/urho/tree/master/Bindings/Portable/Actions
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Scene/ValueAnimationInfo.h

-------------------------

glebedev | 2022-05-22 23:20:08 UTC | #9

I know it is a bit late... But I've started to port the UrhoSharp's action back to c++ codebase:

https://github.com/gleblebedev/rbfx/pull/5

-------------------------

glebedev | 2022-05-23 11:21:49 UTC | #10

Also some yearly prototype results:
https://youtu.be/q1oET_arnpU

-------------------------

