1vanK | 2020-11-10 16:48:06 UTC | #1

At the moment, our engine has a problem that PRs are accepted for a very long time or not at all. The people who made PRs rightly take offense and leave. As an experiment, I propose to create an official fork in which we will accept PRs with little or no checking. And the most successful ones will be transferred to the main stable version. I suspect that this fork will soon turn into a nightmare. In the end, we will at least have a good example of what will happen to the engine if we accept all incoming PRs.

[poll type=regular results=always public=true chartType=bar]
* Yes
* No
[/poll]

EDIT: https://github.com/Urho3D-CE/Urho3D

-------------------------

lebrewer | 2020-11-09 14:17:52 UTC | #2

That's actually a good idea. Like Debian Sid or something. "Urho3D-Experimental".

-------------------------

rku | 2020-11-09 14:28:34 UTC | #3

So idea is a broken version that noone will use because all junk is accepted? I do not see what this will achieve other than waste time of maintainers.

High quality control for PRs is a good thing. Lack of any response is actual problem. Also you should not hesitate to close PRs that have long stalled and have either nothing that useful or no chance to be revived, or both.

-------------------------

1vanK | 2020-11-09 14:33:11 UTC | #4

You complained to me that nobody understood your ideas, so you forked the Engine. Or do you think that only your PRs should be accepted and everyone else is garbage?

-------------------------

rku | 2020-11-09 14:46:24 UTC | #5

Where did i say that? Look at PRs from me. I submitted some garbage as well. So?

-------------------------

1vanK | 2020-11-09 14:47:55 UTC | #6

Your PR is great, the best of all

-------------------------

Eugene | 2020-11-09 14:48:30 UTC | #7

How is having low quality “community edition” related to forks?

Forking is the tool to implement breaking, risky and/or very specialized changes that cannot be merged to master due to this. It’s the primary use case of Urho - to be forked and adjusted instead of being used as is.

I don’t see how it’s related to this particular topic.

-------------------------

1vanK | 2020-11-09 15:06:33 UTC | #8

I added a vote to the first post

-------------------------

Eugene | 2020-11-09 15:22:57 UTC | #9

I have two questions about the subject.

1) Does "official fork" include responsibility of maintainers (I guess it's you, because it's your suggestion) to keep this fork up to date with main repo?

2) Are contributors responsible for PR transferring? I.e. if main repo receives trash PR or vice versa.

-------------------------

1vanK | 2020-11-09 15:31:31 UTC | #10

This is just an experiment. It is unknown how long it will last. And how much activity from contributors will be. At first, until there are big discrepancies, it will be easy to update the fork from the master.

PRs will be merged if no one has made a notes for several days. Silence = agreement.

As for responsibility, I don't understand what you are talking about. Everything happens on a voluntary. For example, are you responsible for something or not?

-------------------------

1vanK | 2020-11-09 15:36:15 UTC | #11

At the very least, we can impose a limitation on reducing functionality, if you contribute, the rest of the things should not stop working.

-------------------------

Eugene | 2020-11-09 15:42:13 UTC | #12

