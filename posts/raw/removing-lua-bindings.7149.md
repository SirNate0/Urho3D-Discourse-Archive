1vanK | 2022-01-24 00:24:45 UTC | #1

I am planning to replace Urho3D::Vector and Urho3D::PODVector with std::vector.  https://discourse.urho3d.io/t/yet-another-vector-benchmark/6962
Is there a person who wants to change the bindings to LUA? If such a person is not found, then the bindings will be removed.

-------------------------

SirNate0 | 2022-01-24 03:30:39 UTC | #2

I'll give a look at automating their generation like the Angel Script ones. But I don't use Lua myself, so if I think it will be too difficult and/or tedious I make no promises that I'll actually do it. So if someone else wants to claim the job feel free. Otherwise I'll probably report back in a week or so what my thoughts are.

-------------------------

1vanK | 2022-01-24 06:03:14 UTC | #3

Ok, my work will be done here <https://github.com/urho3d/Urho3D/pull/2868>

-------------------------

Eugene | 2022-01-24 08:06:35 UTC | #4

[quote="1vanK, post:1, topic:7149"]
I am planning to replace Urho3D::Vector and Urho3D::PODVector with std::vector
If such a person is not found, then the bindings will be removed.
[/quote]
To be honest, it's weird attitude for PR.
It should be "This PR will not be merged unless you help me" and not "I will hurt you unless you help me".

If there are no Lua users, it's fine to drop Lua tho. But I am not sure about that. I think at least @JTippetts1 used it recently?

PS: I obviously don't care about this topic personally, since I don't use Lua. Treat this post as off-hand comment, not a strong opinion.

[spoiler]`<sarcasm>`If I knew I could just replace Urho containers with (EA)STL in PR, nuking all the bindings unless someone fixes them, I would have already done it 2 years ago`</sarcasm>`[/spoiler]

-------------------------

1vanK | 2022-01-24 08:36:30 UTC | #5

There are two variants: do not develop the engine or drop out what no one is going to maint. Those who need LUA and do not need engine development can use the old version with LUA. Nothing will change for them.

-------------------------

1vanK | 2022-01-24 08:38:59 UTC | #6

[quote="Eugene, post:4, topic:7149"]
`` If I knew I could just replace Urho containers with (EA)STL in PR, nuking all the bindings unless someone fixes them, I would have already done it 2 years ago ``
[/quote]

Two years ago there were contributors here

-------------------------

Eugene | 2022-01-24 09:01:32 UTC | #7

[quote="1vanK, post:5, topic:7149"]
There are two variants: do not develop the engine or drop out what no one is going to maint.
[/quote]
Do you have a roadmap of functional changes?
Neither removing Lua nor using STL will help users make games on their own -- they are useful only as prerequisite for other (real) changes.

-------------------------

1vanK | 2022-01-24 09:09:32 UTC | #8

It looks like an attempt to hook me up. I have already explained the reason for change. If there are attempts to make changes, then any changes will be stopped by LUA bindings, which are not automatically generated and there is no person who deals with them. If there are no radical changes, then what's the difference? You can still use the old version of the engine with LUA bindings. 

p.s. Have you roadmap for rbfx?

-------------------------

Eugene | 2022-01-24 09:37:48 UTC | #9

[quote="1vanK, post:8, topic:7149"]
It looks like an attempt to hook me up.
[/quote]
Nah, I'm too old for this -_-

My philosophy is that the engine should help users make games, first and foremost.
So I look at all changes from this point of view: "how would it help someone to make a game?"
And I personally don't make non-functional changes unless I plan to use them for something functional later -- that's why I was curious if you have any plans for future functional updates.

