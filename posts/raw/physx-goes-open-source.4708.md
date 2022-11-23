SirNate0 | 2018-12-03 14:34:59 UTC | #1

It seems Nvidia is releasing PhysX under a BSD-3 license
[https://blogs.nvidia.com/blog/2018/12/03/physx-high-fidelity-open-source/](https://blogs.nvidia.com/blog/2018/12/03/physx-high-fidelity-open-source/)

-------------------------

rku | 2018-12-03 14:57:47 UTC | #2

PhysX integration in Urho3D when

-------------------------

Sinoid | 2018-12-03 20:05:16 UTC | #3

All of that sweet sweet APEX stuff is in there too!

Edit: assuming they follow what they already did with BSD'ing 3.4 last year.

-------------------------

S.L.C | 2018-12-03 20:50:31 UTC | #4

I suppose it depends on how well it works on other compilers and not just VS on windows. Because that'd be a bit disappointing. But as an alternative. Sure, that could be something to look forward to.

-------------------------

Sinoid | 2018-12-04 01:40:57 UTC | #5

> I suppose it depends on how well it works on other compilers and not just VS on windows. Because that’d be a bit disappointing.

3.4 already compiles everywhere that *matters*, even those that factually do not make fiscal sense to be targeting, I can't see them changing that. Android and VS were really trivial to build (again, 3.4 obviously).

Definitely not the easiest build to integrate into an existing CMake/Premake project though. I've been using PhysX 3.4 over the past two weeks in pre-production on a metaprogramming/code-generation series. Definitely easiest to treat as a *precompilation required system dependency* like any sane person does when embedding Mono.

-------------------------

rku | 2018-12-04 14:30:22 UTC | #6

There is ~~https://github.com/diharaw/PhysX-3.4-CMake~~ https://github.com/rokups/PhysX-3.4-CMake. Build scripts are rather awful, but im cleaning them up. Builds on linux already. Time to try on windows.

Edit: Though i would really be interested in broader discussion on PhysX vs Newton. Both seem great, both do simd acceleration.

-------------------------

smellymumbler | 2018-12-04 15:57:00 UTC | #7

I don't get the whole PhysX thing. Bullet seems much more efficient and stable. And it was born open.

-------------------------

S.L.C | 2018-12-04 17:04:00 UTC | #8

Bullet has some issues. Some of them have been pointed out by @Enhex and various other people in the Newton integration [topic](https://discourse.urho3d.io/t/newton-dynamics-integration/1596/3).

Including those issues. The code base in Bullet is ugly as f.. and hasn't been refactored or even touched in years. Most of their focus is now on robotics, machine learning and mainly python bindings. Most of the commits are about python bindings or related in some way. The only changes I've seen to the foundation of the Bullet library have been minor compiler warnings, variable names and a few actual fixes that came mostly from the pull requests by people who encountered them.

Basically, the focus of the Bullet physics engine seems to have shifted away from gaming as a primary target.

Newton is the only one that has seen some growth in game related areas. Such as vehicles and recently animation. I've been keeping an eye on both of them for a while. And with a bit of work you could say that Newton would be a decent replacement to Bullet. While PhysX could be implemented as an alternative for more professional projects.

@rku Newton doesn't really have a ton of SIMD currently. Or maybe I haven't looked where I should. But I definitely see that preparations are taken to make room for SIMD in the future.

-------------------------

Enhex | 2018-12-04 17:59:32 UTC | #9

PhysX isn't deterministic, which makes it problematic to use with networking, something to keep in mind.

-------------------------

rku | 2018-12-04 18:04:57 UTC | #10

I too arrived at a conclusion that maybe newton is a better bet after all. Even people from nvidia agree that newton is very competitive and in some cases much better than physx.

-------------------------

Sinoid | 2018-12-05 03:34:28 UTC | #11

> The code base in Bullet is ugly as f… and hasn’t been refactored or even touched in years.

That's an understatement.

---

I wonder how well Newton copes with origin-shifting/page-teleporting? Bullet's behaviour is really odd there, you have to either `disable -> move -> enable` (thus removing/re-adding the body) or just pray that it won't flicker the transforms on you (with `Activate()` not called for the shift/teleport as that wakes **every** single body, which sucks).

Mysterious flickering transforms is my current bane with bullet.

Without the extra APEX doodads PhysX isn't very appealing IMO. The API is nice, but that's not golden enough for me to justify the work of replacing something that already is there and mostly *works*.

-------------------------

