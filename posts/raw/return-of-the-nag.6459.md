rku | 2020-10-26 17:10:44 UTC | #1

@weitjong i can not help but observe a repeating history. I believe same exact cause resulted in build system to remain a stagnating pile of legacy hacks. When i wanted to fix it - i inevitably needed your help, but you had other things to do. Now someone wants to update SDL. Likewise you have other things to do. No one has a right to demand these things from you of course. However we are in a situation where a maintainer assumes exclusive control of certain parts of the project and is not interested in mentoring future contributors. This simply drives those contributors away. Attempts to improve something without support of maintainer of those subsystems is doomed to fail. I am quite disappointed that these attempts are driven to the ground just like that. Project is not exactly flourishing and does not quite have that many potential contributors to waste. Make your own conclusions now.

I have also a little criticism regarding modifications in SDL cmake script. When i tried to look into upgrading SDL, this part stood out as extremely complicated, because of tiny one reason: modifications are commented and they say "commented out this and that", while in reality code from CMakeLists.txt is _removed_. This creates quite a problem when comparing to upstream cmake script as it is not clear what parts should be omited and what parts were added in upstream between our current version and upstream version, and should be ported to our build script. I would prefer dead code be commented out for the sake of simplifying updates. It may not be a problem to you @weitjong personally, but it artificially raises a bar for new contributors. Actually i would argue same policy should be adopted for modified source code, commenting out original bit and adding a modified section, instead of modifying original code directly, losing ability to see exact modifications versus upstream version at that time.

-------------------------

Modanung | 2020-10-26 11:12:43 UTC | #2

[quote="rku, post:1, topic:6459"]
Project is not exactly flourishing and does not quite have that many potential contributors to waste.
[/quote]

*You* left two/three years ago incessantly claiming Urho was dead, while piping some contributors along with you by simultaneously announcing rbfx as an "experimental branch of Urho". :confused:
But by all means, feel free to contribute to a project that matters, once again. I'm sure you learned a thing or two during your aimless wander.

-------------------------

weitjong | 2020-10-26 11:12:43 UTC | #3

Well the changes are all in the history of git. If you look for it all the changes were there, even when the lines are deleted. I don’t like commented out lines that serve no more purpose to remain in the code. I also don’t like to waste my time keep upgrading the libraries for you guys. So, if you can do a better job at this, then please do it. You see I don’t stop OP from trying. If he can do it then do it. If you want to do it also fine by me.

Also, I am a human too. I only have a pair of good hand but not a good pair of eyes anymore. I may not able to stop immediately what I am currently doing or interested with and then help anyone on first notice, like I am under contract or have obligation to do so.

-------------------------

Modanung | 2020-10-26 11:28:41 UTC | #4