[quote="1vanK, post:8, topic:7149"]
p.s. Have you roadmap for rbfx?
[/quote]
Surprisingly, yes! It's offtopic so I'll hide it.
[details="Nothing to see here"]
1. Move to EASTL
1. Prototype C++ Editor
1. Prototype C# bindings
1. *(I have joined rbfx here)*
1. Unified object serialization
1. Baked lighting
1. New renderer with PBR support and unified shaders
1. Unified animation system
1. Native import of glTF
1. *(`master` is here)*
1. New networking
1. New particles
1. *(`dev` branch is here)*
1. Animation refactoring
1. Compute shaders
1. *(things below I am not 100% sure about and they don't have an order)*
1. Render graph?
1. Basic scripting, maybe Luau with SOL?
1. VR?
1. Vulkan+Metal?
1. Editor refactoring?
1. PhysX integration?
[/details]

-------------------------

1vanK | 2022-01-24 09:55:15 UTC | #10

[quote="Eugene, post:9, topic:7149"]
So I look at all changes from this point of view: “how would it help someone to make a game?”
[/quote]

How does blocking engine changes help to create games?

-------------------------

adhoc99 | 2022-01-24 10:57:08 UTC | #11

Please don't break/remove LUA support.

Although I don't use LUA myself, I think there's people actively using it (I think @evolgames is using LUA, and he's making some really cool games [[1]](https://discourse.urho3d.io/t/random-projects-shots/2431/291) [[2]](https://discourse.urho3d.io/t/random-projects-shots/2431/299) [[3]](https://discourse.urho3d.io/t/random-projects-shots/2431/305) [[4]](https://discourse.urho3d.io/t/random-projects-shots/2431/311)).

Or at least add `std::vector` as a compiling option/flag so it won't break the current engine features for everybody.

-------------------------

1vanK | 2022-01-24 11:08:31 UTC | #12

Are you planning to maintain LUA bindings?

-------------------------

adhoc99 | 2022-01-24 11:23:28 UTC | #13

As I said, I don't use LUA. But I feel for those that use it and now, out of nowhere, could lose it. That's not cool.

Again, if the `std::vector` performance gain is suddenly so important now, just add it as an compiling option/flag so it won't break everything for everybody.

-------------------------

1vanK | 2022-01-24 11:29:48 UTC | #14

Have you read my posts above?

-------------------------

adhoc99 | 2022-01-24 11:30:17 UTC | #15

Yes, have you read mine?

-------------------------

1vanK | 2022-01-24 11:30:58 UTC | #16

Yes, you write nonsense.

-------------------------

1vanK | 2022-01-24 11:32:03 UTC | #17

[quote="adhoc99, post:13, topic:7149"]
`std::vector` performance gain is suddenly so important now, just add it as an compiling option/flag so it won’t break everything for everybody.
[/quote]

How do you imagine that?

-------------------------

adhoc99 | 2022-01-24 11:42:20 UTC | #18

ifdef it...

btw, what happened to [this](https://discourse.urho3d.io/t/scripting-language-binding/6710/2)?

-------------------------

1vanK | 2022-01-24 11:48:25 UTC | #19

[quote="adhoc99, post:18, topic:7149, full:true"]
ifdef it…
[/quote]

ifdef for each vector use? 

[quote="adhoc99, post:18, topic:7149, full:true"]
btw, what happened to [this](https://discourse.urho3d.io/t/scripting-language-binding/6710/2)?
[/quote]

I can teach you how to use git (not free) to keep track of changes

-------------------------

adhoc99 | 2022-01-24 12:04:11 UTC | #20

Won't you change them all anyway?

If it's already there, then what's the issue on supporting LUA?

-------------------------

1vanK | 2022-01-24 12:09:21 UTC | #21

[quote="adhoc99, post:20, topic:7149"]
Won’t you change them all anyway?
[/quote]

Do you have any idea about the scope of using containers in the engine? 

The source code will be 25% of #define.

[quote="adhoc99, post:20, topic:7149"]
If it’s already there, then what’s the issue on supporting LUA?
[/quote]

There ain't no problem, take it on

-------------------------

adhoc99 | 2022-01-24 12:12:18 UTC | #22

Then just change the ones that really need the supposed performance boost.

May as well update Urho3D's website warning people that every single feature is subject to being dropped out of nowhere just because, so they don't even bother to start using the engine.

-------------------------

1vanK | 2022-01-24 12:15:17 UTC | #23

I'll just end this useless dispute

-------------------------

SirNate0 | 2022-01-24 12:35:54 UTC | #24

[quote="adhoc99, post:18, topic:7149"]
ifdef it…
[/quote]

The issue with doing this is primarily that `Urho3D::Vector` and `std::vector` follow different naming conventions (`Size` vs `size`). If we fix that difference then an `ifdef STL_VECTOR` is fairly easy, basically just an optional `typedef` with a few extra chances for `Contains` and such. But that would probably already break the bindings (you can look at my branch in the linked topic with the benchmark, I don't recall actually getting the bindings working. Though if they are, maybe it's less of an issue than it seems).

I share the concerns expressed about breaking the code without concern, but I have several times found the incompatibility of Urho's containers with the STL limiting, and there should be some performance gain to the change.

-------------------------

Eugene | 2022-01-24 12:41:13 UTC | #25

[quote="SirNate0, post:24, topic:7149"]
and there should be some performance gain to the change.
[/quote]
As far as I remember STL was on average slightly slower than Urho Vector, due to being more generic. *Especially* in debug builds, *especially* on MSVC with default iterator debugging level = 2.

Having said that, never once I regretted ditching Urho Containers and moving on in the fork. I have spent several weeks refactoring Urho Vector back when I used it, and damn I hate it now.

-------------------------

1vanK | 2022-01-24 12:48:12 UTC | #26

Some compilers are faster. <https://github.com/1vanK/Urho3DContainersBenchmark/blob/master/vector_mingw32_release.txt>

But that's not the point at all.

-------------------------

SirNate0 | 2022-01-24 13:01:31 UTC | #27

What is the point then? Just so everyone is clear.

To be clear, I support the change, but as was evident above, I may not be correct on all of the reasons, so I'd like some clarification.

-------------------------

1vanK | 2022-01-24 13:50:47 UTC | #29

Initial reason: 

The reason is that we have two vectors instead of one generic vector optimized for any type. Firstly, this is inconvenient in itself and can lead to the use of the wrong container. Also, there are some errors popping up.

<https://github.com/urho3d/Urho3D/pull/2816>

The main reason has been described above.  LUA bindings require manual work and make it difficult to change the engine freely. In addition, we do not have people who want to maint these bindings. Even the author of the LUA bindings tried to rewrite them, but abandoned this idea. 

<https://github.com/urho3d/Urho3D/tree/new-lua-script-test>

In addition, the LUA language itself is experiencing a split. Official version is 5.4.3. LuaJIT use obsolete 5.1. And these versions are not very compatible.

-------------------------

SirNate0 | 2022-01-24 14:50:05 UTC | #31

Came across this binding library that seems very similar to pybind11, which I already started work on making bindings for. So my initial thoughts are that it will be doable.

https://github.com/gengyong/luaaa

-------------------------

vmost | 2022-01-24 21:03:05 UTC | #32

Just want to chime in to say 'yay pybind11 is amazing'. Anything that is 'similar' to pybind11 is also probably amazing.

-------------------------

S.L.C | 2022-01-26 01:15:00 UTC | #33

Honestly tho. If you think the Urho Vector is the performance issue in this engine then I probably have nothing else to say that make you realize otherwise.

If anyone wants STL container-like types they might as well just switch to rbfx fork and get the whole package instead of a half-assed attempt at trying to prove something that just isn't worth it.

Are we really that keen on destroying whatever is left on this engine? Turn it into an experimentation project where everyone just tried stuff that they think is needed?

I was skeptical when the rbfx fork was made. But seeing the recent evolution of vanilla Urho I have to say that was a wise decision when they forked it.

EDIT: replied to wrong post. my bad.

-------------------------

1vanK | 2022-01-26 05:53:54 UTC | #35

I heard you.

If it's not enough for you to have an old copy of the engine on your hard drive, but it is absolutely necessary that there are zero changes in the repository too, this is ridiculous to me, but it's your right.

-------------------------

Eugene | 2022-01-26 10:03:14 UTC | #36

[quote="1vanK, post:35, topic:7149"]
If it’s not enough for you to have an old copy of the engine on your hard drive, but it is absolutely necessary that there are zero changes in the repository too, this is ridiculous to me, but it’s your right.
[/quote]
You know, I really get a deja vu now.

Two years ago I have made a proposal of a similar nature, and received a similar reaction. Except it was somewhat more vocal and intense, perhaps because forum was more active back then.

I personally (of course) support moving forward at the expense of breaking things, but I have also learned that my desires are not the desires of this specific community.

Even if you actually switched to STL (even w/o breaking Lua), you probably wouldn't get the outcome you wanted. I believe that most people would just stay at the older version since it doesn't break their code and offers just as many features. That's why I asked you about functional roadmap: because the only way to push people forward is to offer them substantial benefits they can take and use right now, so these benefits overweigh the pain of change.

-------------------------

1vanK | 2022-01-26 10:25:16 UTC | #37

Probably my English is so bad that no one understands what I mean. I see no reason to spend more time on this.

-------------------------

Naros | 2022-01-26 16:57:14 UTC | #38

I don't think it's a comprehension issue @1vanK FWIW.

Unless the goal here is to release Urho3D 2.0, then I think any type of effort to move a codebase forward should always be mindful of compatibility.  Changes like this can be done in a way in which the code is backward compatible while getting the benefits of the performance you seek.

Compatibility to me is a critical aspect of code adoption.  Anything that causes the adoption of changes to be hindered leads to the potential for more regressions and unstable code due to a lack of rigorous testing across a plethora of platforms and environments.

Lots of users rely on `Urho3D::Vector` and `Urho3D::PODVector` in their code and this change is going to be extremely disruptive, particularly if it's in a micro release.  I would strongly suggest that if you want to get the performance benefits of `std::vector` that you abstract the detail of the change away, as suggested by @S.L.C in his comments on your PR rather than simply changing the usage at every call site as you have begun in your PR.

-------------------------

1vanK | 2022-01-26 21:24:16 UTC | #39

No - this is a problem of understanding. You just confirmed it with your post.

-------------------------

1vanK | 2022-01-26 21:42:14 UTC | #40

I can only repeat only what I wrote earlier. You all write about some mythical engine developers. But they just don’t exist. Your choice is to
1) have zero changes in the repository
2) keep an old copy that you like and be happy with it and ignore changes in the repository

In both cases, you will be using the same old version of the engine. So what’s the difference to you?

Everyone writes about the performance of vectors. I do not understand. Maybe in the title there is something about the performance of vectors? What I write about is that any changes to the engine are complicated by LUA bindings that no one wants to maint.

Oh, and the opinion of the community. This is my favorite phrase. Why on earth should I care about the opinions of people who use the engine out there and contribute zero to the development of the engine. In biology, this is called parasitism. Personally, I participate in the development of the engine in order to create a great engine together. And the parasitic community is simply limited to wishes that someone has to fulfill. But personally, I will fulfill my wishes, since this is not my job and you do not pay me to fulfill your wishes. If you have an idea how the engine should look like, come and write the code. Or keep your wishes to yourself.

-------------------------

S.L.C | 2022-01-26 21:55:06 UTC | #41

[quote="1vanK, post:40, topic:7149"]
keep an old copy that you like and be happy with it and ignore changes in the repository
[/quote]

Not trying to be mean or anything. I'm honestly not that invested in this. But your logic can also be flipped. Why can't you make these breaking changes on a copy of your own? i.e. a fork

-------------------------

1vanK | 2022-01-26 21:59:10 UTC | #42

This is the first variant in my post.

-------------------------

Naros | 2022-01-26 22:27:11 UTC | #43

[quote="1vanK, post:40, topic:7149"]
Your choice is to

1. have zero changes in the repository
2. keep an old copy that you like and be happy with it and ignore changes in the repository
[/quote]

I agree the problem is understanding, but I disagree that its on my part.

I never said you shouldn't evolve the codebase.  Code evolution is equally critical as the steps you take to do it in the first place.  That's where my concern lies, your approach; not the end result.

You want to use `std::vector`, do it but find a way that minimizes the disruptive nature of the change.  I pointed out the suggestion on the PR which is a valid and practical way to do just that.  If you're so against that approach, then why don't you explain why that won't work or why you are against it?

Lastly, your second point again proves you either didn't read my post or comprehend it; and either way that's fine so I'll try and be more clear and direct.

The philosophy I've learned by working in open source development is that it's always important to not only think about what you get out of a change as the developer but to consider the experience and user that will be impacted by your changes.  

There will always be situations where users will remain on legacy versions for this or that.  But it's our job to design clean, clear, and as easy as possible upgrade paths to sustain community involvement.  If you begin to do things that go against that, you hurt whatever community you have left.  And then at what point is the development at all if you lose the community?

I'll happily let this go if you can show me a logical and justified reason for making the change in the manor in which you are.  Again, to be clear, I'm not saying don't make the change; I'm just asking you to do it in a way that's less disruptive.  That's two different things.

-------------------------

1vanK | 2022-01-26 22:30:17 UTC | #44

We took into account the opinions of users for 8 years and now the community consists of only users.

-------------------------

1vanK | 2022-01-26 22:36:08 UTC | #45

[quote="Naros, post:43, topic:7149"]
I’ll happily let this go if you can show me a logical and justified reason for making the change in the manor in which you are. Again, to be clear, I’m not saying don’t make the change; I’m just asking you to do it in a way that’s less disruptive. That’s two different things.
[/quote]

I have already said everything I wanted to say. I can only repeat what has already been said. But I would like to know who you are and why do I have to prove something to you?

-------------------------

Naros | 2022-01-26 22:36:12 UTC | #46

I mean to add more in my prior rely and hit submit, so I'll continue here.
[quote="1vanK, post:40, topic:7149"]
his is my favorite phrase. Why on earth should I care about the opinions of people who use the engine out there and contribute zero to the development of the engine.
[/quote]

I eluded to this above.  If you have a development team that is hellbent on doing it their way and the voice of the users doesn't matter, users will eventually move on and give up and find something else.  Then what's the point of your contributions?  

Sure you might use the engine in your projects, a few others might use it that develop it or are close friends but again is the effort then worth it if your audience is so small?

[quote="1vanK, post:40, topic:7149"]
But personally, I will fulfill my wishes, since this is not my job and you do not pay me to fulfill your wishes. If you have an idea how the engine should look like, come and write the code. Or keep your wishes to yourself.
[/quote]

I don't understand why you seem to feel so attacked by someone who shares your desire to make changes but is asking for those changes to be tackled in a slightly different style.

If I have to contribute to this project to even be allowed to make a constructive critique about something that I agreed with you but challenged your approach; then perhaps I (as well as others) should see this for what it is and move on.

-------------------------

1vanK | 2022-01-26 22:39:44 UTC | #47

My efforts are my efforts, and I myself will decide how to distribute them. You can explain to me what difference it makes to me how many users of the engine, zero or a million, if they do not contribute to the engine, but only, as it turned out, are an obstacle for me.

-------------------------

Naros | 2022-01-26 22:43:31 UTC | #48

[quote="1vanK, post:45, topic:7149"]
But I would like to know who you are and why do I have to prove something to you?
[/quote]

I'm just an avid developer who has been using Urho3D for several years just giving you my perspective on your change; that's all.  I came over from Ogre3D after the massive changes just made the entire upgrade and development experience a mess.  I just would hate to see this project follow in the same footsteps.

And you have to prove nothing to me; you've shown me plenty.

-------------------------

1vanK | 2022-01-26 22:44:51 UTC | #49

Then I would suggest you some commercial engine.

-------------------------

JTippetts1 | 2022-01-26 22:56:01 UTC | #50

Here are my thoughts:

It seems like the whole point of switching to std::vector would be for interface reasons, to allow containers to hold to what is the standard as far as naming and usage, but doing so would, of course, break compatibility. While performance is mentioned in the initial post as the reason for the change, let's be honest here: I doubt there is a single Urho3D project out there where the performance of the vector class is an actual bottleneck. Choosing performance as the reason feels like bikeshedding to a large degree.

I can't really fault @1vanK for not wanting to mess around with the Lua bindings. I say this as someone who likes Lua, who was delighted when Lua was brought to the project, and who is currently using Urho3D+Lua for a work project: those Lua bindings are *rotting*. The Lua language has incremented 3 version numbers since the bindings were written, and coming back to Urho after using other tools with newer Lua versions feels odd. Not to mention, there are still the various wierdnesses inherent to tolua being used as the binding agent. It is a well-known fact that having to implement not one but two script interfaces has demonstrably hampered the progress of this engine. If nobody is willing to step up to do the maintenance work on the Lua bindings, then *Urho3D Lua should be allowed to die.* 

Make a major version release, tag it, then start a new major version and do what is needful to start bringing progress again. Being afraid and stuck in stasis because a handful of users don't want the change seems unwise to me. Let them have a bugfix-only release, and let the devbranch start working on fun new features and technological advancement. This project will not advance, and will instead continue to shed users and spawn forks, if some of the roadblocks to progress aren't removed.

Officiallly bless one of the script interfaces, purge the other, and *move on*. 

Swap out the containers for something that adheres more closely to the standard. rbfx switching to EASTL was one of the lures for me to start using it for some projects. A standard-compliant container interface is wonderful when it comes to integrating old code or code from other projects and places.

-------------------------

Eugene | 2022-01-26 23:02:54 UTC | #51

[quote="1vanK, post:40, topic:7149"]
Oh, and the opinion of the community. This is my favorite phrase. Why on earth should I care about the opinions of people who use the engine out there
[/quote]
Because when you push something to the project with existing community, you are the servant of this community, and must consider its opinions.

When you push something into your personal repository, you do whatever you want.

That’s the main difference, no?

If you remember, I have stayed in the fork and not pushed my agenda exactly because I had no moral right to force my opinion and ignore opinions of the community, completely regardless of how much code I wrote.

PS: I am not advocating for keeping Lua, this is just a general reply.

-------------------------

1vanK | 2022-01-26 23:07:40 UTC | #52

I've been in this project for so long that I'm not sure that there are still people here who were a community before I came. Moreover, even before I started sending commits to the repository, I wrote a series of articles in the Russian-speaking segment to attract Russian-speaking users in the hope that new developers would come.  So I tend to think that it was not me who imposed on the community, but attracted part of the community to the engine. In addition, I did not sign any documents that I should serve someone. I am ready to take into account the opinion of other developers of the engine, but not random people who think that I owe them something.

-------------------------

George1 | 2022-01-28 01:00:04 UTC | #53

I believed any major changes should be in Urho3D 2. 
Maybe you can add Urho3D 2 is in the work and the repository on the main page to draw new developer's attention.   Also add a category Urho3D 2 in the forum.

This way you can have version 1 as bug fix and version 2 is a WIP.   You can then let version 1 die slowly as version 2 pick up momentum. 

I think work together with elix22.

-------------------------

Eugene | 2022-01-28 07:49:51 UTC | #54

By the way, don't forget about this page when making a release:
https://github.com/urho3d/Urho3D/blob/1.8/Docs/Urho3D.dox#L134

-------------------------

1vanK | 2022-01-28 09:01:23 UTC | #55

I'm lazy for this

==== 20 chars

-------------------------

S.L.C | 2022-01-28 13:55:45 UTC | #56

Some of you people really need to get back on the medication. Because you've been given some privileges to this project that you really shouldn't have in the first place. And I'm saying this in the most serious and genuinely concerned way possible.

Like whole mother of !>#@??? The level of communication with the community has gone to absolute nonsense.

I've tried to not say this for quite some time. But someone has to say it. Jeezus :grimacing:

-------------------------

1vanK | 2022-01-28 20:00:10 UTC | #57

Do you think this is the single problem?

-------------------------

1vanK | 2022-01-28 20:05:14 UTC | #58

[quote="S.L.C, post:56, topic:7149"]
Because you’ve been given some privileges to this project that you really shouldn’t have in the first place.
[/quote]

You probably think that I got them just like that? Maybe because I invested my time in the project?

-------------------------

adhoc99 | 2022-01-28 20:46:41 UTC | #59

So what, does that mean this is your engine now?

Might as well rename the engine too.

-------------------------

1vanK | 2022-01-28 20:50:52 UTC | #60

No, I don't think so.

-------------------------

1vanK | 2022-01-28 20:59:34 UTC | #61

And you probably consider yourself a white master who has slaves who should be happy that they follow your orders?

-------------------------

JTippetts1 | 2022-01-28 22:21:06 UTC | #62

Holy shit. Is this what we've come to?

-------------------------

weitjong | 2022-01-29 04:18:09 UTC | #74

I see no valid reason for account suspension, so I have unsuspended those that have been affected. Please read the forum rules and be nice.

-------------------------

