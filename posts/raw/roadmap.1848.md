codder | 2017-01-02 01:10:39 UTC | #1

Any roadmap for future releases? Will be cool to discuss what will be cool to have in next versions  :slight_smile:

-------------------------

dragonCASTjosh | 2017-01-02 01:10:39 UTC | #2

Something along the lines of a Trello might be useful to help see what the developers are working on and highlight areas the community can help

-------------------------

cadaver | 2017-01-02 01:10:39 UTC | #3

If you look at the github issue tracker, core devs (me and Yao Wei Tjong at least) have taken the habit of self-reporting issues, usually with tags such as 'enhancement', to indicate it's not a bugfix. These are items which are likely to be worked on in the future.

Also look at feature branches and threads in the "Developer Talk" subforum.

Compared to that, a separate roadmap might be clearer, but it'd also require duplicate data entry. Furthermore, we never promise features at a given time, considering all development happens on (limited) free time.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:39 UTC | #4

[quote="cadaver"]If you look at the github issue tracker, core devs (me and Yao Wei Tjong at least) have taken the habit of self-reporting issues, usually with tags such as 'enhancement', to indicate it's not a bugfix. These are items which are likely to be worked on in the future.

Also look at feature branches and threads in the "Development" subforum.

Compared to that, a separate roadmap might be clearer, but it'd also require duplicate data entry. Furthermore, we never promise features at a given time, considering all development happens on (limited) free time.[/quote]

I personally noticed that you self-reposted issues and enchancements. I just felt i could be useful to give a way of seeing future features that you would like to see and maybe features you don have time to work on. I appreciate that you work in free time and are unable to provide deadlines and a good roadmap should allow you to not set deadlines and maybe just list released you would like the feature attached to.

-------------------------

gawag | 2017-01-02 01:10:40 UTC | #5

Actually something like a "help needed", "help welcome" marking/list would be good.
Usually things in the issue tracker or in the core developers head (or elsewhere) get some "mind marking" in the sense of:
[ul]
[li] "Oh I can do that easily"[/li]
[li] "That takes some time but I can do that without much trouble, (Most) others would need way longer than me"[/li]
[li] "That would be good but I have to figure that out for a while or I don't really want to do it, maybe someone else could do that better."[/li]
[li] "That would be good but I have no idea and it would take me really long (to get into that area). Anyone else able to do that?"[/li]
[li] "This could be also done by someone else without much trouble, I am more valuable in other areas where others would have more trouble (due to not knowing the complex system/problem as good as me)."[/li][/ul]
("I" could be also replaced by "us usual core developers" or "developers X and/or Y")
I did that in projects by assigning some issues explicitly to me due to already having a good idea and/or plan and/or experience with that and being way more efficient as others in solving that. Maybe somehow labels could be used in combination with text like: "Urho whole system expert needed" "only terrain system interna knowledge needed" "Android developer expertise required" ...

Others could see items in that are and be like "Oh they lack expertise in X and I know area X and should be able to do that easily, I'll help there!" or "Oh they would like X and I got a nearly fitting solution lying around, that could help them!".

Also the planned scheduling would be good to know: "currently being worked on" "working on soon" "scheduled for way later" "paused until X"

Furthermore stuff planned for the next release. Usually there are also certain things in the head that a developer wants done until doing a new release. There could be a list. Even if not everything in there gets done, would be a good roadmap. "X, Y and Z should really be in the next release", "X and Z are too time consuming for this release but could be in the next release". A "rough roadmap".

-------------------------

codder | 2017-01-02 01:10:40 UTC | #6

Having a "rough roadmap" could help.
If two or more people have the same feature in mind maybe they can work together on that specific thing and implementing it in Urho3D.
Like the PBR I'm seeing in the forum. If its tracked on a roadmap maybe more people will try to work on it.

I'm sure @cadaver and @weitjong have some minded roadmap for the engine. So why not explicit write it on a proper roadmap? (ofcorse with no warranties of being made)

-------------------------

gawag | 2017-01-02 01:10:40 UTC | #7

