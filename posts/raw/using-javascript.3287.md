akilarandil | 2017-06-27 12:01:47 UTC | #1

Hi all,

We are about to try a Javascript based Game engine. Is there any possibility of Urho supporting Javascript ? I also saw Atomic Engine which is a fork of Urho. Can we reuse the code we have written? Or something else?

-------------------------

HeadClot | 2017-06-27 12:18:07 UTC | #2

Look into Atomic Game Engine -> https://atomicgameengine.com/

It is based on a fork of Urho3D. :slight_smile:

Hope this helps.

-------------------------

akilarandil | 2017-06-27 12:54:15 UTC | #3

Can we use the code base written in c# in that?

-------------------------

HeadClot | 2017-06-27 13:08:44 UTC | #4

Atomic supports C# so I would say yes. But I am unsure.

-------------------------

Alex-Doc | 2017-06-27 13:20:49 UTC | #5

If I remember correctly, Atomic uses [url=http://duktape.org]Duktape.[/url]
You could also try rolling up your Duktape Urho3D integration, if you are willing to.

-------------------------

