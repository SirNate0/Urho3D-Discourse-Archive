Leith | 2019-09-19 03:55:31 UTC | #1

While playing with some widgets based on DebugRenderer's DrawTriangle method, I noticed that depth testing was failing for debugdraw solids - to be clear, they are properly depth tested against scene geometry, but NOT each other!
When I examined the sourcecode for DebugRenderer:Render method, I noticed that, for some silly reason, depth write is being disabled immediately prior to drawing depthtested triangles!
I moved the offending line of code slightly futher down, to just prior to non-depth triangles, this completely fixes the problem, debug solids will be properly depth-sorted.![Screenshot%20from%202019-09-19%2013-54-28|690x388](upload://hg5f9l4TANGSopc9ylLADMJTHDs.png)

-------------------------

Modanung | 2019-09-18 20:23:57 UTC | #2

Could you turn this into a pull request?

-------------------------

Leith | 2019-09-19 01:27:24 UTC | #3

It's hardly worth the effort!

Very near the end of DebugRenderer::Render method,
[code]
    graphics->SetBlendMode(BLEND_ALPHA);
    // graphics->SetDepthWrite(false);              /// MOVED THIS

    if (triangles_.Size())
    {
        count = triangles_.Size() * 3;
        graphics->SetDepthTest(CMP_LESSEQUAL);
        graphics->Draw(TRIANGLE_LIST, start, count);
        start += count;
    }
    
    graphics->SetDepthWrite(false);                 /// TO HERE
    if (noDepthTriangles_.Size())
    {
[/code]

-------------------------

Leith | 2019-09-19 04:03:39 UTC | #4

Apparently, I can't turn it into a pull request just yet, as my first PR is still being evaluated... I'm denied from issuing another PR under the same credentials until this one is sorted, I gather.

-------------------------

Modanung | 2019-09-19 09:00:14 UTC | #5

That's nonsense. One-liners are more likely to pass without much consideration.
Especially if they fix bugs.

-------------------------

Leith | 2019-09-19 10:20:28 UTC | #6

I am delimited from issuing PR until the current PR is cleared, it appears

-------------------------

Leith | 2019-09-19 10:23:22 UTC | #7

I have over 60 changes to push now, and I can't issue PR, to the master, under my current credentials

-------------------------

TheComet | 2019-09-19 13:00:00 UTC | #8

You can submit multiple PRs. They just have to be on different branches

-------------------------

Leith | 2019-09-19 13:13:49 UTC | #9

So every time I want to issue PR I need another branch, until or unless someone plays catch up? sounds enticing

-------------------------

Modanung | 2019-09-19 16:21:14 UTC | #10

I recently did a [one-line PR](
https://github.com/urho3d/Urho3D/pull/2505). It was merged the same day. The same could be true for your improvement to the DebugRenderer. The amount of simultaneous changes greatly defines how much effort it takes others to make sense them

-------------------------

SirNate0 | 2019-09-19 16:00:38 UTC | #11

Personally, I have no objections to having multiple branches. If you do, I'll offer a benefit to multiple branches that I've experienced: it makes it easier to bring your code into line with the master branch if you have merge conflicts. I have my own personal branch with a couple of changes that have not been merged into master, and I can easily have a dozen files with merge conflicts when updating to the latest master. Using branches, it's easy to just update the branch that follows Urho's master to head, then branch and make the couple line changes without having to merge all the other changes with the new changes that were pulled. It's then just pushing to my GitHub account and creating a new pull request, which as Modanung pointed out, is then very easy to review when it's a couple lines fixing some bug.

-------------------------

Leith | 2019-09-20 07:23:32 UTC | #12

I appreciate that merging, and testing, is not trivial - even when it can be partially automated. I'd have preferred to PR atomically for each change I make, but given that the first one I ever offered is still languishing, I chose to put them up on a cloned repo, and occasionally shuffle them across to my fork. This puts a much greater load on those who are meant to be handling the merging, I know, but if my first atomic PR is still languishing, why should I expect branched atomic PR not to languish also?
Personally, I don't stand to gain anything, whether people can see my changes, or not, but I did offer to donate some time to remedy some outstanding issues, and will continue to document and remedy issues, and push them Somewhere Public - I'll also create a branch or two, because my changes tend to be erratic and not directed at one thing at one time, but rather what I stumble across from day to day. I mean that, when I say "from day to day", I would like to be issuing PR almost daily, but there's no sign that our current crew can keep up.

-------------------------

Modanung | 2019-09-20 08:10:00 UTC | #13

[quote="Leith, post:12, topic:5595"]
I’d have preferred to PR atomically for each change I make, but given that the first one I ever offered is still languishing...
I would like to be issuing PR almost daily, but there’s no sign that our current crew can keep up.
[/quote]
In an ideal world you'd test your unfounded biases. In cases like these it takes you and the "current crew" the same amount of effort as when not making PRs, while having a more productive result.

-------------------------

Leith | 2019-09-20 08:34:07 UTC | #14

I do test each and every thing I would propose, it vexes me that you would imply I do not, it would insinuate I was unprofessional in my approach, which would also reflect on the establishments that provided me with my qualifications, plural.
You do not recognize my qualifications - personally?

-------------------------

Leith | 2019-09-20 08:31:43 UTC | #15

I ask for third party testing, and provide full source, annotated with comments, what more can I do?

-------------------------

Modanung | 2019-09-20 08:35:39 UTC | #16

Bla, bla, bla...
PR?

-------------------------

Leith | 2019-09-20 08:36:23 UTC | #17

I will branch PR as I have no alternative, but I may think twice about what I care to share, ok with you?

-------------------------

Modanung | 2019-09-20 08:38:10 UTC | #18

Fortify your beliefs wherever you like. That does not make them accurate.

-------------------------

Leith | 2019-09-20 08:38:19 UTC | #19

This is not how its meant to be. Sigh.

-------------------------

Leith | 2019-09-20 08:40:15 UTC | #20

My bug fixes are accurate. You're merely setting formalities for sharing of information, and then stepping on it. I do not agree with your process.

-------------------------

Leith | 2019-09-20 08:41:49 UTC | #21

I want to share openly, I am not an annoying idiot, I am a qualified peer, I should have the right to speak.

-------------------------

Leith | 2019-09-20 08:42:41 UTC | #22

please be aware, this conversation is being recorded. I am over abuse of power.

-------------------------

Leith | 2019-09-20 08:44:03 UTC | #23

Tread carefully, because everyone will be able to see what you say next.

-------------------------

Leith | 2019-09-20 08:46:35 UTC | #24

If you continue to suppress me, I will leave, and push my own fork, which is already well better, over 60 files changed, over 1000 code points touched

-------------------------

Leith | 2019-09-20 08:48:50 UTC | #25

you're in a position to be a friend, and all I really want is to improve the engine, so stop being such a dick, and accept I am trained and know my shit, and let me fly

-------------------------

Leith | 2019-09-20 08:50:16 UTC | #26

this sense of being held back, i have documented on my end

-------------------------

Modanung | 2019-09-20 08:51:54 UTC | #27

The sense of being held back is a self-sustaining one.

-------------------------

Leith | 2019-09-20 08:52:51 UTC | #28

just here mate, I can code outside this, wrote entire render pipes, I do not need you, but you could learn a lot if you stopped assuming everyone is a beginner

-------------------------

Modanung | 2019-09-20 08:54:14 UTC | #29

I have some experience with people with experience.

-------------------------

Leith | 2019-09-20 08:54:50 UTC | #30

it does not show, I believe you, but show me the evidence, I have evidence

-------------------------

Leith | 2019-09-20 08:55:37 UTC | #31

I believe you lied to me, when you claimed not to be a coder

-------------------------

Modanung | 2019-09-20 08:56:48 UTC | #32

I have no papers, nor any professional experience writing code. But thanks.

-------------------------

Leith | 2019-09-20 08:56:50 UTC | #33

thats not relevant, recognition of prior learning is a thing, you can clearly understand me

-------------------------

Leith | 2019-09-20 08:57:56 UTC | #34

it does not matter where you learned it, it just matters that you know it and can prove it, that is the base line

-------------------------

Leith | 2019-09-20 08:59:07 UTC | #35

I want to see my fixes applied, but sending them to you, would be a waste of time, and the guy in charge of assimilating and merge, is not doing his job

-------------------------

Leith | 2019-09-20 09:10:55 UTC | #36

I feel alone, but I will push back. It is my nature.
Perhaps the engine, will need to chase me. At least for some time. Who else tests thing at this level, and finds fault, after all these years? I do, I test stuff, because I use it. Making fixes and not providing them is not my scene, I want us all to be on the same page.

-------------------------

Modanung | 2019-09-20 09:19:51 UTC | #37

@Leith You're being a bad contributor. But I'm certain you would be capable of great stuff if we manage to sort this one out.

-------------------------

Leith | 2019-09-20 09:20:00 UTC | #38

Recently in my life, I had no papers, no official recognition of my knowledge or experience, I hope I can show others a way out, at minimal cost

-------------------------

Leith | 2019-09-20 09:32:25 UTC | #39

At least, I can show them a way ahead, and thats gold, right? Thats not stuff you will learn online - the way ahead. If I see potential students I wish to teach, should I hide this? What is my motivation to hide what I do? I will fix bugs, and teach people what ever the fuck I wish to teach them, unless they don't want to learn, or I am over it, which happens around the day I die.

-------------------------

Modanung | 2019-09-20 09:32:26 UTC | #40

As knowledge is omni-dimensional, peer to peer learning makes a whole lot of sense to me. It's a certainty that any random person knows something you do not and vice versa. Seeing yourself not only as a source but also as a receptacle of knowledge can result in a more equanimous dynamic.

-------------------------

Leith | 2019-09-20 09:34:53 UTC | #41

Absolutely, we are repositories of knowledge, each of us, we all have something to contribute, at least in theory, and we can test it

-------------------------

Leith | 2019-09-20 09:37:40 UTC | #42

I certainly did not to expect to find bugs in the debug side of urho, but here I am offering the solution, if thats not ok, I will gladly fuck off and do something else

-------------------------

Leith | 2019-09-20 09:41:22 UTC | #43

I don't have a lot of free time lately, so anything I offer, should be considered as gold, which I found, in a river, while working unrelated problems

-------------------------

Leith | 2019-09-20 09:43:32 UTC | #44

my true name translates to river mouth, I have not signed an NDA nor other formal waiver, all the information I wish to impart, I could do so on another site, and to the detriment of this community

-------------------------

Modanung | 2019-09-20 10:09:42 UTC | #45

[quote="Leith, post:43, topic:5595"]
I don’t have a lot of free time lately, so anything I offer, should be considered as gold
[/quote]
Then offer it... as a PR.

[quote="Leith, post:44, topic:5595"]
my true name translates to river mouth
[/quote]

In Dutch we have the expression _spraakwaterval_, which translates to speach waterfall. :wink:

-------------------------

Leith | 2019-09-20 10:13:27 UTC | #46

I don't need the nods of my friends who gain from my work, I just need a nice place to offer change, and a place to explain why its needed, and thats enough, while our small space does not offer me all i need, it does offer me students, whose minds are open, and this is more than i need, to remain here, if the students want me here, then no power on earth will stop me helping them, and this is just a place, where we met

-------------------------

TheComet | 2019-09-20 11:29:38 UTC | #47

Can you please not double/triple/quadrouple/shitload post and instead edit your previous message? I don't know why mods aren't saying anything but this is standard procedure on forums. This isn't instant chat.

As to your question about branches: Yes, when you want to add a new feature or fix a bug, you do that on a branch appropriately titled ```feature/myfeature``` or ```bugfix/iss4545``` and submit that as a PR when it is ready to be merged. This is also standard practice. See for example https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

That way, if someone on github has a suggestion concerning your fix, you can continue to commit to that branch without having to submit a new PR and while also being able to work on other stuff.

-------------------------

Leith | 2019-09-20 11:41:19 UTC | #48

I will try not to comment at all. :expressionless: you just reduced my chances of putting anything up for discussion.
If you disagree, say so, if you think I talk too much, you can fuck right off. I mean that. And by the way, what does your bug fix rate look like? I don't know you. What did you fix, and where is your name on the credits?

-------------------------

Leith | 2019-09-20 11:43:54 UTC | #49

You need to understand and remember, this is an open sourced project, any one of us, who was a qualified peer, could run away and use it in any way and not share the changes, yet you guys want to rap me on the knuckles, so it serves me well, to ask you, what fucking right you have to question me

-------------------------

Leith | 2019-09-20 11:44:38 UTC | #50

I am waiting, patiently, for you to explain to me

-------------------------

TheComet | 2019-09-20 12:54:40 UTC | #51

Please don't triple post. Forum rules.

[quote="Leith, post:49, topic:5595, full:true"]
You need to understand and remember, this is an open sourced project, any one of us, who was a qualified peer, could run away and use it in any way and not share the changes, yet you guys want to rap me on the knuckles, so it serves me well, to ask you, what fucking right you have to question me
[/quote]

If you want to make a change to any project (open source, commercial, doesn't matter), of course you're going to get feedback on your code from your peers and/or superiors. And you may have to make adjustments based on that feedback. Do you really think you can write perfect code off the bat and it'll get merged immediately with no discussion?

Urho3D is a collaborative effort and I encourage you to partake in discussion without your superiority complex and ego.

You seem to think you have some kind of power over the project because you are offering up your free time and therefore the Urho3D maintainers owe you, or somehow the community doesn't have a right to ask you questions. Are you being serious right now?

[quote="Leith, post:48, topic:5595"]
I will try not to comment at all. :expressionless: you just reduced my chances of putting anything up for discussion.
If you disagree, say so, if you think I talk too much, you can fuck right off. I mean that. And by the way, what does your bug fix rate look like? I don’t know you. What did you fix, and where is your name on the credits?
[/quote]

I'm not sure why comparing dicks ([a fallacous Argument from Authority](https://en.wikipedia.org/wiki/Argument_from_authority)) matters. If you must know, I am the author of the IK subsystem and have made a few bugfixes here and there. I am familiar with Urho3D's PR workflow and its build system and am therefore in a position to help you in that regard, since it seems you've never used git before and have very little experience in code collaboration.

[quote="Leith, post:20, topic:5595, full:true"]
My bug fixes are accurate. You’re merely setting formalities for sharing of information, and then stepping on it. I do not agree with your process.
[/quote]

[quote="Leith, post:35, topic:5595, full:true"]
I want to see my fixes applied, but sending them to you, would be a waste of time, and the guy in charge of assimilating and merge, is not doing his job
[/quote]

He's not asking you to move mountains, he's asking for a simple PR -- The standard process with which open source projects implement collaboration.

[quote="Leith, post:21, topic:5595, full:true"]
I want to share openly, I am not an annoying idiot, I am a qualified peer, I should have the right to speak.
[/quote]

Why do you think you being a "qualified peer" gives you more authority here?

-------------------------

Pencheff | 2019-09-20 13:54:50 UTC | #52

My mouse scroll is screaming for help. How can every simple thread get so much flooded by this guy and he's still around ? Who told him he's a qualified peer ... you can clearly see inconsistency every 2 adjacent lines of his code. I tried hard following what he says trying to find a good advice or anything useful, instead I get lost in time trying not to lose my mind. Just the first time I commented something back I got flooded with private messages from him.

-------------------------

weitjong | 2019-09-20 13:58:07 UTC | #53

I have just suspended this account forever.

-------------------------

weitjong | 2019-09-20 13:59:40 UTC | #54



-------------------------

Modanung | 2019-09-20 18:22:52 UTC | #55

![Mary](https://upload.wikimedia.org/wikipedia/commons/6/66/Elephantmary.jpg)

https://www.youtube.com/watch?v=iHXsUxFQiJs

-------------------------