Though art our beacon, @weitjong. Radiance does not require eyes - not those two anyway - and a [lighthouse](https://invidious.kavin.rocks/watch?v=SDn1KAP5otM) should not be expected to function as a factory. :slightly_smiling_face:

-------------------------

rku | 2020-10-26 11:12:43 UTC | #5

Please do not take my comment as a personal attack. To clarify: you take exclusive charge of certain subsystems which are so complicated (needlessly like SDL, or due to legacy reasons like build system). No one can even to begin help you share the burden without your support. I wanted to help, remember? There were plenty of obstacles in the way that you know how to navigate (build system itself, CI). I wanted your mentorship. You were busy at that time, i get it. But i did not sense any desire to mentor me and help me make project better. I had a feeling i am on my own so i moved on. Now @glebedev wants to help, but message i see is once again "you are on your own". I guess what i am missing in communication from leadership is something like "i am busy, but i would love to help you do this. how about lets chat <insert whatever platform is preferred>?" Answering couple questions in the chat and sharing your burdens with someone is easier than maintaining everything yourself and sometimes deadlocking project, even if for very valid reasons.

tl;dr; when people want to help - please accept help offered. :pray:

-------------------------

weitjong | 2020-10-26 11:12:43 UTC | #6

That’s bullshit. When I first tried to do the SDL upgrade, I didn’t ask anyone else or Lasse for help. I just persevere until I get it work. You don’t have to follow my way in doing thing. Just like years ago you wanted me to explain my CI scripts to you so you can make them work for your own fork. My answer was, why you wanted to reuse my old scripts. And, now when I have my free time and mood, to migrate from the old CI scripts to the Github Actions and I am having fun with it, you asked me to drop it so that I can teach you how to do SDL upgrade. If I may say about you is that each time we have a good momentum in the project progress then you come to throw a curve ball.

I work for this project just for fun, not for profit. And if I cannot even get the fun part then I may stop all together.

-------------------------

Modanung | 2020-10-26 11:12:43 UTC | #7

[quote="weitjong, post:6, topic:6459"]
That’s bullshit. [...] If I may say about you is that each time we have a good momentum in the project progress then you come to throw a curve ball.
[/quote]

I would not oppose banning the trolling fool, just saying.
He's been talking pretty low about you behind your back on Gitter, in the knowledge you don't visit there.

-------------------------

rku | 2020-10-26 12:13:05 UTC | #8

I am sorry you feel that way. You are a maintainer however, and in my eyes such attitude keeps project in a deadlock. I am merely pointing that out. Mentoring someone to take over maintenance burden would be a good way to free more of your time and let you work on this just for fun. I am merely highlighting state of affairs. No need to get defensive about any of that. Although it seems like we will disagree about anything i say. For example a while back i said auto-closing issues was a bad idea and we had no agreement over that. Months later lots of issues get closed even though they were not fixed. This even applies to PRs. For some reason i decided that it would be a good idea to submit a PR updating bullet, because why not. It will soon be closed due to no activity. What message does this send to potential contributors?

-------------------------

GoldenThumbs | 2020-10-26 13:22:24 UTC | #9

Don't stoop that low. This is an actual problem, and whether you want to admit it or not calling him a "troll" for merely airing concerns isn't professional and doesn't help the project in the slightest. There has been a lack of updates, I don't really see any new contributors joining given the current state of things. If you want to help Urho die then please, by all means continue down this path. I don't think we're dead quite yet, but we need contributors and contributions.

-------------------------

Modanung | 2020-10-26 17:00:43 UTC | #10

I'm aware that those ignorant on this matter will consider _me_ the unjustly critical. Still, I rather do it out in the open. This has been going on for years. I do not take these terms lightly, and if you want me to be honest; I believe @rku is a sociopathic money hound *leeching* on other people's hard efforts, good intentions and limited awareness. Poisoning the well, with every opportunity he sees, covertly out for the kill so he may salvage contributors from a poached project.

...of course one can never be certain, but I'm doubting this judgement less and less.

-------------------------

Modanung | 2020-10-26 16:38:25 UTC | #11

[quote="GoldenThumbs, post:9, topic:6459"]
I don’t think we’re dead quite yet, but we need contributors and contributions.
[/quote]

Agreed, go ahead. :slight_smile:

But I'd get it if you'd prefer the waters to clear again first. Moments like these leave everyone who cares about Urho with a bad taste in their mouth, myself included.

-------------------------

Modanung | 2020-10-26 16:49:03 UTC | #12

[quote="GoldenThumbs, post:9, topic:6459"]
I don’t really see any new contributors joining given the current state of things.
[/quote]

https://discourse.urho3d.io/t/update-sdl-2-0-12/6456

You see how it was all developer talk until it *somehow* turned into a soap opera?


---


https://discourse.urho3d.io/t/custom-rtti-and-eventbus/6458

There's people working everywhere, but this is not the industry.

-------------------------

Modanung | 2020-10-26 17:13:34 UTC | #13



-------------------------

weitjong | 2020-10-27 00:35:32 UTC | #14

The project is not just maintained by me. Eugene and others are also there. Why you just blaming it all to me? For as long as I remember, I am only the maintainer for the build system. If you want to take over the project, just say so loudly. Oh, but isn't you guys have tried that and failed? Why not you just concentrate on your own fork and let the Urho3D project die slowly, if you think that is what will happen, but still keeping it in its original state/vision where its original project owner left it. Not the castrated version like in your fork.

-------------------------

