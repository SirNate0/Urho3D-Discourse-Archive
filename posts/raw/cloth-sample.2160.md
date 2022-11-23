NiteLordz | 2017-01-02 01:13:33 UTC | #1

I was searching thru the forum, but couldn't find any mention of anyone working on a Cloth sample.  I am wondering, cause i wanted to enable my models hair to move, and was going to simulate using a cloth simulation, unless someone has a better idea.

Thanks much

-------------------------

codingmonkey | 2017-02-20 14:29:40 UTC | #2

Hi!
I want to note about hair
if urho3d use bullet there is must be to able to create similar stuff like in blender - with bones and constraints.
Actually I'm not dig deep into urho3d's physics, but i see only 2d constraints examples 

https://youtu.be/6Uo0WMvKGxU?t=8m32s

-------------------------

cadaver | 2017-01-02 01:13:36 UTC | #3

VehicleDemo sample has Bullet constraints (wheels attached to car body). However I'm not sure if it's a good idea performance-wise for hair, which contains a lot of small objects. Probably running a specialized lightweight simulation is more appropriate.

-------------------------

Mike | 2017-01-02 01:13:36 UTC | #4

Ragdoll demo also makes heavy use of constraints.
Alternatively you could experiment with jiggle bones, or with shaders.

-------------------------

jmiller | 2017-01-02 01:13:37 UTC | #5

Found some C++ source on Urho3D JiggleBone; might be of some use.
[pastebin.com/hV1gJw8m](http://pastebin.com/hV1gJw8m)

-------------------------

codingmonkey | 2017-02-20 14:35:58 UTC | #6

I just  guess what we may use similar stuff from bullet
[quote="cadaver, post:3, topic:2160"]
However I'm not sure if it's a good idea performance-wise for hair, which contains a lot of small objects.
[/quote]
Yes it meybe cause reduce of the perfomance with bullet, but CE use bones with somekind of constraints.
see this:

https://www.youtube.com/watch?v=3HZygJB9Kfo

-------------------------

