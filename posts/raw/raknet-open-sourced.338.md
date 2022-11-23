boberfly | 2017-01-02 00:59:43 UTC | #1

Hi all, thought I'd just show this here:
[github.com/OculusVR/RakNet](https://github.com/OculusVR/RakNet)

I'm not sure how this middleware compares with kNet though if it's worth switching over to it for Urho3D, but go Oculus for buying and opening it up!

-------------------------

rasteron | 2017-01-02 00:59:43 UTC | #2

Wow was not expecting this Alex, but definitely good news!!  and it's BSD yeah! :smiley:

-------------------------

Mike | 2017-01-02 00:59:44 UTC | #3

RakNet is used by unity and havok. Features are detailed at [url]http://www.jenkinssoftware.com/features.html[/url].

-------------------------

rasteron | 2017-01-02 00:59:44 UTC | #4

Yes, I'm quite familiar with Raknet and have used it before with one of my personal projects.

In my opinion, I would say it's better than kNet and now it will be more active with the FOSS move by Oculus.

-------------------------

cadaver | 2017-01-02 00:59:45 UTC | #5

Nice news. This is definitely worth keeping an eye on in the very least.

kNet was initially developed for the realXtend Tundra virtual world platform and it's not seeing as active development anymore. Furthermore, it's missing some functionality like a robust send rate control, for which a hackish implementation was made in Urho. And of course NAT punchthrough, which was not a priority in kNet development. 

Using RakNet would give HTTP connection support at the same time, so the Civetweb library could even be dropped if integrating RakNet. I would guess a "full" RakNet integration including use of the ReplicaManager would be a huge work and not necessarily good (as it would leak all over Urho), but using it as a kNet replacement for reliable UDP networking would be much easier.

What needs testing is how cleanly RakNet compiles on all supported platforms. Also, with kNet we can support a nice "reliable but latest data" send mechanism for high-bandwidth updates like position, rotation and velocity, which means we don't have to deal separately with continuous and one-shot updates in respect to reliability and ordering. Have to see which RakNet concept (if any) corresponds to this.

-------------------------

friesencr | 2017-01-02 00:59:46 UTC | #6

The portable hashing algorithms were kind of a nice add.  Dumping civetweb for a more popular solution would be nice too.  I did a quick peek at the network code of godot.  It looks like they implimented an http stack from scratch.  Don't know if it works though.  civets formerly mongoose was used for quite a while in the real world.

-------------------------