I support this idea.
Moreover, we already have such code in main repo (changes of `CustomGeometry` in [this PR](https://github.com/urho3d/Urho3D/pull/2476/files)).

I mean, these helpers clearly don't belong to this class. These functions don't *need* access to private members of `CustomGeometry`, don't belong to initial API domain of `CustomGeometry` and are not reusable enough to be common helpers.

I think this is exactly the kind of code "communtiy fork" should harbour.

-------------------------

Modanung | 2020-11-09 17:36:22 UTC | #13

Don't create a fork, when you should be branching.

Experiments should be specific. Otherwise you're just starting _another_ [alchemists' guild](http://wiki.lspace.org/mediawiki/Alchemists'_Guild). [:boom:](https://github.com/rokups/rbfx)

Doesn't GitHub have _protected branches_ and _permissions_, like GitLab?

-------------------------

1vanK | 2020-11-09 19:07:16 UTC | #15

Since the control will be minimal, the second variant

-------------------------

1vanK | 2020-11-09 19:15:52 UTC | #17

If some PR is good, we will ask the authors to make it for the main repository.

-------------------------

Modanung | 2020-11-09 21:05:35 UTC | #19

[:scroll::musical_score: ](http://www.mikseri.net/artists/urho/fish-executioner/364603/)
[Details=Fish Executioner]
> Fish Executioner!
Death to be done on this blasphemous day
Fish Executioner!
Face of the dead fish will never go away
[/Details]


-----

[quote="Modanung, post:13, topic:6513"]
Don’t create a fork, when you should be branching.
[...]
[/quote]

-------------------------

1vanK | 2020-11-09 21:10:08 UTC | #20

What are the benefits?

-------------------------

Modanung | 2020-11-09 23:01:59 UTC | #21

Well, I don't know about GitHub... I'm not getting near that corporate botnet.

But on Git*Lab* branches can be marked _protected_. This prevents "force pushing" and only allows _maintainers_ (not _developers_) to push to these branches. By default the _master_ branch is marked as such.

https://docs.gitlab.com/ee/user/permissions.html#project-members-permissions

What's important is that the master branch compiles just fine.

https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell

[![](https://git-scm.com/book/en/v2/images/topic-branches-1.png)](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)

-------------------------

Modanung | 2020-11-09 22:44:07 UTC | #22

There's also plenty of examples of people creating *feature-specific* forks, which is fine. A general "experimental fork" is simply too wide a scope to merge from, keep synced and tidy. It doesn't solve the problem, it only *sounds* nice while splitting the fish in two.

This is not software development, it is fantasy marketing.

-------------------------

Modanung | 2020-11-09 23:30:10 UTC | #23

Developers should not be treated as outsiders, and responsibility should not be confused with status. When a community-driven project is asking for a "community edition", it may be lacking confidence.

Have some faith. [:wine_glass:](https://www.youtube.com/watch?v=l-EdCNjumvI&disable_polymer=true)

-------------------------

evolgames | 2020-11-09 23:56:54 UTC | #25

I don't have any experience with PR or really open-source development at all. But I'm familiar with how it works. This sounds interesting and I think the information gained from either success or a mess would be valuable to regular Urho3d. I won't be doing any developing, but I'll be happy to play around with the end result of the experimentation.

-------------------------

weitjong | 2020-11-10 02:44:43 UTC | #26

There is only one thing I would propose/hope. Hopefully when we cherry-picking the good bits from this new community fork, we don’t have to treat them as third-party, that is when the code are contributed by its original author they already agreed to the same contribution checklist of Urho3D project and to be using MIT license with the same copyright statement.

-------------------------

Modanung | 2020-11-10 06:03:38 UTC | #27

Nevermind, I'll just leave you guys to your dark ritual. [:tropical_fish: :axe:](https://www.youtube-nocookie.com/embed/hQY20gBlqqo)
...and adopt Urho as a patron saint.

-------------------------

weitjong | 2020-11-10 07:41:19 UTC | #28

Anyone has the right to fork in open source project.

-------------------------

1vanK | 2020-11-10 08:11:21 UTC | #29

The fork will have the same license with "Urho3D project" copiright so no consent is required, but of course it's better to add a mention of the transfer

-------------------------

Modanung | 2020-11-10 08:31:27 UTC | #30

I'm not stopping anyone: Go ahead... fulfill the prophecy. :wastebasket: << **α ω**

[![](https://luckeyproductions.nl/images/urhohindi.svg)](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Matsya_avatar.jpg/564px-Matsya_avatar.jpg)

-------------------------

Modanung | 2020-11-10 08:51:39 UTC | #31

https://www.youtube.com/watch?v=HDm2id3xtrE

<sub>Bloody coincidentists.</sub>

-------------------------

1vanK | 2020-11-10 09:59:12 UTC | #32

Is it possible to fork repo to same organization?

-------------------------

1vanK | 2020-11-10 14:03:25 UTC | #33

glebedev and Eugene helped me make the rules. Any notes?

1. It is guaranteed that your PR will be accepted in a week if nobody objects to it or suggests an improvement. No comments means everybody agrees with the PR.
2. Please test your change thoroughly. PR will be accepted quickly probably with only light eyeballing so the PR author is solely responsible for the quality of the change.
3. Most useful changes will be merged to Urho3D master branch. To make this simple, consider squashing the PR into a single commit so it would be easy to cherry-pick it.
4. Please try keep Urho3D code style in your change. You can keep any style in your change but any deviation from Urho3D code style requires additional effort to merge it into master. Engine maintainers may avoid it.
5. You are welcome to make PR to fix a bug or add new feature
5.1. Don’t reduce engine functionality. The only exception would if the feature is outdated, not in use by anyone and blocking your PR.
5.2. Don’t change existing code style. You can clean up, reformat or refactor code you wrote previously. Changing someone else's code may trigger a downward spiral of hatred. Just leave it as is.
5.3. Don’t spend your time on tweaking interface colors, new logo design, etc. It is highly subjective and a matter of opinion. If you want to make a beautiful art work with Urho3D consider making it in a separate repository and paste link to in at https://discourse.urho3d.io/c/showcase/17
6. It would be great if new code will be accessible via scripting languages. You can provide script bindings but you don’t have to.

-------------------------

SirNate0 | 2020-11-10 13:44:40 UTC | #34

I don't think it's possible to fork to the same GitHub account, I think you have to just make a new repo and then push from a local copy. Though it seems you can also import it from GitHub. Either way, it looks like it's not possible to create a PR from the new repository to the old one.

I like the rules. I think I might mention the binding generators in point 6 to emphasize that this is a lot less work now than it used to be. Though I think it's also not necessary to do so.

Also, it may just be the forum's flavor of markdown, but I think if you add a few more spaces before the sub items bullet points in point 5 they may end up indented and appear as more definitive sub items rather than seeming to be at the same level.

-------------------------

1vanK | 2020-11-10 14:02:25 UTC | #35

Spaces don't work, I changed dots to numbers

-------------------------

weitjong | 2020-11-10 14:33:30 UTC | #36

I have been thinking, why not you just do the work on the master branch directly then. You can make a copy of current master branch to another branch and named it "stable" or "main" or what have you. In the past we have kept our master branch as stable as possible, but I don't think it has to be this way. It is a trade-off. However, since I will be taking a long break from this project, I don't have to worry about it. :slight_smile:

-------------------------

Miegamicis | 2020-11-10 15:14:23 UTC | #37

> In the past we have kept our master branch as stable as possible, but I don’t think it has to be this way

~~Maybe that's not a bad idea since newcomers probably won't know about this approach and will keep submitting PR's to master.~~


~~Anyway I think that this is a great idea overall. Master branch should be updated as often as possible even if it means that there are mistakes and/or bugs, releases should be used for marking stable builds.~~

-------------------------

Eugene | 2020-11-10 15:04:15 UTC | #39

[quote="Miegamicis, post:37, topic:6513"]
Anyway I think that this is a great idea overall. Master branch should be updated as often as possible even if it means that there are mistakes and/or bugs, releases should be used for marking stable builds.
[/quote]
I don't understand the goal anymore. Can you elaborate, please?

If you want to merge low-quality untested not-codestyle-conforming PRs (like @1vanK proposed), it cannot be master branch. I don't think I need to argue why master branch is not a trash can. Especially given that we currently have "releases are outdated, use master branch, it's stable" poilcy.

If you want to carefully review and quality-check PRs, I don't see how it's different from current PR policy.

-------------------------

Miegamicis | 2020-11-10 15:13:21 UTC | #40

You're right, I think I ignored a few of the rules that @1vanK proposed. Ignore my previous post as it is not related to the proposal.

-------------------------

weitjong | 2020-11-10 15:22:09 UTC | #41

Looks, it is all the same, whichever repo or branch you want to designate it as stable and which one is unstable. If 1vanK wants it to be in the prime area under "urho3d" org then we need to two of them. One mark as stable and one as unstable. The new relax rules obviously only apply to the unstable branch/repo. I propose to use the existing master branch as the one designated for unstable because that is the branch normally developer assume to be the target of the PR.

-------------------------

weitjong | 2020-11-10 15:58:04 UTC | #43

It is just an idea. If he wants it to be a experimental fork outside then I will not suggest this in the first place. But if he want to make in the "urho3d" org, why not just switch places. You still have the stable branch as we have now, but just name it differently. Think outside the box. Or if you guys cannot wrap your ahead around still, leave the current master branch as it. Just name the new repo/branch as "unstable". Cheers.

-------------------------

weitjong | 2020-11-10 16:09:48 UTC | #45

I think you still miss my point, but that's OK. Just want to make a simple comparison. In Emscripten, they have a branch named "incoming" and another one named "master". Over there, people understood to send PR to the "incoming" branch. We do not have that kind of setup for Urho3D project. But if we do, I would rather have "master" branch as the branch for accepting PR, because I find myself sending PR to non-default branch to be confusing. Of course, if we do this, the formerly known "master" branch will be renamed and maintained separately. So, you don't lose anything in term of stability.

Again, this is non-issue if the experiment is to be carried out outside of the "urho3d" org.

-------------------------

1vanK | 2020-11-10 16:10:10 UTC | #46

Too risky experiment, I think. I just created a second organization for this.

-------------------------

weitjong | 2020-11-10 16:12:17 UTC | #47

No pain no gain :slight_smile: But, it is your call and I respect that.

-------------------------

1vanK | 2020-11-10 16:49:33 UTC | #50

I added a link to the repository in the first post.

-------------------------

urnenfeld | 2020-12-25 15:12:43 UTC | #51

[quote="1vanK, post:50, topic:6513, full:true"]
I added a link to the repository in the first post.
[/quote]

Shouldn't we add some reference, in the website or the README as well?

As it is in a different org, it will be hard to find for other people which are unaware of this thread.

-------------------------

1vanK | 2020-12-25 14:45:28 UTC | #52

There is no problem to send people there who send pull requests that are not suitable for the main repository.

-------------------------

