setzer22 | 2017-01-02 01:02:48 UTC | #1

This is not a question, I just thought I might avoid some trouble to people encountering this issue. Some people might find this issue when compiling with the latest git version. I had it when including the file LogicComponent.h: Basically lots of compile errors regarding URHO3D_API not being defined. To fix it you should include Urho3D.h in all the files that need it because it's not included by those headers anymore.

This is last commit's message:

[code]
Avoid the include dirs hack for finding the Urho3D.h header.
It is now a library user own's responsibility to include the Urho3D.h in their source code. Or to include it as part of their own precompiled header similar to what Urho3D project has done.
[/code]

Also, even if this is solved I'd like some explanation on why can't Urho3D.h be included in Urho's headers and why that was a hack. Anyone knows?

-------------------------

codingmonkey | 2017-01-02 01:02:48 UTC | #2

i'm fix only RefCounted.h 

[code]
#pragma once

#define URHO3D_API

namespace Urho3D 
{
...
[/code]

and it's all works again )

-------------------------

weitjong | 2017-01-02 01:02:48 UTC | #3

[quote="codingmonkey"]i'm fix only RefCounted.h 

[code]
#pragma once

#define URHO3D_API

namespace Urho3D 
{
...
[/code]

and it's all works again )[/quote]
This is not advisable, especially when you are using SHARED lib type on Windows platform.

-------------------------

codingmonkey | 2017-01-02 01:02:51 UTC | #4

>This is not advisable, especially when you are using SHARED lib type on Windows platform.

look i got compile error even i made new project from scratch with last master-build
[video]http://www.youtube.com/watch?v=vARBHKNAr_g[/video]

that i must to do in that case?) i'm goin in RefCouted.h and add #define ) 

and i guess that need to be fix header including method in example
from " " to <  >
[urho3d.github.io/documentation/H ... _loop.html](http://urho3d.github.io/documentation/HEAD/_main_loop.html)

-------------------------

weitjong | 2017-01-02 01:02:52 UTC | #5

Yes. That's in the name of progress.  :wink:  Actually I am going to say, sorry for any inconvenience has caused. We have to occasionally break things in the master branch in order to move forward. If you need stability then use our release tag instead.

-------------------------

godan | 2017-01-02 01:04:06 UTC | #6

Just ran in to this as well! Thanks for the video!

-------------------------