[quote="codder"]Having a "rough roadmap" could help.
If two or more people have the same feature in mind maybe they can work together on that specific thing and implementing it in Urho3D.
Like the PBR I'm seeing in the forum. If its tracked on a roadmap maybe more people will try to work on it.

I'm sure @cadaver and @weitjong have some minded roadmap for the engine. So why not explicit write it on a proper roadmap? (ofcorse with no warranties of being made)[/quote]

Yes that's exactly what I thought. And I asked about it in the big wiki thread and the answer was: [topic778-60.html#p10696](http://discourse.urho3d.io/t/urho-wiki/760/68)
[quote="weitjong"]
[...]As for all the other questions you asked, if I may sum them all up in one sentence then you are asking about our "wiki roadmap"[?] If so, then I don't have the answer also. The fact is, if you even ask what is the Urho3D development roadmap then none of us will be able to give you any definitely answer, let alone the roadmap for the wiki itself. The wiki pages should be read and written by any of us, so I would like to think that the answers are already available in each of us. It should grow organically by itself without much governing control.[...]
[/quote]
It's really hard to get anything out of the core devs. I don't believe they just sit there, wait for a bug report or feature request and are like "uhm. yeah, uhm. I guess I could try to do that, uhm." There has to be some kind of "goal" or rough direction or stuff they aim for. (I'm being a bit sarcastic, maybe they'll react to that  :laughing: ) [i]*casts core devs: hamana hamana hamana...*[/i]

