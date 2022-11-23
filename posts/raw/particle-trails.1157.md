1vanK | 2017-01-02 01:05:46 UTC | #1

[img]http://s010.radikal.ru/i311/1507/cb/d872f5a1f404.jpg[/img]

Engine patch + Example
https://         drive.google.com/open?id=0B_XuF2wRVpw4d2dQbzZZcm43NXM

P.S. This implementation generates a lot of particles and performance is not perfect

-------------------------

1vanK | 2017-01-02 01:05:46 UTC | #2

Small optimization: shange <sorted enable="true" /> to <sorted enable="false" /> in Particle/Trail.xml and Particle/Trail2.xml
If the trail is dotted, increase <numparticles value = "10000" />

-------------------------

Bananaft | 2017-01-02 01:05:46 UTC | #3

For that sort of things (thin streaks), you probably better use triangle strips, like Unreal's ribbons or Unity's trail renderer.

This implementation is more suitable to make thick smoke or fire trails, as it will take much less particles. 
like this one:
[upload.wikimedia.org/wikipedia/ ... losion.jpg](https://upload.wikimedia.org/wikipedia/commons/2/28/Pi-explosion.jpg)

-------------------------

1vanK | 2017-01-02 01:05:46 UTC | #4

I'm new to this engine, and integration triangle strips to the particle system is difficult for me :) As far as I understand, particle rendering in Urho based on Billboards and need change a lot of code,  which I have not yet know.

-------------------------

friesencr | 2017-01-02 01:05:46 UTC | #5

Coding monkey made a tail generator that you can look at.

[github.com/MonkeyFirst/urho3d-c ... -generator](https://github.com/MonkeyFirst/urho3d-component-tail-generator)

-------------------------

rifai | 2017-01-02 01:07:02 UTC | #6

[quote="1vanK"]

Engine patch + Example
https://         drive.google.com/open?id=0B_XuF2wRVpw4d2dQbzZZcm43NXM

P.S. This implementation generates a lot of particles and performance is not perfect[/quote]

Look nice. Unfortunately, link is broken. Can you fix it? I want to give it a try.  :smiley:

-------------------------

1vanK | 2017-01-02 01:07:02 UTC | #7

[quote="rifai"]
Look nice. Unfortunately, link is broken. Can you fix it? I want to give it a try.  :D[/quote]

I deleted it . Too low performance :)
 [drive.google.com/open?id=0B_XuF ... ldOSnhDSkE](https://drive.google.com/open?id=0B_XuF2wRVpw4RUZjZldOSnhDSkE)

-------------------------

