Leith | 2019-08-17 03:20:17 UTC | #1

I noticed there's a lack of appropriate error handling in the Navigation classes... the first thing I noticed was that NavigationMesh::FindPath has absolutely no error checking of return values, and itself returns void - there is no triggering of a statechange event that could inform us that a pathfinding attempt has failed. The next thing I noticed was that FindNearestPoint does something almost as bad - if it fails to initialize a query object, or fails to locate nearest polygon, it simply returns the input point - no error event is sent, and no useful error appears to be stored anywhere.

All that effectively means that if I try to find a path to a target point that is completely outside the bounds of my navmesh, I am greeted with silence, rather than "path not found"... and if I ask for the closest point on the navmesh to my invalid target point, I am handed back the same invalid point!

Just wondering how others may have approached the lack of appropriate error handling when making invalid navmesh queries..

-------------------------

Modanung | 2019-08-18 10:47:52 UTC | #2

Please read the [git book](https://git-scm.com/book/en/v2) I sent you earlier. The knowledge held within will allow you to suggest concrete changes instead of only being able to point at work. That would be most helpful.

-------------------------

Sinoid | 2019-08-18 03:54:15 UTC | #3

Detour rarely returns any sort of meaningful error-code for us to do anything whatsoever with. In order for Detour's `findNearestPoly` to actually say that it "**failed**" you have to give it garbage it inputs, otherwise Detour will always **succeed**.

Most of navigation runs into philosophical dilemmas about *"what is a failure?"*, crowds only have so much psychotic and overbearing error raising because DetourCrowd does have some sort of discernable valid state, unlike a random query.

So what then is failure for `FindNearestPoint`? Absence of a poly-ref from `dtNavMeshQuery::findNearestPoly`? What does that even rationally mean and what's the ratio of genres where that would be an error to those that it wouldn't be? 

Since navigation is ultimately project specific, a lot of navigation just walks away from that problem and leaves it to the end-user.

---

I regret submitting the PR for detour-crowd. Objectively, none of navigation has any business being there at all and belongs elsewhere like a community repo so that it's approached from the "*I'm going to have to fiddle with dials and tweak some code*" angle as it should be.

-------------------------

Leith | 2019-08-18 13:02:36 UTC | #4

@Sinoid - For FindNearestPoly, this may be the case... but FindPath can return a meaningful result for sure, and we're doing nothing with it.
Please feel no regret for your work with detour-crowd: its good work, I applaud and thank you for taking the time! I plan to make use of at least some of it! 
The issues I refer to are based in the NavigationMesh class, not per se the crowd stuff built on top. I'm certain there's a simple way to remedy this situation without going back to the drawing board :slight_smile:

-------------------------

Leith | 2019-08-18 11:38:20 UTC | #5

@Modanung - There are two parts to problem solving - I'm with you on the GIT stuff and I will remedy, but it would make no sense to publish in a vacuum, without being able to reason, in public, about what the (perceived) issue was - preferably, prior to addressing it. Sometimes I overlook things entirely, and at least to my mind, it's not an attack on the system to point out where the system could be improved.
I'm not offering a solution, I realize it, I was kinda hoping someone else may already have addressed it, perhaps in some far flung fork, where it languishes, waiting to be rediscovered.

-------------------------

throwawayerino | 2019-08-18 13:30:01 UTC | #7

I never had any problems with navigation so far, and the integration is great. My usage of it isn't very demanding, but I'm grateful for it

-------------------------

Leith | 2019-08-18 13:35:20 UTC | #8

Me too - it works perfectly, when we request a target inside a safe volume, but we're game devs, and the volume is never safe... just to see what would happen, I asked for a target outside the world. I got nothing - no errors, no replies. This is not good.

-------------------------

throwawayerino | 2019-08-18 13:35:13 UTC | #9

You're the game dev here. A good game is a game where you provide the illusion of the player being in control. If they can create unsafe environments, then either too much control is being given, or there isn't a warning being shown.

-------------------------

Leith | 2019-08-18 13:36:30 UTC | #10

If WE create unsafe environments, the game is not going to succeed... we need to be rock solid.

-------------------------

Leith | 2019-08-18 13:41:03 UTC | #11

Games rely on robust rules, and so do we, game developers: programmers, artists, audio engineers, marketing people, we all live and breathe rules, but the rules can always give way to positive change. Here's a sore spot though, because the query method, and the query reply structure, neither give us space to talk about who's doing the asking. This makes it slightly harder to make a meaningful event to notify about this failure, without changing the return value, and breaking existing code. Sigh.

-------------------------

Leith | 2019-08-18 14:19:49 UTC | #13

Certainly can give a use-case! NavMeshes are finite creatures, that may or may not be connected to others, via off-mesh links. Games on the other hand, particularly those with physics involved, are unbounded, and things will try to escape our world, with or without the help of the players.
If we are trying to track our way to something we want, that has left the nav mesh, and we are using nav mesh queries to do so, we are screwed - that is to say, we can't seek a target outside of the navmesh in which the query began - whether or not its in a valid navmesh elsewhere.

-------------------------

Leith | 2019-08-18 14:23:50 UTC | #14

I'm pretty sure I got that right... please anyone, step in and enlighten me :slight_smile:

-------------------------

Leith | 2019-08-19 07:36:18 UTC | #15

I've begun to patch this issue, starting with the NavigationMesh class.

The two FindPath methods were returning void - since anyone already calling these methods was not expecting / using the return value, this meant it was "safe" for me to change the return type to dtStatus, and return a meaningful result (success, failed, or pending, but there's actually a lot more rich information available in the status bits than that - see DetourStatus.h)

The FindNearestPoint method was already using its return value - so I tacked on an extra input argument, an optional dtStatus*=nullptr, which if valid, is used to return the status value from its call to navMeshQuery_->findNearestPoly. Adding an optional arg with a default value, again, does not break any existing code.

There were some subtle changes made to the code, mainly to return a failure code, instead of just exiting early. I also had to modify DynamicNavigationMesh.cpp already, just to make it include the dtStatus stuff, so that the NavigationAPI.cpp angelscript stuff stopped complaining.

I am not sure why, but NavigationMesh.cpp is including DynamicNavigationMesh.h, this seems like a backward arrangement, since the classes are related the other way around.

I've checked that my changes compile, and don't affect existing code, but I'll test them out before I take this any further - and by that I simply mean reflecting these changes in DynamicNavigationMesh.

-------------------------

Modanung | 2019-08-19 19:08:24 UTC | #16

Do you plan to issue this improvement as a pull request? If so, I guess it would make sense to do so for the original repo, to which Urho could then sync:
https://github.com/recastnavigation/recastnavigation

I have no idea when our repo was last synchronized with theirs, btw.

Basically this is *not an Urho3D issue*, but rather a feature request for Recast & Detour.

-------------------------

Leith | 2019-08-20 06:16:18 UTC | #45

Yep, I plan to push this to my repo, and then issue PR, not that it has historically been a useful avenue for publication for me personally, but yes, I do plan to PR

-------------------------

Leith | 2019-08-20 06:27:56 UTC | #46

For me, personally, its more valuable to talk about code, to be seen talking about code, than to provide code examples, but I am always happy to adapt to meet the need.

-------------------------

Modanung | 2019-08-20 14:23:24 UTC | #47

[quote="Leith, post:45, topic:5479"]
not that it has historically been a useful avenue for publication for me personally
[/quote]

Could you put to words what you considered not useful about your single PR experience?

https://github.com/urho3d/Urho3D/pull/2412

-------------------------

Leith | 2019-08-26 09:38:48 UTC | #48

Yes.
I patched an issue, my first issue, and my patch is not in the master branch. Why not? It passed all tests. Why was it ignored? I feel like I wasted my time. I've since posted all my current changes, except that one, to my working repo. PR or not.

-------------------------

Miegamicis | 2019-08-26 09:38:24 UTC | #49

The thing is that it's your PR, there was a proposed way how to test it but not further action was taken and no additional comments regarding the test results. I thought that I would be able to help, but so far  haven't found the time to do so and it's not really my duty to do it, since I'm allowed to participate in the project as much as I want to.

-------------------------

Leith | 2019-08-26 10:34:50 UTC | #50

What is the avenue for feedback provided with the PR mechanism? Who has access? Who sees what?

-------------------------

Miegamicis | 2019-08-26 12:27:15 UTC | #51

Everyone can see PR's and discussions with them. So anyone could potentially participate in the conversation.

-------------------------

Leith | 2019-08-27 10:59:45 UTC | #52

So everyone who had access to see my PR, whether they tested or not, effectively ignored it, and nobody is in charge of actually merging the changes?
I'm not sure what to make of that. For now, I'll just post my changes on my own fork. I have a copy, there's a copy on another system, and people can see it if they want to. I can link to it, everyone's happy.

-------------------------

Miegamicis | 2019-08-27 11:17:27 UTC | #53

Yes, almost all viewers ignored it. No one tried to test it, no one commented about the state of the PR and sadly that's when everything stopped. In the past months the activity in the main repo has decreased, but we can still make it better by actively participating in the PR reviews. Your provided changes are still actual to this day and I would like it to get merged, but not without additional testing and feedback.

Don't be discouraged to submit your changes, engine needs improvements and don't let your first PR experience get in your way.

-------------------------

Leith | 2019-08-27 11:21:06 UTC | #54

I won't be submitting PR for the time being. But I will link to my changes, and there is a record.

-------------------------

Miegamicis | 2019-08-27 11:21:07 UTC | #55

Can we continue the discussion in the PR?

-------------------------

Leith | 2019-08-27 11:25:43 UTC | #56

check ur mail ;) I have responded.

-------------------------