My goals regarding Urho are already explained at various placed like here: [topic778-60.html#p10704](http://discourse.urho3d.io/t/urho-wiki/760/69) (the last paragraph with the list, oh boy that's a long post  :unamused: )
My wishes for the/an engine itself are basically: free (software), easy to use, general (not super specialized for specific genres), fast / usable for big projects (think of slightly outdated "AAA" games, I guess top AAA games use very specialized engines where a general usable engine has to be behind).
Oh that are pretty general wishes. A lot that I'm thinking of is more library stuff like water with nice effects, weather system, day-night, voxel terrain (marching cubes or something), voxel water that flows (like in Terraria but 3D), local fog, ...

-------------------------

cadaver | 2017-01-02 01:10:42 UTC | #8

I can only speak for myself, but to be honest a lot of my current Urho3D development *is* reacting to issues and pull requests. The last major feature I coded was D3D11 / GL3 support and there is nothing "hidden" in my mind so to speak.

Now, I recognize this is not the best prospect for the engine's future (and not the best PR), if the lead dev is not proactively working on or planning future features.

How to remedy that is another question. I don't think I can force myself to contribute more or to be more motivated than I already am. However you'll note that with some foresight the Urho3D project in Github is not my personal repository, rather it's under the Urho3D organization. Should there be a good candidate (with both skill and more motivation) I would be open to stepping down and being replaced as the lead dev.

-------------------------

gawag | 2017-01-02 01:10:43 UTC | #9

Interesting.
I think there doesn't necessarily have to be one lead dev with great ideas/goals who pulls the whole thing more or less by himself. There can also be multiple developers, possible working on or being "responsible" for different things. That you are "reacting to issues and pull requests" is of course pretty great, that doesn't have to change necessarily. There could be others (there kinda are already) who are progressing Urho in specific areas and adding features and who don't have to know every area. Not sure how such a system is called but "area guys" are often called something like "module maintainer". The Linux (the kernel) development is managed in such a way, with most core developers being responsible for specific areas. Like a company with department heads.

Many projects die due to not having someone maintaining the whole thing. Many developers only love adding new features and don't fix existing issues with the current system.

I already mentioned some things that would be great to be (easily) possible with Urho. Some other engines like this Unity seem to have various modules that are plugged together to build a game. I'm not familiar with those systems but I've used Ogre which had some libraries/modules that could be used to (more or less easily) get nice water with waves, day-night with nice effects, editable terrain (Ogre's normal terrain is/was static), good performance vegetation/geometry via chunks, ... These Ogre "modules" though often didn't really work well together. Like the grass I had was z-fighting with the water, the sea ground was visible when looking through transparent grass (such things could have been easily fixable though).
Some of such features/modules are better kept separate, others could be integrated into Urho. Some libraries/modules may required additions or changes to Urho itself.

Such libraries/modules could also be called "external features". I made a wiki page with ideas: [github.com/urho3d/Urho3D/wiki/urho3d-wishlist](https://github.com/urho3d/Urho3D/wiki/urho3d-wishlist)
Such a list of "nice to have things" is already a kind of "rough roadmap" for "Urho and Friends" (Urho and/or libraries/modules for Urho).
Add things to that. Can be "Oh I would like X", "I've seen engine/game Y having feature X and that would be cool for Urho too", "I have ideas on how X could be done" or "there's work being done on X see here".

-------------------------

dragonCASTjosh | 2017-01-02 01:10:43 UTC | #10

[quote="gawag"]
I made a wiki page with ideas: [github.com/urho3d/Urho3D/wiki/urho3d-wishlist](https://github.com/urho3d/Urho3D/wiki/urho3d-wishlist)
[/quote]
I updated the questions on the PBR section :slight_smile:

-------------------------

cadaver | 2017-01-02 01:10:43 UTC | #11

Gawag, I definitely agree on the multiple developers, a great deal of Urho's new features like Emscripten support are due to our (relatively speaking) newcomers.

My suggestion regarding development is to use the Github issue tracker and pull requests as much as possible (even in favor of the Developer Talk forum), because then proposed code changes and discussion regarding them can be kept in one place, even when it's very early in some feature's history. Also, by commenting on some issue that interests you, you can quickly verify that no-one else will be doing duplicate work.

What we could do better / more rigorously would be to assign release milestones to issues, in which case the issue tracker would act more as a live roadmap. It was used at one point more but then fell to disuse. However, even then making a new Urho3D release is not necessarily about new features being put in, but more about that the whole is in a good state without major known bugs.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:43 UTC | #12

[quote="cadaver"]
What we could do better / more rigorously would be to assign release milestones to issues, in which case the issue tracker would act more as a live roadmap. It was used at one point more but then fell to disuse. However, even then making a new Urho3D release is not necessarily about new features being put in, but more about that the whole is in a good state without major known bugs.[/quote]
Using the Milestone system early into a development cycle could be useful to set solid goals for the community and everyone to clearly see what the developers imagine being in the next release.

-------------------------

gawag | 2017-01-02 01:10:44 UTC | #13

[quote="dragonCASTjosh"]
I updated the questions on the PBR section :slight_smile:[/quote]
Oh cool. That looks already pretty usable. I added that to the library page and posted a question in the PBR thread.

[quote="dragonCASTjosh"][quote="cadaver"]
What we could do better / more rigorously would be to assign release milestones to issues, in which case the issue tracker would act more as a live roadmap. It was used at one point more but then fell to disuse. However, even then making a new Urho3D release is not necessarily about new features being put in, but more about that the whole is in a good state without major known bugs.[/quote]
Using the Milestone system early into a development cycle could be useful to set solid goals for the community and everyone to clearly see what the developers imagine being in the next release.[/quote]
That sounds great. I actually used that in a GitHub project to mark the features in the issue tracker that I wanted in the next/first release, to set myself a goal.

Another thing that is also important is the stuff surrounding the technical side of Urho: Like documentation and examples. Improvements there would (also) help to get more Urho user and developers in. Generally spoken: A good product is pretty useless if no one understands it.

-------------------------

codder | 2017-01-02 01:10:44 UTC | #14

:smiley: same here... sometime I saw it sometimes no. But yea figured it why...

Anyway there are some issue in the tracker with no tags...

Like:
[github.com/urho3d/Urho3D/issues/1069](https://github.com/urho3d/Urho3D/issues/1069)
[github.com/urho3d/Urho3D/issues/1201](https://github.com/urho3d/Urho3D/issues/1201)

or even older:
[github.com/urho3d/Urho3D/issues/165](https://github.com/urho3d/Urho3D/issues/165)

-------------------------

